---
title: "Tags - How the OSM datamodel works"
description: "Frequently asked questions for Organic Maps application"
taxonomies:
  support: ["OSM (OpenStreetMap)"]
extra:
  tags: ["Android", "iPhone & iPad"]
  order: 70
---

The OpenStreetMap database contains Objects like Nodes, Ways, Areas, and Relations that abstract from real-world features. These Objects have Attributes, so-called Tags to further describe them. A Tag is a Key-Value combination.  
As this sounds more complicated than it is we will give an example:  
A Restaurant is e.g. mapped as a Note or Area with the Tag `amenity=restaurant`. Further Tags like `cousine=*` or `opening_hours=*` can then be used for further details.  
Note that the ID editor hides the internal data structure from the users to be more beginner-friendly. But for reading the Wiki documentation heaving a brief overview of the data structure is helpful.  
In the ID Editor, you can see the Tags that ID is hiding from you by expanding the *Tags* section in the *Edit feature* side panel.
