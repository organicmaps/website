---
title: "Bugfixes and improvements for public transport, routing, search, and bookmarks in the July 2026 update"
date: 2026-07-23
slug: bugfixes-and-improvements-for-public-transport-routing-search-and-bookmarks-july-2026
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

As you may have already noticed, the July Organic Maps update is out. Get it at <https://get.omaps.org> or on the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], and [F-Droid][fdroid].

Thanks to your [donations](@/donate/index.md) and [feedback](@/contribute/index.md), in July we focused on bugfixes and improvements. In case you missed it, the following features from the [previous June release](@/news/2026-06-29/610/index.md) are also available:
- Public transport routes (live schedules are in development)
- Satellite imagery
- Alternate routes for driving, hiking, and cycling
- New search and route planning interface for Android
- Support for large accessibility fonts on iOS

## Detailed changelog

### Map & places

- OpenStreetMap data updated as of July 14
- Notes reported to [OpenStreetMap](https://www.openstreetmap.org) are now placed on the exact spot you selected, instead of in the middle of the whole street or area _(Alexander Borsuk)_
- Improved place selection when tapping the map in regions that cross the 180° antimeridian _(Viktor Govako)_
- Track elevation profiles no longer show outdated or empty charts after a track is deleted _(Kiryl Kaveryn)_

### Public transport

- Stop, transfer, and station names now have a white outline to stay readable in both light and dark themes _(Viktor Govako)_
- The subway layer reappears correctly after you close a public transport route preview _(Mikhail Listratsenka)_

### Routing & navigation

- Route warnings (tolls, ferries, unpaved roads, steps, and so on) are now shown for all alternate routes _(Viktor Govako)_
- Fixed a rare freeze while building a route _(Viktor Govako)_
- Improved handling of dead ends and of start and finish points on restricted roads _(Viktor Govako)_
- Fixed incorrect and missing turn instructions _(Alexander Borsuk)_

### iOS

- New "Save search history" setting that lets you turn the history off and hide it if you would rather not keep it _(Kiryl Kaveryn)_
- New Edit button to remove bookmarks more easily _(Kiryl Kaveryn)_
- Bookmarks are now saved automatically when you leave the screen _(Kiryl Kaveryn)_
- The color palette now offers predefined colors and lets you choose any custom color _(Kiryl Kaveryn)_
- Improved the empty state of the elevation chart for a recorded track _(Kiryl Kaveryn)_
- Improved the route progress shown on the Start button _(Kiryl Kaveryn)_
- Reordering route stops no longer makes the list jump around _(Kiryl Kaveryn)_
- Other minor interface improvements _(Kiryl Kaveryn)_

### Android

- Opening hours now show split shifts (such as a lunch break), start from today, and display the whole week without a separate scrolling area _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Cleaner search bar with a combined clear and voice button, a clear icon that no longer moves, and layout fixes for landscape mode and phone rotation _(Mikhail Listratsenka)_
- Reworked bookmark and track editor _(Mikhail Listratsenka)_
- Route planning fixes and improvements _(Mikhail Listratsenka)_
- The color picker now closes automatically, and a crash on Android 5 is fixed _(Mikhail Listratsenka)_
- Fixed crashes _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop

- The list of maps available for download is now sorted alphabetically _(goncalo109560)_

### Translations

- Improved Chinese wording _(Chenxi Zhao)_
- Updated Ukrainian translations _(Nnifria)_
- Fixed Italian translations of map region names _(Vittorio Bertola)_

## Join beta testing to try early features and report issues:

Hint: the beta version has new hillshading, improved elevation data with support for feet and meters, and other cool features!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Happy summer!
Organic Maps Team

{{ references() }}
