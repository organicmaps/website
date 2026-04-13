---
title: "The May 2024 Organic Maps update with bookmarks and tracks sorting by name, better paved/unpaved paths colors, GPX import fixes, drive-thorough, and many other changes"
date: 2024-05-19T09:48:57+00:00
slug: "the-may-2024-organic-maps-update-bookmarks-and-tracks-sorting-by-name-gpx-fixes"
taxonomies:
  news: ["releases"]
---

The May 2024 Organic Maps update ([get it here](https://omaps.app/get)) supports bookmarks and tracks sorting by name, paved paths are white, and unpaved ones are brown. And there are so many other changes and fixes, thanks to our contributors! Update and enjoy, and don't forget to update maps too. And [donate](https://organicmaps.app/donate/) to [support](https://organicmaps.app/support-us/) the open-source, community-driven, privacy-focused maps project!

General:
* upgraded to the new [OpenStreetMap authentication method](https://github.com/organicmaps/organicmaps/issues/6144) (OAuth 2). All previously authenticated users must re-login!
* new OpenStreetMap data as of April 29
* sort bookmarks and tracks in a list by name
* more feature types could be added to OSM now, e.g. marketplaces, taxi stands, kiosks, wilderness huts, garden centers, historic aircraft, cannons, boundary stones, tombs, etc.
* show the availability of Drive-through service for selected POIs
* ability to toggle Drive through in the OSM editor
* simplify handling of multiple languages feature names in the OSM editor and fix related bugs
* show "Can't find a suitable category?" message hint in the OSM editor
* elevator icon instead of "stairs" for displaying the level number of selected POI
* fix missing local language name versions for selected POIs
* better visible in dark mode $ emoji for paid map features
* improve bicycle routing for some cases

Android:
* import .gpx and .gpx.xml files from Google Files app
* retain routing origin point upon re-opening the app
* night theme fixes
* fix router mode always changing to public transport if the subway layer was active
* fix buttons overlap in landscape navigation mode
* fix freezes on Samsung A50
* fix the incorrect state of the "Keep Search History" setting if toggled two times

iOS:
* fix isolines reminder being displayed on top of other dialogs
* fix circular downloading progress bar layout in selected POIs
* fix On/Off button icons
* fix the alignment of RTL languages in the bottom menu
* fix bug allowing to add the same language two times in the OSM editor
* correct location of "more" menu in bookmark lists
* default email client is supported for bug reports

Mobile Linux and Mac (Windows is possible too!):
* add route marking buttons to place pages
* add an "Exit" menu option and keyboard shortcuts for all menu entries
* improve font clarity on MDPI screens

Map:
* display difficult or indistinct hiking trails as brown-dotted, extreme/expert or indiscernible ones as black sparse dotted
* dark blue lines for dedicated cycleways
* blue lines under white/brown dashes for shared bicycle/pedestrian paths, or over white dashes for segregated ones
* more consistency in displaying paved paths as white dashed lines, unpaved ones as brown dashed
* roads visible under semi-transparent bridge outlines
* added scree and shingle areas; better color of bare rock surfaces
* stop displaying vacant/unused shops
* added natural=stone (displayed as natural=rock), miniature golf
* separate public transport shelters, basic huts and lean-tos from generic shelters
* added icons for animal enclosures and dry cleaning; updated laundry icon
* fix too small font size for smaller cities
* make city labels visible at higher zooms
* reduce the opacity of indigenous lands hatching fill
* don't display nature reserves' hatching fill and icon/caption on very detailed zooms

Search:
* category search improvements (padel, subway stations, wilderness huts, etc.)
* searchable drinking water refills (participating cafes, etc.)
* made private swimming pools not searchable
* type ?wiki in the search to highlight Wikipedia articles on the map
* tuned category search ranking

Updated Basque, German, Greek, and Slovak translations
