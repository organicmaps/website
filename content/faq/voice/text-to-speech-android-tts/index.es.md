---
title: Instrucciones de voz (Text-To-Speech, TTS) en Android
description: Guía sobre cómo hacer que TTS funcione en Android
slug: instrucciones-de-voz-tts-en-android
aliases:
  - /es/faq/voice/text-to-speech-android-tts/
  - /es/faq/instrucciones-de-voz-tts-en-android/
taxonomies:
  faq: ["instrucciones-de-voz"]
extra:
  order: 10
---

## Información general

Organic Maps utiliza el motor de texto a voz (Text-To-Speech, TTS) del sistema para las instrucciones de voz. Los motores predeterminados varían según el dispositivo, que puede ser el motor Text-To-Speech de Google, el motor del fabricante del dispositivo o un motor de terceros.

La recomendación oficial de Organic Maps es [RHVoice](https://rhvoice.org/), que es un motor de voz gratuito y de código abierto que se puede descargar desde [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) y [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instrucciones

- Abre la aplicación de Ajustes de tu dispositivo Android
- Ve a Ajustes Adicionales y después a Accesibilidad
- Elige tu motor preferido, el tono y la velocidad de la voz
- **Reinicia la aplicación Organic Maps**
- Abre Ajustes => Instrucciones de voz en Organic Maps y configúralo
- Reinicia de nuevo la aplicación Organic Maps (o reinicia el dispositivo) si la voz no funciona.


Si no puedes encontrar estos ajustes, abre la aplicación de Ajustes y busca "Instrucciones de voz".

Aviso: Nota que estas instrucciones pueden variar en función de la marca de tu dispositivo.

Estas opciones pueden que no estén disponibles si no tienes la funcionalidad TTS (Instrucciones de voz) instaladas en tu dispositivo. Por favor, revisa la tabla más abajo para instalar cualquier motor que soporte tu idioma.

## Capturas de pantalla

|             |             |
| ----------- | ----------- |
![Ajustes](tts_config_1.png "Ajustes") | ![Accesibilidad](tts_config_2.png "Accesibilidad")

## Motores de síntesis de voz

A continuación se muestra una lista completa de los idiomas y los motores soportados para cada uno de ellos (los enlaces de descarga de cada motor se pueden encontrar después de la tabla):

{{ tts_table() }}

## Soluciones a problemas con RHVoice

Si tienes problemas para inicializar el motor de voz RHVoice en LineageOS o en otras ROM personalizadas, prueba esta solución alternativa. Es posible que RHVoice no se inicialice correctamente y que la aplicación falle, especialmente si no has utilizado ningún motor TTS en tu teléfono antes (por ejemplo, una nueva instalación, un restablecimiento de fábrica, etc.). Si estás utilizando una ROM personalizada como LineageOS <ins>sin los servicios de Google Play y los Servicios de Voz de Google</ins>, y deseas utilizar RHVoice como tu motor TTS preferido, sigue las siguientes instrucciones como solución alternativa:

1. Instala el [motor eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak) disponible en F-Droid.
2. Configúralo como el motor del sistema preferido.
    - Ve a los **Ajustes** principales de LineageOS.
    - Desplázate hacia abajo hasta **Accesibilidad**.
    - Selecciona **Salida de texto a voz** y **Motor preferido** (en el lado izquierdo) y asegúrate de que **eSpeak** esté seleccionado.
3. Regresa y pulsa **Reproducir** para ver si está funcionando.
4. Instala [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/), disponible en F-droid.
    - Ábrelo, selecciona el idioma que deseas usar, toca el ícono de la nube (extremo izquierdo) para descargar las voces.
    - Presiona el botón de reproducción para verificar si está funcionando.
5. Configura **RHVoice** como motor preferido (consulta el paso 2).
6. Ahora, deberías poder utilizar RHVoice sin ningún problema.

## Prueba de la síntesis de voz

Para probar las instrucciones de voz, pulsa en "Probar indicaciones de voz (TTS, Text-To-Speech)" en el menú "Ajustes → Instrucciones de voz" de OM, o puedes iniciar una navegación para recibir cualquier salida de voz. Organic Maps no te dará instrucciones de voz si estás parado.

![Prueba de la funcionalidad de síntesis de voz](tts_test.png "Prueba de la funcionalidad de síntesis de voz")
