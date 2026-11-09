---
title: "Why can Organic Maps not find my location, or only show an approximate position?"
description: "Fix missing or approximate GPS location in Organic Maps and understand precise-location permissions, the accuracy circle and direction arrow."
updated: "2026-11-09"
taxonomies:
  faq: ["location-and-compass"]
extra:
  order: 10
---

Turn on device location services and allow Organic Maps to use precise location. Go outdoors with a clear view of the sky and wait for a satellite fix; buildings and terrain can obstruct signals. An internet connection can help the device obtain an initial location more quickly, but offline GPS does not require mobile data.

Check whether another location app has the same problem. Some tablets have no satellite positioning receiver; hardware capabilities vary by model. If the problem only appears with the screen off, check background permissions and battery restrictions. Include these observations when reporting a problem.

## Android location settings

In your device's app permissions, allow Organic Maps to use your location and enable **Precise location** when that choice is available. On Android 12 or later, device location accuracy settings are usually under **Settings → Location → Location services → Location Accuracy**. On Android 9–11, look under **Location → Advanced → Location Accuracy**; on older versions, look for **High accuracy** under **Location mode**. Menu names vary by manufacturer.

If **Google Play Location Services** is available in Organic Maps settings, try disabling it and restarting the app if location is missing or stops updating. Enable it again if accuracy gets worse. In F-Droid, the option can appear even when no compatible service is installed.

## iPhone and iPad location settings

Open **Settings → Privacy & Security → Location Services → Organic Maps**. Enable location access and **Precise Location**. Some iPad models do not have a satellite positioning receiver, so check the hardware capabilities of your model.

If the problem only happens with the screen off, see [background recording and location restrictions](@/faq/bookmarks/android-track-recording/index.md). If it continues with the app open, [report your device, settings and observations](@/faq/app/report-a-bug/index.md).

## What does the circle around my position mean? Why is there a dot instead of an arrow? {#accuracy-circle}

The circle shows the device's estimated location uncertainty. A larger circle means lower confidence; it is an estimate, not a guarantee that your true position lies inside it.

A position dot without a direction arrow can mean that the device has no usable heading information. This is different from location accuracy: a device may know where it is without knowing which way it is facing. Some devices lack a compass; this is not true of all tablets.

If your position is correct but the arrow points the wrong way, see [compass troubleshooting](@/faq/location/compass-and-orientation/index.md).
