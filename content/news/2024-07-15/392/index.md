---
title: "Have you already installed a July release of Organic Maps? It introduces two major features funded through the NGI0 Entrust Fund"
date: 2024-07-15T21:13:23+00:00
slug: july-release-with-improved-usa-address-search-using-tiger-data-and-fixed-text-rendering-for-non-latin-scripts-funded-by-ngi0-entrust-fund
aliases: ["/news/2024-07-15/have-you-already-installed-a-july-release-of-organic-maps-it-introduces-two-major-features-funded-through-the-ngi0-entrust-fund/"]
taxonomies:
  news: ["releases"]
---

Have you already [installed](https://omaps.app/get) a July release of Organic Maps? It introduces two major features [funded](https://nlnet.nl/project/OrganicMaps/) through the NGI0 Entrust Fund:

1. Better address search in the USA based on Topologically Integrated Geographic Encoding and Referencing system (TIGER) data (preprocessed by [Nominatim project](https://nominatim.org/data/)), [implemented](https://github.com/organicmaps/organicmaps/issues/2532) by Viktor Havaka. Addresses are stored, searched, and displayed as interpolations (lines along streets with a starting house number and ending house number), so don't expect to see buildings on the map (did you know that you can draw buildings and add addresses at [OpenStreetMap.org](https://openstreetmap.org/) yourself?).
There is a heuristic to decide when to use TIGER data and when to use existing OpenStreetMap data.
Map size for the whole USA has increased from 10Gb to 13Gb (including Wikipedia and elevation data, there are some [ideas](https://github.com/organicmaps/organicmaps/issues/8672) to [split it](https://github.com/organicmaps/organicmaps/issues/5912) to improve [incremental map updates](https://github.com/organicmaps/organicmaps/issues/2317)).

2. Proper rendering of texts in Indic (Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Tamil, Telugu), Arabic (N'Ko, Syriac, Mongolian), Thai and Lao, Khmer, Myanmar, Tibetan, Hangul, Hebrew scripts, [implemented](https://github.com/organicmaps/organicmaps/issues/4281) by Alexander Borsuk by integrating [Harfbuzz](https://harfbuzz.github.io/) text shaping library with Organic Maps rendering engine (called "Drape").

There are other notable improvements, thanks to our beloved contributors:

* OpenStreetMap data as of July 2
* New Malayalam and Bengali fonts (please let us know if any other fonts need updating)
* Single tap now selects any point on the map, even if the map is empty -- by Sergiy Kozyr
* Changed long tap to toggle full-screen mode -- by Sergiy Kozyr
* Accidentally deleted bookmark on the map now can be restored immediately (Save button changes to Restore) -- by Kiryl Kaveryn
* Display major roads earlier on the world overview map -- by Konstantin Pastbin
* A selected place now shows more types/categories/amenities -- by David Martinez
* Clearer label for POI's building level -- by Antonin Delpeuch
* Display good quality fine gravel pedestrian paths as white dashed -- by Konstantin Pastbin
* Support more road/path surface types (bricks, stone, grass paver, soil) -- by Konstantin Pastbin
* More clear hints when building a route

Search -- kudos to Viktor Havaka:
* Mountain search also shows volcanoes
* Better search results for faraway places
* Search now finds places with a number in their names
* Find parcel lockers using their ref numbers

Android:
* Fix TTS FAQ link in the settings
* Fix GPX import from WhatsApp
* Save exported files to the local device storage -- by Kiryl Razhdzestvenski

iOS (many kudos to Kiryl Kaveryn):
* Use the Import button in Bookmarks and Tracks dialog to load KML, KMZ, GPX files
* Fix importing of bookmarks and tracks via the "Files" app on a cold start (you can tap a KML, KMZ, GPX or KMB file in any app, then "share" it using a rectangular icon with an up arrow at the bottom left, and then choose Organic Maps icon in the list of all apps)
* Added a TTS voice test button in navigation settings -- by Fabian Wüthrich
* Enable logs in settings to help us with bug fixing
* Open social media links in installed applications
* Removed a non-working traffic button from CarPlay -- by Fabian Wüthrich
* Replaced circle checkboxex with a rounded rectangle in the time editor
* Correct dark mode startup background color -- by Evgeny Fayvuzhinsky

Linux:
* Fix a generic Wayland icon displayed instead of an Organic Maps icon on some systems -- by Ferenc Géczi

Our translators and reviewers helped us to update Belarusian, Chinese, Dutch, Euskara, Hungarian, Polish, Portuguese, Russian, and Ukrainian translations.

We have also started to update the [FAQ section](https://organicmaps.app/faq/) on our website, any help with [adding new articles](https://github.com/organicmaps/organicmaps.github.io/) and their translations is appreciated!

Please report all issues using Report a Bug button in the app, by sending us an email, or (the best!) by creating/updating [an issue](https://github.com/organicmaps/organicmaps/issues/) on our GitHub.

P.S. We're now working on the [track recorder feature](https://github.com/organicmaps/organicmaps/labels/Track%20Recording). Any help with ideas, [testing](https://organicmaps.app/#community), [contributions](https://organicmaps.app/support-us/) and [donations](https://organicmaps.app/donate/) is warmly appreciated ❤️

Enjoy traveling with Organic Maps! 🚕 🛤 ✈️ 🏕 👣
