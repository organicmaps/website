#!/usr/bin/env python3
"""Small shared helper for reading Markdown YAML frontmatter.

Kept separate from the Telegram publisher so translation and CI tooling do not
load networking dependencies merely to split a Markdown document.
"""

import re

import yaml

FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(.*?)^---[ \t]*(?:\r?\n|\Z)(?:[ \t]*\r?\n)*",
    re.DOTALL | re.MULTILINE,
)


class FrontmatterError(ValueError):
    """YAML frontmatter cannot be used as document metadata."""


def strip_frontmatter(text: str) -> tuple[str, dict]:
    """Return ``(body, metadata)`` for a Markdown document.

    Missing or null frontmatter produces empty metadata. Invalid YAML or a
    non-mapping metadata/extra value raises FrontmatterError so a broken
    header cannot silently disappear from translation or publishing.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return text, {}
    try:
        metadata = yaml.safe_load(match.group(1))
    except (yaml.YAMLError, ValueError) as error:
        raise FrontmatterError(f"invalid YAML frontmatter: {error}") from error
    if metadata is None:
        metadata = {}
    if not isinstance(metadata, dict):
        raise FrontmatterError("frontmatter must be a mapping")
    if "extra" in metadata and not isinstance(metadata["extra"], dict):
        raise FrontmatterError("frontmatter 'extra' must be a mapping")
    return text[match.end() :], metadata
