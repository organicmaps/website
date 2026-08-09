#!/usr/bin/env python3
"""Validate a machine translation before it is published.

Machine translation fails in ways that look fine at a glance and are invisible
if you cannot read the language: a dropped link, an attribution yanked into the
middle of a sentence, a word spliced together from two alphabets. This module
compares a translation against its English source and reports what broke.

    from translate_check import check_translation
    problems = check_translation(english_md, translated_md, "ar")

Usage:
    python3 translate_check.py source.md translated.md ar
    python3 translate_check.py content/news/2026-07-23/620/     # whole folder
    python3 translate_check.py <folder> --errors-only

Exit code is 1 if any ERROR-level problem is found, 0 otherwise, so it can gate
a publish step.
"""

import argparse
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from telegram_post import strip_frontmatter
from translate_md import register_ok, expected_register, QUOTE_FOR

ERROR, WARN = "ERROR", "warn"


@dataclass
class Problem:
    level: str
    code: str
    message: str
    detail: str = ""

    def __str__(self) -> str:
        head = f"  [{self.level}] {self.code}: {self.message}"
        return f"{head}\n      {self.detail}" if self.detail else head


# --------------------------------------------------------------- fingerprints

def fingerprint(text: str) -> dict[str, int]:
    """Structural features that translation must preserve exactly."""
    return {
        # Blank-line-separated blocks, not raw lines: a soft line break inside
        # a paragraph renders identically, and prettier normalises it, so a
        # raw-line count would flag pure reformatting as lost content.
        "blocks": len([b for b in re.split(r"\n\s*\n", text) if b.strip()]),
        "bullets": len(re.findall(r"(?m)^[ \t]*[-*+][ \t]+", text)),
        "headings": len(re.findall(r"(?m)^[ \t]*#{1,6}[ \t]+", text)),
        "inline_links": len(re.findall(r"\]\(", text)),
        "ref_links": len(re.findall(r"\]\[", text)),
        "attributions": len(re.findall(r"_\([^)\n]+\)_", text)),
        "shortcodes": len(re.findall(r"\{\{", text)),
        "code_spans": len(re.findall(r"`[^`\n]+`", text)),
        "images": len(re.findall(r"!\[", text)),
    }


BRANDS = ["Organic Maps", "OpenStreetMap", "ID Editor", "Google Play",
          "App Store", "F-Droid", "Obtainium", "Accrescent", "TestFlight",
          "Huawei AppGallery", "AppGallery", "Weblate", "TestFlight"]
QUOTE_CHARS = "\"'«»„“”‘’《》〈〉「」〔〕"
# Opening/closing marks that genuinely pair, so a stray apostrophe used as
# a suffix separator is not mistaken for a closing quote.
QUOTE_PAIRS = [('"', '"'), ("'", "'"), ("«", "»"), ("„", "“"), ("„", "”"),
               ("“", "”"), ("‘", "’"), ("《", "》"), ("〈", "〉"),
               ("「", "」"), ("〔", "〕")]

# Which brands a language is allowed to transliterate. Measured, not assumed:
# he/ar/fa-IR keep Organic Maps, OpenStreetMap and iOS in Latin but render
# Android natively; the Indic scripts transliterate everything.
BRAND_TRANSLITERATING = {
    "he": {"Android"}, "ar": {"Android"}, "fa-IR": {"Android"},
    # hi, ml and te used to be exempt from every brand check because they
    # transliterated the product name. That was decided against: they now keep
    # Latin brands like everyone else, so only Android stays exempt.
    "hi": {"Android"}, "ml": {"Android"}, "te": {"Android"},
}

