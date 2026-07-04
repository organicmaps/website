---
title: "Imagerie satellite, itinéraires de transport public, itinéraires alternatifs, nouvelle interface de recherche et de planification d’itinéraires pour Android, prise en charge des grandes polices d’accessibilité sur iOS, et plus encore dans la mise à jour de juin 2026"
date: 2026-06-29
slug: "imagerie-satellite-itineraires-transport-public-itineraires-alternatifs-nouvelle-recherche-planification-android-grandes-polices-ios-juin-2026"
taxonomies:
  news: ["releases"]
---

La mise à jour de juin d’Organic Maps apporte plein de nouvelles fonctionnalités intéressantes et corrections de bugs à essayer, notamment :
- Imagerie satellite
- Itinéraires de transport public
- Itinéraires alternatifs
- Nouvelle interface de recherche et de planification d’itinéraires pour Android
- Prise en charge des grandes polices d’accessibilité sur iOS

Obtiens-la sur <https://get.omaps.org> ou dans l’[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] et [F-Droid][fdroid], et dis-nous ce que tu en penses !

## Journal des modifications détaillé

- NOUVEAU ! Calcul d’itinéraires en transport public par métro, métro léger, bus et tramway _(Viktor Govako)_
- NOUVEAU ! Itinéraires alternatifs : en plus de l’itinéraire le plus rapide, l’app affiche maintenant l’itinéraire le plus court _(Viktor Govako)_
- NOUVEAU ! Avertissements sur les escaliers, portails et barrières levantes le long des itinéraires à pied et à vélo _(Viktor Govako)_
- NOUVEAU ! Choisis n’importe quelle couleur pour les signets _(Alexander Borsuk, Mikhail Listratsenka)_
- NOUVEAU ! Prise en charge des coordonnées British National Grid (OS Grid), Irish Grid et Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPÉRIMENTAL : active l’imagerie satellite dans les paramètres d’Organic Maps avec l’URL personnalisée d’un serveur de tuiles raster. Nous travaillons encore sur notre propre serveur ; trouve donc un serveur librement accessible contenant les paramètres `{x}`, `{y}`, `{z}` dans son URL _(Viktor Govako, renderexpert)_
- Données OpenStreetMap mises à jour au 24 juin _(Viktor Govako)_
- Données Wikipedia mises à jour au 20 juin, y compris les articles en italien _(Alexander Borsuk)_
- Saisis `?map-download-server:https://your-server.com/` dans la fenêtre de recherche pour remplacer les serveurs de téléchargement de cartes d’Organic Maps. Saisis `?no-map-download-server` pour supprimer ce remplacement _(Alexander Borsuk)_

#### Rendu et styles de carte

- Motifs plus esthétiques pour les plages, le sable, les éboulis, la roche nue, les vergers et les vignobles, avec hachures pour les zones protégées et les zones humides _(Alexander Borsuk)_
- Libellés de texte courbes plus fluides pour les routes et les rivières _(Viktor Govako)_
- Les rivières, ruisseaux et zones humides ont un contraste plus élevé et sont plus visibles en mode sombre _(Alexander Borsuk)_
- Icônes nouvelles et améliorées pour la recherche par catégorie et les résultats de recherche sur la carte _(Anton Makouski)_
- Amélioration de la composition et du rendu du texte multilingue _(Alexander Borsuk)_
- Divers correctifs et améliorations des performances _(Viktor Govako)_

#### Traces, signets et itinéraires

- Les traces GeoJSON conservent désormais l’altitude et les horodatages à l’importation et à l’exportation _(Alexander Borsuk)_
- Correction d’un plantage après le déplacement d’une trace vers une autre liste _(Viktor Govako)_
- Les sites web sont maintenant affichés pour les sites patrimoniaux _(Viktor Govako)_
- Les noms d’opérateurs sont maintenant affichés pour les résultats de recherche sans nom. Par exemple, un distributeur automatique sans nom affiche maintenant sa banque _(Anton Makouski)_
- Éditeur : correction du texte de description pour les modifications/changesets OpenStreetMap concernant les immeubles d’appartements _(titanniya542-spec)_
- Meilleure détection du HTML dans les descriptions de signets et de traces _(Alexander Borsuk)_

### iOS

- NOUVEAU ! Prise en charge de l’accessibilité pour Dynamic Type et les grandes polices _(Kiryl Kaveryn)_
- NOUVEAU ! Touche pour choisir entre des traces et des itinéraires qui se superposent _(Kiryl Kaveryn)_
- Meilleur rendu HTML des descriptions de signets et de traces _(Kiryl Kaveryn)_
- Style de tableaux plus clair dans l’interface _(Kiryl Kaveryn)_

### Android

- NOUVEAU ! Interface de recherche _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NOUVEAU ! Interface de planification d’itinéraires _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Meilleur rendu HTML des descriptions de signets et de traces _(Mikhail Listratsenka)_
- Taille de l’APK réduite _(Alexander Borsuk)_
- L’icône vocale est affichée comme désactivée lorsqu’aucun moteur de synthèse vocale n’est disponible _(Mikhail Listratsenka)_
- Les longues descriptions de signets et de traces affichent maintenant un bouton « …plus » _(Mikhail Listratsenka)_
- Divers correctifs d’interface et un correctif d’API pour les ID de points renvoyés _(Mikhail Listratsenka)_

### Bureau

- Prise en charge du changement du système de coordonnées affiché _(Alexander Borsuk)_
- Les informations sur le lieu sélectionné sont maintenant affichées à gauche _(Viktor Govako)_
- Correction de la position du menu contextuel _(Osyotr)_
- Correction du blocage de la connexion et des modifications OpenStreetMap avec Qt 6.4 et versions antérieures _(Alexander Borsuk)_
- Correction d’un changement inattendu de style de carte pendant le guidage sur macOS _(Alexander Borsuk)_
- Correction d’un plantage à la fermeture de l’app macOS après l’exportation d’un fichier KMZ _(Alexander Borsuk)_

### Traductions

- Guidage vocal virage par virage en cantonais _(Alexander Borsuk)_
- Traductions allemandes et françaises mises à jour _(Wuzzy, Alexander Borsuk)_
- Correction de traductions incorrectes du guidage vocal « onto street » pour le chinois, le serbe et le catalan _(Alexander Borsuk)_

## Rejoins le bêta-test pour essayer les premières fonctionnalités et signaler les problèmes :

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Nous remercions tous nos utilisateurs et contributeurs, toutes celles et ceux qui [font un don](@/donate/index.fr.md) et donnent 5 étoiles à Organic Maps dans les boutiques d’apps. Ensemble, nous pouvons créer la meilleure app de cartes !

Avec amour,
L’équipe Organic Maps

{{ references() }}
