---
title: Text a veu a Android
description: Guia sobre com fer que TTS funcioni a Android
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
---

## Resum

Organic Maps utilitza el motor de text a veu (TTS) del sistema per a instruccions de veu. Els motors predeterminats varien segons el dispositiu. Les opcions poden incloure Google Text-to-Speech, el motor del fabricant del dispositiu o un de tercers.

La recomanació oficial d'Orgànic Maps és [RHVoice](https://rhvoice.org/), que és un motor de veu gratuït i de codi obert que es pot descarregar de [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) i [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instruccions

- Obriu l'aplicació Configuració al vostre dispositiu Android
- Seleccioneu Configuració addicional i després seleccioneu Accessibilitat
- Trieu el vostre motor preferit, velocitat de parla i to
- **Reinicia l'aplicació Organic Maps**
- Obriu Configuració => Instruccions de veu a Mapes orgànics i configureu-lo
- Reinicieu l'aplicació Organic Maps de nou (o reinicieu el dispositiu) si la veu no funciona

Si no trobeu la configuració rellevant, obriu l'aplicació de configuració i cerqueu Text a veu.

PD: Tingueu en compte que aquests passos variaran en funció de la marca de telèfon que utilitzeu.

És possible que aquestes opcions no apareguin si no teniu un TTS ja instal·lat al vostre dispositiu. Consulteu la taula següent per instal·lar-ne qualsevol que admeti el vostre idioma nadiu.

## Captures de pantalla

|             |             |
| ----------- | ----------- |
![Configuració](tts_config_1.png "Configuració") | ![Accessibilitat](tts_config_2.png "Accessibilitat")

## Motors {#motors}

A continuació es mostra una llista completa que mostra diversos motors i els idiomes que admeten (els enllaços de descàrrega es poden trobar després de la taula):

{{ tts_table() }}

## Solucions alternatives

Si teniu problemes per inicialitzar el motor RHVoice TTS a LineageOS o altres ROM personalitzades, proveu aquesta solució. És possible que RHVoice no s'inicialitzi correctament i que l'aplicació es bloquegi, sobretot si no heu utilitzat cap motor TTS al vostre telèfon abans (p. ex., una nova instal·lació, restabliment de fàbrica, etc.). Si utilitzeu una ROM personalitzada com LineageOS <ins>sense els serveis de Google Play i els serveis de veu de Google</ins> i voleu utilitzar RHVoice com a motor TTS preferit, seguiu les instruccions següents com a solució alternativa:

1. Instal·leu el [motor eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak) disponible a F-Droid
2. Configureu-lo com a motor del sistema preferit
    - Aneu a la **Configuració** principal de LineageOS.
    - Desplaceu-vos cap avall fins a **Accessibilitat**.
    - Seleccioneu **sortida de text a veu** i **motor preferit** (costat esquerre) i assegureu-vos que **eSpeak** estigui seleccionat.
3. Torneu enrere i premeu **reproduir** per veure si funciona
4. Instal·leu [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) disponible a F-droid.
    - Obriu-lo, seleccioneu l'idioma que voleu utilitzar, toqueu la icona del núvol (extrem esquerre) per descarregar veus.
    - Premeu el botó de reproducció per verificar si funciona
5. Establiu **RHVoice** com a motor preferit (vegeu el pas 2)
6. Ara, hauríeu de poder utilitzar RHVoice sense cap problema

## Prova

Per provar les instruccions de veu, podeu tocar "Prova les indicacions de veu (TTS, text a veu)" al menú OM "Configuració → Instruccions de veu" o bé podeu iniciar una navegació per rebre qualsevol sortida de veu. Organic Maps no us donarà instruccions de veu mentre esteu parat.

![Prova TTS](tts_test.png "Prova TTS")
