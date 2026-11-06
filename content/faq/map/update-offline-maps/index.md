---
title: "How do I update the app and downloaded maps?"
description: "Update Organic Maps and downloaded regions, check the map-data date and understand when OpenStreetMap edits reach offline maps."
updated: "2026-11-06"
taxonomies:
  faq: ["map"]
extra:
  order: 10
---

Update Organic Maps through the store or official source you used to install it. Then open **Download Maps** and install the available map updates. Updating the app and downloading the new map files are separate steps.

Map releases are generally published with app releases, often around monthly, but there is no fixed schedule. An older app cannot download and use arbitrary newer map releases. Keep the app and all regions needed for a route up to date together.

More frequent, incremental map updates are in development. The aim is to deliver changes more often and reduce how much data an update needs to download.

## Why are my OpenStreetMap changes missing from Organic Maps? {#map-data-date}

Organic Maps uses a snapshot of OpenStreetMap, not a live copy. Check the map-data date in the app or release notes, then download the latest available map for that region. Changes made after the snapshot date need a later map release.

If a change predates the snapshot but still does not appear, the object may be filtered out, shown only at certain zoom levels, or not yet supported. Report the object's OpenStreetMap link, the map-data date, and what you expected to see. Not every OpenStreetMap tag is displayed or searchable.

To fix a missing or incorrect feature, [edit a place](@/faq/editing/organic-maps-map-editing/index.md) or [report a map error](@/faq/editing/map-errors/index.md). For failed downloads, use the [download troubleshooting guide](@/faq/map/cant-download-maps/index.md).
