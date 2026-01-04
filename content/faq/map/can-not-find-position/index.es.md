---
title: "La aplicación no puede encontrar mi posición en el mapa o muestra una ubicación incorrecta"
slug: la-aplicación-no-puede-establecer-mi-posición
description: "Guía de solución de problemas para resolver problemas con la ubicación y la posición GPS actual en el mapa para dispositivos iOS y Android"
updated: "2026-01-04"
taxonomies:
  faq: ["Mapa"]
extra:
  order: 10
aliases:
  - /es/faq/map/can-not-find-position/
---

Asegúrese de que su dispositivo tenga configurados el GPS y la ubicación.

**Android**

En su dispositivo, abra Configuración → Ubicación. Es mejor activar el modo de alta precisión.

Si tiene dificultades para determinar su ubicación con GPS, habilite (deshabilite, si está habilitado) "Servicios de Google Play" en la configuración de la aplicación.

Nota: puede verlo solo si tiene los servicios de Google Play instalados (habilitados) en su dispositivo Android. Los servicios de Google play se usan para determinar la ubicación de manera más precisa; si tiene problemas con la precisión de la ubicación después de deshabilitar la opción, actívela.

**iOS**

Si usted es un usuario de iPhone o iPad, verifique la configuración de iOS → Privacidad → Servicios de ubicación. El intercambio de datos de geolocalización debería estar habilitado para Organic Maps.

**Notas:**

* Para evitar datos no deseados durante el roaming, puede desactivar los datos móviles, activar modo avión o deshabilitar datos móviles para Organic Maps en la configuración de su dispositivo. Los dispositivos Android e iOS pueden usar el GPS en el modo avión.

* Algunos dispositivos móviles no tienen receptores GPS incorporados, como el iPod Touch, el iPad solo WiFi, Amazon Kindle Fire / Kindle Fire HD 7 y algunas tabletas Android. En estos dispositivos, nuestra aplicación mostrará su ubicación aproximada, siempre que esté conectado a internet.

* Por último, recuerde que la determinación de la ubicación con GPS (con WiFi y Red móvil desactivada) puede llevar algo de tiempo. Cuanto más tiempo no se haya utilizado el GPS, más tiempo tomará. La velocidad de determinación de la ubicación depende del dispositivo, no de la aplicación. La operación del GPS también está influenciada por el clima: funciona mejor en exteriores cuando el cielo está despejado. Pueden surgir problemas al tratar de ubicarse en el interior, en una calle estrecha o cuando conduce un automóvil.


**Se muestra una ubicación incorrecta en el mapa**

1. Si hay un gran círculo semitransparente alrededor de la flecha de su ubicación en el mapa, significa que su posición se determina con baja precisión, utilizando conexión WiFi o celular. Asegúrese de haber habilitado la precisión de ubicación "Precisa" para Organic Maps en la configuración del sistema e intente salir al exterior, lejos de edificios altos y árboles, para mejorar la recepción de la señal GPS satelital.

2. Si su posición se determina incorrectamente (por ejemplo, está en una ciudad, pero la aplicación muestra otra ciudad), lo más probable es que se encuentre en un área afectada por una señal GPS falsa (suplantación de GPS) debido a medidas de guerra electrónica (EW). En tales casos, la única solución es moverse a otra ubicación.