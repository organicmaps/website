---
title: "Release 15 september: nieuw routeplan en OSM-beschrijvingen"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

Deze tweede septemberrelease bevat een vernieuwd scherm voor routeplanning en de weergave van de OpenStreetMap-tag `description` op iOS. Typ `?description` in het zoekvak om plaatsen met deze tag te vinden (vergelijkbaar met `?wiki`).

Er zijn ook veel verbeteringen en oplossingen voor iOS en Android (details hieronder).

Recente functies die je misschien gemist hebt:
- Lijnnummers van openbaar vervoer bij selectie van een halte
- Wandel- en fietsroutes (schakel ze in via de knop Lagen linksboven)
- Naamn van markeringen op de kaart tonen (inschakelen in Instellingen)
- Het ✎-pictogram maakt snel bewerken van markeringen mogelijk

Organic Maps is mogelijk dankzij onze bijdragers, [jouw donaties](@/donate/index.nl.md) en [jouw steun](@/contribute/index.md).

### Gedetailleerde release-opmerkingen

- Nieuwe OpenStreetMap-gegevens per 13 september
- Zeer kleine eilanden van de wereldkaart verwijderd (Viktor Govako)
- Postcode (ZIP) tonen in adresdetails (Viktor Govako)
- Onjuiste centrering op huidige positie verholpen (Kiryl Kaveryn, Viktor Govako)
- Marker-kleuren behouden bij exporteren/importeren van GPX (cyber-toad)
- Bijgewerkte vertalingen (Weblate-bijdragers)

#### Kaartstijlen (Viktor Govako)

- Verlichtingswinkels tonen
- Hoogspanningslijnen tonen vanaf zoom 18
- Referentienamen van energiecentrales en onderstations tonen
- Campings en caravanplaatsen in navigatiemodus tonen
- Kleur van secundaire wegen corrigeren in navigatiemodus
- Grenzen van nationale parken tekenen
- Archeologische sites tekenen vanaf zoom 12 in Outdoor-stijl

#### iOS

- NIEUW: OSM `description`-tag inhoud tonen (zoek `?description`) (Kiryl Kaveryn, Viktor Govako)
- NIEUW: vernieuwd routeplanscherm (Kiryl Kaveryn)

#### Android

- Nieuwe rotondepictogrammen in Android Auto (Andrei Shkrob)
- Categorie van geselecteerde markering tonen (Alexander Borsuk)
- Vertraging bij tonen afstand naar markering verholpen (Alexander Borsuk)
- Donker thema herzien (Andrei Shkrob)
- Positie-update probleem in navigatie op custom ROM's verholpen (bv. Lineage + MicroG) (Viktor Govako)
- Blauw potloodpictogram (bewerken) voor markeringen (Alexander Borsuk)
- Verticale hoogte plaatsinfo-voorbeeld verminderd (Alexander Borsuk)
- Azimut naar het noorden verwijderd uit voorbeeld (tik op blauwe pijl met afstand om te zien) (Alexander Borsuk)

Download de nieuwste versie: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Doe mee aan de bèta: [iOS][testflight] / [Android][firebase].

{{ references() }}
