---
title: Testun-i-Leferydd ar Android
slug: testun-i-leferydd-ar-android
description: Canllaw ar sut i wneud i TTS weithio ar Android
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
aliases:
  - /cy/faq/voice/text-to-speech-android-tts/
---

## Crynodeb

Mae Organic Maps yn defnyddio'r peiriant testun-i-leferydd system (TTS) ar gyfer cyfarwyddiadau llais. Mae'r peiriannau rhagosodedig yn amrywio yn ôl dyfais. Gall y dewisiadau gynnwys Google Text-to Speech, injan gwneuthurwr dyfeisiau neu un trydydd parti.

Yr argymhelliad swyddogol gan Organic Maps yw [RHVoice](https://rhvoice.org/), sef peiriant lleferydd ffynhonnell agored am ddim y gellir ei lawrlwytho o [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) a [F-Droid]( https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/ ).

## Cyfarwyddiadau

- Agorwch yr app Gosodiadau ar eich dyfais Android
- Dewiswch Gosodiadau Ychwanegol ac yna dewiswch Hygyrchedd
- Dewiswch eich hoff injan, cyfradd lleferydd a thraw
- **Ailgychwyn ap Mapiau Organig**
- Gosodiadau Agored => Cyfarwyddiadau Llais mewn Mapiau Organig a'i osod
- Ailgychwyn ap Mapiau Organig eto (neu ailgychwyn y ddyfais) os nad yw'r llais yn gweithio

Os na allwch ddod o hyd i'r gosodiad perthnasol, agorwch yr ap gosodiadau a chwiliwch am Testun-i-leferydd.

PS: Sylwch y bydd y camau hyn yn amrywio yn seiliedig ar y brand ffôn rydych chi'n ei ddefnyddio.

Mae'n bosibl na fydd yr opsiynau a ddywedwyd yn ymddangos os nad oes gennych TTS eisoes wedi'i osod ar eich dyfais. Cyfeiriwch at y tabl isod i osod unrhyw un ohonynt sy'n cefnogi eich iaith frodorol.

## Sgrinluniau

|             |             |
| ----------- | ----------- |
![Gosodiadau](tts_config_1.png "Gosodiadau") | ![Hygyrchedd](tts_config_2.png "Hygyrchedd")

## Peiriannau {#engines}

Isod mae rhestr gynhwysfawr yn dangos nifer o beiriannau a'r ieithoedd y maent yn eu cefnogi (gellir dod o hyd i ddolenni lawrlwytho ar ôl y tabl):

{{ tts_table() }}

## Workarounds

Os ydych chi'n cael trafferth cychwyn yr injan RHVoice TTS ar LineageOS neu ROMs arferol eraill, rhowch gynnig ar y datrysiad hwn. Efallai na fydd RHVoice yn cychwyn yn iawn a gall yr ap chwalu, yn enwedig os nad ydych wedi defnyddio unrhyw injan TTS ar eich ffôn o'r blaen (e.e., gosodiad newydd, ailosod ffatri, ac ati). Os ydych chi'n defnyddio ROM personol fel LineageOS <ins>heb wasanaethau Google Play a Gwasanaethau Lleferydd gan Google</ins>, a'ch bod am ddefnyddio RHVoice fel eich peiriant TTS dewisol, dilynwch y cyfarwyddiadau isod fel ateb:

1. Gosodwch yr [injan eSpeak TTS] ( https://f-droid.org/en/packages/com.reecedunn.espeak ) sydd ar gael ar F-Droid
2. Gosodwch ef fel yr injan system a ffefrir
    - Ewch i brif **Gosodiadau** LineageOS.
    - Sgroliwch i lawr i **Hygyrchedd**.
    - Dewiswch **allbwn testun-i-leferydd** a **Injan a ffefrir** (ochr chwith) a gwnewch yn siŵr bod **eSpeak** yn cael ei ddewis.
3. Ewch yn ôl a gwasgwch **chwarae** i weld a yw'n gweithio
4. Gosod [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) ar gael ar F-droid.
    - Agorwch hi, dewiswch yr iaith rydych chi am ei defnyddio, tapiwch eicon y cwmwl (chwith pellaf) i lawrlwytho lleisiau.
    - Pwyswch y botwm chwarae i wirio a yw'n gweithio
5. Gosod **RHVoice** fel yr injan ddewisol (gweler cam 2)
6. Nawr, dylech allu defnyddio RHVoice heb unrhyw broblemau

## Profi

Er mwyn profi'r cyfarwyddiadau llais, gallwch chi tapio ar "Test Voice Directions (TTS, Text-To-Speech)" yn newislen OM "Settings → Voice Instructions" neu gallwch chi ddechrau llywio i dderbyn unrhyw allbwn llais. Ni fydd Mapiau Organig yn rhoi unrhyw gyfarwyddiadau llais i chi tra byddwch yn sefyll yn llonydd.

![TTS Prawf](tts_test.png "Prawf TTS")
