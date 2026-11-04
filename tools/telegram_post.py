#!/usr/bin/env python3
"""
Publish formatted markdown text with optional images, videos, or audio to a
Telegram group.

Usage:
    python3 tools/telegram_post.py --group "@my_group" --text post.md [--media img1.jpg video.mp4 ...]

Environment:
    TELEGRAM_BOT_TOKEN - your bot token from @BotFather

The script will:
  1. Read the markdown file and split into chunks of <=4096 chars (at paragraph boundaries).
  2. Send each chunk as a separate message with MarkdownV2 formatting.
  3. If media files are provided, send them as a media group immediately after.

With --rich the post goes out instead as a single Bot API rich message: real
headings, lists and tables, media inside the post, and a 32768-character limit,
so nothing is escaped or split.
"""

import argparse
import json
import mimetypes
import os
import re
import subprocess
import sys
import tempfile
from collections.abc import Sequence
from pathlib import Path

import requests

from markdown_frontmatter import strip_frontmatter
from markdown_xml import find_balanced_close

BASE_URL = "https://api.telegram.org/bot{token}"


def get_token() -> str:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: set TELEGRAM_BOT_TOKEN environment variable.", file=sys.stderr)
        sys.exit(1)
    return token


SPECIAL_CHARS = set(r"_*[]()~`>#+-=|{}.!")


_TERA_BLOCK_RE = re.compile(r"\{\{.*?\}\}", re.DOTALL)


def strip_tera_blocks(text: str) -> str:
    """Remove Tera expressions and component calls before Telegram rendering."""
    return _TERA_BLOCK_RE.sub("", text)


BUILTIN_REFERENCES: dict[str, tuple[str, str]] = {
    "fdroid": ("https://f-droid.org/packages/app.organicmaps/", "F-Droid"),
    "googleplay": (
        "https://play.google.com/store/apps/details?id=app.organicmaps",
        "Google Play",
    ),
    "appgallery": (
        "https://appgallery.huawei.com/#/app/C104325611",
        "AppGallery",
    ),
    "appstore": (
        "https://apps.apple.com/app/organic-maps/id1567437057",
        "App Store",
    ),
    "obtainium": (
        "https://apps.obtainium.imranr.dev/redirect?r=obtainium://app/%7B%22id%22%3A%22app.organicmaps%22%2C%22url%22%3A%22https%3A%2F%2Fgithub.com%2Forganicmaps%2Forganicmaps%22%7D",
        "Obtainium",
    ),
    "accrescent": (
        "https://accrescent.app/app/app.organicmaps",
        "Accrescent",
    ),
    "testflight": (
        "https://testflight.apple.com/join/lrKCl08I",
        "TestFlight",
    ),
    "firebase": (
        "https://appdistribution.firebase.dev/i/2f0fee463107b137",
        "Firebase",
    ),
}


def load_references(site_root: Path) -> dict[str, tuple[str, str]]:
    """
    Load markdown reference definitions from templates/shortcodes/references.md
    relative to the script directory, merged with built-in references.

    File definitions take precedence over built-ins.
    Returns a dict mapping lowercase id → (url, title).
    Each line should look like: [id]: https://example.com "Optional Title"
    """
    refs: dict[str, tuple[str, str]] = dict(BUILTIN_REFERENCES)

    ref_path = site_root / "templates" / "shortcodes" / "references.md"
    if not ref_path.is_file():
        return refs

    pattern = re.compile(
        r"^\[([^\]]+)\]:\s+"  # [id]:
        r"<?(\S+?)>?"  # URL (optionally wrapped in <>)
        r'(?:\s+["\(](.+?)["\)])?'  # optional "title" or (title)
        r"\s*$"
    )
    for line in ref_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = pattern.match(line)
        if m:
            ref_id = m.group(1).lower()
            url = m.group(2)
            title = m.group(3) or ""
            refs[ref_id] = (url, title)

    return refs


def resolve_references(text: str, refs: dict[str, tuple[str, str]]) -> str:
    """
    Replace markdown reference-style links with inline links.

    Handles:
      [text][id]  → [text](url "title")
      [id][]      → [id](url "title")

    Also collects any reference definitions from the text itself and strips them.
    """
    if not refs:
        # Still need to check for inline definitions even without a refs file
        refs = {}

    # Collect inline reference definitions from the text itself
    def_pattern = re.compile(
        r"^\[([^\]]+)\]:\s+" r"<?(\S+?)>?" r'(?:\s+["\(](.+?)["\)])?\s*$',
        re.MULTILINE,
    )
    for m in def_pattern.finditer(text):
        ref_id = m.group(1).lower()
        if ref_id not in refs:
            url = m.group(2)
            title = m.group(3) or ""
            refs[ref_id] = (url, title)

    # Remove inline reference definitions from text
    text = def_pattern.sub("", text)

    if not refs:
        return text

    # Replace [text][id] full references
    def repl_full(m: re.Match) -> str:
        link_text = m.group(1)
        ref_id = m.group(2).lower()
        if ref_id in refs:
            url, _title = refs[ref_id]
            return f"[{link_text}]({url})"
        return m.group(0)  # leave unresolved as-is

    text = re.sub(r"\[([^\]]+)\]\[([^\]]+)\]", repl_full, text)

    # Replace [id][] collapsed references
    def repl_collapsed(m: re.Match) -> str:
        ref_id = m.group(1).lower()
        if ref_id in refs:
            url, _title = refs[ref_id]
            return f"[{m.group(1)}]({url})"
        return m.group(0)

    text = re.sub(r"\[([^\]]+)\]\[\]", repl_collapsed, text)

    # Clean up blank lines left by removed definitions
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


def load_base_url(site_root: Path) -> str:
    """Read the site's base_url from config.toml. Falls back to organicmaps.app."""
    config_path = site_root / "config.toml"
    if config_path.is_file():
        for line in config_path.read_text(encoding="utf-8").splitlines():
            m = re.match(r'^\s*base_url\s*=\s*"([^"]+)"\s*$', line)
            if m:
                return m.group(1).rstrip("/")
    return "https://organicmaps.app"


