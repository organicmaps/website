---
title: "Meet the second November update of Organic Maps"
date: 2022-11-30T09:58:35+00:00
slug: "meet-the-second-november-update-of-organic-maps"
---

Meet the second November update of Organic Maps! Enjoy your travels and share your experience with us. Let's make the best privacy-focused, fastest and easiest to use offline maps [together](https://organicmaps.app/donate)!

What was done in this release:

* New [OpenStreetMaps](https://www.openstreetmap.org/) data as of November 19
* Added [Organic Maps Mastodon account](https://fosstodon.org/@organicmaps) to follow in Help dialog
* Fixed bug in a wrong bicycle's speed used for routing algorithm

iOS 
* Secondary title in the local language is now displayed on the Place Page
* Fixed [Organic Maps Matrix room](https://omaps.app/matrix) link in Help dialog
* Fixed opening URLs with # and ? symbols
* Update About menu item
* Removed gray line from the menu
* Place Page properly displays 1 hour left before the place closes

Android 🤖
* The blue arrow is properly centered inside the position icon
* Links to our website in Help dialog are localized (en, ru, it, tr are supported at the moment, please help us with [site translations](https://github.com/organicmaps/organicmaps.github.io/#translations))
* Fixed navigation menu visible under navbar in some cases
* The distance to search results in the list is now properly displayed

Styles 🗺️
* Added healthcare=physiotherapist
* Fixed some wrong icons displayed on top of each other
* Added highway=busway type
* place=island and place=archipelago are now visible on the World map
* Fixed leisure area style
* Properly render waterway=dam as a background area
* Fixed water incorrectly drawn over the pier

Translations 🌐
* Added Estonian translations, thanks to Aulo Aasmaa [@auloaasmaa](https://t.me/auloaasmaa)!
* Updated Czech, Italian, Norwegian, Spanish, and Turkish translations
* Fixed missing RV category translations for search
* Fixed non-working Catalan categories search
* Use Metro instead of Subway for en-GB

Desktop 🖥️ (Linux, Mac OS X, Windows)
* Fixed build errors on GCC-12
* Fixed map dragging using the mouse
* "+" key zooms in the map
* Use high-resolution icons on high-DPI displays on Macs
* Improve documentation about running WSL and desktop app (native Windows version is [still in progress](https://github.com/organicmaps/organicmaps/tree/windows), please let us know if you are interested in it)