# The product name rendered as translated words rather than kept in Latin.
# Every pattern here was observed in the corpus, not guessed: a review pass
# found 165 pages across 20 languages doing this. Stems, because most of these
# languages inflect the phrase (Estonian alone had eight case forms).
TRANSLATED_BRAND = {
    "af": r"organiese\s+kaart",
    "ca": r"mapes\s+orgànic",
    "cs": r"organick\w*\s+map",
    "cy": r"[fm]apiau\s+organig",
    "el": r"οργανικ\w*\s+χάρτ",
    "et": r"orgaanili\w*\s+kaar",
    "eu": r"\bmaps?a?k?\s+organiko",
    "fa-IR": r"نقشه‌های ارگانیک",
    "gl": r"mapas\s+orgánico",
    "he": r"המפות האורגניות",
    "hu": r"(organikus|szerves)\s+térkép",
    "id": r"peta\s+organik",
    "it": r"mapp[ae]\s+organic",
    "lt": r"(natūral|organin)\w*\s+žemėlap",
    "mr": r"(सेंद्रिय|ऑरगॅनिक|ऑर्गेनिक)\s*(नकाश|मॅप्स)",
    "nl": r"organische\s+kaart",
    "oc": r"mapas\s+organicas",
    "pl": r"map\w*\s+organiczn|organiczn\w*\s+map",
    "sv": r"organiska\s+kartor",
    "tr": r"organik\s+harita",
    "zh-Hans": r"有机地图",
    # Transliterations as well as translations: these three keep Latin brands.
    "hi": r"ऑर्ग[ैे]?निक\s*(मैप|मानचित्र|नक़?्श)|जैविक\s*(मानचित्र|नक्शे)",
    "ml": r"ഓർഗാനിക്\s*മാപ്|ജ[ൈെ]െ?വ\s*ഭൂപട",
    "te": r"ఆర్గానిక్\s*మ(్య)?ాప|సేంద్రీయ\s*మ్యాప్",
}
# The homepage's "Why organic?" section uses the adjective legitimately.
TRANSLATED_BRAND_EXEMPT = {"mr": ("Why organic", "सेंद्रिय")}

# Scripts that do not put spaces between words: text running straight into a
# link is normal there, so the suffix-outside-link check does not apply.
#
# The Indic languages are here for a different reason. They do use spaces, but
# they attach case markers and postpositions directly to the preceding word,
# and that word may be a link label: Telugu writes `[ID Editor](url)ని` exactly
# as it writes `ఎడిటర్‌ని`. The marker `ని` appears attached to an ordinary
# word 396 times in this corpus, so a link is no different. Twenty of the
# twenty-two warnings this check produced were that, correctly written.
NO_SPACE_SCRIPTS = {"zh-Hans", "ja", "th", "lo", "my", "km",
                    "te", "ml", "mr", "hi", "ta", "kn"}


# Writing systems that combine several Unicode scripts by design: Japanese
# mixes Hiragana, Katakana and Kanji inside one word, Korean mixes Hangul with
# Hanja. Treating them as one script keeps the mixed-script rule from firing on
# perfectly normal text.
# Matched by prefix: the long-vowel mark is named "KATAKANA-HIRAGANA
# PROLONGED SOUND MARK", which no exact-match table would catch.
_CJK_PREFIXES = ("HIRAGANA", "KATAKANA", "HANGUL", "CJK", "IDEOGRAPHIC")


def _script(ch: str) -> str:
    try:
        name = unicodedata.name(ch).split()[0]
    except ValueError:
        return "?"
    # Modifier letters belong to no alphabet. U+02BC MODIFIER LETTER
    # APOSTROPHE is the correct Ukrainian apostrophe in "обʼїзду", and
    # counting it as its own script made every such word look spliced.
    if unicodedata.category(ch) == "Lm":
        return "COMMON"
    return "CJK" if name.startswith(_CJK_PREFIXES) else name


# Only Cyrillic and Greek share enough letterforms with Latin for a translator
# to splice the two inside one word ("мет" + "ek"). Restricting the check to
# them removes three classes of false positive seen in the real corpus:
#   Arabic  وGoogle   - the conjunction و legitimately prefixes a Latin word
#   Chinese 上的FAQ翻译 - no word spaces, so Latin runs sit inside a "word"
#   Indic   OpenStreetMapలో - a case marker attached to a Latin brand
HOMOGLYPH_SCRIPTS = {"CYRILLIC", "GREEK"}


