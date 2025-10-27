---
title: "Vydání 15. září: nové plánování trasy a popisy OSM"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

Toto druhé zářijové vydání přináší přepracovanou obrazovku plánování trasy a zobrazení obsahu tagu OpenStreetMap `description` na iOS. Chcete-li najít místa s tímto tagem, zadejte do vyhledávání `?description` (podobně jako `?wiki`).

Obsahuje také mnoho oprav a vylepšení pro iOS a Android (viz níže).

Nedávné funkce, které vám mohly uniknout:
- Čísla linek veřejné dopravy při výběru zastávky
- Pěší a cyklistické trasy (aktivujte přes tlačítko Vrstvy vlevo nahoře)
- Zobrazení názvů značek na mapě (zapněte v Nastavení)
- Ikona ✎ umožňuje rychlou úpravu značek

Organic Maps je možný díky přispěvatelům, [vašim darům](@/donate/index.cs.md) a [vaší podpoře](@/contribute/index.md).

### Podrobné poznámky k vydání

- Nová data OpenStreetMap k 13. září
- Odstraněny velmi malé ostrovy ze světové mapy (Viktor Govako)
- Zobrazení PSČ (ZIP) v detailech adresy (Viktor Govako)
- Opraveno nesprávné vystředění mapy na aktuální pozici (Kiryl Kaveryn, Viktor Govako)
- Zachování barev značek při exportu/importu GPX (cyber-toad)
- Aktualizované překlady (přispěvatelé Weblate)

#### Styly map (Viktor Govako)

- Zobrazení obchodů s osvětlením
- Zobrazení elektrických vedení od zoomu 18
- Zobrazení referencí elektráren a trafostanic
- Zobrazení kempů a stellplatzů v navigačním režimu
- Oprava barvy sekundárních silnic v navigačním režimu
- Kreslení hranic národních parků
- Kreslení archeologických lokalit od zoomu 12 ve stylu Outdoor

#### iOS

- NOVÉ: zobrazení obsahu tagu OSM `description` (hledejte `?description`) (Kiryl Kaveryn, Viktor Govako)
- NOVÉ: přepracovaná obrazovka plánování trasy (Kiryl Kaveryn)

#### Android

- Nové ikony kruhových objezdů v Android Auto (Andrei Shkrob)
- Zobrazení kategorie vybrané značky (Alexander Borsuk)
- Opraveno zpoždění při zobrazení vzdálenosti ke značce (Alexander Borsuk)
- Přepracované tmavé téma (Andrei Shkrob)
- Opravená aktualizace polohy v navigaci na custom ROM (např. Lineage + MicroG) (Viktor Govako)
- Modrá ikona tužky (úpravy) pro značky (Alexander Borsuk)
- Snížená vertikální výška náhledu informací o místě (Alexander Borsuk)
- Odstraněn azimutální úhel k severu z náhledu (klepněte na modrou šipku se vzdáleností) (Alexander Borsuk)

Stáhněte si nejnovější verzi: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Připojte se k betě: [iOS][testflight] / [Android][firebase].

{{ references() }}
