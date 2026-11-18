---
title: "Can another app open Organic Maps, show places, or build a route?"
description: "Open Organic Maps from another app using deep links and external APIs for places, search and routes on Android and iOS."
updated: "2026-11-06"
taxonomies:
  faq: ["developer-integrations"]
extra:
  order: 10
---

Yes. The external API lets another app open Organic Maps to show one or more places, run a search, or build a route. For example, a travel app can display its recommended stops on the map, and an Android app can ask the user to choose a point and receive its coordinates back.

Try the interactive [API and deep-link examples at omaps.app/api](https://omaps.app/api). Integration code and sample apps are available in [organicmaps/api-ios](https://github.com/organicmaps/api-ios) for Swift and Objective-C, and [organicmaps/api-android](https://github.com/organicmaps/api-android) for Java and Kotlin. These APIs open the installed Organic Maps app; use the [SDK](@/faq/developers/sdk/index.md) to embed maps within your own interface.