def mixed_script_words(text: str) -> list[str]:
    """Words spliced from two alphabets, e.g. Cyrillic "мет" + Latin "ek".

    A word that STARTS Latin and continues in the local script is fine — that
    is a brand taking a native suffix ("OpenStreetMapi" in Estonian). The
    corrupt case is a word that starts in a homoglyph-prone script and switches
    to lowercase Latin partway through.
    """
    bad = []
    for word in re.findall(r"[^\W\d_]{2,}", text, re.UNICODE):
        # Only letters carry script identity. Footnote markers and other
        # non-letter word characters ("מיליון¹") are not a second alphabet.
        scripts = [_script(c) for c in word if c.isalpha()]
        distinct = {s for s in scripts if s not in ("COMMON", "?")}
        # Two different NON-Latin alphabets in one word is always corruption -
        # the corpus had Arabic letters spliced into a Hebrew word.
        if len(distinct) > 1 and "LATIN" not in distinct:
            bad.append(word)
            continue
        if "LATIN" not in scripts or scripts[0] == "LATIN":
            continue
        if not HOMOGLYPH_SCRIPTS & set(scripts):
            continue
        latin = "".join(c for c, s in zip(word, scripts) if s == "LATIN")
        # A capitalised Latin run is a brand embedded in native text, not
        # corruption: "и Android" tokenises oddly but is perfectly fine.
        if latin != latin.lower():
            continue
        bad.append(word)
    return bad


# --------------------------------------------------------------- link diffing

_LANG_SUFFIX = re.compile(r"/index\.[a-zA-Z]{2}(?:-[A-Za-z]+)?\.md\b")


def _inline_targets(text: str) -> Counter:
    """Inline-link targets, normalised so a correct translation matches source.

    Three differences between a source and its translation are legitimate and
    must not read as drift: the `@/…/index.LANG.md` suffix a translated link is
    *required* to carry, an optional `"title"`, and padding inside the parens.
    Leaving them in buried the real drift under noise — every localised link
    showed up as one `missing` plus one `extra`.

    Scanning for the balanced closing paren also fixes a truncation bug: with
    `\\]\\(([^)]+)\\)` a URL containing a bracketed segment — Wikipedia's
    `Çatal_(yazılım_geliştirme)` is one in the corpus — was cut at its first
    inner `)`, so it never matched its own source.
    """
    targets: Counter = Counter()
    for m in re.finditer(r"\]\(", text):
        i = j = m.end()
        depth = 1
        while j < len(text):
            c = text[j]
            if c == "\\":
                j += 2
                continue
            if c == "\n":
                break
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        target = text[i:j].strip()
        target = re.sub(r"""\s+["'][^"']*["']$""", "", target).strip()
        targets[_LANG_SUFFIX.sub("/index.md", target)] += 1
    return targets


def _localised_refs(src_body: str, out_body: str, lang: str) -> Counter:
    """Reference ids a translation may legitimately add to its source.

    A translation localises a community link one of two ways, and only one of
    them changes the reference count:

    - It *substitutes*: `contribute` points a German reader at
      `[telegram_chat_de]` where English has `[telegram_chat]`. One reference
      either way, so the counts already agree and nothing is needed here.
    - It *adds*: the homepage sends every reader to the English chat and, where
      one exists, to their own language's chat too, so `de` carries
      `[telegram_chat]` *and* `[telegram_chat_de]`, and `ru` adds `[matrix_ru]`
      beside `[matrix]`. That is deliberately one reference more than the
      source.

    Only the second case is an allowance, and it needs two guards:

    - `X` must be present alongside `X_<lang>`, or every substituting page
      becomes a phantom "missing X" — 10 of them across `contribute`.
    - Only the *surplus* over the source's own count is discounted. The 500
      release notes list every language's chat in the English source, so
      `telegram_chat_de` appears on both sides there and is not an addition
      at all; discounting it regardless invented a missing reference on 10
      more pages.
    """
    base = lang.split("-")[0]
    src_ids = Counter(re.findall(r"\]\[([^\]]+)\]", src_body))
    out_ids = Counter(re.findall(r"\]\[([^\]]+)\]", out_body))

    added: Counter = Counter()
    for ref, n in out_ids.items():
        if not ref.endswith(f"_{base}"):
            continue
        stem = ref[:-len(base) - 1]
        if stem not in src_ids or stem not in out_ids:
            continue
        surplus = n - src_ids[ref]
        if surplus > 0:
            added[ref] = surplus
    return added


