---
title: "Version d'octobre : Limites de vitesse sur Android Auto, importation GeoJSON, statistiques d'enregistrement de parcours, affichage de la balise de description OSM, enregistrer un signet sur la trace sélectionnée sur iOS, et plus encore"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
---

Cette mise à jour d'octobre d'Organic Maps ajoute l'affichage de la limite de vitesse dans Android Auto, l'importation de GeoJSON, les statistiques d'enregistrement de parcours, affiche les balises de description OSM (tapez `?description` dans la zone de recherche pour les voir), et enregistre un signet sur une trace sur iOS. Il y a également de nombreuses améliorations de l'interface utilisateur, de l'édition OpenStreetMap et diverses corrections de bogues sur toutes les plateformes, y compris la correction du plantage au démarrage sur certains appareils Android.

Organic Maps est possible grâce ❤️ à nos contributeurs, [vos dons](@/donate/index.fr.md) et [votre soutien](@/contribute/index.fr.md).

### Notes de version détaillées (y compris les modifications de la mise à jour mineure précédente)

- NOUVEAU ! Importation GeoJSON (Sergiy Kozyr)
- Données OpenStreetMap au 4 octobre
- Données Wikipédia au 1er octobre
- Prise en charge du train léger de Seattle pour les transports publics (tjasz)
- Ne pas désactiver la sélection de carte lors de l'enregistrement d'un lieu OSM modifié (Kiryl Kaveryn)
- Traductions mises à jour (contributeurs Weblate)

#### Styles de carte

- Afficher les magasins de location de vélos tagués comme amenity=bicycle + rental=shop (David Martinez)
- Afficher les sites archéologiques historiques à partir du zoom 12 et les autres sites historiques à partir du zoom 15 dans le style Extérieur (Viktor Govako)
- Nouvelles icônes pour les mâts, les communications et les tours électriques dans le style Extérieur (David Martinez)
- Augmenter la taille de l'icône de sommet dans le style Extérieur (David Martinez)
- Ajouter des variantes d'icônes de POI manquantes (David Martinez)
- Ajout de types de barrières supplémentaires (Viktor Govako)

#### iOS

- NOUVEAU : Enregistrer un signet sur le point de trace sélectionné (Kiryl Kaveryn)
- NOUVEAU : Supprimer la trace d'enregistrement sans l'enregistrer d'abord (Kiryl Kaveryn)
- Afficher les titres de liste de signets sur plusieurs lignes dans la page de lieu (David Martinez)
- Mise à jour du style des boutons de connexion OSM (Kiryl Kaveryn)
- Correction du problème de mise à jour des informations de navigation (Kiryl Kaveryn)
- Correction des problèmes de planification de nouvel itinéraire (Kiryl Kaveryn)
- Correction de la visibilité d'ajout/modification de lieu OSM pour les cartes de plus de 3 mois (Kiryl Kaveryn)
- Correction de la mise en page du contrôle de segment des options de transport pour iOS 26 (Kiryl Kaveryn)
- Simplification des animations de sélection de signets (Kiryl Kaveryn)
- Correction du problème de sélection des résultats de recherche (Kiryl Kaveryn)
- Style, balayage et animations corrigés pour la page d'information du lieu (Kiryl Kaveryn)

#### Android Auto (Google Play uniquement)

- NOUVEAU : Affichage de la limite de vitesse dans Android Auto (Andrei Shkrob)
- Correction du changement d'affichage en mode navigation Android Auto (Andrei Shkrob)
- Correction du décalage de la flèche d'itinéraire dans Android Auto (Andrei Shkrob)
- Correction du problème lorsqu'un appareil est connecté/déconnecté à une voiture (Andrei Shkrob)
- Ajout du service de localisation Android Auto (Andrei Shkrob)
- Amélioration du simulateur d'itinéraire Android Auto (Viktor Govako)

#### Android

- NOUVEAU : Voir les statistiques d'enregistrement de parcours en temps réel (Kavi Khalique)
- NOUVEAU : Afficher le contenu de la balise `description` OSM (Alexander Borsuk)
- Correction de la gestion du changement de thème (Andrei Shkrob)
- Correction de plusieurs plantages, y compris celui au démarrage (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Notifications de progression de téléchargement silencieuses (Viktor Govako)
- Réduction de l'espace autour de l'icône de crayon (Alexander Borsuk)

#### Bureau

- Correction du blocage de curl sur Linux (Alexander Borsuk)
- Correction du blocage sur macOS lors de la connexion à OSM (Alexander Borsuk)
- Action pour sélectionner une fonction depuis le menu contextuel (Viktor Govako)
- Option pour annuler le téléchargement (Viktor Govako)
- Afficher le type de géométrie dans le menu contextuel (Viktor Govako)

### Fonctionnalités récemment publiées que vous avez peut-être manquées

- Numéros de ligne de transport public lors de la sélection d'un arrêt de bus
- Itinéraires de randonnée et de vélo (activez-les via le bouton Calques en haut à gauche)
- Voir les noms de signets sur la carte en l'activant dans les paramètres de l'application
- L'icône de crayon ✎ offre un moyen rapide de modifier les signets

### Installer Organic Maps

Obtenez la dernière version d'Organic Maps depuis l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] et [F-Droid][fdroid].

Rejoignez les tests bêta pour les fonctionnalités précoces : [iOS][testflight] / [Android][firebase].

{{ references() }}
