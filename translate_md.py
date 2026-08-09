#!/usr/bin/env python3
"""Translate a markdown file into any of the site's languages with DeepL.

Combines the three pieces built for this:
  markdown_xml.py   markdown <-> XML so formatting survives translation
  deepl_glossary.py project terminology, local terms and output repairs
  this module       segmentation, DeepL calls, and the tidy-up passes

Works on any markdown — a Telegram post with no frontmatter, a site article, a
monthly release note — so the same tool serves all of them.

Usage:
    python3 translate_md.py post.md --langs ru,de,fr
    python3 translate_md.py post.md --telegram -o tmp/tg-post/
    python3 translate_md.py content/news/2026-08-04/630/index.md --all
    python3 translate_md.py post.md --langs ru --dry-run

Options:
    --langs a,b,c   explicit language list
    --telegram      the languages that have Telegram channels
    --all           every language configured in config.toml
    -o DIR          write into DIR (default: next to the source)
    --dry-run       show what would be translated, call nothing
    --no-glossary   translate without project terminology (for comparison)

Environment:
    DEEPL_FREE_API_KEY
"""

import argparse
import re
import sys
from pathlib import Path

from markdown_xml import to_xml, from_xml
from deepl_glossary import (
    translate as deepl_translate,
    get_glossary_id,
    get_variant_fixes,
    apply_repairs,
    DEEPL_TARGET,
)
from telegram_post import strip_frontmatter

SCRIPT_DIR = Path(__file__).resolve().parent
BATCH = 45  # DeepL accepts 50 text params per request

# DeepL supports a formality preference for these targets only; the rest need
# the review pass.
FORMALITY_SUPPORTED = {"DE", "ES", "FR", "IT", "NL", "PL", "PT-PT", "PT-BR",
                       "RU", "JA"}

# CLAUDE.md requires the informal second person everywhere EXCEPT these, which
# address the reader politely (ru вы, uk ви, be вы). Maintainer decision.
#
# hi/mr/te/ml/fa-IR are formal for a different reason: in these languages the
# polite form is the UNMARKED way to address an adult stranger, not a stiff
# alternative to a warm one. Hindi आप, Marathi तुम्ही, Telugu మీరు, Malayalam
# നിങ്ങൾ and Persian شما are what every consumer app uses; the familiar forms
# (तुम/तू, तू, నువ్వు, നീ, تو) are for children, intimates and subordinates, so
# a product using them reads as condescending rather than friendly. Organic
# Maps' own app strings already agree: hi 73 formal vs 1 informal marker,
# mr 29 vs 0, fa 49 vs 0 in data/strings/strings.txt.
FORMAL_LANGUAGES = {"ru", "uk", "be", "hi", "mr", "te", "ml", "fa-IR",
                    "cs", "lt"}


def expected_register(lang: str) -> str:
    """The register a translation of `lang` is supposed to use."""
    if lang not in REGISTER_MARKERS:
        return "n-a"
    return "formal" if lang in FORMAL_LANGUAGES else "informal"


def formality_pref(lang: str) -> str:
    return "prefer_more" if lang in FORMAL_LANGUAGES else "prefer_less"

# Purely mechanical register fixes, safe ONLY for languages where the polite
# form is a bare pronoun swap with no verb agreement to follow. Chinese and
# Indonesian qualify; every other formal language needs verb morphology
# rewritten, which is the review pass's job — see REGISTER_MARKERS.
REGISTER_FIXES = {
    "zh-Hans": [("您的", "你的"), ("您", "你")],
    "id": [("Anda", "kamu")],
}

