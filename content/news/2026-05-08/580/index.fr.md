---
title: "Touchez un arrêt de transport en commun pour afficher les lignes sur la carte, les étiquettes des signets ne se chevauchent plus, des régions téléchargeables plus petites au Vietnam, en Malaisie et dans le sud de la Chine dans la mise à jour de mai d'Organic Maps"
date: 2026-05-08
slug: "selection-arret-transport-lignes-etiquettes-signets-sans-chevauchement-vietnam-malaisie-chine-regions-divisees"
taxonomies:
  news: ["releases"]
---

La mise à jour de mai nous rapproche un peu plus d'une prise en charge complète des transports en commun dans Organic Maps. Un arrêt de bus, de train, de ferry ou de tramway donne accès aux lignes qui le desservent : ainsi, lorsque vous touchez une ligne depuis un arrêt, elle s'affiche désormais dans sa propre couleur sur toute la carte. Les horaires réels en ligne arrivent aussi ; n'oubliez pas d'[ajouter ou de mettre à jour les données OSM relatives aux transports en commun](https://gtfs-osm-matcher.organicmaps.app/) dans votre région si ce n'est pas déjà fait !

Comme toujours, un grand merci à nos contributeurs, ainsi qu'à vous pour vos avis positifs, [vos dons](@/donate/index.fr.md) et [votre soutien](@/contribute/index.fr.md).

Téléchargez la mise à jour de mai sur <https://get.omaps.org> ou sur l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] et [F-Droid][fdroid].

## Points forts

- **Touchez un arrêt de bus, de tramway, de train ou de ferry sur la carte,** et Organic Maps met en évidence toute la ligne de transport en commun, sélectionnable dans la liste des lignes et itinéraires affichés.
- **Des étiquettes de signets plus nettes et une carte plus lisible.** Le nouveau placement des étiquettes évite que les titres des signets ne se chevauchent, les zones piétonnes sont légèrement plus sombres et les couleurs des itinéraires ont été ajustées pour offrir un meilleur contraste, sur les thèmes clairs comme sombres.
- **Des régions plus détaillées en Asie.** Le Vietnam et la Malaisie sont désormais divisés en cartes plus petites afin que vous puissiez télécharger uniquement la zone dont vous avez besoin, et Hong Kong, Macao et Hainan sont désormais séparés du Guangdong.

## Notes de mise à jour

### Toutes les plateformes

- NOUVEAU ! Touchez un arrêt de transport en commun et sélectionnez un numéro de ligne pour mettre en évidence tout l'itinéraire de cette ligne sur la carte, comme dans le calque « Plan du métro » (Viktor Govako, Kiryl Kaveryn, Mikhail Listratsenka)
- NOUVEAU ! Les étiquettes des signets sur la carte ne se chevauchent plus (Viktor Govako)
- Correction des calculs de dénivelé positif et négatif sur les graphiques d'altitude des traces afin de mieux correspondre aux valeurs fournies par d'autres applications populaires (Viktor Govako)
- Les transports en commun longue distance et d'autres relations cartographiques sont désormais raccordés au-delà des limites des cartes pour former une seule ligne continue (Viktor Govako)
- Le Vietnam et la Malaisie ont été divisés en régions plus petites, téléchargeables séparément (Viktor Govako)
- Hong Kong, Macao et Hainan sont désormais distincts du Guangdong, et les frontières avec les régions voisines ont été mises à jour (Viktor Govako)
- Mise à jour des isolignes (courbes de niveau) pour l'Indonésie, la Malaisie, la Tanzanie, la Thaïlande et le Vietnam (Viktor Govako)
- Itinéraires : les itinéraires repris ignorent désormais les points intermédiaires que vous avez déjà dépassés (Viktor Govako)
- Ajout d'icônes pour les volcans actifs et les points d'accès aux voies navigables ; les cales de mise à l'eau peuvent désormais être recherchées (David Martinez)
- Ajout des salons de narguilé (alnzrv)
- Ajout des bâtiments en construction (Viktor Govako)
- Ajout de « Lookout » comme synonyme de recherche pour les points de vue (alnzrv)
- Ajout de « pkwy » comme synonyme de rue aux États-Unis (Viktor Govako)
- Les couleurs des zones piétonnes ont été légèrement assombries pour une meilleure lisibilité (Viktor Govako)
- Le texte sur plusieurs lignes est désormais correctement tronqué sur la carte (Viktor Govako)
- Les noms de rue ne comportent plus de répétitions (Viktor Govako)
- Correction de l'importation des fichiers KMB (Alexander Borsuk)
- Mise à jour des traductions des catégories, des synonymes de recherche et des chaînes de l'interface utilisateur (Alexander Borsuk, Viktor Govako)
- Traduction des descriptions de la Nouvelle-Galles du Sud et du Territoire du Nord (alnzrv)
- Amélioration de la stabilité et des performances, notamment pour le façonnage du texte, la mise en cache des glyphes et le découpage des lignes d'itinéraire (Viktor Govako, Alexander Borsuk)

### iOS

- NOUVEAU ! Ajout d'un bouton d'enregistrement de trace dans le panneau d'informations en cours de navigation (Kiryl Kaveryn)
- NOUVEAU ! Deux niveaux supplémentaires dans le tableau de bord de navigation pour obtenir des informations plus précises sur l'altitude et l'itinéraire (Kiryl Kaveryn)
- Mise à jour du style du profil d'altitude dans le tableau de bord de navigation, avec un affichage correct des traces présentant des altitudes négatives (Kiryl Kaveryn)
- Correction de la liste de signets erronée affichée dans la version TestFlight (Alexander Borsuk)
- Un bouton « Arrêter » plus grand et des zones tactiles plus larges pour les boutons du panneau inférieur pendant la navigation : coupure de la synthèse vocale, paramètres, enregistrement de trace (Kiryl Kaveryn)
- Amélioration de l'animation de la section de description extensible sur la page du lieu (Kiryl Kaveryn)
- La page du lieu ne se ferme plus lorsque l'on cesse de parcourir le profil d'altitude, ne rebondit plus de manière inattendue et garde le titre visible lors de la modification avec le clavier ouvert (Kiryl Kaveryn)
- Correction des problèmes de couleur du profil d'altitude et de la barre de progression circulaire lorsque l'apparence du système change (Kiryl Kaveryn)
- Correction des plantages lors de la suppression d'une trace ou d'un signet qui n'existe plus (Kiryl Kaveryn)

### Android

- NOUVEAU ! Tableau de bord d'altitude permanent et profil d'altitude de l'itinéraire amélioré, avec une mise en page RTL adaptée (Eric Jau, Mikhail Listratsenka)
- L'état de l'itinéraire enregistré est désormais conservé lors de la rotation de l'appareil (Mikhail Listratsenka)
- Une seule ligne de référence d'itinéraire unifiée sur la page du lieu (Mikhail Listratsenka)
- Des coins plus arrondis pour les panneaux inférieurs, les boutons et les éléments graphiques, afin d'obtenir un rendu plus homogène (Mikhail Listratsenka)
- Correction de problèmes de mise en page autour des barres système et de la barre de navigation (Mikhail Listratsenka)
- Affichage amélioré des articles Wikipedia, avec une mise en forme optimisée, des couleurs système et la prise en charge du mode sombre (DeshDeepakKant, Mikhail Listratsenka)
- Ajout de séparateurs verticaux entre les segments des traces à géométries multiples sur le profil d'altitude (Mikhail Listratsenka)
- Amélioration du défilement du profil d'altitude (Mikhail Listratsenka)
- Corrections apportées à la mise en page de droite à gauche (RTL) (Mikhail Listratsenka)

### Linux et Mac OS

- Ajout d'un sélecteur d'itinéraire de transport en commun permettant de choisir une ligne spécifique lorsqu'un arrêt est sélectionné (Viktor Govako)
- Affichage des boutons d'action de l'itinéraire directement sur la page du lieu (Viktor Govako)
- Suppression des horaires d'ouverture en double sur la page du lieu (Viktor Govako)
- Le repère d'étape intermédiaire sur un point d'intérêt ou une adresse affiche désormais le nom du lieu (Viktor Govako)
- Le téléchargement des cartes reprend là où il s'était arrêté en cas d'arrêt normal (Alexander Borsuk)
- Organic Maps fonctionne désormais avec les pilotes OpenGL ES 3.0 (Alexander Borsuk)

Participez au test bêta pour découvrir les nouvelles fonctionnalités en avant-première et signaler les problèmes :
- [iOS][testflight]
- [Android][firebase]

Nous adorons nos utilisateurs ❤️ et nous adorons ce que nous faisons

L'équipe Organic Maps

{{ references() }}
