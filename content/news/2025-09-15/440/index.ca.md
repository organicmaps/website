---
title: "Llançament 15 de setembre: nova planificació de rutes i descripcions OSM"
date: 2025-09-15T10:00:00+00:00
---

Aquesta segona versió de setembre aporta una pantalla de planificació de rutes redissenyada i la possibilitat de veure el contingut de l’etiqueta `description` d’OpenStreetMap a iOS. Per trobar llocs amb aquesta etiqueta, escriu `?description` a la cerca (similar a `?wiki`).

També inclou moltes correccions i millores a iOS i Android (detalls a continuació).

Funcions recents que potser us heu perdut:
- Números de línia de transport públic en seleccionar una parada
- Rutes de senderisme i ciclisme (activeu-les amb el botó Capa a dalt a l’esquerra)
- Mostrar noms dels marcadors al mapa (activeu-ho a Configuració)
- La icona ✎ permet editar marcadors ràpidament

Organic Maps és possible gràcies als col·laboradors, [les vostres donacions](@/donate/index.ca.md) i [el vostre suport](@/contribute/index.md).

### Notes detallades

- Noves dades OpenStreetMap del 13 de setembre
- Eliminades illes molt petites del mapa mundial (Viktor Govako)
- Mostrar codi postal (ZIP) en els detalls de l’adreça (Viktor Govako)
- Centrat incorrecte del mapa a la posició actual corregit (Kiryl Kaveryn, Viktor Govako)
- Conservar colors dels marcadors en exportar/importar GPX (cyber-toad)
- Traduccions actualitzades (col·laboradors Weblate)

#### Estils de mapa (Viktor Govako)

- Mostrar botigues d’il·luminació
- Mostrar línies elèctriques des del zoom 18
- Mostrar referències de centrals i subestacions
- Mostrar càmpings i zones de caravanes en mode navegació
- Corregir el color de carreteres secundàries en mode navegació
- Dibuixar fronteres de parcs nacionals
- Dibuixar jaciments arqueològics des del zoom 12 en estil Outdoor

#### iOS

- NOU: mostrar contingut de l’etiqueta OSM `description` (cerca `?description`) (Kiryl Kaveryn, Viktor Govako)
- NOU: pantalla de planificació de rutes redissenyada (Kiryl Kaveryn)

#### Android

- Noves icones de rotonda a Android Auto (Andrei Shkrob)
- Mostrar categoria del marcador seleccionat (Alexander Borsuk)
- Corregit retard mostrant distància a un marcador (Alexander Borsuk)
- Tema fosc refet (Andrei Shkrob)
- Corregida actualització de posició en navegació en ROMs personalitzades (ex. Lineage + MicroG) (Viktor Govako)
- Icona de llapis blau (edició) per a marcadors (Alexander Borsuk)
- Reduïda alçada vertical de la previsualització d’informació del lloc (Alexander Borsuk)
- Eliminat angle d’azimut cap al nord de la previsualització (toqueu la fletxa blava amb la distància per veure’l) (Alexander Borsuk)

Descarregueu l’última versió: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Uniu-vos a la beta: [iOS][testflight] / [Android][firebase].

{{ references() }}