# Matches Zola internal references: @/path/index.md or @/path/index.LANG.md
ZOLA_REF_RE = re.compile(r"@/([^)\s]+?\.md)")
# Captures optional language code from a Zola filename like "index.ru.md",
# "index.fa-IR.md" or "index.zh-Hans.md" (script subtags are 4 letters).
ZOLA_FILENAME_RE = re.compile(
    r"^(?P<stem>.+?)(?:\.(?P<lang>[a-z]{2,3}(?:-[A-Za-z]{2,4})?))?\.md$"
)


def _zola_target_url(
    target: str, site_root: Path, base_url: str
) -> str | None:
    """
    Resolve a Zola @/-style path like "donate/index.ru.md" to a site URL.

    Reads the target file's frontmatter to honor a `slug` override and
    prepends the language code as a URL prefix for non-default languages.
    Returns None if the file can't be found.
    """
    target = target.lstrip("/")
    file_path = site_root / "content" / target

    parts = target.split("/")
    if not parts:
        return None
    filename = parts[-1]
    m = ZOLA_FILENAME_RE.match(filename)
    if not m:
        return None
    stem = m.group("stem")
    lang = m.group("lang") or ""
    dir_parts = parts[:-1]

    if not file_path.is_file():
        return None

    slug: str | None = None
    try:
        _, meta = strip_frontmatter(file_path.read_text(encoding="utf-8"))
        raw_slug = meta.get("slug")
        if isinstance(raw_slug, str) and raw_slug.strip():
            slug = raw_slug.strip()
    except OSError:
        pass

    # Determine the trailing path segment:
    # - If the file is an _index.* (section) or index.* (page), the URL is the directory.
    # - A page file with stem other than "index" appends its stem (rare in this repo).
    if stem in ("index", "_index"):
        url_parts = list(dir_parts)
    else:
        url_parts = list(dir_parts) + [stem]

    # Apply slug override (replaces the last URL segment, which is the folder name).
    if slug and url_parts:
        url_parts[-1] = slug

    path = "/".join(url_parts)
    prefix = f"/{lang}" if lang else ""
    url = f"{base_url}{prefix}/{path}/" if path else f"{base_url}{prefix}/"
    return url


def resolve_zola_references(
    text: str, site_root: Path, base_url: str
) -> tuple[str, list[str]]:
    """
    Replace Zola @/-style internal references like
        [text](@/donate/index.ru.md)
    with absolute site URLs. Returns (new_text, unresolved_targets).
    """
    unresolved: list[str] = []

    def repl(m: re.Match) -> str:
        target = m.group(1)
        url = _zola_target_url(target, site_root, base_url)
        if url is None:
            unresolved.append(target)
            return m.group(0)
        return url

    new_text = ZOLA_REF_RE.sub(repl, text)
    return new_text, unresolved


def find_unresolved_references(text: str) -> list[tuple[str, str, int]]:
    """
    Find any remaining reference-style links that were not resolved.
    Returns list of (match_text, ref_id, line_number).
    """
    unresolved: list[tuple[str, str, int]] = []
    lines = text.splitlines()
    for lineno, line in enumerate(lines, 1):
        # [text][id]
        for m in re.finditer(r"\[([^\]]+)\]\[([^\]]+)\]", line):
            unresolved.append((m.group(0), m.group(2), lineno))
        # [id][]
        for m in re.finditer(r"\[([^\]]+)\]\[\]", line):
            unresolved.append((m.group(0), m.group(1), lineno))
    return unresolved


# Markdown files here are rendered by Zola, which passes raw HTML through, so
# a page can carry a tag that means nothing to Telegram. MarkdownV2 has no HTML
# at all: an unhandled tag is escaped and shown to readers verbatim, which is
# how a literal "<br/>" reached the channels in the 2026-08-31 release post.
BR_RE = re.compile(r"[ \t]*<br\s*/?>[ \t]*\n?", re.IGNORECASE)

# A fenced block or an inline span. Code is content, not markup: neither the
# <br> rewrite nor the tag report may touch what is inside one.
CODE_PATTERN = r"```[\s\S]*?```|`[^`\n]+`"
CODE_RE = re.compile(CODE_PATTERN)


def blank_code(text: str) -> str:
    """Blank out code, keeping every newline so line numbers still line up."""
    return CODE_RE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)

# Anything tag-shaped that is not an autolink: "<https://…>" has no space or
# ">" before its colon, so it never matches.
HTML_TAG_RE = re.compile(r"</?(?P<name>[A-Za-z][A-Za-z0-9-]*)(?:\s[^<>]*)?/?>")

# Tags the Rich HTML style parses. A rich message may carry these; anything
# else is still worth reporting, since unsupported markup is dropped silently.
RICH_HTML_TAGS = frozenset(
    """a aside audio b blockquote cite code del details em figcaption figure
    footer h1 h2 h3 h4 h5 h6 hr i img input ins li mark ol p pre s strike
    strong sub summary sup table td tg-button tg-button-row tg-collage
    tg-document tg-emoji tg-map tg-math tg-math-block tg-reference
    tg-slideshow tg-spoiler tg-thinking tg-time th tr u ul video""".split()
)


def find_raw_html(text: str, rich: bool = False) -> list[tuple[str, int]]:
    """Find HTML tags Telegram cannot render. Returns (tag, line_number).

    Runs on the source markdown, so it reports what an editor wrote rather
    than what the converter made of it. Tags inside code are content and are
    never reported; nor is <br>, which both send paths turn into a line
    break. In rich mode the tags Telegram's Rich HTML style parses are
    excluded too.
    """
    found: list[tuple[str, int]] = []
    for lineno, line in enumerate(blank_code(text).splitlines(), 1):
        for m in HTML_TAG_RE.finditer(line):
            name = m.group("name").lower()
            if name == "br" or (rich and name in RICH_HTML_TAGS):
                continue
            found.append((m.group(0), lineno))
    return found


def utf16_len(text: str) -> int:
    """
    Count UTF-16 code units — this is how Telegram measures message length.
    BMP characters (U+0000–U+FFFF) = 1 unit, supplementary = 2 units.
    """
    return sum(2 if ord(ch) > 0xFFFF else 1 for ch in text)


