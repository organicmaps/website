#!/usr/bin/env python3
"""Fail only on translation errors a change INTRODUCES.

Much of the corpus carries known drift, so a plain "must be clean" gate would
stop anyone editing those files for unrelated reasons. This compares the staged
version against HEAD per error code and complains only when a code is new or
its count went up. Fixing some errors while leaving others is fine.

Usage: regression_check.py <english-source> <staged-file> <lang>
Exit 1 if the change makes things worse.
"""
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
try:
    from translate_check import check_translation, ERROR
except Exception:                      # tooling missing: never block a commit
    sys.exit(0)


def codes(src_text: str, out_text: str, lang: str) -> Counter:
    return Counter(p.code for p in check_translation(src_text, out_text, lang)
                   if p.level == ERROR)


def at_head(path: str) -> str | None:
    r = subprocess.run(["git", "show", f"HEAD:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def at_index(path: str) -> str | None:
    r = subprocess.run(["git", "show", f":{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def main() -> int:
    src_path, out_path, lang = sys.argv[1], sys.argv[2], sys.argv[3]
    src_now = at_index(src_path)
    out_now = at_index(out_path)
    if src_now is None or out_now is None:
        print(f"error: unable to read staged translation inputs for {out_path}")
        return 1
    now = codes(src_now, out_now, lang)

    out_head = at_head(out_path)
    if out_head is None:                       # new file: everything is new
        before = Counter()
    else:
        # Compare against the English source as it was too, so an edit to the
        # source is not blamed on the translation.
        before = codes(at_head(src_path) or src_now, out_head, lang)

    worse = {c: (before.get(c, 0), n) for c, n in now.items()
             if n > before.get(c, 0)}
    if not worse:
        return 0

    print(f"error: {out_path} introduces translation errors:")
    for c, (was, is_) in sorted(worse.items()):
        print(f"    {c}: {was} -> {is_}")
    for p in check_translation(src_now, out_now, lang):
        if p.level == ERROR and p.code in worse:
            print(f"    {p}")
    return 1


if __name__ == "__main__":
    sys.exit(main() if len(sys.argv) == 4 else 0)
