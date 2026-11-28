---
title: "What is the difference between a route and a track? Can I navigate a GPX file?"
description: "Understand routes versus GPX tracks, save a planned Organic Maps route and check the status of Follow Track navigation."
updated: "2026-11-15"
taxonomies:
  faq: ["routes-and-navigation"]
extra:
  order: 40
---

In the current published mobile release, you can [import a GPX track](@/faq/bookmarks/how-to-import/index.md) and display it alongside your position. To build a navigation route, select points on the track and check where the calculated route differs from the original line.

The **Follow Track** feature for navigating along imported or saved tracks is in development and is not available in the published release.

A route is calculated between a start, destination, and optional stops using the selected travel mode and map data. A track is a line made from a sequence of coordinates, usually recorded with GPS or created by another planning tool.

## Can I save a planned route for later? {#save-route}

Yes. [Build a route](@/faq/map/how-to-create-a-route/index.md) and use **Save** in the route-planning interface to save it as a track in **Bookmarks and Tracks**. You can display the saved line on the map or [export it](@/faq/bookmarks/how-to-export/index.md). Give it a useful name so you can find it later.

KML exports preserve a saved route’s intermediate stops and travel mode; GPX and GeoJSON exports include the stops as separate points. A saved track is still different from an active navigation session: opening it does not start spoken turn instructions. Keep the maps needed for the trip downloaded and build a navigation route when you need guidance. Exchanging a GPX file with another app does not guarantee identical routing.
