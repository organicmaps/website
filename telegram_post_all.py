#!/usr/bin/env python3
"""
Post localized markdown content with optional media to multiple Telegram groups.

Usage:
    python telegram_post_all.py <path_to_content_folder> [--dry-run] [--yes]
    python telegram_post_all.py <folder> --only @OrganicMapsRu,de,zh-Hans
    python telegram_post_all.py <folder> --skip ru

The folder should contain markdown files like index.ru.md, index.fr.md, etc.
and optionally media files (images/videos) to attach to every post.

Posting stops at the first failure. Use --only with the channels listed in the
"Resume with" hint to continue without double-posting to channels that already
succeeded.

Environment:
    TELEGRAM_BOT_TOKEN - your bot token from @BotFather
"""

import argparse
import sys
from pathlib import Path

from telegram_post import (
    get_token,
    resolve_chat_id,
    send_text_messages,
    send_media_group,
    strip_frontmatter,
    load_references,
    resolve_references,
    find_unresolved_references,
    load_base_url,
    resolve_zola_references,
    ZOLA_FILENAME_RE,
)
import re

# Telegram group → markdown filename
GROUPS: dict[str, str] = {
    "@OrganicMapsApp": "index.md",
    "@OrganicMapsAR": "index.ar.md",
    "@OrganicMapsDeutsch": "index.de.md",
    "@OrganicMapsES": "index.es.md",
    "@OrganicMapsFR": "index.fr.md",
    "@OrganicMapsIT": "index.it.md",
    "@OrganicMapsPersian": "index.fa-IR.md",
    "@OrganicMapsPT": "index.pt.md",
    "@OrganicMapsRu": "index.ru.md",
    "@OrganicMapsTR": "index.tr.md",
    "@OrganicMapsUA": "index.uk.md",
    "@OrganicMapsZH": "index.zh-Hans.md",
}

MEDIA_EXTENSIONS = {".jpeg", ".jpg", ".png", ".webp", ".mp4", ".mp3", ".m4a"}


def group_lang(filename: str) -> str:
    """Language suffix of a content filename. 'index.zh-Hans.md' → 'zh-Hans'."""
    m = ZOLA_FILENAME_RE.match(filename)
    return (m.group("lang") if m else None) or "en"


def select_groups(only: str | None, skip: str | None) -> dict[str, str]:
    """Filter GROUPS by --only/--skip selectors.

    A selector is either a channel name (with or without '@', case-insensitive)
    or a language suffix such as 'ru' or 'zh-Hans'. Unknown selectors are a
    hard error: a typo in --skip would otherwise post to a channel you meant
    to leave out.
    """

    def parse(raw: str | None) -> list[str]:
        if not raw:
            return []
        return [s.strip() for s in raw.split(",") if s.strip()]

    aliases: dict[str, str] = {}
    for group, filename in GROUPS.items():
        aliases[group.lower()] = group
        aliases[group.lstrip("@").lower()] = group
        aliases[group_lang(filename).lower()] = group

    def resolve(selectors: list[str], flag: str) -> set[str]:
        resolved: set[str] = set()
        for sel in selectors:
            group = aliases.get(sel.lower())
            if group is None:
                known = ", ".join(sorted(group_lang(f) for f in GROUPS.values()))
                print(
                    f"Error: unknown {flag} selector '{sel}'.\n"
                    f"Use a channel name or one of: {known}",
                    file=sys.stderr,
                )
                sys.exit(1)
            resolved.add(group)
        return resolved

    keep = resolve(parse(only), "--only") if only else set(GROUPS)
    drop = resolve(parse(skip), "--skip")

    return {g: f for g, f in GROUPS.items() if g in keep and g not in drop}


def find_media(folder: Path) -> list[Path]:
    """Find all media files in the folder."""
    media = sorted(
        p
        for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in MEDIA_EXTENSIONS
    )
    return media


