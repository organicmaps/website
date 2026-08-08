#!/usr/bin/env python3
"""Manage the Organic Maps DeepL glossary.

The term pairs live in translation_glossary.tsv (the source of truth). This
module uploads them to DeepL, caches the resulting glossary ID, and hands it to
any script that wants to translate with project terminology.

WHY ONE GLOSSARY FOR ALL LANGUAGES
The DeepL API Free plan permits exactly ONE stored glossary, so the obvious
"one glossary per language" layout is impossible — the second create returns
456 "Too many glossaries". The v3 API allows a single *multilingual* glossary
holding one dictionary per language pair, which fits the one-glossary quota and
covers every language at once. Its ID works in ordinary v2 /translate calls;
DeepL picks the dictionary matching the request's target_lang.

Usage:
    python3 deepl_glossary.py sync            # build/refresh the glossary
    python3 deepl_glossary.py sync ru de      # only these languages
    python3 deepl_glossary.py list            # what DeepL currently holds
    python3 deepl_glossary.py check           # verify it changes output
    python3 deepl_glossary.py probe           # find unsupported languages
    python3 deepl_glossary.py clean           # delete it

From another script:
    from deepl_glossary import get_glossary_id
    gid = get_glossary_id("ru")
    if gid:
        params += [("glossary_id", gid), ("source_lang", "EN")]

Environment:
    DEEPL_FREE_API_KEY - DeepL API key
"""

import json
import os
import unicodedata
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
GLOSSARY_FILE = SCRIPT_DIR / "translation_glossary.tsv"
CACHE_FILE = SCRIPT_DIR / ".deepl_glossaries.json"
HOST = "https://api-free.deepl.com"
GLOSSARY_NAME = "om-glossary"

# Site language suffix -> DeepL dictionary target language code.
DICT_LANG = {
    "ar": "ar", "cs": "cs", "de": "de", "el": "el", "es": "es", "et": "et",
    "fr": "fr", "he": "he", "hu": "hu", "id": "id", "it": "it", "ja": "ja",
    "lt": "lt", "nl": "nl", "pl": "pl", "pt": "pt", "pt-BR": "pt",
    "ru": "ru", "sv": "sv", "tr": "tr", "uk": "uk", "zh-Hans": "zh",
}

# Site suffix -> DeepL translation target, for /translate calls.
DEEPL_TARGET = {
    "fa-IR": "FA", "pt": "PT-PT", "pt-BR": "PT-BR", "zh-Hans": "ZH-HANS",
}


def get_key() -> str:
    key = os.environ.get("DEEPL_FREE_API_KEY")
    if not key:
        print("Error: set DEEPL_FREE_API_KEY.", file=sys.stderr)
        sys.exit(1)
    return key


