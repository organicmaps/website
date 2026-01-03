---
title: Tekst kõneks muutmine Androidis
slug: tekst-kõneks-muutmine-androidis
description: Juhend selle kohta, kuidas TTS-i Androidis tööle panna
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
aliases:
  - /et/faq/voice/text-to-speech-android-tts/
---

## Kokkuvõte

Organic Maps kasutab hääljuhiste andmiseks süsteemi teksti kõneks muutmise (TTS) mootorit. Vaikimisi mootorid erinevad seadmeti. Valikuvõimalused võivad hõlmata Google'i kõnesünteesi, seadme tootja mootorit või kolmanda osapoole mootorit.

Organic Mapsi ametlik soovitus on [RHVoice](https://rhvoice.org/), mis on tasuta ja avatud lähtekoodiga kõnemootor, mille saab alla laadida saidilt [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) ja [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Juhised

- Avage oma Android-seadmes rakendus Seaded
- Valige Lisasätted ja seejärel Juurdepääsetavus
- Valige eelistatud mootor, kõne kiirus ja helikõrgus
- **Taaskäivitage rakendus Organic Maps**
- Avage orgaanilistes kaartides Seaded => Hääljuhised ja seadistage see
- Kui hääl ei tööta, taaskäivitage rakendus Organic Maps uuesti (või taaskäivitage seade).

Kui te ei leia asjakohast seadet, avage seadete rakendus ja otsige teksti kõneks muutmist.

P.S. Pange tähele, et need sammud sõltuvad teie kasutatavast telefoni kaubamärgist.

Nimetatud valikuid ei pruugita kuvada, kui teie seadmesse pole juba TTS-i installitud. Palun vaadake allolevat tabelit, et installida mõni neist, mis toetab teie emakeelt.

## Ekraanipildid

|             |             |
| ----------- | ----------- |
![Seaded](tts_config_1.png "Seaded") | ![Accessibility](tts_config_2.png "Juurdepääsetavus")

## Mootorid {#mootorid}

Allpool on põhjalik loend, mis näitab mitut mootorit ja nende toetatavaid keeli (allalaadimislingid leiate pärast tabelit):

{{ tts_table() }}

## Lahendused

Kui teil on probleeme RHVoice TTS-mootori käivitamisega LineageOS-is või muudes kohandatud ROM-ides, proovige seda lahendust. RHVoice ei pruugi korralikult lähtestada ja rakendus võib kokku jooksma, eriti kui te pole varem oma telefonis ühtegi TTS-mootorit kasutanud (nt uus installimine, tehase lähtestamine jne). Kui kasutate kohandatud ROM-i, nagu LineageOS, <ins>ilma Google Play teenuste ja Google'i kõneteenusteta</ins> ning soovite kasutada RHVoice'i eelistatud TTS-mootorina, järgige lahendusena allolevaid juhiseid.

1. Installige F-Droidis saadaval olev [eSpeak TTS-mootor](https://f-droid.org/en/packages/com.reecedunn.espeak).
2. Määrake see eelistatud süsteemimootoriks
    - Minge LineageOS-i põhimenüüsse **Seaded**.
    - Kerige alla jaotiseni **Juurdepääsetavus**.
    - Valige **kõnesünteesi väljund** ja **Eelistatud mootor** (vasakul) ning veenduge, et valitud on **eSpeak**.
3. Minge tagasi ja vajutage **esita**, et näha, kas see töötab
4. Installige [RHVoice] (https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/), mis on saadaval F-droidis.
    - Avage see, valige keel, mida soovite kasutada, puudutage häälte allalaadimiseks pilvikooni (vasakul).
    - Vajutage esitusnuppu, et kontrollida, kas see töötab
5. Määrake eelistatud mootoriks **RHVoice** (vt 2. sammu)
6. Nüüd peaksite saama RHVoice'i probleemideta kasutada

## Testimine

Hääljuhiste testimiseks võite puudutada OM-i menüüs "Seaded → Hääljuhised" valikut "Testi hääljuhiseid (TTS, tekst kõneks muutmine)" või saate tegelikult alustada navigeerimist, et saada mis tahes häälväljundit. Orgaanilised kaardid ei anna teile paigal seistes hääljuhiseid.

![TTS-test](tts_test.png "TTS-test")
