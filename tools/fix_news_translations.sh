#!/bin/bash

# This script creates required _index files to properly process news translations.
# TODO: Automatize it or find a way to avoid required translated _index files.

set -euo pipefail

# Resolve the corpus and the recursive self-call from this file's own location,
# so the script works from the repo root or from anywhere else.
SELF="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
REPO_ROOT="$(dirname "$(dirname "$SELF")")"

if [ -z ${1:-} ]; then
  find "$REPO_ROOT/content/news" -type f -name 'index.*.md' -exec "$SELF" {} \;
else
  PARENT_DIR="$(dirname $1)/.."
  LANG_INDEX=$(basename $1)
  rsync -a "$PARENT_DIR/_index.md" "$PARENT_DIR/_$LANG_INDEX"
fi
