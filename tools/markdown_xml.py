#!/usr/bin/env python3
"""Lossless markdown <-> XML mapping for machine translation.

Machine translators mangle raw markdown: they move `**` markers, drop the
opening `[` of links, and translate URLs. DeepL's XML tag handling solves this
properly — inline tags are repositioned *grammatically* for the target language
— but only if markdown is expressed as tags first. That is what this module
does.

    payload, ctx = to_xml(md)      # markdown -> XML payload
    md2 = from_xml(payload, ctx)   # XML payload -> markdown
    assert md2 == md               # exact, for any markdown

Two kinds of tag come out:

  <x>N</x>      Content that must never be translated: code, URLs, shortcodes,
                contributor attributions, raw HTML, brand names, list markers.
                Send with DeepL's ignore_tags=x.
  <b0> <i1>     Formatting wrappers whose *content* is translatable: bold,
  <a2> <s3>     italic, strikethrough, link labels. Indexed so the original
                delimiters and link targets survive even when the translator
                reorders them (Turkish and Chinese both do).

The module is deliberately free of any DeepL, Telegram or Zola knowledge so the
same mapping serves Telegram posts, site articles and release notes alike.
"""

import re

__all__ = ["to_xml", "from_xml", "Context", "xml_escape", "xml_unescape",
           "find_balanced_close", "PROTECTED_BRANDS"]

# Brand and product names that must stay verbatim in every language. DeepL
# transliterates these into non-Latin scripts otherwise.
PROTECTED_BRANDS = [
    "Organic Maps", "OpenStreetMap", "ID Editor", "Google Play", "App Store",
    "Huawei AppGallery", "AppGallery", "TestFlight", "F-Droid", "Obtainium",
    "Accrescent", "Android Auto", "CarPlay", "Android", "iOS", "GitHub",
    "Firebase", "Wikipedia", "Mapbox", "GPX", "KML", "KMZ", "GeoJSON",
]


class Context:
    """Everything needed to turn a payload back into markdown."""

    def __init__(self):
        self.stash: list[str] = []          # <x>N</x> -> original text
        self.wrappers: dict[str, tuple[str, str]] = {}   # tag -> (open, close)
        self.counters: dict[str, int] = {}

    def protect(self, text: str) -> str:
        self.stash.append(text)
        return f"<x>{len(self.stash) - 1}</x>"

    def wrap(self, kind: str, open_delim: str, close_delim: str) -> str:
        n = self.counters.get(kind, 0)
        self.counters[kind] = n + 1
        tag = f"{kind}{n}"
        self.wrappers[tag] = (open_delim, close_delim)
        return tag


def xml_escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def xml_unescape(text: str) -> str:
    # &amp; last, so "&amp;lt;" survives as the literal "&lt;".
    return text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


# --------------------------------------------------------------------------
# Scanning helpers
# --------------------------------------------------------------------------

def find_balanced_close(s: str, start: int, open_ch: str, close_ch: str) -> int:
    """Index of the balanced closing delimiter, or -1.

    Backslash-escaped delimiters do not count — the corpus contains
    "[\\[matrix\\]](url)", which a naive [^\\]]* pattern truncates.
    """
    depth = 0
    i = start
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


