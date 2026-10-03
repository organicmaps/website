---
title: "Ruttoptimering, förbättrade alternativa rutter, möjlighet att dölja enskilda spår och områden med sporadiska vattenförekomster i uppdateringen från september 2026"
date: 2026-09-29
slug: "flerval-bokmarken-spar-carplay-instrumentpanel-dolja-spar-delningslankar-augusti-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Redo att ge dig av? Septemberuppdateringen innehåller förbättrade alternativa rutter, en inställning för att optimera ordningen på ruttens stopp, tydligare markeringar för områden där vatten förekommer periodvis och en ögonikon för att dölja enskilda spår, tillsammans med många andra korrigeringar och förbättringar (se nedan).

Installera eller uppdatera Organic Maps via <https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] eller [F-Droid][fdroid].

Om du har missat våra tidigare uppdateringar kan du ta en titt på de funktioner som lanserades i [juni](@/news/2026-06-29/610/index.sv.md), [juli](@/news/2026-07-23/620/index.sv.md) och [augusti](@/news/2026-08-31/630/index.sv.md). Ett stort tack till våra bidragsgivare och användare som har gjort dessa uppdateringar möjliga!

## Så här kan du stödja Organic Maps

- [Donera](@/donate/index.sv.md) för att stödja utvecklingen och täcka kostnaderna för kartvärdtjänsten
- [Skicka dina synpunkter och bidra](@/contribute/index.sv.md) till projektet
- Delta i betatestningen för att testa nya funktioner i förväg och rapportera problem på [iOS][testflight], [Android][firebase] och [datorn][flathub]
- Sprid budskapet och hjälp oss att skapa ett bättre alternativ till de stora tech-företagens kartor!

## Versionsinformation

### Karta

- Data från OpenStreetMap per den 28 september 2026
- Uppgifter från Wikipedia per den 21 september 2026
- Åtgärdat problemet med sökningar när det synliga kartområdet passerar 180°-meridianen (±180° longitud) _(Viktor Govako)_
- Områden med tillfälliga vattenförekomster visas nu med ett prickmönster, liknande det som används för sand _(Alexander Borsuk)_
- Vattenreservoarerna syns nu när man zoomar ut ytterligare _(Alexander Borsuk)_
- Vattentunnlar visas inte längre på kartan _(Alexander Borsuk)_
- Ikonerna för tunnelbanestationer och ingångar i Suzhou har korrigerats _(Alexander Borsuk)_
- Man har åtgärdat några sällsynta fall där etiketterna hamnade fel på metrokartlagret _(Viktor Govako)_

### Ruttplanering och navigering

- Förbättrade alternativa rutter och deras beräknade ankomsttider _(Alexander Borsuk, Viktor Govako)_
- Den valda alternativa rutten bevaras nu när navigeringen räknar om rutten _(Alexander Borsuk)_
- Ordningen på ruttens stopp återställs nu efter att appen har startats om _(Kiryl Kaveryn)_

### Övriga förbättringar

- Öppettiderna visar nu ”Middagstid” för 12:00 och ”Midnatt” för 00:00 eller 24:00 _(Alexander Borsuk)_
- Buggar har åtgärdats och spårinspelningen har förbättrats _(Alexander Borsuk)_
- Import av KMB-filer har åtgärdats _(Alexander Borsuk)_
- Korrigerade översättningar till franska och asturiska _(Alexander Borsuk)_
- Rättat ett stavfel i den engelska versionen _(Carl Morris)_

### iOS

- Lagt till en ögonikon för att dölja enskilda spår _(Kiryl Kaveryn)_
- Lagt till knappar för att lägga till eller byta ut ett stopp i en planerad rutt _(Kiryl Kaveryn)_
- En inställning har lagts till för att optimera ordningen på ruttens mellanliggande stopp _(Kiryl Kaveryn)_
- Manöverinstruktioner har lagts till för kompatibla head-up-displayer (HUD) i bilar samt i CarPlay-instrumentpanelen _(Kiryl Kaveryn)_
- CarPlay-knapparna och sökfunktionen har åtgärdats _(Alexander Borsuk)_
- Olika buggar har åtgärdats och användargränssnittet har förbättrats _(Kiryl Kaveryn, Alexander Borsuk)_
- Stöd har lagts till för att välja en installerad navigationsröst och förhandslyssna på den _(Kiryl Kaveryn, Alexander Borsuk)_
- Kategorisökningen i Spotlight har återställts _(Kiryl Kaveryn)_

### Android

- En inställning har lagts till för att optimera ordningen på ruttens mellanliggande stopp _(Mikhail Listratsenka)_
- Lagt till knappar för att lägga till eller byta ut ett stopp i en planerad rutt _(Mikhail Listratsenka)_
- Nu går det att stoppa spårinspelningen och spara spåret direkt från aviseringen _(Alexander Borsuk)_
- Knappen ”Lägg till stopp” lägger nu till ett stopp efter de befintliga stoppen, före destinationen _(Mikhail Listratsenka)_
- Förbättrade uppladdningar från OpenStreetMap-redigeraren _(Owm)_
- Uppdaterad design av användargränssnittet _(Mikhail Listratsenka)_
- Bokmärkesredigeraren och andra dialogrutor förblir nu öppna under navigering _(Mikhail Listratsenka)_
- Renderingen av höjddiagrammet för plana spår och i gränssnitt med layout från höger till vänster har åtgärdats _(Mikhail Listratsenka)_
- Åtgärdat problemet med att kartknapparna skärs av av systemfältet _(Mikhail Listratsenka)_
- Buggar har åtgärdats och stödet för Android Auto har förbättrats _(Andrei Shkrob)_
- En krasch vid kartrendering har åtgärdats _(Viktor Govako)_

### Dator

- Har bytt namn på den körbara filen för skrivbordet och app-paketet för macOS till `OrganicMaps` _(Alexander Borsuk)_
- Problem i Windows-appen har åtgärdats _(Osyotr, Alexander Borsuk)_
- Kommandoradsargumentet `--lang` åsidosätter nu appens språkinställning _(Alexander Borsuk)_

Med glädje och passion,

Ditt Organic Maps-team

{{ <references lang /> }}