# ----------------------------------------------------------------- emphasis

# Only the two-character delimiters are checkable. A lone `*` or `_` is
# ordinary text far too often here — `cuisine=*`, `opening_hours=*`,
# `stripe_eur`, `base_url()` — and a lone `~` means "approximately" in
# `~2000 bug reports`. `**`, `__` and `~~` have no other meaning in prose.
_EMPH = ("**", "__", "~~")


def _checkable(text: str) -> str:
    """Drop the regions where these characters are not markup."""
    text = re.sub(r"`[^`\n]*`", " ", text)          # code spans
    text = re.sub(r"\{\{[^}]*\}\}", " ", text)      # shortcode arguments
    text = re.sub(r"<[^>]+>", " ", text)            # inline HTML
    text = re.sub(r"\]\([^)\s]*\)", "]( )", text)   # link targets
    return re.sub(r"(?m)^\[[^\]]+\]:.*$", " ", text)  # reference definitions


def emphasis_faults(body: str) -> list[str]:
    """Emphasis that CommonMark will not close, leaving the raw characters.

    Three shapes, each seen in this corpus and each invisible until someone
    looks at the built page:

        ~~Dim plaladdwyr ~~     a closer after whitespace is not right-flanking
        ~~कीटकनाशक नाही~~~      `~~~` is not an inline delimiter
        ** Android **           an opener before whitespace is not left-flanking

    `***x***` and `___x___` are valid strong+emphasis and are left alone; only
    a run of four or more asterisks or underscores is wrong. Tildes have no
    triple form, so three is already wrong.
    """
    faults: list[str] = []
    for para in re.split(r"\n\s*\n", body):
        p = _checkable(para)
        for d in _EMPH:
            ch = d[0]
            if ch == "~" and re.search(r"~{3,}", p):
                faults.append(f"'~~~' is not an inline delimiter")
                continue
            if ch != "~" and re.search(re.escape(ch) + r"{4,}", p):
                faults.append(f"run of four or more '{ch}'")
                continue
            n = len(re.findall(re.escape(d), p))
            if not n:
                continue
            if n % 2:
                faults.append(f"{n} '{d}' delimiters — one is never closed")
                continue
            # Pair the delimiters in order — 1st with 2nd, 3rd with 4th — as
            # CommonMark does. Scanning for `**(.+?)**` instead matches the gap
            # *between* two spans, so `**A** en **B**` reports a phantom
            # `** en **`; that cost two false positives out of five.
            spots = [m.start() for m in re.finditer(re.escape(d), p)]
            for open_at, close_at in zip(spots[::2], spots[1::2]):
                inner = p[open_at + len(d):close_at]
                if inner[:1].isspace() or inner[-1:].isspace():
                    faults.append(f"'{d}' with a space beside it: "
                                  f"{p[open_at:close_at + len(d)][:36]!r}")
    return faults


# ------------------------------------------------------------------- checks

