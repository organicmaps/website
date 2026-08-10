---
title: "La aplicación no puede encontrar mi posición en el mapa o muestra una ubicación incorrecta"
slug: la-aplicación-no-puede-establecer-mi-posición
description: "Guía de solución de problemas para resolver problemas con la ubicación y la posición GPS actual en el mapa para dispositivos iOS y Android"
updated: "2026-01-04"
taxonomies:
  faq: ["mapa"]
extra:
  order: 10
aliases:
  - /es/faq/map/can-not-find-position/
---

Asegúrate de que tu dispositivo tenga GPS, de que los servicios de ubicación estén activados y de que hayas concedido a Organic Maps los permisos de ubicación.

**Android**

En tu dispositivo, abre Configuración → Ubicación. Es mejor activar el modo de alta precisión.

Si tienes dificultades para determinar tu ubicación con GPS, habilita (deshabilita, si está habilitado) «Servicios de Google Play» en la configuración de la aplicación.

Nota: puedes verlo solo si tienes los servicios de Google Play instalados (habilitados) en tu dispositivo Android. Los servicios de Google play se usan para determinar la ubicación de manera más precisa; si tienes problemas con la precisión de la ubicación después de deshabilitar la opción, actívala.

**iOS**

Si eres un usuario de iPhone o iPad, verifica la configuración de iOS → Privacidad → Servicios de ubicación. El intercambio de datos de geolocalización debería estar habilitado para Organic Maps.

**Se muestra una ubicación incorrecta en el mapa**

1. Si hay un gran círculo semitransparente alrededor de la flecha de tu ubicación en el mapa, significa que tu posición se determina con baja precisión, utilizando conexión WiFi o celular. Asegúrate de haber habilitado la precisión de ubicación «Precisa» para Organic Maps en la configuración del sistema e intenta salir al exterior, lejos de edificios altos y árboles, para mejorar la recepción de la señal GPS satelital.

2. Si tu posición se determina incorrectamente (por ejemplo, estás en una ciudad, pero la aplicación muestra otra ciudad), lo más probable es que te encuentres en un área afectada por una señal GPS falsa (suplantación de GPS) debido a medidas de guerra electrónica (EW). En tales casos, la única solución es moverse a otra ubicación.

**Notas:**

* Para evitar datos no deseados durante el roaming, puedes desactivar los datos móviles, activar modo avión o deshabilitar datos móviles para Organic Maps en la configuración de tu dispositivo. Los dispositivos Android e iOS pueden usar el GPS en el modo avión.

* Algunos dispositivos móviles no tienen receptores GPS incorporados, como el iPod Touch, el iPad solo WiFi, Amazon Kindle Fire / Kindle Fire HD 7 y algunas tabletas Android. En estos dispositivos, nuestra aplicación mostrará tu ubicación aproximada, siempre que estés conectado a internet.

* Por último, recuerda que la determinación de la ubicación con GPS (con WiFi y Red móvil desactivada) puede llevar algo de tiempo. Cuanto más tiempo no se haya utilizado el GPS, más tiempo tomará. La velocidad de determinación de la ubicación depende del dispositivo, no de la aplicación. La operación del GPS también está influenciada por el clima: funciona mejor en exteriores cuando el cielo está despejado. Pueden surgir problemas al tratar de ubicarte en el interior, en una calle estrecha o cuando conduces un automóvil.
