---
title: "How do I import bookmarks and GPX tracks into Organic Maps?"
description: "Import KML, KMZ, KMB, GPX, GeoJSON and supported Google Takeout files into Organic Maps, with steps for Android and iOS."
updated: "2026-11-09"
taxonomies:
  faq: ["bookmarks-and-tracks"]
extra:
  order: 30
---

Organic Maps imports KML, KMZ, KMB, GPX, and GeoJSON files. Supported JSON imports also include Google Takeout's **Saved Places.json**; this does not mean that every JSON file or every Google Maps export layout is supported. [KML polygon import, export, and rendering](@/faq/bookmarks/how-to-import/index.md#kml-polygons) are being prepared for an upcoming release.

Download the file to your device, then use its **Open with** or **Share** action and choose Organic Maps. You can also use **Import Bookmarks and Tracks** inside the app. On iOS, choose one supported file in the file picker; a KMZ backup can contain several lists. On Android, you can choose a folder and import supported files from it and its subfolders, subject to Android's storage-access restrictions.

Check the imported list in **Bookmarks and Tracks**. If a file will not open, make sure it is downloaded locally, update the app, and retry through the app's import control. If it still fails, [report the format, error, and a non-private example file](@/faq/app/report-a-bug/index.md). Reimporting can create duplicates; check the list before repeating it.

For exports from another app, see [moving saved places from Google Maps or MAPS.ME](@/faq/bookmarks/import-from-google-maps-and-mapsme/index.md). To use an imported GPX file, see [tracks and navigation](@/faq/navigation/navigate-gpx-track/index.md).

## Can I import, display, and export KML polygons? {#kml-polygons}

KML polygon support is being prepared for release. Polygons represent areas, such as a park boundary or a survey area, and this feature will display those shapes on the map alongside saved places and tracks.

Use KML or KMZ to preserve polygon areas when sharing or backing up this data. GPX does not support polygon areas.