# Formal / informal second-person markers per language, for detecting register
# rather than changing it. Used by the validation gate to flag drafts that came
# back polite, and to catch texts that mix both registers in one post.
REGISTER_MARKERS = {
    "af": (r"\bu\b|\bU\b", r"\bjy\b|\bjou\b|\bJy\b"),
    "ca": (r"\bvostè\b|\bvós\b", r"\btu\b|\bteu\b|\bteva\b"),
    "cs": (r"\bvy\b|\bVy\b|\bváš|\bvaše|\bvám\b|\bvás\b|ete\b", r"\bty\b|\btvůj|\btvo|eš\b"),
    "cy": (r"\bchi\b|\bchwi\b|\beich\b", r"\bti\b|\bdy\b|\bdi\b"),
    "de": (r"\bSie\b|\bIhre?[nmrs]?\b|\bIhnen\b", r"\bdu\b|\bDu\b|\bdein|\bdir\b|\bdich\b"),
    "el": (r"\bεσείς\b|\bσας\b|είτε\b", r"\bεσύ\b|\bσου\b|εις\b"),
    "es": (r"\busted\b|\bUsted\b", r"\btú\b|\btu\b|\btus\b|\bti\b"),
    # "teid" is the partitive plural of "tee" (road) as often as it is the
    # pronoun — "ei saa lisada teid, järvi" is "cannot add roads, lakes" — and
    # \bteie\b already covers the pronoun stem. The informal side needs the
    # capitalised forms or a sentence-initial "Sinu" reads as register-free.
    "et": (r"\bteie\b|\bTeie\b|\bteil\w*\b|\bteie\w+\b",
           r"\b[Ss]ina\b|\b[Ss]inu\b|\b[Ss]a\b|\b[Ss]ind\b"),
    # Bare "شما" also matches شماره (number) and شمالی (northern).
    # Persian marks the informal register on the verb as often as on the
    # pronoun, so the 2sg endings are listed too: without them a post whose
    # only informality is "بپیوند"/"کنی" reads as register-free.
    "fa-IR": (r"(?<![ؠ-ۓ])شما(?![ؠ-ۓ])",
              r"(?<![ؠ-ۓ])(?:تو|کنی|توانی|بتوانی|بپیوند|بدهی|باشی)(?![ؠ-ۓ])"),
    "fr": (r"\bvous\b|\bvotre\b|\bvos\b", r"\btu\b|\bton\b|\bta\b|\btes\b|\bt'"),
    "gl": (r"\bvostede\b", r"\bti\b|\bteu\b|\btúa\b"),
    # Indic scripts cannot use \b: Python classifies vowel signs and the
    # virama as non-word, so \bतुम्ही\b never matches the Marathi polite
    # pronoun at all, \bतू\b never matches तू but DOES match inside वस्तू,
    # धातू and मस्तूल, and "నీ " hits కానీ ("but"). These use explicit script
    # boundaries: a marker may not touch another letter of the same script.
    "hi": (r"(?<![ऀ-ॣ०-ॿ])आप(?:क[ोेाी]|न[ेा]|से|में)?(?![ऀ-ॣ०-ॿ])",
           r"(?<![ऀ-ॣ०-ॿ])(?:तुम|तुझ)|(?<![ऀ-ॣ०-ॿ])तू(?![ऀ-ॣ०-ॿ])"),
    # Hungarian marks the informal imperative with -d/-sd, which is how a text
    # ends up mixed: "szerkesztheti" (formal) beside "Töltsd le" (informal).
    "hu": (r"\bÖn\b|\bÖnök\b|\bÖnnek\b|heti\b|hatja\b", r"\bte\b|\bti\b|\bneked\b|hetsz\b|\w+sd\b|\w+dd\b"),
    "id": (r"\bAnda\b", r"\bkamu\b|\bmu\b"),
    "it": (r"\bLei\b|\bSuo\b|\bSua\b", r"\btu\b|\btuo|\btua|\bti\b"),
    "lt": (r"\bjūs\b|\bJūs\b|\bjūsų\b|kite\b", r"\btu\b|\btavo\b|\btave\b"),
    # Bare നീ / നീ- also begins നീല (blue), നീണ്ട (long), നീക്കം (removal).
    "ml": (r"(?<![ഀ-ൿ])(?:നിങ്ങ|താങ്ക)",
           r"(?<![ഀ-ൿ])(?:നിന്റെ|നിനക്ക|നിന്നെ|നിന്നോട)|(?<![ഀ-ൿ])നീ(?![ഀ-ൿ])"),
    "mr": (r"(?<![ऀ-ॣ०-ॿ])(?:तुम्ही|तुमच|तुम्हा|आपण|आपल)",
           r"(?<![ऀ-ॣ०-ॿ])(?:तुझ|तुला)|(?<![ऀ-ॣ०-ॿ])तू(?![ऀ-ॣ०-ॿ])"),
    "nl": (r"\bu\b|\bU\b|\buw\b", r"\bje\b|\bjij\b|\bjouw\b"),
    "oc": (r"\bvos\b|\bvòstre\b|\bvòstra\b", r"\btu\b|\bton\b|\bta\b"),
    "pl": (r"\bPan\b|\bPani\b|\bPaństw", r"\bty\b|\btwoj|\bcię\b|sz\b"),
    "pt": (r"\bvocê\b|\bvocês\b|\bo senhor\b", r"\btu\b|\bteu|\btua"),
    "pt-BR": (r"\bo senhor\b|\bvós\b", r"\bvocê\b|\bseu\b|\bsua\b"),
    "ru": (r"\bВы\b|\bвы\b|\bваш|\bвас\b|\bвам\b", r"\bты\b|\bтво|\bтебя\b|шь\b"),
    "sv": (r"\bni\b|\bNi\b|\ber\b", r"\bdu\b|\bDu\b|\bdin\b|\bdig\b"),
    # Bare నీ / నీ- also begins నీలం (blue), నీటి (water), నీడ (shade).
    "te": (r"(?<![ఀ-౿])(?:మీరు|మీకు|మీతో|మిమ్మల్ని)|(?<![ఀ-౿])మీ(?![ఀ-౿])",
           r"(?<![ఀ-౿])(?:నువ్వు|నీవు|నిన్ను|నీకు|నీతో)|(?<![ఀ-౿])నీ(?![ఀ-౿])"),
    "tr": (r"\bsiz\b|iniz\b|ınız\b|unuz\b|ünüz\b|yin\b|yın\b", r"\bsen\b|\bsenin\b|\bsana\b"),
    "uk": (r"\bВи\b|\bви\b|\bваш|\bвас\b", r"\bти\b|\bтво|єш\b|иш\b"),
    "zh-Hans": (r"您", r"你"),
}


