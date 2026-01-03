---
title: Text-a-la-parla sus Android
slug: text-a-la-parla-sus-android
description: Guia sus cossí far foncionar lo TTS sus Android
taxonomies:
  faq:
  - Instruccions de votz
extra:
  order: 10
aliases:
  - /oc/faq/voice/text-to-speech-android-tts/
---

## Resumit

Organic Maps utiliza lo motor de sintèsi vocala (TTS) del sistèma per las instruccions vocalas. Los motors per defaut varian segon l'aparelh. Las causidas pòdon inclure Google Text-to-Speech, lo motor del fabricant de l'aparelh o un motor d'un tèrç.

La recomandacion oficiala d'Organic Maps es [RHVoice](https://rhvoice.org/), qu'es un motor de sintèsi vocala liure e de còdi font que se pòt telecargar dempuèi [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice. android) e [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instruccions

- Dobrissètz l'aplicacion Paramètres sus vòstre aparelh Android
- Seleccionatz Paramètres suplementaris puèi seleccionatz Accessibilitat
- Causissètz vòstre motor preferit, la velocitat de la paraula e lo ton
- **Reamodar l'aplicacion Organic Maps**
- Dobrissètz Paramètres => Instruccions vocalas dins Organic Maps e configuratz-las
- Reamodatz tornarmai l'aplicacion Organic Maps (o reamodatz lo dispositiu) se la votz fonciona pas

Se trobatz pas lo paramètre pertinent, dobrissètz l'aplicacion de paramètres e cercatz 'Text-to-speech'.

P.S: Notatz que las estapas poirián variar segon la marca de vòstre telefòn.

Aquestas opcions poirián pas aparéisser s'avètz pas ja un TTS installat sus vòstre aparelh. Consultatz la taula çaijós per installar un d'eles que supòrta vòstra lenga materna.

## Capturas d'ecran

|             |             |
| ----------- | ----------- |
![Paramètres](tts_config_1.png "Paramètres") | ![Accessibilitat](tts_config_2.png "Accessibilitat")

## Motors {#engines}

Çaijós trobaretz una lista completa que mòstra plusors motors e las lengas que supòrtan (los ligams de telecargament se tròban après la taula):

{{ tts_table() }}

## Solucions de contornament

S'avètz de problèmas per inicializar lo motor TTS RHVoice sus LineageOS o d'autras ROM personalizadas, ensajatz aquesta solucion de contornament. Es possible que RHVoice s'inicialize pas corrèctament e que l'aplicacion s'arrèste, especialament s'avètz pas jamai utilizat cap de motor TTS sus vòstre telefòn (per exemple, installacion novèla, restabliment d'usina, etc.). S'utilizatz una ROM personalizada coma LineageOS <ins>sens los servicis Google Play e los servicis de paraula de Google</ins>, e volètz utilizar RHVoice coma vòstre motor TTS preferit, seguissètz las instruccions çaijós coma solucion de contornament:

1. Installatz lo [motor TTS eSpeak](https://f-droid.org/en/packages/com.reecedunn.espeak) disponible sus F-Droid
2. Lo configurar coma motor preferit del sistèma
    - Anatz dins los **Paramètres** principals de LineageOS.
    - Desfilatz cap aval fins a **Accessibilitat**.
    - Seleccionatz **Sortida text-a-la-parla** e **Motor preferit** (costat esquèrre) e asseguratz-vos que **eSpeak** siá seleccionat.
3. Tornatz en arrièr e premetz sus **play** per veire se fonciona
4. Installatz [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) disponible sus F-droid.
    - Dobrissètz-lo, seleccionatz la lenga que volètz utilizar, picatz sus l'icòna del nívol (a l'extrèma esquèrra) per telecargar de voses.
    - Quichatz sul boton de lectura per verificar se fonciona
5. Configuratz **RHVoice** coma motor preferit (veire l'etapa 2)
6. Ara, deuriatz poder utilizar RHVoice sens cap de problèma

## Testatge

Per testar las instruccions vocalas, podètz picar sus « Testar las Directivas Vocalas (TTS, Tèxte-Vòs) » dins lo menú OM « Paramètres → Instruccions Vocalas » o podètz efectivament començar una navigacion per recebre una sortida vocala. Organic Maps vos donarà pas cap d'instruccion vocala quand sètz immobil.

![Tèst TTS](tts_test.png "Tèst TTS")