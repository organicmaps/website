---
title: "October 23 Release: Organic Maps as default navigation app in EU on iOS, road shields displaying on Android, and more improvements and fixes"
date: 2025-10-23T17:20:21+00:00
slug: "october-23-release-organic-maps-default-navigation-app-eu-ios-road-shields-displaying-android-improvements-fixes"
taxonomies:
  news: ["Releases"]
---

In the October 23 release we focused on fixes and improvements. Check the detailed list below.

For those who missed, the [previous October 7 update](https://organicmaps.app/news/2025-10-07/android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display/
) added GeoJSON import, recording track statistics, speed limit display in Android Auto, displaying of OSM description tags (type `?description` in the search box to see them), saving a bookmark on a track on iOS, and many other improvements.

## All Platforms

- Fresh OpenStreetMap data from October 21, 2025 (Viktor Govako)
- Show names of subway entrances/exits on the map (Viktor Govako)
- New POI types and icons: monitoring stations, traffic islands, Kneipp water cure facilities, miniature railways (Viktor Govako), camp pitches in outdoors style, airport terminals, indoor play areas, telecommunication shops, boat rental facilities, slipway facilities, updated waste disposal and landfill icons (David Martinez)
- Slovenian app interface translations (Alexander Borsuk) and TTS voice guidance for navigation (Erik Bucik)
- On some devices/screens, the map in city centers is now less cluttered (Viktor Govako)
- Fixed map rotations on bad compass sensors when walking in pedestrian navigation mode (Viktor Govako)
- Improved information displayed after selecting a river or waterway segment (Viktor Govako)
- Better EV charging station search with improved synonyms in all languages (Alexander Borsuk)
- Fixed emoji search with variant selectors (Alexander Borsuk)
- Fixed too many search results displayed for some full address match queries (Viktor Govako)
- Importing GeoJSON from https://umap.openstreetmap.fr/ should now preserve all metadata (Shubh Kesharwani)
- Additional colors are supported for waymarked trails for the Hiking Routes map layer (Viktor Govako)

## iOS

- EU users can set Organic Maps as the default navigation app in iOS Settings → Apps → Default Apps → Navigation (Kiryl Kaveryn)
- Fixed white-on-white status bar in navigation mode (Kiryl Kaveryn)
- Increased Start Navigation button size (Kiryl Kaveryn)
- Removed empty space when planning a route on iPad (Kiryl Kaveryn)
- Organic Maps may ask you to rate it in the App Store. Your good reviews are motivating our team!

## Android

- Road shields now appear in navigation directions (Andrei Shkrob)
- Track recording information improvements (Kavi Khalique)
- Organic Maps works on some older Intel x86 devices (Andrei Shkrob)
- Fixed TTS voice directions not working in some cases (Andrei Shkrob)
- Better splash screen on startup (Andrei Shkrob)

### Android Auto
- Restore the route after cancellation (Andrei Shkrob)
- Fixed crashes on some devices (Andrei Shkrob)

## Linux/Mac OS

- POI details now show "name | ref" format (Viktor Govako)
- dark mode automatically syncs with system settings (DeepChirp)

## Footnotes

Organic Maps is possible thanks ❤️ to our contributors, [your donations](@/donate/index.md), and [your support](@/contribute/index.md).

Get the latest Organic Maps version from the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], and [F-Droid][fdroid].

P.S. Join beta testing for early features:
- [iOS][testflight]
- [Android][firebase].

With love to our users and community
The Organic Maps Team

{{ references() }}
