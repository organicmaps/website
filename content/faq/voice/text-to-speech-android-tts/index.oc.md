---
title: Text-a-la-parla sus Android
slug: text-a-la-parla-sus-android
description: Guia sus cossí far foncionar lo TTS sus Android
taxonomies:
  faq:
  - instruccions-de-votz
extra:
  order: 10
aliases:
  - /oc/faq/voice/text-to-speech-android-tts/
---

## Resumit

Organic Maps utiliza lo motor de sintèsi vocala (TTS) del sistèma per las instruccions vocalas. Los motors per defaut varian segon l'aparelh. Las causidas pòdon inclure Google Text-to-Speech, lo motor del fabricant de l'aparelh o un motor d'un tèrç.

La recomandacion oficiala d'Organic Maps es [RHVoice](https://rhvoice.org/), qu'es un motor de sintèsi vocala liure e de còdi font que se pòt telecargar dempuèi [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice. android) e [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instruccions

- Dobrís l'aplicacion Paramètres sus ton aparelh Android
- Selecciona Paramètres suplementaris puèi selecciona Accessibilitat
- Causís ton motor preferit, la velocitat de la paraula e lo ton
- **Reamodar l'aplicacion Organic Maps**
- Dobrís Paramètres => Instruccions vocalas dins Organic Maps e configura-las
- Reamoda tornarmai l'aplicacion Organic Maps (o reamoda lo dispositiu) se la votz fonciona pas

Se tròbas pas lo paramètre pertinent, dobrís l'aplicacion de paramètres e cerca 'Text-to-speech'.

P.S: Nòta que las estapas poirián variar segon la marca de ton telefòn.

Aquestas opcions poirián pas aparéisser s'as pas ja un TTS installat sus ton aparelh. Consulta la taula çaijós per installar un d'eles que supòrta ta lenga materna.

## Capturas d'ecran

|             |             |
| ----------- | ----------- |
![Paramètres](tts_config_1.png "Paramètres") | ![Accessibilitat](tts_config_2.png "Accessibilitat")

## Motors {#engines}

Çaijós trobaràs una lista completa que mòstra plusors motors e las lengas que supòrtan (los ligams de telecargament se tròban après la taula):

{{ tts_table() }}

## Solucions de contornament

S'as de problèmas per inicializar lo motor TTS RHVoice sus LineageOS o d'autras ROM personalizadas, ensaja aquesta solucion de contornament. Es possible que RHVoice s'inicialize pas corrèctament e que l'aplicacion s'arrèste, especialament s'as pas jamai utilizat cap de motor TTS sus ton telefòn (per exemple, installacion novèla, restabliment d'usina, etc.). S'utilizas una ROM personalizada coma LineageOS <ins>sens los servicis Google Play e los servicis de paraula de Google</ins>, e vòles utilizar RHVoice coma ton motor TTS preferit, seguís las instruccions çaijós coma solucion de contornament:

1. Installa lo [motor TTS eSpeak](https://f-droid.org/en/packages/com.reecedunn.espeak) disponible sus F-Droid
2. Lo configurar coma motor preferit del sistèma
    - Vai dins los **Paramètres** principals de LineageOS.
    - Desfila cap aval fins a **Accessibilitat**.
    - Selecciona **Sortida text-a-la-parla** e **Motor preferit** (costat esquèrre) e assegura-te que **eSpeak** siá seleccionat.
3. Torna en arrièr e prem sus **play** per veire se fonciona
4. Installa [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) disponible sus F-droid.
    - Dobrís-lo, selecciona la lenga que vòles utilizar, pica sus l'icòna del nívol (a l'extrèma esquèrra) per telecargar de voses.
    - Quicha sul boton de lectura per verificar se fonciona
5. Configura **RHVoice** coma motor preferit (veire l'etapa 2)
6. Ara, deuriás poder utilizar RHVoice sens cap de problèma

## Testatge

Per testar las instruccions vocalas, pòdes picar sus « Testar las Directivas Vocalas (TTS, Tèxte-Vòs) » dins lo menú OM « Paramètres → Instruccions Vocalas » o pòdes efectivament començar una navigacion per recebre una sortida vocala. Organic Maps te donarà pas cap d'instruccion vocala quand siás immobil.

![Tèst TTS](tts_test.png "Tèst TTS")