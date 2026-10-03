---
title: "Optimisation des itinéraires, amélioration des itinéraires alternatifs, masquage de traces individuelles et zones d’eau intermittentes dans la mise à jour de septembre 2026"
date: 2026-09-29
slug: "selection-multiple-signets-traces-tableau-bord-carplay-masquer-traces-liens-partage-aout-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Prêt à partir ? La mise à jour de septembre propose des itinéraires alternatifs améliorés, un réglage pour optimiser l’ordre des étapes de l’itinéraire, un marquage plus clair des zones où l’eau n’est présente que par intermittence et une icône en forme d’œil pour masquer des traces individuelles, ainsi que de nombreuses autres corrections et améliorations (voir ci-dessous).

Installe ou mets à jour Organic Maps via <https://get.omaps.org>, l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ou [F-Droid][fdroid].

Si tu as raté nos dernières mises à jour, jette un œil aux nouvelles fonctionnalités lancées en [juin](@/news/2026-06-29/610/index.fr.md), [juillet](@/news/2026-07-23/620/index.fr.md) et [août](@/news/2026-08-31/630/index.fr.md). Un grand merci à nos contributeurs et à nos utilisateurs qui ont rendu ces mises à jour possibles !

## Comment soutenir Organic Maps

- [Fais un don](@/donate/index.fr.md) pour soutenir le développement et couvrir les frais d'hébergement des cartes
- [Envoie-nous tes commentaires et participe](@/contribute/index.fr.md) au projet
- Rejoins le programme de bêta-test pour découvrir les nouvelles fonctionnalités en avant-première et signaler les problèmes sur [iOS][testflight], [Android][firebase] et sur [ordinateur][flathub]
- Fais passer le mot et aide-nous à créer une meilleure alternative aux cartes des géants de la tech !

## Notes de mise à jour

### Carte

- Données OpenStreetMap au 28 septembre 2026
- Données de Wikipédia au 21 septembre 2026
- On a corrigé les recherches quand la zone visible de la carte traverse le méridien de 180° (longitude ±180°) _(Viktor Govako)_
- Les zones d'eau intermittentes sont désormais représentées par un motif en pointillés, similaire à celui utilisé pour le sable _(Alexander Borsuk)_
- Les réservoirs d’eau sont désormais visibles lorsqu’on dézoome davantage _(Alexander Borsuk)_
- Les tunnels d'eau n'apparaissent plus sur la carte _(Alexander Borsuk)_
- Correction des icônes des stations et des entrées du métro de Suzhou _(Alexander Borsuk)_
- On a corrigé quelques rares cas où les libellés se décalaient sur la couche du plan du métro _(Viktor Govako)_

### Itinéraires et navigation

- Amélioration des itinéraires alternatifs et de leurs heures d’arrivée estimées _(Alexander Borsuk, Viktor Govako)_
- L'itinéraire alternatif choisi est désormais conservé lorsque la navigation recalcule l'itinéraire _(Alexander Borsuk)_
- L'ordre des arrêts de l'itinéraire est désormais rétabli après le redémarrage de l'appli _(Kiryl Kaveryn)_

### Autres améliorations

- Les horaires d’ouverture affichent désormais « Midi » pour 12:00 et « Minuit » pour 00:00 ou 24:00 _(Alexander Borsuk)_
- Correction de bugs et amélioration de l’enregistrement des traces _(Alexander Borsuk)_
- Correction de l'importation des fichiers KMB _(Alexander Borsuk)_
- Traductions corrigées en français et en asturien _(Alexander Borsuk)_
- Correction d'une faute de frappe en anglais _(Carl Morris)_

### iOS

- On a ajouté une icône en forme d'œil pour masquer des traces individuelles _(Kiryl Kaveryn)_
- On a ajouté des boutons pour ajouter ou remplacer un arrêt dans un itinéraire prévu _(Kiryl Kaveryn)_
- On a ajouté un paramètre pour optimiser l'ordre des étapes intermédiaires d'un itinéraire _(Kiryl Kaveryn)_
- Ajout d’instructions de manœuvre sur les affichages tête haute (HUD) compatibles des voitures et sur le tableau de bord CarPlay _(Kiryl Kaveryn)_
- Correction des boutons et de la recherche dans CarPlay _(Alexander Borsuk)_
- On a corrigé plusieurs bugs et amélioré l'interface utilisateur _(Kiryl Kaveryn, Alexander Borsuk)_
- Ajout de la possibilité de choisir une voix de navigation installée et d’en écouter un échantillon _(Kiryl Kaveryn, Alexander Borsuk)_
- La recherche par catégorie a été rétablie dans Spotlight _(Kiryl Kaveryn)_

### Android

- On a ajouté un paramètre pour optimiser l'ordre des étapes intermédiaires d'un itinéraire _(Mikhail Listratsenka)_
- On a ajouté des boutons pour ajouter ou remplacer un arrêt dans un itinéraire prévu _(Mikhail Listratsenka)_
- Ajout de la possibilité d’arrêter l’enregistrement d’une trace et de la sauvegarder depuis la notification _(Alexander Borsuk)_
- Le bouton « Ajouter un arrêt » ajoute désormais un arrêt après les arrêts existants, avant la destination _(Mikhail Listratsenka)_
- Amélioration de l’envoi des modifications depuis l’éditeur OpenStreetMap _(Owm)_
- Mise à jour du design de l'interface utilisateur _(Mikhail Listratsenka)_
- L'éditeur de signets et les autres boîtes de dialogue restent désormais ouverts pendant la navigation _(Mikhail Listratsenka)_
- Correction du rendu des graphiques d’altitude pour les traces avec peu de dénivelé et dans les interfaces de droite à gauche _(Mikhail Listratsenka)_
- Correction du problème où les boutons de la carte étaient coupés par les barres du système _(Mikhail Listratsenka)_
- Correction de bugs et amélioration de la prise en charge d'Android Auto _(Andrei Shkrob)_
- Correction d'un plantage lors du rendu de la carte _(Viktor Govako)_

### Bureau

- L’exécutable de bureau et le bundle de l’application macOS ont été renommés en `OrganicMaps` _(Alexander Borsuk)_
- Correction de bugs dans l'application Windows _(Osyotr, Alexander Borsuk)_
- L’argument de ligne de commande `--lang` prend désormais le pas sur le réglage de langue de l’application _(Alexander Borsuk)_

Avec joie et passion,

Ton équipe Organic Maps

{{ <references lang /> }}
