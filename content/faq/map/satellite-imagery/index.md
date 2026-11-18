---
title: "Does Organic Maps have satellite imagery?"
description: "Learn how experimental satellite imagery in Organic Maps uses a custom tile server and how it differs from offline vector maps."
updated: "2026-11-06"
taxonomies:
  faq: ["map"]
extra:
  order: 70
---

Current releases have an experimental satellite-imagery setting that requires a custom raster tile server URL with `{x}`, `{y}`, and `{z}` placeholders. Organic Maps satellite-imagery servers are planned so that imagery will work out of the box, without configuring a custom server.

Use a provider that permits this use and follow its terms. Imagery requests use the network and reveal the requested map area to that provider. This is separate from the downloadable offline vector maps; do not rely on it being available offline.
