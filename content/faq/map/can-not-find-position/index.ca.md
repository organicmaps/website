---
title: L'aplicació no pot trobar la meva posició al mapa
slug: laplicació-no-pot-trobar-la-meva-posició-al-mapa
description: Guia de resolució de problemes per resoldre problemes amb la determinació
  de la ubicació per a dispositius iOS i Android
updated: '2024-06-20'
taxonomies:
  faq:
  - Map
extra:
  order: 10
aliases:
  - /ca/faq/map/can-not-find-position/
---

Assegureu-vos que el vostre dispositiu tingui GPS, que els serveis d'ubicació estiguin activats i que s'atorguin permisos d'ubicació a Organic Maps.

**Android**

Al dispositiu, obriu Configuració → Ubicació. És millor activar el mode d'alta precisió, ja que permet una ubicació GPS precisa.

Si el vostre dispositiu Android no pot determinar la vostra ubicació, activeu (o desactiveu, si està activat) l'opció "Google Play Services" a la configuració de l'aplicació.

Nota: només el podeu veure si teniu els serveis de Google Play instal·lats (activats) al vostre dispositiu Android. Els serveis de Google Play s'utilitzen per determinar la ubicació amb més precisió; si teniu problemes amb la precisió de la ubicació després d'haver desactivat l'opció, activeu-la.

**iOS**

Si sou un usuari d'iPhone o iPad, comproveu la configuració d'iOS → Privadesa → Serveis d'ubicació. L'ús compartit de dades de geolocalització s'hauria d'habilitar per als mapes orgànics.

**Notes:**

* Per evitar dades no desitjades durant la itinerància, podeu desactivar totes les dades mòbils, activar un mode de vol o desactivar les dades mòbils per als mapes orgànics a la configuració del dispositiu. Els dispositius Android i iOS poden utilitzar el GPS en mode vol.

* Alguns dispositius mòbils no tenen receptors GPS integrats, com ara l'iPod Touch, l'iPad només amb WiFi, Amazon Kindle Fire/Kindle Fire HD 7 i algunes tauletes Android. En aquests dispositius, totes les aplicacions mostraran la vostra ubicació aproximada detectada mitjançant una xarxa Wi-Fi, sempre que estigueu connectat a Internet.

* La detecció d'ubicació amb satèl·lits GPS (quan el WiFi i les xarxes mòbils estan desactivades) pot trigar una mica. Com més temps no s'ha utilitzat el GPS, més temps trigarà. La velocitat de detecció de la ubicació depèn del dispositiu, no de l'aplicació. El funcionament del GPS també està influenciat pel temps: funciona millor a l'aire lliure quan el cel està clar. Els problemes poden sorgir quan intenteu localitzar-vos a l'interior, en un carrer estret o quan conduïu un cotxe, amb molt de metall al voltant o amb un metall/imant a la carcassa del dispositiu.