def detect_register(text: str, lang: str) -> tuple[str, int, int]:
    """Classify second-person register as informal / formal / mixed / n-a.

    Returns (verdict, formal_hits, informal_hits). Languages with no T/V
    distinction (ar, he, eu, ja) report "n-a".
    """
    markers = REGISTER_MARKERS.get(lang)
    if not markers:
        return "n-a", 0, 0
    formal, informal = markers
    nf = len(re.findall(formal, text))
    ni = len(re.findall(informal, text))
    if nf and ni:
        return "mixed", nf, ni
    if nf:
        return "formal", nf, ni
    if ni:
        return "informal", nf, ni
    return "none", 0, 0


def register_ok(text: str, lang: str) -> tuple[bool, str]:
    """Does the text use the register this language is supposed to use?

    Returns (ok, message). "mixed" always fails: CLAUDE.md forbids switching
    register inside one text regardless of which register is expected.
    """
    want = expected_register(lang)
    got, nf, ni = detect_register(text, lang)
    if want == "n-a" or got in ("n-a", "none"):
        return True, f"{lang}: register not applicable"
    if got == "mixed":
        return False, f"{lang}: MIXED register (formal={nf}, informal={ni})"
    if got != want:
        return False, f"{lang}: {got} but should be {want}"
    return True, f"{lang}: {got} as expected"

# Brands are left VISIBLE to the translator wherever they survive as Latin,
# because hiding them behind placeholders wrecks word order ("OpenStreetMap
# Теперь включены данные…"). Glossary languages carry brand-lock entries that
# guarantee it; these extra ones were measured to keep brands Latin unaided.
BRAND_SAFE_WITHOUT_GLOSSARY = {"af", "ca", "cy", "eu", "gl", "oc", "mr"}
# Measured to transliterate brands (hi/ml 0 of 4 kept, te 1 of 4, fa-IR 3 of 4)
# and having no glossary to lock them, so they keep placeholder protection.
BRAND_MUST_HIDE = {"hi", "ml", "te", "fa-IR"}


