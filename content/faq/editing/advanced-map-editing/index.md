---
title: How can I do more advanced map editing?
description: Tutorial for editing OpenStreetMap with more advanced tools like ID Editor, Go Map and Vespucci
updated: "2026-08-23"

taxonomies:
  faq: ["map-editing"]

extra:
  order: 40
---

Organic Maps includes a simple and easy-to-use map editor. It is limited to simple point features, which means it cannot add building outlines, roads, lakes, towns, and similar objects. This FAQ explains how to change anything that the built-in editor cannot edit.

All map data used in Organic Maps comes from [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), so you can update the map directly there. Your changes will be included in Organic Maps with the next map update.

## OpenStreetMap Editors

For editing OSM, there are several options. If you have a laptop or desktop computer at hand, it's better to use the [ID Editor](https://www.openstreetmap.org/edit) that runs in your browser. The ID Editor is easy for beginners, and a bigger screen, mouse, and keyboard make map editing easier.

For advanced map editing from a mobile device, use [Go Map](https://apps.apple.com/us/app/go-map/id592990211) for iOS or [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) for Android. Go Map is easy for beginners, while Vespucci targets more advanced users. LearnOSM provides tutorials for [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) and [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

For simpler edits with more fun, you may also try [Every Door app](https://every-door.app/) for iOS and Android and [StreetComplete app](https://streetcomplete.app/) for Android.

#### ID Editor

To edit OpenStreetMap, follow these steps:

1. Create a new account or log in at [OpenStreetMap.org](https://www.openstreetmap.org)
2. Browse to the location you want to edit on OpenStreetMap.org and click *Edit* at the top
3. *Start the Walkthrough* and follow the short tutorial that explains the ID Editor
4. Edit the map
5. Upload your changes

That's it; you are now part of the OSM community.

## What happens with my edits?

Once you press *Upload*, your changes are instantly added to the public OSM database, so be considerate when editing. In Organic Maps, your changes will be visible after the next monthly map update.

Your email address is not published, but other people can see your OSM username. OSM contributors may ask questions about your edits through its change-discussion system. Notifications are sent to the email address registered with your OSM account. OSM is a collaborative community project, so you should always answer such questions.

## Community and Wiki

OpenStreetMap is a community. If you need help or have questions, ask in the [OSM Forum](https://community.openstreetmap.org/c/help-and-support) or read the [OSM Wiki](https://wiki.openstreetmap.org/) documentation.

## Tags - How the OSM data model works

The OpenStreetMap database represents real-world features as objects such as nodes, ways, areas, and relations. Tags further describe these objects. A tag is a key-value combination.

This sounds more complicated than it is, so consider an example:
A restaurant can be mapped as a node or area with the tag `amenity=restaurant`. Other tags such as `cuisine=*` or `opening_hours=*` add further details.

> The editor hides the internal data structure to be more beginner-friendly, but a brief overview of that structure helps when reading the Wiki documentation.
In ID Editor, expand the *Tags* section in the *Edit feature* side panel to see the tags hidden by the editor.

## OSM Notes {#osm-note}

If you don't have time or the problem is too complicated for editing the OSM data yourself, OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) are the way to go. You can place such a note in the location of the map error and describe the problem in detail. Other OSM volunteers can then help and solve the issue. You will get e-mail notifications via your OSM account in case they have further questions or the OSM Note is solved.

1. Create a new account or log in at [OpenStreetMap.org](https://www.openstreetmap.org)
   > You can also open anonymous notes, but this is not recommended because you will not be notified when the issue is solved or there are further questions.
2. Zoom to the map location on [OpenStreetMap.org](https://www.openstreetmap.org) and press *Add a note to the map* (the second icon from the bottom in the right menu). Then drag the blue map marker to the exact location.
   > Be as precise as possible.
3. Provide a detailed description of the map problem and press *Add Note*
   > For a shop, provide its name and mention what it sells or which services it offers.
