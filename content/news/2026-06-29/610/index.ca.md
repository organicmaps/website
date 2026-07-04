---
title: "Imatges de satèl·lit, rutes de transport públic, rutes alternatives, nova interfície de cerca i de planificació de rutes per a Android, suport de fonts grans d'accessibilitat per a iOS i més a l'actualització de juny de 2026"
date: 2026-06-29
slug: "imatges-satelit-rutes-transport-public-rutes-alternatives-nova-interficie-cerca-planificacio-rutes-android-fonts-grans-accessibilitat"
taxonomies:
  news: ["releases"]
---

Hi ha moltes funcions noves interessants i correccions d'errors a l'actualització de juny d'Organic Maps per provar, incloent-hi:
- Imatges de satèl·lit
- Rutes de transport públic
- Rutes alternatives
- Nova interfície de cerca i de planificació de rutes per a Android
- Suport de fonts grans d'accessibilitat per a iOS

Aconsegueix-la a <https://get.omaps.org> o a l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] i [F-Droid][fdroid], i digues-nos què en penses!

## Registre de canvis detallat

- NOU! Rutes de transport públic amb metro, tren lleuger, autobús i tramvia _(Viktor Govako)_
- NOU! Rutes alternatives: a més de la ruta més ràpida, l'aplicació ara mostra la ruta més curta _(Viktor Govako)_
- NOU! Avisos a les rutes a peu i en bicicleta sobre escales, portes i barreres de pas elevables al llarg del camí _(Viktor Govako)_
- NOU! Tria qualsevol color per als marcadors _(Alexander Borsuk, Mikhail Listratsenka)_
- NOU! Suport per a coordenades British National Grid (OS Grid), Irish Grid i Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTAL: Activa les imatges de satèl·lit a la configuració d'Organic Maps amb un URL personalitzat de servidor de tessel·les ràster. Encara estem treballant en el nostre propi servidor; per tant, cerca'n un de disponible obertament amb els marcadors de posició `{x}`, `{y}`, `{z}` a l'URL _(Viktor Govako, renderexpert)_
- Dades d'OpenStreetMap actualitzades a data del 24 de juny _(Viktor Govako)_
- Dades de Wikipedia actualitzades a data del 20 de juny, incloent-hi articles en italià _(Alexander Borsuk)_
- Escriu `?map-download-server:https://your-server.com/` a la finestra de cerca per substituir els servidors de descàrrega de mapes d'Organic Maps. Escriu `?no-map-download-server` per eliminar la substitució _(Alexander Borsuk)_

#### Renderització i estils del mapa

- Patrons amb millor aspecte per a zones de platja, sorra, tartera, roca nua, verger i vinya, a més del ratllat d'àrees protegides i aiguamolls _(Alexander Borsuk)_
- Etiquetes de text corbes més suaus per a carreteres i rius _(Viktor Govako)_
- Rius, rieres i aiguamolls tenen més contrast i són més visibles en mode fosc _(Alexander Borsuk)_
- Icones noves i millorades per a la cerca per categories i els resultats de cerca al mapa _(Anton Makouski)_
- S'ha millorat la composició i renderització de text multilingüe _(Alexander Borsuk)_
- Diverses correccions d'errors i millores de rendiment _(Viktor Govako)_

#### Traces, marcadors i rutes

- Les traces GeoJSON ara conserven l'altitud i les marques de temps en importar-les i exportar-les _(Alexander Borsuk)_
- S'ha corregit un bloqueig després de moure una traça a una altra llista _(Viktor Govako)_
- Ara es mostren els llocs web dels llocs patrimonials _(Viktor Govako)_
- Ara es mostren els noms dels operadors per als resultats de cerca sense nom. Per exemple, un caixer automàtic sense nom ara mostra el seu banc _(Anton Makouski)_
- Editor: s'ha corregit el text de descripció per a les edicions/conjunts de canvis d'edificis d'apartaments a OpenStreetMap _(titanniya542-spec)_
- S'ha millorat la detecció d'HTML a les descripcions de marcadors i traces _(Alexander Borsuk)_

### iOS

- NOU! Suport d'accessibilitat per a Dynamic Type i fonts grans _(Kiryl Kaveryn)_
- NOU! Toca per triar entre traces i rutes superposades _(Kiryl Kaveryn)_
- S'ha millorat la renderització HTML de les descripcions de marcadors i traces _(Kiryl Kaveryn)_
- Estil de taules més net a la interfície d'usuari _(Kiryl Kaveryn)_

### Android

- NOU! Interfície de cerca _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NOU! Interfície de planificació de rutes _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- S'ha millorat la renderització HTML de les descripcions de marcadors i traces _(Mikhail Listratsenka)_
- S'ha reduït la mida de l'APK _(Alexander Borsuk)_
- La icona de veu es mostra desactivada quan no hi ha cap motor de text a veu disponible _(Mikhail Listratsenka)_
- Les descripcions llargues de marcadors i traces ara mostren un botó «…més» _(Mikhail Listratsenka)_
- Diverses correccions de la interfície d'usuari i una correcció de l'API per als identificadors de punts retornats _(Mikhail Listratsenka)_

### Desktop

- Suport per canviar el sistema de coordenades mostrat _(Alexander Borsuk)_
- Ara la informació sobre el lloc seleccionat es mostra a l'esquerra _(Viktor Govako)_
- S'ha corregit la posició del menú contextual _(Osyotr)_
- S'ha corregit que l'inici de sessió i les edicions d'OpenStreetMap es quedessin penjats a Qt 6.4 i versions anteriors _(Alexander Borsuk)_
- S'ha corregit el canvi inesperat d'estil del mapa durant el càlcul de rutes a macOS _(Alexander Borsuk)_
- S'ha corregit un bloqueig en tancar l'aplicació de macOS després d'exportar un fitxer KMZ _(Alexander Borsuk)_

### Traduccions

- Indicacions de veu pas a pas en cantonès _(Alexander Borsuk)_
- Traduccions a l'alemany i al francès actualitzades _(Wuzzy, Alexander Borsuk)_
- S'han corregit les traduccions incorrectes de les indicacions de veu «onto street» per al xinès, el serbi i el català _(Alexander Borsuk)_

## Uneix-te a les proves beta per provar funcions anticipades i informar de problemes:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Agraïm a tots els nostres usuaris i col·laboradors, a tots els qui [fan donacions](@/donate/index.ca.md) i donen 5 estrelles a Organic Maps a les botigues d'aplicacions. Junts podem crear la millor aplicació de mapes!

Amb afecte,
L'equip d'Organic Maps

{{ references() }}
