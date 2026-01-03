---
title: Texto a voz en Android
description: Guía sobre como facer que TTS funcione en Android
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
---

## Resumo

Organic Maps usa o motor de texto a voz (TTS) do sistema para as instrucións de voz. Os motores predeterminados varían segundo o dispositivo. As opcións poden incluír Google Text-to-Speech, o motor do fabricante do dispositivo ou outro de terceiros.

A recomendación oficial de Organic Maps é [RHVoice](https://rhvoice.org/), que é un motor de voz gratuíto e de código aberto que se pode descargar de [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) e [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instrucións

- Abre a aplicación Configuración no teu dispositivo Android
- Seleccione Configuración adicional e, a continuación, seleccione Accesibilidade
- Escolla o seu motor preferido, velocidade de voz e ton
- **Reinicie a aplicación Organic Maps**
- Abre Configuración => Instrucións de voz en Mapas orgánicos e configúrao
- Reinicie de novo a aplicación Organic Maps (ou reinicie o dispositivo) se a voz non funciona

Se non atopa a configuración relevante, abra a aplicación de configuración e busque Texto a voz.

P.S.: Ten en conta que estes pasos variarán segundo a marca do teléfono que esteas a usar.

É posible que ditas opcións non aparezan se non tes xa un TTS instalado no teu dispositivo. Consulte a seguinte táboa para instalar calquera deles que admita o seu idioma nativo.

## Capturas de pantalla

|             |             |
| ----------- | ----------- |
![Configuración](tts_config_1.png "Configuración") | ![Accesibilidade](tts_config_2.png "Accesibilidade")

## Motores {#motores}

A continuación móstrase unha lista completa que mostra varios motores e os idiomas que admiten (as ligazóns de descarga pódense atopar despois da táboa):

{{ tts_table() }}

## Solucións alternativas

Se tes problemas para inicializar o motor RHVoice TTS en LineageOS ou noutras ROM personalizadas, proba esta solución. É posible que RHVoice non se inicialice correctamente e que a aplicación poida fallar, especialmente se non utilizaches ningún motor TTS no teu teléfono antes (por exemplo, unha nova instalación, o restablecemento de fábrica, etc.). Se estás a usar unha ROM personalizada como LineageOS <ins>sen os servizos de Google Play e os servizos de voz de Google</ins>, e queres utilizar RHVoice como o teu motor TTS preferido, siga as instrucións a continuación como solución alternativa:

1. Instala o [motor eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak) dispoñible en F-Droid
2. Establéceo como o motor do sistema preferido
    - Vaia á **Configuración** principal de LineageOS.
    - Desprázate ata **Accesibilidade**.
    - Seleccione **saída de texto a voz** e **Motor preferido** (lado esquerdo) e asegúrese de que **eSpeak** estea seleccionado.
3. Volve atrás e preme **reproducir** para ver se está a funcionar
4. Instala [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) dispoñible en F-droid.
    - Ábreo, selecciona o idioma que queres usar, toca a icona da nube (extremo á esquerda) para descargar voces.
    - Preme o botón de reprodución para verificar se está a funcionar
5. Establece **RHVoice** como motor preferido (consulta o paso 2)
6. Agora, deberías poder usar RHVoice sen ningún problema

## Probas

Para probar as instrucións de voz, pode tocar "Probar indicacións de voz (TTS, texto a voz)" no menú "Configuración → Instrucións de voz" de OM ou pode iniciar unha navegación para recibir calquera saída de voz. Organic Maps non che dará instrucións de voz mentres esteas parado.

![Proba TTS](tts_test.png "Proba TTS")
