# Organic Maps Website - AI Agent Guide

This is a multilingual static website built with [Zola](https://www.getzola.org/) for the Organic Maps app, deployed via Cloudflare Pages.

## Architecture & Key Concepts

### Multilingual Structure

- **Default language**: English (`en`) - base content in `content/_index.md`, `content/news/_index.md`, etc.
- **Translations**: Suffixed files like `_index.ru.md`, `index.de.md` for each language
- **30+ languages** configured in `config.toml` under `[languages.XX]` sections
- Each language must define `taxonomies` and `translations` keys in config
- URL structure: `/` (en), `/ru/`, `/de/faq/`, etc.

### Taxonomy System (Critical Pattern)

Zola uses taxonomies to auto-generate category pages:

1. **FAQ taxonomy**: Each FAQ question has `taxonomies: faq: ["App"]` in frontmatter
   - Zola collects all unique values: "App", "Map", "Bookmarks and Tracks", etc.
   - Auto-generates: `/faq/` (list of categories) and `/faq/app/` (questions in category)
   - Templates: `templates/faq/list.html` (all categories), `templates/faq/single.html` (category questions)
   - Questions sorted by `extra.order: 40` in frontmatter

2. **News taxonomy**: Posts have `taxonomies: news: ["Releases"]` or `["Press"]`
   - Auto-generates category pages like `/news/releases/`
   - Date-based folders: `content/news/2024-03-18/323/index.md`

**Limitation**: Taxonomy values are sorted alphabetically, cannot be reordered manually.

### Template Hierarchy

- `base.html`: Main wrapper, handles RTL languages, meta tags, resource detection (page/section/term/taxonomy)
- `index.html`: Homepage only (extends base)
- `page.html`: Generic page template
- `news/single.html`, `faq/single.html`: Taxonomy term pages
- `news/page.html`: Individual news post

### Shortcodes (Reusable Components)

In content Markdown, use `{{ shortcode_name() }}` syntax:

- `{{ badges() }}` → App store download badges
- `{{ screenshot(src='/images/screenshots/hiking.jpg', alt='Hiking') }}` → Responsive image
- Located in `templates/shortcodes/` as `.html` or `.md` files

### Resource References in Templates

Zola distinguishes resource types:

- `page`: Individual content file (`index.md`)
- `section`: Directory index (`_index.md`)
- `term`: Taxonomy value page (e.g., `/faq/app/`)
- `taxonomy`: Taxonomy root (e.g., `/faq/`)

Access with `get_page(path="donate/index.md")` or `get_section(path="news/_index.md")`.

### Translation Function

Use `{{ trans(key='faq-menu-title', lang=lang) }}` to get localized strings from `config.toml` `[translations]` sections.

## Developer Workflows

### Local Development

```bash
zola serve           # Live preview at http://127.0.0.1:1111
zola build           # Generate static site in public/
npm test             # Offline translation, hook and Telegram regressions
npm run format       # Format MD + SCSS (stylelint + prettier + js-beautify)
npm run upgrade      # Update npm dependencies
```

Install Python dependencies from `requirements-check.txt` for translation
checks, or `requirements-telegram.txt` (which includes the check dependencies)
for Telegram publishing and the complete test suite.

### Adding Content

#### New FAQ Question

1. Create `content/faq/category-name/question-slug/index.md`
2. Frontmatter:
   ```yaml
   title: Full question text
   description: SEO description
   taxonomies:
     faq: ["App"] # or "Map", "Bookmarks and Tracks", etc.
   extra:
     order: 40 # Controls sort order within category
   ```
3. Zola auto-adds to appropriate category page
4. For translations: create `index.ru.md`, `index.de.md` in same folder

#### New News Post

1. Create `content/news/YYYY-MM-DD/NNN/index.md` (NNN = sequential number)
2. Frontmatter:
   ```yaml
   title: "Post title"
   date: 2024-03-18T17:45:35+00:00
   slug: "url-friendly-slug"
   taxonomies:
     news: ["Releases"] # or ["Press"] for external links
   ```
3. **CRITICAL**: Run `./fix_news_translations.sh` after adding translated news files
   - Creates required `_index.XX.md` files for proper translation processing

#### New Language

1. Add to `config.toml`:
   ```toml
   [languages.XX]
   taxonomies = [
     {name = "faq", feed = false},
     {name = "news", feed = true},
   ]
   [languages.XX.translations]
   faq-menu-title = "Translated FAQ"
   language = "Language Name"
   # ... other translation keys
   ```
2. Create translated content files with `.XX.md` suffix
3. Add to RTL list in `base.html` if right-to-left language

### Menu & Navigation

- Top menu built dynamically in `templates/top_menu.html`
- Reads pages via `get_section()` and `get_page()`
- Finds translations via `page.translations | filter(attribute='lang', value=lang)`
- Menu titles from `extra.menu_title` in content frontmatter

### Styling

- Main styles: `sass/main.scss`
- Modular imports: `sass/_language_selector.scss`, `sass/_top_menu.scss`
- Dark mode: `@media (prefers-color-scheme: dark)` blocks
- RTL support: `dir="rtl"` on `<html>` for RTL languages
- Responsive design: Mobile-first, uses flexbox for layout

### Static Assets

- `static/_redirects`: Cloudflare redirect rules (e.g., `/support-us → /contribute/`)
- `static/_headers`: Cloudflare headers (noindex for preview deployments)
- `static/images/`, `static/logos/`, `static/sponsors/`: Media assets

## Common Patterns

### Embedded FAQ

Special single-page FAQ at `/faq/embedded-faq/` for in-app display. Template handles language switching via `?lang=XX` query param.

### Language Selector

Pure CSS dropdown using hidden checkbox trick (`input.lang-menu-trigger`). JavaScript stores preference in `localStorage`.

### Preview Images

OpenGraph images auto-detected from `resource.extra.preview_image` or first asset in `resource.assets[]`, fallback to `images/screenshots/prague.jpg`.

## Deployment

- **PR**: Auto-deploys preview at unique URL
- **Merge to master**: Deploys to production https://organicmaps.app
- Build process: Cloudflare Pages runs `zola build`

## Project Conventions

- **File naming**: Use `index.md` for pages, `_index.md` for sections
- **Date format**: ISO 8601 with timezone (`2024-03-18T17:45:35+00:00`)
- **Slugs**: Lowercase with hyphens, translated appropriately
- **Image optimization**: Store content-related images at the same content folder. Store global images in `static/images/`, use shortcodes for consistent rendering
- **Config order**: Sort language sections and translation keys alphabetically in `config.toml`

## Translating markdown

`translate_md.py` translates any markdown file — with or without frontmatter — into the site's languages, preserving every link, list marker, attribution and shortcode. Use it for Telegram posts, site articles and release notes alike.

```bash
python3 translate_md.py post.md --langs ru,de,fr
python3 translate_md.py post.md --telegram -o tmp/tg-post/   # channel languages
python3 translate_md.py content/news/2026-08-04/630/index.md --all
python3 translate_md.py post.md --langs ru --dry-run         # cost, no API call
```

It translates `title:` and `description:`, leaves `date:`/`slug:`/`taxonomies:` verbatim, rewrites `@/…/index.md` links to the translated page when that page exists, applies the glossary below, and runs the tidy-up passes (native quotes, brand unquoting, ellipsis, link-label hygiene, informal register where DeepL supports it). **Output is a draft**: the slug and the informal register in `tr`/`uk`/`fa-IR` still need the proofreading pass.

Two behaviours worth knowing, both established by measurement:

- **Brands stay visible to the translator.** Hiding them behind placeholders wrecks word order — "OpenStreetMap data as of August 4" came back as "OpenStreetMap Теперь включены данные…". Identity entries in the glossary keep them Latin instead. Languages that transliterate brands and have no glossary (`hi`, `ml`, `te`, `fa-IR`) keep placeholder protection.
- **Formality** is requested where DeepL supports it — `prefer_less` for most languages, `prefer_more` for ru/uk/be, which take the polite address. Chinese and Indonesian are fixed mechanically (您→你, Anda→kamu) because their polite form is a bare pronoun with no verb agreement. The other 11 formal-by-default languages need the review pass, since informalising them means rewriting verb morphology. `detect_register()` and `register_ok()` report which.

## Keeping translations correct

These are the invariants a translated markdown file must hold. Each one was broken somewhere in this repo and cost a repair pass; `translate_check.py` enforces most of them.

**Identifiers are not prose. Never translate:**

- Product names — `Organic Maps`, `OpenStreetMap`, `ID Editor`, `Google Play`, `App Store`, `F-Droid`, `Obtainium`, `Accrescent`, `Weblate`. This holds in every language and every script: not `Organiese kaarte`, not `Οργανικούς Χάρτες`, not `الخرائط العضوية`, and **not transliterated** either — not `ऑर्गेनिक मैप्स`, `ఆర్గానిక్ మ్యాప్స్` or `ഓർഗാനിക് മാപ്`. Only `Android` and `iOS` may be transliterated in non-Latin scripts.
- Contributor names in `_(Name)_`, `(Name)` and `-- Name` credit lines.
- Heading anchors — `{#osm-note}`, `{#engines}`, `{#install}`. A translated anchor breaks every link pointing at it and fails the Zola build.
- OSM tags and values — `craft=*`, `parking_entrance`, `healthcare=*`.
- Anything inside a code span, a `{{ shortcode }}`, or a URL.

**Never change `slug:` or `aliases:`.** They are published URLs. Several slugs contain a translated brand; they stay that way.

**Structure must match the English source** line for line: same paragraphs, bullets, headings, links, and `_(Contributor)_` attributions, each attribution at the end of its bullet.

**Write one paragraph per line.** Do not hard-wrap prose. Wrapped text makes line-based tooling read every paragraph as a structural mismatch, and in CJK a soft line break renders as a visible space.

**`[label](target)` takes no space.** `[label] (target)` does not parse — it renders as literal text, which happened to 78 links here.

**Point readers at their own language's Telegram group** where one exists (`ar de es fa-IR fr it pt ru tr uk zh-Hans`), otherwise the English chat. The "Join local communities" list is the exception: it names every chat on purpose.

**Localize `@/…/index.md` links** to `@/…/index.LANG.md` when that translation exists, so a translated page does not send the reader to the English one.

**Watch the glossary in non-map contexts.** Terminology substitution is context-blind: `track → 轨迹` turned "no tracking" in the privacy policy into "no GPS traces". Translate such text with `use_glossary=False`.

## Formatting and validating on commit

`npm run hooks:install` points `core.hooksPath` at `.githooks`, so committing
runs `.githooks/pre-commit` on **staged** files. It rejects a `[label] (target)`
link with a space, rejects a non-ASCII heading anchor, and runs
`translate_check.py` — reporting only errors the change **introduces**, since
much of the corpus carries known drift and blocking on that would stop anyone
editing those files for unrelated reasons. Bypass once with `--no-verify`.

The hook deliberately does **not** format. Running prettier from it was tried
and removed: the corpus is not prettier-clean, so it rewrites whatever you
touch, and `proseWrap: never` merges soft line breaks, which shifts the block
counts `translate_check` compares against the unformatted English source. Run
`npm run format` deliberately, as its own commit.

CI (`.github/workflows/check.yml`) enforces the two syntax guards corpus-wide
and runs `npm run check` (`translate_check.py --all`) as a report, alongside
the Zola build.

## Validating a translation

`translate_check.py` compares a translation against its English source and reports what broke. `translate_md.py` runs it automatically after each language and exits non-zero if anything is ERROR-level, so it can gate a publish step.

```bash
python3 translate_check.py content/news/2026-08-04/630/   # whole folder
python3 translate_check.py index.md index.ar.md ar        # one file
```

ERROR blocks publication — structural mismatch against the source (lines, bullets, headings, links, attributions, shortcodes), leftover `<x>`/`<a0>` tags, a link that lost its opening `[`, an attribution moved out of its bullet, a lost brand, or a word spliced from two alphabets. Warnings cover polish: register, straight quotes, `...`, quoted brands, and suffixes stranded outside a link.

The Russian donation page intentionally omits the UAH payment reference and
the Ukrainian page intentionally omits RUB. They declare those exact omissions
with `extra.translation_omits_refs`; the checker rejects that field for every
other language, reference, or page, and rejects it once the reference is no
longer missing.

Calibrated against the 383 human-proofread translations of the 2026 posts: 380 pass. The three that do not are genuine defects that review missed — `de` and `zh-Hans` both lost the "Join beta testing" heading in the May release, and `mr` dropped "Organic Maps" entirely. Checks were narrowed where the corpus proved them wrong: mixed-script detection applies only to Cyrillic and Greek, since Arabic `وGoogle`, Chinese `上的FAQ翻译` and Telugu `OpenStreetMapలో` are all correct.

## Terminology glossary

`translation_glossary.tsv` is the source of truth for domain terminology in every language. It was mined from the site's own proofread translations (see `tmp/glossary_extract.py`) and is enforced automatically when translating with DeepL — it is what stops "bookmarks" becoming _закладки_ or "tracks" collapsing into "routes".

```bash
python3 deepl_glossary.py sync     # upload/refresh from the TSV
python3 deepl_glossary.py check    # show what it changes, per language
python3 deepl_glossary.py list     # what DeepL currently stores
```

From any translation script:

```python
from markdown_xml import to_xml, from_xml
from deepl_glossary import get_glossary_id, get_local_terms, apply_repairs

payload, ctx = to_xml(markdown)      # markdown -> XML DeepL can reposition
# ... translate payload with tag_handling=xml, ignore_tags=x, glossary_id=gid
text = apply_repairs(from_xml(translated, ctx), lang)
```

- `get_glossary_id(lang)` — `None` means translate without a glossary.
- `get_local_terms(lang)` — terms to substitute after translating.
- `apply_repairs(text, lang)` — undo known translator defects in the output.

`markdown_xml.py` maps markdown to XML tags so the translator repositions formatting grammatically instead of mangling it, and is content-agnostic: the same module serves Telegram posts, site articles and release notes. Its test suite (`tmp/test_xml_roundtrip.py`) requires no API key and asserts three properties over all 2,900+ markdown files in the repo — exact round-trip, payload purity (nothing untranslatable reaches the translator), and correct tag classification per construct.

Two constraints shape the design, both verified against the API:

- **The DeepL Free plan stores exactly one glossary.** One glossary per language is therefore impossible (the second create returns 456 "Too many glossaries"). Instead a single _multilingual_ v3 glossary holds one dictionary per language; its ID works in ordinary v2 `/translate` calls.
- **Dictionaries are keyed by base language code.** `pt-PT`, `pt-BR` and `zh-Hans` are rejected as dictionary targets, so `pt` and `pt-BR` share one `pt` dictionary. `deepl_glossary.py` uploads only the entries the two variants agree on and returns the rest through `get_local_terms()` for post-translation substitution — the same path used by the 11 languages DeepL glossaries do not support at all (af, ca, cy, eu, fa-IR, gl, hi, ml, mr, oc, te).

When adding a term, prefer one that is unambiguous in every context: whole-word substitution is context-blind, which is why "steps", "note", "style", "place" and "search" are deliberately excluded. Terms with contradictory evidence are listed under NEEDS NATIVE REVIEW at the bottom of the TSV rather than guessed at — currently the recorded-track term for `ar`, `cs`, `el` and `he`, where the existing translations use one word for both "track" and "route".

## When translating content from English:

- The glossary above covers these mechanically for DeepL; the notes below still apply to manual and LLM proofreading.
- "bookmark" or "bookmarks" (favorite place, saved by user) , use word "метка" or "метки" for Russian, use word "мітка" or "міткі" for Ukrainian
- "track" (recorded path on the map that user walked) to Russian, use word "трек"; for Lithuanian, use word "trasa"
- "route" to Russian, use word "маршрут"
- "icon" or "icons" (place's image symbol on the map), use word "иконка" или "иконки" for Russian
- "outdoors" or "outdoors style" or "outdoors map style" use "стиль для активного отдыха" for Russian, use "режим Активний відпочинок" for Ukrainian.
- "map" use "мапа" for Ukrainian and Belarusian.
- use "…" instead of "..."
- use the informal / familiar second-person address (the casual "you" a brand uses to speak to a single user) consistently in every language that distinguishes formal from informal — e.g. French tu (not vous), German du (not Sie), Spanish tú (not usted), Italian tu (not Lei), Catalan/Occitan tu, Polish ty, Turkish sen, Hungarian te, Greek εσύ, European Portuguese tu. Never mix registers within a text. Exception: Brazilian Portuguese (pt-BR) informal form is "você" — keep it.
- **Ten languages are the exception: use the FORMAL/polite address.** Russian вы (not ты), Ukrainian ви (not ти), Belarusian вы (not ты), Czech vy (not ty), Lithuanian jūs (not tu), Hindi आप (not तुम/तू), Marathi तुम्ही (not तू), Telugu మీరు (not నువ్వు), Malayalam നിങ്ങൾ (not നീ), Persian شما (not تو) — with the matching verb forms. This overrides the informal rule above for those languages only. `translate_md.py` requests `formality=prefer_more` for them and `prefer_less` for everyone else; `register_ok()` checks the result against the language's expected register.

  Russian, Ukrainian and Belarusian take the polite address by convention; Czech and Lithuanian were added by the project owner after the site had been converted the other way, so treat the informal forms you may still find in older commits as superseded. A practical benefit came with it: the informal singular forces a grammatical gender that the polite plural does not, so those two languages no longer address every reader as male. The other five are a different case: their familiar forms are for children, intimates and subordinates, so the polite form is the _unmarked_ way to address an adult stranger rather than a stiff alternative to a warm one — the opposite of French `tu` or German `du`. The app's own shipped strings settle it, addressing users formally in Hindi (66 markers to 1), Marathi (51 to 0) and Persian (49 to 0); Telugu and Malayalam have too few second-person strings to judge and follow their siblings.
- prefer the target language's native quotation marks (« » for French, Spanish, Catalan, Galician, Greek, Occitan, Russian and European Portuguese; „ " for German, Czech, Polish, Hungarian, Estonian and Lithuanian; full-width quotes for Chinese; etc.) instead of straight ASCII "" or '' (programmer's) quotes.
- use ё instead е in Russian where applicable
- do not translate Organic Maps and ID Editor
- do not replace amounts like 5K with zeroes (5.000), either leave it (if it is a normal language practice) or use "5 thousands" equivalent (like 5 тыс. in Russian)
- do not insert newlines (do not split) for a yaml value in markdown frontmatters
- replace markdown links starting with @/ and ending with index.md with index.LANGUAGE.md in each translated file.
- also translate markdown header, including title:, description: and slug: fields
- Replace /index.md in any links that start with @/ with /index.LANGCODE.md so links in the translated markdown file can point to the related translated page in LANGCODE language.
