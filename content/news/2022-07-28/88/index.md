---
title: "New update 2022.07.27 is already available in AppStore and Huawei AppGallery but is still reviewed in other stores"
date: 2022-07-28T16:19:51+00:00
slug: "new-update-is-already-available-in-appstore-and-huawei-appgallery-but-is-still-reviewed-in-other-stores"
---

New update 2022.07.27 is already available in [AppStore](https://apps.apple.com/app/organic-maps/id1567437057) and [Huawei AppGallery](https://appgallery.huawei.com/#/app/C104325611) but is still reviewed in other stores. The detailed changelog for all platforms:
* New OSM data as of July 18, 2022
* Added missing shop types from OpenStreetMap tags: antiques, art, baby\_goods, bag, boutique, charity, cheese, craft, dairy, deli, electrical, farm, fishing, grocery, health\_food, houseware, interior\_decoration, kitchen, lottery, medical\_supply, nutrition\_supplements, paint, pastry, perfumery, second\_hand, sewing, storage\_rental, tobacco, trade, watches, wholesale
* Properly select max speed in some routing cases
* sport=\* tags have higher priority than leisure=pitch
* Fill transit mark place page with feature info
* Show text info about the next turn's street longer
* Use building:min\_level for 3D buildings
* Allow removing cuisines from selection in the Editor
* Fix Belarusian, German, Russian, and Ukrainian translations
* Add missing translations for OSM natural=\* and amenity=events\_venue types

**Android:**
* Fixed and updated API support. Now you can select a point on the map and return it back to your app. See <https://omaps.app/api> for more details, check our [API examples for Android](https://github.com/organicmaps/api-android/), or let us know if you are interested in integrating Organic Maps with your app.
* Fixed invisible paths and trails on Mali-G72 Huawei devices
* Fix Facebook URLs validation
* Limited bottom sheet menu title to max 3 lines
* Show only one back arrow in bookmark search
* Fixed padding of bookmark categories

**iOS:**
* Show "Open"/"Opens in"/"Closes in" in search results
* Show speed limit near the current speed in navigation mode

**Linux:**
* Fix assertion failure in ES3 scenario on Linux, now OM should work on mobile Linux too
