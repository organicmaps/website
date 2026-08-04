---
title: "Bugfixes en verbeteringen voor het openbaar vervoer, routebepaling, zoeken en bladwijzers in de update van juli 2026"
date: 2026-07-23
slug: "bugfixes-verbeteringen-openbaar-vervoer-routes-zoeken-bladwijzers-juli-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Zoals je misschien al hebt gemerkt, is de juli-update van Organic Maps nu beschikbaar. Je kunt hem downloaden via <https://get.omaps.org> of via de [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] en [F-Droid][fdroid].

Dankzij jouw [donaties](@/donate/index.nl.md) en [feedback](@/contribute/index.nl.md) hebben we ons in juli gericht op het verhelpen van bugs en het doorvoeren van verbeteringen. Mocht je het gemist hebben: de volgende functies uit de [vorige release van juni](@/news/2026-06-29/610/index.nl.md) zijn ook beschikbaar:
- Openbaarvervoersroutes (realtime dienstregelingen worden momenteel ontwikkeld)
- Satellietbeelden
- Alternatieve routes voor de auto, wandelen en fietsen
- Nieuwe interface voor zoeken en routeplanning op Android
- Ondersteuning voor grote toegankelijkheidslettertypen op iOS

## Gedetailleerd wijzigingslogboek

### Kaart & plaatsen
- OpenStreetMap-gegevens bijgewerkt tot 14 juli
- Notities die aan [OpenStreetMap](https://www.openstreetmap.org) worden gemeld, worden nu op de exacte plek geplaatst die je hebt geselecteerd, in plaats van in het midden van de hele straat of het hele gebied _(Alexander Borsuk)_
- Verbeterde plaatskeuze bij het tikken op de kaart in gebieden die de 180°-antimeridiaan doorkruisen _(Viktor Govako)_
- In hoogteprofielen van tracks worden geen verouderde of lege grafieken meer weergegeven nadat een track is verwijderd _(Kiryl Kaveryn)_

### Openbaar vervoer
- De namen van haltes, overstapplaatsen en stations hebben nu een witte omtrek, zodat ze zowel in het lichte als in het donkere thema goed leesbaar blijven _(Viktor Govako)_
- De metrolaag verschijnt weer correct nadat je het voorbeeld van een openbaarvervoerroute hebt gesloten _(Mikhail Listratsenka)_

### Routebepaling en navigatie
- Routewaarschuwingen (tolwegen, veerboten, onverharde wegen, trappen, enzovoort) worden nu weergegeven voor alle alternatieve routes _(Viktor Govako)_
- Een zeldzame vastloper tijdens het uitstippelen van een route is verholpen _(Viktor Govako)_
- Verbeterde afhandeling van doodlopende wegen en van begin- en eindpunten op wegen met toegangsbeperkingen _(Viktor Govako)_
- Onjuiste en ontbrekende aanwijzingen voor afslagen gecorrigeerd _(Alexander Borsuk)_

### iOS
- Nieuwe instelling ‘Zoekgeschiedenis opslaan’, waarmee je de geschiedenis kunt uitschakelen en verbergen als je deze liever niet wilt bewaren _(Kiryl Kaveryn)_
- Nieuwe knop ‘Bewerken’ om bladwijzers gemakkelijker te verwijderen _(Kiryl Kaveryn)_
- Bladwijzers worden nu automatisch opgeslagen wanneer je het scherm verlaat _(Kiryl Kaveryn)_
- Het kleurenpalet biedt nu vooraf gedefinieerde kleuren en geeft je de mogelijkheid om elke gewenste kleur te kiezen _(Kiryl Kaveryn)_
- De lege toestand van de hoogtegrafiek voor een opgenomen track is verbeterd _(Kiryl Kaveryn)_
- De weergave van de voortgang van de route op de Start-knop is verbeterd _(Kiryl Kaveryn)_
- Het herschikken van de haltes op een route zorgt er niet langer voor dat de lijst gaat springen _(Kiryl Kaveryn)_
- Andere kleine verbeteringen aan de gebruikersinterface _(Kiryl Kaveryn)_

### Android
- De openingstijden tonen nu gesplitste diensten (zoals een lunchpauze), beginnen bij de huidige dag en tonen de hele week zonder apart scrollgebied _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Een overzichtelijkere zoekbalk met een gecombineerde knop voor ‘Wissen’ en ‘Spraak’, een ‘Wissen’-pictogram dat niet meer verschuift, en lay-outcorrecties voor liggende modus en telefoonrotatie _(Mikhail Listratsenka)_
- Vernieuwde bladwijzer- en track-editor _(Mikhail Listratsenka)_
- Correcties en verbeteringen aan de routeplanning _(Mikhail Listratsenka)_
- De kleurenkiezer sluit nu automatisch, en een crash in Android 5 is verholpen _(Mikhail Listratsenka)_
- Crashes verholpen _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- De lijst met kaarten die je kunt downloaden, is nu alfabetisch gesorteerd _(goncalo109560)_

### Vertalingen
- Verbeterde Chinese formulering _(Chenxi Zhao)_
- Bijgewerkte Oekraïense vertalingen _(Nnifria)_
- Italiaanse vertalingen van de namen van kaartregio’s gecorrigeerd _(Vittorio Bertola)_

## Neem deel aan bètatesten om vroege functies te proberen en problemen te melden:

Tip: de bètaversie bevat nieuwe reliëfschaduw, verbeterde hoogtegegevens met ondersteuning voor voet en meter, en nog meer coole functies!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Fijne zomer!
Organic Maps Team

{{ references() }}
