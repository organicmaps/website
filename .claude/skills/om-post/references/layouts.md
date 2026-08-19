# Slide types

Four types cover every release post. Resist inventing new ones — vary the
`theme` instead.

## `cover`

App icon, kicker, oversized title, one-sentence subtitle, a short rule.
Always green. This is the thumbnail in the feed, so the title must be readable
at 150px wide: three words at most, no punctuation.

Keys: `kicker`, `title`, `subtitle`.

## `feature`

One change, one screenshot. Eyebrow chip names the platform and area
(`iOS · Bookmarks`, `Routing`), title states the benefit, body gives one
sentence of detail.

Keys: `eyebrow`, `title`, `body`, `media`, `device`, `theme`, `bleed`.

`device`:

- `iphone` — portrait iOS shot. Continuous corners, a bright titanium rim,
  volume rocker on the left and the side button opposite.
- `android` — portrait Android shot. Tighter corners, graphite rim, power
  above the volume rocker, both on the right.
- `phone` — portrait shot on no particular platform. The plain dark bezel.
- `desktop` — landscape shot. Rounded corners and a drop shadow only; the
  macOS traffic lights are already inside the screenshot. Runs nearly full
  canvas width.
- `plain` — rounded card, no device pretence. For diagrams or crops.

All three phone frames bleed off the bottom edge by default.

**The platform is usually inferred.** A slide with no `device`, or with
`device = "phone"`, whose eyebrow names iOS or Android gets that platform's
frame — `eyebrow = "iOS · Bookmarks"` is enough. Both names stay Latin in
every translation, so this holds for `post.ar.toml` as much as for the English
source. Set `device` explicitly when the eyebrow says something else, or to
force the generic frame on a platform slide.

The camera cutout is drawn back in — a Dynamic Island for `iphone`, a
punch-hole for `android` — sized as a share of the screen off the real
hardware, so it holds at any rendered size. It is not decoration on top of the
screenshot: the cutout is a hole in the display, neither system draws into it,
and the screenshot has an empty gap in the status bar exactly where it belongs.

That is also why `phone` has none. It exists for a screenshot whose device is
unknown, and putting a Dynamic Island on an iPhone SE shot would be worse than
drawing nothing.

## `list`

Changes with no screenshot worth showing. Light theme by default so the
carousel breathes between image slides. Keep to 4–5 items; each item should
fit two lines at most — in English, which means one line, since the
translations will use the second.

Keys: `eyebrow`, `title`, `items`, `theme`.

## `cta`

Centred. Title, optional body, a pill with the short URL, then a row of store
badges. Always the last slide.

Keys: `title`, `body`, `url`, `badges`.

# Themes

| theme   | use                                            |
|---------|------------------------------------------------|
| `green` | default; brand gradient, white text            |
| `blue`  | one or two slides for rhythm — do not overuse  |
| `light` | list slides, and any screenshot with a dark UI |
| `dark`  | rare; a night-mode screenshot                  |

# Rhythm

A seven-slide carousel that works: cover → feature → feature (different theme)
→ feature → list → list → cta. Never put two `light` slides adjacent to two
image slides of the same theme; alternate so the swipe has contrast.

# Formats

All render from the same `post.toml`. The canvas differs only in size, padding
and type scale, so a slide that reads well at 4:5 generally survives the other
two. The exception is 9:16, which reserves 250px at the top and 300px at the
bottom for the Stories interface — check long list slides there.

`4x5` is what the Telegram channels get. Render `1x1` and `9x16` only when the
post is also going to Instagram, since every extra format is another render per
language.

# Right-to-left

Arabic and Persian render with `dir="rtl"`: the layout mirrors, the watermark
moves to the other corner, and the eyebrow drops its uppercase tracking, which
does nothing for those scripts but pull them apart. The short URL and the
`organicmaps.app` footer stay left-to-right — they are identifiers.