def check_translation(src: str, out: str, lang: str) -> list[Problem]:
    """Compare a translated markdown body against its English source."""
    src_body, _ = strip_frontmatter(src)
    out_body, out_meta = strip_frontmatter(out)
    problems: list[Problem] = []

    # A section _index body is a note to whoever maintains the templates —
    # "This page is replaced with taxonomy \"faq\" from templates/faq/list.html".
    # No template renders it, so its typography is nobody's concern, and the
    # strings it quotes are identifiers that must stay as they are.
    if re.search(r"templates/\S+\.html", src_body) and "replaced with taxonomy" in src_body:
        return problems

    # 1. Structure must match the source exactly — unless the page says it
    #    deliberately does not. A few translations are not renderings of the
    #    English page but their own edition of it: the Russian homepage runs a
    #    volunteer-recruitment section English has never had and rewrites the
    #    community list around its own chats. Reporting that forever as
    #    "structure" errors trains people to ignore the check, and worse, it
    #    hides real losses behind noise that is known to be fine.
    #
    #    Declaring it costs a sentence in the page's own frontmatter:
    #
    #        extra:
    #          translation_diverges: "Carries a volunteer section English lacks."
    #
    #    The reason is mandatory — an empty flag does nothing — so the
    #    exemption cannot be added silently. Only the structural comparison is
    #    waived. Everything that catches actual damage still runs: lost brands,
    #    translated anchors, spliced alphabets, orphaned links, leftover XML
    #    tags and register.
    diverges = (out_meta.get("extra") or {}).get("translation_diverges")
    a, b = fingerprint(src_body), fingerprint(out_body)
    localised = _localised_refs(src_body, out_body, lang)
    b["ref_links"] -= sum(localised.values())
    for key in ([] if isinstance(diverges, str) and diverges.strip() else a):
        if a[key] == b[key]:
            continue
        detail = ""
        if key in ("ref_links", "inline_links"):
            if key == "ref_links":
                pat = r"\]\[([^\]]+)\]"
                src_ids = Counter(re.findall(pat, src_body))
                out_ids = Counter(re.findall(pat, out_body)) - localised
            else:
                src_ids = _inline_targets(src_body)
                out_ids = _inline_targets(out_body)
            missing = sorted((src_ids - out_ids).elements())
            extra = sorted((out_ids - src_ids).elements())
            bits = []
            if missing:
                bits.append(f"missing {missing[:6]}")
            if extra:
                bits.append(f"extra {extra[:6]}")
            detail = "; ".join(bits)
        elif key == "blocks":
            kind = lambda t: Counter(
                "bullet" if b.lstrip().startswith(("-", "*", "+")) else
                "heading" if b.lstrip().startswith("#") else
                "html" if b.lstrip().startswith("<") else "paragraph"
                for b in re.split(r"\n\s*\n", t) if b.strip())
            ks, ko = kind(src_body), kind(out_body)
            detail = ", ".join(f"{k}: {ko[k] - ks[k]:+d}"
                               for k in sorted(set(ks) | set(ko)) if ks[k] != ko[k])
        problems.append(Problem(
            ERROR, "structure",
            f"{key}: source has {a[key]}, translation has {b[key]}", detail))

    # 2. Leftover machinery from the XML round-trip.
    leftover = re.findall(r"</?x>|</?[abis]\d+>", out_body)
    if leftover:
        problems.append(Problem(
            ERROR, "leftover-tags",
            f"{len(leftover)} untranslated placeholder tag(s) remain",
            ", ".join(sorted(set(leftover))[:8])))

    # 2b. Heading anchors are identifiers, not prose. A translated anchor
    #     silently breaks every link that points at it — Estonian had turned
    #     `{#engines}` into `{#mootorid}` while the other 31 languages kept it,
    #     so every inbound link to that section died for Estonian readers only.
    src_anchors = set(re.findall(r"\{#([^}\s]+)\}", src_body))
    out_anchors = set(re.findall(r"\{#([^}\s]+)\}", out_body))
    invented = sorted(out_anchors - src_anchors)
    if invented:
        problems.append(Problem(
            ERROR, "anchor-translated",
            f"{len(invented)} heading anchor(s) differ from the source",
            ", ".join(f"{{#{a}}}" for a in invented[:6])
            + (f" (source has {', '.join(sorted(src_anchors)[:4])})"
               if src_anchors else "")))

    # 3. Bracket integrity, per link rather than per line: an earlier well-formed
    #    link on the same line must not mask a later one that lost its "[".
    for lineno, line in enumerate(out_body.split("\n"), 1):
        depth = 0
        i = 0
        while i < len(line):
            c = line[i]
            if c == "\\":
                i += 2
                continue
            if c == "[":
                depth += 1
            elif c == "]":
                if depth:
                    depth -= 1
                elif i + 1 < len(line) and line[i + 1] in "([":
                    problems.append(Problem(
                        ERROR, "orphan-link",
                        f"line {lineno}: link markup with no opening '['",
                        line[max(0, i - 30):i + 40].strip()))
            i += 1

    # 4. A word character glued onto a link's closing paren: the translator put
    #    a suffix outside the label, as in "[تبرعات](url)كم". Skipped for
    #    scripts that do not separate words with spaces, where text following a
    #    link immediately is completely normal. A warning rather than an error:
    #    Indic and Turkic case markers land here routinely and human reviewers
    #    have accepted them, so it is a polish issue, not a correctness one.
    if lang not in NO_SPACE_SCRIPTS:
        for m in re.finditer(r"\]\([^)]*\)(\w+)", out_body):
            problems.append(Problem(
                WARN, "suffix-outside-link",
                f"'{m.group(1)}' is attached after a link instead of inside it",
                out_body[max(0, m.start() - 30):m.end() + 10].strip()))

    # 5. Attributions must stay at the end of their bullet.
    for line in out_body.split("\n"):
        if re.match(r"[ \t]*[-*+][ \t]", line) and "_(" in line:
            if not line.rstrip().endswith(")_"):
                problems.append(Problem(
                    ERROR, "attribution-moved",
                    "bullet contains an attribution but does not end with it",
                    line.strip()[:100]))

    # 5b. Contributor names inside _(...)_ are people's names and must stay in
    #     Latin script. Indic translations were found transliterating them
    #     (Alexander Borsuk rendered in Devanagari), which the attribution
    #     count alone cannot detect.
    for m in re.finditer(r"_\(([^)\n]+)\)_", out_body):
        name = m.group(1)
        letters = [c for c in name if c.isalpha()]
        if letters and not any(_script(c) == "LATIN" for c in letters):
            problems.append(Problem(
                ERROR, "attribution-transliterated",
                f"contributor name '{name}' is not in Latin script"))

    # 5c. Every contributor name the English source credits must still appear,
    #     in Latin, somewhere in the translation. Catches names transliterated
    #     in plain "(Name)" parens and inside "[Name](url)" link labels, which
    #     the attribution check above cannot see.
    # Only credit positions count: "_(Name)_", a "(Name)" closing a bullet, or
    # a "-- Name" sign-off. A "[Label](url)" link label looks identical but is
    # meant to be translated ("Our GitHub", "British Pound GBP"), so bracketed
    # text is excluded.
    NAME = r"[A-Z][\w.'-]+(?: [A-Z][\w.'-]+){1,3}"
    src_names = set()
    for pat in (rf"_\(({NAME})\)_",
                rf"\(_({NAME})_\)",
                rf"(?<!\])\(({NAME})\)[ \t]*$",
                rf"(?m)--[ \t]*({NAME})[ \t]*$"):
        src_names.update(re.findall(pat, src_body, re.M))
    for name in sorted(src_names):
        if name not in out_body:
            problems.append(Problem(
                ERROR, "contributor-name-lost",
                f"contributor '{name}' from the source does not appear here"))

    # 5d. The product name translated into local words. Distinct from
    #     brand-lost: the page may also use the Latin form elsewhere, so a
    #     count check cannot see it.
    pat = TRANSLATED_BRAND.get(lang)
    if pat and not (lang in TRANSLATED_BRAND_EXEMPT
                    and TRANSLATED_BRAND_EXEMPT[lang][0] in src_body):
        found = re.findall(pat, out_body, re.IGNORECASE)
        if found:
            problems.append(Problem(
                ERROR, "brand-translated",
                f"the product name appears translated {len(found)}x, not as "
                f"'Organic Maps'",
                str(sorted({f if isinstance(f, str) else " ".join(f)
                            for f in found})[:3])))

    # 6. Brands: same count, Latin, and never wrapped in quotes.
    exempt = BRAND_TRANSLITERATING.get(lang, set())
    if exempt is not None:
        for brand in BRANDS:
            if brand in exempt:
                continue
            n_src, n_out = src_body.count(brand), out_body.count(brand)
            if n_src and n_out < n_src:
                problems.append(Problem(
                    ERROR, "brand-lost",
                    f"'{brand}' appears {n_src}x in source but {n_out}x here",
                ))
    # The two marks must actually pair. Turkish writes the shipped label
    # "OpenStreetMap'e Yer Ekle", where the apostrophe attaches the case suffix
    # and the quotes belong to the whole label, not to the brand.
    for brand in BRANDS:
        if any(re.search(f"{re.escape(o)}{re.escape(brand)}{re.escape(c)}", out_body)
               for o, c in QUOTE_PAIRS):
            problems.append(Problem(
                WARN, "brand-quoted",
                f"'{brand}' is wrapped in quotation marks"))

    # 7. Words spliced from two alphabets.
    mixed = mixed_script_words(out_body)
    if mixed:
        problems.append(Problem(
            ERROR, "mixed-script",
            f"{len(mixed)} word(s) mix two alphabets",
            ", ".join(sorted(set(mixed))[:8])))

    # 8. Register.
    ok, msg = register_ok(out_body, lang)
    if not ok:
        problems.append(Problem(WARN, "register", msg))

    # 9. Untranslated frontmatter fields.
    if out_meta:
        src_meta = strip_frontmatter(src)[1]
        for key in ("title", "description"):
            if (isinstance(src_meta.get(key), str)
                    and src_meta.get(key) == out_meta.get(key)
                    and src_meta[key].strip()):
                problems.append(Problem(
                    WARN, "untranslated-frontmatter",
                    f"'{key}' is identical to the English source"))

    # 10. Straight ASCII quotes where the language wants its own marks — but
    #     only in prose. HTML attributes, shortcode arguments, code spans and
    #     markdown link titles all *require* a straight quote, so warning about
    #     them asks for something that would break the page. The Russian
    #     homepage was warned on nothing but its sponsor table's `width="200"`.
    prose = re.sub(r"(?s)<[^>]+>", " ", out_body)
    prose = re.sub(r"\{\{[^}]*\}\}", " ", prose)
    prose = re.sub(r"`[^`\n]*`", " ", prose)
    prose = re.sub(r"\]\([^)\s]+\s+\"[^\"]*\"\)", "]()", prose)
    # Only worth saying where we know what the language wants instead. Hebrew,
    # Italian and Turkish have no pair defined in QUOTES, and Hebrew in
    # particular uses the straight mark by convention — warning there asks for
    # a change with no target. That alone was 104 of the 562 warnings.
    if QUOTE_FOR.get(lang) and re.search(r'(?<![\w=])"[^"\n]{1,120}"', prose):
        problems.append(Problem(
            WARN, "ascii-quotes",
            "straight \" quotes present; use the language's native marks"))

    # 10b. Emphasis that will not close, so the markers show on the page.
    for fault in emphasis_faults(out_body):
        problems.append(Problem(ERROR, "emphasis-broken", fault))

    # 11. Ellipsis style, in prose only. GitHub's compare URLs put `...`
    #     between two refs, and a code span may contain it literally.
    if "..." in _checkable(out_body):
        problems.append(Problem(WARN, "ellipsis", "'...' should be '…'"))

    return problems


