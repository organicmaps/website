---
title: "Flerval för bokmärken och spår, en CarPlay-instrumentpanel, möjlighet att dölja spår på kartan samt läsbara delningslänkar i uppdateringen från augusti 2026"
date: 2026-08-31
slug: "flerval-bokmarken-spar-carplay-instrumentpanel-dolja-spar-delningslankar-augusti-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 02-bookmarks-tracks-multi-selection.jpg
---

Ladda ner Organic Maps-versionen från augusti 2026 på <https://get.omaps.org> eller via [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery] och [Obtainium][obtainium] ([Accrescent][accrescent] och [F-Droid][fdroid] kommer snart).

Varför uppdatera?
- Flerval i bokmärken och spår med möjlighet att radera, flytta och ändra färg på flera objekt samtidigt
- CarPlay-instrumentpanel
- Dölja enskilda spår på kartan
- Läsbara delningslänkar för platser, bokmärken och aktuell position – plus AirDrop på iOS och funktionen ”Share” på datorn
- Röstvägledning på armeniska och laotiska
- Wikipedia-artiklar på 19 språk
…samt många andra förbättringar, buggfixar och uppdaterade kartdata nedan.

Glöm inte heller att läsa versionsanteckningarna för [juni](@/news/2026-06-29/610/index.sv.md) och [juliuppdateringen](@/news/2026-07-23/620/index.sv.md).

## Fullständig ändringslogg

### Karta och platser

- Uppdaterade OpenStreetMap-data per den 26 augusti 2026 _(Viktor Govako)_
- Uppdaterade Wikipedia-artiklar på arabiska, bengali, kinesiska, engelska, franska, tyska, hindi, italienska, japanska, koreanska, marathi, polska, portugisiska, ryska, spanska, tamil, telugu, turkiska och urdu _(Alexander Borsuk)_
- Många problem som ledde till att öppettiderna visades felaktigt har åtgärdats _(Alexander Borsuk)_
- Stöd för fågelskådningsgömslen har lagts till _(Batmaclos, Viktor Govako)_
- Scener, kullar och naturliga bågar har lagts till på kartan, samt en ny ikon för klippor _(David Martinez)_
- Ikonerna för bergstoppar, grottor och bergspass har fått ny storlek _(David Martinez)_
- Skyddade områden, nationalparker och våtmarker visas nu i ljusare nyanser _(Alexander Borsuk)_
- Ett problem med att appen hängde sig och ett problem som ibland ledde till att tryckningar och gester ignorerades har åtgärdats _(Alexander Borsuk)_

### Dela, bokmärken och spår

- När du delar en plats, ett bokmärke eller din aktuella position skickas nu en läsbar länk med användbar information _(Alexander Borsuk)_
- Exporterade bokmärken behåller nu sina ursprungliga namn och beskrivningar _(Alexander Borsuk)_
- Delade bokmärkeslistor använder nu sina visade namn i stället för interna filnamn _(Alexander Borsuk)_
- Ett problem med visningen av höjddiagrammet som kunde uppstå direkt efter att en spårinspelning påbörjats har åtgärdats _(Kiryl Kaveryn)_

### Ruttplanering och navigering

- Om du trycker på en hållplats eller en markering på en rutt öppnas den nu korrekt, i stället för att du växlar mellan planerade rutter _(Viktor Govako)_
- Planeringen av rutter för kollektivtrafik går nu snabbare _(Viktor Govako)_
- Rättat felaktiga svänganvisningar _(Alexander Borsuk)_
- En felaktig startpunkt efter att en rutt hade beräknats om har åtgärdats _(Viktor Govako)_
- Vid ruttplanering betraktas lateritvägar numera som vägar med en oasfalterad vägbana av dålig kvalitet _(Julien Etienne)_
- Vägar med taggen `access=unknown` behandlas nu på samma sätt som vägar med privat tillträde eller tillträde endast för destinationstrafik _(Julien Etienne)_
- Röstvägledning på armeniska och laotiska har lagts till _(Alexander Borsuk)_

### OpenStreetMap-redigerare

- Om du rensar fältet för öppettider förblir knappen ”Spara” eller ”Klar” inte längre inaktiverad _(Alexander Borsuk)_
- Uppladdningar som delvis misslyckas görs nu om i stället för att rapporteras som helt lyckade _(Alexander Borsuk)_

### Översättningar

