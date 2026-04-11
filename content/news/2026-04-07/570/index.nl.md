---
title: "Wandel- en fietsroutes met hoogteprofielen, slimmer zoeken naar adressen in de VS, naadloze kaartdoorloop bij de antimeridiaan en meer in de Organic Maps-update van april"
date: 2026-04-07
slug: "wandel-fietsroutes-hoogtegrafieken-vs-adres-zoeken-antimeridiaan-kaart-april-2026-organic-maps-update"
taxonomies:
  news: ["Releases"]
---

Deze release van april draait, naast veel bugfixes en verbeteringen, om drie simpele waarheden: wandelaars willen weten hoeveel hoogtemeters hen te wachten staan, iedereen wil dat het zoeken naar een adres gewoon werkt en niemand mag het gevoel hebben van de rand van de kaart te vallen. Dankzij onze bijdragers, jullie goede recensies, [donaties](@/donate/index.nl.md) en [steun](@/contribute/index.nl.md), hebben we alle drie aangepakt — en nog veel meer.

Of de lente je nu naar nieuwe paden trekt of de herfst op het zuidelijk halfrond vraagt om een laatste lange rit, we hopen dat deze update je volgende tocht een beetje makkelijker en een stuk mooier maakt.

Download de april-update op <https://get.omaps.org> of in de [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], en [F-Droid][fdroid].

## Hoogtepunten

