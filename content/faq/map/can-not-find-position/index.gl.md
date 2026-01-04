---
title: "A aplicación non pode atopar a miña posición no mapa ou mostra unha localización incorrecta"
slug: a-aplicación-non-pode-atopar-a-miña-posición-no-mapa
description: "Guía de resolución de problemas para resolver problemas coa localización e a posición GPS actual no mapa para dispositivos iOS e Android"
updated: "2026-01-04"
taxonomies:
  faq:
  - Map
extra:
  order: 10
aliases:
  - /gl/faq/map/can-not-find-position/
---

Asegúrate de que o teu dispositivo teña GPS, que os servizos de localización estean activados e que se outorguen permisos de localización a Organic Maps.

**Android**

No seu dispositivo abra Configuración → Localización. É mellor activar o modo de alta precisión, xa que permite unha localización GPS precisa.

Se o teu dispositivo Android non pode determinar a túa localización, activa (ou desactiva, se está activada) a opción "Servizos de Google Play" na configuración da aplicación.

Nota: só podes velo se tes os servizos de Google Play instalados (activados) no teu dispositivo Android. Os servizos de Google Play utilízanse para determinar a localización con máis precisión. Se tes problemas coa precisión da localización despois de desactivar a opción, actívaa.

**iOS**

Se es un usuario de iPhone ou iPad, comprobe a configuración de iOS → Privacidade → Servizos de localización. O uso compartido de datos de xeolocalización debería estar activado para os mapas orgánicos.

**Notas:**

* Para evitar datos non desexados durante a itinerancia, podes desactivar todos os datos móbiles, activar un modo de voo ou desactivar os datos móbiles para os mapas orgánicos na configuración do teu dispositivo. Os dispositivos Android e iOS poden usar o GPS no modo voo.

* Algúns dispositivos móbiles non teñen receptores GPS integrados, como o iPod Touch, o iPad só con WiFi, Amazon Kindle Fire/Kindle Fire HD 7 e algunhas tabletas Android. Nestes dispositivos, todas as aplicacións mostrarán a túa localización aproximada detectada mediante unha rede wifi, sempre que esteas conectado a Internet.

* A detección de localización con satélites GPS (cando a WiFi e as redes móbiles están desactivadas) pode levar algún tempo. Canto máis tempo non se use o GPS, máis tempo leva. A velocidade de detección de localización depende do dispositivo, non da aplicación. O funcionamento do GPS tamén está influenciado polo tempo: funciona mellor ao aire libre cando o ceo está despexado. Poden xurdir problemas ao intentar localizarse no interior, nunha rúa estreita ou ao conducir un coche, con moito metal ao redor ou cun metal/imán na carcasa do dispositivo.


**Móstrase unha localización incorrecta no mapa**

1. Se hai un gran círculo semitransparente arredor da frecha da túa localización no mapa, significa que a túa posición se determina con baixa precisión, usando conexión WiFi ou móbil. Asegúrate de ter activada a precisión de localización "Precisa" para Organic Maps na configuración do sistema e proba a saír ao exterior, lonxe de edificios altos e árbores, para mellorar a recepción do sinal GPS por satélite.

2. Se a túa posición se determina incorrectamente (por exemplo, estás nunha cidade, pero a aplicación mostra outra cidade), o máis probable é que esteas nunha zona afectada por un sinal GPS falso (suplantación de GPS) debido a medidas de guerra electrónica (EW). Nestes casos, a única solución é moverse a outra localización.