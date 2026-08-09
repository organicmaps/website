---
title: "Az alkalmazás nem találja a pozíciómat a térképen, vagy helytelen helyet mutat"
slug: az-alkalmazás-nem-találja-a-pozíciómat-a-térképen
description: "Hibaelhárítási útmutató a helymeghatározással és az aktuális GPS-pozícióval kapcsolatos problémák megoldásához a térképen iOS és Android eszközökön"
updated: "2026-01-04"
taxonomies:
  faq:
  - map
extra:
  order: 10
aliases:
  - /hu/faq/map/can-not-find-position/
---

Kérjük, győződj meg arról, hogy az eszközöd rendelkezik GPS-szel, a helymeghatározási szolgáltatások engedélyezve vannak, és az Organic Maps helymeghatározási engedélyekkel rendelkezik.

**Android**

Az eszközödön nyisd meg a Beállítások → Hely lehetőséget. Jobb, ha bekapcsolod a Nagy pontosságú módot, mivel ez lehetővé teszi a pontos GPS helymeghatározást.

Ha az Android-eszközöd nem tudja meghatározni a tartózkodási helyedet, engedélyezd (vagy tiltsd le, ha engedélyezve van) a „Google Play Services” opciót az alkalmazás beállításainál.

Megjegyzés: csak akkor láthatod, ha a Google Play-szolgáltatások telepítve (engedélyezve) vannak az Android-eszközödön. A Google Play szolgáltatásai a hely pontosabb meghatározására szolgálnak. Ha az opció letiltása után problémákat tapasztalsz a helymeghatározás pontosságával kapcsolatban, kapcsold be.

**iOS**

Ha iPhone vagy iPad felhasználó vagy, kérjük, ellenőrizd az iOS beállításait → Adatvédelem → Helymeghatározási szolgáltatások. A földrajzi helyadatok megosztását engedélyezni kell az Organic Maps-hez.

**Megjegyzések:**

* A barangolás közbeni nem kívánt adatforgalom elkerülése érdekében az eszközöd beállításaiban kikapcsolhatod az összes mobiladat-forgalmat, aktiválhatsz egy repülési módot, vagy letilthatod a mobiladatokat az Organic Maps-hez. Az Android és iOS eszközök repülési módban használhatják a GPS-t.

* Egyes mobileszközök nem rendelkeznek beépített GPS-vevővel, például az iPod Touch, a csak WiFi-t használó iPad, az Amazon Kindle Fire/Kindle Fire HD 7 és néhány Android táblagép. Ezeken az eszközökön minden alkalmazás megjeleníti a hozzávetőleges tartózkodási helyedet a Wi-Fi hálózaton keresztül, mindaddig, amíg csatlakozol az internethez.

* A helyérzékelés GPS-műholdakkal (ha a WiFi és a mobilhálózatok le vannak tiltva) eltarthat egy ideig. Minél hosszabb ideig nem használod a GPS-t, annál több időt vesz igénybe. A helyérzékelés sebessége az eszköztől függ, nem az alkalmazástól. A GPS működését az időjárás is befolyásolja – szabadban működik a legjobban, ha tiszta az ég. Problémák adódhatnak, ha beltérben, szűk utcán próbálunk elhelyezkedni, vagy ha autót vezetünk, ha sok fém van körülötte, vagy fém/mágnes van a készülék házán.


**Helytelen hely jelenik meg a térképen**

1. Ha a térképen a helyzetjelző nyíl körül egy nagy, félig átlátszó kör látható, az azt jelenti, hogy a pozíciód alacsony pontossággal, WiFi vagy mobilkapcsolat használatával került meghatározásra. Győződj meg arról, hogy a rendszerbeállításokban engedélyezted a „Pontos“ helymeghatározást az Organic Maps számára, és próbálj meg kimenni a szabadba, távol a magas épületektől és fáktól, hogy javítsd a műholdas GPS-jel vételét.

2. Ha a pozíciód helytelenül van meghatározva (például az egyik városban tartózkodsz, de az alkalmazás egy másik várost mutat), akkor valószínűleg olyan területen tartózkodsz, amelyet elektronikus hadviselési (EW) intézkedések miatt hamis GPS-jel (GPS-hamisítás) érint. Ilyen esetekben az egyetlen megoldás az, ha másik helyre mész.