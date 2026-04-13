---
title: "Organic Maps November 2023 Release with outdoor map style preview"
date: 2023-11-22T11:46:18+00:00
slug: "organic-maps-november-2023-release-with-outdoor-map-style-preview"
taxonomies:
  news: ["releases"]
---

This release was delayed due to [OpenStreetMap vandalism](https://community.openstreetmap.org/t/vandalism-and-blocks-in-israel/105176), and due to a longer testing of many fixes and changes prepared by our contributors.

Highlights
* New OpenStreetMap data as of November 13, 2023
* It is possible to zoom in deeper now and see more POIs in dense areas
* Outdoors map style preview (please read on to know how to activate it)
* Added an experimental referral link "Details on Kayak" for some hotels that are already present in OpenStreetMap. Booking a hotel using this link will give a few dollars to Organic Maps as a donation toward the project development. This is not expected to bring in much, but every dollar counts. Remember, that Organic Maps doesn’t collect or share any information about you or your device. Please be aware that Kayak may have tracking on their website like most other websites, including Facebook and Twitter.
* "Inertial" kinetic scroll improvements
* Removed max limit to search bookmarks
* Brands are displayed on the Place Page

Android
* Fixed import of bookmarks in KMB format from Maps.Me -- kudos to strump
* Fixed missing system location indicator at the right top of the Android screen -- rtsisyk
* Disabled the screen wake lock by default to improve power-saving -- rtsisyk
* Corrected the location search indication when the map is moved or zoomed -- rtsisyk
* Smoother corners for the place page -- Vinod Patil
* Landscape layout for About screen and other theme color fixes -- Jean-Baptiste

iOS -- most changes are done by Kiryl Kaveryn
* Removed the bottom tab bar to show more map on the screen
* Removed the unnecessary "route" button on the map (tap or long-tap a place on the map or select a search result to build a route using the "Route To" button instead)
* Highlighted the Route To button and hinted the FAQ for new users
* Fixed CarPlay dark/light mode colors
* Fixed keyboard input on iPadOS 15+ -- Keith Conger

Routing -- vng
* Don't route through access=emergency, military, agricultural, forestry
* Tuned ferry crossing estimations
* Improved cross-country and cross-region routing
* Improved residential routes

Search -- vng
* Process platz-pl like strasse-str
* Improved address matching
* Improved search of brands

Map Styling -- kudos to RedAuburn, pastk, map-per, dvdmrtnz, vng, RicoElectrico
* Added flowerbeds, rental shops, bicycle rentals, motorcycle repairs, petting zoo, prison areas, compressed air
* Added nature reserves and military zones rendering to the car navigation mode
* Added Docklands Light Railway, Porto metro
* Display names of ski pistes
* Tuned/updated icons of fitness center, yoga, theatre, artwork, statue, theme park, bbq, lighthouse, windmill, heliport & helipad, hunting stand, Kingdom Hall of Jehovah's Witnesses, paid & private versions of parking and parking entrances, convenience, deli, farm, grocery, health food, tobacco shops
* Better farmyard & garage landuse area fills
* Increased scrubs, alpine huts visibility
* Updated sanitary dump station icons and adjusted their priority
* Reduced visibility of cave entrances and improved the icon
* Increased visibility of standalone house numbers
* Reduced Tokyo subway visibility -- kudos to charlie2clarke
* Removed minor road markers/shields cluttering the map in Estonia
* Fix colors of Estonia and Germany road markers/shields
* Increased visibilities of road markers/shields on tertiary and residential roads
* Fixed "gaps" in some densely mapped lines
* Fixed "gaps" in the outlines of bridges and other compound lines

Outdoors map style preview
* Tailored for out-of-the-city outdoor activities like hiking, backcountry cycling/MTB, 4x4, etc.
* Emphasizes paths/tracks, cliffs, railways, powerlines, rivers and streams, water sources, peaks, mountain saddles and passes, waterfalls, lighthouses, caves, viewpoints, campsites, huts, shelters, picnic sites, gates, stiles, fords, etc.
* Make sure to update your downloaded maps!
* Enable by typing `?olight` in the search field and return to the map; type `?light` to switch back to the main style
* Use `?odark` and `?dark` for a dark style
* Android and iOS developers [wanted](https://github.com/organicmaps/organicmaps/issues/6269) to help with adding a nice UI for style switching!

Translations
* Improved "avoid …" routing options wording
* Improved Arabic, Basque, Chinese, Czech, Danish, Finnish, Greek, Hungarian, Indonesian, Italian, Korean, Marathi, Polish, Romanian, Slovak, Spanish, Sweden, Thai, Turkish, Ukrainian, and Vietnamese translations
