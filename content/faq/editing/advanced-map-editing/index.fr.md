---
title: Comment puis-je effectuer des modifications de carte plus avancées ?
description: Tutoriel pour éditer OpenStreetMap avec des outils plus avancés comme
  ID, Go Map et Vespucci
updated: '2024-06-20'
taxonomies:
  faq: ["Édition de la carte"]
extra:
  order: 40
---

Organic Maps comprend un éditeur simple et facile à utiliser que vous pouvez utiliser pour modifier la carte. L'éditeur est cependant limité et permet uniquement d'ajouter des entités ponctuelles simples, c'est-à-dire pas de contours de bâtiments, de routes, de lacs, de villes, etc. Si vous souhaitez modifier quelque chose qui ne peut pas être modifié avec l'éditeur intégré, c'est la bonne page FAQ à lire.

Comme toutes les données cartographiques utilisées dans Organic Maps proviennent de [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), vous pouvez directement mettre à jour la carte ici. Vos modifications seront ensuite incluses dans Organic Maps lors de la prochaine mise à jour de la carte.

## Éditeurs OpenStreetMap

Pour éditer OSM, il existe plusieurs options. Si vous disposez d'un ordinateur portable ou de bureau, il est préférable d'utiliser l'[ID Editor](https://www.openstreetmap.org/edit) qui s'exécute dans votre navigateur. L'éditeur d'ID est simple pour les débutants, et un écran, une souris et un clavier plus grands facilitent l'édition de cartes.

Pour une édition avancée de cartes à partir d'un appareil mobile, utilisez [Go Map](https://apps.apple.com/us/app/go-map/id592990211) pour iOS ou [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) pour Android. Go Map est facile pour les débutants, tandis que Vespucci cible les utilisateurs plus avancés. LearnOSM propose des didacticiels pour [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) et [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Pour des modifications plus simples et plus amusantes, vous pouvez également essayer [l'application Every Door](https://every-door.app/) pour iOS et Android et [l'application StreetComplete](https://streetcomplete.app/) pour Android.

#### Éditeur d'identifiants

Pour modifier OpenStreetMap avec ID, suivez ces étapes :

1. Créez un nouveau compte ou connectez-vous à [OpenStreetMap.org](https://www.openstreetmap.org)
2. Accédez à l'emplacement que vous souhaitez modifier sur OpenStreetMap.org et cliquez sur *Modifier* en haut.
3. *Démarrez la procédure pas à pas* et suivez le court didacticiel qui explique l'éditeur d'ID.
4. Modifiez la carte
5. Téléchargez vos modifications

Ça y est, vous faites désormais partie de la communauté OSM.

## Que se passe-t-il avec mes modifications ?

Une fois que vous appuyez sur *Télécharger*, vos modifications sont instantanément ajoutées à la base de données publique OSM. Soyez donc attentif lors de l'édition. Dans Organic Maps, vos modifications seront visibles après la prochaine mise à jour mensuelle de la carte.

Votre e-mail n'est pas publié, mais d'autres personnes pourront voir votre nom d'utilisateur OSM. Comme OSM offre la possibilité de discuter des modifications, vous pourriez recevoir des questions sur vos modifications de la part d'autres contributeurs OSM. Vous en serez informé via l’adresse e-mail que vous avez utilisée pour enregistrer votre compte OSM. Comme OSM est un projet communautaire qui s'appuie sur la collaboration, vous devez toujours répondre à ces questions.

## Communauté et wiki

OpenStreetMap est une communauté. Si vous avez besoin d'aide ou si vous avez des questions, vous pouvez les poser sur le [Forum OSM](https://community.openstreetmap.org/c/help-and-support) ou consulter la documentation du [OSM Wiki](https://wiki.openstreetmap.org/).

## Tags - Comment fonctionne le modèle de données OSM

La base de données OpenStreetMap contient des objets tels que des nœuds, des chemins, des zones et des relations qui font abstraction des fonctionnalités du monde réel. Ces objets ont des attributs, appelés balises pour les décrire plus en détail. Une balise est une combinaison clé-valeur.

Comme cela semble plus compliqué qu’il ne l’est, nous allons donner un exemple :
Un restaurant est par ex. mappé comme une note ou une zone avec la balise ``` amenity=restaurant```. D'autres balises comme ```cousine=*``` ou ```opening_hours=*``` peuvent ensuite être utilisées pour plus de détails.

> Notez que l'éditeur d'ID cache la structure de données interne aux utilisateurs pour être plus convivial pour les débutants. Mais pour lire la documentation Wiki, un bref aperçu de la structure des données est utile.
Dans l'éditeur d'ID, vous pouvez voir les balises que l'ID vous cache en développant la section *Tags* dans le panneau latéral *Modifier la fonctionnalité*.

## Notes OSM {#osm-note}

Si vous n'avez pas le temps ou si le problème est trop compliqué pour éditer vous-même les données OSM, les notes OSM ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) sont la voie à suivre. Vous pouvez placer une telle note à l'emplacement de l'erreur cartographique et décrire le problème en détail. D’autres bénévoles OSM peuvent alors aider et résoudre le problème. Vous recevrez des notifications par e-mail via votre compte OSM au cas où ils auraient d'autres questions ou si la note OSM serait résolue.

1. Créez un nouveau compte ou connectez-vous à [OpenStreetMap.org](https://www.openstreetmap.org)
   > Vous pouvez également ouvrir des notes anonymes, mais cela n'est pas recommandé car vous ne serez pas averti lorsque le problème sera résolu ou qu'il y aura d'autres questions.
2. Zoomez sur l'emplacement de la carte sur [OpenStreetMap.org](https://www.openstreetmap.org) et appuyez sur *Ajouter une note à la carte* (deuxième icône en partant du bas dans le menu de droite). Faites ensuite glisser le marqueur de carte bleu vers l'emplacement exact.
   > Essayez d'être aussi précis que possible.
3. Fournissez une description détaillée du problème de carte et appuyez sur *Ajouter une note*
   > Pour les magasins par ex. fournir le nom et mentionner ce qui y est vendu ou quels services y sont offerts.
