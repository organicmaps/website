---
title: Como podo facer edicións de mapas máis avanzadas?
slug: como-podo-facer-edicións-de-mapas-máis-avanzadas
description: Titorial para editar OpenStreetMap con ferramentas máis avanzadas como
  ID, Go Map e Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
aliases:
  - /gl/faq/editing/advanced-map-editing/
---

Organic Maps inclúe un editor sinxelo e fácil de usar que podes usar para editar o mapa. Non obstante, o editor é limitado e só permite engadir funcións puntuais simples, o que significa que non hai contornos de edificios, estradas, lagos, cidades, etc. Se queres cambiar algo que non se pode editar co editor integrado, esta é a páxina de preguntas frecuentes correcta para ler.

Como todos os datos do mapa utilizados en Organic Maps proceden de [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), podes actualizar o mapa directamente alí. As túas modificacións incluiranse en Organic Maps coa próxima actualización do mapa.

## Editores de OpenStreetMap

Para editar OSM, hai varias opcións. Se tes un ordenador portátil ou de escritorio a man, é mellor utilizar o [Editor de ID](https://www.openstreetmap.org/edit) que se executa no teu navegador. O Editor de ID é sinxelo para os principiantes, e unha pantalla, rato e teclado máis grandes facilitan a edición de mapas.

Para editar mapas avanzado desde un dispositivo móbil, usa [Go Map](https://apps.apple.com/us/app/go-map/id592990211) para iOS ou [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) para Android. Go Map é fácil para os principiantes, mentres que Vespucci está dirixido a usuarios máis avanzados. LearnOSM ofrece titoriais para [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) e [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Para realizar edicións máis sinxelas e divertidas, tamén podes probar [aplicación Every Door](https://every-door.app/) para iOS e Android e [aplicación StreetComplete](https://streetcomplete.app/) para Android.

#### Editor de ID

Para editar OpenStreetMap con ID, siga estes pasos:

1. Crea unha nova conta ou inicia sesión en [OpenStreetMap.org](https://www.openstreetmap.org)
2. Navega ata a localización que queres editar en OpenStreetMap.org e fai clic en *Editar* na parte superior
3. *Inicie o tutorial* e siga o breve tutorial que explica o Editor de ID
4. Edita o mapa
5. Carga os teus cambios

Iso é todo, agora formas parte da comunidade OSM.

## Que pasa coas miñas edicións?

Unha vez que premes *Cargar*, os teus cambios engádense instantáneamente á base de datos pública OSM. Polo tanto, teña en conta ao editar. En Organic Maps, os teus cambios serán visibles despois da próxima actualización mensual do mapa.

O teu correo electrónico non está publicado, pero outras persoas poderán ver o teu nome de usuario OSM. Dado que OSM ofrece a posibilidade de discutir os cambios, pode recibir preguntas sobre as súas edicións doutros colaboradores de OSM. Serás notificado sobre isto a través do enderezo de correo electrónico que utilizaches para rexistrar a túa conta OSM. Como OSM é un proxecto comunitario que se basea na colaboración, sempre debes responder a estas preguntas.

## Comunidade e Wiki

OpenStreetMap é unha comunidade. Se precisas axuda ou tes algunha dúbida, podes preguntar no [OSM Forum](https://community.openstreetmap.org/c/help-and-support) ou botar unha ollada á [OSM Wiki](https://wiki.openstreetmap.org/).

## Etiquetas - Como funciona o modelo de datos OSM

A base de datos OpenStreetMap contén Obxectos como Nodos, Camiños, Áreas e Relacións que abstraen de características do mundo real. Estes Obxectos teñen Atributos, os chamados Etiquetas para describilos aínda máis. Unha etiqueta é unha combinación clave-valor.

Como isto parece máis complicado do que é, imos poñer un exemplo:
Un restaurante é por exemplo. mapeada como nota ou área coa etiqueta ``` amenity=restaurant```. Pódense usar outras etiquetas como ```cousine=*``` ou ```opening_hours=*``` para obter máis detalles.

> Teña en conta que o editor de ID oculta a estrutura de datos interna dos usuarios para que sexa máis amigable para principiantes. Pero para ler a documentación do Wiki é útil facer unha breve visión xeral da estrutura de datos.
No Editor de ID, podes ver as etiquetas que o ID está agochando para ti ampliando a sección *Etiquetas* no panel lateral *Función de edición*.

## Notas OSM {#osm-note}

Se non tes tempo ou o problema é demasiado complicado para editar ti mesmo os datos OSM, OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) é o camiño a seguir. Podes colocar esa nota na localización do erro do mapa e describir o problema en detalle. Outros voluntarios de OSM poden axudar e resolver o problema. Recibirás notificacións por correo electrónico a través da túa conta de OSM no caso de que teñan máis preguntas ou se resolva a nota OSM.

1. Crea unha nova conta ou inicia sesión en [OpenStreetMap.org](https://www.openstreetmap.org)
   > Tamén pode abrir Notas anónimas, pero non se recomenda, xa que non recibirá notificacións cando se resolva o problema ou haxa máis preguntas.
2. Zoom na localización do mapa en [OpenStreetMap.org](https://www.openstreetmap.org) e prema *Engadir unha nota ao mapa* (segunda icona da parte inferior no menú dereito). A continuación, arrastre o marcador azul do mapa ata a localización exacta.
   > Tenta ser o máis preciso posible.
3. Proporcione unha descrición detallada do problema do mapa e prema *Engadir nota*
   > Para tendas p.ex. indica o nome e menciona o que alí se vende ou os servizos que se ofrecen.