def brands_visible(lang: str) -> bool:
    if lang in BRAND_MUST_HIDE:
        return False
    return bool(get_glossary_id(lang)) or lang in BRAND_SAFE_WITHOUT_GLOSSARY

BRANDS_TO_UNQUOTE = [
    "Organic Maps", "OpenStreetMap", "ID Editor", "Android", "iOS", "F-Droid",
    "Google Play", "App Store", "Obtainium", "Accrescent", "TestFlight",
]
QUOTE_CHARS = "\"'«»„“”‘’《》〈〉「」〔〕"

# Native quotation marks per CLAUDE.md.
QUOTES = {
    "«»": ["fr", "es", "ca", "gl", "el", "oc", "ru", "uk", "pt", "ar", "fa-IR",
           "eu"],
    "„“": ["de", "cs", "pl", "hu", "et", "lt"],
    "“”": ["nl", "sv", "pt-BR", "id", "hi", "mr", "ml", "te", "af",
           # Simplified Chinese uses “ ”; the corner brackets are
           # Traditional Chinese and Japanese. The corpus agrees, 55 to 5.
           "zh-Hans"],
    "「」": ["ja"],
    "‘’": ["cy"],
}
QUOTE_FOR = {lang: pair for pair, langs in QUOTES.items() for lang in langs}


def site_languages() -> list[str]:
    """Language codes configured in config.toml."""
    cfg = SCRIPT_DIR / "config.toml"
    if not cfg.is_file():
        return []
    return re.findall(r"^\[languages\.([A-Za-z-]+)\]",
                      cfg.read_text(encoding="utf-8"), re.M)


def telegram_languages() -> list[str]:
    from telegram_post_all import GROUPS, group_lang
    return [group_lang(f) for f in GROUPS.values() if group_lang(f) != "en"]


# --------------------------------------------------------------- tidy passes

def tidy(text: str, lang: str) -> str:
    """Repair the predictable damage a translator does to markdown."""
    # DeepL emits "[label ](url)" and "[ label](url)".
    text = re.sub(r"[  ]+\]\(", "](", text)
    text = re.sub(r"\[[  ]+", "[", text)

    # Punctuation dragged inside a link label: "[下载，](url)" -> "[下载](url)，"
    text = re.sub(r"\[([^\]]*?)([,.;:!?、，。；：！？])\]\(", r"[\1](", text)

    # The translator adds a space after the ignored list/heading marker token,
    # leaving "-  item" and "##  Heading".
    text = re.sub(r"(?m)^([ \t]*(?:[-*+]|#{1,6}|\d+\.))[ \t]{2,}", r"\1 ", text)

    # Brands must stay Latin AND unquoted.
    for brand in BRANDS_TO_UNQUOTE:
        text = re.sub(f"[{QUOTE_CHARS}]({re.escape(brand)})[{QUOTE_CHARS}]",
                      r"\1", text)

    text = text.replace("...", "…")

    # Straight ASCII quotes -> the language's own marks.
    pair = QUOTE_FOR.get(lang)
    if pair:
        text = re.sub(r'"([^"\n]{1,200})"', lambda m: f"{pair[0]}{m.group(1)}{pair[1]}",
                      text)

    # Register fixes preserve sentence-initial capitalisation, so replacing
    # Indonesian "Anda" with "kamu" does not leave a lowercase sentence start.
    for wrong, right in REGISTER_FIXES.get(lang, []):
        def _sub(m: re.Match, right=right) -> str:
            before = text[:m.start()].rstrip()
            starts = not before or before[-1] in ".!?:\n•"
            return right[:1].upper() + right[1:] if starts else right
        text = re.sub(re.escape(wrong), _sub, text)

    # Regional variants sharing a base dictionary: turn the primary variant's
    # term into this one's (pt "trilho" -> pt-BR "trilha").
    for primary, mine in get_variant_fixes(lang).items():
        text = re.sub(rf"\b{re.escape(primary)}\b", mine, text)

    return apply_repairs(text, lang)


