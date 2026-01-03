---
title: Teks-na-spraak op Android
description: Gids oor hoe om TTS op Android te laat werk
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
---

## Opsomming

Organiese kaarte gebruik die stelsel teks-na-spraak (TTS)-enjin vir steminstruksies. Die verstek enjins verskil volgens toestel. Die keuses kan Google teks-na-spraak, toestelvervaardiger se enjin of 'n derdeparty een insluit.

Die amptelike aanbeveling van Organic Maps is [RHVoice](https://rhvoice.org/), wat 'n gratis en oopbron-spraakenjin is wat afgelaai kan word vanaf [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) en [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instruksies

- Maak die Instellings-toepassing op jou Android-toestel oop
- Kies Addisionele instellings en kies dan Toeganklikheid
- Kies jou voorkeurenjin, spraaktempo en toonhoogte
- ** Herbegin Organic Maps-toepassing**
- Maak instellings oop => steminstruksies in organiese kaarte en stel dit op
- Herbegin Organic Maps-toepassing weer (of herlaai die toestel) as die stem nie werk nie

As jy nie die toepaslike instelling kan kry nie, maak die instellingsprogram oop en soek vir Teks-na-spraak.

P.S: Let daarop dat hierdie stappe sal verskil na gelang van die telefoonhandelsmerk wat jy gebruik.

Genoemde opsies sal dalk nie verskyn as jy nie reeds 'n TTS op jou toestel geïnstalleer het nie. Verwys asseblief na die tabel hieronder om enige een daarvan te installeer wat jou moedertaal ondersteun.

## Skermkiekies

|             |             |
| ---------- | ---------- |
![Settings](tts_config_1.png "Instellings") | ![Toeganklikheid](tts_config_2.png "Toeganklikheid")

## Enjins {#enjins}

Hieronder is 'n omvattende lys met verskeie enjins en die tale wat hulle ondersteun (aflaaiskakels kan na die tabel gevind word):

{{ tts_table() }}

## Oplossings

As jy probleme ondervind om die RHVoice TTS-enjin op LineageOS of ander pasgemaakte ROM's te inisialiseer, probeer hierdie oplossing. RHVoice kan dalk nie behoorlik inisialiseer nie en die toepassing kan ineenstort, veral as jy nog nie voorheen enige TTS-enjin op jou foon gebruik het nie (bv. nuwe installasie, fabriekterugstelling, ens.). As jy 'n pasgemaakte ROM soos LineageOS <ins>sonder Google Play-dienste en Spraakdienste deur Google</ins> gebruik, en jy wil RHVoice as jou voorkeur-TTS-enjin gebruik, volg die instruksies hieronder as 'n oplossing:

1. Installeer die [eSpeak TTS-enjin](https://f-droid.org/en/packages/com.reecedunn.espeak) beskikbaar op F-Droid
2. Stel dit as die voorkeurstelselenjin
    - Gaan na LineageOS hoof **Instellings**.
    - Rollees af na **Toeganklikheid**.
    - Kies **teks-na-spraak-uitset** en **Voorkeurenjin** (linkerkant) en maak seker dat **eSpeak** gekies is.
3. Gaan terug en druk **speel** om te sien of dit werk
4. Installeer [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) beskikbaar op F-droid.
    - Maak dit oop, kies die taal wat jy wil gebruik, tik op die wolkikoon (heel links) om stemme af te laai.
    - Druk die speelknoppie om te verifieer of dit werk
5. Stel **RHVoice** as voorkeurenjin (sien stap 2)
6. Nou behoort jy RHVoice sonder enige probleme te kan gebruik

## Toets

Om die steminstruksies te toets, kan jy op "Toets stemaanwysings (TTS, teks-na-spraak)" in OM "Instellings → Steminstruksies"-kieslys tik of jy kan eintlik 'n navigasie begin om enige stemuitset te ontvang. Organiese kaarte sal jou geen steminstruksies gee terwyl jy stilstaan ​​nie.

![TTS-toets](tts_test.png "TTS-toets")
