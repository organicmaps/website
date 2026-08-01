---
title: "Hibajavítások és fejlesztések a tömegközlekedés, az útvonaltervezés, a keresés és a könyvjelzők terén a 2026. júliusi frissítésben"
date: 2026-07-23
slug: "hibajavitasok-fejlesztesek-tomegkozlekedes-utvonaltervezes-kereses-konyvjelzok-2026-julius"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Ahogyan talán már észrevette, megjelent a júliusi Organic Maps frissítés. Letöltheti a <https://get.omaps.org> oldalról, illetve az [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] és [F-Droid][fdroid] weboldalakon.

Az Ön [adományainak](@/donate/index.hu.md) és [visszajelzéseinek](@/contribute/index.hu.md) köszönhetően júliusban a hibajavításokra és a fejlesztésekre összpontosítottunk. Ha esetleg elkerülte volna a figyelmét, az [előző, júniusi kiadásból](@/news/2026-06-29/610/index.hu.md) a következő funkciók is elérhetők:
- Tömegközlekedési útvonalak (az élő menetrendek kidolgozás alatt állnak)
- Műholdas felvételek
- Alternatív útvonalak autózáshoz, túrázáshoz és kerékpározáshoz
- Új keresési és útvonaltervezési felület Androidra
- Nagy méretű, akadálymentes betűtípusok támogatása iOS-en

## Részletes változásnapló

### Térkép és helyek
- OpenStreetMap-adatok frissítve július 14-i állapotra
- Az [OpenStreetMap](https://www.openstreetmap.org)-re beküldött jegyzetek mostantól pontosan az Ön által kiválasztott helyre kerülnek, nem pedig az egész utca vagy terület közepére _(Alexander Borsuk)_
- Javított helyválasztás a térkép megérintésekor azokon a területeken, amelyek átnyúlnak a 180°-os antimeridiánon _(Viktor Govako)_
- A nyomvonalak magassági profiljai már nem mutatnak elavult vagy üres grafikont a nyomvonal törlése után _(Kiryl Kaveryn)_

### Tömegközlekedés
- A megálló-, átszállóhely- és állomásnevek mostantól fehér kontúrral jelennek meg, hogy világos és sötét témákban egyaránt jól olvashatók legyenek _(Viktor Govako)_
- A metróréteg helyesen jelenik meg újra, miután bezárja a tömegközlekedési útvonal előnézetét _(Mikhail Listratsenka)_

### Útvonaltervezés és navigáció
- Az útvonalra vonatkozó figyelmeztetések (útdíjak, kompok, földutak, lépcsők stb.) mostantól minden alternatív útvonal esetében megjelennek _(Viktor Govako)_
- Kijavítottuk az útvonal létrehozása közben ritkán előforduló lefagyást _(Viktor Govako)_
- A zsákutcák, valamint a korlátozott forgalmú utak kiindulási és végpontjainak kezelésének javítása _(Viktor Govako)_
- Kijavítottuk a hibás és hiányzó kanyarodási utasításokat _(Alexander Borsuk)_

### iOS
- Új „Keresési előzmények mentése” beállítás, amely lehetővé teszi az előzmények kikapcsolását és elrejtését, ha nem szeretné megőrizni őket _(Kiryl Kaveryn)_
- Új „Szerkesztés” gomb a könyvjelzők egyszerűbb eltávolításához _(Kiryl Kaveryn)_
- A könyvjelzők mostantól automatikusan elmentésre kerülnek, amikor elhagyja a képernyőt _(Kiryl Kaveryn)_
- A színpaletta mostantól előre definiált színeket kínál, és lehetővé teszi bármely egyéni szín kiválasztását _(Kiryl Kaveryn)_
- Javítottuk a rögzített nyomvonal magassági diagramjának üres állapotát _(Kiryl Kaveryn)_
- Javítottuk a „Start” gombon megjelenő útvonal-haladást _(Kiryl Kaveryn)_
- Az útvonal állomásainak átrendezése már nem okoz ugrálást a listában _(Kiryl Kaveryn)_
- Egyéb kisebb felületi fejlesztések _(Kiryl Kaveryn)_

### Android
- A nyitvatartási idők mostantól osztott műszakokat is mutatnak (például az ebédszünetet), a mai nappal kezdődnek, és a teljes hetet külön görgetési terület nélkül jelenítik meg _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Tisztább keresősáv, amelyben a törlés és a hangvezérlés gombjai egybeolvadtak, a törlés ikonja már nem mozog, valamint elrendezési javítások fekvő módhoz és a telefon elforgatásához _(Mikhail Listratsenka)_
- Átdolgozott könyvjelző- és nyomvonalszerkesztő _(Mikhail Listratsenka)_
- Útvonaltervezési javítások és fejlesztések _(Mikhail Listratsenka)_
- A színválasztó mostantól automatikusan bezárul, és kijavították az Android 5-ön előforduló összeomlást _(Mikhail Listratsenka)_
- Kijavított összeomlások _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- A letölthető térképek listája mostantól ábécé sorrendben van rendezve _(goncalo109560)_

### Fordítások
- Javított kínai megfogalmazás _(Chenxi Zhao)_
- Frissített ukrán fordítások _(Nnifria)_
- Kijavítottuk a térkép régióneveinek olasz fordításait _(Vittorio Bertola)_

## Csatlakozzon a bétateszteléshez, próbálja ki korán az új funkciókat, és jelentse a hibákat:

Tipp: A béta verzió új domborzati árnyékolással, továbbfejlesztett magassági adatokkal – amelyek már lábban és méterben is megjelennek –, valamint egyéb remek funkciókkal rendelkezik!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Kellemes nyarat!
Az Organic Maps csapat

{{ references() }}
