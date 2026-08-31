---
title: "Sélection multiple des signets et des traces, un tableau de bord CarPlay, la possibilité de masquer des traces sur la carte et des liens de partage lisibles dans la mise à jour d'août 2026"
date: 2026-08-31
slug: "selection-multiple-signets-traces-tableau-bord-carplay-masquer-traces-liens-partage-aout-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 02-bookmarks-tracks-multi-selection.jpg
---

Télécharge la version d'août 2026 d'Organic Maps sur <https://get.omaps.org> ou sur l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium] ([Accrescent][accrescent] et [F-Droid][fdroid] arrivent bientôt eux aussi).

Pourquoi mettre à jour ?
- Sélection multiple dans les signets et les traces, avec suppression, déplacement et changement de couleur groupés
- Tableau de bord CarPlay
- Masquage de traces individuelles sur la carte
- Liens de partage lisibles pour les lieux, les signets et ta position actuelle — sans oublier AirDrop sur iOS et une action « Share » sur ordinateur
- Guidage vocal en arménien et en lao
- Articles Wikipédia en 19 langues
…et bien d'autres améliorations, corrections de bugs et données cartographiques mises à jour ci-dessous.

N'oublie pas non plus de consulter les notes des versions précédentes de [juin](@/news/2026-06-29/610/index.fr.md) et de la [mise à jour de juillet](@/news/2026-07-23/620/index.fr.md).

## Journal des modifications complet

### Carte et lieux

- Données OpenStreetMap mises à jour au 26 août 2026 _(Viktor Govako)_
- Articles Wikipédia mis à jour en arabe, bengali, chinois, anglais, français, allemand, hindi, italien, japonais, coréen, marathi, polonais, portugais, russe, espagnol, tamoul, télougou, turc et ourdou _(Alexander Borsuk)_
- Correction de nombreux problèmes qui provoquaient un affichage erroné des horaires d'ouverture _(Alexander Borsuk)_
- Ajout de la prise en charge des observatoires ornithologiques _(Batmaclos, Viktor Govako)_
- Ajout des scènes de spectacle, des collines et des arches naturelles sur la carte, ainsi que d'une nouvelle icône pour les rochers _(David Martinez)_
- Redimensionnement des icônes des sommets, des grottes et des cols de montagne _(David Martinez)_
- Les zones protégées, les parcs nationaux et les zones humides s'affichent désormais dans des teintes plus claires _(Alexander Borsuk)_
- Correction d'un blocage de l'application et d'un problème qui faisait parfois ignorer les appuis et les gestes _(Alexander Borsuk)_

### Partage, signets et traces

- Le partage d'un lieu, d'un signet ou de ta position actuelle envoie désormais un lien lisible contenant des informations utiles _(Alexander Borsuk)_
- Les signets exportés conservent désormais leurs noms et descriptions d'origine _(Alexander Borsuk)_
- Les listes de signets partagées utilisent désormais leur nom affiché plutôt que le nom du fichier interne _(Alexander Borsuk)_
- Correction d'un problème d'affichage du graphique d'altitude qui pouvait survenir juste après le lancement d'un enregistrement de trace _(Kiryl Kaveryn)_

### Itinéraires et navigation

- Appuyer sur un arrêt ou un repère d'itinéraire l'ouvre désormais correctement au lieu de basculer entre les itinéraires planifiés _(Viktor Govako)_
- Les itinéraires en transports en commun sont désormais calculés plus rapidement _(Viktor Govako)_
- Correction d'instructions de virage erronées _(Alexander Borsuk)_
- Correction d'un point de départ incorrect après le recalcul d'un itinéraire _(Viktor Govako)_
- Les routes en latérite sont désormais considérées comme des voies non revêtues de mauvaise qualité lors du calcul d'itinéraire _(Julien Etienne)_
- Les routes marquées `access=unknown` sont désormais traitées comme les routes à accès privé ou réservé aux riverains _(Julien Etienne)_
- Ajout du guidage vocal en arménien et en lao _(Alexander Borsuk)_

### Éditeur OpenStreetMap

- Vider le champ des horaires d'ouverture ne laisse plus le bouton « Sauvegarder » ou « Terminé » désactivé _(Alexander Borsuk)_
- Les envois partiellement en échec font désormais l'objet d'une nouvelle tentative au lieu d'être signalés comme entièrement réussis _(Alexander Borsuk)_

### Traductions

