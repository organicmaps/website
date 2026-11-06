---
title: "Can I store maps on an SD card?"
description: "Move Organic Maps downloads to supported Android SD cards and learn why map files and bookmark backups are different."
updated: "2026-11-06"
taxonomies:
  faq: ["map"]
extra:
  order: 30
---

On supported Android devices, **Settings → Save maps to** lets you choose an available storage location. The setting depends on your device and Android version. Use the app's setting to move maps.

An unreliable or slow SD card can cause download errors or poor performance. If that happens, try internal storage. Back up your files before any card repair or replacement. Formatting a card is not a general fix for app crashes.

## Where are map and bookmark files stored? Can I copy maps manually? {#map-files}

Organic Maps manages its files in app-specific storage. Paths and access restrictions differ between Android versions, installation sources, and devices. Moving maps to an SD card does not turn the map folder into a bookmark backup.

Use **Download Maps** for maps and **Export** for bookmarks and tracks. Copying arbitrary `.mwm` files into an installation can fail because map versions and related files must match the app. Advanced users can consult the repository's [map-generation documentation](https://github.com/organicmaps/organicmaps/tree/master/generator); building or sideloading maps is not needed for normal updates.

Use the [bookmark and track export instructions](@/faq/bookmarks/how-to-export/index.md) for personal data backups. For download failures, [check the connection and storage](@/faq/map/cant-download-maps/index.md).
