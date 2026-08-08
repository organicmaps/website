---
title: "Október 7-i kiadás: Android Auto sebességkorlátozás, GeoJSON import, nyomvonalrögzítési statisztikák, OSM leírás címke megjelenítése, könyvjelző mentése a kiválasztott nyomvonalra iOS-en, és még több"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["releases"]
---

Ez az október 7-i Organic Maps frissítés sebességkorlátozás-megjelenítést hoz az Android Autóba, GeoJSON importot és nyomvonalrögzítési statisztikákat ad, megjeleníti az OSM leírás címkéket (ha látni szeretnéd őket, írd be a keresőmezőbe: `?description`), iOS-en pedig könyvjelzőt menthetsz egy nyomvonalra. Emellett számos fejlesztés érkezett a felhasználói felülethez és az OpenStreetMap-szerkesztéshez, valamint sok hibajavítás minden platformon, köztük az indításkori összeomlás javítása néhány Android készüléken.

Az Organic Maps a közreműködőinknek, [az adományaidnak](@/donate/index.hu.md) és [a támogatásodnak](@/contribute/index.hu.md) köszönhető ❤️.

### Részletes kiadási megjegyzések (az előző kisebb frissítés változásaival együtt)

- ÚJ! GeoJSON import (Sergiy Kozyr)
- OpenStreetMap adatok október 4-i állapot szerint
- Wikipédia adatok október 1-jei állapot szerint
- Seattle-i gyorsvasút támogatása a tömegközlekedésben (tjasz)
- A térképi kijelölés megmarad a szerkesztett OSM hely mentésekor (Kiryl Kaveryn)
- Frissített fordítások (Weblate közreműködők)

#### Térképstílusok

- Kerékpárkölcsönző boltok megjelenítése amenity=bicycle + rental=shop címkével (David Martinez)
- Régészeti helyszínek megjelenítése 12-es nagyítástól, egyéb történelmi helyszínek 15-ös nagyítástól Outdoor stílusban (Viktor Govako)
- Új ikonok az árbocokhoz, a távközlési és a villanyoszlopokhoz Outdoors stílusban (David Martinez)
- A csúcs ikon méretének növelése Outdoors stílusban (David Martinez)
- Hiányzó POI-ikonváltozatok pótlása (David Martinez)
- További sorompótípusok hozzáadva (Viktor Govako)

#### iOS

- ÚJ: Könyvjelző mentése a kiválasztott nyomvonalpontra (Kiryl Kaveryn)
- ÚJ: A rögzített nyomvonal törlése előzetes mentés nélkül (Kiryl Kaveryn)
- Többsoros könyvjelzőlista-címek megjelenítése a Hely oldalon (David Martinez)
- Az OSM bejelentkezési gombok stílusának frissítése (Kiryl Kaveryn)
- A navigációs információk frissítési hibájának javítása (Kiryl Kaveryn)
- Az új útvonaltervezés hibáinak javítása (Kiryl Kaveryn)
- OSM hely hozzáadásának és szerkesztésének láthatósága javítva a 3 hónapnál régebbi térképeknél (Kiryl Kaveryn)
- A közlekedési módok szegmensvezérlőjének elrendezése javítva iOS 26-hoz (Kiryl Kaveryn)
- Egyszerűsített könyvjelző-kijelölési animációk (Kiryl Kaveryn)
- Javítva a keresési találat kijelölésekor fellépő hiba (Kiryl Kaveryn)
- Javított stílus, csúsztatás és animációk a Hely információs oldalon (Kiryl Kaveryn)

#### Android Auto (csak Google Play)

- ÚJ: Sebességkorlátozás megjelenítése az Android Autóban (Andrei Shkrob)
- A képernyőváltás javítása az Android Auto navigációs módjában (Andrei Shkrob)
- Az útvonalnyíl eltolódásának javítása az Android Autóban (Andrei Shkrob)
- Javítva a hiba, amely az eszköz autóhoz csatlakoztatásakor vagy leválasztásakor lépett fel (Andrei Shkrob)
- Android Auto helyszolgáltatás hozzáadva (Andrei Shkrob)
- Az Android Auto útvonalszimulátorának fejlesztése (Viktor Govako)

#### Android

- ÚJ: A nyomvonalrögzítés statisztikáinak megtekintése valós időben (Kavi Khalique)
- ÚJ: Az OSM `description` címke tartalmának megjelenítése (Alexander Borsuk)
- A témaváltás kezelésének javítása (Andrei Shkrob)
- Több összeomlás javítva, köztük az indításkori is (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Csendes letöltési folyamatjelző értesítések (Viktor Govako)
- A ceruza ikon belső margójának csökkentése (Alexander Borsuk)

#### Asztali gép

- A Linuxon lefagyó curl javítása (Alexander Borsuk)
- A macOS-en az OSM-be való bejelentkezéskor tapasztalt lefagyás javítása (Alexander Borsuk)
- Objektum kijelölése a helyi menüből (Viktor Govako)
- Letöltés megszakítási lehetőség (Viktor Govako)
- Geometriatípus megjelenítése a helyi menüben (Viktor Govako)

### Friss funkciók, amelyeket esetleg kihagytál

- Tömegközlekedési járatszámok megjelenítése megálló kiválasztásakor
- Túra- és kerékpárútvonalak (kapcsold be őket a bal felső Rétegek gombbal)
- A könyvjelzők nevei a térképen: kapcsold be a Beállításokban
- A ✎ ceruza ikonnal gyorsan szerkesztheted a könyvjelzőket

### Az Organic Maps telepítése

Töltsd le a legújabb Organic Maps verziót innen: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] és [F-Droid][fdroid].

Csatlakozz a béta teszteléshez, hogy elsőként próbálhasd ki az újdonságokat: [iOS][testflight] / [Android][firebase].

{{ references() }}
