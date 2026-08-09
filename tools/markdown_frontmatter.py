#!/usr/bin/env python3
"""Small shared helper for reading Markdown YAML frontmatter.

Kept separate from the Telegram publisher so translation and CI tooling do not
load networking dependencies merely to split a Markdown document.
"""

import re

import yaml


def strip_frontmatter(text: str) -> tuple[str, dict]:
    """Return ``(body, metadata)`` for a Markdown document.

    Invalid YAML yields empty metadata while still returning the body, matching
    the historical behaviour of the publishing and translation tools.
    """
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
    if not match:
        return text, {}
    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        metadata = {}
    return text[match.end() :], metadata
