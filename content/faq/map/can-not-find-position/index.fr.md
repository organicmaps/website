---
title: "L'application ne trouve pas ma position sur la carte ou affiche une localisation incorrecte"
slug: lapplication-narrive-pas-à-déterminer-ma-position
description: "Guide de dépannage pour résoudre les problèmes de localisation et de position GPS actuelle sur la carte pour les appareils iOS et Android"
updated: "2026-01-04"
taxonomies:
  faq: ["Carte"]
extra:
  order: 10
aliases:
  - /fr/faq/map/can-not-find-position/
---

Veuillez vous assurer que votre appareil dispose de GPS et que les paramètres de localisation sont activés.

**Android**

Sur votre appareil, ouvrez Paramètres → Localisation. Il est préférable d'activer le mode Haute précision.

Si vous avez des difficultés à déterminer votre position avec le GPS, activez (désactivez, si activé) "Google Play Services" dans les paramètres de l'application.

Remarque : vous ne pouvez le voir que si les services Google Play sont installés (activés) sur votre ordinateur. Appareil Android Les services Google Play sont utilisés pour déterminer l'emplacement plus précisément, si vous vous rencontrez des problèmes de précision de localisation après avoir désactivé l'option, activez-la.

**iOS**

Si vous utilisez un iPhone ou un iPad, veuillez vérifier les paramètres iOS → Confidentialité → Services de localisation. Le partage de données de géolocalisation doit être activé pour Organic Maps.

**Notes:**

* Pour éviter les données indésirables en itinérance, vous pouvez désactiver toutes les données mobiles, activer le mode Avion ou désactiver les données mobiles pour Organic Maps dans les paramètres de votre appareil. Les appareils Android et iOS peuvent utiliser le GPS en mode Avion.

* Certains appareils mobiles ne disposent pas de récepteurs GPS intégrés, tels que l'iPod Touch, l'iPad WiFi uniquement, Amazon Kindle Fire / Kindle Fire HD 7 et quelques tablettes Android. Sur ces appareils, notre application montrera votre position approximative, tant que vous êtes connecté à Internet.

* Enfin, rappelez-vous que l'emplacement déterminé avec le GPS (avec WiFi et Mobile Réseau éteint) peut prendre un certain temps. Moins le GPS a été utilisé, plus il prend de temps. La vitesse de détermination de l'emplacement dépend de l'appareil, pas de l'application. Le fonctionnement du GPS est influencé par la météo aussi - il fonctionne mieux à l'extérieur quand le ciel est clair. Des problèmes peuvent survenir si vous vous trouvez à l'intérieur, dans une rue étroite ou en conduisant une voiture.


**Une localisation incorrecte est affichée sur la carte**

1. S'il y a un grand cercle semi-transparent autour de votre flèche de localisation sur la carte, cela signifie que votre position est déterminée avec une faible précision, en utilisant une connexion WiFi ou cellulaire. Assurez-vous d'avoir activé la précision de localisation "Précise" pour Organic Maps dans les paramètres du système, et essayez d'aller à l'extérieur, loin des grands bâtiments et des arbres, pour améliorer la réception du signal GPS par satellite.

2. Si votre position est déterminée de manière incorrecte (par exemple, vous êtes dans une ville, mais l'application affiche une autre ville), vous êtes très probablement dans une zone affectée par un faux signal GPS (usurpation GPS) en raison de mesures de guerre électronique (GE). Dans de tels cas, la seule solution est de se déplacer vers un autre endroit.