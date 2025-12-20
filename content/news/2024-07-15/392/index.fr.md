---
title: "Avez-vous déjà installé la version d'Organic Maps du mois de juillet ? Elle introduit deux fonctionnalités majeures financées par le fonds d'investissement de l'NGI0"
date: 2024-07-15T21:13:23+00:00
slug: version-de-juillet-avec-une-recherche-amelioree-dadresses-aux-etats-unis-utilisant-les-donnees-tiger-et-un-rendu-de-texte-corrige-pour-les-ecritures-non-latines-financees-par-le-fonds-dinvestissement-de-lngi0
taxonomies:
  news: ["Releases"]
---

Avez-vous déjà [installé](https://omaps.app/get) la version d'Organic Maps du mois de juillet ? Elle introduit deux fonctionnalités majeures [financées](https://nlnet.nl/project/OrganicMaps/) par le fond d'investissement de l'NGI0 :

1. Meilleure recherche d'adresses aux États-Unis basée sur les données du système _Topologically Integrated Geographic Encoding and Referencing_ (TIGER) (prétraitées par le [projet Nominatim](https://nominatim.org/data/)), [implémentées](https://github.com/organicmaps/organicmaps/issues/2532) par Viktor Havaka. Les adresses sont stockées, recherchées et affichées sous forme d'interpolations (lignes le long des rues avec un numéro de maison de départ et un numéro de maison d'arrivée), donc ne vous attendez pas à voir des bâtiments sur la carte (saviez-vous que vous pouvez dessiner des bâtiments et ajouter des adresses vous-même sur [OpenStreetMap.org](https://openstreetmap.org/) ?)
Il existe une heuristique pour décider quand utiliser les données TIGER et quand utiliser les données OpenStreetMap existantes.
La taille de la carte pour l'ensemble des États-Unis est passée de 10 Go à 13 Go (y compris Wikipedia et les données d'élévation, il y a quelques [idées](https://github.com/organicmaps/organicmaps/issues/8672) pour [la diviser](https://github.com/organicmaps/organicmaps/issues/5912) afin d'améliorer [les mises à jour incrémentielles de la carte](https://github.com/organicmaps/organicmaps/issues/2317)).

2. Rendu correct des textes en alphabet indien (Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Tamil, Telugu), arabe (N'Ko, syriaque, mongol), thaï et lao, khmer, myanmar, tibétain, hangul, hébreu, [implémenté](https://github.com/organicmaps/organicmaps/issues/4281) par Alexander Borsuk en intégrant la bibliothèque de mise en forme de texte [Harfbuzz](https://harfbuzz.github.io/) avec le moteur de rendu d'Organic Maps (appelé "Drape").

D'autres améliorations notables ont été apportées grâce à nos contributeurs bien-aimés:

* Données OpenStreetMap du 2 juillet
* Nouvelles polices de caractères pour le Malayalam et le Bengali (veuillez nous faire savoir si d'autres polices ont besoin d'être mises à jour)
* Une simple pression permet désormais de sélectionner n'importe quel point sur la carte, même si celle-ci est vide -- par Sergiy Kozyr
* Modification de l'appui long pour basculer en mode plein écran -- par Sergiy Kozyr
* Un signet supprimé accidentellement sur la carte peut maintenant être restauré immédiatement (le bouton Enregistrer devient Restaurer) -- par Kiryl Kaveryn
* Affichage des routes principales plus tôt sur la carte du monde -- par Konstantin Pastbin
* Un lieu sélectionné affiche maintenant plus de types/catégories/aménagements -- par David Martinez
* Un texte plus explicite pour indiquer l'étage à laquelle se trouve un POI -- par Antonin Delpeuch
* Affichage des chemins piétonniers en graviers fin de bonne qualité en pointillés blancs -- par Konstantin Pastbin
* Prise en charge de plus de types de surfaces de routes/chemins (briques, pierres, pavés d'herbe, terre) -- par Konstantin Pastbin
* Des conseils plus clairs lors de la construction d'une route

La recherche -- merci à Viktor Havaka :
* La recherche de montagnes montre également les volcans
* Meilleurs résultats de recherche pour les lieux éloignés
* La recherche permet désormais de trouver les lieux dont le nom contient un chiffre
* Trouver les consignes à colis à l'aide de leur numéro de référence

Android:
* Correction du lien de la FAQ pour la synthèse vocale dans les paramètres
* Correction de l'importation de GPX depuis WhatsApp
* Sauvegarde des fichiers exportés sur le périphérique de stockage local -- par Kiryl Razhdzestvenski

iOS (un grand merci à Kiryl Kaveryn):
* Utilisez le bouton Importer dans la boîte de dialogue Signets et traces pour charger des fichiers KML, KMZ, GPX.
* Correction de l'importation des signets et des traces via l'application "Fichiers" lors d'un démarrage à froid (vous pouvez appuyer sur un fichier KML, KMZ, GPX ou KMB dans n'importe quelle application, puis sur le bouton "partager" , et enfin choisir l'icône Organic Maps dans la liste des applications).
* Ajout d'un bouton de test de la synthèse vocale dans les paramètres de navigation -- par Fabian Wüthrich
* Vous pouvez activer les journaux dans les paramètres pour nous aider à résoudre les bugs.
* Ouverture des liens vers les médias sociaux dans les applications installées
* Suppression du bouton trafic non fonctionnel de CarPlay -- par Fabian Wüthrich
* Remplacement de la case à cocher circulaire par un rectangle arrondi dans l'éditeur d'horaires d'ouverture
* Correction de la couleur d'arrière-plan du démarrage en mode sombre -- par Evgeny Fayvuzhinsky

Linux:
* Correction de l'icône Wayland générique affichée à la place de l'icône d'Organic Maps sur certains systèmes -- par Ferenc Géczi

Nos traducteurs et réviseurs nous ont aidés à mettre à jour les traductions en biélorusse, chinois, néerlandais, euskara, hongrois, polonais, portugais, russe et ukrainien.

Nous avons également commencé à mettre à jour la [section FAQ](https://organicmaps.app/faq/) sur notre site web. Toute aide pour [ajouter de nouveaux articles](https://github.com/organicmaps/organicmaps.github.io/) et leurs traductions est appréciée !

Nous vous invitons à nous signaler tous les bugs en utilisant le bouton Signaler un bug dans l'application, en nous envoyant un email, ou (le mieux !) en créant/mettant à jour [un problème](https://github.com/organicmaps/organicmaps/issues/) sur notre GitHub.

P.S. Nous travaillons actuellement sur la [fonction d'enregistrement des traces](https://github.com/organicmaps/organicmaps/labels/Track%20Recording). Toute aide sous forme d'idées, de [tests](https://organicmaps.app/#community), de [contributions](https://organicmaps.app/support-us/) et de [dons](https://organicmaps.app/donate/) est chaleureusement appréciée ❤️

Profitez de vos voyages avec Organic Maps ! 🚕 🛤 ✈️ 🏕 👣
