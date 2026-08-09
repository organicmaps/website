---
title: "L'aplicació no pot trobar la meva posició al mapa o mostra una ubicació incorrecta"
slug: laplicació-no-pot-trobar-la-meva-posició-al-mapa
description: "Guia de resolució de problemes per solucionar problemes amb la ubicació i la posició GPS actual al mapa per a dispositius iOS i Android"
updated: "2026-01-04"
taxonomies:
  faq:
  - map
extra:
  order: 10
aliases:
  - /ca/faq/map/can-not-find-position/
---

Assegura't que el teu dispositiu tingui GPS, que els serveis d'ubicació estiguin activats i que s'atorguin permisos d'ubicació a Organic Maps.

**Android**

Al dispositiu, obre Configuració → Ubicació. És millor activar el mode d'alta precisió, ja que permet una ubicació GPS precisa.

Si el teu dispositiu Android no pot determinar la teva ubicació, activa (o desactiva, si està activat) l'opció «Google Play Services» a la configuració de l'aplicació.

Nota: només el pots veure si tens els serveis de Google Play instal·lats (activats) al teu dispositiu Android. Els serveis de Google Play s'utilitzen per determinar la ubicació amb més precisió; si tens problemes amb la precisió de la ubicació després d'haver desactivat l'opció, activa-la.

**iOS**

Si ets un usuari d'iPhone o iPad, comprova la configuració d'iOS → Privadesa → Serveis d'ubicació. L'ús compartit de dades de geolocalització s'hauria d'habilitar per a Organic Maps.

**Es mostra una ubicació incorrecta al mapa**

1. Si hi ha un gran cercle semitransparent al voltant de la fletxa de la teva ubicació al mapa, significa que la teva posició es determina amb poca precisió, utilitzant WiFi o connexió mòbil. Assegura't que has activat la precisió de la ubicació «Precisa» per a Organic Maps a la configuració del sistema i prova de sortir a l'exterior, lluny d'edificis alts i arbres, per millorar la recepció del senyal GPS per satèl·lit.

2. Si la teva posició es determina incorrectament (per exemple, ets a una ciutat, però l'aplicació mostra una altra ciutat), és molt probable que et trobis en una zona afectada per un senyal GPS fals (suplantació de GPS) a causa de mesures de guerra electrònica (EW). En aquests casos, l'única solució és moure's a una altra ubicació.

**Notes:**

* Per evitar dades no desitjades durant la itinerància, pots desactivar totes les dades mòbils, activar un mode de vol o desactivar les dades mòbils per a Organic Maps a la configuració del dispositiu. Els dispositius Android i iOS poden utilitzar el GPS en mode vol.

* Alguns dispositius mòbils no tenen receptors GPS integrats, com ara l'iPod Touch, l'iPad només amb WiFi, Amazon Kindle Fire/Kindle Fire HD 7 i algunes tauletes Android. En aquests dispositius, totes les aplicacions mostraran la teva ubicació aproximada detectada mitjançant una xarxa Wi-Fi, sempre que estiguis connectat a Internet.

* La detecció d'ubicació amb satèl·lits GPS (quan el WiFi i les xarxes mòbils estan desactivades) pot trigar una mica. Com més temps no s'ha utilitzat el GPS, més temps trigarà. La velocitat de detecció de la ubicació depèn del dispositiu, no de l'aplicació. El funcionament del GPS també està influenciat pel temps: funciona millor a l'aire lliure quan el cel està clar. Els problemes poden sorgir quan intentes localitzar-te a l'interior, en un carrer estret o quan condueixes un cotxe, amb molt de metall al voltant o amb un metall/imant a la carcassa del dispositiu.
