# Organic Maps Website

[Organic Maps website](https://organicmaps.app) is built with [Zola](https://www.getzola.org/) and runs on [Cloudflare Pages](https://developers.cloudflare.com/pages/).

## Development

Install the latest [zola](https://www.getzola.org/documentation/getting-started/installation/) for your operating system.

Run `zola serve` for a local preview or `zola build` to generate static site in the `public` folder.

Run `npm i && npm run format` when you want to pretty-format the Markdown and SCSS files.

Upgrade npm dependencies with `npm run upgrade`, make sure that you have installed `npm-check-updates` package.

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

## Taxonomy and F.A.Q. architecture

Each MD page in `/faq/` has one or more taxonomy defined in header. E.g.:

```yaml
taxonomies:
  faq: ["app"]
```

Zola collects all such taxonomies:

| File                                    | Taxonomy key | Taxonomy value     |
| --------------------------------------- | ------------ | ------------------ |
| map/can-find-position/index.md          | `faq`        | `Map`              |
| map/search-cannot-find-a-place/index.md | `faq`        | `Map`              |
| editing/map-errors/index.md             | `faq`        | `Map Editing`      |
| app/crash/index.md                      | `faq`        | `App`              |
| text-to-speech-android-tts/index.md     | `faq`        | `Voice Directions` |
| ...                                     | ...          | ...                |

After that Zola gets all values for `faq` taxonomy: `[app, map, editing, tts, ...]`. And generates pages:

- For key `/faq/` with the list of values (see `templates/faq/list.html`)
- For each value `/faq/app`, `/faq/map`, etc. (including translated `/es/faq/aplicacion`, `/de/faq/karte/`) with the list of questions (see `templates/faq/single.html`)

If you want to add new question then create .md file with header:

```yaml
title: A full question that is the title of the page
description: More detailed info with necessary keywords for better SEO

taxonomies:
  faq: ["Bookmarks and tracks"]
extra:
  order: 40
```

Zola will add your question to specific F.A.Q. sub-page.

If you need to translate the FAQ to a new language please add next lines to config.toml:

```toml
[languages.XX]
taxonomies = [
  {name = "faq", feed = false},
]
[languages.XX.translations]
faq-menu-title = "{Translation of 'F.A.Q.' to a new language}"
```

**Limitation**: F.A.Q. categories (taxonomies) are sorted alphabetically: "app", "bookmarks", "editing", "map", "tts".

**Limitation**: Each F.A.Q. category has only a name. No description, no icon. Only name 'App', or 'Bookmarks and Tracks', or 'Map Editing', etc.

## Embedded FAQ

A subset of FAQ questions is used to generate static single-page FAQ: [`/faq/embedded-faq/`](https://organicmaps.app/faq/embedded-faq/?lang=en). This page should be used as an embedded offline help page in Organic Maps app on Android and iOS. To see how it looks in different languages use following links:

- https://organicmaps.app/faq/embedded-faq/?lang=en
- https://organicmaps.app/faq/embedded-faq/?lang=de
- https://organicmaps.app/faq/embedded-faq/?lang=ru
- etc.

List of supported languages could be found in `templates/faq/embedded-faq.html`: `en`, `de`, `es`, `fr`, `pt`, `pt-BR`, `pl`, `ru`, `tr`, `uk`, `zh`.

To update embedded FAQ replace [`data/faq.html`](https://github.com/organicmaps/organicmaps/blob/master/data/faq.html) file with the latest version generate by Zola.

## Contribution

Any good ideas and help with web site improvement are appreciated. And it's always better to discuss
any improvement before implementing it to sync with our vision and plans.

## Translations

Please help us with translating this web-site in your language.

Markdown files in the content directly can be [edited directly on GitHub](https://github.com/organicmaps/website/tree/master/content) by pressing the Edit button
(synchronize the translated file structure with the English `index.md` source). Or create an issue/ [send us](mailto:hello@organicmaps.app) the text, and we'll add translations.

New language should be also added in `config.toml`.
