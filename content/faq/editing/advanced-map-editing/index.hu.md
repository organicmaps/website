---
title: Hogyan végezhetek fejlettebb térképszerkesztést?
slug: hogyan-végezhetek-fejlettebb-térképszerkesztést
description: Oktatóanyag az OpenStreetMap szerkesztéséhez olyan fejlettebb eszközökkel,
  mint az ID, a Go Map és a Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - map-editing
extra:
  order: 40
aliases:
  - /hu/faq/editing/advanced-map-editing/
---

Az Organic Maps tartalmaz egy egyszerű és könnyen használható szerkesztőt, amellyel szerkesztheted a térképet. A szerkesztő azonban korlátozott, és csak egyszerű pontjellemzők hozzáadását teszi lehetővé, ami azt jelenti, hogy nincsenek épületek körvonalai, utak, tavak, városok stb. Ha olyan dolgot szeretnél megváltoztatni, amelyet nem szerkeszthetsz a beépített szerkesztővel, akkor ez a megfelelő GYIK oldal.

Mivel az Organic Maps-ben használt összes térképadat az [OpenStreetMap.org (OSM)](https://www.openstreetmap.org) webhelyről származik, ott közvetlenül frissítheted a térképet. A módosítások ezután a következő térképfrissítéssel bekerülnek az Organic Maps-be.

## OpenStreetMap szerkesztők

Az OSM szerkesztéséhez több lehetőség is van. Ha van kéznél laptopod vagy asztali számítógéped, jobb, ha a böngésződben futó [ID Editor](https://www.openstreetmap.org/edit)-t használod. Az ID Editor a kezdők számára egyszerű, a nagyobb képernyő, az egér és a billentyűzet pedig megkönnyíti a térképszerkesztést.

Ha speciális térképszerkesztést szeretnél végezni mobileszközről, használd a [Go Map](https://apps.apple.com/us/app/go-map/id592990211) alkalmazást iOS rendszeren vagy a [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) alkalmazást Android esetén. A Go Map a kezdők számára egyszerű, míg a Vespucci a haladóbb felhasználókat célozza meg. A LearnOSM oktatóanyagokat biztosít a [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) és a [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/) számára.

Az egyszerűbb és szórakoztatóbb szerkesztések érdekében kipróbálhatod az [Every Door alkalmazást](https://every-door.app/) iOS-re és Androidra, illetve a [StreetComplete alkalmazást](https://streetcomplete.app/) Androidra.

#### ID Editor

Az OpenStreetMap azonosítóval történő szerkesztéséhez kövesd az alábbi lépéseket:

1. Hozz létre egy új fiókot, vagy jelentkezz be az [OpenStreetMap.org](https://www.openstreetmap.org) oldalon
2. Keresd meg a szerkeszteni kívánt helyet az OpenStreetMap.org oldalon, és kattints a felül található *Szerkesztés* gombra.
3. *Indítsd el a Walkthrough-t*, és kövesd az ID Editor-t ismertető rövid útmutatót
4. Szerkeszd a térképet
5. Töltsd fel a módosításokat

Ez az, most az OSM közösség tagja vagy.

## Mi történik a szerkesztéseimmel?

Miután megnyomtad a *Feltöltés* gombot, a módosítások azonnal hozzáadódnak a nyilvános OSM adatbázishoz. Tehát legyél körültekintő a szerkesztés során. Az Organic Maps-ben a módosítások a következő havi térképfrissítés után lesznek láthatók.

Az e-mailed nincs közzétéve, de mások láthatják az OSM-felhasználónevedet. Mivel az OSM lehetőséget kínál a változtatások megvitatására, előfordulhat, hogy az OSM többi közreműködőjétől kérdéseket kaphatsz a módosításaiddal kapcsolatban. Erről az OSM-fiók regisztrálásához használt e-mail címen kapsz értesítést. Mivel az OSM egy együttműködésre épülő közösségi projekt, mindig válaszolnod kell az ilyen kérdésekre.

## Közösség és Wiki

Az OpenStreetMap egy közösség. Ha segítségre van szükséged, vagy bármilyen kérdésed van, felteheted az [OSM fórumon](https://community.openstreetmap.org/c/help-and-support), vagy tekintsd meg az [OSM Wiki](https://wiki.openstreetmap.org/) dokumentációját.

## Címkék – Hogyan működik az OSM adatmodell

Az OpenStreetMap adatbázis olyan objektumokat tartalmaz, mint a csomópontok, utak, területek és kapcsolatok, amelyek elvonatkoztatnak a való világ jellemzőitől. Ezek az objektumok attribútumokkal, úgynevezett címkékkel rendelkeznek a további leírásukra. A címke kulcs-érték kombináció.

Mivel ez bonyolultabbnak hangzik, mint amilyen, adunk egy példát:
Az étterem pl. jegyzetként vagy területként leképezve az `amenity=restaurant` címkével. Ezután további címkék, például `cuisine=*` vagy `opening_hours=*` használhatók további részletekért.

> Vedd figyelembe, hogy az ID szerkesztő elrejti a belső adatstruktúrát a felhasználók elől, hogy kezdőbarátabb legyen. De a Wiki-dokumentáció olvasásához hasznos az adatstruktúra rövid áttekintése.
Az ID Editor-ben megtekintheted az azonosító által elrejtett címkéket, ha kibontod a *Címkék* részt a *Szerkesztési szolgáltatás* oldalsó panelén.

## OSM Notes {#osm-note}

Ha nincs időd, vagy a probléma túl bonyolult ahhoz, hogy magad szerkeszd az OSM-adatokat, az OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) a megfelelő út. Elhelyezhetsz egy ilyen megjegyzést a térképhiba helyén, és részletesen leírhatod a problémát. Más OSM önkéntesek segíthetnek és megoldhatják a problémát. E-mail értesítést kapsz az OSM-fiókodon keresztül, ha további kérdéseik vannak, vagy az OSM Note megoldódik.

1. Hozz létre egy új fiókot, vagy jelentkezz be az [OpenStreetMap.org](https://www.openstreetmap.org) oldalon
   > Névtelen jegyzeteket is megnyithatsz, de ez nem ajánlott, mivel nem kapsz értesítést, ha a probléma megoldódott, vagy további kérdések merülnek fel.
2. Nagyítsd ki a térkép helyét az [OpenStreetMap.org](https://www.openstreetmap.org) oldalon, majd nyomd meg a *Jegyzet hozzáadása a térképhez* gombot (a második ikon alulról a jobb oldali menüben). Ezután húzd a kék térképjelzőt a pontos helyre.
   > Próbálj meg a lehető legpontosabban fogalmazni.
3. Add meg a térképprobléma részletes leírását, majd nyomd meg a *Megjegyzés* gombot.
   > Boltok számára pl. add meg a nevet, és említsd meg, hogy mit árulnak ott, vagy milyen szolgáltatásokat kínálnak.
