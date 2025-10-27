---
title: "Version du 23 octobre : Organic Maps comme application de navigation par défaut dans l'UE sur iOS, affichage des panneaux routiers sur Android, et plus d'améliorations et de corrections"
date: 2025-10-23T17:20:21+00:00
slug: "version-23-octobre-organic-maps-application-navigation-par-défaut-ue-ios-panneaux-routiers-android-améliorations-corrections"
taxonomies:
  news: ["Releases"]
---

Dans la version du 23 octobre, nous nous sommes concentrés sur les corrections et les améliorations. Consultez la liste détaillée ci-dessous.

Pour ceux qui l'ont manqué, la [mise à jour précédente du 7 octobre](https://organicmaps.app/news/2025-10-07/android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display/
) a ajouté l'import GeoJSON, les statistiques d'enregistrement de trace, l'affichage de la limite de vitesse dans Android Auto, l'affichage des balises de description OSM (tapez `?description` dans la zone de recherche pour les voir), la sauvegarde d'un signet sur une trace sur iOS et de nombreuses autres améliorations.

## Toutes les plateformes

- Données OpenStreetMap fraîches du 21 octobre 2025 (Viktor Govako)
- Afficher les noms des entrées/sorties de métro sur la carte (Viktor Govako)
- Nouveaux types et icônes de POI : stations de surveillance, îlots de circulation, installations de cure d'eau Kneipp, chemins de fer miniatures (Viktor Govako), emplacements de camping en style plein air, terminaux d'aéroport, aires de jeux intérieures, magasins de télécommunications, installations de location de bateaux, installations de cale de mise à l'eau, icônes mises à jour pour l'élimination des déchets et les décharges (David Martinez)
- Traductions de l'interface de l'application en slovène (Alexander Borsuk) et guidage vocal TTS pour la navigation (Erik Bucik)
- Sur certains appareils/écrans, la carte dans les centres-villes est maintenant moins encombrée (Viktor Govako)
- Correction des rotations de carte sur les mauvais capteurs de boussole lors de la marche en mode de navigation piétonne (Viktor Govako)
- Amélioration des informations affichées après la sélection d'une rivière ou d'un segment de voie navigable (Viktor Govako)
- Meilleure recherche de station de recharge EV avec des synonymes améliorés dans toutes les langues (Alexander Borsuk)
- Correction de la recherche d'emoji avec des sélecteurs de variantes (Alexander Borsuk)
- Correction de trop de résultats de recherche affichés pour certaines requêtes de correspondance d'adresse complète (Viktor Govako)
- L'importation de GeoJSON depuis https://umap.openstreetmap.fr/ devrait maintenant préserver toutes les métadonnées (Shubh Kesharwani)
- Des couleurs supplémentaires sont prises en charge pour les sentiers balisés pour la couche de carte des itinéraires de randonnée (Viktor Govako)

## iOS

- Les utilisateurs de l'UE peuvent définir Organic Maps comme application de navigation par défaut dans Réglages iOS → Apps → Apps par défaut → Navigation (Kiryl Kaveryn)
- Correction de la barre d'état blanc sur blanc en mode navigation (Kiryl Kaveryn)
- Augmentation de la taille du bouton Démarrer la navigation (Kiryl Kaveryn)
- Suppression de l'espace vide lors de la planification d'un itinéraire sur iPad (Kiryl Kaveryn)
- Organic Maps peut vous demander de l'évaluer dans l'App Store. Vos bons avis motivent notre équipe !

## Android

- Les panneaux routiers apparaissent maintenant dans les directions de navigation (Andrei Shkrob)
- Améliorations des informations d'enregistrement de trace (Kavi Khalique)
- Organic Maps fonctionne sur certains appareils Intel x86 plus anciens (Andrei Shkrob)
- Correction des directions vocales TTS ne fonctionnant pas dans certains cas (Andrei Shkrob)
- Meilleur écran de démarrage au lancement (Andrei Shkrob)

### Android Auto
- Restaurer l'itinéraire après annulation (Andrei Shkrob)
- Correction des plantages sur certains appareils (Andrei Shkrob)

## Linux/Mac OS

- Les détails de POI affichent maintenant le format « nom | ref » (Viktor Govako)
- le mode sombre se synchronise automatiquement avec les paramètres système (DeepChirp)

## Notes de bas de page

Organic Maps est possible grâce ❤️ à nos contributeurs, [vos dons](@/donate/index.fr.md) et [votre soutien](@/contribute/index.fr.md).

Obtenez la dernière version d'Organic Maps depuis l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] et [F-Droid][fdroid].

P.S. Rejoignez les tests bêta pour les fonctionnalités anticipées :
- [iOS][testflight]
- [Android][firebase].

Avec amour pour nos utilisateurs et notre communauté
L'équipe Organic Maps

{{ references() }}