def visible_text(formatted: str) -> str:
    """
    Extract the visible/rendered text from a MarkdownV2 string by stripping
    formatting markers and escape backslashes.
    """
    stash: list[str] = []

    def keep(value: str) -> str:
        stash.append(value)
        return f"\x00V{len(stash) - 1}\x00"

    # Code contents are visible but their punctuation is not formatting.
    s = re.sub(r"```\w*\n?([\s\S]*?)```", lambda m: keep(m.group(1)), formatted)
    s = re.sub(r"`([^`]+)`", lambda m: keep(m.group(1)), s)
    # Remove balanced link markup [text](url) → text.
    s = _replace_inline_links(
        s, lambda label, _target: label, telegram_targets=True
    )
    # Preserve escaped MarkdownV2 characters before stripping real markers.
    s = re.sub(r"\\(.)", lambda m: keep(m.group(1)), s)
    # Remove formatting pairs: * _ ~ ||
    s = re.sub(r"\|\|", "", s)
    for ch in "*_~":
        s = s.replace(ch, "")
    for index, value in enumerate(stash):
        s = s.replace(f"\x00V{index}\x00", value)
    return s


def plain_text_fallback(formatted: str) -> str:
    """Downgrade a MarkdownV2 string to readable plain text.

    Like visible_text(), but keeps link targets — "[label](url)" becomes
    "label (url)" instead of just "label", so a formatting failure never
    silently drops the URLs a post exists to share.

    URLs are stashed before the formatting markers are stripped: visible_text()
    deletes every '*', '_' and '~' it sees, which would quietly turn
    "example.com/a_b" into "example.com/ab". That is tolerable when only
    measuring length, but not in text that actually gets sent.
    """
    stash: list[str] = []

    def keep(url: str) -> str:
        stash.append(re.sub(r"\\(.)", r"\1", url))  # undo MarkdownV2 escaping
        return f"\x00U{len(stash) - 1}\x00"

    # Inline links "[label](url)" → "label (url)", target preserved verbatim.
    s = _replace_inline_links(
        formatted,
        lambda label, target: f"{label} ({keep(target)})",
        telegram_targets=True,
    )
    # Bare URLs left in the text.
    s = re.sub(r"https?://\S+", lambda m: keep(m.group(0)), s)

    s = visible_text(s)

    for i, url in enumerate(stash):
        s = s.replace(f"\x00U{i}\x00", url)
    return s


def escape_chars(text: str) -> str:
    """Escape all MarkdownV2 special characters in plain text."""
    return "".join(f"\\{ch}" if ch in SPECIAL_CHARS else ch for ch in text)


def _escaped_at(text: str, index: int) -> bool:
    backslashes = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        backslashes += 1
        index -= 1
    return backslashes % 2 == 1


def _find_unescaped_close(text: str, start: int, delimiter: str) -> int:
    """Return the first unescaped delimiter at or after ``start``."""
    index = start
    while index < len(text):
        if text[index] == delimiter and not _escaped_at(text, index):
            return index
        index += 1
    return -1


def _replace_inline_links(text: str, replace, telegram_targets: bool = False) -> str:
    """Replace inline Markdown links without truncating parenthesized targets.

    Standard Markdown balances parentheses in destinations. Telegram
    MarkdownV2 instead escapes every destination ``)`` and leaves only the
    entity-closing parenthesis unescaped, so its converted links need a
    different closing-delimiter scan.
    """
    out: list[str] = []
    copied = 0
    search = 0
    while True:
        start = text.find("[", search)
        if start < 0:
            break
        if _escaped_at(text, start) or (start > 0 and text[start - 1] == "!"):
            search = start + 1
            continue
        label_end = find_balanced_close(text, start, "[", "]")
        if label_end < 0 or label_end + 1 >= len(text) or text[label_end + 1] != "(":
            search = start + 1
            continue
        if telegram_targets:
            target_end = _find_unescaped_close(text, label_end + 2, ")")
        else:
            target_end = find_balanced_close(text, label_end + 1, "(", ")")
        if target_end < 0:
            search = start + 1
            continue
        out.append(text[copied:start])
        out.append(replace(text[start + 1:label_end], text[label_end + 2:target_end]))
        copied = target_end + 1
        search = copied
    out.append(text[copied:])
    return "".join(out)


