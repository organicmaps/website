---
title: "Can I embed Organic Maps in my own app? Is there an SDK?"
description: "Embed Organic Maps in an Android app with the SDK, find integration examples and understand the source-code license and iOS plans."
updated: "2026-11-06"
taxonomies:
  faq: ["developer-integrations"]
extra:
  order: 20
---

Yes. The Android SDK lets you embed Organic Maps rendering, offline search, map downloads, bookmarks, and routing in an Android app. The [organicmaps/sdk-android examples](https://github.com/organicmaps/sdk-android) demonstrate a basic map, offline map downloads and search, and route planning and navigation.

Follow the [Android SDK integration guide](https://github.com/organicmaps/organicmaps/blob/master/android/sdk/README.md) for setup and API details. The SDK is evolving, so integrations should track changes to its API. An iOS SDK is planned; iOS apps can already use the [external API](@/faq/developers/external-api/index.md) to open Organic Maps and exchange information.

## Can I reuse the Organic Maps source code? {#license}

The project's own source code is distributed under the Apache License 2.0. Consult the repository's [license](https://github.com/organicmaps/organicmaps/blob/master/LICENSE) and the notices for included components. The source-code license is separate from the licenses for map data and other assets.
