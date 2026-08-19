#!/usr/bin/env python3
"""Render a social post from its post.toml slide scripts.

    python3 tools/social_build.py social/2026-07-23-620
    python3 tools/social_build.py social/2026-07-23-620 --langs ru,de --only 4x5
    python3 tools/social_build.py social/2026-07-23-620 --all-langs --slide 3

Writes HTML into <dir>/html/<lang>/<fmt>/ and final PNGs into
<dir>/export/<lang>/<fmt>/, plus a contact sheet per language so the result
can actually be looked at before it is published.

Rendering goes through headless Chrome at 2x device scale, then Pillow
downsamples to the exact target size.

Requires Pillow (tools/requirements-check.txt) and Google Chrome or Chromium.
"""

import argparse
import html
import os
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import pathname2url

from PIL import Image

from social_post import (
    LOGO,
    LOGO_MARK,
    REPO_ROOT,
    PostError,
    available_langs,
    badge_path,
    export_dir,
    load_post,
    post_path,
    resolve_media,
)

BRAND_CSS = REPO_ROOT / ".claude" / "skills" / "om-post" / "assets" / "brand.css"

# Canvas sizes. Keys must match the `formats` list in post.toml.
FORMATS = {"4x5": (1080, 1350), "1x1": (1080, 1080), "9x16": (1080, 1920)}

SCALE = 2  # render at 2x, downsample for crisp text
RENDER_TIMEOUT_S = 40
WORKERS = 4

CHROME_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
)


def find_chrome() -> str:
    """Locate a Chrome-family browser, or explain how to point at one."""
    override = os.environ.get("CHROME_BIN")
    if override:
        if not Path(override).is_file():
            raise SystemExit(f"CHROME_BIN is set but not a file: {override}")
        return override
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).is_file():
            return candidate
    for name in ("google-chrome", "chromium", "chromium-browser"):
        found = shutil.which(name)
        if found:
            return found
    raise SystemExit(
        "No Chrome or Chromium found. Install Google Chrome, or set CHROME_BIN "
        "to the browser binary."
    )


def furl(path: Path) -> str:
    """Absolute file:// URL. Chrome hangs on top-level data: URLs, so every
    asset reference must be a real file."""
    return "file://" + pathname2url(str(path.resolve()))


def esc(text) -> str:
    return html.escape(str(text), quote=True)


# --------------------------------------------------------------------------
# slide -> HTML body
# --------------------------------------------------------------------------

# Translated copy runs longer than English — German and Russian by a third —
# so the type scale is shrunk until the slide fits instead of letting the
# bottom of a list run off the canvas. Media is allowed to give up space down
# to MIN_MEDIA of the canvas before the text starts shrinking; a phone that
# bleeds off the bottom edge is doing so deliberately and is measured by the
# space its box was granted, not by how far the image overflows.
AUTOFIT_JS = """
(function () {
  var slide = document.querySelector('.slide');
  var media = slide.querySelector('.media');
  var bleeding = slide.classList.contains('bleed');
  var minMedia = media ? slide.clientHeight * 0.34 : 0;
  // Measured against the real children, never scrollHeight: the watermark is
  // an absolutely positioned ::after hanging 200px below the canvas on every
  // green slide, and scrollHeight counts it as overflow that no amount of
  // shrinking can fix.
  function overflowing() {
    if (media && media.clientHeight < minMedia) return true;
    if (bleeding) return false;
    var box = slide.getBoundingClientRect();
    var style = getComputedStyle(slide);
    var top = box.top + parseFloat(style.paddingTop);
    var bottom = box.bottom - parseFloat(style.paddingBottom);
    var kids = slide.children;
    // A centred slide overflows in both directions at once.
    return (
      kids[kids.length - 1].getBoundingClientRect().bottom > bottom + 1 ||
      kids[0].getBoundingClientRect().top < top - 1
    );
  }
  var fit = 1;
  while (fit > 0.62 && overflowing()) {
    fit -= 0.03;
    slide.style.setProperty('--fit', fit.toFixed(2));
  }
  document.documentElement.setAttribute('data-fit', fit.toFixed(2));
})();
"""


def render_media(post: dict, slide: dict, post_dir: Path) -> str:
    media = slide.get("media")
    if not media:
        return ""
    device = slide.get("device", "phone")
    src = resolve_media(post, post_dir, media)
    return (
        f'<div class="media">'
        f'<img class="device {esc(device)}" src="{furl(src)}" alt="">'
        f"</div>"
    )


def render_footer(slide: dict, index: int, total: int) -> str:
    if slide.get("type") in ("cover", "cta"):
        return ""
    return (
        f'<div class="footer"><img src="{furl(LOGO_MARK)}" alt="">'
        f'<span>organicmaps.app</span>'
        f'<span class="spacer"></span><span>{index}/{total}</span></div>'
    )


