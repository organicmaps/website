---
title: Text a veu a Android
slug: text-a-veu-a-android
description: Guia sobre com fer que TTS funcioni a Android
taxonomies:
  faq:
  - voice-directions
extra:
  order: 10
aliases:
  - /ca/faq/voice/text-to-speech-android-tts/
---

## Resum

Organic Maps utilitza el motor de text a veu (TTS) del sistema per a instruccions de veu. Els motors predeterminats varien segons el dispositiu. Les opcions poden incloure Google Text-to-Speech, el motor del fabricant del dispositiu o un de tercers.

La recomanació oficial d'Organic Maps és [RHVoice](https://rhvoice.org/), que és un motor de veu gratuït i de codi obert que es pot descarregar de [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) i [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instruccions

- Obre l'aplicació Configuració al teu dispositiu Android
- Selecciona Configuració addicional i després selecciona Accessibilitat
- Tria el teu motor preferit, velocitat de parla i to
- **Reinicia l'aplicació Organic Maps**
- Obre Configuració => Instruccions de veu a Organic Maps i configura'l
- Reinicia l'aplicació Organic Maps de nou (o reinicia el dispositiu) si la veu no funciona

Si no trobes la configuració rellevant, obre l'aplicació de configuració i cerca Text a veu.

PD: Tingues en compte que aquests passos variaran en funció de la marca de telèfon que utilitzis.

És possible que aquestes opcions no apareguin si no tens un TTS ja instal·lat al teu dispositiu. Consulta la taula següent per instal·lar-ne qualsevol que admeti el teu idioma nadiu.

## Captures de pantalla

|             |             |
| ----------- | ----------- |
![Configuració](tts_config_1.png "Configuració") | ![Accessibilitat](tts_config_2.png "Accessibilitat")

## Motors {#engines}

A continuació es mostra una llista completa que mostra diversos motors i els idiomes que admeten (els enllaços de descàrrega es poden trobar després de la taula):

{{ tts_table() }}

## Solucions alternatives

Si tens problemes per inicialitzar el motor RHVoice TTS a LineageOS o altres ROM personalitzades, prova aquesta solució. És possible que RHVoice no s'inicialitzi correctament i que l'aplicació es bloquegi, sobretot si no has utilitzat cap motor TTS al teu telèfon abans (p. ex., una nova instal·lació, restabliment de fàbrica, etc.). Si utilitzes una ROM personalitzada com LineageOS <ins>sense els serveis de Google Play i els serveis de veu de Google</ins> i vols utilitzar RHVoice com a motor TTS preferit, segueix les instruccions següents com a solució alternativa:

1. Instal·la el [motor eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak) disponible a F-Droid
2. Configura'l com a motor del sistema preferit
    - Vés a la **Configuració** principal de LineageOS.
    - Desplaça't cap avall fins a **Accessibilitat**.
    - Selecciona **sortida de text a veu** i **motor preferit** (costat esquerre) i assegura't que **eSpeak** estigui seleccionat.
3. Torna enrere i prem **reproduir** per veure si funciona
4. Instal·la [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) disponible a F-droid.
    - Obre'l, selecciona l'idioma que vols utilitzar, toca la icona del núvol (extrem esquerre) per descarregar veus.
    - Prem el botó de reproducció per verificar si funciona
5. Estableix **RHVoice** com a motor preferit (mira el pas 2)
6. Ara, hauries de poder utilitzar RHVoice sense cap problema

## Prova

Per provar les instruccions de veu, pots tocar «Prova les indicacions de veu (TTS, text a veu)» al menú OM «Configuració → Instruccions de veu» o bé pots iniciar una navegació per rebre qualsevol sortida de veu. Organic Maps no et donarà instruccions de veu mentre estiguis parat.

![Prova TTS](tts_test.png "Prova TTS")
