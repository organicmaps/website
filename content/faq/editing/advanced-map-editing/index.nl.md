---
title: Hoe kan ik geavanceerder kaartbewerkingen uitvoeren?
slug: hoe-kan-ik-geavanceerder-kaartbewerkingen-uitvoeren
description: Tutorial voor het bewerken van OpenStreetMap met meer geavanceerde tools
  zoals ID, Go Map en Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
aliases:
  - /nl/faq/editing/advanced-map-editing/
---

Organische kaarten bevatten een eenvoudige en gebruiksvriendelijke editor waarmee u de kaart kunt bewerken. De editor is echter beperkt en staat alleen toe om eenvoudige puntkenmerken toe te voegen, dat wil zeggen geen bebouwingscontouren, wegen, meren, steden, etc. Als je iets wilt veranderen dat niet kan worden bewerkt met de ingebouwde editor, dan is dit de juiste FAQ-pagina om te lezen.

Omdat alle kaartgegevens die in Organische kaarten worden gebruikt, afkomstig zijn van [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), kunt u de kaart daar direct bijwerken. Uw wijzigingen worden vervolgens bij de volgende kaartupdate opgenomen in Organische kaarten.

## OpenStreetMap-editors

Voor het bewerken van OSM zijn er verschillende opties. Als u een laptop of desktopcomputer bij de hand heeft, kunt u beter de [ID Editor](https://www.openstreetmap.org/edit) gebruiken die in uw browser draait. De ID-editor is gemakkelijk voor beginners, en een groter scherm, muis en toetsenbord maken het bewerken van kaarten eenvoudiger.

Voor geavanceerde kaartbewerking vanaf een mobiel apparaat gebruikt u [Go Map](https://apps.apple.com/us/app/go-map/id592990211) voor iOS of [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) voor Android. Go Map is gemakkelijk voor beginners, terwijl Vespucci zich richt op meer gevorderde gebruikers. LearnOSM biedt tutorials voor [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) en [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Voor eenvoudigere bewerkingen met meer plezier kunt u ook de [Every Door-app](https://every-door.app/) voor iOS en Android en de [StreetComplete-app](https://streetcomplete.app/) voor Android proberen.

#### ID-editor

Volg deze stappen om OpenStreetMap met ID te bewerken:

1. Maak een nieuw account aan of log in op [OpenStreetMap.org](https://www.openstreetmap.org)
2. Blader naar de locatie die u wilt bewerken op OpenStreetMap.org en klik bovenaan op *Bewerken*
3. *Start de Walkthrough* en volg de korte tutorial waarin de ID-editor wordt uitgelegd
4. Bewerk de kaart
5. Upload uw wijzigingen

Dat is alles, u maakt nu deel uit van de OSM-gemeenschap.

## Wat gebeurt er met mijn bewerkingen?

Zodra u op *Upload* drukt, worden uw wijzigingen onmiddellijk toegevoegd aan de openbare database van OSM. Wees dus attent bij het bewerken. In Organische kaarten zijn uw wijzigingen zichtbaar na de volgende maandelijkse kaartupdate.

Uw e-mail wordt niet gepubliceerd, maar andere mensen kunnen uw OSM-gebruikersnaam zien. Omdat OSM de mogelijkheid biedt om wijzigingen te bespreken, kunt u vragen krijgen over uw bewerkingen van andere OSM-bijdragers. U wordt hierover geïnformeerd via het e-mailadres dat u heeft gebruikt bij het registreren van uw OSM-account. Omdat OSM een gemeenschapsproject is dat voortbouwt op samenwerking, moet u dergelijke vragen altijd beantwoorden.

## Gemeenschap en Wiki

OpenStreetMap is een gemeenschap. Als u hulp nodig heeft of vragen heeft, kunt u deze stellen op het [OSM Forum](https://community.openstreetmap.org/c/help-and-support) of een kijkje nemen in de [OSM Wiki](https://wiki.openstreetmap.org/) documentatie.

## Tags - Hoe het OSM-datamodel werkt

De OpenStreetMap-database bevat objecten zoals knooppunten, wegen, gebieden en relaties die abstractie maken van kenmerken uit de echte wereld. Deze objecten hebben attributen, zogenaamde tags, om ze verder te beschrijven. Een tag is een sleutel-waardecombinatie.

Omdat dit ingewikkelder klinkt dan het is, zullen we een voorbeeld geven:
Een restaurant is b.v. in kaart gebracht als een notitie of gebied met de tag `amenity=restaurant`. Verdere tags zoals `cuisine=*` of `opening_hours=*` kunnen dan worden gebruikt voor meer details.

> Merk op dat de ID-editor de interne datastructuur voor de gebruikers verbergt om beginnersvriendelijker te zijn. Maar voor het lezen van de Wiki-documentatie is een kort overzicht van de datastructuur nuttig.
In de ID-editor kunt u de tags zien die ID voor u verbergt door de sectie *Tags* in het zijpaneel *Functie bewerken* uit te vouwen.

## OSM-notities {#osm-note}

Als u geen tijd heeft of als het probleem te ingewikkeld is om de gegevens van OSM zelf te bewerken, is OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) de juiste keuze. U kunt een dergelijke notitie op de locatie van de kaartfout plaatsen en het probleem gedetailleerd beschrijven. Andere vrijwilligers van OSM kunnen dan helpen en het probleem oplossen. U ontvangt e-mailmeldingen via uw OSM-account voor het geval ze nog vragen hebben of de OSM-opmerking is opgelost.

1. Maak een nieuw account aan of log in op [OpenStreetMap.org](https://www.openstreetmap.org)
   > Je kunt ook anonieme Notes openen, maar dit wordt niet aanbevolen omdat je geen melding krijgt als het probleem is opgelost of als er verdere vragen zijn.
2. Zoom naar de kaartlocatie op [OpenStreetMap.org](https://www.openstreetmap.org) en druk op *Een notitie toevoegen aan de kaart* (tweede pictogram van onderen in het rechtermenu). Sleep vervolgens de blauwe kaartmarkering naar de exacte locatie.
   > Probeer zo nauwkeurig mogelijk te zijn.
3. Geef een gedetailleerde beschrijving van het kaartprobleem en druk op *Opmerking toevoegen*
   > Voor winkels b.v. vermeld de naam en vermeld wat daar wordt verkocht of welke diensten worden aangeboden.
