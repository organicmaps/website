---
title: "Organic Crowdfunding and the September update"
date: 2023-09-30T22:50:03+00:00
slug: "organic-maps-crowdfunding-and-september-update"
taxonomies:
  news: ["releases"]
---

A short announcement before the details about the September Organic Maps release.
We are looking for volunteers to help us in different areas. A lot of interesting and challenging work (did you already check [1800+ issues on Github](https://github.com/organicmaps/organicmaps/issues/)? 💪) awaits on the open-source, community-built road to the best, fastest 🚀, easy-to-use 👴 👵 🧒, and privacy-focused maps. Want to [help us ](https://organicmaps.app/support-us/)with the app and website development, marketing, PR, financing, user support, or in any other way? Say hello@organicmaps.app.

If we get enough money, we can significantly speed up the development by hiring a full-time team and rewarding the most active contributors. If we get more users, we get more donations. [Donate](https://organicmaps.app/donate/) and spread the word 💸! Let's call it **Organic Crowdfunding** 💰

Several new features are available in the September update. You can easily measure distance and build straight-line routes in the same way as you are building other routes, and even simpler, with a single tap! We called it Helicopter Routing but then decided to rename into the Ruler to avoid confusion.
Another new Android feature is background voice directions. Now Organic Maps can talk with you from your pocket 🙂

* New OSM maps data as of September 20
* Added new route type "Ruler" (aka Helicopter Routing) to measure straight distances quickly, many thanks to Sergiy [@strump](https://github.com/strump) for bringing it to life!
* Set decimal and grouping separators depending on the system locale, thanks to Gonzalo [@gpesquero](https://github.com/gpesquero)
* Removed annoying zoom in route planning mode
* Parking entrances are searchable now
* Improved street matching and results relevance (thanks to Viktar [@vng](https://github.com/vng) for all search improvements!)
* Search for grocery and houseware
* Caves can be added in the Editor
* Improved Arabic, Polish, and Spanish translations

Android
* Background voice and directions, thanks to Roman [@rtsisyk](https://github.com/rtsisyk)
* Fixed "Wait..." dialog on startup on Android 13 with many downloaded maps on SD card (thanks to Viktar again!)
* Fixed distance on the route preview panel (thanks to Sergiy again!)
* Fixed the blue arrow icon on the location button on Android 5 and 6 devices, thanks to Michał [@RicoElectrico](https://github.com/RicoElectrico)
* Voice test in the settings menu (again, thanks to Gonzalo!)
* Fixed backurl API parameter
* Do not pause music when the screen is rotated (credits to Roman again!)
* Fixed bug with the invisible color of imported GPX tracks

iOS
* Fixed Open/Closed shown sometimes in gray color

Ferenc [@Ferenc-](https://github.com/Ferenc-) made Linux improvements:
* Add positioning support via GeoClue2
* Use OpenGL ES 3.0 instead of desktop OpenGL

Map styling was done mostly by Konstantin [@pastk](https://github.com/pastk), David [@dvdmrtnz](https://github.com/dvdmrtnz), Harry [@RedAuburn](https://github.com/RedAuburn), and [@map-per](https://github.com/map-per):
* New or updated icons for factory, winery, bookcase, library, brothel, bicycle repair station, bicycle rental, bicycle parking, sauna, lottery, bookmaker, massage, sewing, books, underground parking, disabled parking space, gate, excrement bags vending, wholesale shop, outdoor seating, handicraft, grinding mill, caterer, HVAC, key cutter and locksmith. That's a long list, huh?
* Added vehicle inspection, public bath, strip club, gambling, cycle barrier, waterways (drain, ditch, moat, wastewater), aquarium, assembly point, adult gaming center, amusement arcade, Mormon churches, visitor center, industrial mine, historical objects (cannon, anchor, stone, aircraft, tank, mine, wreck, locomotive). Even longer list!
* Added bridges and tunnels rendering for cycleways, footways, paths, tracks, bridleways, steps
* Render barrier=ditch differently from waterway=ditch
* Reduced priorities of river names (and of other lower-importance lines) in navigation mode
* Tuned road names and road shield priorities
* Fixed icons display for parking buildings
* Reduced visibility of minor and private parking icons, removed area fill for underground parking
* Reduced fire hydrants visibility
* Display house numbers above icons and main POI captions, and don’t display house numbers for buildings that are too small for the current zoom level
* Don't display star icons for squares
* Fine-tune house numbers font and drawing priority
* Added highway-pedestrian, bridleway, and cycleway lines for detailed zooms (z18-) in navigation mode
* Pedestrian tunnels are not visible in navigation mode

We are infinitely grateful to everyone who [helps us](https://organicmaps.app/support-us/) and [donates](https://organicmaps.app/donate/). Organic Maps would not be possible without our users and our contributors ♥️ 🙏 🤟