def prepare_text(md_path: Path, script_dir: Path) -> str:
    """Read markdown file, strip frontmatter, resolve references, clean up."""
    raw = md_path.read_text(encoding="utf-8")

    text, meta = strip_frontmatter(raw)
    title = meta.get("title", "")
    if title:
        text = f"**{title}**\n\n{text.lstrip()}"

    # Remove template shortcodes
    text = re.sub(r"^\s*\{\{.*?\}\}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\{\{.*?\}\}", "", text)

    # Strip angle brackets from bare URLs
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)

    # Clean up blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Resolve markdown reference-style links
    refs = load_references(script_dir)
    text = resolve_references(text, refs)

    # Resolve Zola @/-style internal references → absolute site URLs.
    base_url = load_base_url(script_dir)
    text, zola_unresolved = resolve_zola_references(text, script_dir, base_url)
    if zola_unresolved:
        print(
            f"Warning: {md_path.name} has "
            f"{len(zola_unresolved)} unresolved Zola @/-reference(s):",
            file=sys.stderr,
        )
        for target in zola_unresolved:
            print(f"  @/{target}", file=sys.stderr)

    return text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Post localized content to multiple Telegram groups."
    )
    parser.add_argument(
        "folder",
        type=Path,
        help="Path to folder with index.*.md files and optional media",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be posted without actually sending",
    )
    parser.add_argument(
        "--yes", "-y", action="store_true", help="Skip confirmation prompts"
    )
    parser.add_argument(
        "--only",
        help="Comma-separated channels or language codes to post to "
        "(e.g. '@OrganicMapsRu,de,zh-Hans'). Use this to resume after a failure.",
    )
    parser.add_argument(
        "--skip",
        help="Comma-separated channels or language codes to leave out",
    )
    parser.add_argument(
        "--allow-plain-fallback",
        action="store_true",
        help="If Telegram rejects the MarkdownV2 markup, post the message "
        "unformatted instead of aborting (default: abort)",
    )
    args = parser.parse_args()

    if not args.folder.is_dir():
        print(f"Error: not a directory: {args.folder}", file=sys.stderr)
        sys.exit(1)

    groups = select_groups(args.only, args.skip)
    if not groups:
        print("Error: no channels left after --only/--skip.", file=sys.stderr)
        sys.exit(1)

    # A dry run never talks to the API, so it must not require a token.
    token = "" if args.dry_run else get_token()
    script_dir = Path(__file__).resolve().parent

    # Discover media files
    media = find_media(args.folder)

    # Discover which groups have matching markdown files, and render each post
    # once — prepare_text() is not free and its warnings should print once.
    tasks: list[tuple[str, Path, str]] = []
    for group, filename in groups.items():
        md_path = args.folder / filename
        if md_path.is_file():
            tasks.append((group, md_path, prepare_text(md_path, script_dir)))

    if not tasks:
        print("No matching markdown files found in the folder.", file=sys.stderr)
        print(f"Expected filenames: {', '.join(groups.values())}")
        sys.exit(1)

    # Summary
    print(f"Folder: {args.folder}")
    print(f"Media:  {len(media)} file(s)")
    for m in media:
        print(f"  {m.name}")
    print(f"Posts:  {len(tasks)} group(s)")
    for group, md_path, _ in tasks:
        print(f"  {group} ← {md_path.name}")

    skipped = {fn for fn in groups.values()} - {t[1].name for t in tasks}
    if skipped:
        print(f"Skipped (file not found): {', '.join(sorted(skipped))}")
    excluded = set(GROUPS) - set(groups)
    if excluded:
        print(f"Excluded by --only/--skip: {', '.join(sorted(excluded))}")
    print()

    # Check for unresolved references in all files before posting
    has_warnings = False
    for group, md_path, text in tasks:
        unresolved = find_unresolved_references(text)
        if unresolved:
            has_warnings = True
            print(
                f"Warning: {md_path.name} has {len(unresolved)} "
                f"unresolved reference(s):",
                file=sys.stderr,
            )
            for match_text, ref_id, lineno in unresolved:
                print(
                    f"  line {lineno}: {match_text}  " f"(undefined id: {ref_id})",
                    file=sys.stderr,
                )

    if has_warnings and not args.yes:
        answer = input("\nContinue posting with unresolved references? [y/N] ").strip()
        if answer.lower() not in ("y", "yes"):
            print("Aborted.")
            sys.exit(0)

    if not args.yes and not args.dry_run:
        answer = input(f"Post to {len(tasks)} group(s)? [y/N] ").strip()
        if answer.lower() not in ("y", "yes"):
            print("Aborted.")
            sys.exit(0)

    # Resolve every chat up front. resolve_chat_id() exits on an unknown
    # channel, and doing that mid-run would leave a half-published post with
    # nothing posted yet, this is a safe abort.
    chat_ids: dict[str, str] = {}
    if not args.dry_run:
        print("Resolving channels...")
        for group, _, _ in tasks:
            chat_ids[group] = resolve_chat_id(token, group)

    def abort(message: str, remaining: list[str]) -> None:
        """Report a failure and show how to resume without double-posting."""
        print(f"\nFATAL: {message}", file=sys.stderr)
        if remaining:
            print(
                f"\nResume with:\n"
                f"  {sys.argv[0]} {args.folder} --only {','.join(remaining)}",
                file=sys.stderr,
            )
        sys.exit(1)

    # Post to each group
    for i, (group, md_path, text) in enumerate(tasks, 1):
        print(f"\n{'='*60}")
        print(f"[{i}/{len(tasks)}] {group} ← {md_path.name}")
        print(f"{'='*60}")

        # Channels not yet posted to, including the current one.
        remaining = [t[0] for t in tasks[i - 1 :]]

        if args.dry_run:
            print(
                f"  [DRY RUN] Would send text ({len(text)} chars)"
                f" + {len(media)} media file(s)"
            )
            continue

        chat_id = chat_ids[group]

        results = send_text_messages(
            token, chat_id, text, strict=not args.allow_plain_fallback
        )
        for result in results:
            if not result.get("ok"):
                desc = result.get("description", "unknown error")
                # A long post is several messages; if earlier ones already
                # landed, re-posting this channel would duplicate them.
                sent_ok = sum(1 for r in results if r.get("ok"))
                if sent_ok:
                    abort(
                        f"Failed to post to {group}: {desc}\n"
                        f"NOTE: {sent_ok} message(s) of this post already "
                        f"reached {group}; resuming it would duplicate them. "
                        f"Send the remainder by hand, then resume the rest.",
                        remaining[1:],
                    )
                abort(f"Failed to post to {group}: {desc}", remaining)
            if result.get("_markdown_fallback"):
                print(
                    f"  Warning: {group} was posted WITHOUT formatting.",
                    file=sys.stderr,
                )

        if media:
            media_result = send_media_group(token, chat_id, media)
            if not media_result.get("ok"):
                desc = media_result.get("description", "unknown error")
                # The text is already published, so resuming this channel would
                # duplicate it — only the media needs re-sending by hand.
                abort(
                    f"Failed to send media to {group}: {desc}\n"
                    f"NOTE: the text of {group} was posted successfully; "
                    f"do NOT include it when resuming.",
                    remaining[1:],
                )

        print(f"  Done: {group}")

    print(f"\n{'='*60}")
    if args.dry_run:
        print(f"Dry run complete. {len(tasks)} group(s) would be posted to.")
    else:
        print(f"All {len(tasks)} group(s) posted successfully.")


if __name__ == "__main__":
    main()
