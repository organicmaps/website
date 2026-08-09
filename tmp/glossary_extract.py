#!/usr/bin/env python3
"""Mine canonical terminology from the site's own proofread translations.

For each English glossary term, find the translated lines whose English
counterpart contains that term, then score target-language tokens by how much
more often they appear in those lines than in the rest of the corpus
(log-odds keyness). The top-scoring token is almost always the term itself.

The news release notes are line-aligned by construction (the DeepL translator
preserves the line plan), so a file pair is only used when its line counts
match — that keeps alignment precision high without any alignment model.

Usage: python3 tmp/glossary_extract.py [lang ...]
"""
import glob
import math
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from telegram_post import strip_frontmatter  # noqa: E402

# Languages whose scripts have no spaces — score character n-grams instead.
CJK = {"zh-Hans", "ja"}

TERMS = [
    "bookmark", "bookmarks", "track", "tracks", "route", "routes",
    "icon", "icons", "layer", "layers", "isolines", "elevation profile",
    "hillshading", "light rail", "tram", "subway", "public transport",
    "outdoors", "map style", "track recording", "offline maps",
    "antimeridian", "crash", "donation", "team", "voice guidance",
]


def body_lines(path):
    body, _ = strip_frontmatter(Path(path).read_text(encoding="utf-8"))
    return body.strip("\n").split("\n")


# Terms that constantly co-occur ("bookmarks and tracks") drown each other out
# in a plain frequency comparison. Contrast each against its siblings instead:
# a word shared by both appears in positives AND negatives, so it scores ~0.
GROUPS = [
    {"bookmark", "bookmarks", "track", "tracks", "route", "routes",
     "track recording"},
    {"tram", "light rail", "subway", "public transport"},
    {"icon", "icons", "layer", "layers"},
]


def siblings(term):
    for g in GROUPS:
        if term in g:
            return g - {term}
    return set()


def tokenize(line, lang):
    if lang in CJK:
        s = re.sub(r"[\s\W_]+", "", line)
        return [s[i:i + n] for n in (2, 3, 4) for i in range(len(s) - n + 1)]
    # Keep hyphens so compounds like "U-Bahn" survive as one token.
    return [t for t in re.findall(r"[\w-]{3,}", line.lower(), re.UNICODE)]


def build_pairs(lang):
    """Yield (english_line, translated_line) for every line-aligned file pair."""
    for en_path in glob.glob("content/news/*/*/index.md"):
        tr_path = en_path.replace("index.md", f"index.{lang}.md")
        if not Path(tr_path).is_file():
            continue
        en, tr = body_lines(en_path), body_lines(tr_path)
        if len(en) != len(tr):
            continue
        yield from zip(en, tr)


def keyness(lang, terms=TERMS, top=4):
    pairs = list(build_pairs(lang))
    if not pairs:
        return None, 0

    # Language-agnostic stopword removal: a token appearing in more than 6% of
    # all lines is grammatical furniture ("der", "для", "için"), not a term.
    # Avoids hand-maintaining stopword lists for 20+ languages.
    df = Counter()
    for _, tr in pairs:
        df.update(set(tokenize(tr, lang)))
    stop = {t for t, c in df.items() if c > len(pairs) * 0.06}

    results = {}
    for term in terms:
        pat = re.compile(rf"\b{re.escape(term)}\b", re.I)
        sib_pat = None
        if siblings(term):
            sib_pat = re.compile(
                "|".join(rf"\b{re.escape(s)}\b" for s in siblings(term)), re.I)

        pos, neg = Counter(), Counter()
        n_pos = n_neg = 0
        n_loanword = 0
        samples = []
        for en, tr in pairs:
            if pat.search(en):
                # The term may be a loanword kept verbatim (German "Team").
                if pat.search(tr):
                    n_loanword += 1
                # Other tokens echoed from English are contributor names,
                # brands and numbers — never the term we are mining.
                en_low = en.lower()
                toks = {t for t in tokenize(tr, lang) if t not in en_low}
                pos.update(toks)
                n_pos += 1
                if len(samples) < 2 and len(tr) < 160:
                    samples.append(tr)
            elif sib_pat is None or sib_pat.search(en):
                # Contrastive negatives when the term has siblings, else all
                # remaining lines.
                neg.update(set(tokenize(tr, lang)))
                n_neg += 1
        if n_pos < 3 or n_neg < 3:
            continue

        scored = []
        for tok, c in pos.items():
            if tok in stop or c < max(3, n_pos * 0.25):
                continue
            p = c / n_pos
            q = (neg.get(tok, 0) + 0.5) / (n_neg + 1)
            scored.append((math.log(p / q) * p, tok, c, n_pos))
        scored.sort(reverse=True)

        # Drop substrings of a higher-ranked n-gram (CJK produces nested hits).
        kept = []
        for s, tok, c, n in scored:
            if any(tok in k[1] for k in kept):
                continue
            kept.append((s, tok, c, n))
            if len(kept) == top:
                break
        results[term] = (kept, samples, n_loanword, n_pos)
    return results, len(pairs)


def main():
    langs = sys.argv[1:] or ["ru"]
    verbose = "-v" in langs
    langs = [l for l in langs if l != "-v"]
    for lang in langs:
        res, n = keyness(lang)
        print(f"\n{'='*74}\n{lang}  ({n} aligned lines)\n{'='*74}")
        if not res:
            print("  no aligned corpus")
            continue
        for term, (cands, samples, n_loan, n_pos) in res.items():
            shown = "   ".join(f"{t} ({c}/{n_})" for _, t, c, n_ in cands)
            if n_loan >= max(3, n_pos * 0.5):
                shown = f"[kept as-is {n_loan}/{n_pos}]   " + shown
            print(f"  {term:18s} {shown}")
            if verbose and samples:
                print(f"{'':20s}  ↳ {samples[0]}")


if __name__ == "__main__":
    main()
