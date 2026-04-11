---
title: "Hiking and cycling routes with elevation charts, smarter US address search, seamless map wrapping at the antimeridian, and more in April's Organic Maps update"
date: 2026-04-07
slug: "hiking-cycling-routes-elevation-charts-us-address-search-antimeridian-map-wrapping-april-2026-organic-maps-update"
taxonomies:
  news: ["Releases"]
---

This April release, in addition to many bug fixes and improvements, is built around three simple truths: hikers want to know how much they'll climb, everyone wants their search address to just work, and no one should feel like they're falling off the edge of the map. Thanks to our contributors, your good reviews, [donations](@/donate/index.md), and [support](@/contribute/index.md), we've tackled all three — and a whole lot more.

Whether spring is pulling you out onto new trails or autumn in the southern hemisphere is calling for one last long ride, we hope this update makes your next trip a little easier and a lot more beautiful.

Get the April update at <https://get.omaps.org> or on the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], and [F-Droid][fdroid].

## Highlights

- **Tap a trail, see the climb.** Hiking and cycling routes are now selectable directly on the map. Tap a route to highlight it and instantly see its elevation profile.
- **Two million more US addresses and smarter search.** More addresses, parsed from the TIGER Census dataset now live inside the app. In addition to smarter house numbers matching, that improves search results everywhere. Don't forget that adding missing addresses to [OpenStreetMap](https://www.openstreetmap.org) is always the best way to improve the search.
- **A map without edges.** Organic Maps now wraps smoothly across the antimeridian (±180° longitude). Drag and rotate between Chukotka and Alaska, or New Zealand and Fiji with no invisible walls and no awkward resets — the Pacific finally feels round.
- **Repaint a whole category at once.** Change every bookmark and/or track color inside a category in one tap — a small touch that turns last summer's messy trip archive into something you actually want to open.

## Release notes

### All platforms

- NEW! Better search in the USA, with two million additional addresses parsed from TIGER Census data (Viktor Govako)
- NEW! Improved multi-color rendering for hiking and cycling routes; tap a route to select it and view its elevation chart (Viktor Govako)
- OpenStreetMap data updated as of April 4
- Wikipedia data updated as of April 1
- Adjusted elevation gain and loss approximation on track graphs to better match values shown in other apps (Viktor Govako)
- You can now add a new place to OpenStreetMap after selecting your current position on the map (Mikhail Listratsenka)
- Added icons for food courts and city gates (David Martinez)
- Added clothing shop subcategories: women, men, children, wedding, sports, and underwear, plus office types (Viktor Govako)
- Updated search categories: added "Bread" for bakeries, "Shawarma" cuisine, and other synonym improvements (Viktor Govako)
- The map now wraps correctly at the antimeridian (±180° longitude) while dragging and rotating (Alexander Borsuk, Viktor Govako)
- Cycling navigation now uses compass heading at low speeds (HossamSaberr)
- Improved house-number address search (Viktor Govako)
- Fixed a system error when planning routes near some regional borders (Viktor Govako)
- Fixed search results when city and state names are the same (Viktor Govako)
- Added US street synonyms: highway, hwy, freeway, and fwy (Viktor Govako)
- Fixed editor crosshair misalignment when pressing "Add Place" (José Araújo)
- Fixed opening hours display for places with sunrise/sunset offsets (Alexander Borsuk)
- Fixed GPS track recording dropping points between segments (Alexander Borsuk)
- Fixed daylight saving time handling for time zones (Andrei Shkrob)
- Fixed Sydney subway line colors (Alexander Borsuk)
- Fixed GeoJSON import (Alexander Borsuk)
- Improved stability and performance (Alexander Borsuk, Viktor Govako)
- Updated translations (Alexander Borsuk, Viktor Govako, Weblate contributors)

### iOS

**Heads up for older iPhone and iPad owners:** due to recent changes in TestFlight and the App Store, this release supports only iOS 15 and later. iOS 12, 13, and 14 are no longer supported. Previously installed versions of Organic Maps will continue to work on older devices, but new maps, features and fixes will now arrive only on iOS 15 and above.

- NEW! Change all bookmark and track colors in a category at once (Kiryl Kaveryn)
- Improved display of HTML content with tables and images in bookmark details (Alexander Borsuk, Kiryl Kaveryn)
- Added vertical separators for multi-segment tracks in the elevation chart (Kiryl Kaveryn)
- Fixed point selection in the elevation chart for interpolated points (Kiryl Kaveryn)
- Improved modal gestures: snap to the nearest step, close on edge pan, and restore the previous state when reopened (Kiryl Kaveryn)
- You can now start a valid route even when prompted to download additional maps (Kiryl Kaveryn)
- Increased the touch area of buttons in the "Add Place" navigation bar (Noahdyn)
- Fixed a crash when exporting tracks (Alexander Borsuk, Kiryl Kaveryn)
- Fixed bookmark/track list search when tapping it from Place Details (Kiryl Kaveryn)

### Android

- NEW! Change all bookmark and track colors in a category at once (Mikhail Listratsenka)
- NEW! Scheduled appearance mode in Settings for automatic light/dark theme switching based on sunrise and sunset (Dzmitry Strekha)
- Added recently used category history in the map editor (Mikhail Listratsenka)
- Added a tram icon for tram stops selected on the map (Mikhail Listratsenka)
- Hide the download button when all maps are already downloaded (Mikhail Listratsenka)
- Fixed uploading map edits to OpenStreetMap (Viktor Govako)
- Fixed file sharing to Google Drive and other apps (Alexander Borsuk)
- Fixed bookmark re-import when reopening the app from recent apps (Alexander Borsuk)
- Opening OpenStreetMap search URLs such as `openstreetmap.org/search?query=Pizza` now launches search in Organic Maps (Rawdyrathaur)
- Fixed several crashes (Alexander Borsuk)

### Desktop (Linux and Mac OS)

- Added the ability to select a guide track for routing (Viktor Govako)
- Fixed bookmarks/tracks save or export producing broken files in some locales because of locale-dependent decimal separators (Alexander Borsuk)


Join beta testing to try early features and report issues:
- [iOS][testflight]
- [Android][firebase]

With love and care ❤️
The Organic Maps Team

{{ references() }}
