---
title: "What is OpenStreetMap, and how do I correct a missing or wrong place?"
description: "Add or correct places in Organic Maps, upload offline edits to OpenStreetMap and troubleshoot unavailable editing or upload errors."
updated: "2026-11-06"
taxonomies:
  faq: ["map-editing"]
extra:
  order: 20
---

[OpenStreetMap](https://www.openstreetmap.org/) is a worldwide map database maintained by contributors. Organic Maps uses its data for places, roads, paths, and routing. Improving OpenStreetMap can therefore help Organic Maps and other apps that use the same data.

To add a place or correct its details:

1. Update the downloaded map for the region.
2. Create an [OpenStreetMap account](https://www.openstreetmap.org/user/new) if needed, then sign in to it through the OpenStreetMap settings in Organic Maps.
3. Select an existing place and tap **Edit place**, or choose **Add a place** in the main menu and position the new place accurately.
4. Choose the appropriate category for a new place, then fill in or correct details such as its name, opening hours and website.
5. Save your changes. Connect to the internet so the app can upload them.

A private bookmark does not add a public place to OpenStreetMap. The built-in editor handles supported points of interest; to add roads, lakes or building outlines, or to move an existing place, use an [OpenStreetMap editor](@/faq/editing/advanced-map-editing/index.md). If the needed category or field is unavailable, [report the correction in a note](@/faq/editing/advanced-map-editing/index.md#osm-note).

## Why is Edit place unavailable? {#editing-disabled}

Download and update the map for that region and update the app. Editing can be disabled when the installed map is too old. Some objects and fields are not editable in Organic Maps even with a current map.

For an unsupported change, use an [OpenStreetMap editor](@/faq/editing/advanced-map-editing/index.md) or [add a note](@/faq/editing/advanced-map-editing/index.md#osm-note). A missing **Edit place** button does not necessarily mean that your OpenStreetMap account is broken.

## When are offline map edits uploaded? What if uploading fails? {#upload-edits}

Organic Maps stores supported edits locally while you are offline. Sign into OpenStreetMap and reconnect to the internet so the app can upload them. Open the app and allow time for uploads. Changes are not public until the upload succeeds.

To inspect pending edits and errors, enter `?edits` in search. If uploads fail, check your connection and OpenStreetMap login, then [report the displayed error](@/faq/app/report-a-bug/index.md). Do not uninstall the app or clear its data while you still have unsent edits.

Other users receive your uploaded changes through a later Organic Maps [map-data snapshot](@/faq/map/update-offline-maps/index.md#map-data-date), rather than immediately after upload.