# ---------------------------------------------------------------------- CLI

def _lang_of(path: Path) -> str | None:
    m = re.search(r"\.([a-zA-Z-]+)\.md$", path.name)
    return m.group(1) if m else None


def check_folder(folder: Path, errors_only: bool = False) -> int:
    src_path = folder / "index.md"
    if not src_path.is_file():
        print(f"Error: no index.md in {folder}", file=sys.stderr)
        return 2
    src = src_path.read_text(encoding="utf-8")

    n_err = n_warn = n_clean = 0
    for path in sorted(folder.glob("index.*.md")):
        lang = _lang_of(path)
        if not lang:
            continue
        problems = check_translation(src, path.read_text(encoding="utf-8"), lang)
        if errors_only:
            problems = [p for p in problems if p.level == ERROR]
        errs = sum(p.level == ERROR for p in problems)
        n_err += errs
        n_warn += len(problems) - errs
        if not problems:
            n_clean += 1
            continue
        print(f"\n{path.name}  ({lang})")
        for p in problems:
            print(p)

    print(f"\n{'='*66}")
    print(f"{n_clean} clean, {n_err} error(s), {n_warn} warning(s)")
    return 1 if n_err else 0


def check_all(errors_only: bool = True) -> int:
    """Sweep every translated page that has an English sibling."""
    import glob
    n = bad = 0
    for f in sorted(glob.glob("content/**/*.md", recursive=True)):
        p = Path(f)
        m = re.search(r"\.([a-zA-Z-]+)\.md$", p.name)
        if not m:
            continue
        base = p.parent / ("_index.md" if p.name.startswith("_index") else "index.md")
        if not base.is_file():
            continue
        # news date folders carry template-only _index stubs with no prose
        if p.name.startswith("_index") and "/news/" in f and p.parent.name != "news":
            continue
        n += 1
        problems = check_translation(base.read_text(encoding="utf-8"),
                                     p.read_text(encoding="utf-8"), m.group(1))
        if errors_only:
            problems = [x for x in problems if x.level == ERROR]
        if problems:
            bad += 1
            print(f"\n{f}")
            for x in problems:
                print(x)
    print(f"\n{'='*66}\n{n - bad}/{n} pages clean")
    return 1 if bad else 0


