#!/usr/bin/env python3
"""Round-trip tests for markdown_xml. No network, no API keys.

Acceptance: from_xml(*to_xml(md)) == md, byte for byte, for every markdown
file in the repository and for every hand-written construct case.

Usage: python3 tmp/test_xml_roundtrip.py [-v]
"""
import glob
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from markdown_xml import to_xml, from_xml  # noqa: E402
from markdown_frontmatter import strip_frontmatter  # noqa: E402

VERBOSE = "-v" in sys.argv
passed = failed = 0
failures: list[tuple[str, str]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    global passed, failed
    if ok:
        passed += 1
        if VERBOSE:
            print(f"  PASS  {label}")
    else:
        failed += 1
        failures.append((label, detail))
        print(f"  FAIL  {label}")
        if detail:
            print(detail)


def roundtrip(md: str) -> tuple[bool, str]:
    try:
        payload, ctx = to_xml(md)
        back = from_xml(payload, ctx)
    except Exception as e:  # noqa: BLE001 - report, don't crash the suite
        return False, f"        raised {type(e).__name__}: {e}"
    if back == md:
        return True, ""
    for i, (a, b) in enumerate(zip(md.splitlines(), back.splitlines())):
        if a != b:
            return False, (f"        line {i+1}\n"
                           f"        in : {a[:120]!r}\n"
                           f"        out: {b[:120]!r}")
    return False, (f"        length {len(md)} -> {len(back)}\n"
                   f"        tail in : {md[-80:]!r}\n"
                   f"        tail out: {back[-80:]!r}")


# ------------------------------------------------------- construct unit tests
print("=" * 70)
print("Construct unit tests")
print("=" * 70)

CASES = {
    "inline link": "See [the docs](https://organicmaps.app/docs) now.",
    "reference link": "Get it on [Google Play][googleplay] today.",
    "link definition": "[googleplay]: https://play.google.com/x \"Google Play\"",
    "autolink": "Visit <https://organicmaps.app> for more.",
    "bare url": "Mirror at https://cdn.organicmaps.app/file_a.zip ok.",
    "image": "![A screenshot](/images/shot.png) above.",
    "code span": "Use the `--dry-run` flag.",
    "fenced code": "```python\nprint('hi')\n```",
    "shortcode": "{{ references() }}",
    "bold": "This is **very** important.",
    "italic underscore": "This is _subtle_ emphasis.",
    "italic star": "This is *subtle* emphasis.",
    "bold italic": "This is ***loud*** emphasis.",
    "strikethrough": "This is ~~gone~~ now.",
    "attribution": "- Fixed a crash _(Kiryl Kaveryn)_",
    "heading": "## Detailed changelog",
    "bullet": "- Added a new icon",
    "numbered": "1. Open the app",
    "blockquote": "> A quoted line",
    "table": "| a | b |",
    "raw html br": "✅ No ads<br/>\n✅ No tracking<br/>",
    "raw html pre": "<pre>text</pre>",
    "escaped chars": r"Literal \*not bold\* and \[not a link\].",
    "brands": "Organic Maps uses OpenStreetMap on Android and iOS.",
    "snake_case not italic": "The flag is do_not_translate here.",
    "math not italic": "Compute 3*4 and 5*6 values.",
    "ampersand": "Organic Maps is an Android & iOS offline maps app",
    "angle brackets": "Compare a < b and c > d values.",
    "two links one line": "[one](https://a.example) then [two](https://b.example)",
    "escaped brackets in label": r"[\[matrix\]](https://omaps.app/matrix)",
    "url with underscores": "See https://wiki.osm.org/wiki/About_OpenStreetMap fine.",
    "url with ampersand": "Go https://x.example/t?_x_tr_sl=ru&_x_tr_tl=en now.",
    "link inside bold": "**See [the docs](https://a.example) now**",
    "bold inside link": "[**bold label**](https://a.example)",
    "empty": "",
    "plain": "Just a sentence with no markup at all.",
    "multiline": "Para one.\n\nPara two.\n\n- bullet\n- bullet\n",
}

for name, md in CASES.items():
    ok, detail = roundtrip(md)
    check(name, ok, detail)

# ------------------------------------------------------------ safety checks
print()
print("=" * 70)
print("Safety and structural checks")
print("=" * 70)

# Placeholder collision must be refused loudly, not silently corrupted.
try:
    to_xml("text with a literal <x>0</x> in it")
    check("literal <x> in input raises", False, "        no exception raised")
except ValueError:
    check("literal <x> in input raises", True)

# Everything that must never reach the translator.
NEVER_TRANSLATED = {
    "url": ("See [docs](https://organicmaps.app/a_b) now.", "https://organicmaps.app/a_b"),
    "code": ("Use `--dry-run` now.", "--dry-run"),
    "shortcode": ("{{ references() }}", "references()"),
    "attribution": ("- Fixed _(Kiryl Kaveryn)_", "Kiryl Kaveryn"),
    "brand": ("Organic Maps is great", "Organic Maps"),
    "html": ("No ads<br/>", "<br/>"),
    "list marker": ("- Added an icon", "- "),
}
for name, (md, must_be_hidden) in NEVER_TRANSLATED.items():
    payload, _ = to_xml(md)
    check(f"{name} kept out of payload", must_be_hidden not in payload,
          f"        payload: {payload!r}")

# Link labels MUST stay translatable — that is the point of <a> over <x>.
payload, _ = to_xml("Read [the full changelog](https://a.example) here.")
check("link label stays translatable", "the full changelog" in payload,
      f"        payload: {payload!r}")
payload, _ = to_xml("This is **very important** today.")
check("bold content stays translatable", "very important" in payload,
      f"        payload: {payload!r}")

# The payload must be valid XML — a bare & is an HTTP 400 from DeepL for every
# language, which is the failure this check exists to prevent.
for name, md in CASES.items():
    payload, _ = to_xml(md)
    try:
        ElementTree.fromstring(f"<root>{payload}</root>")
        ok, detail = True, ""
    except ElementTree.ParseError as e:
        ok, detail = False, f"        {e}\n        payload: {payload[:160]!r}"
    check(f"valid XML: {name}", ok, detail)

# Stash indices must each be referenced exactly once.
for name, md in CASES.items():
    payload, ctx = to_xml(md)
    used = [int(i) for i in re.findall(r"<x>(\d+)</x>", payload)]
    ok = sorted(used) == sorted(set(used)) and set(used) <= set(range(len(ctx.stash)))
    check(f"stash integrity: {name}", ok,
          f"        used={used} stash={len(ctx.stash)}")

# --------------------------------------------------------- payload purity
# Round-trip alone proves reversibility, NOT correct classification: a URL
# misclassified as italic still restores perfectly, because the wrapper stores
# its original delimiters. What actually matters is that nothing untranslatable
# reaches the translator. This is the check with teeth.
print()
print("=" * 70)
print("Payload purity — what DeepL would actually see")
print("=" * 70)

_TAG = re.compile(r"<x>\d+</x>|</?[a-z]+\d+>")

FORBIDDEN = [
    ("a URL", re.compile(r"https?://|www\.")),
    ("a markdown link", re.compile(r"\]\(|\]\[")),
    ("a code span", re.compile(r"`")),
    ("a shortcode", re.compile(r"\{\{|\}\}")),
    ("bold markers", re.compile(r"\*\*")),
    ("strikethrough markers", re.compile(r"~~")),
    ("an attribution", re.compile(r"_\([^)]*\)_")),
    ("raw HTML", re.compile(r"&lt;/?(?:br|pre|sdk|div|span|img|table)\b")),
    ("a list marker", re.compile(r"(?m)^[ \t]*[-*+][ \t]+")),
    ("a heading marker", re.compile(r"(?m)^[ \t]*#{1,6}[ \t]+")),
    ("a brand name", re.compile("|".join(
        re.escape(b) for b in ["Organic Maps", "OpenStreetMap", "ID Editor",
                               "Google Play", "App Store", "F-Droid"]))),
]


def translatable_text(payload: str) -> str:
    """Only the text DeepL is asked to translate.

    Tags collapse to \\x00, not a space: a space would make "<x>Organic Maps</x>
    - це…" look like a line-initial list marker and report a false leak.
    """
    return _TAG.sub("\x00", payload)


def purity_problems(md: str) -> list[str]:
    payload, _ = to_xml(md)
    text = translatable_text(payload)
    return [name for name, rx in FORBIDDEN if rx.search(text)]


PURITY_CASES = {
    "url in link": "See [the docs](https://organicmaps.app/a_b) now.",
    "bare url": "Mirror at https://cdn.organicmaps.app/f_a.zip ok.",
    "autolink": "Visit <https://organicmaps.app> now.",
    "code span": "Use the `--dry-run` flag.",
    "shortcode": "{{ references() }}",
    "attribution": "- Fixed a crash _(Kiryl Kaveryn)_",
    "brand": "Organic Maps uses OpenStreetMap data.",
    "raw html": "✅ No ads<br/>",
    "bullet": "- Added a new icon",
    "heading": "## Detailed changelog",
    "bold": "This is **very** important.",
    "reference link": "Get it on [Google Play][googleplay].",
    "escaped bracket label": r"[\[matrix\]](https://omaps.app/matrix)",
}
for name, md in PURITY_CASES.items():
    probs = purity_problems(md)
    check(f"purity: {name}", not probs,
          f"        payload leaks {', '.join(probs)}\n"
          f"        payload: {to_xml(md)[0]!r}")


# ------------------------------------------------------- tagging structure
# Purity regexes catch content that leaks *as itself*, but not misclassification:
# a lost attribution becomes "<i0>(Kiryl Kaveryn)</i0>", which has no underscores
# left to detect while the name is now translatable. These assert the exact tag
# each construct must produce.
print()
print("=" * 70)
print("Tagging structure — each construct maps to the right kind of tag")
print("=" * 70)

EXACT = {
    "attribution is fully protected": ("_(Kiryl Kaveryn)_", "<x>0</x>"),
    "autolink is fully protected": ("<https://organicmaps.app>", "<x>0</x>"),
    "code span is fully protected": ("`--dry-run`", "<x>0</x>"),
    "shortcode is fully protected": ("{{ references() }}", "<x>0</x>"),
    "brand is fully protected": ("Organic Maps", "<x>0</x>"),
    "image is fully protected": ("![alt](/a.png)", "<x>0</x>"),
    "bare url is fully protected": ("https://a.example/x", "<x>0</x>"),
    "raw html is fully protected": ("<br/>", "<x>0</x>"),
    "email autolink is protected": ("<sdk@organicmaps.app>", "<x>0</x>"),
    "bold becomes a wrapper": ("**loud**", "<b0>loud</b0>"),
    "italic becomes a wrapper": ("_soft_", "<i0>soft</i0>"),
    "strike becomes a wrapper": ("~~gone~~", "<s0>gone</s0>"),
    "link becomes a wrapper": ("[label](https://a.example)", "<a0>label</a0>"),
    "ref link becomes a wrapper": ("[label][id]", "<a0>label</a0>"),
}
for name, (md, expected) in EXACT.items():
    payload, _ = to_xml(md)
    check(name, payload == expected,
          f"        expected {expected!r}\n        got      {payload!r}")

NO_TAGS = {
    "snake_case is not emphasis": "do_not_translate",
    "arithmetic is not emphasis": "3*4 and 5*6",
    "plain prose has no tags": "Just a normal sentence.",
    "mid-word underscore": "some_var and other_var",
}
for name, md in NO_TAGS.items():
    payload, _ = to_xml(md)
    check(name, "<" not in payload,
          f"        payload: {payload!r}")


# ------------------------------------------------------------ corpus sweep
print()
print("=" * 70)
print("Repository corpus round-trip")
print("=" * 70)

files = sorted(
    glob.glob("content/**/*.md", recursive=True)
    + glob.glob("templates/shortcodes/*.md")
)
by_ext: dict[str, list[int]] = {}
bad_files: list[str] = []
n_ok = 0

for path in files:
    raw = Path(path).read_text(encoding="utf-8")
    body, _ = strip_frontmatter(raw)
    ok, detail = roundtrip(body)
    # Purity is a property of the translation SOURCE. Already-translated files
    # legitimately inflect brands (Estonian "OpenStreetMapi", Hungarian
    # "Organic Mapsot"), so only English files are held to it.
    is_source = not re.search(r"\.[a-zA-Z-]+\.md$", path)
    probs = purity_problems(body) if (ok and is_source) else []
    if probs:
        ok = False
        detail = f"        payload leaks {', '.join(probs)}"
    lang = re.search(r"\.([a-zA-Z-]+)\.md$", path)
    key = lang.group(1) if lang else "en"
    tally = by_ext.setdefault(key, [0, 0])
    tally[0] += 1
    if ok:
        n_ok += 1
        tally[1] += 1
    else:
        bad_files.append(path)
        if len(bad_files) <= 8:
            print(f"  FAIL  {path}")
            print(detail)

print(f"\n  {n_ok}/{len(files)} files round-trip exactly AND keep the payload clean")
if bad_files:
    print(f"  {len(bad_files)} failing; first 8 shown above")
    worst: dict[str, int] = {}
    for p in bad_files:
        lang = re.search(r"\.([a-zA-Z-]+)\.md$", p)
        worst[lang.group(1) if lang else "en"] = worst.get(
            lang.group(1) if lang else "en", 0) + 1
    print("  by language: " + ", ".join(
        f"{k}:{v}" for k, v in sorted(worst.items(), key=lambda x: -x[1])[:12]))
else:
    langs = len(by_ext)
    print(f"  covering {langs} language variants")

check("whole corpus round-trips", not bad_files,
      f"        {len(bad_files)} file(s) differ")

print()
print("=" * 70)
print(f"{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
