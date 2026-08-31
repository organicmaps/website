---
title: "Multi-selection for bookmarks and tracks, a CarPlay dashboard, hiding tracks on the map, and readable share links in the August 2026 update"
date: 2026-08-31
slug: "multi-selection-bookmarks-tracks-carplay-dashboard-hiding-tracks-share-links-august-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 02-bookmarks-tracks-multi-selection.jpg
---

Get the August 2026 Organic Maps release at <https://get.omaps.org> or on the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium] ([Accrescent][accrescent] and [F-Droid][fdroid] are coming soon too).

Why update?
- Multi-selection in Bookmarks and Tracks with batch delete, move, and color change
- CarPlay dashboard
- Hiding individual tracks on the map
- Readable share links for places, bookmarks, and current position — plus AirDrop on iOS and a Share action on Desktop
- Voice guidance in Armenian and Lao
- Wikipedia articles in 19 languages
…and many other improvements, bug fixes, and updated map data below.

Also, don't forget to check the previous release notes for [June](@/news/2026-06-29/610/index.md) and the [July update](@/news/2026-07-23/620/index.md).

## Full Changelog

### Map & places

- Updated OpenStreetMap data as of August 26, 2026 _(Viktor Govako)_
- Updated Wikipedia articles in Arabic, Bengali, Chinese, English, French, German, Hindi, Italian, Japanese, Korean, Marathi, Polish, Portuguese, Russian, Spanish, Tamil, Telugu, Turkish, and Urdu _(Alexander Borsuk)_
- Fixed many issues that caused opening hours to be displayed incorrectly _(Alexander Borsuk)_
- Added support for bird hides _(Batmaclos, Viktor Govako)_
- Added stages, hills, and natural arches to the map, plus a new icon for rocks _(David Martinez)_
- Resized the icons for peaks, caves, and mountain passes _(David Martinez)_
- Protected areas, national parks, and wetlands are now displayed in lighter shades _(Alexander Borsuk)_
- Fixed an app freeze and an issue that occasionally caused taps and gestures to be ignored _(Alexander Borsuk)_

### Sharing, bookmarks & tracks

- Sharing a place, bookmark, or current position now sends a readable link with useful information _(Alexander Borsuk)_
- Exported bookmarks now preserve their original names and descriptions _(Alexander Borsuk)_
- Shared bookmark lists now use their displayed names instead of internal file names _(Alexander Borsuk)_
- Fixed an elevation chart display issue that could occur immediately after starting a track recording _(Kiryl Kaveryn)_

### Routing & navigation

- Tapping a route stop or mark now opens it correctly instead of switching between planned routes _(Viktor Govako)_
- Public transport routes are now planned faster _(Viktor Govako)_
- Fixed incorrect turn instructions _(Alexander Borsuk)_
- Fixed an incorrect start point after a route was rebuilt _(Viktor Govako)_
- Laterite roads are now treated as having a poor-quality unpaved surface during route planning _(Julien Etienne)_
- Roads tagged `access=unknown` are now handled like roads with private or destination-only access _(Julien Etienne)_
- Added voice guidance in Armenian and Lao _(Alexander Borsuk)_

### OpenStreetMap editor

- Clearing the opening hours field no longer leaves the Save or Done button disabled _(Alexander Borsuk)_
- Uploads that partially fail are now retried instead of being reported as fully successful _(Alexander Borsuk)_

### Translations

- Updated the [Frequently Asked Questions](https://organicmaps.app/faq/), including the Japanese translation _(Alexander Borsuk)_
- Corrected the Japanese translation of "Closed now" _(Viktor Govako)_
- Improved the Chinese translations of "track" and "disable" _(Chenxi Zhao)_

### iOS

- NEW: Added multi-selection to the Bookmarks and Tracks list, with batch actions to delete, move, and change the color of selected items, plus Select All and Deselect All _(Kiryl Kaveryn)_
- NEW: Added a CarPlay dashboard _(Kiryl Kaveryn)_
- Added AirDrop support for sharing places _(Kiryl Kaveryn)_
- Fixed multiple CarPlay issues _(Kiryl Kaveryn, Alexander Borsuk)_
- Fixed the rendering of HTML descriptions when a bookmark is selected on the map _(Kiryl Kaveryn)_
- Fixed the activation of the car navigation map style _(Kiryl Kaveryn, Alexander Borsuk)_
- Reorganized settings into General Settings, Map, Navigation, Network, and Privacy sections _(Kiryl Kaveryn)_
- Removed the compass calibration setting because calibration is now handled automatically _(Kiryl Kaveryn)_
- Restored the custom color picker in the color palette popover _(Kiryl Kaveryn)_
- The corresponding point is now shown on the map while you drag across the elevation profile in a walking or cycling route preview _(Kiryl Kaveryn)_
- Fixed compass issues that could cause the current-position arrow to point in the wrong direction or freeze _(Alexander Borsuk)_
- Fixed a crash when an OpenStreetMap upload finished in the background _(Alexander Borsuk)_

### Android

- NEW: Added multi-selection mode to the Bookmarks and Tracks list. Enter it by long-pressing an item or using the toolbar, then change the color, move, or delete any combination of bookmarks and tracks _(Mikhail Listratsenka)_
- NEW: Individual tracks can now be hidden from the map using the eye icon in the list or on the track details screen _(cyber-toad)_
- Android Auto and Android Automotive: fixed U-turn lane arrows _(Andrei Shkrob, Viktor Govako)_
- Android Auto and Android Automotive: fixed day/night mode switching _(Andrei Shkrob)_
- Android Auto and Android Automotive: the search list now remains open while typing _(Viktor Govako)_
- The list description is now shown when the list is sorted _(Mikhail Listratsenka)_
- Updated the design of the bookmark list settings screen _(Mikhail Listratsenka)_
- The search panel now collapses after you tap a category _(Mikhail Listratsenka)_
- Keyboard focus now returns to the search field after you clear it _(Mikhail Listratsenka)_
- The route elevation chart now uses the full width of the panel _(Mikhail Listratsenka)_
- Fixed an issue that could leave the zoom buttons stuck at the top _(Mikhail Listratsenka)_
- Dialog corners are now rounded consistently on all Android versions _(Mikhail Listratsenka)_
- Fixed a crash in the track export menu _(Mikhail Listratsenka)_
- Fixed app freezes _(Alexander Borsuk, Viktor Govako)_
- Fixed duplicate imports of KML and KMZ files and a "file could not be opened" error _(Alexander Borsuk)_
- Fixed search categories in Brazilian Portuguese, Mexican Spanish, and British English _(Alexander Borsuk)_
- Search now works correctly in the keyboard language when it differs from the interface language _(Alexander Borsuk)_
- OpenStreetMap edits are no longer lost when an upload takes too long or partially fails _(Alexander Borsuk)_

### Desktop

- Added a Share action to the place page, with Copy Link, Copy Text, and Email… options _(Alexander Borsuk)_
- The download spinner is now drawn programmatically, keeping it sharp on every display _(Kuzey Bilgin)_

## How to support Organic Maps

- [Donate](@/donate/index.md) to support development and cover map hosting costs
- [Send your feedback and contribute](@/contribute/index.md) to the project
- Join beta testing to try early features and report issues for [iOS][testflight], [Android][firebase], and [Desktop][flathub]
- Spread the word!

With love and gratitude to all our users and contributors,<br/>
Organic Maps Team

{{ <references lang /> }}
