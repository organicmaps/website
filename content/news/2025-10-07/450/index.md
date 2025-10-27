---
title: "October 7 Release: Android Auto speed limits, GeoJSON import, recording track stats, OSM description tag display, save bookmark on the selected track on iOS, and more"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

This October 7 Organic Maps update adds speed limit display in Android Auto, GeoJSON import, recording track statistics, shows OSM description tags (type `?description` in the search box to see them), and saves a bookmark on a track on iOS. There are also many improvements to the user interface, OpenStreetMap editing, and various bug fixes across all platforms, including the crash fix on startup on some Android devices.

Organic Maps is possible thanks ❤️ to our contributors, [your donations](@/donate/index.md), and [your support](@/contribute/index.md).

### Detailed Release Notes (including the previous minor update changes)

- NEW! Import GeoJSON (Sergiy Kozyr)
- OpenStreetMap data as of October 4
- Wikipedia data as of October 1
- Seattle light rail support for Public Transport (tjasz)
- Do not deactivate map selection when saving an edited OSM place (Kiryl Kaveryn)
- Updated translations (Weblate contributors)

#### Map Styles

- Show bicycle rental shops tagged as amenity=bicycle + rental=shop (David Martinez)
- Show historic archaeological sites from zoom 12 and other historic sites from zoom 15 in Outdoor style (Viktor Govako)
- New icons for mast, communication, and power towers in Outdoors style (David Martinez)
- Increase peak icon size in Outdoors style (David Martinez)
- Add missing POI icon variants (David Martinez)
- Added more barrier types (Viktor Govako)

#### iOS

- NEW: Save bookmark on selected track point (Kiryl Kaveryn)
- NEW: Delete the recording track without saving it first (Kiryl Kaveryn)
- Show multi-line bookmark list titles in Place Page (David Martinez)
- Update OSM login buttons style (Kiryl Kaveryn)
- Fix navigation info updating issue (Kiryl Kaveryn)
- Fix new route planning issues (Kiryl Kaveryn)
- Fix OSM add/edit place visibility for maps older than 3 months (Kiryl Kaveryn)
- Fix transport options segment control layout for iOS 26 (Kiryl Kaveryn)
- Simplify bookmark selection animations (Kiryl Kaveryn)
- Fix search result selection issue (Kiryl Kaveryn)
- Fixed styling, swipe and animations for Place Information Page (Kiryl Kaveryn)

#### Android Auto (Google Play only)

- NEW: Speed limit display in Android Auto (Andrei Shkrob)
- Fix display switching in Android Auto navigation mode (Andrei Shkrob)
- Fix routing arrow offset in Android Auto (Andrei Shkrob)
- Fix issue when a device is connected/disconnected to a car (Andrei Shkrob)
- Add Android Auto Location Service (Andrei Shkrob)
- Improve Android Auto route simulator (Viktor Govako)

#### Android

- NEW: View recording track statistics in real time (Kavi Khalique)
- NEW: Show OSM `description` tag content (Alexander Borsuk)
- Fix theme change handling (Andrei Shkrob)
- Fixed several crashes, including the one on the startup (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Silent download progress notifications (Viktor Govako)
- Reduce pencil icon padding (Alexander Borsuk)

#### Desktop

- Fix hanging curl on Linux (Alexander Borsuk)
- Fix hanging on macOS when logging in to OSM (Alexander Borsuk)
- Action to select feature from context menu (Viktor Govako)
- Cancel downloading option (Viktor Govako)
- Show geometry type in context menu (Viktor Govako)

### Recently released features you might have missed

- Public transport route numbers when selecting a bus stop
- Hiking and cycling routes (toggle them via the Layers button in the top left)
- See bookmark names on the map by activating it in the app Settings
- The ✎ pencil icon offers a quick way to edit bookmarks

### Install Organic Maps

Get the latest Organic Maps version from the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], and [F-Droid][fdroid].

Join beta testing for early features: [iOS][testflight] / [Android][firebase].

{{ references() }}
