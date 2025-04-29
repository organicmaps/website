---
title: "Are there any “secret” debug search commands?"
description: "Frequently asked questions for Organic Maps application"
taxonomies:
  support: ["Search"]
extra:
  tags: ["Android", "iPhone & iPad"]
  order: 20
---

Yes, Organic Maps exposes different “debug commands” to help you control the native components (engine, editor, navigation, ...). These commands are not intended for regular users and are only used for debug purposes. Please only use these commands if you are working on Organic Maps.  
Each command is entered in the search input field (Android and iOS) and is activated as soon as the full search keyword is entered. Unless specified, the effects triggered are discarded after a restart.  
Here are a few examples of debug commands:

* `?dark` or `mapstyle:dark` - Enable night mode for the map view only. You may need to change the zoom level to fully apply the new mode.  
* `?vulkan` - Forces the Vulkan renderer on Android. Vulkan is used by default on newer Android 7+ devices.  
* `?gl` - Forces the OpenGL renderer. OpenGL renderer is supported on all platforms and is used by default on older Android devices and on the desktop.  
* `?edits` - Shows the changes that you’ve made lately and their status. You can see if changes are already uploaded to [OpenStreetMap.org](https://osm.org) or if there were any problems.

See this [documentation](https://github.com/organicmaps/organicmaps/blob/master/docs/DEBUG_COMMANDS.md) for the full list of available “secret” debug commands.
