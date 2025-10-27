---
title: "Říjnové vydání: Rychlostní limity v Android Auto, import GeoJSON, statistiky nahrávání tras, zobrazení popisu OSM, ukládání značek na vybrané trase v iOS a další"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

Tato říjnová aktualizace Organic Maps přidává zobrazení rychlostních limitů v Android Auto, import GeoJSON, statistiky nahrávání tras, zobrazuje značky popisu OSM (zadejte `?description` do vyhledávacího pole, abyste je viděli) a ukládá značku na trase v iOS. Existuje také mnoho vylepšení uživatelského rozhraní, úprav OpenStreetMap a různé opravy chyb na všech platformách, včetně opravy pády při spuštění na některých zařízeních Android.

Organic Maps je možný díky ❤️ našim přispěvatelům, [vašim darům](@/donate/index.cs.md) a [vaší podpoře](@/contribute/index.cs.md).

### Podrobné poznámky k vydání (včetně změn předchozí menší aktualizace)

- NOVÉ! Import GeoJSON (Sergiy Kozyr)
- Data OpenStreetMap k 4. říjnu
- Data Wikipedie k 1. říjnu
- Podpora lehké železnice Seattle pro veřejnou dopravu (tjasz)
- Nedeaktivovat výběr mapy při ukládání upraveného místa OSM (Kiryl Kaveryn)
- Aktualizované překlady (přispěvatelé Weblate)

#### Styly map

- Zobrazení půjčoven kol označených jako amenity=bicycle + rental=shop (David Martinez)
- Zobrazení historických archeologických lokalit od zoomu 12 a dalších historických lokalit od zoomu 15 ve stylu Outdoor (Viktor Govako)
- Nové ikony pro stožáry, komunikační a elektrické věže ve stylu Outdoor (David Martinez)
- Zvětšení ikony vrcholu ve stylu Outdoor (David Martinez)
- Přidání chybějících variant ikon POI (David Martinez)
- Přidáno více typů bariér (Viktor Govako)

#### iOS

- NOVÉ: Uložení značky na vybraném bodě trasy (Kiryl Kaveryn)
- NOVÉ: Odstranění nahrávané trasy bez jejího uložení (Kiryl Kaveryn)
- Zobrazení víceřádkových názvů seznamů značek na stránce Místo (David Martinez)
- Aktualizace stylu přihlašovacích tlačítek OSM (Kiryl Kaveryn)
- Oprava problému s aktualizací navigačních informací (Kiryl Kaveryn)
- Oprava problémů s plánováním nové trasy (Kiryl Kaveryn)
- Oprava viditelnosti přidání/úpravy místa OSM pro mapy starší než 3 měsíce (Kiryl Kaveryn)
- Oprava rozložení ovládání segmentu dopravních možností pro iOS 26 (Kiryl Kaveryn)
- Zjednodušení animací výběru značek (Kiryl Kaveryn)
- Oprava problému s výběrem výsledku vyhledávání (Kiryl Kaveryn)
- Opravený styl, přejetí a animace pro stránku Informace o místě (Kiryl Kaveryn)

#### Android Auto (pouze Google Play)

- NOVÉ: Zobrazení rychlostního limitu v Android Auto (Andrei Shkrob)
- Oprava přepínání displeje v režimu navigace Android Auto (Andrei Shkrob)
- Oprava posunu šipky trasy v Android Auto (Andrei Shkrob)
- Oprava problému při připojení/odpojení zařízení k automobilu (Andrei Shkrob)
- Přidání služby polohy Android Auto (Andrei Shkrob)
- Vylepšení simulátoru trasy Android Auto (Viktor Govako)

#### Android

- NOVÉ: Zobrazení statistik nahrávání tras v reálném čase (Kavi Khalique)
- NOVÉ: Zobrazení obsahu značky `description` OSM (Alexander Borsuk)
- Oprava zpracování změny motivu (Andrei Shkrob)
- Opraveno několik pádů, včetně pádu při spuštění (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Tiché oznámení o průběhu stahování (Viktor Govako)
- Zmenšení odsazení ikony tužky (Alexander Borsuk)

#### Desktop

- Oprava zamrznutí curl na Linuxu (Alexander Borsuk)
- Oprava zamrznutí na macOS při přihlašování k OSM (Alexander Borsuk)
- Akce pro výběr funkce z kontextového menu (Viktor Govako)
- Možnost zrušení stahování (Viktor Govako)
- Zobrazení typu geometrie v kontextovém menu (Viktor Govako)

### Nedávno vydané funkce, které jste mohli přehlédnout

- Čísla tras veřejné dopravy při výběru autobusové zastávky
- Pěší a cyklistické trasy (aktivujte je přes tlačítko Vrstvy v levém horním rohu)
- Zobrazení názvů značek na mapě jejich aktivací v nastavení aplikace
- Ikona tužky ✎ nabízí rychlý způsob úpravy značek

### Instalace Organic Maps

Získejte nejnovější verzi Organic Maps z [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] a [F-Droid][fdroid].

Připojte se k beta testování pro včasné funkce: [iOS][testflight] / [Android][firebase].

{{ references() }}
