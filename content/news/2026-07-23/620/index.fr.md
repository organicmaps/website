---
title: "Corrections de bugs et améliorations concernant les transports en commun, le calcul d’itinéraires, la recherche et les signets dans la mise à jour de juillet 2026"
date: 2026-07-23
slug: "corrections-bugs-ameliorations-transports-publics-itineraires-recherche-signets-juillet-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Comme tu l’as peut-être déjà remarqué, la mise à jour de juillet d’Organic Maps est disponible. Tu peux la télécharger sur <https://get.omaps.org> ou sur [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] et [F-Droid][fdroid].

Grâce à tes [dons](@/donate/index.fr.md) et à tes [commentaires](@/contribute/index.fr.md), nous nous sommes concentrés en juillet sur la correction de bugs et l’apport d’améliorations. Au cas où tu l’aurais manqué, les fonctionnalités suivantes de la [version précédente de juin](@/news/2026-06-29/610/index.fr.md) sont également disponibles :
- Itinéraires en transports en commun (les horaires en temps réel sont en cours d’élaboration)
- Images satellites
- Itinéraires alternatifs pour la voiture, la randonnée et le vélo
- Nouvelle interface de recherche et de calcul d’itinéraire pour Android
- Prise en charge des polices de grande taille pour l’accessibilité sur iOS

## Journal des modifications détaillé

### Carte et lieux

- Données OpenStreetMap mises à jour au 14 juillet
- Les notes signalées à [OpenStreetMap](https://www.openstreetmap.org) sont désormais placées à l’endroit précis que tu as sélectionné, et non plus au milieu de la rue ou de la zone concernée _(Alexander Borsuk)_
- Amélioration de la sélection des lieux lorsque l’on appuie sur la carte dans les régions qui traversent l’antiméridien de 180° _(Viktor Govako)_
- Les profils d’altitude des traces n’affichent plus de graphiques obsolètes ou vides après la suppression d’une trace _(Kiryl Kaveryn)_

### Transports en commun

- Les noms des arrêts, des correspondances et des stations sont désormais entourés d’un contour blanc afin de rester lisibles aussi bien avec le thème clair qu’avec le thème sombre _(Viktor Govako)_
- La couche « Métro » s’affiche à nouveau correctement une fois que tu as fermé l’aperçu d’un itinéraire en transports en commun _(Mikhail Listratsenka)_

### Itinéraires et navigation

- Les avertissements relatifs à l’itinéraire (péages, ferries, routes non goudronnées, marches, etc.) s’affichent désormais pour tous les itinéraires alternatifs _(Viktor Govako)_
- Correction d’un blocage rare lors de la création d’un itinéraire _(Viktor Govako)_
- Amélioration de la gestion des impasses ainsi que des points de départ et d’arrivée sur les routes à circulation restreinte _(Viktor Govako)_
- Correction des instructions de virage erronées ou manquantes _(Alexander Borsuk)_

### iOS

- Nouveau paramètre « Enregistrer l’historique de recherche » qui te permet de désactiver l’historique et de le masquer si tu préfères ne pas le conserver _(Kiryl Kaveryn)_
- Nouveau bouton « Modifier » pour supprimer plus facilement les signets _(Kiryl Kaveryn)_
- Les signets sont désormais enregistrés automatiquement lorsque tu quittes l’écran _(Kiryl Kaveryn)_
- La palette de couleurs propose désormais des couleurs prédéfinies et te permet de choisir n’importe quelle couleur personnalisée _(Kiryl Kaveryn)_
- Amélioration de l’état vide du graphique d’altitude pour une trace enregistrée _(Kiryl Kaveryn)_
- Amélioration de l’affichage de la progression de l’itinéraire sur le bouton « Démarrer » _(Kiryl Kaveryn)_
- Le réordonnancement des arrêts d’un itinéraire ne provoque plus de sauts dans la liste _(Kiryl Kaveryn)_
- Autres améliorations mineures de l’interface _(Kiryl Kaveryn)_

### Android

- Les horaires d’ouverture indiquent désormais les horaires coupés (comme la pause déjeuner), commencent au jour actuel et affichent toute la semaine sans zone de défilement distincte _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Une barre de recherche plus épurée, dotée d’un bouton combiné « Effacer » et « Commande vocale », d’une icône « Effacer » qui ne bouge plus, ainsi que de corrections de mise en page en mode paysage et après la rotation du téléphone _(Mikhail Listratsenka)_
- Éditeur de signets et de traces remanié _(Mikhail Listratsenka)_
- Corrections et améliorations apportées au calcul d’itinéraire _(Mikhail Listratsenka)_
- Le sélecteur de couleur se ferme désormais automatiquement, et un plantage sous Android 5 a été corrigé _(Mikhail Listratsenka)_
- Correction de plantages _(Alexander Borsuk, Mikhail Listratsenka)_

### Bureau

- La liste des cartes disponibles au téléchargement est désormais classée par ordre alphabétique _(goncalo109560)_

### Traductions

- Formulation chinoise améliorée _(Chenxi Zhao)_
- Traductions en ukrainien mises à jour _(Nnifria)_
- Correction des traductions en italien des noms des régions de la carte _(Vittorio Bertola)_

## Rejoins le bêta-test pour essayer les premières fonctionnalités et signaler les problèmes :

Astuce : la version bêta propose un nouvel ombrage du relief, des données altimétriques améliorées avec prise en charge des pieds et des mètres, ainsi que d’autres fonctionnalités sympas !

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Bon été !
L’équipe Organic Maps

{{ references() }}
