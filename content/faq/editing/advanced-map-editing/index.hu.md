---
title: Hogyan végezhetek fejlettebb térképszerkesztést?
slug: hogyan-végezhetek-fejlettebb-térképszerkesztést
description: Oktatóanyag az OpenStreetMap szerkesztéséhez olyan fejlettebb eszközökkel,
  mint az ID, a Go Map és a Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
aliases:
  - /hu/faq/editing/advanced-map-editing/
---

Az Organic Maps tartalmaz egy egyszerű és könnyen használható szerkesztőt, amellyel szerkesztheti a térképet. A szerkesztő azonban korlátozott, és csak egyszerű pontjellemzők hozzáadását teszi lehetővé, ami azt jelenti, hogy nincsenek épületek körvonalai, utak, tavak, városok stb. Ha olyan dolgot szeretne megváltoztatni, amelyet nem szerkeszthet a beépített szerkesztővel, akkor ez a megfelelő GYIK oldal.

Mivel az organikus térképekben használt összes térképadat az [OpenStreetMap.org (OSM)] webhelyről (https://www.openstreetmap.org) származik, ott közvetlenül frissítheti a térképet. A módosítások ezután a következő térképfrissítéssel bekerülnek az Organikus térképek közé.

## OpenStreetMap szerkesztők

Az OSM szerkesztéséhez több lehetőség is van. Ha van kéznél laptopja vagy asztali számítógépe, jobb, ha a böngészőjében futó [ID Editor]-t (https://www.openstreetmap.org/edit) használja. Az ID Editor a kezdők számára egyszerű, a nagyobb képernyő, az egér és a billentyűzet pedig megkönnyíti a térképszerkesztést.

Ha speciális térképszerkesztést szeretne végezni mobileszközről, használja a [Go Map](https://apps.apple.com/us/app/go-map/id592990211) alkalmazást iOS rendszeren vagy a [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) alkalmazást Android esetén. A Go Map a kezdők számára egyszerű, míg a Vespucci a haladóbb felhasználókat célozza meg. A LearnOSM oktatóanyagokat biztosít a [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) és a [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/) számára.

Az egyszerűbb és szórakoztatóbb szerkesztések érdekében kipróbálhatja az [Every Door alkalmazást](https://every-door.app/) iOS-re és Androidra, illetve a [StreetComplete alkalmazást](https://streetcomplete.app/) Androidra.

#### Azonosító szerkesztő

Az OpenStreetMap azonosítóval történő szerkesztéséhez kövesse az alábbi lépéseket:

1. Hozzon létre egy új fiókot, vagy jelentkezzen be az [OpenStreetMap.org] oldalon (https://www.openstreetmap.org)
2. Keresse meg a szerkeszteni kívánt helyet az OpenStreetMap.org oldalon, és kattintson a felül található *Szerkesztés* gombra.
3. *Indítsa el a Walkthrough-t*, és kövesse az ID-szerkesztőt ismertető rövid útmutatót
4. Szerkessze a térképet
5. Töltse fel a módosításokat

Ez az, most az OSM közösség tagja vagy.

## Mi történik a szerkesztéseimmel?

Miután megnyomta a *Feltöltés* gombot, a módosítások azonnal hozzáadódnak a nyilvános OSM adatbázishoz. Tehát legyen körültekintő a szerkesztés során. Az Organikus térképekben a módosítások a következő havi térképfrissítés után lesznek láthatók.

Az Ön e-mailje nincs közzétéve, de mások láthatják az Ön OSM-felhasználónevét. Mivel az OSM lehetőséget kínál a változtatások megvitatására, előfordulhat, hogy az OSM többi közreműködőjétől kérdéseket kaphat a módosításaival kapcsolatban. Erről az OSM-fiók regisztrálásához használt e-mail címen kap értesítést. Mivel az OSM egy együttműködésre épülő közösségi projekt, mindig válaszolnia kell az ilyen kérdésekre.

## Közösség és Wiki

Az OpenStreetMap egy közösség. Ha segítségre van szüksége, vagy bármilyen kérdése van, felteheti az [OSM fórumon](https://community.openstreetmap.org/c/help-and-support), vagy tekintse meg az [OSM Wiki](https://wiki.openstreetmap.org/) dokumentációját.

## Címkék – Hogyan működik az OSM adatmodell

Az OpenStreetMap adatbázis olyan objektumokat tartalmaz, mint a csomópontok, utak, területek és kapcsolatok, amelyek elvonatkoztatnak a való világ jellemzőitől. Ezek az objektumok attribútumokkal, úgynevezett címkékkel rendelkeznek a további leírásukra. A címke kulcs-érték kombináció.

Mivel ez bonyolultabbnak hangzik, mint amilyen, adunk egy példát:
Az étterem pl. jegyzetként vagy területként leképezve az ``` amenity=restaurant``` címkével. Ezután további címkék, például ```cousine=*``` vagy ```opening_hours=*``` használhatók további részletekért.

> Vegye figyelembe, hogy az ID szerkesztő elrejti a belső adatstruktúrát a felhasználók elől, hogy kezdőbarátabb legyen. De a Wiki-dokumentáció olvasásához hasznos az adatstruktúra rövid áttekintése.
Az azonosítószerkesztőben megtekintheti az azonosító által elrejtett címkéket, ha kibontja a *Címkék* részt a *Szerkesztési szolgáltatás* oldalsó panelén.

## OSM Notes {#osm-note}

Ha nincs ideje, vagy a probléma túl bonyolult ahhoz, hogy saját maga szerkeszthesse az OSM-adatokat, az OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) a megfelelő út. Elhelyezhet egy ilyen megjegyzést a térképhiba helyén, és részletesen leírhatja a problémát. Más OSM önkéntesek segíthetnek és megoldhatják a problémát. E-mail értesítést kap az OSM-fiókján keresztül, ha további kérdéseik vannak, vagy az OSM Note megoldódik.

1. Hozzon létre egy új fiókot, vagy jelentkezzen be az [OpenStreetMap.org] oldalon (https://www.openstreetmap.org)
   > Névtelen jegyzeteket is megnyithat, de ez nem ajánlott, mivel nem kap értesítést, ha a probléma megoldódott, vagy további kérdések merülnek fel.
2. Nagyítsa ki a térkép helyét az [OpenStreetMap.org] oldalon (https://www.openstreetmap.org), majd nyomja meg a *Jegyzet hozzáadása a térképhez* gombot (a második ikon alulról a jobb oldali menüben). Ezután húzza a kék térképjelzőt a pontos helyre.
   > Próbálj meg a lehető legpontosabban fogalmazni.
3. Adja meg a térképprobléma részletes leírását, majd nyomja meg a *Megjegyzés* gombot.
   > Boltok számára pl. adja meg a nevet, és említse meg, hogy mit árulnak ott, vagy milyen szolgáltatásokat kínálnak.