def convert_markdown_to_telegramv2(text: str) -> str:
    """
    Convert standard Markdown to Telegram MarkdownV2.

    Handles: **bold** → *bold*, *italic*/_italic_ → _italic_,
    ~~strike~~ → ~strike~, `code`, ```pre```, [link](url),
    # headings → *bold*, - lists → • bullets.
    Special characters in plain text are escaped.
    """
    placeholders: list[tuple[str, str]] = []

    def ph(telegram_text: str) -> str:
        token = f"\x00PH{len(placeholders)}\x00"
        placeholders.append((token, telegram_text))
        return token

    # --- Code blocks (preserve content verbatim, no inner escaping) ---
    def repl_codeblock(m: re.Match) -> str:
        lang = m.group(1) or ""
        code = m.group(2)
        return ph(f"```{lang}\n{code}```")

    text = re.sub(r"```(\w*)\n?([\s\S]*?)```", repl_codeblock, text)

    # --- Inline code (no inner escaping) ---
    def repl_code(m: re.Match) -> str:
        return ph(f"`{m.group(1)}`")

    text = re.sub(r"`([^`]+)`", repl_code, text)

    # --- Line breaks: <br>, <br/>, <br /> → newline (Zola renders these; a
    #     literal tag would otherwise be escaped and shown to readers). A tag
    #     that already ends its line consumes that newline instead of adding
    #     a second one, so a soft break does not become a paragraph break. ---
    text = BR_RE.sub("\n", text)

    # --- Links [text](url) — strip optional "title" since Telegram
    #     MarkdownV2 does not support link titles ---
    def repl_link(link_label: str, raw_url: str) -> str:
        link_text = escape_chars(link_label)
        # Remove trailing  "title" or 'title' from URL
        url = re.sub(r"""\s+["'].*["']\s*$""", "", raw_url)
        url = url.replace("\\", "\\\\").replace(")", "\\)")
        return ph(f"[{link_text}]({url})")

    text = _replace_inline_links(text, repl_link)

    # --- Bold+Italic ***text*** → *_text_* ---
    def repl_bold_italic(m: re.Match) -> str:
        inner = escape_chars(m.group(1))
        return ph(f"*_{inner}_*")

    text = re.sub(r"\*\*\*(.+?)\*\*\*", repl_bold_italic, text)

    # --- Bold **text** → *text* ---
    def repl_bold(m: re.Match) -> str:
        inner = escape_chars(m.group(1))
        return ph(f"*{inner}*")

    text = re.sub(r"\*\*(.+?)\*\*", repl_bold, text)

    # --- Strikethrough ~~text~~ → ~text~ ---
    def repl_strike(m: re.Match) -> str:
        inner = escape_chars(m.group(1))
        return ph(f"~{inner}~")

    text = re.sub(r"~~(.+?)~~", repl_strike, text)

    # --- Italic *text* or _text_ → _text_ ---
    def repl_italic_star(m: re.Match) -> str:
        inner = escape_chars(m.group(1))
        return ph(f"_{inner}_")

    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", repl_italic_star, text)

    def repl_italic_under(m: re.Match) -> str:
        inner = escape_chars(m.group(1))
        return ph(f"_{inner}_")

    text = re.sub(r"(?<!_)_(?!_)(.+?)(?<!_)_(?!_)", repl_italic_under, text)

    # --- Headings: # Heading → *Heading* (bold) ---
    def repl_heading(m: re.Match) -> str:
        inner = escape_chars(m.group(2).strip())
        return ph(f"*{inner}*")

    text = re.sub(r"^(#{1,6})\s+(.+)$", repl_heading, text, flags=re.MULTILINE)

    # --- Bullet lists: - item or * item → • item ---
    text = re.sub(r"^[\-\*]\s+", "• ", text, flags=re.MULTILINE)

    # --- Numbered lists: 1. item → 1) item (escape the dot) ---
    text = re.sub(r"^(\d+)\.\s+", r"\1\) ", text, flags=re.MULTILINE)

    # --- Horizontal rules ---
    text = re.sub(r"^-{3,}$", "———", text, flags=re.MULTILINE)

    # --- Escape remaining plain text, restore placeholders ---
    result = []
    for part in re.split(r"(\x00PH\d+\x00)", text):
        if part.startswith("\x00PH") and part.endswith("\x00"):
            for token, telegram_text in placeholders:
                if token == part:
                    result.append(telegram_text)
                    break
        else:
            result.append(escape_chars(part))

    return "".join(result)


def _contains_unescaped_markup(text: str) -> bool:
    index = 0
    while index < len(text):
        if text[index] == "\\" and index + 1 < len(text):
            index += 2
            continue
        if text[index] in "*_~`[|":
            return True
        index += 1
    return False


def _hard_split_markdownv2_line(line: str, max_len: int) -> list[str]:
    """Split one oversized line without breaking escapes or UTF-16 pairs.

    Formatting on an exceptionally long single line is downgraded to escaped
    plain text. This is safer than cutting an open MarkdownV2 entity in half.
    """
    if _contains_unescaped_markup(line):
        line = escape_chars(plain_text_fallback(line))

    atoms = re.findall(r"\\.|[\s\S]", line)
    chunks: list[str] = []
    current: list[str] = []
    used = 0
    for atom in atoms:
        visible = atom[1:] if atom.startswith("\\") and len(atom) == 2 else atom
        units = utf16_len(visible)
        if current and used + units > max_len:
            chunks.append("".join(current))
            current = []
            used = 0
        current.append(atom)
        used += units
    if current:
        chunks.append("".join(current))
    return chunks


def split_text(text: str, max_len: int = 4096) -> list[str]:
    """
    Split MarkdownV2 text into chunks at paragraph boundaries.
    The max_len limit is checked against visible text length
    measured in UTF-16 code units (how Telegram counts characters).

    When a paragraph doesn't fit into the current chunk whole, its
    individual lines are used to fill the remaining space before
    starting a new chunk.
    """

    def vlen(s: str) -> int:
        return utf16_len(visible_text(s))

    if vlen(text) <= max_len:
        return [text]

    chunks: list[str] = []
    current = ""

    def try_append(current: str, addition: str, sep: str) -> tuple[str, bool]:
        """Try to append addition to current. Returns (result, success)."""
        candidate = f"{current}{sep}{addition}".strip() if current else addition
        if vlen(candidate) <= max_len:
            return candidate, True
        return current, False

    def flush(current: str, chunks: list[str]) -> str:
        if current:
            chunks.append(current)
        return ""

    paragraphs = text.split("\n\n")

    for para in paragraphs:
        current, ok = try_append(current, para, "\n\n")
        if ok:
            continue

        # Paragraph doesn't fit whole — split it by lines and
        # fill the current chunk as much as possible.
        lines = para.split("\n")
        for j, line in enumerate(lines):
            # First line of a new paragraph needs \n\n separator;
            # subsequent lines within the same paragraph use \n.
            sep = "\n\n" if (j == 0 and current) else ("\n" if current else "")
            current, ok = try_append(current, line, sep)
            if ok:
                continue

            # Line doesn't fit in current chunk — start a new one
            current = flush(current, chunks)

            # If a single line still exceeds max_len, split it at UTF-16-safe
            # MarkdownV2 atom boundaries.
            if vlen(line) > max_len:
                pieces = _hard_split_markdownv2_line(line, max_len)
                chunks.extend(pieces[:-1])
                current = pieces[-1]
            else:
                current = line

    flush(current, chunks)

    if any(vlen(chunk) > max_len for chunk in chunks):
        raise ValueError("unable to split Telegram text within its UTF-16 limit")
    return chunks


