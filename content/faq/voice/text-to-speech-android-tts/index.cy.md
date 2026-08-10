---
title: Testun-i-Leferydd ar Android
slug: testun-i-leferydd-ar-android
description: Canllaw ar sut i wneud i TTS weithio ar Android
taxonomies:
  faq:
  - voice-directions
extra:
  order: 10
aliases:
  - /cy/faq/voice/text-to-speech-android-tts/
---

## Crynodeb

Mae Organic Maps yn defnyddio'r peiriant testun-i-leferydd system (TTS) ar gyfer cyfarwyddiadau llais. Mae'r peiriannau rhagosodedig yn amrywio yn ôl dyfais. Gall y dewisiadau gynnwys Google Text-to Speech, injan gwneuthurwr dyfeisiau neu un trydydd parti.

Yr argymhelliad swyddogol gan Organic Maps yw [RHVoice](https://rhvoice.org/), sef peiriant lleferydd ffynhonnell agored am ddim y gellir ei lawrlwytho o [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) a [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Cyfarwyddiadau

- Agora'r app Gosodiadau ar dy ddyfais Android
- Dewisa Gosodiadau Ychwanegol ac yna dewisa Hygyrchedd
- Dewisa dy hoff injan, cyfradd lleferydd a thraw
- **Ailgychwyn ap Organic Maps**
- Gosodiadau Agored => Cyfarwyddiadau Llais yn Organic Maps a'i osod
- Ailgychwyn ap Organic Maps eto (neu ailgychwyn y ddyfais) os nad yw'r llais yn gweithio

Os na elli ddod o hyd i'r gosodiad perthnasol, agora'r ap gosodiadau a chwilia am Testun-i-leferydd.

PS: Sylwa y bydd y camau hyn yn amrywio yn seiliedig ar y brand ffôn rwyt ti'n ei ddefnyddio.

Mae'n bosibl na fydd yr opsiynau a ddywedwyd yn ymddangos os nad oes gennyt TTS eisoes wedi'i osod ar dy ddyfais. Cyfeiria at y tabl isod i osod unrhyw un ohonynt sy'n cefnogi dy iaith frodorol.

## Sgrinluniau

|             |             |
| ----------- | ----------- |
![Gosodiadau](tts_config_1.png "Gosodiadau") | ![Hygyrchedd](tts_config_2.png "Hygyrchedd")

## Peiriannau {#engines}

Isod mae rhestr gynhwysfawr yn dangos nifer o beiriannau a'r ieithoedd y maent yn eu cefnogi (gellir dod o hyd i ddolenni lawrlwytho ar ôl y tabl):

{{ tts_table() }}

## Workarounds

Os wyt ti'n cael trafferth cychwyn yr injan RHVoice TTS ar LineageOS neu ROMs arferol eraill, rho gynnig ar y datrysiad hwn. Efallai na fydd RHVoice yn cychwyn yn iawn a gall yr ap chwalu, yn enwedig os nad wyt wedi defnyddio unrhyw injan TTS ar dy ffôn o'r blaen (e.e., gosodiad newydd, ailosod ffatri, ac ati). Os wyt ti'n defnyddio ROM personol fel LineageOS <ins>heb wasanaethau Google Play a Gwasanaethau Lleferydd gan Google</ins>, a dy fod am ddefnyddio RHVoice fel dy beiriant TTS dewisol, dilyna'r cyfarwyddiadau isod fel ateb:

1. Gosoda'r [injan eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak) sydd ar gael ar F-Droid
2. Gosoda ef fel yr injan system a ffefrir
    - Dos i brif **Gosodiadau** LineageOS.
    - Sgrolia i lawr i **Hygyrchedd**.
    - Dewisa **allbwn testun-i-leferydd** a **Injan a ffefrir** (ochr chwith) a gwna'n siŵr bod **eSpeak** yn cael ei ddewis.
3. Dos yn ôl a gwasga **chwarae** i weld a yw'n gweithio
4. Gosod [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) ar gael ar F-droid.
    - Agora hi, dewisa'r iaith rwyt ti am ei defnyddio, tapia eicon y cwmwl (chwith pellaf) i lawrlwytho lleisiau.
    - Pwysa'r botwm chwarae i wirio a yw'n gweithio
5. Gosod **RHVoice** fel yr injan ddewisol (gweler cam 2)
6. Nawr, dylet allu defnyddio RHVoice heb unrhyw broblemau

## Profi

Er mwyn profi'r cyfarwyddiadau llais, gelli di tapio ar ‘Test Voice Directions (TTS, Text-To-Speech)’ yn newislen OM ‘Settings → Voice Instructions’ neu gelli di ddechrau llywio i dderbyn unrhyw allbwn llais. Ni fydd Organic Maps yn rhoi unrhyw gyfarwyddiadau llais i ti tra byddi'n sefyll yn llonydd.

![TTS Prawf](tts_test.png "Prawf TTS")