def render_slide(post: dict, slide: dict, post_dir: Path, index: int,
                 total: int) -> tuple[str, str]:
    """Return (theme_class, inner_html)."""
    kind = slide.get("type", "feature")
    theme = slide.get("theme") or ("light" if kind == "list" else "green")
    parts = []

    if kind == "cover":
        parts.append(f'<img class="logo" src="{furl(LOGO)}" alt="">')
        if slide.get("kicker"):
            parts.append(f'<div class="kicker">{esc(slide["kicker"])}</div>')
        parts.append(f'<h1 class="title">{esc(slide["title"])}</h1>')
        if slide.get("subtitle"):
            parts.append(f'<p class="body">{esc(slide["subtitle"])}</p>')
        parts.append('<div class="rule"></div>')

    elif kind == "cta":
        parts.append(f'<h1 class="title">{esc(slide["title"])}</h1>')
        if slide.get("body"):
            parts.append(f'<p class="body">{esc(slide["body"])}</p>')
        if slide.get("url"):
            parts.append(f'<div class="url">{esc(slide["url"])}</div>')
        badges = slide.get("badges", [])
        if badges:
            imgs = "".join(
                f'<img src="{furl(badge_path(b))}" alt="">' for b in badges
            )
            parts.append(f'<div class="badges">{imgs}</div>')

    else:  # feature | list
        if slide.get("eyebrow"):
            parts.append(f'<div class="eyebrow">{esc(slide["eyebrow"])}</div>')
        parts.append(f'<h1 class="title">{esc(slide["title"])}</h1>')
        if slide.get("body"):
            parts.append(f'<p class="body">{esc(slide["body"])}</p>')
        if slide.get("items"):
            lis = "".join(f"<li>{esc(i)}</li>" for i in slide["items"])
            parts.append(f'<ul class="items">{lis}</ul>')
        parts.append(render_media(post, slide, post_dir))

    parts.append(render_footer(slide, index, total))
    return theme, "".join(p for p in parts if p)


def layout(slide: dict) -> tuple[str, str]:
    """Portrait mockups bleed off the bottom, landscape ones run full width.

    `bleed` may be false to disable, or a pixel number to override how much of
    the phone is allowed off-canvas — useful when the feature being shown sits
    low in the screenshot.
    """
    device = slide.get("device", "phone") if slide.get("media") else None
    bleed = slide.get("bleed", True)
    if device == "phone" and bleed is not False:
        style = f" style='--bleed:{int(bleed)}px'" if bleed is not True else ""
        return " bleed", style
    if device == "desktop":
        return " wide", ""
    return "", ""


def render_html(post: dict, slide: dict, post_dir: Path, fmt: str, index: int,
                total: int, rtl: bool = False) -> str:
    theme, inner = render_slide(post, slide, post_dir, index, total)
    extra_class, extra_style = layout(slide)
    kind = slide.get("type", "feature") + extra_class
    mark_var = f"url({furl(LOGO_MARK)})"
    direction = " dir='rtl'" if rtl else ""
    return (
        f"<!doctype html><html{direction}><head><meta charset='utf-8'>"
        f"<link rel='stylesheet' href='{furl(BRAND_CSS)}'>"
        f"<style>:root{{--mark-white:{mark_var}}}</style></head>"
        f"<body class='fmt-{fmt} theme-{theme}'>"
        f"<div class='slide {kind}'{extra_style}>{inner}</div>"
        f"<script>{AUTOFIT_JS}</script>"
        "</body></html>"
    )


# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------

