---
title: "Szeptember 15-i kiadás: új útvonaltervezés és OSM leírások"
date: 2025-09-15T10:00:00+00:00
---

A szeptemberi második kiadás egy áttervezett útvonaltervező képernyőt és az OpenStreetMap `description` címke tartalmának megjelenítését hozza iOS-en. Helyek kereséséhez ezzel a címkével írd be a keresésbe: `?description` (hasonló a `?wiki`-hez).

Számos javítást és fejlesztést is tartalmaz iOS-hez és Androidhoz (részletek lentebb).

Friss funkciók, amelyeket esetleg kihagytál:
- Tömegközlekedési járatszámok megjelenítése megálló kiválasztásakor
- Túra- és kerékpár-útvonalak (kapcsold be a Rétegek gombbal bal felül)
- Jelölők neveinek megjelenítése a térképen (Beállításokban engedélyezhető)
- A ✎ ikon gyors szerkesztést biztosít a jelölőknél

Az Organic Maps a közreműködőknek, [adományaidnak](@/donate/index.hu.md) és [támogatásodnak](@/contribute/index.md) köszönhető.

### Részletes kiadási megjegyzések

- Új OpenStreetMap adatok: szeptember 13.
- Nagyon kicsi szigetek eltávolítva a világtérképről (Viktor Govako)
- Irányítószám (ZIP) megjelenítése a cím részleteiben (Viktor Govako)
- Hibás térkép-középre igazítás javítva az aktuális pozícióra (Kiryl Kaveryn, Viktor Govako)
- Jelölőszínek megőrzése GPX export/import során (cyber-toad)
- Frissített fordítások (Weblate közreműködők)

#### Térképstílusok (Viktor Govako)

- Világítási üzletek megjelenítése
- Távvezetékek megjelenítése 18-as nagyítástól
- Erőművek és alállomások referencia-neveinek megjelenítése
- Kempingek és lakókocsi-helyek megjelenítése navigációs módban
- Másodlagos utak színének javítása navigációs módban
- Nemzeti parkok határainak rajzolása
- Régészeti helyszínek rajzolása 12-es nagyítástól Outdoor stílusban

#### iOS

- ÚJ: OSM `description` címke tartalmának megjelenítése (keresd: `?description`) (Kiryl Kaveryn, Viktor Govako)
- ÚJ: áttervezett útvonaltervező képernyő (Kiryl Kaveryn)

#### Android

- Új körforgalom ikonok Android Auto-ban (Andrei Shkrob)
- Kiválasztott jelölő kategóriájának megjelenítése (Alexander Borsuk)
- Késleltetés javítása jelölő távolságának megjelenítésénél (Alexander Borsuk)
- Újrastrukturált sötét téma (Andrei Shkrob)
- Pozíciófrissítési hiba javítva navigációban egyedi ROM-okon (pl. Lineage + MicroG) (Viktor Govako)
- Kék ceruza (szerkesztés) ikon jelölőkhöz (Alexander Borsuk)
- Helyinformáció-előnézet függőleges magasságának csökkentése (Alexander Borsuk)
- Észak felé mutató azimut szög eltávolítva az előnézetből (kék nyíl érintésével megtekinthető) (Alexander Borsuk)

Töltsd le a legújabb verziót: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Csatlakozz a béta teszteléshez: [iOS][testflight] / [Android][firebase].

{{ references() }}
