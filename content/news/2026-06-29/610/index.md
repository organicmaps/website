---
title: "Satellite imagery, public transport routes, alternate routes, new search and route planning interface for Android, large accessibility fonts support for iOS, and more in the June 2026 update"
date: 2026-06-29
slug: satellite-imagery-public-transport-routes-alternate-routes-new-search-and-route-planning-interface-for-android-large-accessibility-fonts
taxonomies:
  news: ["releases"]
---

There are many new exciting features and bugfixes in the June Organic Maps update to try out, including:
- Satellite imagery
- Public transport routes
- Alternate routes
- New search and route planning interface for Android
- Large accessibility fonts support for iOS

Get it at <https://get.omaps.org> or on the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], and [F-Droid][fdroid] and let us know what you think!

## Detailed changelog

- NEW! Public transport routing by subway, light rail, bus, and tram _(Viktor Govako)_
- NEW! Alternate routes: in addition to the fastest route, the app now shows the shortest route _(Viktor Govako)_
- NEW! Walking and cycling route warnings about steps, gates, and lift gates along the way _(Viktor Govako)_
- NEW! Select any color for bookmarks _(Alexander Borsuk, Mikhail Listratsenka)_
- NEW! Support for British National Grid (OS Grid), Irish Grid, and Irish Transverse Mercator (ITM) coordinates _(Alexander Borsuk)_
- EXPERIMENTAL: Enable Satellite Imagery in Organic Maps settings with a custom raster tile server URL. We are still working on our own server, so please find an openly available one with `{x}`, `{y}`, `{z}` placeholders in its URL _(Viktor Govako, renderexpert)_
- OpenStreetMap data updated as of June 24 _(Viktor Govako)_
- Wikipedia data updated as of June 20, including articles in Italian _(Alexander Borsuk)_
- Type `?map-download-server:https://your-server.com/` in the search window to override the Organic Maps map download servers. Type `?no-map-download-server` to remove the override _(Alexander Borsuk)_

#### Map rendering & styles

- Better-looking patterns for beach, sand, scree, bare rock, orchard, and vineyard areas, plus protected area and wetland hatching _(Alexander Borsuk)_
- Smoother curved text labels for roads and rivers _(Viktor Govako)_
- Rivers, streams, and wetlands have higher contrast and are more visible in dark mode _(Alexander Borsuk)_
- New and improved icons for category search and search results on the map _(Anton Makouski)_
- Improved multilingual text shaping and rendering _(Alexander Borsuk)_
- Various bug fixes and performance improvements _(Viktor Govako)_

#### Tracks, bookmarks & routes

- GeoJSON tracks now keep elevation and timestamps on import and export _(Alexander Borsuk)_
- Fixed a crash after moving a track to another list _(Viktor Govako)_
- Websites are now shown for heritage sites _(Viktor Govako)_
- Operator names are now shown for unnamed search results. For example, an unnamed ATM now shows its bank _(Anton Makouski)_
- Editor: corrected the description text for apartment-building OpenStreetMap edits/changesets _(titanniya542-spec)_
- Improved HTML detection in bookmark and track descriptions _(Alexander Borsuk)_

### iOS

- NEW! Accessibility support for Dynamic Type and large fonts _(Kiryl Kaveryn)_
- NEW! Tap to choose between overlapping tracks and routes _(Kiryl Kaveryn)_
- Improved HTML rendering of bookmark and track descriptions _(Kiryl Kaveryn)_
- Cleaner table styling in the UI _(Kiryl Kaveryn)_

### Android

- NEW! Search interface _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NEW! Routing interface _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Improved HTML rendering of bookmark and track descriptions _(Mikhail Listratsenka)_
- Reduced APK size _(Alexander Borsuk)_
- The voice icon is shown as disabled when no text-to-speech engine is available _(Mikhail Listratsenka)_
- Long bookmark and track descriptions now show a "…more" button _(Mikhail Listratsenka)_
- Various UI fixes and an API fix for returned point IDs _(Mikhail Listratsenka)_

### Desktop

- Support for switching the displayed coordinate system _(Alexander Borsuk)_
- Information about the selected place is now displayed on the left _(Viktor Govako)_
- Fixed the context menu position _(Osyotr)_
- Fixed OpenStreetMap login and edits hanging on Qt versions 6.4 and earlier _(Alexander Borsuk)_
- Fixed unexpected map style switching during routing on macOS _(Alexander Borsuk)_
- Fixed a crash when closing the macOS app after exporting a KMZ file _(Alexander Borsuk)_

### Translations

- Cantonese turn-by-turn voice guidance _(Alexander Borsuk)_
- Updated German and French translations _(Wuzzy, Alexander Borsuk)_
- Fixed incorrect "onto street" voice guidance translations for Chinese, Serbian, and Catalan _(Alexander Borsuk)_

## Join beta testing to try early features and report issues:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

We are grateful to all our users and contributors, to those who [donate](@/donate/index.md) and give Organic Maps 5 stars in app stores. Together we can build the best maps app!

With love,
Organic Maps Team

{{ references() }}
