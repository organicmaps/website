#!/usr/bin/env python3
"""The `post.toml` slide script: reading it, writing it, and finding its files.

A social post lives in `social/<release>/` and is described by one `post.toml`
per language — `post.toml` is English, `post.ru.toml` its Russian translation.
`social_build.py` renders them, `social_translate.py` produces them and
`telegram_post_all.py` picks the rendered images up per channel.

This module holds everything the three have to agree on: the schema, which
fields are prose and which are identifiers, where a slide's screenshot comes
from, and how a news folder maps to its social folder.
"""

import re
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent  # tools/ sits below it
SOCIAL_ROOT = REPO_ROOT / "social"

# Brand assets, taken from the site itself rather than copied — a second copy
# would drift away from the one the website actually serves.
LOGO = REPO_ROOT / "static" / "logos" / "white-on-green.svg"
LOGO_MARK = REPO_ROOT / "static" / "logos" / "white-on-transparent.svg"
BADGE_DIR = REPO_ROOT / "static" / "images" / "badges"

# Store badges are named after their file in static/images/badges/. These
# aliases accept the names the organicmaps repo's version of this pipeline
# uses, so a post.toml can be moved between the two repos unchanged.
BADGE_ALIASES = {
    "google-play": "googleplay",
    "play": "googleplay",
    "fdroid": "f-droid",
    "appstore": "apple-appstore",
    "apple": "apple-appstore",
    "appgallery": "huawei-appgallery",
    "huawei": "huawei-appgallery",
}

SLIDE_TYPES = ("cover", "feature", "list", "cta")
THEMES = ("green", "blue", "light", "dark")
# "phone" is the generic frame; iphone/android add the platform's own corner
# radius, rim and side buttons. A plain "phone" on a slide whose eyebrow names
# a platform is upgraded to it at render time.
DEVICES = ("phone", "iphone", "android", "desktop", "plain")

# Prose. Everything else in a slide is an identifier: a file path, a theme
# name, a badge name, a pixel count or the short URL — none of which survive
# being translated.
TEXT_FIELDS = ("kicker", "title", "subtitle", "eyebrow", "body")
LIST_FIELDS = ("items",)

# The order keys are written back out in, so a translated post.toml diffs
# cleanly against its English source.
SLIDE_KEY_ORDER = (
    "type", "kicker", "eyebrow", "title", "subtitle", "body", "items",
    "media", "device", "theme", "bleed", "url", "badges",
)
TOP_KEY_ORDER = ("release", "source", "lang", "formats")


class PostError(Exception):
    """A post.toml that cannot be rendered as written."""


# ----------------------------------------------------------------- reading

def load_post(path: Path) -> dict:
    """Parse and validate a post.toml."""
    try:
        post = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as e:
        raise PostError(f"{path}: {e}") from e

    slides = post.get("slides")
    if not slides:
        raise PostError(f"{path}: no [[slides]]")

    for i, slide in enumerate(slides, start=1):
        kind = slide.get("type", "feature")
        if kind not in SLIDE_TYPES:
            raise PostError(
                f"{path}: slide {i} has type {kind!r}; "
                f"known: {', '.join(SLIDE_TYPES)}"
            )
        if not str(slide.get("title", "")).strip():
            raise PostError(f"{path}: slide {i} ({kind}) has no title")
        theme = slide.get("theme")
        if theme is not None and theme not in THEMES:
            raise PostError(
                f"{path}: slide {i} has theme {theme!r}; "
                f"known: {', '.join(THEMES)}"
            )
        device = slide.get("device")
        if device is not None and device not in DEVICES:
            raise PostError(
                f"{path}: slide {i} has device {device!r}; "
                f"known: {', '.join(DEVICES)}"
            )
        for badge in slide.get("badges", []):
            badge_path(badge)  # raises PostError on an unknown badge
    return post


def badge_path(name: str) -> Path:
    """Resolve a badge name to its SVG in static/images/badges/."""
    stem = BADGE_ALIASES.get(name, name)
    path = BADGE_DIR / f"{stem}.svg"
    if not path.is_file():
        known = sorted(p.stem for p in BADGE_DIR.glob("*.svg"))
        raise PostError(f"unknown badge {name!r}; available: {', '.join(known)}")
    return path


