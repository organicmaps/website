---
title: Com puc fer una edició de mapes més avançada?
description: Tutorial per editar OpenStreetMap amb eines més avançades com ID, Go
  Map i Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
---

Organic Maps inclou un editor senzill i fàcil d'utilitzar que podeu utilitzar per editar el mapa. Tanmateix, l'editor és limitat i només permet afegir funcions puntuals senzilles, això vol dir que no hi ha contorns d'edificis, carreteres, llacs, pobles, etc. Si voleu canviar alguna cosa que no es pot editar amb l'editor integrat, aquesta és la pàgina de preguntes freqüents adequada per llegir.

Com que totes les dades del mapa que s'utilitzen als mapes orgànics provenen de [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), podeu actualitzar el mapa directament allà. Aleshores, les vostres modificacions s'inclouran a Organic Maps amb la propera actualització del mapa.

## Editors d'OpenStreetMap

Per editar OSM, hi ha diverses opcions. Si teniu un ordinador portàtil o d'escriptori a mà, és millor utilitzar l'[Editor d'ID](https://www.openstreetmap.org/edit) que s'executa al vostre navegador. L'Editor d'identificació és fàcil per als principiants, i una pantalla, un ratolí i un teclat més grans faciliten l'edició de mapes.

Per a l'edició avançada de mapes des d'un dispositiu mòbil, utilitzeu [Go Map](https://apps.apple.com/us/app/go-map/id592990211) per a iOS o [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) per a Android. Go Map és fàcil per als principiants, mentre que Vespucci s'adreça als usuaris més avançats. LearnOSM ofereix tutorials per a [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) i [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Per a edicions més senzilles i més divertides, també podeu provar [aplicació Every Door](https://every-door.app/) per a iOS i Android i [aplicació StreetComplete](https://streetcomplete.app/) per a Android.

#### Editor d'identificació

Per editar OpenStreetMap amb ID, seguiu aquests passos:

1. Creeu un compte nou o inicieu sessió a [OpenStreetMap.org](https://www.openstreetmap.org)
2. Navegueu a la ubicació que voleu editar a OpenStreetMap.org i feu clic a *Edita* a la part superior
3. *Inicieu el tutorial* i seguiu el tutorial breu que explica l'editor d'ID
4. Editeu el mapa
5. Carregueu els vostres canvis

Això és tot, ara formeu part de la comunitat OSM.

## Què passa amb les meves edicions?

Un cop premeu *Puja*, els vostres canvis s'afegeixen instantàniament a la base de dades pública OSM. Així que tingueu cura a l'hora d'editar. A Organic Maps, els vostres canvis seran visibles després de la propera actualització mensual del mapa.

El vostre correu electrònic no es publica, però altres persones podran veure el vostre nom d'usuari OSM. Com que OSM ofereix la possibilitat de discutir els canvis, és possible que rebeu preguntes sobre les vostres edicions d'altres col·laboradors d'OSM. Se us notificarà sobre això mitjançant l'adreça de correu electrònic que vau utilitzar per registrar el vostre compte OSM. Com que OSM és un projecte comunitari que es basa en la col·laboració, sempre hauríeu de respondre aquestes preguntes.

## Comunitat i Viqui

OpenStreetMap és una comunitat. Si necessiteu ajuda o teniu cap pregunta, podeu fer-ho al [Fòrum OSM](https://community.openstreetmap.org/c/help-and-support) o fer una ullada a la documentació [OSM Wiki](https://wiki.openstreetmap.org/).

## Etiquetes - Com funciona el model de dades OSM

La base de dades OpenStreetMap conté objectes com ara nodes, vies, àrees i relacions que abstreuen de les característiques del món real. Aquests Objectes tenen Atributs, els anomenats Etiquetes per descriure'ls amb més detall. Una etiqueta és una combinació clau-valor.

Com que això sembla més complicat del que és, posarem un exemple:
Un restaurant és, p. assignat com a nota o àrea amb l'etiqueta ``` amenity=restaurant```. A continuació, es poden utilitzar etiquetes addicionals com ```cousine=*``` o ```opening_hours=*``` per a més detalls.

> Tingueu en compte que l'editor d'identificació amaga l'estructura interna de dades als usuaris perquè sigui més fàcil de començar. Però per llegir la documentació de Wiki és útil fer una breu visió general de l'estructura de dades.
A l'Editor d'identificació, podeu veure les etiquetes que l'ID us amaga expandint la secció *Etiquetes* al tauler lateral *Funció d'edició*.

## Notes OSM {#osm-note}

Si no teniu temps o el problema és massa complicat per editar les dades OSM vosaltres mateixos, les notes OSM ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) són el camí a seguir. Podeu col·locar aquesta nota a la ubicació de l'error del mapa i descriure el problema amb detall. Altres voluntaris de l'OSM poden ajudar i resoldre el problema. Rebràs notificacions per correu electrònic a través del teu compte OSM per si tenen més preguntes o la nota OSM està resolta.

1. Creeu un compte nou o inicieu sessió a [OpenStreetMap.org](https://www.openstreetmap.org)
   > També podeu obrir Notes anònimes, però això no és recomanable, ja que no rebreu notificacions quan el problema es resolgui o hi hagi més preguntes.
2. Amplieu la ubicació del mapa a [OpenStreetMap.org](https://www.openstreetmap.org) i premeu *Afegeix una nota al mapa* (segona icona a la part inferior del menú dret). A continuació, arrossegueu el marcador blau del mapa fins a la ubicació exacta.
   > Intenta ser tan precís com puguis.
3. Proporcioneu una descripció detallada del problema del mapa i premeu *Afegeix una nota*
   > Per a botigues, p. indica el nom i esmenta què s'hi ven o quins serveis s'ofereixen.