def shoot(chrome: str, html_path: Path, png_path: Path, size: tuple[int, int],
          profile: Path) -> None:
    """Chrome writes a valid PNG but never exits, so poll for the file and kill."""
    w, h = size
    png_path.unlink(missing_ok=True)
    cmd = [
        chrome, "--headless", "--disable-gpu", "--no-first-run",
        "--disable-component-update", "--disable-background-networking",
        "--hide-scrollbars", f"--user-data-dir={profile}",
        f"--window-size={w},{h}", f"--force-device-scale-factor={SCALE}",
        f"--screenshot={png_path}", furl(html_path),
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        deadline = time.time() + RENDER_TIMEOUT_S
        stable = 0
        while time.time() < deadline:
            time.sleep(0.4)
            if png_path.exists() and png_path.stat().st_size > 0:
                stable += 1
                if stable >= 3:  # give the write a moment to finish
                    return
    finally:
        proc.kill()
        proc.wait()
    if not (png_path.exists() and png_path.stat().st_size):
        raise SystemExit(f"chrome produced no screenshot for {html_path}")


def finalize(png_path: Path, size: tuple[int, int]) -> None:
    """Downsample the 2x render to the exact target size and sanity-check it."""
    with Image.open(png_path) as im:
        im = im.convert("RGB")
        if im.size != size:
            im = im.resize(size, Image.LANCZOS)
        extrema = im.getextrema()
        if all(lo == hi for lo, hi in extrema):
            raise SystemExit(
                f"{png_path.name} rendered as a flat frame — check the HTML"
            )
        im.save(png_path, "PNG", optimize=True)
    with Image.open(png_path) as im:
        assert im.size == size, f"{png_path}: {im.size} != {size}"


def contact_sheet(pngs: list[Path], out: Path, columns: int = 4) -> None:
    """One image of every slide, for the review pass.

    Building a post and looking at nothing is how a cropped feature or an
    orphaned word reaches a channel, so this is written by default.
    """
    if not pngs:
        return
    cell_w = 320
    thumbs = []
    for path in pngs:
        with Image.open(path) as im:
            ratio = im.height / im.width
            thumbs.append(
                im.convert("RGB").resize(
                    (cell_w, round(cell_w * ratio)), Image.LANCZOS
                )
            )
    gap = 12
    cell_h = max(t.height for t in thumbs)
    rows = (len(thumbs) + columns - 1) // columns
    sheet = Image.new(
        "RGB",
        (columns * (cell_w + gap) + gap, rows * (cell_h + gap) + gap),
        (232, 232, 232),
    )
    for i, thumb in enumerate(thumbs):
        x = gap + (i % columns) * (cell_w + gap)
        y = gap + (i // columns) * (cell_h + gap)
        sheet.paste(thumb, (x, y))
    sheet.save(out, "PNG", optimize=True)


# --------------------------------------------------------------------------

# Right-to-left languages, matching templates/base.html.
RTL_LANGS = {"ar", "fa-IR", "he"}


def build(post_dir: Path, langs: list[str], only_format: str | None,
          only_slide: int | None, sheet: bool) -> list[Path]:
    """Render every requested language × format × slide. Returns the PNGs."""
    chrome = find_chrome()
    if not BRAND_CSS.is_file():
        raise SystemExit(f"missing stylesheet: {BRAND_CSS}")

    jobs: list[tuple[Path, Path, tuple[int, int]]] = []
    sheets: list[tuple[Path, list[Path]]] = []

    for lang in langs:
        source = post_path(post_dir, lang)
        if not source.is_file():
            raise SystemExit(f"no slide script for {lang}: {source}")
        post = load_post(source)
        slides = post["slides"]
        formats = [only_format] if only_format else post.get("formats", ["4x5"])
        for fmt in formats:
            if fmt not in FORMATS:
                raise SystemExit(
                    f"unknown format {fmt!r}; known: {', '.join(FORMATS)}"
                )
            html_dir = post_dir / "html" / lang / fmt
            out_dir = export_dir(post_dir, lang, fmt)
            html_dir.mkdir(parents=True, exist_ok=True)
            out_dir.mkdir(parents=True, exist_ok=True)

            produced: list[Path] = []
            for i, slide in enumerate(slides, start=1):
                if only_slide and i != only_slide:
                    continue
                name = f"{i:02d}-{slide.get('type', 'feature')}"
                html_path = html_dir / f"{name}.html"
                html_path.write_text(
                    render_html(post, slide, post_dir, fmt, i, len(slides),
                                rtl=lang in RTL_LANGS),
                    encoding="utf-8",
                )
                png_path = out_dir / f"{name}.png"
                jobs.append((html_path, png_path, FORMATS[fmt]))
                produced.append(png_path)
            if sheet and not only_slide:
                sheets.append((post_dir / "export" / lang / f"sheet-{fmt}.png",
                               produced))

    profiles = post_dir / ".cache" / "chrome-profile"
    shutil.rmtree(profiles, ignore_errors=True)

    print(f"rendering {len(jobs)} image(s)…")

    def run(job) -> None:
        html_path, png_path, size = job
        # One profile per thread, not per job: two Chrome processes sharing a
        # --user-data-dir means the second one exits without rendering, and
        # nothing dispatches job N to the thread that ran job N-WORKERS.
        profile = profiles / threading.current_thread().name
        shoot(chrome, html_path, png_path, size, profile)
        finalize(png_path, size)
        print(f"  ✓ {png_path.relative_to(post_dir)}")

    with ThreadPoolExecutor(WORKERS) as pool:
        list(pool.map(run, jobs))

    shutil.rmtree(profiles, ignore_errors=True)

    for out, pngs in sheets:
        contact_sheet([p for p in pngs if p.is_file()], out)
        print(f"  ✓ {out.relative_to(post_dir)}  (contact sheet)")

    return [png for _, png, _ in jobs]


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("post_dir", type=Path, help="folder holding post.toml")
    ap.add_argument("--langs", help="comma-separated language codes")
    ap.add_argument("--all-langs", action="store_true",
                    help="every language this post has a post.<lang>.toml for")
    ap.add_argument("--only", help="render a single format, e.g. 4x5")
    ap.add_argument("--slide", type=int, help="render a single slide (1-based)")
    ap.add_argument("--no-sheet", action="store_true",
                    help="skip the per-language contact sheet")
    args = ap.parse_args()

    post_dir = args.post_dir.resolve()
    if not post_dir.is_dir():
        raise SystemExit(f"not a directory: {post_dir}")

    if args.langs:
        langs = [s.strip() for s in args.langs.split(",") if s.strip()]
    elif args.all_langs:
        langs = available_langs(post_dir)
    else:
        langs = ["en"]
    if not langs:
        raise SystemExit(f"no post.toml found in {post_dir}")

    try:
        build(post_dir, langs, args.only, args.slide, sheet=not args.no_sheet)
    except PostError as e:
        raise SystemExit(f"Error: {e}") from e

    print(f"done → {post_dir / 'export'}")


if __name__ == "__main__":
    main()