- [Vanliga frågor](https://organicmaps.app/sv/faq/) har uppdaterats, inklusive den japanska översättningen _(Alexander Borsuk)_
- Den japanska översättningen av ”Stängt just nu” har korrigerats _(Viktor Govako)_
- De kinesiska översättningarna av ”spår” och ”inaktivera” har förbättrats _(Chenxi Zhao)_

### iOS

- NYTT: Flerval har lagts till i listan över bokmärken och spår, med samlingsåtgärder för att radera, flytta och ändra färg på valda objekt, samt ”Markera alla” och ”Avmarkera alla” _(Kiryl Kaveryn)_
- NYTT: En CarPlay-instrumentpanel har lagts till _(Kiryl Kaveryn)_
- Stöd för AirDrop har lagts till för delning av platser _(Kiryl Kaveryn)_
- Flera CarPlay-problem har åtgärdats _(Kiryl Kaveryn, Alexander Borsuk)_
- Visningen av HTML-beskrivningar när ett bokmärke är valt på kartan har åtgärdats _(Kiryl Kaveryn)_
- Aktiveringen av kartstilen för bilnavigeringen har åtgärdats _(Kiryl Kaveryn, Alexander Borsuk)_
- Inställningarna har omorganiserats i avsnitten ”Allmänna inställningar”, ”Karta”, ”Navigering”, ”Nätverk” och ”Integritet” _(Kiryl Kaveryn)_
- Inställningen för kompasskalibrering har tagits bort, eftersom kalibreringen nu sker automatiskt _(Kiryl Kaveryn)_
- Den anpassade färgväljaren i popup-fönstret för färgpaletten har återställts _(Kiryl Kaveryn)_
- Motsvarande punkt visas nu på kartan när du drar fingret längs höjdprofilen i förhandsvisningen av en vandrings- eller cykelrutt _(Kiryl Kaveryn)_
- Problem med kompassen som kunde leda till att pilen för aktuell position pekade åt fel håll eller fastnade har åtgärdats _(Alexander Borsuk)_
- Ett problem som orsakade en krasch när en uppladdning till OpenStreetMap slutfördes i bakgrunden har åtgärdats _(Alexander Borsuk)_

### Android

- NYTT: Läget för flerval har lagts till i listan över bokmärken och spår. Du aktiverar det genom att trycka länge på ett objekt eller använda verktygsfältet. Därefter kan du ändra färg, flytta eller ta bort valfri kombination av bokmärken och spår _(Mikhail Listratsenka)_
- NYTT: Enskilda spår kan nu döljas på kartan med hjälp av ögonikonen i listan eller på skärmen med spårinformation _(cyber-toad)_
- Android Auto och Android Automotive: pilarna för U-svängsfältet har korrigerats _(Andrei Shkrob, Viktor Govako)_
- Android Auto och Android Automotive: problemet med växling mellan dag- och nattläge har åtgärdats _(Andrei Shkrob)_
- Android Auto och Android Automotive: söklistan förblir nu öppen medan du skriver _(Viktor Govako)_
- Listbeskrivningen visas nu när listan är sorterad _(Mikhail Listratsenka)_
- Designen på inställningsskärmen för bokmärkeslistan har uppdaterats _(Mikhail Listratsenka)_
- Sökpanelen fälls nu ihop när du har tryckt på en kategori _(Mikhail Listratsenka)_
- Tangentbordsfokus återgår nu till sökfältet efter att du har rensat det _(Mikhail Listratsenka)_
- Höjddiagrammet för rutten utnyttjar nu panelens hela bredd _(Mikhail Listratsenka)_
- Ett problem har åtgärdats som kunde leda till att zoomknapparna fastnade längst upp _(Mikhail Listratsenka)_
- Dialogfönstrens hörn är nu konsekvent rundade i alla Android-versioner _(Mikhail Listratsenka)_
- Ett kraschfel i menyn för export av spår har åtgärdats _(Mikhail Listratsenka)_
- Åtgärdat problem med att appen hänger sig _(Alexander Borsuk, Viktor Govako)_
- Ett problem med dubbla importer av KML- och KMZ-filer samt felmeddelandet ”Filen kunde inte öppnas” har åtgärdats _(Alexander Borsuk)_
- Sökkategorier på brasiliansk portugisiska, mexikansk spanska och brittisk engelska har korrigerats _(Alexander Borsuk)_
- Sökfunktionen fungerar nu korrekt på tangentbordsspråket när det skiljer sig från gränssnittsspråket _(Alexander Borsuk)_
- Ändringar i OpenStreetMap går inte längre förlorade när en uppladdning tar för lång tid eller misslyckas delvis _(Alexander Borsuk)_

### Desktop

- Funktionen ”Share” har lagts till på platssidan, med alternativen ”Copy Link”, ”Copy Text” och ”Email…” _(Alexander Borsuk)_
- Nedladdningsindikatorn ritas nu programmatiskt, vilket gör att den ser skarp ut på alla skärmar _(Kuzey Bilgin)_

## Så här kan du stödja Organic Maps

- [Donera](@/donate/index.sv.md) för att stödja utvecklingen och täcka kostnaderna för kartservrarna
- [Skicka dina synpunkter och bidra till projektet](@/contribute/index.sv.md)
- Delta i betatestningen för att testa nya funktioner i förväg och rapportera problem för [iOS][testflight], [Android][firebase] och [Desktop][flathub]
- Sprid budskapet!

Med kärlek och tacksamhet till alla våra användare och bidragsgivare,<br/>
Organic Maps-teamet

{{ <references lang /> }}