def resolve_chat_id(token: str, group: str) -> str:
    """
    Resolve a group identifier. If it looks like a numeric ID, return as-is.
    If it's a username like @mygroup, use getChat to validate and return the ID.
    """
    if group.lstrip("-").isdigit():
        return group

    if not group.startswith("@"):
        group = f"@{group}"

    url = f"{BASE_URL.format(token=token)}/getChat"
    resp = requests.post(url, json={"chat_id": group})
    data = resp.json()
    if not data.get("ok"):
        print(
            f"Error resolving group '{group}': {data.get('description')}",
            file=sys.stderr,
        )
        sys.exit(1)

    return str(data["result"]["id"])


AUDIO_EXTENSIONS = {".m4a", ".mp3"}


def classify_media(path: Path) -> str | None:
    """Return Telegram's photo/video/audio kind, or None if unsupported."""
    if path.suffix.lower() in AUDIO_EXTENSIONS:
        return "audio"
    mime, _ = mimetypes.guess_type(str(path))
    if not mime:
        return None
    if mime.startswith("image/"):
        return "photo"
    if mime.startswith("video/"):
        return "video"
    return None


def validate_media_set(media_paths: list[Path]) -> str | None:
    """Validate one Telegram upload before any part of the post is published."""
    if len(media_paths) > 10:
        return "Telegram media albums support at most 10 files"
    kinds = [classify_media(path) for path in media_paths]
    unsupported = [
        path.name for path, kind in zip(media_paths, kinds) if kind is None
    ]
    if unsupported:
        return "unsupported media file(s): " + ", ".join(unsupported)
    distinct = set(kinds)
    if "audio" in distinct and len(distinct) > 1:
        return "Telegram audio albums must contain audio files only"
    return None


def send_text_messages(
    token: str, chat_id: str, text: str, strict: bool = False
) -> list[dict]:
    """Send one or more text messages. Returns list of API responses.

    `text` should be raw markdown (will be converted to MarkdownV2).

    If Telegram rejects a chunk's MarkdownV2 markup:
      - strict=True  → give up immediately and return the error response, so the
        caller can abort before the same broken post reaches more channels.
      - strict=False → resend the chunk as plain text with the markup stripped
        (never the raw MarkdownV2, which would show escape backslashes and
        stray asterisks to readers). The response is tagged with
        "_markdown_fallback": True so callers can tell a degraded post from a
        clean one — `ok` alone is not enough.
    """
    converted = convert_markdown_to_telegramv2(text)
    vis = visible_text(converted)
    vis_len = utf16_len(vis)
    print(
        f"Text length: {len(text)} raw chars, "
        f"{len(converted)} MarkdownV2 chars, "
        f"{vis_len} visible UTF-16 units"
    )

    chunks = split_text(converted)
    url = f"{BASE_URL.format(token=token)}/sendMessage"
    results = []

    for i, chunk in enumerate(chunks, 1):
        chunk_vis_len = utf16_len(visible_text(chunk))
        print(
            f"Sending text message {i}/{len(chunks)} "
            f"({chunk_vis_len} visible / {len(chunk)} raw chars)..."
        )
        resp = requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": chunk,
                "parse_mode": "MarkdownV2",
                "disable_web_page_preview": True,
            },
        )
        data = resp.json()
        if not data.get("ok"):
            print(
                f"  MarkdownV2 rejected by Telegram: {data.get('description')}",
                file=sys.stderr,
            )
            if strict:
                print(
                    f"  Aborting chunk {i}/{len(chunks)} (strict mode): "
                    f"fix the markup instead of posting it unformatted.",
                    file=sys.stderr,
                )
                results.append(data)
                return results

            # Retry as plain text with the markup stripped — sending the raw
            # MarkdownV2 would leak escape backslashes into the message.
            print("  Retrying as plain text (formatting will be lost)...")
            resp = requests.post(
                url,
                json={
                    "chat_id": chat_id,
                    "text": plain_text_fallback(chunk),
                    "disable_web_page_preview": True,
                },
            )
            data = resp.json()
            if data.get("ok"):
                data["_markdown_fallback"] = True
                print(
                    "  Warning: posted WITHOUT formatting (links are now bare "
                    "text).",
                    file=sys.stderr,
                )
            else:
                print(f"  Error: {data.get('description')}", file=sys.stderr)
        results.append(data)

    return results


VIDEO_METADATA_EXTENSIONS = {".mp4", ".mov"}


def probe_video(path: Path) -> dict | None:
    """Probe a video with ffprobe.

    Returns a dict with width/height (corrected for rotation), duration in
    seconds, and (if present) the stream index of an embedded poster frame
    under "attached_pic_index". Returns None if ffprobe is unavailable or
    the file can't be parsed.
    """
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "v",
                "-show_streams",
                "-show_format",
                "-of",
                "json",
                str(path),
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        print(f"  ffprobe failed for {path.name}: {e}", file=sys.stderr)
        return None

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None

    streams = data.get("streams", [])
    main = next(
        (s for s in streams if not s.get("disposition", {}).get("attached_pic")),
        None,
    )
    attached = next(
        (s for s in streams if s.get("disposition", {}).get("attached_pic")),
        None,
    )
    if main is None:
        return None

    try:
        w, h = int(main["width"]), int(main["height"])
    except (KeyError, ValueError):
        return None

    # Rotation: prefer side_data (newer ffmpeg), fall back to tags.rotate.
    rotation = 0
    for sd in main.get("side_data_list", []):
        if "rotation" in sd:
            try:
                rotation = abs(int(float(sd["rotation"]))) % 360
            except (ValueError, TypeError):
                pass
            break
    if rotation == 0:
        rotate_tag = main.get("tags", {}).get("rotate")
        if rotate_tag:
            try:
                rotation = abs(int(rotate_tag)) % 360
            except ValueError:
                pass
    if rotation in (90, 270):
        w, h = h, w

    duration = 0
    try:
        duration = int(float(data.get("format", {}).get("duration", 0)))
    except (ValueError, TypeError):
        pass

    info = {"width": w, "height": h, "duration": duration}
    if attached is not None:
        try:
            info["attached_pic_index"] = int(attached["index"])
        except (KeyError, ValueError):
            pass
    return info


