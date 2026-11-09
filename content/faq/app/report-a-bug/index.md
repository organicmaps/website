---
title: "How do I report a bug or send logs?"
description: "Report an Organic Maps bug with useful device details, reproduction steps and logs, or check diagnostic search commands."
updated: "2026-11-06"
taxonomies:
  faq: ["app"]
extra:
  order: 80
---

Use **Report a bug** in the app's About/Organic Maps screen, email [support@organicmaps.app](mailto:support@organicmaps.app), or search and file an issue on [GitHub](https://github.com/organicmaps/organicmaps/issues).

Include your app version, device and OS version, what you did, what you expected, and what happened. For map or routing problems, include coordinates, the map-data date, route mode, and relevant settings. Screenshots or a short recording help. For import failures, a small non-private example file is useful.

If logs are needed, enable logging in Organic Maps settings, reproduce the problem, and send the report using the in-app control; disable logging afterward. Logging is available on both Android and iOS. Review what you send because diagnostic files and screenshots can contain locations or other personal details. For an iOS crash, a matching Organic Maps crash report can be found in the device's Analytics Data settings when available.

## Are there special search commands for troubleshooting? {#debug-commands}

Yes. For example, `?edits` shows the status of local OpenStreetMap edits. Other commands change rendering or diagnostic settings and should be used for a specific troubleshooting task. Effects and persistence vary; do not assume every command resets when the app restarts.

Use the current [debug-command documentation](https://github.com/organicmaps/organicmaps/blob/master/docs/DEBUG_COMMANDS.md) or follow the instructions given for your issue.

For common problems, start with [crashes](@/faq/app/crash/index.md), [GPS location](@/faq/map/can-not-find-position/index.md), [map downloads](@/faq/map/cant-download-maps/index.md) or [unexpected routes](@/faq/navigation/routing-problems/index.md).
