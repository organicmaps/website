---
title: "Felkorrigeringar och förbättringar av kollektivtrafik, ruttplanering, sökfunktion och bokmärken i uppdateringen från juli 2026"
date: 2026-07-23
slug: "buggfixar-forbattringar-kollektivtrafik-rutter-sokning-bokmarken-juli-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Som ni kanske redan har märkt har juli-uppdateringen av Organic Maps släppts. Ladda ner den på <https://get.omaps.org> eller från [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] och [F-Droid][fdroid].

Tack vare era [donationer](@/donate/index.sv.md) och [synpunkter](@/contribute/index.sv.md) kunde vi under juli månad fokusera på buggfixar och förbättringar. Om ni missade det finns även följande funktioner från den [tidigare juni-versionen](@/news/2026-06-29/610/index.sv.md) tillgängliga:
- Kollektivtrafikrutter (tidtabeller i realtid är under utveckling)
- Satellitbilder
- Alternativa rutter för bilkörning, vandring och cykling
- Nytt gränssnitt för sökning och ruttplanering på Android
- Stöd för stora tillgänglighetstypsnitt på iOS

## Detaljerad ändringslogg

### Karta och platser
- OpenStreetMap-data är uppdaterade per den 14 juli
- Anteckningar som skickas till [OpenStreetMap](https://www.openstreetmap.org) placeras nu exakt på den plats ni valt, istället för mitt på hela gatan eller området _(Alexander Borsuk)_
- Förbättrat platsval när man trycker på kartan i områden som sträcker sig över 180°-antimeridianen _(Viktor Govako)_
- Höjdprofilerna för spår visar inte längre föråldrade eller tomma diagram efter att ett spår har raderats _(Kiryl Kaveryn)_

### Kollektivtrafik
- Namnen på hållplatser, byten och stationer har nu en vit kontur för att vara läsbara både i ljusa och mörka teman _(Viktor Govako)_
- Tunnelbanelagret visas igen på rätt sätt när ni stänger förhandsvisningen av en kollektivtrafikrutt _(Mikhail Listratsenka)_

### Ruttplanering och navigering
- Vägvarningar (vägtullar, färjor, oasfalterade vägar, trappsteg och så vidare) visas nu för alla alternativa rutter _(Viktor Govako)_
- Ett sällsynt problem som orsakade att programmet hängde sig vid skapandet av en rutt har åtgärdats _(Viktor Govako)_
- Förbättrad hantering av återvändsgränder samt start- och målpunkter på vägar med trafikbegränsningar _(Viktor Govako)_
- Rättat felaktiga och saknade svänganvisningar _(Alexander Borsuk)_

### iOS
- Ny inställning ”Spara sökhistorik” som gör att ni kan stänga av historiken och dölja den om ni hellre inte vill spara den _(Kiryl Kaveryn)_
- Ny knapp ”Redigera” för att enklare ta bort bokmärken _(Kiryl Kaveryn)_
- Bokmärken sparas nu automatiskt när ni lämnar skärmen _(Kiryl Kaveryn)_
- Färgpaletten innehåller nu fördefinierade färger och ger er möjlighet att välja vilken anpassad färg som helst _(Kiryl Kaveryn)_
- Det tomma tillståndet för höjddiagrammet för ett inspelat spår har förbättrats _(Kiryl Kaveryn)_
- Visningen av framsteg längs rutten på Start-knappen har förbättrats _(Kiryl Kaveryn)_
- När man ändrar ordningen på hållplatserna hoppar listan inte längre hit och dit _(Kiryl Kaveryn)_
- Andra mindre förbättringar av gränssnittet _(Kiryl Kaveryn)_

### Android
- Öppettiderna visar nu delade arbetspass (till exempel lunchrast), börjar med dagens datum och visar hela veckan utan ett separat rullningsområde _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Ett överskådligare sökfält med en kombinerad rensnings- och röstknapp, en rensningsikon som inte längre flyttar sig samt layoutkorrigeringar för liggande läge och telefonrotation _(Mikhail Listratsenka)_
- Omarbetad bokmärkes- och spårredigerare _(Mikhail Listratsenka)_
- Korrigeringar och förbättringar av ruttplaneringen _(Mikhail Listratsenka)_
- Färgväljaren stängs nu automatiskt, och en programkrasch på Android 5 har åtgärdats _(Mikhail Listratsenka)_
- Krascher har åtgärdats _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- Listan över kartor som går att ladda ner är nu sorterad i alfabetisk ordning _(goncalo109560)_

### Översättningar
- Förbättrad kinesisk formulering _(Chenxi Zhao)_
- Uppdaterade ukrainska översättningar _(Nnifria)_
- Korrigeringar av de italienska översättningarna av kartregionernas namn _(Vittorio Bertola)_

## Delta i betatestningen för att prova tidiga funktioner och rapportera problem:

Tips: Betaversionen har ny skuggning av terrängen, förbättrade höjddata med stöd för både fot och meter samt andra häftiga funktioner!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Ha en trevlig sommar!
Organic Maps-teamet

{{ references() }}
