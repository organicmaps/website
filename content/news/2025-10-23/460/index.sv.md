---
title: "23 oktober-utgåvan: Organic Maps som standardnavigeringsapp i EU på iOS, vägskyltar visas på Android och fler förbättringar och fixar"
date: 2025-10-23T17:20:21+00:00
slug: "23-oktober-utgåvan-organic-maps-standardnavigeringsapp-eu-ios-vägskyltar-android-förbättringar-fixar"
taxonomies:
  news: ["Releases"]
---

I 23 oktober-utgåvan fokuserade vi på fixar och förbättringar. Kolla den detaljerade listan nedan.

För dem som missade, den [tidigare uppdateringen den 7 oktober](https://organicmaps.app/news/2025-10-07/android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display/
) lade till GeoJSON-import, inspelningsstatistik för spår, hastighetsgränser i Android Auto, visning av OSM-beskrivningstaggar (skriv `?description` i sökrutan för att se dem), spara ett bokmärke på ett spår på iOS och många andra förbättringar.

## Alla plattformar

- Färsk OpenStreetMap-data från 21 oktober 2025 (Viktor Govako)
- Visa namn på tunnelbaneingångar/-utgångar på kartan (Viktor Govako)
- Nya POI-typer och ikoner: övervakningsstationer, trafiköar, Kneipp-vattenkuranläggningar, miniatyrjärnvägar (Viktor Govako), campingplatser i utomhusstil, flygplatsterminaler, inomhuslekplatser, telekommunikationsbutiker, båtuthyrningsanläggningar, slipanläggningar, uppdaterade avfallshantering och deponiikoner (David Martinez)
- Slovenska appgränssnittsöversättningar (Alexander Borsuk) och TTS-röstvägledning för navigering (Erik Bucik)
- På vissa enheter/skärmar är kartan i stadskärnor nu mindre rörig (Viktor Govako)
- Fixade kartrotationer på dåliga kompasssensorer när man går i fotgängarnavigeringsläge (Viktor Govako)
- Förbättrad information som visas efter val av flod eller vattenvägsegment (Viktor Govako)
- Bättre sökning efter elbilsladdningsstationer med förbättrade synonymer på alla språk (Alexander Borsuk)
- Fixad emoji-sökning med variantväljare (Alexander Borsuk)
- Fixat för många sökresultat som visas för vissa fullständiga adressmatchningsfrågor (Viktor Govako)
- Import av GeoJSON från https://umap.openstreetmap.fr/ bör nu bevara all metadata (Shubh Kesharwani)
- Ytterligare färger stöds för markerade stigar för kartlagret Vandringsleder (Viktor Govako)

## iOS

- EU-användare kan ställa in Organic Maps som standardnavigeringsapp i iOS-inställningar → Appar → Standardappar → Navigering (Kiryl Kaveryn)
- Fixad vit-på-vit statusfält i navigeringsläge (Kiryl Kaveryn)
- Ökad knappstorlek för Starta navigering (Kiryl Kaveryn)
- Borttaget tomt utrymme vid ruttpanering på iPad (Kiryl Kaveryn)
- Organic Maps kan be dig betygsätta den i App Store. Dina bra recensioner motiverar vårt team!

## Android

- Vägskyltar visas nu i navigeringsinstruktioner (Andrei Shkrob)
- Förbättringar av inspelningsinformation för spår (Kavi Khalique)
- Organic Maps fungerar på vissa äldre Intel x86-enheter (Andrei Shkrob)
- Fixade TTS-röstinstruktioner som inte fungerade i vissa fall (Andrei Shkrob)
- Bättre startskärm vid uppstart (Andrei Shkrob)

### Android Auto
- Återställ rutten efter avbokning (Andrei Shkrob)
- Fixade krascher på vissa enheter (Andrei Shkrob)

## Linux/Mac OS

- POI-detaljer visar nu formatet "namn | ref" (Viktor Govako)
- mörkt läge synkroniseras automatiskt med systeminställningar (DeepChirp)

## Fotnoter

Organic Maps är möjligt tack vare ❤️ våra bidragsgivare, [dina donationer](@/donate/index.sv.md) och [ditt stöd](@/contribute/index.sv.md).

Hämta den senaste versionen av Organic Maps från [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] och [F-Droid][fdroid].

P.S. Delta i betatestning för tidiga funktioner:
- [iOS][testflight]
- [Android][firebase].

Med kärlek till våra användare och community
Organic Maps-teamet

{{ references() }}