- **Tik op een route, zie de klim.** Wandel- en fietsroutes kunnen nu direct op de kaart worden geselecteerd. Tik op een route om die te markeren en meteen het hoogteprofiel te bekijken.
- **Twee miljoen extra adressen in de VS en slimmer zoeken.** Meer adressen, ontleed uit de TIGER Census-dataset, zitten nu in de app. Naast slimmere herkenning van huisnummers verbetert dat overal de zoekresultaten. Vergeet niet dat ontbrekende adressen toevoegen aan [OpenStreetMap](https://www.openstreetmap.org) nog altijd de beste manier is om zoeken te verbeteren.
- **Een kaart zonder randen.** Organic Maps loopt nu vloeiend door over de antimeridiaan (±180° lengtegraad). Sleep en draai tussen Tsjoekotka en Alaska, of Nieuw-Zeeland en Fiji, zonder onzichtbare muren en zonder rare resets — de Stille Oceaan voelt eindelijk rond.
- **Een hele categorie in één keer herkleuren.** Verander met één tik de kleur van alle bladwijzers en/of tracks in een categorie — een klein detail dat het rommelige reisarchief van vorige zomer verandert in iets dat je echt weer wilt openen.

## Release-opmerkingen

### Alle platforms

- NIEUW! Beter zoeken in de VS, met twee miljoen extra adressen ontleed uit TIGER Census-gegevens (Viktor Govako)
- NIEUW! Verbeterde meerkleurenweergave voor wandel- en fietsroutes; tik op een route om die te selecteren en het hoogteprofiel te bekijken (Viktor Govako)
- OpenStreetMap-gegevens bijgewerkt tot en met 4 april
- Wikipedia-gegevens bijgewerkt per 1 april
- Benadering van stijgen en dalen in trackgrafieken aangepast zodat die beter overeenkomt met de waarden in andere apps (Viktor Govako)
- Je kunt nu een nieuwe plaats toevoegen aan OpenStreetMap na het selecteren van je huidige positie op de kaart (Mikhail Listratsenka)
- Pictogrammen toegevoegd voor foodcourts en stadspoorten (David Martinez)
- Subcategorieën voor kledingwinkels toegevoegd: dames, heren, kinderen, bruidsmode, sport en ondergoed, plus kantoortypes (Viktor Govako)
- Zoekcategorieën bijgewerkt: "Brood" toegevoegd voor bakkerijen, "Shawarma" als keuken en andere synoniemverbeteringen (Viktor Govako)
- De kaart loopt nu correct door over de antimeridiaan (±180° lengtegraad) tijdens slepen en draaien (Alexander Borsuk, Viktor Govako)
- Fietsnavigatie gebruikt nu kompasrichting bij lage snelheden (HossamSaberr)
- Zoeken naar adressen op huisnummer verbeterd (Viktor Govako)
- Een systeemfout opgelost bij het plannen van routes in de buurt van sommige regionale grenzen (Viktor Govako)
- Zoekresultaten verbeterd wanneer plaats- en staatsnamen hetzelfde zijn (Viktor Govako)
- Amerikaanse straatsynoniemen toegevoegd: highway, hwy, freeway en fwy (Viktor Govako)
- Uitlijning van het editor-kruis hersteld bij het indrukken van "Plaats toevoegen" (José Araújo)
- Weergave van openingstijden voor plaatsen met offsets voor zonsopgang/-ondergang hersteld (Alexander Borsuk)
- Verholpen dat GPS-trackopname punten tussen segmenten liet vallen (Alexander Borsuk)
- Afhandeling van zomertijd voor tijdzones hersteld (Andrei Shkrob)
- Kleuren van de metro van Sydney hersteld (Alexander Borsuk)
- GeoJSON-import hersteld (Alexander Borsuk)
- Stabiliteit en prestaties verbeterd (Alexander Borsuk, Viktor Govako)
- Vertalingen bijgewerkt (Alexander Borsuk, Viktor Govako, Weblate-bijdragers)

### iOS

**Let op voor bezitters van oudere iPhones en iPads:** Door recente wijzigingen in TestFlight en de App Store ondersteunt deze release alleen iOS 15 en nieuwer. iOS 12, 13 en 14 worden niet langer ondersteund. Eerder geïnstalleerde versies van Organic Maps blijven werken op oudere apparaten, maar nieuwe kaarten, functies en fixes komen voortaan alleen nog naar iOS 15 en hoger.

- NIEUW! Verander in één keer de kleuren van alle bladwijzers en tracks in een categorie (Kiryl Kaveryn)
- Verbeterde weergave van HTML-inhoud met tabellen en afbeeldingen in bladwijzergegevens (Alexander Borsuk, Kiryl Kaveryn)
- Verticale scheidingslijnen toegevoegd voor tracks met meerdere segmenten in het hoogteprofiel (Kiryl Kaveryn)
- Puntselectie in het hoogteprofiel voor geïnterpoleerde punten hersteld (Kiryl Kaveryn)
- Modale gebaren verbeterd: springt naar de dichtstbijzijnde stap, sluit bij slepen vanaf de rand en herstelt de vorige toestand bij opnieuw openen (Kiryl Kaveryn)
- Je kunt nu een geldige route starten, zelfs als je wordt gevraagd om extra kaarten te downloaden (Kiryl Kaveryn)
- Het aanraakgebied van knoppen in de navigatiebalk "Plaats toevoegen" vergroot (Noahdyn)
- Crash verholpen bij het exporteren van tracks (Alexander Borsuk, Kiryl Kaveryn)
- Zoeken in bladwijzer-/tracklijsten hersteld wanneer je erop tikt vanuit plaatsdetails (Kiryl Kaveryn)

### Android

- NIEUW! Verander in één keer de kleuren van alle bladwijzers en tracks in een categorie (Mikhail Listratsenka)
- NIEUW! Geplande weergavemodus in Instellingen voor automatisch wisselen tussen licht en donker op basis van zonsopgang en zonsondergang (Dzmitry Strekha)
- Geschiedenis van recent gebruikte categorieën toegevoegd aan de kaarteditor (Mikhail Listratsenka)
- Een trampictogram toegevoegd voor tramhaltes die op de kaart zijn geselecteerd (Mikhail Listratsenka)
- De downloadknop verbergen wanneer alle kaarten al zijn gedownload (Mikhail Listratsenka)
- Uploaden van kaartbewerkingen naar OpenStreetMap hersteld (Viktor Govako)
- Delen van bestanden naar Google Drive en andere apps hersteld (Alexander Borsuk)
- Opnieuw importeren van bladwijzers hersteld bij het heropenen van de app vanuit recente apps (Alexander Borsuk)
- Het openen van OpenStreetMap-zoek-URL's zoals `openstreetmap.org/search?query=Pizza` start nu direct een zoekopdracht in Organic Maps (Rawdyrathaur)
- Diverse crashes verholpen (Alexander Borsuk)

### Desktop (Linux en Mac OS)

- De mogelijkheid toegevoegd om een gidsspoor te selecteren voor routering (Viktor Govako)
- Verholpen dat het opslaan of exporteren van bladwijzers/tracks in sommige landinstellingen kapotte bestanden opleverde door locale-afhankelijke decimale scheidingstekens (Alexander Borsuk)


Doe mee aan bètatests om vroege functies te proberen en problemen te melden:
- [iOS][testflight]
- [Android][firebase]

Met liefde en zorg ❤️
Het Organic Maps Team

{{ references() }}
