---
title: "While many are enjoying their holidays, our community and contributors are creating better maps"
date: 2023-08-21T22:05:00+00:00
slug: "while-many-are-enjoying-their-holidays-our-community-and-contributors-are-creating-better-maps"
taxonomies:
    category: ["Blog Posts"]
---

While many are enjoying their holidays, our community and contributors are creating better maps! Thanks ♥️ to everyone who helps and supports us, it motivates us more and more 🚀

August Organic Maps update is available in [Google Play](https://play.google.com/store/apps/details?id=app.organicmaps&hl=en), [Huawei AppGallery](https://appgallery.huawei.com/#/app/C104325611?local=en), [AppStore](https://apps.apple.com/app/organic-maps/id1567437057), and soon should be available in [FDroid](https://f-droid.org/en/packages/app.organicmaps/) too.

* New OpenStreetMap maps data as of August 14. We're grateful to the OSM for their work and congratulate the community on their [19th OSM birthday](https://wiki.openstreetmap.org/wiki/Birthday)!
* Updated more than a year old Wikipedia articles, thanks to [Evan Lloyd New-Schmidt](https://evan.new-schmidt.com/), who replaced an old, rate-limited online Wikipedia parser with a new blazing-fast, offline wiki dump processing, written in Rust. Maybe someday we'll rewrite our core algorithms in Rust too 😂
* Added missing isolines for some regions of Argentina, Chile, Kazakhstan, Tibet, USA, and Russia (that obviously increased map sizes in these regions), made isolines denser in many other areas and reduced many other map sizes too. How? It's code magic 🪄 by [Konstantin Pastbin](https://github.com/pastk)
* Import comments from GPX cmt tag and treat GPX track segments as part of the singular track they belong to (all GPX joy comes from [@cyber-toad](https://github.com/cyber-toad) contribution 🙏)
* Fixed a bug when editing social contacts, thanks to [Sergiy Kozyr](https://github.com/strump)
* Dog Park can now be added in the Editor, thanks to our beloved and talented QA volunteer [Jean-Baptiste](https://github.com/Jean-BaptisteC)!
* Updated Persian voice directions

Android
* Fixed blank screen bug on Nexus 5X
* Fixed “…more” buttons in bookmark lists
* Replaced the Twitter logo

iOS
* Fixed Wiki text in the dark mode, it's [Artem Trukhanoff](https://github.com/ArtemX9)'s first contribution!

Routing would not improve without our cofounder and algorithms guru [Viktar Havaka](https://github.com/vng)!
* Updated road surface factors for car routing profile
* Better pedestrian routing in Turkey and Georgia
* Fixed cross-region routing when "avoid …" options are enabled

Search… guess what? It's also [Viktar](https://github.com/vng)'s work!
* Fixed search for addresses in Czech and Slovakia
* Improved street matching
* Do not filter duplicated search results except for very close bus stops
* Better ranking when searching by category
* Fixed search by a house name
* Faster search on the map screen
* [RedAuburn](https://github.com/RedAuburn), our contributor 🙏, has removed Tourist Information, Place of Worship, Park, Information Board, and Tourist Map from the Sightseeings category to avoid map cluttering

Styles have been greatly refactored by [Konstantin](https://github.com/pastk) on our way to separate styles for outdoor, cycling, driving, city tourism, and other activities:
* Added ferry routes to the World map
* [RedAuburn](https://github.com/RedAuburn) removed the square background from parking icons and did many other parking improvements. It took a lot of time, but we did it together 👍
* Added separate icons for paid and private parking
* Made the bicycle parking icon differ more from the motorcycle one
* Updated parking entrance icon
* Street-side and lane parkings use a smaller icon and appear later when zooming in
* Added motorcycle parking and parking entrance icons to the navigation mode
* Fixed motorway=trunk links visibility in navigation mode
* Improved motorway=trunk colors
* Removed too small isolines at overview zoom levels
* Added Tehran metro icon
* Revamped priorities system, especially for POIs
* Many other fixes and enhancements

Follow our news at <https://organicmaps.app/news/> , [donate](https://organicmaps.app/donate/), and [support us](https://organicmaps.app/support-us/) to build the fastest, most detailed, easiest-to-use maps together!
