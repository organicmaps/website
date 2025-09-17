---
title: "Release 15 september: ny ruttplanering och OSM-beskrivningar"
date: 2025-09-15T10:00:00+00:00
---

Den här andra septemberreleasen ger en omarbetad skärm för ruttplanering och möjligheten att visa innehåll i OpenStreetMap-taggen `description` på iOS. För att hitta platser med taggen, skriv `?description` i sökfältet (liknande `?wiki`).

Den innehåller också många fixar och förbättringar för iOS och Android (detaljer nedan).

Nya funktioner du kanske missat:
- Linjenummer för kollektivtrafik när du väljer en hållplats
- Vandrings- och cykelleder (aktivera via knappen Lager uppe till vänster)
- Visa markörnamn på kartan (aktivera i Inställningar)
- ✎-ikonen gör snabb redigering av markörer möjlig

Organic Maps är möjlig tack vare våra bidragsgivare, [dina donationer](@/donate/index.sv.md) och [ditt stöd](@/contribute/index.md).

### Detaljerade versionsnoteringar

- Nya OpenStreetMap-data per 13 september
- Mycket små öar borttagna från världskartan (Viktor Govako)
- Visa postnummer (ZIP) i adressdetaljer (Viktor Govako)
- Felaktig kartcentrering på aktuell position fixad (Kiryl Kaveryn, Viktor Govako)
- Behåll markörfärger vid export/import av GPX (cyber-toad)
- Uppdaterade översättningar (Weblate-bidragsgivare)

#### Kartstilar (Viktor Govako)

- Visa belysningsbutiker
- Visa kraftledningar från zoom 18
- Visa referensnamn för kraftstationer och ställverk
- Visa camping- och husvagnsplatser i navigationsläge
- Korrigera färg för sekundära vägar i navigationsläge
- Rita gränser för nationalparker
- Rita arkeologiska platser från zoom 12 i Outdoor-stil

#### iOS

- NYTT: Visa innehåll i OSM-taggen `description` (sök `?description`) (Kiryl Kaveryn, Viktor Govako)
- NYTT: Omarbetad skärm för ruttplanering (Kiryl Kaveryn)

#### Android

- Nya rondell-ikoner i Android Auto (Andrei Shkrob)
- Visa kategori för vald markör (Alexander Borsuk)
- Fördröjning vid visning av avstånd till markör fixad (Alexander Borsuk)
- Omstrukturerat mörkt tema (Andrei Shkrob)
- Positionsuppdateringsproblem i navigering på anpassade ROM:ar fixat (t.ex. Lineage + MicroG) (Viktor Govako)
- Blå penna (redigera)-ikon för markörer (Alexander Borsuk)
- Minskad vertikal höjd på platsinföregivning (Alexander Borsuk)
- Azimutvinkel mot norr borttagen från förhandsvisning (tryck blå pil) (Alexander Borsuk)

Hämta senaste versionen: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Gå med i betan: [iOS][testflight] / [Android][firebase].

{{ references() }}
