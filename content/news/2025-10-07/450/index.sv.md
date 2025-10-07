---
title: "Oktober-release: Hastighetsbegränsningar i Android Auto, GeoJSON-import, statistik för inspelningsspår, visning av OSM-beskrivningstagg, spara bokmärke på valt spår på iOS och mer"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
---

Denna oktober-uppdatering av Organic Maps lägger till visning av hastighetsbegränsningar i Android Auto, GeoJSON-import, statistik för inspelningsspår, visar OSM-beskrivningstaggar (skriv `?description` i sökrutan för att se dem) och sparar ett bokmärke på ett spår på iOS. Det finns också många förbättringar av användargränssnittet, OpenStreetMap-redigering och olika buggfixar på alla plattformar, inklusive kraschfixen vid start på vissa Android-enheter.

Organic Maps är möjlig tack vare ❤️ våra bidragsgivare, [dina donationer](@/donate/index.sv.md) och [ditt stöd](@/contribute/index.sv.md).

### Detaljerade versionsnoteringar (inklusive ändringar från föregående mindre uppdatering)

- NYTT! Importera GeoJSON (Sergiy Kozyr)
- OpenStreetMap-data per 4 oktober
- Wikipedia-data per 1 oktober
- Stöd för Seattle light rail för kollektivtrafik (tjasz)
- Avaktivera inte kartvalet när en redigerad OSM-plats sparas (Kiryl Kaveryn)
- Uppdaterade översättningar (Weblate-bidragsgivare)

#### Kartstilar

- Visa cykeluthyrningsbutiker taggade som amenity=bicycle + rental=shop (David Martinez)
- Visa historiska arkeologiska platser från zoom 12 och andra historiska platser från zoom 15 i Outdoor-stil (Viktor Govako)
- Nya ikoner för master, kommunikations- och krafttorn i Outdoor-stil (David Martinez)
- Öka toppikonstorlek i Outdoor-stil (David Martinez)
- Lägg till saknade POI-ikonvarianter (David Martinez)
- Fler barriärtyper tillagda (Viktor Govako)

#### iOS

- NYTT: Spara bokmärke på vald spårpunkt (Kiryl Kaveryn)
- NYTT: Ta bort inspelningsspåret utan att spara det först (Kiryl Kaveryn)
- Visa bokmärkeslisttitlar med flera rader på Platssidan (David Martinez)
- Uppdatera OSM-inloggningsknappstil (Kiryl Kaveryn)
- Åtgärda uppdateringsproblem för navigeringsinformation (Kiryl Kaveryn)
- Åtgärda problem med ny ruttplanering (Kiryl Kaveryn)
- Åtgärda synlighet för att lägga till/redigera OSM-plats för kartor äldre än 3 månader (Kiryl Kaveryn)
- Åtgärda layout för transportalternativ segmentkontroll för iOS 26 (Kiryl Kaveryn)
- Förenkla bokmärkesvalsanimationer (Kiryl Kaveryn)
- Åtgärda problem med sökresulatval (Kiryl Kaveryn)
- Åtgärdad stil, svepning och animationer för Platsinformationssidan (Kiryl Kaveryn)

#### Android Auto (endast Google Play)

- NYTT: Hastighetsbegränsningsvisning i Android Auto (Andrei Shkrob)
- Åtgärda displaybyte i Android Auto-navigeringsläge (Andrei Shkrob)
- Åtgärda ruttpilsförskjutning i Android Auto (Andrei Shkrob)
- Åtgärda problem när en enhet ansluts/kopplas från en bil (Andrei Shkrob)
- Lägg till Android Auto-platstjänst (Andrei Shkrob)
- Förbättra Android Auto-ruttsimulator (Viktor Govako)

#### Android

- NYTT: Visa statistik för inspelningsspår i realtid (Kavi Khalique)
- NYTT: Visa OSM `description`-tagginnehåll (Alexander Borsuk)
- Åtgärda temaändrinkshantering (Andrei Shkrob)
- Åtgärdat flera krascher, inklusive den vid start (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Tysta nedladdningsförloppsaviseringar (Viktor Govako)
- Minska pennikon-utfyllnad (Alexander Borsuk)

#### Desktop

- Åtgärda hängande curl på Linux (Alexander Borsuk)
- Åtgärda hängning på macOS vid inloggning till OSM (Alexander Borsuk)
- Åtgärd för att välja funktion från kontextmeny (Viktor Govako)
- Alternativ för att avbryta nedladdning (Viktor Govako)
- Visa geometrityp i kontextmeny (Viktor Govako)

### Nyligen släppta funktioner som du kanske missat

- Linjenummer för kollektivtrafik när du väljer en busshållplats
- Vandrings- och cykelleder (aktivera via knappen Lager uppe till vänster)
- Se bokmärkesnamn på kartan genom att aktivera det i appinställningarna
- Pennikonen ✎ erbjuder ett snabbt sätt att redigera bokmärken

### Installera Organic Maps

Hämta den senaste versionen av Organic Maps från [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] och [F-Droid][fdroid].

Gå med i betatestning för tidiga funktioner: [iOS][testflight] / [Android][firebase].

{{ references() }}
