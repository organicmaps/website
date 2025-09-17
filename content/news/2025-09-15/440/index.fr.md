---
title: "Version du 15 septembre : nouvel écran d’itinéraire et descriptions OSM"
date: 2025-09-15T10:00:00+00:00
---

Cette deuxième version de septembre apporte un écran de planification d’itinéraire repensé et l’affichage du contenu de la balise OpenStreetMap `description` sur iOS. Pour trouver les lieux qui possèdent cette balise, saisissez `?description` dans la recherche (similaire à `?wiki`).

Elle inclut aussi de nombreuses corrections et améliorations sur iOS et Android (détails ci‑dessous).

Fonctionnalités récentes que vous avez peut‑être manquées :
- Numéros de lignes de transport public lors de la sélection d’un arrêt
- Itinéraires de randonnée et de cyclisme (activez‑les via le bouton Couches en haut à gauche)
- Affichage des noms de marqueurs sur la carte (à activer dans Réglages)
- L’icône ✎ permet d’éditer rapidement les marqueurs

Organic Maps est possible grâce à nos contributeurs, [vos dons](@/donate/index.fr.md) et [votre soutien](@/contribute/index.md).

### Notes de version détaillées

- Nouvelles données OpenStreetMap au 13 septembre
- Suppression de très petites îles de la carte du monde (Viktor Govako)
- Affichage du code postal (ZIP) dans les détails d’adresse (Viktor Govako)
- Correction du centrage incorrect de la carte sur la position actuelle (Kiryl Kaveryn, Viktor Govako)
- Conservation des couleurs des marqueurs lors de l’export/import GPX (cyber-toad)
- Traductions mises à jour (contributeurs Weblate)

#### Styles de carte (Viktor Govako)

- Affichage des magasins d’éclairage
- Affichage des lignes électriques à partir du zoom 18
- Affichage des références des centrales et sous‑stations électriques
- Affichage des campings et aires pour caravanes en mode navigation
- Correction de la couleur des routes secondaires en mode navigation
- Tracé des frontières des parcs nationaux
- Tracé des sites archéologiques à partir du zoom 12 dans le style Outdoor

#### iOS

- NOUVEAU : affichage du contenu de la balise OSM `description` (recherche `?description`) (Kiryl Kaveryn, Viktor Govako)
- NOUVEAU : écran de planification d’itinéraire repensé (Kiryl Kaveryn)

#### Android

- Nouveaux icônes de rond‑point dans Android Auto (Andrei Shkrob)
- Affichage de la catégorie du marqueur sélectionné (Alexander Borsuk)
- Correction du délai d’affichage de la distance vers un marqueur (Alexander Borsuk)
- Refonte du thème sombre (Andrei Shkrob)
- Correction de la mise à jour de position en navigation sur ROM personnalisée (ex. Lineage + MicroG) (Viktor Govako)
- Icône crayon bleu (édition) pour les marqueurs (Alexander Borsuk)
- Réduction de la hauteur verticale de l’aperçu d’information lieu (Alexander Borsuk)
- Suppression de l’angle d’azimut vers le nord dans l’aperçu (toucher la flèche bleue avec la distance pour le voir) (Alexander Borsuk)

Téléchargez la dernière version : [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Rejoignez la bêta : [iOS][testflight] / [Android][firebase].

{{ references() }}
