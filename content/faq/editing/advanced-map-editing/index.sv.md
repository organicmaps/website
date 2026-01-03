---
title: Hur kan jag göra mer avancerad kartredigering?
description: Handledning för redigering av OpenStreetMap med mer avancerade verktyg
  som ID, Go Map och Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
---

Organiska kartor innehåller en enkel och lättanvänd redigerare som du kan använda för att redigera kartan. Redaktören är dock begränsad och tillåter bara att lägga till enkla punktfunktioner, det vill säga inga byggnadskonturer, vägar, sjöar, städer etc. Om du vill ändra något som inte går att redigera med den inbyggda editorn är detta rätt FAQ-sida att läsa.

Eftersom all kartdata som används i Organic Maps kommer från [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), kan du uppdatera kartan direkt där. Dina ändringar kommer sedan att inkluderas i Organic Maps med nästa kartuppdatering.

## OpenStreetMap Editors

För redigering av OSM finns det flera alternativ. Om du har en bärbar eller stationär dator till hands är det bättre att använda [ID Editor](https://www.openstreetmap.org/edit) som körs i din webbläsare. ID Editor är lätt för nybörjare, och en större skärm, mus och tangentbord gör kartredigering enklare.

För avancerad kartredigering från en mobil enhet, använd [Go Map](https://apps.apple.com/us/app/go-map/id592990211) för iOS eller [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) för Android. Go Map är lätt för nybörjare, medan Vespucci riktar sig till mer avancerade användare. LearnOSM tillhandahåller självstudier för [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) och [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

För enklare redigeringar med roligare kan du också prova [Every Door-appen](https://every-door.app/) för iOS och Android och [StreetComplete-appen](https://streetcomplete.app/) för Android.

#### ID Editor

Följ dessa steg för att redigera OpenStreetMap med ID:

1. Skapa ett nytt konto eller logga in på [OpenStreetMap.org](https://www.openstreetmap.org)
2. Bläddra till platsen du vill redigera på OpenStreetMap.org och klicka på *Redigera* längst upp
3. *Starta genomgången* och följ den korta handledningen som förklarar ID-redigeraren
4. Redigera kartan
5. Ladda upp dina ändringar

Det är allt, du är nu en del av OSM-gemenskapen.

## Vad händer med mina redigeringar?

När du trycker på *Ladda upp* läggs dina ändringar omedelbart till i den offentliga OSM-databasen. Så var hänsynsfull när du redigerar. I Organic Maps kommer dina ändringar att vara synliga efter nästa månatliga kartuppdatering.

Din e-post är inte publicerad, men andra personer kommer att kunna se ditt OSM-användarnamn. Eftersom OSM erbjuder möjligheten att diskutera ändringar kan du få frågor om dina redigeringar från andra OSM-bidragsgivare. Du kommer att meddelas om detta via den e-postadress du använde för att registrera ditt OSM-konto. Eftersom OSM är ett samhällsprojekt som bygger på samarbete bör du alltid svara på sådana frågor.

## Community och Wiki

OpenStreetMap är en gemenskap. Om du behöver hjälp eller har några frågor kan du ställa dem i [OSM Forum](https://community.openstreetmap.org/c/help-and-support) eller ta en titt på [OSM Wiki](https://wiki.openstreetmap.org/) dokumentationen.

## Taggar - Hur OSM-datamodellen fungerar

OpenStreetMap-databasen innehåller objekt som noder, sätt, områden och relationer som abstraherar från verkliga funktioner. Dessa objekt har attribut, så kallade taggar för att ytterligare beskriva dem. En tagg är en nyckel-värde kombination.

Eftersom detta låter mer komplicerat än vad det är kommer vi att ge ett exempel:
En Restaurang är t.ex. mappas som en anteckning eller område med taggen ``` amenity=restaurang```. Ytterligare taggar som ```cousine=*``` eller ```opening_hours=*``` kan sedan användas för ytterligare information.

> Observera att ID-redigeraren döljer den interna datastrukturen för användarna för att vara mer nybörjarvänlig. Men för att läsa Wiki-dokumentationen är en kort översikt över datastrukturen till hjälp.
I ID Editor kan du se taggar som ID döljer för dig genom att expandera avsnittet *Taggar* i sidopanelen *Redigera funktion*.

## OSM-anteckningar {#osm-note}

Om du inte har tid eller om problemet är för komplicerat för att själv redigera OSM-data är OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) rätt väg att gå. Du kan placera en sådan anteckning på platsen för kartfelet och beskriva problemet i detalj. Andra OSM-volontärer kan då hjälpa till och lösa problemet. Du kommer att få e-postmeddelanden via ditt OSM-konto om de har ytterligare frågor eller OSM-anteckningen är löst.

1. Skapa ett nytt konto eller logga in på [OpenStreetMap.org](https://www.openstreetmap.org)
   > Du kan också öppna anonyma anteckningar, men detta rekommenderas inte eftersom du inte får något meddelande när problemet är löst eller det finns ytterligare frågor.
2. Zooma till kartplatsen på [OpenStreetMap.org](https://www.openstreetmap.org) och tryck på *Lägg till en anteckning på kartan* (andra ikonen längst ner till höger i menyn). Dra sedan den blå kartmarkören till den exakta platsen.
   > Försök att vara så precis du kan.
3. Ge en detaljerad beskrivning av kartproblemet och tryck på *Lägg till anteckning*
   > För butiker t.ex. ange namn och ange vad som säljs där eller vilka tjänster som erbjuds.
