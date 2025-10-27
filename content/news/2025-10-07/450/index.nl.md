---
title: "Release oktober: Snelheidslimiet in Android Auto, GeoJSON-import, statistieken van opname tracks, weergave OSM beschrijvingstag, markering opslaan op geselecteerde track op iOS en meer"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

Deze oktober-update van Organic Maps voegt snelheidslimietweergave in Android Auto toe, GeoJSON-import, statistieken van opname tracks, toont OSM beschrijvingstags (typ `?description` in het zoekvak om ze te zien), en slaat een markering op een track op iOS op. Er zijn ook veel verbeteringen aan de gebruikersinterface, OpenStreetMap-bewerking en verschillende bugfixes op alle platforms, inclusief de crashfix bij opstarten op sommige Android-apparaten.

Organic Maps is mogelijk dankzij ❤️ onze bijdragers, [jouw donaties](@/donate/index.nl.md) en [jouw steun](@/contribute/index.nl.md).

### Gedetailleerde release-opmerkingen (inclusief wijzigingen van de vorige kleine update)

- NIEUW! Importeer GeoJSON (Sergiy Kozyr)
- OpenStreetMap-gegevens per 4 oktober
- Wikipedia-gegevens per 1 oktober
- Ondersteuning Seattle light rail voor openbaar vervoer (tjasz)
- Kaartselectie niet deactiveren bij opslaan van een bewerkte OSM-locatie (Kiryl Kaveryn)
- Bijgewerkte vertalingen (Weblate-bijdragers)

#### Kaartstijlen

- Fietsverhuurwinkels tonen die zijn getagd als amenity=bicycle + rental=shop (David Martinez)
- Historische archeologische sites tonen vanaf zoom 12 en andere historische sites vanaf zoom 15 in Outdoor-stijl (Viktor Govako)
- Nieuwe pictogrammen voor masten, communicatie- en stroomtorens in Outdoor-stijl (David Martinez)
- Pictogramgrootte van bergtoppen vergroten in Outdoor-stijl (David Martinez)
- Ontbrekende POI-pictogramvarianten toevoegen (David Martinez)
- Meer barriëretypes toegevoegd (Viktor Govako)

#### iOS

- NIEUW: Markering opslaan op geselecteerd trackpunt (Kiryl Kaveryn)
- NIEUW: Opnametrack verwijderen zonder deze eerst op te slaan (Kiryl Kaveryn)
- Markeringslijsttitels met meerdere regels tonen op Locatiepagina (David Martinez)
- OSM-aanmeldknoppenstijl bijwerken (Kiryl Kaveryn)
- Probleem met bijwerken navigatie-informatie oplossen (Kiryl Kaveryn)
- Problemen met nieuwe routeplanning oplossen (Kiryl Kaveryn)
- Zichtbaarheid van OSM-locatie toevoegen/bewerken voor kaarten ouder dan 3 maanden oplossen (Kiryl Kaveryn)
- Lay-out transportopties segmentbesturing voor iOS 26 oplossen (Kiryl Kaveryn)
- Markeringsselectie-animaties vereenvoudigen (Kiryl Kaveryn)
- Probleem met selectie zoekresultaat oplossen (Kiryl Kaveryn)
- Opgeloste stijl, veegbeweging en animaties voor Locatie-informatiepagina (Kiryl Kaveryn)

#### Android Auto (alleen Google Play)

- NIEUW: Snelheidslimietweergave in Android Auto (Andrei Shkrob)
- Displaywissel in Android Auto-navigatiemodus oplossen (Andrei Shkrob)
- Routepijl-offset in Android Auto oplossen (Andrei Shkrob)
- Probleem oplossen wanneer een apparaat wordt aangesloten/losgekoppeld op een auto (Andrei Shkrob)
- Android Auto-locatieservice toevoegen (Andrei Shkrob)
- Android Auto-routesimulator verbeteren (Viktor Govako)

#### Android

- NIEUW: Bekijk opname track-statistieken in realtime (Kavi Khalique)
- NIEUW: Toon OSM `description`-taginhoud (Alexander Borsuk)
- Themawijzigingsafhandeling oplossen (Andrei Shkrob)
- Verschillende crashes opgelost, inclusief de crash bij opstarten (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Stille downloadvoortgangsmeldingen (Viktor Govako)
- Potloodpictogram-opvulling verminderen (Alexander Borsuk)

#### Desktop

- Hangende curl op Linux oplossen (Alexander Borsuk)
- Vastlopen op macOS bij inloggen op OSM oplossen (Alexander Borsuk)
- Actie om functie te selecteren uit contextmenu (Viktor Govako)
- Optie om download te annuleren (Viktor Govako)
- Geometrietype tonen in contextmenu (Viktor Govako)

### Recent uitgebrachte functies die je mogelijk gemist hebt

- Lijnnummers van openbaar vervoer bij selectie van een bushalte
- Wandel- en fietsroutes (schakel ze in via de knop Lagen linksboven)
- Zie markeringsnamen op de kaart door het in de app-instellingen te activeren
- Het ✎ potloodpictogram biedt een snelle manier om markeringen te bewerken

### Installeer Organic Maps

Download de nieuwste versie van Organic Maps van de [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] en [F-Droid][fdroid].

Doe mee met bètatesten voor vroege functies: [iOS][testflight] / [Android][firebase].

{{ references() }}