def extract_thumbnail(video: Path, out: Path, attached_pic_index: int | None) -> bool:
    """Write a Telegram-compliant JPEG thumbnail (≤320px on the longer side).

    Uses the video's embedded poster frame if attached_pic_index is given,
    otherwise grabs a frame ~1 s in (with a 0 s fallback for very short clips).
    """
    scale = "scale=320:320:force_original_aspect_ratio=decrease"

    if attached_pic_index is not None:
        cmds = [
            [
                "ffmpeg",
                "-y",
                "-i",
                str(video),
                "-map",
                f"0:{attached_pic_index}",
                "-frames:v",
                "1",
                "-vf",
                scale,
                "-q:v",
                "5",
                str(out),
            ]
        ]
    else:
        cmds = [
            [
                "ffmpeg",
                "-y",
                "-ss",
                "1",
                "-i",
                str(video),
                "-frames:v",
                "1",
                "-vf",
                scale,
                "-q:v",
                "5",
                str(out),
            ],
            [
                "ffmpeg",
                "-y",
                "-i",
                str(video),
                "-frames:v",
                "1",
                "-vf",
                scale,
                "-q:v",
                "5",
                str(out),
            ],
        ]

    last_err = ""
    for cmd in cmds:
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            if out.exists() and out.stat().st_size > 0:
                return True
        except FileNotFoundError as e:
            print(f"  ffmpeg not found: {e}", file=sys.stderr)
            return False
        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or b"").decode(errors="replace").strip()
            last_err = stderr.splitlines()[-1] if stderr else str(e)

    print(
        f"  Could not extract thumbnail from {video.name}: {last_err}",
        file=sys.stderr,
    )
    return False


def video_metadata(
    path: Path,
    index: int,
    files: dict[str, tuple[str, bytes, str]],
    tmp_dir: Path,
) -> dict:
    """InputMedia fields that make Telegram render a video correctly.

    Probes width/height/duration and attaches a poster frame, without which
    Telegram shows a square placeholder instead of the right aspect ratio.
    Returns {} for anything that is not a probe-able video. A thumbnail, when
    one could be extracted, is registered in `files` so it uploads in the same
    multipart request as the video.
    """
    if classify_media(path) != "video":
        return {}
    if path.suffix.lower() not in VIDEO_METADATA_EXTENSIONS:
        return {}
    meta = probe_video(path)
    if not meta:
        return {}

    attached_idx = meta.pop("attached_pic_index", None)
    fields: dict = {**meta, "supports_streaming": True}

    thumb_path = tmp_dir / f"thumb{index}.jpg"
    if extract_thumbnail(path, thumb_path, attached_idx):
        thumb_key = f"thumb{index}"
        files[thumb_key] = (thumb_path.name, thumb_path.read_bytes(), "image/jpeg")
        fields["thumbnail"] = f"attach://{thumb_key}"

    print(
        f"  Video {path.name}: {meta['width']}x{meta['height']}, "
        f"{meta['duration']}s"
        f"{' (with thumbnail)' if 'thumbnail' in fields else ''}"
    )
    return fields


def send_media_group(token: str, chat_id: str, media_paths: list[Path]) -> dict:
    """Send 2–10 photos/videos or a homogeneous audio album.

    For .mp4/.mov videos, probes width/height/duration via ffprobe and
    attaches a thumbnail (embedded poster or extracted frame) so Telegram
    renders the correct aspect ratio instead of a square placeholder.
    """
    problem = validate_media_set(media_paths)
    if problem:
        return {"ok": False, "description": problem}
    if len(media_paths) < 2:
        return {"ok": False, "description": "a media group needs at least 2 files"}

    url = f"{BASE_URL.format(token=token)}/sendMediaGroup"
    media_json: list[dict] = []
    files: dict[str, tuple[str, bytes, str]] = {}

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)

        for i, path in enumerate(media_paths):
            kind = classify_media(path)
            if kind is None:
                print(f"Skipping unsupported file: {path}", file=sys.stderr)
                continue

            attach_key = f"file{i}"
            mime, _ = mimetypes.guess_type(str(path))
            files[attach_key] = (
                path.name,
                path.read_bytes(),
                mime or "application/octet-stream",
            )
            entry: dict = {"type": kind, "media": f"attach://{attach_key}"}
            entry.update(video_metadata(path, i, files, tmp_dir))

            media_json.append(entry)

        if not media_json:
            print("No valid media files to send.", file=sys.stderr)
            return {}

        print(f"Sending media group ({len(media_json)} files)...")
        resp = requests.post(
            url,
            data={
                "chat_id": chat_id,
                "media": json.dumps(media_json),
            },
            files=files,
        )
        data = resp.json()

        if not data.get("ok"):
            print(f"Error sending media: {data.get('description')}", file=sys.stderr)
        else:
            print("Media group sent successfully.")

        return data


def send_single_media(token: str, chat_id: str, path: Path) -> dict:
    """Send one photo, video or audio file through its dedicated endpoint."""
    kind = classify_media(path)
    if kind is None:
        return {"ok": False, "description": f"unsupported media file: {path.name}"}
    endpoint = {
        "photo": "sendPhoto",
        "video": "sendVideo",
        "audio": "sendAudio",
    }[kind]
    mime, _ = mimetypes.guess_type(str(path))
    print(f"Sending {kind} {path.name}...")
    response = requests.post(
        f"{BASE_URL.format(token=token)}/{endpoint}",
        data={"chat_id": chat_id},
        files={
            kind: (
                path.name,
                path.read_bytes(),
                mime or "application/octet-stream",
            )
        },
    )
    data = response.json()
    if not data.get("ok"):
        print(f"Error sending {kind}: {data.get('description')}", file=sys.stderr)
    else:
        print(f"{kind.capitalize()} sent successfully.")
    return data


def send_media(token: str, chat_id: str, media_paths: list[Path]) -> dict:
    """Dispatch a validated single file or Telegram media album."""
    problem = validate_media_set(media_paths)
    if problem:
        print(f"Error: {problem}", file=sys.stderr)
        return {"ok": False, "description": problem}
    if not media_paths:
        return {"ok": True, "result": []}
    if len(media_paths) == 1:
        return send_single_media(token, chat_id, media_paths[0])
    return send_media_group(token, chat_id, media_paths)