def resolve_media(post: dict, post_dir: Path, media: str) -> Path:
    """Find a slide's screenshot.

    Looked for next to post.toml first, then under the post's `source` folder
    (the news post the screenshots already live in), then from the repo root.
    That way a slide can say `media = "Barriers on a route.jpg"` and pick up
    the file the website already ships, without a copy or a ../../.. path.
    """
    candidates = [post_dir / media]
    source = post.get("source")
    if source:
        candidates.append(REPO_ROOT / source / media)
    candidates.append(REPO_ROOT / media)

    for candidate in candidates:
        if candidate.is_file():
            return candidate
    tried = "\n  ".join(str(c) for c in candidates)
    raise PostError(f"missing media {media!r}; looked in:\n  {tried}")


# ----------------------------------------------------------------- writing

def _toml_string(value: str) -> str:
    escaped = (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\t", "\\t")
    )
    return f'"{escaped}"'


def _toml_value(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return _toml_string(value)
    if isinstance(value, list):
        if not value:
            return "[]"
        rendered = [_toml_value(v) for v in value]
        inline = "[" + ", ".join(rendered) + "]"
        if len(inline) <= 72:  # formats = ["4x5"] stays on one line
            return inline
        return "[\n" + "".join(f"    {r},\n" for r in rendered) + "]"
    raise PostError(f"cannot write {type(value).__name__} to TOML: {value!r}")


def _ordered(keys, order) -> list:
    """Known keys in canonical order, then anything unexpected, alphabetically."""
    known = [k for k in order if k in keys]
    return known + sorted(k for k in keys if k not in order)


def dump_post(post: dict) -> str:
    """Serialize a post back to TOML.

    Written by hand rather than with a library: the schema is small, and the
    output has to stay diffable against the English source it was translated
    from — a generic dumper reorders and requotes everything.
    """
    lines = []
    for key in _ordered(post.keys(), TOP_KEY_ORDER):
        if key == "slides":
            continue
        lines.append(f"{key} = {_toml_value(post[key])}")

    for slide in post["slides"]:
        lines.append("")
        lines.append("[[slides]]")
        for key in _ordered(slide.keys(), SLIDE_KEY_ORDER):
            lines.append(f"{key} = {_toml_value(slide[key])}")

    return "\n".join(lines) + "\n"


def text_fields(slide: dict) -> list[tuple[str, int | None, str]]:
    """Every translatable string in a slide, as (key, index, value).

    `index` is None for a plain string field and the position in the list for
    an item of `items`.
    """
    found: list[tuple[str, int | None, str]] = []
    for key in TEXT_FIELDS:
        value = slide.get(key)
        if isinstance(value, str) and value.strip():
            found.append((key, None, value))
    for key in LIST_FIELDS:
        for i, value in enumerate(slide.get(key, [])):
            if isinstance(value, str) and value.strip():
                found.append((key, i, value))
    return found


def set_field(slide: dict, key: str, index: int | None, value: str) -> None:
    if index is None:
        slide[key] = value
    else:
        slide[key][index] = value


# -------------------------------------------------------------- file layout

def post_path(post_dir: Path, lang: str) -> Path:
    """post.toml for English, post.<lang>.toml for everything else."""
    return post_dir / ("post.toml" if lang == "en" else f"post.{lang}.toml")


def available_langs(post_dir: Path) -> list[str]:
    """Languages this post has a slide script for, English first."""
    langs = ["en"] if (post_dir / "post.toml").is_file() else []
    for path in sorted(post_dir.glob("post.*.toml")):
        m = re.fullmatch(r"post\.([A-Za-z-]+)\.toml", path.name)
        if m:
            langs.append(m.group(1))
    return langs


def export_dir(post_dir: Path, lang: str, fmt: str) -> Path:
    return post_dir / "export" / lang / fmt


def social_dir_for(folder: Path) -> Path:
    """The social folder belonging to a news folder.

    content/news/2026-07-23/620  ->  social/2026-07-23-620
    Anything outside content/news keeps its own folder name.
    """
    folder = folder.resolve()
    news_root = (REPO_ROOT / "content" / "news").resolve()
    try:
        parts = folder.relative_to(news_root).parts
    except ValueError:
        return SOCIAL_ROOT / folder.name
    return SOCIAL_ROOT / "-".join(parts)