def localize_zola_links(text: str, lang: str) -> str:
    """Point @/… links at the translated page when that page exists."""
    def repl(m: re.Match) -> str:
        target = m.group(1)
        if re.search(r"\.[a-zA-Z-]+\.md$", target):
            return m.group(0)  # already localized
        candidate = target[:-3] + f".{lang}.md"
        if (SCRIPT_DIR / "content" / candidate).is_file():
            return f"@/{candidate}"
        return m.group(0)

    return re.sub(r"@/([^)\s]+?\.md)", repl, text)


# ------------------------------------------------------------- the translator

def _segments(body: str, visible_brands: bool = True) -> tuple[list[str], list[tuple]]:
    """Split into translatable payloads plus a plan to rebuild the text."""
    payloads: list[str] = []
    plan: list[tuple] = []
    for line in body.split("\n"):
        if not line.strip():
            plan.append(("blank",))
            continue
        payload, ctx = to_xml(line, protect_brands=not visible_brands)
        # A line with nothing but protected spans needs no translation.
        if not re.sub(r"<x>\d+</x>|</?[a-z]+\d+>", "", payload).strip():
            plan.append(("verbatim", line))
            continue
        plan.append(("text", len(payloads), ctx))
        payloads.append(payload)
    return payloads, plan


def _rebuild(plan: list[tuple], translated: list[str], lang: str) -> str:
    out: list[str] = []
    for step in plan:
        if step[0] == "blank":
            out.append("")
        elif step[0] == "verbatim":
            out.append(step[1])
        else:
            _, idx, ctx = step
            out.append(tidy(from_xml(translated[idx], ctx), lang))
    return "\n".join(out)


def translate_text(body: str, lang: str, use_glossary: bool = True) -> str:
    """Translate markdown body text into `lang`, preserving all structure."""
    payloads, plan = _segments(body, brands_visible(lang))
    if not payloads:
        return body

    target = DEEPL_TARGET.get(lang, lang.upper())
    extra = [("tag_handling", "xml"), ("ignore_tags", "x")]
    if target in FORMALITY_SUPPORTED:
        extra.append(("formality", formality_pref(lang)))
    gid = get_glossary_id(lang) if use_glossary else None

    translated: list[str] = []
    for i in range(0, len(payloads), BATCH):
        chunk = payloads[i:i + BATCH]
        out, err = deepl_translate(chunk, target, glossary_id=gid, extra=extra)
        if err:
            raise RuntimeError(f"DeepL failed for {lang}: {err}")
        translated.extend(out)

    text = _rebuild(plan, translated, lang)
    return localize_zola_links(text, lang)


_FM_TRANSLATE = ("title", "description")


def translate_post(raw: str, lang: str, use_glossary: bool = True) -> str:
    """Translate a whole markdown file, frontmatter included if present."""
    body, meta = strip_frontmatter(raw)
    if not meta:
        return translate_text(raw, lang, use_glossary)

    # Translate only the human-facing fields; date/slug/taxonomies stay put.
    fields = [(k, meta[k]) for k in _FM_TRANSLATE
              if isinstance(meta.get(k), str) and meta[k].strip()]
    new_values = {}
    if fields:
        payloads, ctxs = [], []
        for _, value in fields:
            p, c = to_xml(value, protect_brands=not brands_visible(lang))
            payloads.append(p)
            ctxs.append(c)
        target = DEEPL_TARGET.get(lang, lang.upper())
        extra = [("tag_handling", "xml"), ("ignore_tags", "x")]
        if target in FORMALITY_SUPPORTED:
            extra.append(("formality", formality_pref(lang)))
        out, err = deepl_translate(
            payloads, target,
            glossary_id=get_glossary_id(lang) if use_glossary else None,
            extra=extra)
        if err:
            raise RuntimeError(f"DeepL failed for {lang} frontmatter: {err}")
        for (key, _), ctx, res in zip(fields, ctxs, out):
            new_values[key] = tidy(from_xml(res, ctx), lang)

    # Rewrite the frontmatter line-wise so unrelated fields keep their exact
    # formatting — round-tripping through a YAML dumper would reflow them.
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n", raw, re.DOTALL)
    fm_text = m.group(1)
    for key, value in new_values.items():
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        fm_text = re.sub(rf'(?m)^{key}:[ \t]*.*$', f'{key}: "{escaped}"',
                         fm_text, count=1)

    return f"---\n{fm_text}---\n\n" + translate_text(
        body.lstrip("\n"), lang, use_glossary)


