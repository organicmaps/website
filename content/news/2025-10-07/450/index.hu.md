---
title: "Október 7-i kiadás: Android Auto sebességkorlátozás, GeoJSON import és még több"
date: 2025-10-07T10:00:00+00:00
---

Az Android Auto felhasználók mostantól láthatják a sebességkorlátozás figyelmeztetéseket. Hozzáadódott a GeoJSON fájlok importja, amelyek jelölőkké alakíthatók.

Különféle javítások és fejlesztések iOS-hez, Androidhoz, Android Autóhoz és Desktophoz. Részletek lentebb.

Friss funkciók, amelyeket esetleg kihagytál:
- Új útvonaltervező képernyő (iOS)
- OSM `description` címke iOS-en (keresd: `?description`)
- Tömegközlekedési járatszámok megjelenítése megálló kiválasztásakor
- Túra- és kerékpár-útvonalak (kapcsold be a Rétegek gombbal bal felül)
- Jelölők neveinek megjelenítése a térképen (Beállításokban engedélyezhető)
- A ✎ ikon gyors szerkesztést biztosít a jelölőknél

Az Organic Maps a közreműködőknek, [adományaidnak](@/donate/index.hu.md) és [támogatásodnak](@/contribute/index.hu.md) köszönhető.

### Részletes kiadási megjegyzések

- Új OpenStreetMap adatok: október 5.
- Frissített fordítások (Weblate közreműködők)
- Helyzetnyíl javítva GNSS jel nélkül (Viktor Govako)

#### Térképstílusok (Viktor Govako)

- Újratervezett "Outdoor" stílusikonok
- Vízcímke színének javítása
- Épületek megjelenítése 16-os nagyításnál
- Kilátópontok és nézőpontok megjelenítése 14-es nagyítástól
- Általános térképjavítások és fejlesztések

#### iOS

- Útvonalpont-színek javítva (Alexander Borsuk)
- Hosszú nyomás menü fejlesztései (Alexander Borsuk)
- Érkezési idő javítva mértékegység-típus váltásakor (Viktor Govako)
- Törölt objektumok szerkesztésének megakadályozása (Kiryl Kaveryn)

#### Android

- ÚJ: GeoJSON fájlok importálása és jelölőkké alakítása (Andrei Shkrob, Alexander Borsuk)
- Közeli WiFi és mobilhálózatok felsorolása a "Saját pozíció" alatt (csak debug build) (Kiryl Kaveryn)
- OSM bejelentkezés frissítve (Viktor Govako)
- Térkép letöltési hibaüzenet javítva (Viktor Govako)
- Megbízhatóbb GeoIntent kezelés (Alexander Borsuk)
- Adatáttelepítés felhasználói felület fejlesztései (Alexander Borsuk)
- Kategória-besorolás felhasználói felület fejlesztései (Alexander Borsuk)
- Google helyszolgáltatások eltávolítva (Alexander Borsuk)
- "Városi cím" keresési kategória most "Cím" (Alexander Borsuk)
- Lehetséges fekete képernyő javítva keresési eredmény kattintásakor (Viktor Govako)
- Felhasználói felület finomítások "Mi van a közelben" keresésben (Viktor Govako)
- Felugró párbeszédek javítva, amelyek nem tartják tiszteletben a sötét témát (Andrei Shkrob)

#### Android Auto

- ÚJ: Sebességkorlátozás és sebességmérő kamera figyelmeztetések (Denis Koronchik)
- Útvonal-előnézet javítva (Andrei Shkrob)
- Keresési felhasználói felület fejlesztései (Andrei Shkrob)

#### Desktop

- Térképadaptáció fejlesztései (Andrew Shkrob)
- Egérmutató kontrasztja javítva sötét témában (Andrew Shkrob)

Töltsd le a legújabb verziót: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Csatlakozz a béta teszteléshez: [iOS][testflight] / [Android][firebase].

{{ references() }}