_FENCE_RE = re.compile(r"```[\s\S]*?```")
_CODE_RE = re.compile(r"`[^`\n]+`")
_SHORTCODE_RE = re.compile(r"\{\{[^}]*\}\}")
# Autolinks cover URLs, explicit schemes and bare e-mail addresses. The corpus
# contains <sdk@organicmaps.app>, which no HTML-tag pattern matches.
_AUTOLINK_RE = re.compile(
    r"<(?:[a-zA-Z][a-zA-Z0-9+.-]*:[^>\s]*|[^\s<>@]+@[^\s<>]+)>"
)
_HTML_RE = re.compile(r"</?[a-zA-Z][a-zA-Z0-9]*(?:\s[^>]*)?/?>")
# A link-definition URL may embed a shortcode containing spaces, as in
# "[appgallery]: https://…?local={{ lang }} "…"" — so \S+ is not enough.
_LINKDEF_RE = re.compile(
    r"(?m)^\[[^\]]+\]:[ \t]+(?:\{\{[^}]*\}\}|\S)+"
    r"(?:[ \t]+[\"(](?:\{\{[^}]*\}\}|[^\"())])*[\")])?[ \t]*$"
)
_ATTRIB_RE = re.compile(r"_\([^)\n]+\)_")
_BARE_URL_RE = re.compile(r"https?://[^\s<>\[\]()]+")
_MARKER_RE = re.compile(r"(?m)^([ \t]*)(?:([-*+])[ \t]+|(#{1,6})[ \t]+|(\d+\.)[ \t]+)")
_ESCAPE_RE = re.compile(r"\\.")
# A trailing plural "s" is part of the brand token: without it "OpenStreetMaps"
# fails the right-boundary check and the whole word leaks into translatable text.
_BRAND_RE = re.compile(
    "(?:"
    + "|".join(re.escape(b) for b in sorted(PROTECTED_BRANDS, key=len, reverse=True))
    + ")s?"
)

# Emphasis: the delimiter must not sit against a word character on the outside,
# so snake_case and 3*4 are left alone.
_EMPHASIS = [
    ("b", "***", "i"),   # ***x*** -> bold-italic, handled as one wrapper
    ("b", "**", None),
    ("s", "~~", None),
    ("i", "*", None),
    ("i", "_", None),
]


def _protect_markers(md: str, ctx: Context) -> str:
    """Turn leading list/heading markers into ignored tokens.

    Keeps "- " and "### " out of the translated payload without needing the
    caller to split lines, so a whole document round-trips in one call.
    """
    def repl(m: re.Match) -> str:
        return m.group(1) + ctx.protect(m.group(0)[len(m.group(1)):])

    return _MARKER_RE.sub(repl, md)


def to_xml(md: str, protect_brands: bool = True) -> tuple[str, Context]:
    """Convert markdown to an XML payload plus the context to reverse it."""
    if "<x>" in md or "</x>" in md:
        raise ValueError(
            "input already contains an <x> tag, which would collide with the "
            "placeholder scheme"
        )

    ctx = Context()
    md = _protect_markers(md, ctx)
    return _convert(md, ctx, protect_brands), ctx


