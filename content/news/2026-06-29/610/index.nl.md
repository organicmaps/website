---
title: "Satellietbeelden, ov-routes, alternatieve routes, nieuwe zoek- en routeplanningsinterface voor Android, ondersteuning voor grote toegankelijkheidslettertypen op iOS en meer in de update van juni 2026"
date: 2026-06-29
slug: "satellietbeelden-ov-routes-alternatieve-routes-nieuwe-zoek-routeplanning-android-grote-lettertypen-ios-juni-2026"
taxonomies:
  news: ["releases"]
---

In de juni-update van Organic Maps zijn er veel spannende nieuwe functies en bugfixes om uit te proberen, waaronder:
- Satellietbeelden
- Ov-routes
- Alternatieve routes
- Nieuwe zoek- en routeplanningsinterface voor Android
- Ondersteuning voor grote toegankelijkheidslettertypen op iOS

Download hem via <https://get.omaps.org> of in de [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] en [F-Droid][fdroid], en laat ons weten wat je ervan vindt!

## Gedetailleerd wijzigingslogboek

- NIEUW! Routeplanning met openbaar vervoer per metro, lightrail, bus en tram _(Viktor Govako)_
- NIEUW! Alternatieve routes: naast de snelste route toont de app nu ook de kortste route _(Viktor Govako)_
- NIEUW! Waarschuwingen op wandel- en fietsroutes voor trappen, poorten en slagbomen onderweg _(Viktor Govako)_
- NIEUW! Kies elke gewenste kleur voor bladwijzers _(Alexander Borsuk, Mikhail Listratsenka)_
- NIEUW! Ondersteuning voor coördinaten van British National Grid (OS Grid), Irish Grid en Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTEEL: schakel satellietbeelden in de instellingen van Organic Maps in met een aangepaste URL van een rastertegelserver. We werken nog aan onze eigen server, dus zoek voorlopig een openbaar beschikbare server met `{x}`, `{y}`, `{z}`-plaatsaanduidingen in de URL _(Viktor Govako, renderexpert)_
- OpenStreetMap-gegevens bijgewerkt per 24 juni _(Viktor Govako)_
- Wikipedia-gegevens bijgewerkt per 20 juni, inclusief artikelen in het Italiaans _(Alexander Borsuk)_
- Typ `?map-download-server:https://your-server.com/` in het zoekvenster om de kaartdownloadservers van Organic Maps te overschrijven. Typ `?no-map-download-server` om de overschrijving te verwijderen _(Alexander Borsuk)_

#### Kaartweergave en stijlen

- Mooiere patronen voor strand-, zand-, puinhelling-, kale rots-, boomgaard- en wijngaardgebieden, plus arcering voor beschermde gebieden en wetlands _(Alexander Borsuk)_
- Vloeiendere gebogen tekstlabels voor wegen en rivieren _(Viktor Govako)_
- Rivieren, beken en wetlands hebben meer contrast en zijn beter zichtbaar in de donkere modus _(Alexander Borsuk)_
- Nieuwe en verbeterde pictogrammen voor categoriezoekopdrachten en zoekresultaten op de kaart _(Anton Makouski)_
- Verbeterde vormgeving en weergave van meertalige tekst _(Alexander Borsuk)_
- Diverse bugfixes en prestatieverbeteringen _(Viktor Govako)_

#### Tracks, bladwijzers en routes

- GeoJSON-tracks behouden nu hoogte en tijdstempels bij import en export _(Alexander Borsuk)_
- Crash opgelost na het verplaatsen van een track naar een andere lijst _(Viktor Govako)_
- Websites worden nu getoond voor erfgoedlocaties _(Viktor Govako)_
- Operatornamen worden nu getoond voor naamloze zoekresultaten. Een naamloze geldautomaat toont bijvoorbeeld nu de bank _(Anton Makouski)_
- Editor: beschrijvingstekst voor OpenStreetMap-bewerkingen/changesets van appartementencomplexen gecorrigeerd _(titanniya542-spec)_
- Verbeterde HTML-detectie in beschrijvingen van bladwijzers en tracks _(Alexander Borsuk)_

### iOS

- NIEUW! Toegankelijkheidsondersteuning voor Dynamic Type en grote lettertypen _(Kiryl Kaveryn)_
- NIEUW! Tik om te kiezen tussen overlappende tracks en routes _(Kiryl Kaveryn)_
- Verbeterde HTML-weergave van beschrijvingen van bladwijzers en tracks _(Kiryl Kaveryn)_
- Nettere tabelstijl in de gebruikersinterface _(Kiryl Kaveryn)_

### Android

- NIEUW! Zoekinterface _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NIEUW! Routeplanningsinterface _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Verbeterde HTML-weergave van beschrijvingen van bladwijzers en tracks _(Mikhail Listratsenka)_
- APK-grootte verkleind _(Alexander Borsuk)_
- Het spraakpictogram wordt uitgeschakeld weergegeven wanneer er geen tekst-naar-spraak-engine beschikbaar is _(Mikhail Listratsenka)_
- Lange beschrijvingen van bladwijzers en tracks tonen nu een knop “…meer” _(Mikhail Listratsenka)_
- Diverse UI-fixes en een API-fix voor geretourneerde punt-ID’s _(Mikhail Listratsenka)_

### Desktop

- Ondersteuning voor het wisselen van het weergegeven coördinatensysteem _(Alexander Borsuk)_
- Informatie over de geselecteerde plaats wordt nu links weergegeven _(Viktor Govako)_
- Positie van het contextmenu gecorrigeerd _(Osyotr)_
- Vastlopen van OpenStreetMap-login en -bewerkingen op Qt-versies 6.4 en ouder opgelost _(Alexander Borsuk)_
- Onverwachte kaartstijlwisseling tijdens routebegeleiding op macOS opgelost _(Alexander Borsuk)_
- Crash opgelost bij het sluiten van de macOS-app na het exporteren van een KMZ-bestand _(Alexander Borsuk)_

### Vertalingen

- Kantonese stapsgewijze gesproken routebegeleiding _(Alexander Borsuk)_
- Duitse en Franse vertalingen bijgewerkt _(Wuzzy, Alexander Borsuk)_
- Onjuiste vertalingen van gesproken aanwijzingen voor “onto street” in Chinees, Servisch en Catalaans gecorrigeerd _(Alexander Borsuk)_

## Doe mee met bètatesten om vroege functies te proberen en problemen te melden:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

We zijn al onze gebruikers en bijdragers dankbaar, iedereen die [doneert](@/donate/index.nl.md) en Organic Maps 5 sterren geeft in appstores. Samen kunnen we de beste kaarten-app bouwen!

Met liefde,
Organic Maps Team

{{ references() }}
