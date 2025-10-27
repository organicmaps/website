---
title: "September 15 Release: New Route Planning and OSM Descriptions"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

This second September release brings a redesigned route planning screen and the ability to view OpenStreetMap `description` tag contents for iOS users. To discover places that have this tag, type `?description` in the search box (similar to typing `?wiki` for Wikipedia-linked places).

There are also many fixes and improvements on both iOS and Android (details below).

And, of course, a reminder about other recent features you might have missed:
- Public transport route numbers when selecting a bus stop
- Hiking and cycling routes (toggle them via the Layers button in the top left)
- Enable bookmark names on the map in the app Settings
- The ✎ pencil icon offers a quick way to edit bookmarks

Organic Maps is possible thanks to our contributors, [your donations](@/donate/index.md), and [your support](@/contribute/index.md).

### Detailed Release Notes

- New OpenStreetMap data as of September 13
- Removed tiny islands from the world map (Viktor Govako)
- Show postcode / ZIP code in address details (Viktor Govako)
- Fixed incorrect map centering on current position (Kiryl Kaveryn, Viktor Govako)
- Preserve bookmark colors when exporting and importing GPX (cyber-toad)
- Updated translations (Weblate contributors)

#### Map Styles (by Viktor Govako)

- Display lighting shops
- Show power lines from zoom 18
- Show reference names for power stations and substations
- Show campsites and caravan sites in navigation mode
- Fix secondary highway color in navigation mode
- Draw national park borders
- Draw archaeological sites from zoom 12 in Outdoor style

#### iOS

- NEW: Show OSM `description` tag contents (type `?description` in the search box to test) (Kiryl Kaveryn, Viktor Govako)
- NEW: Redesigned route planning screen (Kiryl Kaveryn)

#### Android

- New roundabout icons in Android Auto (Andrei Shkrob)
- Show bookmarked place category when it is selected (Alexander Borsuk)
- Fix delay when displaying distance to a bookmarked place (Alexander Borsuk)
- Refactored dark theme (Andrei Shkrob)
- Fix position update bug in Navigation on custom ROMs (e.g. Lineage + MicroG) (Viktor Govako)
- Blue pencil (edit) icon for bookmarks (Alexander Borsuk)
- Reduce vertical space of place information preview (Alexander Borsuk)
- Remove azimuth-to-North angle from place information preview (tap on the blue arrow with distance to see it) (Alexander Borsuk)

Get the latest Organic Maps version from the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], and [F-Droid][fdroid].

P.S. Join beta testing for early features: [iOS][testflight] / [Android][firebase].

{{ references() }}
