---
title: "Organic Maps November 2026 update: 3D terrain, ocean depths, imported areas, and route reversal"
date: 2026-11-11
slug: "3d-terrain-hillshading-ocean-depths-imported-area-polygons-on-the-map-route-reversal-november-2026"
taxonomies:
  news: ["Releases"]
---

Explore 3D terrain and ocean depths, reverse routes, and view imported areas and track direction arrows. Android adds detailed public transport directions, a redesigned speed display, and a track recording widget. See all improvements below.

Get Organic Maps at [get.omaps.org](https://get.omaps.org) and spread the word. Thanks to all our users, contributors, donors, and supporters!

## Release notes

### Map and places

- NEW! 3D terrain, ocean depths, contour lines in meters and feet, and elevation anywhere on the map _(Viktor Govako, Alexander Borsuk)_
- OpenStreetMap data as of November 10, 2026
- Wikipedia articles as of November 1, 2026
- Improved water colors, widened rivers, and added subtle outlines to water labels _(David Martinez, Viktor Govako)_
- Improved display of intermittent rivers, canals, drains, and other waterways _(Alexander Borsuk)_
- Added bridge outlines for trams, monorails, funiculars, and narrow-gauge railways _(Alexander Borsuk)_
- Added barbers, Pilates studios, window installers, waterworks, and covered reservoirs _(Viktor Govako)_
- Fixed gaps in filled areas, including missing water near the Arctic _(Viktor Govako)_
- Fixed transliteration _(Alexander Borsuk)_
- Improved performance and reduced memory use _(Viktor Govako)_
- Fixed a crash and rendering errors when switching map styles _(Mikhail Listratsenka)_
- Corrected download region boundaries _(Viktor Govako, Alexander Borsuk)_
- Search suggestions now keep original spelling, accents, and capitalization _(Alexander Borsuk)_
- Removed unrelated beauty salons from hairdresser and barber searches _(Viktor Govako)_

### Bookmarks, tracks, and areas

- NEW! Import and display KML, KMZ, and GeoJSON areas with colored outlines, fills, and holes _(Alexander Borsuk, Viktor Govako)_
- Added track direction arrows _(Alexander Borsuk)_
- Selected tracks are now highlighted _(Alexander Borsuk)_
- Opening a track from a list selects its start _(Alexander Borsuk)_
- Bookmark and track names now sort correctly for your language _(Alexander Borsuk)_
- Bookmark list names, descriptions, and images now update after reload _(Kiryl Kaveryn, Alexander Borsuk)_
- Saved KML routes keep intermediate stops and travel mode. GPX and GeoJSON exports include stops as waypoints _(Alexander Borsuk)_
- Fixed crashes when deleting edited tracks or returning to an open deletion dialog _(Viktor Govako)_
- Track recordings now save every minute for crash recovery _(Viktor Govako)_
- Fixed duplicate map counts and inflated download sizes in update summaries _(Alexander Borsuk)_

### Routing and navigation

- NEW! Separate route avoidance settings for driving, cycling, and walking _(Alexander Borsuk, Mikhail Listratsenka)_
- Connected route point icons and clarified “Add destination” labels on Android and iOS _(Kiryl Kaveryn, Mikhail Listratsenka)_
- You can add destinations even if route calculation fails _(Kiryl Kaveryn)_
- Improved routing algorithm _(Viktor Govako)_
- Improved route recalculation _(Alexander Borsuk)_
- Fixed mismatched route durations on the map and information panel _(Alexander Borsuk)_
- Fixed outdated speed camera warnings and delayed speed limit updates _(Alexander Borsuk)_
- Fixed issues with saved routes _(Alexander Borsuk)_
- Improved route restoration _(Alexander Borsuk, Mikhail Listratsenka)_
- Improved public transport arrival estimates, walking connections, and station entrance markers _(Alexander Borsuk)_

### OpenStreetMap editor

- Improved category search _(Alexander Borsuk)_
- Cuisine names now sort correctly for your language _(Alexander Borsuk)_
- Fixed category sorting _(Alexander Borsuk)_

### Translations

- Added Welsh: app interface, place types, search categories, and download region names _(Carl Morris, Alexander Borsuk)_
- Added system language options: Android (Asturian, Galician, Croatian, Armenian, Icelandic, Lao, and Albanian) and iOS (Asturian, Canadian French, Galician, Croatian, and Icelandic) _(Alexander Borsuk)_
- Corrected Slovenian search categories _(Alexander Borsuk)_
- Improved Ukrainian, Czech, Swedish, and Korean translations; fixed wording and brand spelling in other languages _(Nnifria, Alexander Borsuk, bilykralik16, Jonatan Nyberg, Dmitry Gribenchuk, M)_
- Corrected distance and duration units and public transport platform labels _(Alexander Borsuk)_
- Improved Arabic and Czech spoken directions; fixed Catalan, Danish, and Galician navigation distances _(Alexander Borsuk, Anquanna)_
- Fixed Norwegian Bokmål place names and uploads of edited names _(Alexander Borsuk)_
- About page links now open the correct language groups _(Alexander Borsuk)_

### iOS

- NEW! Added a button to reverse routes with all stops _(Kiryl Kaveryn)_
- Remove any route point from the planner, including the start and destination _(Kiryl Kaveryn)_
- Improved navigation voice sorting and added missing preview phrases _(Alexander Borsuk, Kiryl Kaveryn)_
- Fixed dark mode readability for ruler distances and pressed route point labels _(Alexander Borsuk)_
- Improved public transport previews: more symbols, clearer line colors, wrapped line numbers, and better right-to-left layouts _(Alexander Borsuk, Kiryl Kaveryn)_
- Fixed the compass button in right-to-left layouts _(Kiryl Kaveryn)_
- Fixed place details that stayed open after dismissal, moved during drags, or disappeared when opening another map link _(Kiryl Kaveryn)_
- Fixed a crash when map downloads update place details before loading finishes _(Kiryl Kaveryn)_
- Highlighted the main action in place details _(Kiryl Kaveryn)_
- Fixed menu and Settings links, including scrolling to and highlighting options _(Kiryl Kaveryn)_
- Fixed confirmation buttons with large text when starting navigation for the first time _(Kiryl Kaveryn)_
- Fixed route point replacement at the stop limit and replacement labels for saved tracks _(Kiryl Kaveryn)_
- Fixed elevation profiles after returning to the map, selecting a track’s start, or viewing flat or zoomed sections _(Kiryl Kaveryn)_
- CarPlay bookmark lists refresh after edits and reloads, show all items that fit, and handle deleted entries _(Kiryl Kaveryn, Alexander Borsuk)_
- Fixed the routing settings indicator being cut off in previews _(Kiryl Kaveryn)_
- Improved canceling, retrying, and resuming downloads, including in the background _(Viktor Govako)_

### Android

- NEW! Redesigned speed and speed limit display, including in Android Auto _(Andrei Shkrob)_
- NEW! Full-screen public transport directions: boarding stops, transfers, exits, and expandable lists of intermediate stops _(Paal Williams)_
- NEW! Home screen widget to start track recording and show elapsed time, distance, and elevation _(Mikhail Listratsenka)_
- NEW! Added a button to reverse routes with all stops _(Mikhail Listratsenka)_
- NEW! Display and record altitude relative to mean sea level (MSL) _(Alexander Borsuk)_
- Added a one-time reminder to check battery restrictions when starting track recording, with a system settings shortcut. See <https://dontkillmyapp.com> _(Harsh Mishra, Alexander Borsuk)_
- Remove any route point from the planner, including the start and destination _(Mikhail Listratsenka)_
- Fixed interface issues and highlighted the main routing action in place details _(Mikhail Listratsenka)_
- Fixed Android Auto crashes _(Andrei Shkrob, Mikhail Listratsenka)_
- Category search results now clear when you tap Search again or stop navigation _(Mikhail Listratsenka)_
- Country folder icons now open their regions; old search results no longer replace open folders _(Mikhail Listratsenka)_
- Added “Bookmarks and Tracks backup” to Privacy settings, opening Android’s backup settings _(Mikhail Listratsenka)_
- Improved readability of bookmark and track descriptions in light and dark themes _(Mikhail Listratsenka)_
- Fixed editing of opening hours spanning 24 hours _(Alexander Borsuk)_
- Fixed arrival times across daylight saving time changes _(Alexander Borsuk)_
- Fixed editor crashes when tapping street or self-service options twice _(Kevin Coughlin)_
- Fixed crashes and incomplete imports of missing or unsupported bookmark files shared by other apps _(Darafei Praliaskouski)_
- Fixed Vulkan rendering errors and crashes when the graphics context changes _(Alexander Borsuk)_

### Desktop

- Translated the interface and place types; improved language fallback and right-to-left layouts _(Alexander Borsuk)_
- Fixed non-Latin links and description previews in place details _(Alexander Borsuk)_
- Fixed saving cuisine choices and deleting places in the OpenStreetMap editor _(Alexander Borsuk)_
- Fixed a crash when closing the map download window during searches _(Alexander Borsuk)_
- Fixed map rendering when resizing the window _(Alexander Borsuk)_
- Improved location updates and fixed the “My Position” button after location errors _(Alexander Borsuk, Vladislav Shadiuk)_

Try new features and help test them at <https://beta.omaps.app>.

Thanks for using and supporting Organic Maps!

Your Organic Maps Team

{{ <references lang /> }}