def jreq(path: str, payload=None, method: str | None = None):
    """JSON request against the v3 API. Returns (data, error_string)."""
    req = urllib.request.Request(
        HOST + path,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={
            "Authorization": f"DeepL-Auth-Key {get_key()}",
            "Content-Type": "application/json",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read()
        return (json.loads(body) if body else {}), None
    except urllib.error.HTTPError as e:
        return None, f"{e.code} {e.read().decode(errors='replace')[:400]}"


def translate(texts, target, glossary_id=None, extra=None):
    """v2 /translate helper, so callers need only this module."""
    data = [("target_lang", target), ("source_lang", "EN")]
    data += [("text", t) for t in texts]
    if glossary_id:
        data.append(("glossary_id", glossary_id))
    data += extra or []
    req = urllib.request.Request(
        HOST + "/v2/translate",
        data=urllib.parse.urlencode(data).encode(),
        headers={
            "Authorization": f"DeepL-Auth-Key {get_key()}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return [t["text"] for t in json.load(r)["translations"]], None
    except urllib.error.HTTPError as e:
        return None, f"{e.code} {e.read().decode(errors='replace')[:300]}"


def load_repairs() -> dict[str, dict[str, str]]:
    """Post-translation output fixes: {site_lang: {wrong: right}}.

    Rows marked "repair" in the 4th column. Unlike glossary terms these match
    translated text, not English, and exist to undo known translator defects.
    """
    repairs: dict[str, dict[str, str]] = {}
    if not GLOSSARY_FILE.is_file():
        return repairs
    for raw in GLOSSARY_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("\t")]
        if len(parts) == 4 and parts[3] == "repair":
            repairs.setdefault(parts[1], {})[parts[0]] = parts[2]
    return repairs


def get_repairs(site_lang: str) -> dict[str, str]:
    """Known output defects to fix for a language."""
    return load_repairs().get(site_lang, {})


def apply_repairs(text: str, site_lang: str) -> str:
    """Apply the known output repairs for a language."""
    for wrong, right in get_repairs(site_lang).items():
        text = text.replace(wrong, right)
    return text


def load_terms() -> dict[str, dict[str, str]]:
    """Parse translation_glossary.tsv into {site_lang: {source: target}}."""
    if not GLOSSARY_FILE.is_file():
        print(f"Error: {GLOSSARY_FILE.name} not found.", file=sys.stderr)
        sys.exit(1)

    terms: dict[str, dict[str, str]] = {}
    for lineno, raw in enumerate(
        GLOSSARY_FILE.read_text(encoding="utf-8").splitlines(), 1
    ):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) == 4 and parts[3].strip() == "repair":
            continue  # handled by load_repairs()
        if len(parts) != 3:
            print(
                f"Warning: {GLOSSARY_FILE.name}:{lineno} expected 3 "
                f"tab-separated fields, got {len(parts)} — skipped.",
                file=sys.stderr,
            )
            continue
        source, lang, target = (p.strip() for p in parts)
        bucket = terms.setdefault(lang, {})
        if source in bucket:
            print(
                f"Warning: {GLOSSARY_FILE.name}:{lineno} duplicate source "
                f"{source!r} for {lang} — later entry wins.",
                file=sys.stderr,
            )
        bucket[source] = target
    return terms


def load_cache() -> dict:
    if CACHE_FILE.is_file():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def get_glossary_id(site_lang: str) -> str | None:
    """Glossary ID to use for a site language, or None if it has no dictionary.

    Callers should treat None as "translate without a glossary", not an error.
    Run `deepl_glossary.py sync` to populate the cache.
    """
    cache = load_cache()
    if site_lang in cache.get("languages", []):
        return cache.get("glossary_id")
    return None


def glossary_languages() -> list[str]:
    """Site languages covered by the synced glossary."""
    return load_cache().get("languages", [])


def find_ours() -> dict | None:
    listed, err = jreq("/v3/glossaries")
    if err:
        print(f"Error listing glossaries: {err}", file=sys.stderr)
        return None
    for g in listed.get("glossaries", []):
        if g.get("name") == GLOSSARY_NAME:
            return g
    return None


def _same_but_for_accents(a: str, b: str) -> bool:
    strip = lambda s: "".join(
        c for c in unicodedata.normalize("NFD", s.lower())
        if unicodedata.category(c) != "Mn")
    return strip(a) == strip(b)


def split_uploadable(terms, langs):
    """Partition terms into what DeepL can hold and what must be applied locally.

    Glossary dictionaries are keyed by BASE language code, so regional variants
    (pt / pt-BR) share one dictionary and cannot disagree. The PRIMARY variant
    (the one whose site code equals the base code) supplies the shared entry;
    each other variant gets a target->target fix turning the primary's term into
    its own. That works because the glossary makes the primary's term appear
    deterministically — unlike an English->target mapping, which cannot be
    applied after the fact since you do not know which wrong word to replace.

    Returns (dictionaries, variant_fixes, review_terms):
      variant_fixes  {lang: {primary_term: variant_term}}  auto-applicable
      review_terms   {lang: {english: target}}             guidance only, for
                     languages with no glossary support at all
    """
    variant_fixes: dict[str, dict[str, str]] = {}
    review_terms: dict[str, dict[str, str]] = {}
    by_code: dict[str, list[str]] = {}
    for lang in langs:
        if not terms.get(lang):
            continue
        if lang not in DICT_LANG:
            review_terms[lang] = dict(terms[lang])
            continue
        by_code.setdefault(DICT_LANG[lang], []).append(lang)

    dicts = []
    for code, group in sorted(by_code.items()):
        primary = next((l for l in group if l == code), sorted(group)[0])
        merged = dict(terms[primary])
        for lang in group:
            if lang == primary:
                continue
            for src, mine in terms[lang].items():
                theirs = merged.get(src)
                if theirs and theirs != mine:
                    # Only auto-apply when the two forms differ by diacritics
                    # ("metro"/"metrô"). A gender or stem change cannot be
                    # substituted safely: swapping pt "trilho" for pt-BR
                    # "trilha" leaves the article behind, giving "nos trilhas".
                    if _same_but_for_accents(theirs, mine):
                        variant_fixes.setdefault(lang, {})[theirs] = mine
                    else:
                        review_terms.setdefault(lang, {})[src] = mine
                elif not theirs:
                    merged[src] = mine
        if merged:
            dicts.append({
                "source_lang": "en",
                "target_lang": code,
                "entries": "\n".join(f"{s}\t{t}" for s, t in sorted(merged.items())),
                "entries_format": "tsv",
            })
    return dicts, variant_fixes, review_terms


def get_variant_fixes(site_lang: str) -> dict[str, str]:
    """Target->target fixes for a regional variant sharing a base dictionary."""
    return load_cache().get("variant_fixes", {}).get(site_lang, {})


def get_review_terms(site_lang: str) -> dict[str, str]:
    """English->target terms the glossary cannot enforce, for the review pass."""
    return load_cache().get("review_terms", {}).get(site_lang, {})


def sync(langs: list[str] | None = None) -> None:
    terms = load_terms()
    targets = langs or sorted(terms)
    dicts, variant_fixes, review_terms = split_uploadable(terms, targets)
    if not dicts:
        print("Nothing to upload.", file=sys.stderr)
        sys.exit(1)

    # The Free plan holds one glossary, so the old one must go before the new
    # one is created. Only ever delete our own.
    existing = find_ours()
    if existing:
        _, err = jreq(f"/v3/glossaries/{existing['glossary_id']}", method="DELETE")
        if err:
            print(f"Error deleting old glossary: {err}", file=sys.stderr)
            sys.exit(1)
        print(f"Removed previous {GLOSSARY_NAME} ({existing['glossary_id']})")

    created, err = jreq(
        "/v3/glossaries", {"name": GLOSSARY_NAME, "dictionaries": dicts}
    )
    if err:
        print(f"\nFAILED to create glossary: {err}", file=sys.stderr)
        if "Quota" in err or "Too many" in err:
            print(
                "\nThe DeepL Free plan stores only one glossary and another one "
                "is occupying the slot. Run 'deepl_glossary.py list' to see it.",
                file=sys.stderr,
            )
        else:
            print(
                "\nOne of the dictionaries may use an unsupported language. "
                "Run 'deepl_glossary.py probe' to find which.",
                file=sys.stderr,
            )
        sys.exit(1)

    covered = []
    print(f"Created {GLOSSARY_NAME} ({created['glossary_id']})")
    by_target = {d["target_lang"].lower(): d for d in created.get("dictionaries", [])}
    for lang in targets:
        if lang not in terms or lang not in DICT_LANG:
            continue
        d = by_target.get(DICT_LANG[lang].lower())
        if d:
            covered.append(lang)
            extra = (f"  +{len(variant_fixes[lang])} variant fixes"
                     if lang in variant_fixes else "")
            print(f"  {lang:8s} -> {d['target_lang']:4s} "
                  f"{d.get('entry_count'):3d} entries{extra}")
        else:
            print(f"  {lang:8s} -> DROPPED by DeepL", file=sys.stderr)

    if review_terms:
        print("\nNo DeepL glossary support — terms flagged for the review pass:")
        for lang in sorted(review_terms):
            print(f"  {lang:8s} {len(review_terms[lang])} term(s)")

    CACHE_FILE.write_text(
        json.dumps(
            {
                "glossary_id": created["glossary_id"],
                "languages": sorted(covered),
                "variant_fixes": {k: v for k, v in sorted(variant_fixes.items())},
                "review_terms": {k: v for k, v in sorted(review_terms.items())},
            },
            indent=2, sort_keys=True, ensure_ascii=False,
        ) + "\n",
        encoding="utf-8",
    )
    print(f"\nCached in {CACHE_FILE.name}: {len(covered)} glossary language(s), "
          f"{len(variant_fixes)} with variant fixes")


def cmd_list() -> None:
    listed, err = jreq("/v3/glossaries")
    if err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)
    gs = listed.get("glossaries", [])
    if not gs:
        print("No glossaries stored. Run: deepl_glossary.py sync")
        return
    for g in gs:
        mine = " (ours)" if g.get("name") == GLOSSARY_NAME else ""
        print(f"{g['name']}{mine}  {g['glossary_id']}")
        for d in g.get("dictionaries", []):
            print(f"    {d['source_lang']} -> {d['target_lang']:6s} "
                  f"{d.get('entry_count')} entries")


def cmd_probe() -> None:
    """Create each language's dictionary alone to find unsupported ones."""
    terms = load_terms()
    existing = find_ours()
    if existing:
        print("Delete the current glossary first: deepl_glossary.py clean",
              file=sys.stderr)
        sys.exit(1)

    ok, bad = [], []
    for lang in sorted(terms):
        dicts = dictionaries_for(terms, [lang])
        created, err = jreq("/v3/glossaries",
                            {"name": f"probe-{lang}", "dictionaries": dicts})
        if err:
            bad.append((lang, err))
            print(f"  {lang:8s} REJECTED: {err}")
            continue
        ok.append(lang)
        print(f"  {lang:8s} ok ({DICT_LANG[lang]})")
        jreq(f"/v3/glossaries/{created['glossary_id']}", method="DELETE")

    print(f"\n{len(ok)} supported, {len(bad)} rejected")
    if bad:
        print("Rejected:", ", ".join(l for l, _ in bad))


def cmd_check(langs: list[str] | None = None) -> None:
    cache = load_cache()
    gid = cache.get("glossary_id")
    if not gid:
        print("No glossary cached. Run: deepl_glossary.py sync")
        return
    terms = load_terms()
    probe = "Bookmarks and tracks can now be edited on the route screen."
    targets = langs or cache.get("languages", [])

    changed = same = 0
    for lang in targets:
        target = DEEPL_TARGET.get(lang, lang.upper())
        without, e1 = translate([probe], target)
        with_, e2 = translate([probe], target, glossary_id=gid)
        if e1 or e2:
            print(f"  {lang:8s} FAILED: {e1 or e2}", file=sys.stderr)
            continue
        differs = without[0] != with_[0]
        changed += differs
        same += not differs
        print(f"\n  {lang:8s} [{'changed' if differs else 'same'}] "
              f"({len(terms.get(lang, {}))} entries)")
        print(f"    without: {without[0]}")
        print(f"    with   : {with_[0]}")

    print(f"\n{changed} language(s) changed by the glossary, {same} unchanged.")
    if same:
        print("'same' just means DeepL already produced the glossary term.")


def cmd_clean() -> None:
    listed, err = jreq("/v3/glossaries")
    if err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)
    n = 0
    for g in listed.get("glossaries", []):
        if g.get("name") == GLOSSARY_NAME or g.get("name", "").startswith("probe-"):
            jreq(f"/v3/glossaries/{g['glossary_id']}", method="DELETE")
            print(f"  deleted {g['name']}")
            n += 1
    if CACHE_FILE.is_file():
        CACHE_FILE.unlink()
        print(f"  removed {CACHE_FILE.name}")
    print(f"Removed {n} glossary/ies.")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "sync":
        sync(args or None)
    elif cmd == "list":
        cmd_list()
    elif cmd == "check":
        cmd_check(args or None)
    elif cmd == "probe":
        cmd_probe()
    elif cmd == "clean":
        cmd_clean()
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
