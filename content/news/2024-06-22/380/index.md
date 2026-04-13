---
title: "The major June update and a follow-up OSM data-only update (with a hotfix for the iOS app hanging) were successfully published and are available in all app stores and on our GitHub."
date: 2024-06-22T14:08:52+00:00
slug: june-release-with-uk-and-us-postal-zip-code-search-street-name-announcements-and-gpx-export
aliases: ["/news/2024-06-22/the-major-june-update-and-a-follow-up-osm-data-only-update-with-a-hotfix-for-the-ios-app-hanging-were-successfully-published-and-are-available-in-all-app-stores-and-on-our-github/"]
taxonomies:
  news: ["releases"]
---

The major June update and a follow-up OSM data-only update (with a hotfix for the iOS app hanging) were successfully published and are available in [all app stores](https://omaps.app/get) and on our [GitHub](https://github.com/organicmaps/organicmaps/releases/).

Thanks to Viktar Havaka, now you can search for the US zip codes and UK postcodes! The external address data is taken from the TIGER database and Ordnance Survey, and pre-processed by [Nominatim project](https://nominatim.org/) used in OpenStreetMap search.

Another major feature is street name announcements during the navigation, contributed by Will Bradley. Please enable it in OM settings, and let us know about any issues.

A long-awaited iOS iCloud synchronization is also available, thanks to Kiryl Kaveryn. Please enable it in OM settings (you will be offered to back up all your bookmarks and tracks first) and report any issues.

Bookmarks and tracks GPX export is also ready, in addition to the existing KML (KMZ) export. It will become very handy when we finish the long-awaited Track Recorder feature. Kudos to cyber-toad!

As always, thanks to everyone for your contributions, [donations](https://organicmaps.app/donate/), [support](https://organicmaps.app/support-us/), and positive reviews. They motivate and inspire our team!

General changes and fixes:
* new OpenStreetMap data as of June 13
* search for US zip codes and UK (GB) postcodes -- by Viktar Havaka
* street name announcements in verbal TTS turn instructions (please enable it in settings) -- by Will Bradley
* export bookmarks and tracks in GPX file format -- by cyber-toad and Kiryl Kaveryn
* add, edit, and display web links to menus of restaurants, bars, and food services -- by Arthur Gayot and Kiryl Kaveryn
* fix missing addresses in fitness center details
* add "pastry" and "cakes" search keywords
* fix Wikipedia links that contain a question mark

Android:
* export bookmarks and tracks to a local device
* always show the next turn (in navigation mode)
* add an Exit button to navigation notifications
* improved OSM user profile settings page -- by Harry Bond
* fix display of stop points in the ruler and transit mode for RTL languages

Android Auto:
* use compass and location data from car sensors -- by Andrew Shkrob
* update the UI for the main and category screens -- by Andrew Shkrob

iOS:
* iCloud bookmarks and tracks synchronization (please enable it in settings) -- by Kiryl Kaveryn
* use the map when CarPlay is connected -- by Oleg Montak
* fix CarPlay text color in dark mode
* more TTS voice options
* TTS turn announcements interrupt podcasts instead of ducking them
* fix some buttons that disappeared when adding a place to the map
* fix place details not updated after a bookmark's edit
* fix the non-business hours button in the Editor to work after midnight

Mobile Linux and Desktop versions:
* improve selected place details dialog

Updated Czech, German, and Portuguese translations.

🚀 🚀 🚀 🚀 🚀
