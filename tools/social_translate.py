#!/usr/bin/env python3
"""Translate a post.toml slide script into the site's languages.

    python3 tools/social_translate.py social/2026-07-23-620 --telegram
    python3 tools/social_translate.py social/2026-07-23-620 --langs ru,de
    python3 tools/social_translate.py social/2026-07-23-620 --telegram --dry-run

Writes post.<lang>.toml next to post.toml. Only prose is translated — slide
types, themes, device names, media paths, badge names and the short URL are
identifiers and stay verbatim, the same rule the site's markdown translations
follow for slugs and anchors.

Runs through the same DeepL path as translate_md.py, so the terminology
glossary, the formality preference per language and the tidy-up passes
(native quotes, unquoted brands, ellipsis) all apply.

Environment:
    DEEPL_FREE_API_KEY
"""

import argparse
import copy
import sys
from pathlib import Path

from deepl_glossary import DEEPL_TARGET, get_glossary_id
from deepl_glossary import translate as deepl_translate
from markdown_xml import from_xml, to_xml
from social_post import (
    PostError,
    dump_post,
    load_post,
    post_path,
    set_field,
    text_fields,
)
from translate_md import (
    BATCH,
    FORMALITY_SUPPORTED,
    brands_visible,
    formality_pref,
    register_ok,
    site_languages,
    telegram_languages,
    tidy,
)

# A translation this much longer than its English source will have its type
# shrunk by the renderer's auto-fit. That is not a failure, but a title that
# doubles in length usually reads better rewritten by hand than set smaller.
LENGTH_WARN_RATIO = 1.5
LENGTH_WARN_MIN_CHARS = 25


def collect(post: dict) -> list[tuple[int, str, int | None, str]]:
    """Every translatable string in the post, as (slide index, key, i, text)."""
    found = []
    for slide_index, slide in enumerate(post["slides"]):
        for key, item_index, value in text_fields(slide):
            found.append((slide_index, key, item_index, value))
    return found


def translate_strings(values: list[str], lang: str,
                      use_glossary: bool = True) -> list[str]:
    """Translate short prose strings, one payload each.

    Field values are translated individually rather than as one document —
    the same treatment translate_md.py gives frontmatter titles, since a slide
    title is a fragment and gains nothing from surrounding context.
    """
    payloads, ctxs = [], []
    for value in values:
        payload, ctx = to_xml(value, protect_brands=not brands_visible(lang))
        payloads.append(payload)
        ctxs.append(ctx)

    target = DEEPL_TARGET.get(lang, lang.upper())
    extra = [("tag_handling", "xml"), ("ignore_tags", "x")]
    if target in FORMALITY_SUPPORTED:
        extra.append(("formality", formality_pref(lang)))
    gid = get_glossary_id(lang) if use_glossary else None

    out: list[str] = []
    for i in range(0, len(payloads), BATCH):
        chunk, err = deepl_translate(
            payloads[i:i + BATCH], target, glossary_id=gid, extra=extra
        )
        if err:
            raise RuntimeError(f"DeepL failed for {lang}: {err}")
        out.extend(chunk)

    return [tidy(from_xml(res, ctx), lang) for res, ctx in zip(out, ctxs)]


def translate_post_toml(post: dict, lang: str,
                        use_glossary: bool = True) -> tuple[dict, list[str]]:
    """Return a translated copy of the post plus any warnings about it."""
    translated = copy.deepcopy(post)
    translated["lang"] = lang

    fields = collect(post)
    if not fields:
        return translated, []

    results = translate_strings([f[3] for f in fields], lang, use_glossary)

    warnings: list[str] = []
    for (slide_index, key, item_index, english), result in zip(fields, results):
        set_field(translated["slides"][slide_index], key, item_index, result)
        if (
            len(english) >= LENGTH_WARN_MIN_CHARS
            and len(result) > len(english) * LENGTH_WARN_RATIO
        ):
            warnings.append(
                f"slide {slide_index + 1} {key}: "
                f"{len(result)} chars vs {len(english)} in English — "
                f"the renderer will shrink the type"
            )

    joined = "\n".join(
        value for slide in translated["slides"]
        for _, _, value in text_fields(slide)
    )
    ok, message = register_ok(joined, lang)
    if not ok:
        warnings.append(message)

    return translated, warnings


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("post_dir", type=Path, help="folder holding post.toml")
    ap.add_argument("--langs", help="comma-separated language codes")
    ap.add_argument("--telegram", action="store_true",
                    help="the languages that have Telegram channels")
    ap.add_argument("--all", action="store_true",
                    help="every language in config.toml")
    ap.add_argument("--dry-run", action="store_true",
                    help="show the budget, call nothing")
    ap.add_argument("--no-glossary", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="overwrite existing post.<lang>.toml files")
    args = ap.parse_args()

    post_dir = args.post_dir.resolve()
    source = post_path(post_dir, "en")
    if not source.is_file():
        raise SystemExit(f"no post.toml in {post_dir}")

    if args.langs:
        langs = [s.strip() for s in args.langs.split(",") if s.strip()]
    elif args.telegram:
        langs = telegram_languages()
    elif args.all:
        langs = [lang for lang in site_languages() if lang != "en"]
    else:
        raise SystemExit("pass --langs, --telegram or --all.")

    try:
        post = load_post(source)
    except PostError as e:
        raise SystemExit(f"Error: {e}") from e

    fields = collect(post)
    chars = sum(len(f[3]) for f in fields)
    print(f"Source:    {source}")
    print(f"Strings:   {len(fields)} across {len(post['slides'])} slide(s), "
          f"{chars} chars each language")
    print(f"Languages: {len(langs)} -> {', '.join(langs)}")
    print(f"Budget:    ~{chars * len(langs):,} DeepL characters total")
    print(f"Glossary:  {'off' if args.no_glossary else 'on'}")
    if not args.no_glossary and not any(get_glossary_id(lang) for lang in langs):
        # Without it "bookmarks" comes back as закладки rather than метки, and
        # nothing downstream would ever say so.
        print("           WARNING: no glossary is uploaded for any of these "
              "languages.\n           Run: python3 tools/deepl_glossary.py sync")
    print()

    if args.dry_run:
        print("[DRY RUN] nothing sent. Strings:")
        for _, key, _, value in fields[:8]:
            print(f"  {key}: {value}")
        return

    failures: list[str] = []
    for i, lang in enumerate(langs, 1):
        dest = post_path(post_dir, lang)
        if dest.is_file() and not args.force:
            print(f"  [{i}/{len(langs)}] {lang:8s} exists, skipped "
                  f"(--force to overwrite)")
            continue
        try:
            translated, warnings = translate_post_toml(
                post, lang, use_glossary=not args.no_glossary
            )
        except RuntimeError as e:
            print(f"  [{i}/{len(langs)}] {lang:8s} FAILED: {e}", file=sys.stderr)
            failures.append(lang)
            continue

        dest.write_text(dump_post(translated), encoding="utf-8")
        note = f"  [{len(warnings)} warning(s)]" if warnings else ""
        gid = "" if args.no_glossary or get_glossary_id(lang) else " (no glossary)"
        print(f"  [{i}/{len(langs)}] {lang:8s} -> {dest.name}{gid}{note}")
        for warning in warnings:
            print(f"        {warning}")

    print(f"\n{len(langs) - len(failures)}/{len(langs)} translated.")
    print("Review the copy, then render:\n"
          f"  python3 tools/social_build.py {args.post_dir} --all-langs")
    if failures:
        print(f"Failed: {', '.join(failures)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