def main() -> None:
    ap = argparse.ArgumentParser(description="Validate machine translations.")
    ap.add_argument("target", type=Path, nargs="?", help="folder, or the English source")
    ap.add_argument("translated", type=Path, nargs="?")
    ap.add_argument("lang", nargs="?")
    ap.add_argument("--errors-only", action="store_true")
    ap.add_argument("--all", action="store_true",
                    help="check every translated page in content/")
    ap.add_argument("--syntax", nargs="*", metavar="FILE",
                    help="language-independent syntax only, on the given files "
                         "or all of content/; covers the English source too, "
                         "which --all never sees because it has no source to "
                         "compare against")
    args = ap.parse_args()

    if args.syntax is not None:
        paths = ([Path(p) for p in args.syntax] if args.syntax
                 else sorted(Path("content").rglob("*.md")))
        bad = 0
        for path in paths:
            body, _ = strip_frontmatter(path.read_text(encoding="utf-8"))
            for fault in emphasis_faults(body):
                print(f"{path}: {fault}")
                bad += 1
        print(f"\n{bad} emphasis fault(s) in {len(paths)} file(s)")
        sys.exit(1 if bad else 0)

    if args.all:
        sys.exit(check_all(args.errors_only))

    if args.target is None:
        ap.error("pass a target, or --all")

    if args.target.is_dir():
        sys.exit(check_folder(args.target, args.errors_only))

    if not args.translated or not args.lang:
        print("Error: pass a folder, or source + translation + language.",
              file=sys.stderr)
        sys.exit(2)

    problems = check_translation(
        args.target.read_text(encoding="utf-8"),
        args.translated.read_text(encoding="utf-8"),
        args.lang)
    if args.errors_only:
        problems = [p for p in problems if p.level == ERROR]
    for p in problems:
        print(p)
    errs = sum(p.level == ERROR for p in problems)
    print(f"\n{errs} error(s), {len(problems) - errs} warning(s)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
