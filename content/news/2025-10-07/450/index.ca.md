---
title: "Llançament d'octubre: Límits de velocitat a Android Auto, importació GeoJSON, estadístiques de gravació de rutes, visualització de l'etiqueta de descripció OSM, desar punts d'interès en la ruta seleccionada a iOS i més"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

Aquesta actualització d'octubre d'Organic Maps afegeix la visualització del límit de velocitat a Android Auto, la importació de GeoJSON, les estadístiques de gravació de rutes, mostra les etiquetes de descripció d'OSM (escriviu `?description` al quadre de cerca per veure-les) i desa un punt d'interès en una ruta a iOS. També hi ha moltes millores a la interfície d'usuari, l'edició d'OpenStreetMap i diverses correccions d'errors a totes les plataformes, inclosa la correcció del bloqueig a l'inici en alguns dispositius Android.

Organic Maps és possible gràcies ❤️ als nostres col·laboradors, [les vostres donacions](@/donate/index.ca.md) i [el vostre suport](@/contribute/index.ca.md).

### Notes de llançament detallades (incloent els canvis de l'actualització menor anterior)

- NOU! Importació de GeoJSON (Sergiy Kozyr)
- Dades d'OpenStreetMap del 4 d'octubre
- Dades de Wikipedia de l'1 d'octubre
- Suport del tren lleuger de Seattle per al transport públic (tjasz)
- No desactivar la selecció del mapa en desar un lloc OSM editat (Kiryl Kaveryn)
- Traduccions actualitzades (col·laboradors de Weblate)

#### Estils de mapa

- Mostrar botigues de lloguer de bicicletes etiquetades com a amenity=bicycle + rental=shop (David Martinez)
- Mostrar llocs arqueològics històrics des del zoom 12 i altres llocs històrics des del zoom 15 en l'estil Exterior (Viktor Govako)
- Noves icones per a masts, comunicació i torres elèctriques en l'estil Exterior (David Martinez)
- Augmentar la mida de la icona de pic en l'estil Exterior (David Martinez)
- Afegir variants d'icones de PDI que faltaven (David Martinez)
- Afegits més tipus de barreres (Viktor Govako)

#### iOS

- NOU: Desar punt d'interès en el punt de ruta seleccionat (Kiryl Kaveryn)
- NOU: Suprimir la ruta de gravació sense desar-la primer (Kiryl Kaveryn)
- Mostrar títols de llista de punts d'interès de diverses línies a la Pàgina de lloc (David Martinez)
- Actualitzar l'estil dels botons d'inici de sessió d'OSM (Kiryl Kaveryn)
- Corregir problema d'actualització d'informació de navegació (Kiryl Kaveryn)
- Corregir problemes de planificació de noves rutes (Kiryl Kaveryn)
- Corregir la visibilitat d'afegir/editar lloc d'OSM per a mapes amb més de 3 mesos (Kiryl Kaveryn)
- Corregir el disseny del control de segment d'opcions de transport per a iOS 26 (Kiryl Kaveryn)
- Simplificar les animacions de selecció de punts d'interès (Kiryl Kaveryn)
- Corregir problema de selecció de resultats de cerca (Kiryl Kaveryn)
- Estil, lliscament i animacions corregits per a la Pàgina d'informació del lloc (Kiryl Kaveryn)

#### Android Auto (només Google Play)

- NOU: Visualització del límit de velocitat a Android Auto (Andrei Shkrob)
- Corregir el canvi de pantalla en el mode de navegació d'Android Auto (Andrei Shkrob)
- Corregir el desplaçament de la fletxa de ruta a Android Auto (Andrei Shkrob)
- Corregir problema quan un dispositiu es connecta/desconnecta d'un cotxe (Andrei Shkrob)
- Afegir servei d'ubicació d'Android Auto (Andrei Shkrob)
- Millorar el simulador de rutes d'Android Auto (Viktor Govako)

#### Android

- NOU: Veure estadístiques de gravació de rutes en temps real (Kavi Khalique)
- NOU: Mostrar el contingut de l'etiqueta `description` d'OSM (Alexander Borsuk)
- Corregir la gestió del canvi de tema (Andrei Shkrob)
- Corregits diversos bloquejos, inclòs el de l'inici (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Notificacions silencioses de progrés de descàrrega (Viktor Govako)
- Reduir el farciment de la icona de llapis (Alexander Borsuk)

#### Escriptori

- Corregir bloqueig de curl a Linux (Alexander Borsuk)
- Corregir bloqueig a macOS en iniciar sessió a OSM (Alexander Borsuk)
- Acció per seleccionar funció des del menú contextual (Viktor Govako)
- Opció per cancel·lar la descàrrega (Viktor Govako)
- Mostrar tipus de geometria al menú contextual (Viktor Govako)

### Funcions llançades recentment que podríeu haver perdut

- Números de ruta de transport públic en seleccionar una parada d'autobús
- Rutes de senderisme i ciclisme (activeu-les amb el botó Capes a l'extrem superior esquerre)
- Veure noms de punts d'interès al mapa activant-ho a la Configuració de l'aplicació
- La icona de llapis ✎ ofereix una manera ràpida d'editar punts d'interès

### Instal·lar Organic Maps

Obteniu l'última versió d'Organic Maps des de l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] i [F-Droid][fdroid].

Uniu-vos a les proves beta per a funcions primerenques: [iOS][testflight] / [Android][firebase].

{{ references() }}
