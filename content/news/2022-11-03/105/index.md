---
title: "Finally, after fixing some critical issues, the November Organic Maps update is available in the Apple Store, Huawei AppGallery, and on our Github"
date: 2022-11-03T17:30:48+00:00
slug: "finally-after-fixing-some-critical-issues-the-november-organic-maps-update-is-available-in-the-apple-store-huawei-appgallery-and-on-our-github"
---

Finally, after fixing some critical issues, the November Organic Maps update is available in the [Apple Store](https://apps.apple.com/app/organic-maps/id1567437057), [Huawei AppGallery](https://appgallery.huawei.com/#/app/C104325611), and on our [Github](https://github.com/organicmaps/organicmaps/releases/tag/2022.11.02-2-android). [Google Play](https://play.google.com/store/apps/details?id=app.organicmaps) and [FDroid](https://f-droid.org/en/packages/app.organicmaps/) are coming soon too.

Here is the full list of improvements, kudos to our contributors and our small team:

* New OSM data as of October 29
* Minor performance improvements
* Dump corrupted KMLs to the log on startup
* Do not strip non-ASCII characters from exported bookmark files
* Simplify/smooth road altitudes chart

Routing and Navigation:
* Show "Roads to avoid" options and warnings on the route also for walking, cycling, and metro routes
* Fixed some routing issues, including wrong routing via highway exits/links
* Enable Catalan TTS
* Show speed camera on tap

Search:
* Show all found results on the map screen
* Improved villages search
* Show only matched categories if they were selected from the list, not names
* Fixed street synonyms for nordic languages

Styles:
* Use regional metro/subway icons for entrances and stations
* Added brewery, plumber, tailor, carpenter, sawmill, beekeeper, blacksmith, electrician, painter, and other craft icons
* Added natural=shrubbery, natural=desert, leisure=dance, amenity=charging\_station-motorcar, and more barrier types
* Draw international airport icon on z7-9
* Draw metro for major cities starting from z12
* Do not draw railway station icon for building=train\_station
* Updated icons for garden, park, forest, national park, nature reserve, power, chimney
* Add historic battlefield, gallows, pillory, memorial cross, stolperstein and war\_memorial
* Fixed historic=\* priority
* Support sauna=yes tags
* Better colors for natural=scrub
* Draw entrance icon instead of a dot

Android
* Improved detecting current position
* Crossed out target icon means that you need to press it to detect current position
* Suggest turning on networking location service if it is disabled
* Hide system bars in full-screen mode
* On Android 13+ you can change OM language
* Use non-bold font in the Place Page title
* Properly handle notch on Android 8.1+
* Keep transparent status bar only on the map screen
* Fix crash on exit split screen
* Fix crash on login to OSM
* Fix crash in the "Location is disabled" dialog
* Crosshair [API](https://github.com/organicmaps/api-android) now supports "cll=lat,lon" argument to center the map
* Remove unused BATTERY\_STATS system permission
* Use numbers for transit intermediate points
* Add missing icons in the editor
* Improve Wikipedia description in the Place Page

iOS Place Page:
* Use system 12/24h time format
* Show Wikipedia and Wikimedia Commons links

Mac & Linux Desktop version:
* Fixed search indicator in Viewport mode
* Fixed search table update, now old results are always replaced by new ones

Translations:
* Use larger, more geographically significant names for Oregon maps in Downloader
* Updated Catalan, Chinese, Dutch, Finnish, German, Hungarian, Italian, Polish, Portuguese (European and Brazilian), Turkish translations
