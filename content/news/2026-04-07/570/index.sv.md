---
title: "Vandrings- och cykelleder med höjdprofiler, smartare adressökning i USA, sömlös kartfortsättning vid antimeridianen och mycket mer i Organic Maps uppdatering för april"
date: 2026-04-07
slug: "vandrings-cykelleder-hojdkurvor-us-adressokning-antimeridian-kartomslagning-april-2026-organic-maps-uppdatering"
taxonomies:
  news: ["Releases"]
---

Den här aprilversionen innehåller, utöver många buggfixar och förbättringar, tre enkla sanningar: vandrare vill veta hur många höjdmeter som väntar, alla vill att adressökningen bara ska fungera, och ingen ska känna att de faller av kartans kant. Tack vare våra bidragsgivare, era fina recensioner, [donationer](@/donate/index.sv.md) och [stöd](@/contribute/index.sv.md) har vi löst alla tre — och mycket mer därtill.

Oavsett om våren lockar dig ut på nya stigar eller om hösten på södra halvklotet manar till en sista lång tur, hoppas vi att den här uppdateringen gör din nästa resa lite enklare och mycket vackrare.

Hämta apriluppdateringen på <https://get.omaps.org> eller på [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] och [F-Droid][fdroid].

## Höjdpunkter

- **Tryck på en led och se stigningen.** Vandrings- och cykelleder går nu att välja direkt på kartan. Tryck på en led för att markera den och se dess höjdprofil direkt.
- **Två miljoner fler amerikanska adresser och smartare sökning.** Fler adresser, hämtade från TIGER Census-datasetet, finns nu i appen. Tillsammans med smartare matchning av husnummer förbättrar det sökresultaten överallt. Glöm inte att det alltid är bästa sättet att förbättra sökningen att lägga till saknade adresser i [OpenStreetMap](https://www.openstreetmap.org).
- **En karta utan kanter.** Organic Maps fortsätter nu sömlöst över antimeridianen (±180° longitud). Dra och rotera mellan Tjuktjien och Alaska, eller Nya Zeeland och Fiji, utan osynliga väggar och klumpiga återställningar — Stilla havet känns äntligen runt.
- **Måla om en hel kategori på en gång.** Ändra färg på alla bokmärken och/eller spår i en kategori med ett tryck — en liten detalj som gör förra sommarens röriga researkiv till något du faktiskt vill öppna.

## Releaseinformation

### Alla plattformar

- NYHET! Bättre sökning i USA med ytterligare två miljoner adresser hämtade från TIGER Census-data (Viktor Govako)
- NYHET! Förbättrad flerfärgsrendering för vandrings- och cykelleder; tryck på en led för att välja den och se dess höjdprofil (Viktor Govako)
- OpenStreetMap-data uppdaterade den 4 april
- Wikipedia-data uppdaterade den 1 april
- Justerad beräkning av stigning och nedförsbacke i spårgrafer för att bättre matcha värden som visas i andra appar (Viktor Govako)
- Du kan nu lägga till en ny plats i OpenStreetMap efter att ha valt din nuvarande position på kartan (Mikhail Listratsenka)
- Lade till ikoner för food courts och stadsportar (David Martinez)
- Lagt till underkategorier för klädbutiker: kvinnor, män, barn, bröllop, sport och underkläder, plus kontorstyper (Viktor Govako)
- Uppdaterade sökkategorier: lade till "Bread" för bagerier, "Shawarma" som kök och andra synonymförbättringar (Viktor Govako)
- Kartan fortsätter nu korrekt över antimeridianen (±180° longitud) när du drar och roterar den (Alexander Borsuk, Viktor Govako)
- Cykelnavigering använder nu kompassriktning vid låga hastigheter (HossamSaberr)
- Förbättrad adressökning med husnummer (Viktor Govako)
- Åtgärdat ett systemfel vid planering av rutter nära vissa regionala gränser (Viktor Govako)
- Korrigerade sökresultat när stads- och delstatsnamn är desamma (Viktor Govako)
- Lagt till synonymer för amerikanska gator: highway, hwy, freeway och fwy (Viktor Govako)
- Åtgärdade felplacerat hårkors i redigeraren när du trycker på "Lägg till plats" (José Araújo)
- Fixad visning av öppettider för platser med förskjuten soluppgång/solnedgång (Alexander Borsuk)
- Fixade att GPS-spårinspelning tappade punkter mellan segment (Alexander Borsuk)
- Korrigerad hantering av sommartid för tidszoner (Andrei Shkrob)
- Färgerna på Sydneys tunnelbanelinjer korrigerade (Alexander Borsuk)
- Fixad GeoJSON-import (Alexander Borsuk)
- Förbättrad stabilitet och prestanda (Alexander Borsuk, Viktor Govako)
- Uppdaterade översättningar (Alexander Borsuk, Viktor Govako, Weblate-bidragsgivare)

### iOS

**Observera för dig med en äldre iPhone eller iPad:** på grund av de senaste ändringarna i TestFlight och App Store stöder den här versionen bara iOS 15 och senare. iOS 12, 13 och 14 stöds inte längre. Redan installerade versioner av Organic Maps fortsätter att fungera på äldre enheter, men nya kartor, funktioner och rättningar kommer nu bara till iOS 15 och senare.

- NYHET! Ändra alla bokmärkes- och spårfärger i en kategori på en gång (Kiryl Kaveryn)
- Förbättrad visning av HTML-innehåll med tabeller och bilder i bokmärkesdetaljer (Alexander Borsuk, Kiryl Kaveryn)
- Lade till vertikala avdelare för spår med flera segment i höjdprofilen (Kiryl Kaveryn)
- Fixat punktval i höjdprofilen för interpolerade punkter (Kiryl Kaveryn)
- Förbättrade gester i modala vyer: snäpper till närmaste steg, stängs vid kantdragning och återställer föregående läge när de öppnas igen (Kiryl Kaveryn)
- Du kan nu starta en giltig rutt även när du uppmanas att ladda ner ytterligare kartor (Kiryl Kaveryn)
- Ökade tryckytan för knapparna i navigeringsfältet "Lägg till plats" (Noahdyn)
- Fixade en krasch vid export av spår (Alexander Borsuk, Kiryl Kaveryn)
- Fixad sökning i listor över bokmärken och spår när du öppnar den från platsdetaljer (Kiryl Kaveryn)

### Android

- NYHET! Ändra alla bokmärkes- och spårfärger i en kategori på en gång (Mikhail Listratsenka)
- NYHET! Schemalagt utseende i Inställningar för automatisk växling mellan ljust och mörkt tema baserat på soluppgång och solnedgång (Dzmitry Strekha)
- Lagt till historik för nyligen använda kategorier i kartredigeraren (Mikhail Listratsenka)
- Lade till en spårvagnsikon för spårvagnshållplatser som valts på kartan (Mikhail Listratsenka)
- Döljer nedladdningsknappen när alla kartor redan har laddats ner (Mikhail Listratsenka)
- Fixat uppladdning av kartredigeringar till OpenStreetMap (Viktor Govako)
- Fixat fildelning till Google Drive och andra appar (Alexander Borsuk)
- Fixade återimport av bokmärken när appen öppnas igen från de senaste apparna (Alexander Borsuk)
- Att öppna OpenStreetMap-sök-URL:er som `openstreetmap.org/search?query=Pizza` startar nu sökningen i Organic Maps (Rawdyrathaur)
- Flera krascher åtgärdade (Alexander Borsuk)

### Skrivbord (Linux och Mac OS)

- Lade till möjligheten att välja ett guidespår för routning (Viktor Govako)
- Fixade sparande eller export av bokmärken/spår som skapade trasiga filer i vissa språkinställningar på grund av lokalanpassade decimaltecken (Alexander Borsuk)


Gå med i betatestning för att prova tidiga funktioner och rapportera problem:
- [iOS][testflight]
- [Android][firebase]

Med kärlek och omtanke ❤️
Organic Maps-teamet

{{ references() }}
