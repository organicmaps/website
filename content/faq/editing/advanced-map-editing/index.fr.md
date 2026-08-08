---
title: Comment puis-je effectuer des modifications de carte plus avancées ?
slug: comment-puis-je-effectuer-des-modifications-de-carte-plus-avancées
description: Tutoriel pour éditer OpenStreetMap avec des outils plus avancés comme
  ID, Go Map et Vespucci
updated: '2024-06-20'
taxonomies:
  faq: ["édition-de-la-carte"]
extra:
  order: 40
aliases:
  - /fr/faq/editing/advanced-map-editing/
---

Organic Maps comprend un éditeur simple et facile à utiliser que tu peux utiliser pour modifier la carte. L'éditeur est cependant limité et permet uniquement d'ajouter des entités ponctuelles simples, c'est-à-dire pas de contours de bâtiments, de routes, de lacs, de villes, etc. Si tu souhaites modifier quelque chose qui ne peut pas être modifié avec l'éditeur intégré, c'est la bonne page FAQ à lire.

Comme toutes les données cartographiques utilisées dans Organic Maps proviennent de [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), tu peux directement mettre à jour la carte ici. Tes modifications seront ensuite incluses dans Organic Maps lors de la prochaine mise à jour de la carte.

## Éditeurs OpenStreetMap

Pour éditer OSM, il existe plusieurs options. Si tu disposes d'un ordinateur portable ou de bureau, il est préférable d'utiliser l'[ID Editor](https://www.openstreetmap.org/edit) qui s'exécute dans ton navigateur. L'ID Editor est simple pour les débutants, et un écran, une souris et un clavier plus grands facilitent l'édition de cartes.

Pour une édition avancée de cartes à partir d'un appareil mobile, utilise [Go Map](https://apps.apple.com/us/app/go-map/id592990211) pour iOS ou [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) pour Android. Go Map est facile pour les débutants, tandis que Vespucci cible les utilisateurs plus avancés. LearnOSM propose des didacticiels pour [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) et [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Pour des modifications plus simples et plus amusantes, tu peux également essayer [l'application Every Door](https://every-door.app/) pour iOS et Android et [l'application StreetComplete](https://streetcomplete.app/) pour Android.

#### ID Editor

Pour modifier OpenStreetMap avec ID, suis ces étapes :

1. Crée un nouveau compte ou connecte-toi à [OpenStreetMap.org](https://www.openstreetmap.org)
2. Accède à l'emplacement que tu souhaites modifier sur OpenStreetMap.org et clique sur *Modifier* en haut.
3. *Démarrez la procédure pas à pas* et suis le court didacticiel qui explique l'ID Editor.
4. Modifie la carte
5. Télécharge tes modifications

Ça y est, tu fais désormais partie de la communauté OSM.

## Que se passe-t-il avec mes modifications ?

Une fois que tu appuies sur *Télécharger*, tes modifications sont instantanément ajoutées à la base de données publique OSM. Sois donc attentif lors de l'édition. Dans Organic Maps, tes modifications seront visibles après la prochaine mise à jour mensuelle de la carte.

Ton e-mail n'est pas publié, mais d'autres personnes pourront voir ton nom d'utilisateur OSM. Comme OSM offre la possibilité de discuter des modifications, tu pourrais recevoir des questions sur tes modifications de la part d'autres contributeurs OSM. Tu en seras informé via l’adresse e-mail que tu as utilisée pour enregistrer ton compte OSM. Comme OSM est un projet communautaire qui s'appuie sur la collaboration, tu dois toujours répondre à ces questions.

## Communauté et wiki

OpenStreetMap est une communauté. Si tu as besoin d'aide ou si tu as des questions, tu peux les poser sur le [Forum OSM](https://community.openstreetmap.org/c/help-and-support) ou consulter la documentation du [OSM Wiki](https://wiki.openstreetmap.org/).

## Tags - Comment fonctionne le modèle de données OSM

La base de données OpenStreetMap contient des objets tels que des nœuds, des chemins, des zones et des relations qui font abstraction des fonctionnalités du monde réel. Ces objets ont des attributs, appelés balises pour les décrire plus en détail. Une balise est une combinaison clé-valeur.

Comme cela semble plus compliqué qu’il ne l’est, nous allons donner un exemple :
Un restaurant est par ex. mappé comme une note ou une zone avec la balise `amenity=restaurant`. D'autres balises comme `cuisine=*` ou `opening_hours=*` peuvent ensuite être utilisées pour plus de détails.

> Note que l'ID editor cache la structure de données interne aux utilisateurs pour être plus convivial pour les débutants. Mais pour lire la documentation Wiki, un bref aperçu de la structure des données est utile.
Dans l'ID Editor, tu peux voir les balises que l'ID te cache en développant la section *Tags* dans le panneau latéral *Modifier la fonctionnalité*.

## Notes OSM {#osm-note}

Si tu n'as pas le temps ou si le problème est trop compliqué pour éditer toi-même les données OSM, les notes OSM ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) sont la voie à suivre. Tu peux placer une telle note à l'emplacement de l'erreur cartographique et décrire le problème en détail. D’autres bénévoles OSM peuvent alors aider et résoudre le problème. Tu recevras des notifications par e-mail via ton compte OSM au cas où ils auraient d'autres questions ou si la note OSM serait résolue.

1. Crée un nouveau compte ou connecte-toi à [OpenStreetMap.org](https://www.openstreetmap.org)
   > Tu peux également ouvrir des notes anonymes, mais cela n'est pas recommandé car tu ne seras pas averti lorsque le problème sera résolu ou qu'il y aura d'autres questions.
2. Zoome sur l'emplacement de la carte sur [OpenStreetMap.org](https://www.openstreetmap.org) et appuie sur *Ajouter une note à la carte* (deuxième icône en partant du bas dans le menu de droite). Fais ensuite glisser le marqueur de carte bleu vers l'emplacement exact.
   > Essaie d'être aussi précis que possible.
3. Fournis une description détaillée du problème de carte et appuie sur *Ajouter une note*
   > Pour les magasins par ex. fournir le nom et mentionner ce qui y est vendu ou quels services y sont offerts.