# --- Rich messages (Bot API 10.1+) -----------------------------------------
#
# sendRichMessage takes GitHub-Flavored Markdown in one field and renders it
# natively: headings stay headings, lists stay lists, media sits in the post
# rather than in a trailing album, and the 4096-character sendMessage limit
# becomes 32768 — a release post is one message instead of the two or three
# MarkdownV2 splits it into. Nothing needs escaping, so this path bypasses the
# convert/escape/split machinery above rather than reusing it.

# Code first, so build_rich_markdown() rewrites only the <br> tags in prose.
CODE_OR_BR_RE = re.compile(
    f"(?P<code>{CODE_PATTERN})|(?P<br>{BR_RE.pattern})", re.IGNORECASE
)

RICH_TEXT_LIMIT = 32768  # "Up to 32768 UTF-8 characters in the rich message text"
RICH_MEDIA_LIMIT = 50  # "Up to 50 media attachments in total"

# tg:// scheme per media kind, for the "![](tg://photo?id=...)" media blocks.
RICH_MEDIA_SCHEMES = {"photo": "photo", "video": "video", "audio": "audio"}

# Languages base.html lays out right-to-left; is_rtl does the same for a post.
RTL_LANGS = frozenset(
    ["ar", "arc", "dv", "fa", "fa-IR", "ha", "he", "khw", "ks", "ku", "ps", "ur", "yi"]
)


def is_rtl_lang(lang: str) -> bool:
    """Whether a post in this language must be laid out right-to-left."""
    return lang in RTL_LANGS or lang.split("-")[0] in RTL_LANGS


def rich_media_id(path: Path, index: int) -> str:
    """A tg:// media id for one file: 1-64 chars of A-Z, a-z, 0-9, _ and -.

    The index keeps ids unique — two files can share a stem ("a.jpg", "a.png")
    — while the cleaned stem keeps the generated markdown readable.
    """
    stem = re.sub(r"[^A-Za-z0-9_-]", "-", path.stem)
    return f"m{index}-{stem}"[:64]


def build_rich_markdown(text: str, media_paths: Sequence[Path] = ()) -> str:
    """Render prepared post markdown as Telegram Rich Markdown.

    Rich Markdown is GFM, so the text passes through almost unchanged. Two
    things do not survive as they are:

    - <br/>, which Zola renders but Telegram does not list among the tags it
      parses, becomes a Markdown hard break (two trailing spaces). A bare
      newline would not do: Rich Markdown joins consecutive lines into one,
      exactly as CommonMark does. Two spaces degrade to a single space where
      a passed-through tag would degrade to a visible "<br/>" — the defect
      this replaces. A <br/> inside code is left alone, as in the MarkdownV2
      path: a post documenting HTML must survive being published.
    - Media, which "can be specified only as a separate block", is appended
      one block per file, in the order the site shows the post's assets.
    """
    # Code alternates first, so a match inside it is returned unchanged and
    # only the <br> tags in prose reach the replacement.
    text = CODE_OR_BR_RE.sub(
        lambda m: m.group("code") if m.group("code") else "  \n", text
    ).rstrip()

    blocks = []
    for index, path in enumerate(media_paths):
        scheme = RICH_MEDIA_SCHEMES.get(classify_media(path))
        if scheme is None:
            print(f"Skipping unsupported file: {path}", file=sys.stderr)
            continue
        blocks.append(f"![](tg://{scheme}?id={rich_media_id(path, index)})")

    return "\n\n".join([text, *blocks]) if blocks else text


def validate_rich_media(media_paths: Sequence[Path]) -> str | None:
    """Validate a rich message's attachments before any of it is published.

    Rich messages have neither the 10-file album cap nor the homogeneous-audio
    rule of sendMediaGroup, so validate_media_set() does not apply here.
    """
    if len(media_paths) > RICH_MEDIA_LIMIT:
        return (
            f"{len(media_paths)} media files, over Telegram's limit of "
            f"{RICH_MEDIA_LIMIT}"
        )
    unsupported = [p.name for p in media_paths if classify_media(p) is None]
    if unsupported:
        return "unsupported media file(s): " + ", ".join(unsupported)
    return None


def validate_rich_message(
    markdown: str, media_paths: Sequence[Path]
) -> str | None:
    """Check the limits sendRichMessage enforces, before anything is sent."""
    if not markdown.strip():
        return "the rich message is empty"

    # "UTF-8 characters" reads as code points but could mean bytes, and the
    # docs settle it nowhere. Both are checked: a post that passes here and is
    # refused by the API would abort a run that has already published to
    # earlier channels, where a false rejection is merely loud and early.
    characters = len(markdown)
    utf8_bytes = len(markdown.encode("utf-8"))
    if max(characters, utf8_bytes) > RICH_TEXT_LIMIT:
        return (
            f"rich message is {characters} characters / {utf8_bytes} UTF-8 "
            f"bytes, over Telegram's limit of {RICH_TEXT_LIMIT}"
        )
    return validate_rich_media(media_paths)


