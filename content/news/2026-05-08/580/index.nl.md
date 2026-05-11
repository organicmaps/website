---
title: "Tik op een ov-halte om openbaarvervoerlijnen op de kaart te zien, bladwijzerlabels overlappen niet meer, kleinere downloadregio's in Vietnam, Maleisië en Zuid-China in de Organic Maps-update van mei"
date: 2026-05-08
slug: "ov-halte-selecteren-bladwijzerlabels-overlappen-niet-vietnam-maleisie-china-regiosplitsingen"
taxonomies:
  news: ["releases"]
---

De update van mei brengt volledige ondersteuning voor openbaar vervoer in Organic Maps een stap dichterbij. Een bus-, trein-, veerboot- of tramhalte is het startpunt voor de ov-lijnen die er langskomen — dus als je nu bij een halte op een route tikt, wordt die lijn in een eigen kleur over de hele kaart weergegeven. Er komen ook actuele online dienstregelingen aan, dus vergeet niet om de [OSM-gegevens voor openbaar vervoer in je regio toe te voegen of bij te werken](https://gtfs-osm-matcher.organicmaps.app/) als je dat nog niet hebt gedaan!

Zoals altijd: veel dank aan onze bijdragers, en bedankt voor jullie positieve recensies, [donaties](@/donate/index.nl.md) en [steun](@/contribute/index.nl.md).

Download de update van mei via <https://get.omaps.org> of via de [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] en [F-Droid][fdroid].

## Hoogtepunten

- **Tik op een bus-, tram-, trein- of veerboothalte op de kaart,** en Organic Maps markeert de volledige ov-lijn, die je kunt selecteren uit de lijst met weergegeven lijnen en routes.
- **Duidelijkere bladwijzerlabels en een beter leesbare kaart.** Dankzij de nieuwe plaatsing van labels verdringen bladwijzertitels elkaar niet meer, zijn voetgangersgebieden iets donkerder gemaakt en zijn de routekleuren aangepast voor een beter contrast in zowel het lichte als het donkere thema.
- **Fijnere regio-indeling in Azië.** Vietnam en Maleisië zijn nu opgedeeld in kleinere kaarten, zodat je alleen het gebied kunt downloaden dat je nodig hebt, en Hongkong, Macau en Hainan zijn nu gescheiden van Guangdong.

## Release-opmerkingen

### Alle platforms

- NIEUW! Tik op een ov-halte en selecteer een lijnnummer om de volledige ov-route op de kaart te markeren, net als in de metrokaartlaag (Viktor Govako, Kiryl Kaveryn, Mikhail Listratsenka)
- NIEUW! Bladwijzerlabels op de kaart overlappen elkaar niet meer (Viktor Govako)
- De berekeningen van hoogteverlies en hoogtewinst op de trackgrafieken zijn gecorrigeerd, zodat deze beter aansluiten bij de waarden van andere populaire apps (Viktor Govako)
- Openbaar vervoer over lange afstanden en andere kaartrelaties worden nu over kaartgrenzen heen samengevoegd tot één doorlopende lijn (Viktor Govako)
- Vietnam en Maleisië zijn opgedeeld in kleinere regio's die afzonderlijk kunnen worden gedownload (Viktor Govako)
- Hongkong, Macau en Hainan zijn gescheiden van Guangdong, waarbij de grenzen met aangrenzende gebieden zijn bijgewerkt (Viktor Govako)
- Bijgewerkte isolijnen (hoogtelijnen) voor Indonesië, Maleisië, Tanzania, Thailand en Vietnam (Viktor Govako)
- Routeplanning: hervatte routes slaan nu tussenpunten over die je al bent gepasseerd (Viktor Govako)
- Pictogrammen toegevoegd voor actieve vulkanen en toegangspunten tot waterwegen; botenhellingen zijn nu doorzoekbaar (David Martinez)
- Waterpijp-lounges toegevoegd (alnzrv)
- Gebouwen in aanbouw toegevoegd (Viktor Govako)
- "Lookout" toegevoegd als zoeksynoniem voor uitkijkpunten (alnzrv)
- "pkwy" toegevoegd als synoniem voor een straatnaam in de VS (Viktor Govako)
- De kleuren van voetgangersgebieden zijn iets donkerder gemaakt voor een betere leesbaarheid (Viktor Govako)
- Tekst over meerdere regels wordt nu netjes afgekapt op de kaart (Viktor Govako)
- Straatnamen bevatten geen dubbele onderdelen meer (Viktor Govako)
- KMB-bestandsimport hersteld (Alexander Borsuk)
- Vertalingen bijgewerkt voor categorieën, zoeksynoniemen en UI-teksten (Alexander Borsuk, Viktor Govako)
- Beschrijvingen van New South Wales en het Northern Territory vertaald (alnzrv)
- Verbeterde stabiliteit en prestaties, waaronder lettertypevorming, glyph-caching en het afkappen van routelijnen (Viktor Govako, Alexander Borsuk)

### iOS

- NIEUW! Knop voor trackopname toegevoegd aan het infopaneel tijdens het navigeren (Kiryl Kaveryn)
- NIEUW! Twee extra stappen in het navigatiedashboard voor gedetailleerdere informatie over hoogte en route (Kiryl Kaveryn)
- Bijgewerkte stijl van het hoogteprofiel in het navigatiedashboard, met correcte weergave voor tracks met negatieve hoogtes (Kiryl Kaveryn)
- Onjuiste lijst met bladwijzers in de TestFlight-versie verholpen (Alexander Borsuk)
- Grotere stopknop en grotere aanraakgebieden voor de knoppen in het onderste paneel tijdens het navigeren: TTS dempen, instellingen, trackopname (Kiryl Kaveryn)
- Verfijnde animatie van het uitklapbare beschrijvingsgedeelte op de plaatspagina (Kiryl Kaveryn)
- De plaatspagina verdwijnt niet meer na het verslepen in het hoogteprofiel, springt niet meer onverwacht heen en weer en houdt de titel zichtbaar wanneer je bewerkt met het toetsenbord geopend (Kiryl Kaveryn)
- Problemen met de kleur van het hoogteprofiel en de cirkelvormige voortgangsindicator bij wijzigingen in de systeemweergave verholpen (Kiryl Kaveryn)
- Crashes bij het verwijderen van een track of bladwijzer die niet meer bestaat, verholpen (Kiryl Kaveryn)

### Android

- NIEUW! Blijvend zichtbaar hoogtedashboard en verfijnd hoogteprofiel van de route, met correcte RTL-indeling (Eric Jau, Mikhail Listratsenka)
- De opgeslagen routestatus blijft nu behouden wanneer het apparaat wordt gedraaid (Mikhail Listratsenka)
- Eén enkele, uniforme referentielijn voor de route op de plaatspagina (Mikhail Listratsenka)
- Grotere hoekradius voor bottom sheets, knoppen en drawables voor een consistentere uitstraling (Mikhail Listratsenka)
- Problemen met de lay-out rond de systeembalken en de navigatiebalk verholpen (Mikhail Listratsenka)
- Verbeterde weergave van Wikipedia-artikelen met betere opmaak, systeemkleuren en betere verwerking van de donkere modus (DeshDeepakKant, Mikhail Listratsenka)
- Verticale scheidingslijnen toegevoegd tussen segmenten van tracks met meerdere geometrieën in het hoogteprofiel (Mikhail Listratsenka)
- Verbeterd scrollgedrag van het hoogteprofiel (Mikhail Listratsenka)
- Correcties in de rechts-naar-links (RTL)-lay-out (Mikhail Listratsenka)

### Linux en Mac OS

- Een ov-routekiezer toegevoegd om een specifieke lijn te selecteren wanneer een halte is gekozen (Viktor Govako)
- Routeactieknoppen direct op de plaatspagina weergegeven (Viktor Govako)
- Dubbele openingstijden uit de plaatspagina verwijderd (Viktor Govako)
- De tussenliggende routemarkering op een POI of adres toont nu de naam van de plaats (Viktor Govako)
- Het downloaden van kaarten wordt bij een nette afsluiting hervat op het punt waar het was gebleven (Alexander Borsuk)
- Organic Maps werkt nu met OpenGL ES 3.0-stuurprogramma's (Alexander Borsuk)

Doe mee aan de bètatest om nieuwe functies alvast te proberen en problemen te melden:
- [iOS][testflight]
- [Android][firebase]

Wij houden van onze gebruikers ❤️ en wij houden van wat we doen

Het Organic Maps-team

{{ references() }}
