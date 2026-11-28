# Organic Maps Website

[Organic Maps website](https://organicmaps.app) is built with [Zola](https://www.getzola.org/) and runs on [Cloudflare Pages](https://developers.cloudflare.com/pages/).

## Development

Install the latest [zola](https://www.getzola.org/documentation/getting-started/installation/) for your operating system.

Run `zola serve` for a local preview or `zola build` to generate static site in the `public` folder.

Run `npm i && npm run format` when you want to pretty-format the Markdown and SCSS files.

Upgrade npm dependencies with `npm run upgrade`, make sure that you have installed `npm-check-updates` package.

The translation and publishing scripts live in [`tools/`](tools/) and are meant to be run from the repository root,
e.g. `python3 tools/translate_check.py --all`. Install their Python dependencies with
`pip install -r tools/requirements-telegram.txt`.

Run `python3 tools/test_navigation.py` for homepage, navigation, news media, FAQ and donation template regressions. For browser regressions, install Node dependencies with `npm ci` and Chromium with `npx playwright install chromium`, then run `zola build` and `npm run test:browser`. Browser tests fulfill requests locally to check donation checkout and FAQ navigation.

## Deployment

Every PR deploys a preview version of the site at unique url.

Every merge into the _master_ branch deploys changes into the production at https://organicmaps.app

### Updating News

Use previously published news as a template.

An example of a news post that is related to app updates/releases:

```yaml
title: "OpenStreetMap login was fixed in Google Play"
date: 2024-03-18T17:45:35+00:00
slug: "openstreetmap-login-was-fixed-in-google-play"
taxonomies:
  news: ["Releases"]
```

For external links and press releases use this taxonomy:

```yaml
taxonomies:
  news: ["Press"]
```

Use the `sponsored_link` component for paid referral links. Its body is the
localized link label, and the self-closing form displays the URL itself.
Both forms preserve the link when publishing to Telegram.

```jinja
{% <sponsored_link url="https://example.org/ref"> %}our referral link{% </sponsored_link> %}
{{ <sponsored_link url="https://example.org/ref" /> }}
```

JPEG, PNG and WebP images stored alongside a news post are rendered automatically.
The article, news listing and date archive share one media renderer. Filenames
are sorted and extensions are case-insensitive. MP4 files render as videos;
MP3 files can be embedded in the text with the `audio` component. Other file
types stop the build. Images reserve their dimensions and use async decoding;
listing and archive images load lazily. Articles keep their first image eager.
Listing and archive videos preload metadata so their previews and dimensions
are available before playback.

For new posts, publish WebP images once and reuse them for both the website and
sharing previews. The first image is used automatically, or `extra.preview_image`
can select another published image. Keep a separate sharing cover only when it
needs different artwork or framing, using the parent-folder convention below.
Do not add JPEG/PNG duplicates for new posts or introduce redirects or aliases
when converting news images.

Already-published posts retain their original preview filenames, paths and
`extra.preview_image` values. An original preview may remain alongside a lowercase
`.webp` with the same filename stem. The gallery and Telegram use the WebP.
Key `extra.media_alt` by the filename shown in the gallery.

For image optimization, install `cwebp` from libwebp and prepare a temporary
candidate outside the article folder:

```bash
cwebp -lossless -q 100 -m 6 -exact -metadata icc source.png -o /tmp/news-candidate.webp
cwebp -q 90 -m 6 -sharp_yuv -metadata icc source.jpg -o /tmp/news-candidate.webp
```

These settings preserve image dimensions and ICC profiles. WebP is 8-bit, so
16-bit PNG sources are reduced to 8-bit before lossless encoding. Compare size
and visual quality, then publish the WebP in the article folder when it is
smaller. Update filename references in every translation when you replace an
original.

Add specific image descriptions in each translation's frontmatter:

```yaml
extra:
  media_alt:
    "01-map.webp": "Mountain trails and contour lines around the summit"
    "02-decoration.png": ""
```

Keys must match image filenames exactly or the build stops. An image without
a `media_alt` entry uses the localized article title; use an empty description
only for decorative or redundant images. Translate `extra.media_alt` manually,
because `translate_md.py` copies `extra` unchanged. `translate_check.py` warns
when an entry from the English source is missing (including an empty entry
for a decorative image), or a description is still identical to English.

Social previews use this order:

1. An explicit `extra.preview_image` (a colocated filename or site-root path).
2. A parent-folder cover named `<article-folder>-preview.jpg` or `<article-folder>-preview.webp` for a bundled news post. Existing JPEG covers take priority.
3. The first supported article image in filename order, detecting extensions case-insensitively.
4. The default site image.

A new post in `content/news/YYYY-MM-DD/NNN/` can use
`content/news/YYYY-MM-DD/NNN-preview.webp` as its separate cover. Zola finds it
by source folder name and uses it for translations without preview YAML. The
cover stays out of the article gallery and Telegram album. The image sitemap
includes explicit and automatic parent previews. A missing explicit local
preview stops the build.

Telegram media discovery also recognizes `.webp` files. Standalone Telegram
folders can include `.mov` and `.m4a`; news folders must use the website's
supported formats listed above.
For shared images in `static/`, the `screenshot` component accepts WebP paths and
reads their dimensions just as it does for JPEG and PNG.

## Taxonomy and F.A.Q. architecture

Each MD page in `/faq/` has one or more taxonomy defined in header. E.g.:

```yaml
taxonomies:
  faq: ["app"]
```

Zola collects all such taxonomies:

| File                                      | Taxonomy key | Taxonomy value         |
| ----------------------------------------- | ------------ | ---------------------- |
| map/can-not-find-position/index.md        | `faq`        | `location-and-compass` |
| map/search-cannot-find-a-place/index.md   | `faq`        | `search`               |
| editing/map-errors/index.md               | `faq`        | `map-editing`          |
| app/crash/index.md                        | `faq`        | `app`                  |
| voice/text-to-speech-android-tts/index.md | `faq`        | `voice-directions`     |
| bookmarks/how-to-import/index.md          | `faq`        | `bookmarks-and-tracks` |

Zola then collects the `faq` taxonomy values and generates pages:

- `/faq/`, with the list of categories (see `templates/faq/list.html`)
- One page for each category, such as `/faq/app/` or `/faq/map/`, including localized category URLs such as `/es/faq/aplicación/` (see `templates/faq/single.html`)

If you want to add new question then create .md file with header:

```yaml
title: A full question that is the title of the page
description: More detailed info with necessary keywords for better SEO

taxonomies:
  faq: ["bookmarks-and-tracks"]
extra:
  order: 40
```

Zola will add your question to specific F.A.Q. sub-page.

Use a distinct `extra.order` within each category and language; `npm test` checks these values across the FAQ corpus.

Answers can group related questions under H2 headings. Set `extra.start_here: true` on a complete FAQ index to enable topic shortcuts and subquestion links. Edit the shared Start here list in the default FAQ index’s `extra.start_here_pages`. Each index resolves those paths and titles in its own language. Translate the discovery labels with `faq-start-here`, `faq-browse-topics` and `faq-topics` in `config.toml`. Keep published heading fragments stable when editing answers; an alias anchor can preserve a fragment alongside a descriptive heading.

Language-selector links follow fragment changes, including browser Back and Forward. Complete FAQ inventories use shared heading fragments and topic IDs so readers can stay on the same section when switching languages. Map localized topic slugs to their shared IDs in `extra.faq_topic_ids`. The build checks that every index with topic shortcuts has the same IDs as the default language. Partial indexes retain the fragment so switching back returns to the selected topic.

News is a taxonomy landing page. Inside Markdown, resolve it with `get_url(path="news", lang=lang, trailing_slash=true)`, stripping `config.base_url` for browser navigation. Keep the label outside the expression so translation tools can translate it; the navigation suite checks the rendered destinations.

If you need to translate the FAQ to a new language please add next lines to config.toml:

```toml
[languages.XX]
taxonomies = [
  {name = "faq", feed = false},
  {name = "news", feed = true},
]
[languages.XX.translations]
faq-menu-title = "{Translation of 'F.A.Q.' to a new language}"
faq-term-description = "{Description containing a {} placeholder for the category}"
```

Each translated FAQ page uses a localized taxonomy value, or a language-neutral name such as `linux`. The corresponding `content/faq/_index.XX.md` has `render: false`, allowing the translated FAQ taxonomy to own `/XX/faq/` without colliding with the section page.

F.A.Q. categories keep Zola's alphabetical order, with the localized category IDs in `extra.faq_last_categories` placed last in listings, menus and translation status. Add any new localized Linux category ID to that list. `extra.faq_category_titles` preserves product-name capitalization for the separate `android-auto` and `apple-carplay` topics; their answer paths remain independent of their categories.

**Limitation**: Each F.A.Q. category has only a name; Zola taxonomies do not provide per-term content or icons.

## Embedded FAQ

A subset of FAQ questions is used to generate static single-page FAQ: [`/faq/embedded-faq/`](https://organicmaps.app/faq/embedded-faq/?lang=en). This page should be used as an embedded offline help page in Organic Maps app on Android and iOS. To see how it looks in different languages use following links:

- https://organicmaps.app/faq/embedded-faq/?lang=en
- https://organicmaps.app/faq/embedded-faq/?lang=de
- https://organicmaps.app/faq/embedded-faq/?lang=ru
- etc.

The curated embedded and translation-status language subsets are defined once in `config.toml` as `extra.faq_embedded_languages` and `extra.faq_translation_status_languages`. The embedded template fails the Zola build if any selected question is missing in a configured embedded language.

Use localized Markdown `@/…` links between FAQ answers. The embedded renderer uses the bundled inventory to turn whole-answer links and shared heading targets into local fragments. Links outside the bundle open their standalone pages. The displayed language also resolves legacy embedded fragments. On the website, an explicit English FAQ fragment takes precedence over automatic language selection.

To update the embedded FAQ, replace [`data/faq.html`](https://github.com/organicmaps/organicmaps/blob/master/data/faq.html) with the latest version generated by Zola.

Run `zola build` and `npm run test:browser` to check the bundled links from a local file with the browser offline.

## Contribution

Any good ideas and help with web site improvement are appreciated. And it's always better to discuss
any improvement before implementing it to sync with our vision and plans.

## Translations

Please help us with translating this web-site in your language.

Markdown files in the content directly can be [edited directly on GitHub](https://github.com/organicmaps/website/tree/master/content) by pressing the Edit button
(synchronize the translated file structure with the English `index.md` source). Or create an issue/ [send us](mailto:hello@organicmaps.app) the text, and we'll add translations.

New language should be also added in `config.toml`.
