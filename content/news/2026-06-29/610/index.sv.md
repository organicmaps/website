---
title: "Satellitbilder, kollektivtrafikrutter, alternativa rutter, nytt sök- och ruttplaneringsgränssnitt för Android, stöd för stora tillgänglighetstypsnitt i iOS och mer i juniuppdateringen 2026"
date: 2026-06-29
slug: "satellitbilder-kollektivtrafikrutter-alternativa-rutter-ny-sok-ruttplanering-android-stora-typsnitt-ios-juni-2026"
taxonomies:
  news: ["releases"]
---

I Organic Maps juniuppdatering finns många spännande nya funktioner och buggfixar att testa, bland annat:
- Satellitbilder
- Kollektivtrafikrutter
- Alternativa rutter
- Nytt sök- och ruttplaneringsgränssnitt för Android
- Stöd för stora tillgänglighetstypsnitt i iOS

Hämta den på <https://get.omaps.org> eller i [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] och [F-Droid][fdroid], och berätta vad du tycker!

## Detaljerad ändringslogg

- NYTT! Ruttplanering med kollektivtrafik: tunnelbana, snabbspårväg, buss och spårvagn _(Viktor Govako)_
- NYTT! Alternativa rutter: utöver den snabbaste rutten visar appen nu den kortaste rutten _(Viktor Govako)_
- NYTT! Varningar för gång- och cykelrutter om trappor, grindar och bommar längs vägen _(Viktor Govako)_
- NYTT! Välj valfri färg för bokmärken _(Alexander Borsuk, Mikhail Listratsenka)_
- NYTT! Stöd för koordinater i British National Grid (OS Grid), Irish Grid och Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTELLT: aktivera satellitbilder i Organic Maps-inställningarna med en egen URL till en rastertileserver. Vi arbetar fortfarande på vår egen server, så hitta gärna en öppet tillgänglig server med platshållarna `{x}`, `{y}`, `{z}` i URL:en _(Viktor Govako, renderexpert)_
- OpenStreetMap-data uppdaterade per den 24 juni _(Viktor Govako)_
- Wikipedia-data uppdaterade per den 20 juni, inklusive artiklar på italienska _(Alexander Borsuk)_
- Skriv `?map-download-server:https://your-server.com/` i sökfönstret för att åsidosätta Organic Maps servrar för kartnedladdning. Skriv `?no-map-download-server` för att ta bort åsidosättningen _(Alexander Borsuk)_

#### Kartrendering och stilar

- Snyggare mönster för strand, sand, rasbrant, kalt berg, fruktträdgård och vingårdar, plus skraffering för skyddade områden och våtmarker _(Alexander Borsuk)_
- Mjukare böjda textetiketter för vägar och floder _(Viktor Govako)_
- Floder, bäckar och våtmarker har högre kontrast och syns bättre i mörkt läge _(Alexander Borsuk)_
- Nya och förbättrade ikoner för kategorisökning och sökresultat på kartan _(Anton Makouski)_
- Förbättrad formning och rendering av flerspråkig text _(Alexander Borsuk)_
- Diverse buggfixar och prestandaförbättringar _(Viktor Govako)_

#### Spår, bokmärken och rutter

- GeoJSON-spår behåller nu höjd och tidsstämplar vid import och export _(Alexander Borsuk)_
- Krasch efter att ett spår flyttats till en annan lista har åtgärdats _(Viktor Govako)_
- Webbplatser visas nu för kulturarvsplatser _(Viktor Govako)_
- Operatörsnamn visas nu för namnlösa sökresultat. Till exempel visar en namnlös bankomat nu sin bank _(Anton Makouski)_
- Editor: korrigerad beskrivningstext för OpenStreetMap-redigeringar/changesets för flerbostadshus _(titanniya542-spec)_
- Förbättrad HTML-identifiering i beskrivningar av bokmärken och spår _(Alexander Borsuk)_

### iOS

- NYTT! Tillgänglighetsstöd för Dynamic Type och stora typsnitt _(Kiryl Kaveryn)_
- NYTT! Tryck för att välja mellan överlappande spår och rutter _(Kiryl Kaveryn)_
- Förbättrad HTML-rendering av beskrivningar för bokmärken och spår _(Kiryl Kaveryn)_
- Renare tabellstil i användargränssnittet _(Kiryl Kaveryn)_

### Android

- NYTT! Sökgränssnitt _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NYTT! Ruttplaneringsgränssnitt _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Förbättrad HTML-rendering av beskrivningar för bokmärken och spår _(Mikhail Listratsenka)_
- Minskad APK-storlek _(Alexander Borsuk)_
- Röstikonen visas som inaktiverad när ingen text-till-tal-motor finns tillgänglig _(Mikhail Listratsenka)_
- Långa beskrivningar av bokmärken och spår visar nu en ”…mer”-knapp _(Mikhail Listratsenka)_
- Diverse UI-fixar och en API-fix för returnerade punkt-ID:n _(Mikhail Listratsenka)_

### Desktop

- Stöd för att byta det visade koordinatsystemet _(Alexander Borsuk)_
- Information om den valda platsen visas nu till vänster _(Viktor Govako)_
- Kontextmenyns position har åtgärdats _(Osyotr)_
- Åtgärdat att OpenStreetMap-inloggning och redigeringar hängde sig på Qt-versioner 6.4 och äldre _(Alexander Borsuk)_
- Åtgärdat oväntat byte av kartstil under ruttplanering på macOS _(Alexander Borsuk)_
- Åtgärdat en krasch när macOS-appen stängdes efter export av en KMZ-fil _(Alexander Borsuk)_

### Översättningar

- Kantonesisk sväng-för-sväng-röstvägledning _(Alexander Borsuk)_
- Uppdaterade tyska och franska översättningar _(Wuzzy, Alexander Borsuk)_
- Felaktiga röstvägledningsöversättningar av ”onto street” för kinesiska, serbiska och katalanska har åtgärdats _(Alexander Borsuk)_

## Gå med i betatestningen för att prova tidiga funktioner och rapportera problem:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Vi är tacksamma mot alla våra användare och bidragsgivare, mot dem som [donerar](@/donate/index.sv.md) och ger Organic Maps 5 stjärnor i appbutiker. Tillsammans kan vi bygga den bästa kartappen!

Med kärlek,
Organic Maps-teamet

{{ references() }}