def send_rich_message(
    token: str,
    chat_id: str,
    text: str,
    media_paths: Sequence[Path] = (),
    is_rtl: bool = False,
) -> dict:
    """Send one post as a single rich message. Returns the API response.

    Unlike the MarkdownV2 path there is nothing to split and no unformatted
    fallback: the post either lands whole or does not land at all, so a
    failure never leaves a channel half-published.
    """
    media_paths = list(media_paths)
    markdown = build_rich_markdown(text, media_paths)

    problem = validate_rich_message(markdown, media_paths)
    if problem:
        print(f"Error: {problem}", file=sys.stderr)
        return {"ok": False, "description": problem}

    print(
        f"Rich message: {len(markdown)} characters, "
        f"{len(media_paths)} media file(s){', RTL' if is_rtl else ''}"
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        files: dict[str, tuple[str, bytes, str]] = {}
        media_json: list[dict] = []

        for index, path in enumerate(media_paths):
            attach_key = f"file{index}"
            mime, _ = mimetypes.guess_type(str(path))
            files[attach_key] = (
                path.name,
                path.read_bytes(),
                mime or "application/octet-stream",
            )
            entry: dict = {
                "type": classify_media(path),
                "media": f"attach://{attach_key}",
            }
            entry.update(video_metadata(path, index, files, tmp_dir))
            media_json.append({"id": rich_media_id(path, index), "media": entry})

        payload: dict = {"markdown": markdown}
        if media_json:
            payload["media"] = media_json
        if is_rtl:
            payload["is_rtl"] = True

        resp = requests.post(
            f"{BASE_URL.format(token=token)}/sendRichMessage",
            data={"chat_id": chat_id, "rich_message": json.dumps(payload)},
            files=files,
        )
        data = resp.json()

    if not data.get("ok"):
        print(f"  Error: {data.get('description')}", file=sys.stderr)
    return data


def main():
    parser = argparse.ArgumentParser(
        description="Publish a markdown post with optional media to a Telegram group."
    )
    parser.add_argument(
        "--group",
        "-g",
        required=True,
        help="Telegram group username (@name) or numeric chat ID",
    )
    parser.add_argument(
        "--text", "-t", required=True, type=Path, help="Path to markdown text file"
    )
    parser.add_argument(
        "--media",
        "-m",
        nargs="*",
        type=Path,
        default=[],
        help="Paths to image/video/audio files to attach",
    )
    parser.add_argument(
        "--yes",
        "-y",
        action="store_true",
        help="Skip confirmation prompts (e.g. for unresolved references)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Abort if Telegram rejects the MarkdownV2 markup, instead of "
        "falling back to unformatted plain text",
    )
    parser.add_argument(
        "--rich",
        action="store_true",
        help="Send one Bot API rich message (real headings, lists and inline "
        "media, 32768-character limit) instead of chunked MarkdownV2",
    )
    args = parser.parse_args()

    if not args.text.is_file():
        print(f"Error: text file not found: {args.text}", file=sys.stderr)
        sys.exit(1)

    for mp in args.media:
        if not mp.is_file():
            print(f"Error: media file not found: {mp}", file=sys.stderr)
            sys.exit(1)
    media_problem = validate_media_set(args.media)
    if media_problem:
        print(f"Error: {media_problem}", file=sys.stderr)
        sys.exit(1)

    token = get_token()
    chat_id = resolve_chat_id(token, args.group)
    raw_text = args.text.read_text(encoding="utf-8")

    # Strip frontmatter; use "title" field as a bold header
    text, meta = strip_frontmatter(raw_text)
    title = meta.get("title", "")
    if title:
        # Rich messages render headings; MarkdownV2 can only fake one in bold.
        heading = f"# {title}" if args.rich else f"**{title}**"
        text = f"{heading}\n\n{text.lstrip()}"

    # Tera expressions and components are site-only and do not belong in posts.
    text = strip_tera_blocks(text)

    # Strip angle brackets from bare URLs: <https://...> → https://...
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)

    # Clean up blank lines left by removed Tera blocks.
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Resolve markdown reference-style links
    # tools/ lives one level below the site root
    site_root = Path(__file__).resolve().parent.parent
    refs = load_references(site_root)
    text = resolve_references(text, refs)
    if refs:
        print(f"Loaded {len(refs)} reference(s) from references.md")

    # Resolve Zola @/-style internal references → absolute site URLs.
    base_url = load_base_url(site_root)
    text, zola_unresolved = resolve_zola_references(text, site_root, base_url)
    if zola_unresolved:
        print(
            f"\nWarning: {len(zola_unresolved)} Zola @/-reference(s) could not be resolved:",
            file=sys.stderr,
        )
        for target in zola_unresolved:
            print(f"  @/{target}", file=sys.stderr)
        print(file=sys.stderr)

    raw_html = find_raw_html(text, rich=args.rich)
    if raw_html:
        print(
            f"\nWarning: {len(raw_html)} HTML tag(s) Telegram will show "
            f"literally:",
            file=sys.stderr,
        )
        for tag, lineno in raw_html:
            print(f"  line {lineno}: {tag}", file=sys.stderr)
        print(file=sys.stderr)

    # Warn about any unresolved references
    unresolved = find_unresolved_references(text)
    if unresolved:
        print(
            f"\nWarning: {len(unresolved)} unresolved reference(s) found:",
            file=sys.stderr,
        )
        for match_text, ref_id, lineno in unresolved:
            print(
                f"  line {lineno}: {match_text}  (undefined id: {ref_id})",
                file=sys.stderr,
            )
        print(file=sys.stderr)
        if not args.yes:
            answer = input(
                "Continue posting with unresolved references? [y/N] "
            ).strip()
            if answer.lower() not in ("y", "yes"):
                print("Aborted.")
                sys.exit(0)

    print(f"Target chat: {chat_id}")
    if title:
        print(f"Title: {title}")
    print(f"Media files: {len(args.media)}")
    print()

    if args.rich:
        lang = ZOLA_FILENAME_RE.match(args.text.name)
        result = send_rich_message(
            token,
            chat_id,
            text,
            args.media,
            is_rtl=is_rtl_lang((lang.group("lang") if lang else None) or "en"),
        )
        if not result.get("ok"):
            print("\nFATAL: the rich message was not sent.", file=sys.stderr)
            sys.exit(1)
        print("\nDone.")
        return

    results = send_text_messages(token, chat_id, text, strict=args.strict)

    failed = [r for r in results if not r.get("ok")]
    if failed:
        print(
            f"\nFATAL: {len(failed)} message(s) failed to send.", file=sys.stderr
        )
        sys.exit(1)

    degraded = [r for r in results if r.get("_markdown_fallback")]
    if degraded:
        print(
            f"\nWarning: {len(degraded)} message(s) were posted without "
            f"formatting. Re-run with --strict to catch this before posting.",
            file=sys.stderr,
        )

    if args.media:
        media_result = send_media(token, chat_id, args.media)
        if not media_result.get("ok"):
            print(
                "FATAL: text was posted, but media failed. Resend only the "
                "media manually; rerunning this command would duplicate the text.",
                file=sys.stderr,
            )
            sys.exit(1)

    print("\nDone.")


if __name__ == "__main__":
    main()