- Mise à jour de la [Foire aux questions](https://organicmaps.app/fr/faq/), y compris de sa traduction en japonais _(Alexander Borsuk)_
- Correction de la traduction japonaise de « Fermé actuellement » _(Viktor Govako)_
- Amélioration des traductions chinoises de « trace » et « désactiver » _(Chenxi Zhao)_

### iOS

- NOUVEAU : ajout de la sélection multiple dans la liste des signets et des traces, avec des actions groupées pour supprimer, déplacer et changer la couleur des éléments sélectionnés, ainsi que les options « Tout sélectionner » et « Tout désélectionner » _(Kiryl Kaveryn)_
- NOUVEAU : ajout d'un tableau de bord CarPlay _(Kiryl Kaveryn)_
- Ajout de la prise en charge d'AirDrop pour partager des lieux _(Kiryl Kaveryn)_
- Correction de plusieurs problèmes liés à CarPlay _(Kiryl Kaveryn, Alexander Borsuk)_
- Correction de l'affichage des descriptions HTML lorsqu'un signet est sélectionné sur la carte _(Kiryl Kaveryn)_
- Correction de l'activation du style de carte pour la navigation en voiture _(Kiryl Kaveryn, Alexander Borsuk)_
- Réorganisation des paramètres en sections « Paramètres généraux », « Carte », « Navigation », « Réseau » et « Vie privée » _(Kiryl Kaveryn)_
- Suppression du paramètre de calibrage de la boussole, le calibrage étant désormais automatique _(Kiryl Kaveryn)_
- Rétablissement du sélecteur de couleur personnalisée dans la fenêtre contextuelle de la palette de couleurs _(Kiryl Kaveryn)_
- Le point correspondant s'affiche désormais sur la carte lorsque tu fais glisser ton doigt sur le profil d'altitude dans l'aperçu d'un itinéraire à pied ou à vélo _(Kiryl Kaveryn)_
- Correction de problèmes de boussole qui pouvaient faire pointer la flèche de position actuelle dans la mauvaise direction ou la figer _(Alexander Borsuk)_
- Correction d'un plantage lorsqu'un envoi vers OpenStreetMap se terminait en arrière-plan _(Alexander Borsuk)_

### Android

- NOUVEAU : ajout d'un mode de sélection multiple dans la liste des signets et des traces. Pour l'activer, appuie longuement sur un élément ou utilise la barre d'outils, puis change la couleur, déplace ou supprime n'importe quelle combinaison de signets et de traces _(Mikhail Listratsenka)_
- NOUVEAU : tu peux désormais masquer des traces individuelles sur la carte grâce à l'icône en forme d'œil de la liste ou de l'écran de détails de la trace _(cyber-toad)_
- Android Auto et Android Automotive : correction des flèches de voie de demi-tour _(Andrei Shkrob, Viktor Govako)_
- Android Auto et Android Automotive : correction du basculement entre les modes jour et nuit _(Andrei Shkrob)_
- Android Auto et Android Automotive : la liste de recherche reste désormais ouverte pendant la saisie _(Viktor Govako)_
- La description de la liste s'affiche désormais lorsque la liste est triée _(Mikhail Listratsenka)_
- Mise à jour du design de l'écran des paramètres de la liste de signets _(Mikhail Listratsenka)_
- Le panneau de recherche se replie désormais lorsque tu appuies sur une catégorie _(Mikhail Listratsenka)_
- Le focus du clavier revient désormais dans le champ de recherche après que tu l'as effacé _(Mikhail Listratsenka)_
- Le graphique d'altitude de l'itinéraire occupe désormais toute la largeur du panneau _(Mikhail Listratsenka)_
- Correction d'un problème qui pouvait laisser les boutons de zoom bloqués en haut de l'écran _(Mikhail Listratsenka)_
- Les coins des boîtes de dialogue sont désormais arrondis de manière uniforme sur toutes les versions d'Android _(Mikhail Listratsenka)_
- Correction d'un plantage dans le menu d'exportation des traces _(Mikhail Listratsenka)_
- Correction de blocages de l'application _(Alexander Borsuk, Viktor Govako)_
- Correction des importations en double de fichiers KML et KMZ et d'une erreur « Impossible d'ouvrir le fichier » _(Alexander Borsuk)_
- Correction des catégories de recherche en portugais brésilien, en espagnol mexicain et en anglais britannique _(Alexander Borsuk)_
- La recherche fonctionne désormais correctement dans la langue du clavier lorsqu'elle diffère de la langue de l'interface _(Alexander Borsuk)_
- Les modifications OpenStreetMap ne sont plus perdues lorsqu'un envoi prend trop de temps ou échoue partiellement _(Alexander Borsuk)_

### Bureau

- Ajout d'une action « Share » sur la page d'un lieu, avec les options « Copy Link », « Copy Text » et « Email… » _(Alexander Borsuk)_
- L'indicateur de téléchargement est désormais dessiné par programmation, ce qui le garde net sur tous les écrans _(Kuzey Bilgin)_

## Comment soutenir Organic Maps

- [Fais un don](@/donate/index.fr.md) pour soutenir le développement et couvrir les frais d'hébergement des cartes
- [Envoie-nous tes commentaires et participe](@/contribute/index.fr.md) au projet
- Rejoins le bêta-test pour essayer les nouveautés en avant-première et signaler les problèmes sur [iOS][testflight], [Android][firebase] et [ordinateur][flathub]
- Fais passer le mot !

Avec toute notre affection et notre gratitude envers tous nos utilisateurs et contributeurs,<br/>
L'équipe Organic Maps

{{ <references lang /> }}
