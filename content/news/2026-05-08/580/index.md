---
title: "Tap a public transport stop to see transit routes on the map, bookmark labels no longer overlap, smaller downloaded regions in Vietnam, Malaysia, and southern China in May's Organic Maps update"
date: 2026-05-08
slug: "public-transport-stop-selection-not-overlapping-bookmark-labels-vietnam-malaysia-china-region-splits"
taxonomies:
  news: ["releases"]
---

May's update brings full public transport support in Organic Maps a step closer. A bus, train, ferry, or tram stop is a starting point for the transit lines that pass through it — so tapping a route at a stop now shows that line, in its own colour, all the way across the map. Actual online schedules are coming too, don't forget to [add/update OSM public transport data](https://gtfs-osm-matcher.organicmaps.app/) in your area if you haven't already!

As always, many thanks to our contributors, your good reviews, [donations](@/donate/index.md), and [support](@/contribute/index.md).

Get the May update at <https://get.omaps.org> or on the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], and [F-Droid][fdroid].

## Highlights

- **Tap a bus, tram, train, or ferry stop on the map,** and Organic Maps highlights the entire transit line, selectable from the list of displayed lines and routes.
- **Cleaner bookmark labels and a more legible map.** New label placement keeps bookmark titles from crowding each other out, pedestrian areas are a touch darker, and route colours have been tuned for better contrast on both light and dark themes.
- **Finer regions across Asia.** Vietnam and Malaysia are now split into smaller maps so you can download just the area you need, and Hong Kong, Macau, and Hainan are now separate from Guangdong.

## Release notes

### All platforms

- NEW! Tap a public transport stop and select a route number to highlight the entire transit route on the map, like in the Subway map layer (Viktor Govako, Kiryl Kaveryn, Mikhail Listratsenka)
- NEW! Bookmark labels on the map don't overlap (Viktor Govako)
- Corrected elevation loss and gain calculations on the track graphs to better match values from other popular apps (Viktor Govako)
- Long-distance public transport and other map relations are now stitched across map borders into a single continuous line (Viktor Govako)
- Vietnam and Malaysia split into smaller, individually downloadable regions (Viktor Govako)
- Hong Kong, Macau, and Hainan are separated from Guangdong, with neighbouring borders updated (Viktor Govako)
- Updated isolines (contour lines) for Indonesia, Malaysia, Tanzania, Thailand, and Vietnam (Viktor Govako)
- Routing: resumed routes now drop intermediate points you have already passed (Viktor Govako)
- Added icons for active volcanoes and waterway access points; slipways are now searchable (David Martinez)
- Added hookah lounges (alnzrv)
- Added buildings under construction (Viktor Govako)
- Added "Lookout" as a search synonym for viewpoints (alnzrv)
- Added "pkwy" as a US street synonym (Viktor Govako)
- Pedestrian area colours darkened slightly for better legibility (Viktor Govako)
- Multi-line text is now clipped cleanly on the map (Viktor Govako)
- Street names no longer contain duplicated parts (Viktor Govako)
- Fixed KMB file import (Alexander Borsuk)
- Updated translations across categories, search synonyms, and UI strings (Alexander Borsuk, Viktor Govako)
- New South Wales and Northern Territory descriptions translated (alnzrv)
- Improved stability and performance, including font shaping, glyph caching, and route line clipping (Viktor Govako, Alexander Borsuk)

### iOS

- NEW! Track recording button added to the in-navigation info panel (Kiryl Kaveryn)
- NEW! Two extra steps in the navigation dashboard for finer altitude/route information (Kiryl Kaveryn)
- Updated elevation chart style in the navigation dashboard, with correct rendering for tracks that have negative altitudes (Kiryl Kaveryn)
- Fixed wrong bookmark list shown in the TestFlight version (Alexander Borsuk)
- Larger Stop button and bigger touch targets for in-navigation bottom panel buttons: TTS mute, settings, track recording (Kiryl Kaveryn)
- Refined expandable description section animation in the place page (Kiryl Kaveryn)
- Place page no longer dismisses when the elevation chart scrub ends, no longer bounces unexpectedly, and keeps the title visible when editing with the keyboard up (Kiryl Kaveryn)
- Fixed elevation chart and circular progress colour issues when the system appearance changes (Kiryl Kaveryn)
- Fixed crashes when deleting a track or bookmark that no longer exists (Kiryl Kaveryn)

### Android

- NEW! Persistent altitude dashboard and refined route elevation profile, with proper RTL layout (Eric Jau, Mikhail Listratsenka)
- Saved route state is now preserved across device rotation (Mikhail Listratsenka)
- Single, unified route reference line in the place page (Mikhail Listratsenka)
- Larger corner radius for bottom sheets, buttons, and drawables for a more consistent look (Mikhail Listratsenka)
- Fixed layout glitches around the system bars and navigation bar (Mikhail Listratsenka)
- Improved Wikipedia article display with better formatting, system colours, and dark mode handling (DeshDeepakKant, Mikhail Listratsenka)
- Added vertical dividers between segments of multi-geometry tracks on the elevation graph (Mikhail Listratsenka)
- Improved elevation chart scroll behaviour (Mikhail Listratsenka)
- Right-to-left (RTL) layout fixes (Mikhail Listratsenka)

### Linux and Mac OS

- Added a public transport route selector to pick a specific transit line when a stop is selected (Viktor Govako)
- Show route action buttons directly in the place page (Viktor Govako)
- Removed duplicated opening hours from the place page (Viktor Govako)
- Intermediate route mark on a POI or address now shows the place's title (Viktor Govako)
- Map downloads resume where they left off on graceful shutdown (Alexander Borsuk)
- Organic Maps now works on OpenGL ES 3.0 drivers (Alexander Borsuk)

Join beta testing to try early features and report issues:
- [iOS][testflight]
- [Android][firebase]

We love our users ❤️ and we love what we do

The Organic Maps Team

{{ references() }}
