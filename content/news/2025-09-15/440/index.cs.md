---
title: "Vydání 15. září: nové plánování trasy a popisy OSM"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["releases"]
---

Toto druhé zářijové vydání přináší přepracovanou obrazovku plánování trasy a zobrazení obsahu tagu OpenStreetMap `description` na iOS. Chceš-li najít místa s tímto tagem, zadej do vyhledávání `?description` (podobně jako `?wiki` u míst propojených s Wikipedií).

Obsahuje také mnoho oprav a vylepšení pro iOS a Android (viz níže).

A samozřejmě připomínka dalších nedávných funkcí, které ti mohly uniknout:
- Čísla linek veřejné dopravy při výběru zastávky
- Pěší a cyklistické trasy (aktivuj je tlačítkem Vrstvy vlevo nahoře)
- Zobrazení názvů záložek na mapě (zapni v Nastavení aplikace)
- Ikona tužky ✎ umožňuje rychlou úpravu záložek

Organic Maps je možný díky přispěvatelům, [tvým darům](@/donate/index.cs.md) a [tvé podpoře](@/contribute/index.md).

### Podrobné poznámky k vydání

- Nová data OpenStreetMap k 13. září
- Odstraněny velmi malé ostrovy ze světové mapy (Viktor Govako)
- Zobrazení PSČ (ZIP) v detailech adresy (Viktor Govako)
- Opraveno nesprávné vystředění mapy na aktuální pozici (Kiryl Kaveryn, Viktor Govako)
- Zachování barev záložek při exportu/importu GPX (cyber-toad)
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

- NOVÉ: zobrazení obsahu tagu OSM `description` (vyzkoušej zadáním `?description` do vyhledávání) (Kiryl Kaveryn, Viktor Govako)
- NOVÉ: přepracovaná obrazovka plánování trasy (Kiryl Kaveryn)

#### Android

- Nové ikony kruhových objezdů v Android Auto (Andrei Shkrob)
- Zobrazení kategorie vybrané záložky (Alexander Borsuk)
- Opraveno zpoždění při zobrazení vzdálenosti k záložce (Alexander Borsuk)
- Přepracované tmavé téma (Andrei Shkrob)
- Opravená aktualizace polohy v navigaci na custom ROM (např. Lineage + MicroG) (Viktor Govako)
- Modrá ikona tužky (úpravy) pro záložky (Alexander Borsuk)
- Snížená vertikální výška náhledu informací o místě (Alexander Borsuk)
- Odstraněn azimutální úhel k severu z náhledu informací o místě (klepni na modrou šipku se vzdáleností a uvidíš ho) (Alexander Borsuk)

Stáhni si nejnovější verzi Organic Maps z [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] a [F-Droid][fdroid].

P.S. Připoj se k beta testování a vyzkoušej novinky dřív: [iOS][testflight] / [Android][firebase].

{{ references() }}
