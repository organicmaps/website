---
title: "Route optimization, improved alternative routes, hiding individual tracks, and intermittent water areas in the September 2026 update"
date: 2026-09-29
slug: "route-optimization-improved-alternative-routes-hide-individual-tracks-visibility-intermittent-water-areas-in-september-2026-update"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Ready to roll? The September update brings improved alternative routes, a setting to optimize the order of route stops, clearer markings for intermittent water areas, and an eye icon to hide individual tracks, along with many other fixes and improvements (see below).

Install or update Organic Maps via <https://get.omaps.org>, the [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], or [F-Droid][fdroid].

If you missed our previous updates, check out the features released in [June](@/news/2026-06-29/610/index.md), [July](@/news/2026-07-23/620/index.md), and [August](@/news/2026-08-31/630/index.md). Kudos to our contributors and users who made these updates possible!

## How to support Organic Maps

- [Donate](@/donate/index.md) to support development and cover map hosting costs
- [Send your feedback and contribute](@/contribute/index.md) to the project
- Join beta testing to try new features early and report issues on [iOS][testflight], [Android][firebase], and [desktop][flathub]
- Spread the word and help us build a better alternative to Big Tech maps!

## Release notes

### Map

- OpenStreetMap data as of September 28, 2026
- Wikipedia data as of September 21, 2026
- Fixed searches when the visible map area crosses the 180° meridian (±180° longitude) _(Viktor Govako)_
- Intermittent water areas are now shown with a dotted pattern, similar to the one used for sand _(Alexander Borsuk)_
- Water reservoirs are now visible when zoomed further out _(Alexander Borsuk)_
- Water tunnels are no longer shown on the map _(Alexander Borsuk)_
- Fixed Suzhou Metro station and entrance icons _(Alexander Borsuk)_
- Fixed rare cases where labels shifted out of position on the metro map layer _(Viktor Govako)_

### Routing and navigation

- Improved alternative routes and their estimated arrival times _(Alexander Borsuk, Viktor Govako)_
- The selected alternative route is now preserved when navigation recalculates the route _(Alexander Borsuk)_
- The order of route stops is now restored after restarting the app _(Kiryl Kaveryn)_

### Other improvements

- Opening hours now display “Noon” for 12:00 and “Midnight” for 00:00 or 24:00 _(Alexander Borsuk)_
- Fixed bugs and improved track recording _(Alexander Borsuk)_
- Fixed KMB file imports _(Alexander Borsuk)_
- Corrected French and Asturian translations _(Alexander Borsuk)_
- Fixed a typo in English _(Carl Morris)_

### iOS

- Added an eye icon to hide individual tracks _(Kiryl Kaveryn)_
- Added buttons to add or replace a stop in a planned route _(Kiryl Kaveryn)_
- Added a setting to optimize the order of intermediate route stops _(Kiryl Kaveryn)_
- Added maneuver instructions to supported car head-up displays (HUDs) and the CarPlay dashboard _(Kiryl Kaveryn)_
- Fixed CarPlay buttons and search _(Alexander Borsuk)_
- Fixed various bugs and improved the user interface _(Kiryl Kaveryn, Alexander Borsuk)_
- Added support for choosing and previewing an installed navigation voice _(Kiryl Kaveryn, Alexander Borsuk)_
- Restored category search in Spotlight _(Kiryl Kaveryn)_

### Android

- Added a setting to optimize the order of intermediate route stops _(Mikhail Listratsenka)_
- Added buttons to add or replace a stop in a planned route _(Mikhail Listratsenka)_
- Added the ability to stop track recording and save the track from the notification _(Alexander Borsuk)_
- The “Add Stop” button now adds a stop after the existing stops, before the destination _(Mikhail Listratsenka)_
- Improved uploads from the OpenStreetMap editor _(Owm)_
- Updated the user interface design _(Mikhail Listratsenka)_
- The bookmark editor and other dialogs now remain open during navigation _(Mikhail Listratsenka)_
- Fixed elevation chart rendering for flat tracks and in right-to-left interfaces _(Mikhail Listratsenka)_
- Fixed map buttons being cut off by system bars _(Mikhail Listratsenka)_
- Fixed bugs and improved Android Auto support _(Andrei Shkrob)_
- Fixed a crash during map rendering _(Viktor Govako)_

### Desktop

- Renamed the desktop executable and macOS app bundle to `OrganicMaps` _(Alexander Borsuk)_
- Fixed issues in the Windows app _(Osyotr, Alexander Borsuk)_
- The `--lang` command-line argument now overrides the app's language _(Alexander Borsuk)_

With joy and passion,

Your Organic Maps Team

{{ <references lang /> }}
