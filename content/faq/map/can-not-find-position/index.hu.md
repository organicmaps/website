---
title: "Az alkalmazás nem találja a pozíciómat a térképen, vagy helytelen helyet mutat"
slug: az-alkalmazás-nem-találja-a-pozíciómat-a-térképen
description: "Hibaelhárítási útmutató a helymeghatározással és az aktuális GPS-pozícióval kapcsolatos problémák megoldásához a térképen iOS és Android eszközökön"
updated: "2026-01-04"
taxonomies:
  faq:
  - Map
extra:
  order: 10
aliases:
  - /hu/faq/map/can-not-find-position/
---

Kérjük, győződjön meg arról, hogy eszköze rendelkezik GPS-szel, a helymeghatározási szolgáltatások engedélyezve vannak, és az Organikus térképek helymeghatározási engedélyekkel rendelkeznek.

**Android**

Eszközén nyissa meg a Beállítások → Hely lehetőséget. Jobb, ha bekapcsolja a Nagy pontosságú módot, mivel ez lehetővé teszi a pontos GPS helymeghatározást.

Ha Android-eszköze nem tudja meghatározni a tartózkodási helyét, engedélyezze (vagy tiltsa le, ha engedélyezve van) a „Google Play Services” opciót az alkalmazás beállításainál.

Megjegyzés: csak akkor láthatja, ha a Google Play-szolgáltatások telepítve (engedélyezve) vannak Android-eszközén. A Google Play szolgáltatásai a hely pontosabb meghatározására szolgálnak. Ha az opció letiltása után problémákat tapasztal a helymeghatározás pontosságával kapcsolatban, kapcsolja be.

**iOS**

Ha Ön iPhone vagy iPad felhasználó, kérjük, ellenőrizze az iOS beállításait → Adatvédelem → Helymeghatározási szolgáltatások. A földrajzi helyadatok megosztását engedélyezni kell az organikus térképekhez.

**Megjegyzések:**

* A barangolás közbeni nem kívánt adatforgalom elkerülése érdekében eszköze beállításaiban kikapcsolhatja az összes mobiladat-forgalmat, aktiválhat egy repülési módot, vagy letilthatja a mobiladatokat az Organikus térképekhez. Az Android és iOS eszközök repülési módban használhatják a GPS-t.

* Egyes mobileszközök nem rendelkeznek beépített GPS-vevővel, például az iPod Touch, a csak WiFi-t használó iPad, az Amazon Kindle Fire/Kindle Fire HD 7 és néhány Android táblagép. Ezeken az eszközökön minden alkalmazás megjeleníti az Ön hozzávetőleges tartózkodási helyét a Wi-Fi hálózaton keresztül, mindaddig, amíg csatlakozik az internethez.

* A helyérzékelés GPS-műholdakkal (ha a WiFi és a mobilhálózatok le vannak tiltva) eltarthat egy ideig. Minél hosszabb ideig nem használja a GPS-t, annál több időt vesz igénybe. A helyérzékelés sebessége az eszköztől függ, nem az alkalmazástól. A GPS működését az időjárás is befolyásolja – szabadban működik a legjobban, ha tiszta az ég. Problémák adódhatnak, ha beltérben, szűk utcán próbálunk elhelyezkedni, vagy ha autót vezetünk, ha sok fém van körülötte, vagy fém/mágnes van a készülék házán.


**Helytelen hely jelenik meg a térképen**

1. Ha a térképen a helyzetjelző nyíl körül egy nagy, félig átlátszó kör látható, az azt jelenti, hogy a pozíciója alacsony pontossággal, WiFi vagy mobilkapcsolat használatával került meghatározásra. Győződjön meg arról, hogy a rendszerbeállításokban engedélyezte a "Pontos" helymeghatározást az Organic Maps számára, és próbáljon meg kimenni a szabadba, távol a magas épületektől és fáktól, hogy javítsa a műholdas GPS-jel vételét.

2. Ha a pozíciója helytelenül van meghatározva (például az egyik városban tartózkodik, de az alkalmazás egy másik várost mutat), akkor valószínűleg olyan területen tartózkodik, amelyet elektronikus hadviselési (EW) intézkedések miatt hamis GPS-jel (GPS-hamisítás) érint. Ilyen esetekben az egyetlen megoldás az, ha másik helyre megy.