# ---------------------------------------------------------------------- CLI

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path, help="English markdown file")
    ap.add_argument("--langs", help="comma-separated language codes")
    ap.add_argument("--telegram", action="store_true",
                    help="languages that have Telegram channels")
    ap.add_argument("--all", action="store_true",
                    help="every language in config.toml")
    ap.add_argument("-o", "--out", type=Path, help="output directory")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-glossary", action="store_true")
    ap.add_argument("--no-check", action="store_true",
                    help="skip validation of the result")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="show warnings as well as errors")
    args = ap.parse_args()

    if not args.source.is_file():
        print(f"Error: not a file: {args.source}", file=sys.stderr)
        sys.exit(1)

    if args.langs:
        langs = [l.strip() for l in args.langs.split(",") if l.strip()]
    elif args.telegram:
        langs = telegram_languages()
    elif args.all:
        langs = site_languages()
    else:
        print("Error: pass --langs, --telegram or --all.", file=sys.stderr)
        sys.exit(1)

    out_dir = args.out or args.source.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    raw = args.source.read_text(encoding="utf-8")
    stem = args.source.name[:-3] if args.source.name.endswith(".md") else args.source.stem

    body, meta = strip_frontmatter(raw)
    payloads, _ = _segments(body if meta else raw, brands_visible(langs[0]))
    chars = sum(len(p) for p in payloads)
    print(f"Source:    {args.source}")
    print(f"Frontmatter: {'yes' if meta else 'no'}"
          f"{' (title, description translated)' if meta else ''}")
    print(f"Segments:  {len(payloads)} line(s), ~{chars} chars each language")
    print(f"Languages: {len(langs)} -> {', '.join(langs)}")
    print(f"Budget:    ~{chars * len(langs):,} DeepL characters total")
    print(f"Glossary:  {'off' if args.no_glossary else 'on'}")
    print(f"Output:    {out_dir}/{stem}.<lang>.md\n")

    if args.dry_run:
        print("[DRY RUN] nothing sent. First 3 payloads:")
        for p in payloads[:3]:
            print(f"  {p[:150]}")
        return

    failures, blocked = [], []
    for i, lang in enumerate(langs, 1):
        dest = out_dir / f"{stem}.{lang}.md"
        try:
            result = translate_post(raw, lang, use_glossary=not args.no_glossary)
        except RuntimeError as e:
            print(f"  [{i}/{len(langs)}] {lang:8s} FAILED: {e}", file=sys.stderr)
            failures.append(lang)
            continue
        dest.write_text(result, encoding="utf-8")

        # Imported here, not at module scope: translate_check imports from this
        # module for the register helpers.
        from translate_check import check_translation
        problems = [] if args.no_check else check_translation(raw, result, lang)
        errs = [p for p in problems if p.level == "ERROR"]
        if errs:
            blocked.append(lang)

        gid = "" if args.no_glossary or get_glossary_id(lang) else " (no glossary)"
        note = ""
        if problems:
            note = f"  [{len(errs)} error, {len(problems)-len(errs)} warn]"
        print(f"  [{i}/{len(langs)}] {lang:8s} -> {dest.name}{gid}{note}")
        for p in problems if args.verbose else errs:
            print(f"        {p}".replace("\n", "\n    "))

    print(f"\n{len(langs) - len(failures)}/{len(langs)} translated.")
    if blocked:
        print(f"\n{len(blocked)} translation(s) have ERRORS and should not be "
              f"published as-is: {', '.join(blocked)}", file=sys.stderr)
        print(f"Inspect with: translate_check.py {args.source} "
              f"{out_dir}/{stem}.<lang>.md <lang>", file=sys.stderr)
    if failures:
        print(f"Failed: {', '.join(failures)}", file=sys.stderr)
        sys.exit(1)
    if blocked:
        sys.exit(1)


if __name__ == "__main__":
    main()
