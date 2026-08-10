#!/usr/bin/env python3
"""Proofread a machine translation: fix register, terminology and defects.

DeepL cannot produce the informal second person for most languages — doing so
means rewriting verb morphology, not swapping a pronoun — and it drifts from
project terminology in ways a glossary cannot always catch. This module hands
the draft to an LLM with the source, the expected register, the language's
glossary and the concrete findings from translate_check, and asks for a
corrected version.

The result is validated before it is accepted: if the review introduces a
structural error the draft did not have, the draft is kept and the failure is
reported. A proofreader that breaks markdown is worse than none.

    from translate_review import review_translation
    fixed, note = review_translation(src_md, translated_md, "tr")

Usage:
    python3 tools/translate_review.py source.md translated.md tr          # in place
    python3 tools/translate_review.py <folder>                            # every lang
    python3 tools/translate_review.py <folder> --langs tr,uk --dry-run

Requires the `claude` CLI on PATH.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

from translate_check import check_translation, ERROR
from translate_md import expected_register, detect_register
from deepl_glossary import load_terms, get_review_terms

MODEL_TIMEOUT = 300


def build_prompt(src: str, out: str, lang: str) -> str:
    problems = check_translation(src, out, lang)
    want = expected_register(lang)
    got = detect_register(out, lang)[0]
    terms = load_terms().get(lang, {})
    review_terms = get_review_terms(lang)

    lines = [
        f"You are proofreading a machine translation of an Organic Maps post "
        f"into {lang}. Correct it. Do not retranslate from scratch.",
        "",
        "## Rules, in priority order",
        "",
        "1. PRESERVE STRUCTURE EXACTLY. Same number of lines, bullets, "
        "headings, links, and `_(Contributor Name)_` attributions as the "
        "English source. Never translate, reorder or reformat a URL, a link "
        "target, a `{{ shortcode }}`, a `code span`, or a contributor name.",
        "2. Every `_(Name)_` attribution stays at the END of its bullet.",
        "3. Keep these product names in Latin script, unquoted: Organic Maps, "
        "OpenStreetMap, ID Editor, Android, iOS, Google Play, App Store, "
        "F-Droid.",
        "4. Use the language's native quotation marks, and `…` rather than "
        "`...`.",
    ]

    if want == "formal":
        lines.append(
            f"5. REGISTER: address the reader with the POLITE/FORMAL second "
            f"person throughout ({lang} uses the V-form: Russian вы, "
            f"Ukrainian ви, Belarusian вы), with matching verb forms. Be "
            f"consistent — never mix registers."
        )
    elif want == "informal":
        lines.append(
            "5. REGISTER: address the reader with the INFORMAL/familiar "
            "second person throughout (the T-form), with matching verb "
            "morphology — not just the pronoun. Convert every reader-facing "
            "statement and imperative. Leave first-person 'we' and "
            "third-person description alone. Never mix registers."
        )
        if got == "formal":
            lines.append(
                "   The draft is currently FORMAL. This is the main thing to "
                "fix."
            )
        elif got == "mixed":
            lines.append(
                "   The draft MIXES both registers. Make it consistently "
                "informal."
            )

    if terms:
        lines += ["", "## Required terminology (English -> " + lang + ")"]
        lines += [f"  {en} -> {tgt}" for en, tgt in sorted(terms.items())
                  if en[0].islower()][:40]
    if review_terms:
        lines += ["", "## Terminology the glossary could not enforce — apply it"]
        lines += [f"  {en} -> {tgt}" for en, tgt in sorted(review_terms.items())]

    if problems:
        lines += ["", "## Problems detected automatically in this draft"]
        lines += [f"  [{p.level}] {p.code}: {p.message}" for p in problems]

    lines += [
        "",
        "## English source",
        "```markdown", src.rstrip(), "```",
        "",
        f"## Draft translation ({lang}) — correct this",
        "```markdown", out.rstrip(), "```",
        "",
        "Return ONLY the corrected markdown file, complete, with no commentary "
        "and no code fence around it. If the draft is already correct, return "
        "it unchanged.",
    ]
    return "\n".join(lines)


def _strip_fence(text: str) -> str:
    text = text.strip()
    m = re.match(r"^```[a-zA-Z]*\n([\s\S]*?)\n```$", text)
    return m.group(1) if m else text


def review_translation(src: str, out: str, lang: str,
                       timeout: int = MODEL_TIMEOUT) -> tuple[str, str]:
    """Proofread one translation. Returns (text, note).

    The draft is returned unchanged whenever the review cannot be trusted:
    the CLI failed, the output was empty, or it introduced a structural error
    the draft did not already have.
    """
    prompt = build_prompt(src, out, lang)
    try:
        proc = subprocess.run(
            ["claude", "-p"], input=prompt, capture_output=True,
            text=True, timeout=timeout)
    except FileNotFoundError:
        return out, "claude CLI not found"
    except subprocess.TimeoutExpired:
        return out, f"timed out after {timeout}s"

    if proc.returncode != 0:
        return out, f"claude exited {proc.returncode}: {proc.stderr.strip()[:120]}"

    fixed = _strip_fence(proc.stdout)
    if not fixed.strip():
        return out, "empty response"

    before = {(p.code, p.message) for p in check_translation(src, out, lang)
              if p.level == ERROR}
    after = [p for p in check_translation(src, fixed, lang) if p.level == ERROR]
    introduced = [p for p in after if (p.code, p.message) not in before]
    if introduced:
        return out, ("rejected: review introduced "
                     + "; ".join(f"{p.code}: {p.message}" for p in introduced[:3]))

    if fixed.strip() == out.strip():
        return out, "no change needed"
    return fixed, f"corrected ({len(after)} error(s) remain)"


def _lang_of(path: Path) -> str | None:
    m = re.search(r"\.([a-zA-Z-]+)\.md$", path.name)
    return m.group(1) if m else None


def main() -> None:
    ap = argparse.ArgumentParser(description="Proofread machine translations.")
    ap.add_argument("target", type=Path, help="folder, or the English source")
    ap.add_argument("translated", type=Path, nargs="?")
    ap.add_argument("lang", nargs="?")
    ap.add_argument("--langs", help="comma-separated subset, folder mode only")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the prompt instead of calling the model")
    args = ap.parse_args()

    if args.target.is_dir():
        src_path = args.target / "index.md"
        if not src_path.is_file():
            print(f"Error: no index.md in {args.target}", file=sys.stderr)
            sys.exit(2)
        src = src_path.read_text(encoding="utf-8")
        only = (
            {language.strip() for language in args.langs.split(",")}
            if args.langs
            else None
        )
        paths = [p for p in sorted(args.target.glob("index.*.md"))
                 if _lang_of(p) and (not only or _lang_of(p) in only)]
    else:
        if not args.translated or not args.lang:
            print("Error: pass a folder, or source + translation + language.",
                  file=sys.stderr)
            sys.exit(2)
        src = args.target.read_text(encoding="utf-8")
        paths = [args.translated]

    changed = 0
    for path in paths:
        lang = _lang_of(path) or args.lang
        out = path.read_text(encoding="utf-8")
        if args.dry_run:
            print(build_prompt(src, out, lang))
            continue
        fixed, note = review_translation(src, out, lang)
        if fixed != out:
            path.write_text(fixed, encoding="utf-8")
            changed += 1
        print(f"  {lang:8s} {note}")

    if not args.dry_run:
        print(f"\n{changed}/{len(paths)} file(s) changed.")


if __name__ == "__main__":
    main()
