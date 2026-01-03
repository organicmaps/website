---
title: How can I do more advanced map editing?
description: Tutorial for editing OpenStreetMap with more advanced tools like ID, Go Map and Vespucci
updated: "2024-06-20"

taxonomies:
  faq: ["Map Editing"]

extra:
  order: 40
---

Organic Maps includes a simple and easy-to-use editor that you can use to edit the map. The editor is, however, limited and only allows to add simple point features, that means no building outlines, roads, lakes, towns, etc. If you want to change something that can not be edited with the build-in editor, this is the right FAQ page to read.

As all map data used in Organic Maps comes from [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), you can directly update the map there. Your modifications will then be included into Organic Maps with the next map update.

## OpenStreetMap Editors

For editing OSM, there are several options. If you have a laptop or desktop computer at hand, it's better to use the [ID Editor](https://www.openstreetmap.org/edit) that runs in your browser. The ID Editor is easy for beginners, and a bigger screen, mouse, and keyboard make map editing easier.

For advanced map editing from a mobile device, use [Go Map](https://apps.apple.com/us/app/go-map/id592990211) for iOS or [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) for Android. Go Map is easy for beginners, while Vespucci targets more advanced users. LearnOSM provides tutorials for [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) and [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

For simpler edits with more fun, you may also try [Every Door app](https://every-door.app/) for iOS and Android and [StreetComplete app](https://streetcomplete.app/) for Android.

#### ID Editor

For editing OpenStreetMap with ID follow these steps:

1. Create a new account or log in at [OpenStreetMap.org](https://www.openstreetmap.org)
2. Browse to the location you want to edit on OpenStreetMap.org and click *Edit* at the top
3. *Start the Walkthrough* and follow the short tutorial that explains the ID Editor
4. Edit the map
5. Upload your changes

That's it, you are now part of the OSM community.

## What happens with my edits?

Once you press *Upload* your changes are instantly added to the public OSM database. So be considerate when editing. In Organic Maps, your changes will be visible after the next monthly map update.

Your e-mail is not published, but other people will be able to see your OSM user name. As OSM offers the possibility to discuss changes, you might get questions about your edits from other OSM contributors. You will be notified about this via the e-mail address you used for registering your OSM account. As OSM is a community project that builds on collaboration you should always answer such questions.

## Community and Wiki

OpenStreetMap is a community. If you need help or have any questions you can ask in the [OSM Forum](https://community.openstreetmap.org/c/help-and-support) or take a look at the [OSM Wiki](https://wiki.openstreetmap.org/) documentation.

## Tags - How the OSM datamodel works

The OpenStreetMap database contains Objects like Nodes, Ways, Areas, and Relations that abstract from real-world features. These Objects have Attributes, so-called Tags to further describe them. A Tag is a Key-Value combination.

As this sounds more complicated than it is we will give an example:
A Restaurant is e.g. mapped as a Node or Area with the Tag ``` amenity=restaurant```. Further Tags like ```cousine=*``` or ```opening_hours=*``` can then be used for further details.

> Note that the ID editor hides the internal data structure from the users to be more beginner-friendly. But for reading the Wiki documentation heaving a brief overview of the data structure is helpful.
In the ID Editor, you can see the Tags that ID is hiding from you by expanding the *Tags* section in the *Edit feature* side panel.

## OSM Notes {#osm-note}

If you don't have time or the problem is too complicated for editing the OSM data yourself OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) are the way to go. You can place such a note in the location of the map error and describe the problem in detail. Other OSM volunteers can then help and solve the issue. You will get e-mail notifications via your OSM account in case they have further questions or the OSM Note is solved.

1. Create a new account or log in at [OpenStreetMap.org](https://www.openstreetmap.org)
   > You can also open anonymous Notes, but this is not recomended as you won't get notified when the issue is solved or there are further questions.
2. Zoom to the map location on [OpenStreetMap.org](https://www.openstreetmap.org) and press *Add a note to the map* (second icon from the bottom on the right menue). Then drag the blue map marker to the exact location.
   > Try to be as precice as you can.
3. Provide a detailed description of the map problem and press *Add Note*
   > For shops e.g. provide the name and mention what is sold there or what services are offered.
