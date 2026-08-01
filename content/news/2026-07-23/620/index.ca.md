---
title: "Correccions d'errors i millores en el transport públic, les rutes, la cerca i els marcadors a l'actualització de juliol de 2026"
date: 2026-07-23
slug: "correccions-errors-millores-transport-public-rutes-cerca-marcadors-juliol-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Com potser ja ha notat, ja està disponible l'actualització de juliol d'Organic Maps. Obtingui-la a <https://get.omaps.org> o a [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] i [F-Droid][fdroid].

Gràcies a les seves [donacions](@/donate/index.ca.md) i als seus [comentaris](@/contribute/index.ca.md), al juliol ens vam centrar en correccions d'errors i millores. Per si s'ho va perdre, les funcions següents de l'[anterior llançament de juny](@/news/2026-06-29/610/index.ca.md) també estan disponibles:
- Rutes de transport públic (els horaris en directe estan en desenvolupament)
- Imatges per satèl·lit
- Rutes alternatives per a cotxe, senderisme i bicicleta
- Nova interfície de cerca i planificació d'itineraris per a Android
- Suport per a fonts d'accessibilitat de gran mida a iOS

## Registre de canvis detallat

### Mapa i llocs
- Dades d'OpenStreetMap actualitzades a 14 de juliol
- Les notes enviades a [OpenStreetMap](https://www.openstreetmap.org) ara es col·loquen exactament al lloc que ha seleccionat, en lloc del mig de tot el carrer o de la zona _(Alexander Borsuk)_
- Millora de la selecció de llocs en tocar el mapa a les regions que travessen l'antimeridià de 180° _(Viktor Govako)_
- Els perfils d'altitud de les traces ja no mostren gràfics obsolets o buits després d'eliminar una traça _(Kiryl Kaveryn)_

### Transport públic
- Els noms de parades, transbordaments i estacions ara tenen un contorn blanc per mantenir-se llegibles tant en temes clars com foscos _(Viktor Govako)_
- La capa del metro reapareix correctament després que tanqui la previsualització d'una ruta de transport públic _(Mikhail Listratsenka)_

### Rutes i navegació
- Els avisos de ruta (peatges, ferris, carreteres sense asfaltar, esglaons, etc.) ara es mostren per a totes les rutes alternatives _(Viktor Govako)_
- S'ha corregit un bloqueig poc freqüent en crear una ruta _(Viktor Govako)_
- Millora de la gestió dels carrers sense sortida i dels punts d'inici i final en vies restringides _(Viktor Govako)_
- Correcció d'instruccions de gir incorrectes i absents _(Alexander Borsuk)_

### iOS
- Nou paràmetre «Desa l'historial de cerques» que li permet desactivar l'historial i amagar-lo si prefereix no conservar-lo _(Kiryl Kaveryn)_
- Nou botó «Edita» per eliminar marcadors més fàcilment _(Kiryl Kaveryn)_
- Els marcadors ara es guarden automàticament quan surt de la pantalla _(Kiryl Kaveryn)_
- La paleta de colors ara ofereix colors predefinits i li permet triar qualsevol color personalitzat _(Kiryl Kaveryn)_
- S'ha millorat l'estat buit del gràfic d'altitud d'una traça enregistrada _(Kiryl Kaveryn)_
- S'ha millorat el progrés de la ruta que es mostra al botó «Inicia» _(Kiryl Kaveryn)_
- Reordenar les parades de la ruta ja no fa que la llista salti _(Kiryl Kaveryn)_
- Altres millores menors de la interfície _(Kiryl Kaveryn)_

### Android
- L'horari d'obertura ara mostra torns partits (com ara la pausa per dinar), comença pel dia actual i mostra tota la setmana sense una àrea de desplaçament a part _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Barra de cerca més neta amb un botó combinat d'esborrar i de veu, una icona d'esborrar que ja no es mou, i correccions de disposició per al mode horitzontal i la rotació del telèfon _(Mikhail Listratsenka)_
- Redisseny de l'editor de marcadors i de traces _(Mikhail Listratsenka)_
- Correccions i millores de la planificació d'itineraris _(Mikhail Listratsenka)_
- El selector de colors ara es tanca automàticament i s'ha solucionat un bloqueig a Android 5 _(Mikhail Listratsenka)_
- S'han corregit diverses fallades _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- La llista de mapes disponibles per a descarregar ja està ordenada alfabèticament _(goncalo109560)_

### Traduccions
- Millora de la redacció en xinès _(Chenxi Zhao)_
- Traduccions ucraïneses actualitzades _(Nnifria)_
- Correcció de les traduccions italianes dels noms de les regions del mapa _(Vittorio Bertola)_

## Uneixi's a les proves beta per provar funcions anticipades i informar de problemes:

Pista: la versió beta inclou un nou ombrejat del relleu, dades d'elevació millorades amb suport per a peus i metres, i altres funcions genials!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Bon estiu!
L'equip d'Organic Maps

{{ references() }}
