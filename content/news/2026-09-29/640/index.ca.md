---
title: "Optimització de la ruta, rutes alternatives millorades, ocultació de traces individuals i zones d’aigua intermitent a l’actualització de setembre de 2026"
date: 2026-09-29
slug: "optimitzacio-rutes-rutes-alternatives-amagar-traces-individuals-zones-aigua-intermitent-setembre-2026"
aliases: ["/ca/news/2026-09-29/seleccio-multiple-marcadors-traces-tauler-carplay-amagar-traces-enllacos-compartir-agost-2026/"]
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

A punt per sortir? L’actualització de setembre inclou rutes alternatives millorades, un ajust per optimitzar l’ordre de les parades de la ruta, marques més clares per a les zones d’aigua intermitent i una icona d’ull per amagar traces individuals, a més de moltes altres correccions i millores (mira més avall).

Instal·la o actualitza Organic Maps a través de <https://get.omaps.org>, l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] o [F-Droid][fdroid].

Si t’has perdut les nostres actualitzacions anteriors, fes un cop d’ull a les funcions publicades al [juny](@/news/2026-06-29/610/index.ca.md), al [juliol](@/news/2026-07-23/620/index.ca.md) i a l’[agost](@/news/2026-08-31/630/index.ca.md). Moltes gràcies als nostres col·laboradors i usuaris que han fet possibles aquestes actualitzacions!

## Com donar suport a Organic Maps

- [Fes una donació](@/donate/index.ca.md) per donar suport al desenvolupament i cobrir els costos d'allotjament del mapa
- [Envia els teus comentaris i contribueix](@/contribute/index.ca.md) al projecte
- Participa en les proves beta per provar les noves funcions abans que ningú i informar de problemes a [iOS][testflight], [Android][firebase] i [ordinadors][flathub]
- Fes córrer la veu i ajuda'ns a construir una alternativa millor als mapes de les grans tecnològiques!

## Notes de la versió

### Mapa

- Dades d'OpenStreetMap a 28 de setembre de 2026
- Dades de la Viquipèdia a 21 de setembre de 2026
- S'han corregit les cerques quan l'àrea visible del mapa creua el meridià 180° (±180° de longitud) _(Viktor Govako)_
- Les zones d’aigua intermitent ara es mostren amb un patró de punts, similar al que s'utilitza per a la sorra _(Alexander Borsuk)_
- Els embassaments ara són visibles quan s’allunya més la vista _(Alexander Borsuk)_
- Els túnels d'aigua ja no apareixen al mapa _(Alexander Borsuk)_
- S’han corregit les icones de les estacions i les entrades del metro de Suzhou _(Alexander Borsuk)_
- S'han corregit casos rars en què les etiquetes es desplaçaven de posició a la capa del mapa de metro _(Viktor Govako)_

### Rutes i navegació

- S’han millorat les rutes alternatives i les hores d’arribada previstes _(Alexander Borsuk, Viktor Govako)_
- La ruta alternativa seleccionada ara es conserva quan la navegació recalcula la ruta _(Alexander Borsuk)_
- Ara es recupera l’ordre de les parades de la ruta després de reiniciar l’aplicació _(Kiryl Kaveryn)_

### Altres millores

- Els horaris d’obertura ara mostren «Migdia» per a les 12:00 i «Mitjanit» per a les 00:00 o 24:00 _(Alexander Borsuk)_
- S’han corregit errors i s’ha millorat l’enregistrament de traces _(Alexander Borsuk)_
- S’ha corregit la importació de fitxers KMB _(Alexander Borsuk)_
- Traduccions corregides al francès i a l'asturià _(Alexander Borsuk)_
- S’ha corregit una errada tipogràfica en anglès _(Carl Morris)_

### iOS

- S’ha afegit una icona d’ull per amagar traces individuals _(Kiryl Kaveryn)_
- S'han afegit botons per afegir o substituir una parada en una ruta planificada _(Kiryl Kaveryn)_
- S’ha afegit un ajust per optimitzar l’ordre de les parades intermèdies de la ruta _(Kiryl Kaveryn)_
- S’han afegit indicacions de maniobra a les pantalles de projecció al parabrisa (HUD) compatibles dels cotxes i al tauler de CarPlay _(Kiryl Kaveryn)_
- S’han corregit els botons i la cerca de CarPlay _(Alexander Borsuk)_
- S'han corregit diversos errors i s'ha millorat la interfície d'usuari _(Kiryl Kaveryn, Alexander Borsuk)_
- S’ha afegit la possibilitat de triar una veu de navegació instal·lada i escoltar-ne una mostra _(Kiryl Kaveryn, Alexander Borsuk)_
- S'ha restablert la cerca per categoria a Spotlight _(Kiryl Kaveryn)_

### Android

- S’ha afegit un ajust per optimitzar l’ordre de les parades intermèdies de la ruta _(Mikhail Listratsenka)_
- S'han afegit botons per afegir o substituir una parada en una ruta planificada _(Mikhail Listratsenka)_
- S’ha afegit la possibilitat d’aturar l’enregistrament d’una traça i desar-la des de la notificació _(Alexander Borsuk)_
- El botó «Afegeix parada» ara afegeix una parada després de les parades existents, abans de la destinació _(Mikhail Listratsenka)_
- Millora de les pujades des de l'editor d'OpenStreetMap _(Owm)_
- S'ha actualitzat el disseny de la interfície d'usuari _(Mikhail Listratsenka)_
- L'editor de marcadors i altres diàlegs ara romanen oberts durant la navegació _(Mikhail Listratsenka)_
- S’ha corregit la representació del gràfic d’altitud per a traces planes i en interfícies de dreta a esquerra _(Mikhail Listratsenka)_
- S’ha corregit el problema que feia que les barres del sistema retallessin els botons del mapa _(Mikhail Listratsenka)_
- S'han corregit errors i s'ha millorat el suport per a Android Auto _(Andrei Shkrob)_
- S'ha solucionat una fallada durant el renderitzat de mapes _(Viktor Govako)_

### Escriptori

- S’han canviat els noms de l’executable d’escriptori i del paquet de l’aplicació per a macOS a `OrganicMaps` _(Alexander Borsuk)_
- S'han solucionat problemes a l'aplicació de Windows _(Osyotr, Alexander Borsuk)_
- L’argument de línia d’ordres `--lang` ara té prioritat sobre el paràmetre d’idioma de l’aplicació _(Alexander Borsuk)_

Amb alegria i passió,

El teu equip d’Organic Maps

{{ <references lang /> }}
