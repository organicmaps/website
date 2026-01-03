---
title: ¿Cómo puedo realizar una edición de mapas más avanzada?
description: Tutorial para editar OpenStreetMap con herramientas más avanzadas como
  ID, Go Map y Vespucci
updated: '2024-06-20'
taxonomies:
  faq: ["Edición de mapas"]
extra:
  order: 40
---

Organic Maps incluye un editor simple y fácil de usar que puede utilizar para editar el mapa. Sin embargo, el editor es limitado y solo permite agregar características de puntos simples, es decir, no se permiten contornos de edificios, carreteras, lagos, ciudades, etc. Si desea cambiar algo que no se puede editar con el editor integrado, esta es la página de preguntas frecuentes adecuada para leer.

Como todos los datos de mapas utilizados en Organic Maps provienen de [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), puede actualizar el mapa directamente allí. Sus modificaciones se incluirán en Organic Maps con la próxima actualización del mapa.

## Editores de OpenStreetMap

Para editar OSM, existen varias opciones. Si tiene una computadora portátil o de escritorio a mano, es mejor usar el [Editor de ID] (https://www.openstreetmap.org/edit) que se ejecuta en su navegador. El editor de ID es fácil para principiantes y una pantalla, un mouse y un teclado más grandes facilitan la edición de mapas.

Para la edición avanzada de mapas desde un dispositivo móvil, utilice [Go Map](https://apps.apple.com/us/app/go-map/id592990211) para iOS o [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) para Android. Go Map es fácil para principiantes, mientras que Vespucci está dirigido a usuarios más avanzados. LearnOSM proporciona tutoriales para [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) y [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Para realizar ediciones más sencillas y más divertidas, también puedes probar la [aplicación Every Door](https://every-door.app/) para iOS y Android y la [aplicación StreetComplete](https://streetcomplete.app/) para Android.

#### Editor de identificación

Para editar OpenStreetMap con ID sigue estos pasos:

1. Cree una cuenta nueva o inicie sesión en [OpenStreetMap.org](https://www.openstreetmap.org)
2. Busque la ubicación que desea editar en OpenStreetMap.org y haga clic en *Editar* en la parte superior.
3. *Inicie el tutorial* y siga el breve tutorial que explica el Editor de ID
4. Edita el mapa
5. Sube tus cambios

Eso es todo, ahora eres parte de la comunidad OSM.

## ¿Qué pasa con mis ediciones?

Una vez que presione *Cargar*, sus cambios se agregarán instantáneamente a la base de datos pública de OSM. Así que sea considerado al editar. En Organic Maps, sus cambios serán visibles después de la próxima actualización mensual del mapa.

Su correo electrónico no se publica, pero otras personas podrán ver su nombre de usuario de OSM. Como OSM ofrece la posibilidad de discutir cambios, es posible que otros contribuyentes de OSM le pregunten sobre sus ediciones. Se le notificará sobre esto a través de la dirección de correo electrónico que utilizó para registrar su cuenta OSM. Como OSM es un proyecto comunitario que se basa en la colaboración, siempre debes responder estas preguntas.

## Comunidad y Wiki

OpenStreetMap es una comunidad. Si necesita ayuda o tiene alguna pregunta, puede preguntar en el [Foro de OSM](https://community.openstreetmap.org/c/help-and-support) o echar un vistazo a la documentación de [OSM Wiki](https://wiki.openstreetmap.org/).

## Etiquetas: cómo funciona el modelo de datos de OSM

La base de datos de OpenStreetMap contiene objetos como nodos, vías, áreas y relaciones que se abstraen de características del mundo real. Estos Objetos tienen Atributos, los llamados Etiquetas para describirlos con más detalle. Una etiqueta es una combinación clave-valor.

Como esto suena más complicado de lo que es, daremos un ejemplo:
Un restaurante es p.e. mapeado como una Nota o Área con la Etiqueta ``` amenity=restaurant```. Luego se pueden utilizar más etiquetas como ```cousine=*``` o ```opening_hours=*``` para obtener más detalles.

> Tenga en cuenta que el editor de ID oculta la estructura de datos interna a los usuarios para que sea más amigable para los principiantes. Pero para leer la documentación Wiki es útil tener una breve descripción general de la estructura de datos.
En el Editor de ID, puede ver las etiquetas que ID le oculta expandiendo la sección *Etiquetas* en el panel lateral *Función de edición*.

## Notas de OSM {#osm-note}

Si no tiene tiempo o el problema es demasiado complicado, edite los datos de OSM usted mismo. Las Notas de OSM ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) son el camino a seguir. Puede colocar dicha nota en la ubicación del error del mapa y describir el problema en detalle. Otros voluntarios de OSM pueden ayudar y resolver el problema. Recibirá notificaciones por correo electrónico a través de su cuenta de OSM en caso de que tengan más preguntas o se resuelva la nota de OSM.

1. Cree una cuenta nueva o inicie sesión en [OpenStreetMap.org](https://www.openstreetmap.org)
   > También puedes abrir Notas anónimas, pero no se recomienda ya que no recibirás una notificación cuando se resuelva el problema o haya más preguntas.
2. Acérquese a la ubicación del mapa en [OpenStreetMap.org](https://www.openstreetmap.org) y presione *Agregar una nota al mapa* (segundo ícono desde abajo en el menú derecho). Luego arrastre el marcador azul del mapa a la ubicación exacta.
   > Intenta ser lo más preciso que puedas.
3. Proporcione una descripción detallada del problema del mapa y presione *Agregar nota*
   > Para tiendas, p. proporcione el nombre y mencione qué se vende allí o qué servicios se ofrecen.
