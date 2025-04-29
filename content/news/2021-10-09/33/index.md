---
title: "Sorry, the latest 21.10.07 release for Android has a bug"
date: 2021-10-09T18:07:49+00:00
slug: "sorry-the-latest-release-for-android-has-a-bug"
---

Sorry, the latest 21.10.07 release for Android has a bug: if you clicked before on coordinates in the place info (to switch coordinates format), then you'll have a crash on startup. Only reinstall can help (but you'll loose your bookmarks!). If you have root access, then close the app and delete `/data/data/app.organicmaps.app/files/settings.ini` file.

If you didn't click on coordinates before, then it should work.

Good news: the fix is already on it's way into app stores! After updating to the latest 21.10.09 version everything will work back again.

Here is the fixed Google Play apk which can be installed manually (the same as is waiting for review now): <https://t.me/organicmaps/8486>
