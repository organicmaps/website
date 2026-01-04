---
title: The app can't find my position on the map or shows incorrect location
description: Troubleshooting guide for solving problems with location and current GPS position on the map for iOS and Android devices
updated: "2026-01-04"
taxonomies:
  faq: ["Map"]
extra:
  order: 10
---

Please make sure your device has GPS, location services are enabled, and location permissions are given to Organic Maps.

**Android**

On your device open Settings → Location. It is better to switch on High accuracy mode, as it enables precise GPS location.

If your Android device can not determine your location, enable (or disable, if enabled) “Google Play Services” option in the app settings.

Note: you can see it only if you have Google Play services installed (enabled) on your Android device. Google play services are used to determine location more precisely, if you experience issues with location accuracy after you disabled the option, turn it on.

**iOS**

If you are an iPhone or iPad user, please check iOS settings → Privacy → Location services. Geolocation data sharing should be enabled for Organic Maps.

**Incorrect location is shown on the map**

1. If there is a large semi-transparent circle around your location arrow on the map, it means that your position is determined with low accuracy, using WiFi or cellular connection. Make sure that you enabled "Precise" location accuracy for Organic Maps in system settings, and try going outside, away from tall buildings and trees, to improve satellite GPS signal reception.

2. If your position is determined incorrectly (for example, you are in one city, but the app shows another city), then you are most likely in an area affected by a false GPS signal (GPS spoofing) due to electronic warfare (EW) measures. In such cases, the only solution is to move to another location.

**Notes:**

* To avoid unwanted data while roaming, you can turn off all mobile data, activate a flight mode or disable mobile data for Organic Maps in your device settings. Android and iOS devices can use GPS in the flight mode.

* Some mobile devices do not have built-in GPS receivers, such as the iPod Touch, WiFi-only iPad, Amazon Kindle Fire/Kindle Fire HD 7, and some Android tablets. On these devices, all apps will show your approximate location detected using a Wi-Fi network, as long as you are connected to the internet.

* Location detection with GPS satellites (when WiFi and Mobile Networks are disabled) may take some time. The longer the GPS has not been used, the more time it takes. The speed of location detection depends on the device, not the app. The GPS operation is influenced by the weather as well – it works best outdoors when the sky is clear. Problems may arise when trying to locate yourself indoors, on a narrow street, or when driving a car, with a lot of metal around or with a metal/magnet on the device's case.