def _convert(s: str, ctx: Context, protect_brands: bool) -> str:
    out: list[str] = []
    i = 0
    n = len(s)

    def flush_text(text: str) -> str:
        return xml_escape(text)

    plain_start = 0

    def emit_plain(upto: int) -> None:
        nonlocal plain_start
        if upto > plain_start:
            out.append(flush_text(s[plain_start:upto]))
        plain_start = upto

    while i < n:
        c = s[i]

        # Already-emitted placeholder from marker protection.
        if s.startswith("<x>", i):
            end = s.index("</x>", i) + 4
            emit_plain(i)
            out.append(s[i:end])
            i = plain_start = end
            continue

        # Backslash escape — copy both characters verbatim.
        if c == "\\" and i + 1 < n:
            i += 2
            continue

        # --- spans that are protected wholesale -------------------------
        matched = None
        for rx in (_FENCE_RE, _CODE_RE, _SHORTCODE_RE, _AUTOLINK_RE,
                   _LINKDEF_RE, _ATTRIB_RE, _HTML_RE):
            m = rx.match(s, i)
            if m:
                matched = m
                break
        if matched:
            emit_plain(i)
            out.append(ctx.protect(matched.group(0)))
            i = plain_start = matched.end()
            continue

        # --- images and links -------------------------------------------
        if c == "!" and i + 1 < n and s[i + 1] == "[":
            close = find_balanced_close(s, i + 1, "[", "]")
            if close != -1 and close + 1 < n and s[close + 1] == "(":
                paren = find_balanced_close(s, close + 1, "(", ")")
                if paren != -1:
                    emit_plain(i)
                    out.append(ctx.protect(s[i:paren + 1]))
                    i = plain_start = paren + 1
                    continue

        if c == "[":
            close = find_balanced_close(s, i, "[", "]")
            if close != -1:
                label = s[i + 1:close]
                after = close + 1
                tail = None
                if after < n and s[after] == "(":
                    paren = find_balanced_close(s, after, "(", ")")
                    if paren != -1:
                        tail = s[close:paren + 1]      # "](url)"
                        end = paren + 1
                elif after < n and s[after] == "[":
                    brack = find_balanced_close(s, after, "[", "]")
                    if brack != -1:
                        tail = s[close:brack + 1]      # "][id]"
                        end = brack + 1
                if tail is not None:
                    emit_plain(i)
                    tag = ctx.wrap("a", "[", tail)
                    inner = _convert(label, ctx, protect_brands)
                    out.append(f"<{tag}>{inner}</{tag}>")
                    i = plain_start = end
                    continue

        # --- emphasis ----------------------------------------------------
        handled = False
        for kind, delim, _extra in _EMPHASIS:
            if not s.startswith(delim, i):
                continue
            # Opening delimiter must not follow a word character for _ and *.
            if delim in ("_", "*") and i > 0 and (s[i - 1].isalnum() or s[i - 1] == delim):
                continue
            search = i + len(delim)
            while True:
                j = s.find(delim, search)
                if j == -1:
                    break
                if s[j - 1] == "\\":
                    search = j + len(delim)
                    continue
                after = j + len(delim)
                if delim in ("_", "*") and after < n and (s[after].isalnum() or s[after] == delim):
                    search = after
                    continue
                break
            if j == -1 or j == i + len(delim):
                continue
            inner_src = s[i + len(delim):j]
            if not inner_src.strip():
                continue
            emit_plain(i)
            tag = ctx.wrap(kind, delim, delim)
            out.append(f"<{tag}>{_convert(inner_src, ctx, protect_brands)}</{tag}>")
            i = plain_start = j + len(delim)
            handled = True
            break
        if handled:
            continue

        # --- bare URLs and brands ---------------------------------------
        m = _BARE_URL_RE.match(s, i)
        if m:
            emit_plain(i)
            out.append(ctx.protect(m.group(0)))
            i = plain_start = m.end()
            continue

        if protect_brands:
            m = _BRAND_RE.match(s, i)
            if m and (i == 0 or not s[i - 1].isalnum()):
                end = m.end()
                if end >= n or not s[end].isalnum():
                    emit_plain(i)
                    out.append(ctx.protect(m.group(0)))
                    i = plain_start = end
                    continue

        i += 1

    emit_plain(n)
    return "".join(out)


_TOKEN_RE = re.compile(r"<x>(\d+)</x>|</?([a-z]+\d+)>")


def from_xml(payload: str, ctx: Context) -> str:
    """Turn a payload back into markdown using the context from to_xml().

    Walks tokens linearly rather than matching pairs, so a translator that
    reorders or splits tags still produces sane output; the caller's validation
    step is what decides whether the result is acceptable.
    """
    out: list[str] = []
    pos = 0
    for m in _TOKEN_RE.finditer(payload):
        if m.start() > pos:
            out.append(xml_unescape(payload[pos:m.start()]))
        idx, tag = m.group(1), m.group(2)
        if idx is not None:
            i = int(idx)
            out.append(ctx.stash[i] if i < len(ctx.stash) else "")
        else:
            delims = ctx.wrappers.get(tag)
            if delims:
                out.append(delims[0] if m.group(0)[1] != "/" else delims[1])
        pos = m.end()
    if pos < len(payload):
        out.append(xml_unescape(payload[pos:]))
    return "".join(out)
