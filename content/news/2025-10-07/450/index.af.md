---
title: "Oktober-vrystelling: Spoedbeperkings in Android Auto, GeoJSON-invoer, opname-baan statistieke, OSM-beskrywing-etiket vertoon, stoor boekmerk op gekose baan op iOS, en meer"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
---

Hierdie Oktober Organic Maps-opdatering voeg spoedbeperkingsvertoning in Android Auto, GeoJSON-invoer, opname-baan statistieke, wys OSM-beskrywingetikette (tik `?description` in die soekveld om hulle te sien), en stoor 'n boekmerk op 'n baan op iOS. Daar is ook baie verbeterings aan die gebruikerskoppelvlak, OpenStreetMap-redigering, en verskeie foutoplossings oor alle platforms, insluitend die breekoplossing by aanvang op sommige Android-toestelle.

Organic Maps is moontlik danksy ❤️ ons bydraers, [jou donasies](@/donate/index.af.md), en [jou ondersteuning](@/contribute/index.af.md).

### Gedetailleerde vrystellingsnotas (insluitend die vorige klein opdatering-wysigings)

- NUUT! Invoer GeoJSON (Sergiy Kozyr)
- OpenStreetMap-data vanaf 4 Oktober
- Wikipedia-data vanaf 1 Oktober
- Seattle light rail ondersteuning vir openbare vervoer (tjasz)
- Moenie kaartseleksie deaktiveer wanneer 'n geredigeerde OSM-plek gestoor word nie (Kiryl Kaveryn)
- Vertalings opgedateer (Weblate-bydraers)

#### Kaartstyle

- Wys fiets-verhuurwinkels gemerk as amenity=bicycle + rental=shop (David Martinez)
- Wys historiese argeologiese terreine vanaf zoom 12 en ander historiese terreine vanaf zoom 15 in Outdoor-styl (Viktor Govako)
- Nuwe ikone vir maste, kommunikasie en kragtorings in Outdoor-styl (David Martinez)
- Vergroot piek-ikoongrootte in Outdoor-styl (David Martinez)
- Voeg ontbrekende POI-ikoonvariante by (David Martinez)
- Meer versperring-tipes bygevoeg (Viktor Govako)

#### iOS

- NUUT: Stoor boekmerk op gekose baanpunt (Kiryl Kaveryn)
- NUUT: Verwyder die opname-baan sonder om dit eers te stoor (Kiryl Kaveryn)
- Wys multi-lyn boekmerklys-titels in Plek-bladsy (David Martinez)
- Opdateer OSM-aanmeldknoppie-styl (Kiryl Kaveryn)
- Regmaak navigasie-inligting opdatering kwessie (Kiryl Kaveryn)
- Regmaak nuwe roete-beplanningkwessies (Kiryl Kaveryn)
- Regmaak OSM voeg by/wysig plek sigbaarheid vir kaarte ouer as 3 maande (Kiryl Kaveryn)
- Regmaak vervoer-opsies segmentbeheer uitleg vir iOS 26 (Kiryl Kaveryn)
- Vereenvoudig boekmerkselectie-animasies (Kiryl Kaveryn)
- Regmaak soekresultaat-seleksie kwessie (Kiryl Kaveryn)
- Opgeloste styl, vee en animasies vir Plek-inligtingbladsy (Kiryl Kaveryn)

#### Android Auto (slegs Google Play)

- NUUT: Spoedbeperkingsvertoning in Android Auto (Andrei Shkrob)
- Regmaak vertoonskakel in Android Auto navigasiemodus (Andrei Shkrob)
- Regmaak roete-pyltjie-verplasing in Android Auto (Andrei Shkrob)
- Regmaak kwessie wanneer 'n toestel gekoppel/ontkoppel word aan 'n motor (Andrei Shkrob)
- Voeg Android Auto Ligging-diens by (Andrei Shkrob)
- Verbeter Android Auto roete-simulator (Viktor Govako)

#### Android

- NUUT: Bekyk opname-baan statistieke in reële tyd (Kavi Khalique)
- NUUT: Wys OSM `description`-etiketinhoud (Alexander Borsuk)
- Regmaak tema-verandering hantering (Andrei Shkrob)
- Verskeie brekes reggemaak, insluitend die een by aanvang (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Stil aflaai-vordering kennisgewings (Viktor Govako)
- Verminder potlood-ikoon-vulling (Alexander Borsuk)

#### Desktop

- Regmaak hangende curl op Linux (Alexander Borsuk)
- Regmaak hangende op macOS wanneer by OSM aangemeld word (Alexander Borsuk)
- Aksie om kenmerk uit kontekskieslys te kies (Viktor Govako)
- Kanselleer aflaai-opsie (Viktor Govako)
- Wys geometrie-tipe in kontekskieslys (Viktor Govako)

### Onlangs vrygestel funksies wat jy dalk gemis het

- Openbare vervoer roetenommers wanneer 'n bushalte gekies word
- Stap- en fietsroetes (skakel hulle aan via die Lae-knoppie links bo)
- Sien boekmerknaam op die kaart deur dit in die app Instellings te aktiveer
- Die ✎ potlood-ikoon bied 'n vinnige manier om boekmerke te wysig

### Installeer Organic Maps

Kry die nuutste Organic Maps-weergawe vanaf die [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], en [F-Droid][fdroid].

Sluit aan by beta-toetsing vir vroeë kenmerke: [iOS][testflight] / [Android][firebase].

{{ references() }}
