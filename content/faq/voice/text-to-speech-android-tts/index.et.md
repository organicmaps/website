---
title: Tekst kõneks muutmine Androidis
slug: tekst-kõneks-muutmine-androidis
description: Juhend selle kohta, kuidas TTS-i Androidis tööle panna
taxonomies:
  faq:
  - voice-directions
extra:
  order: 10
aliases:
  - /et/faq/voice/text-to-speech-android-tts/
---

## Kokkuvõte

Organic Maps kasutab hääljuhiste andmiseks süsteemi teksti kõneks muutmise (TTS) mootorit. Vaikimisi mootorid erinevad seadmeti. Valikuvõimalused võivad hõlmata Google'i kõnesünteesi, seadme tootja mootorit või kolmanda osapoole mootorit.

Organic Mapsi ametlik soovitus on [RHVoice](https://rhvoice.org/), mis on tasuta ja avatud lähtekoodiga kõnemootor, mille saab alla laadida saidilt [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) ja [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Juhised

- Ava oma Android-seadmes rakendus Seaded
- Vali Lisasätted ja seejärel Juurdepääsetavus
- Vali eelistatud mootor, kõne kiirus ja helikõrgus
- **Taaskäivita rakendus Organic Maps**
- Ava Organic Mapsis Seaded => Hääljuhised ja seadista see
- Kui hääl ei tööta, taaskäivita rakendus Organic Maps uuesti (või taaskäivita seade).

Kui sa ei leia asjakohast seadet, ava seadete rakendus ja otsi teksti kõneks muutmist.

P.S. Pane tähele, et need sammud sõltuvad sinu kasutatavast telefoni kaubamärgist.

Nimetatud valikuid ei pruugita kuvada, kui sinu seadmesse pole juba TTS-i installitud. Palun vaata allolevat tabelit, et installida mõni neist, mis toetab sinu emakeelt.

## Ekraanipildid

|             |             |
| ----------- | ----------- |
![Seaded](tts_config_1.png "Seaded") | ![Accessibility](tts_config_2.png "Juurdepääsetavus")

## Mootorid {#engines}

Allpool on põhjalik loend, mis näitab mitut mootorit ja nende toetatavaid keeli (allalaadimislingid leiad pärast tabelit):

{{ tts_table() }}

## Lahendused

Kui sul on probleeme RHVoice TTS-mootori käivitamisega LineageOS-is või muudes kohandatud ROM-ides, proovi seda lahendust. RHVoice ei pruugi korralikult lähtestada ja rakendus võib kokku jooksma, eriti kui sa pole varem oma telefonis ühtegi TTS-mootorit kasutanud (nt uus installimine, tehase lähtestamine jne). Kui kasutad kohandatud ROM-i, nagu LineageOS, <ins>ilma Google Play teenuste ja Google'i kõneteenusteta</ins> ning soovid kasutada RHVoice'i eelistatud TTS-mootorina, järgi lahendusena allolevaid juhiseid.

1. Installi F-Droidis saadaval olev [eSpeak TTS-mootor](https://f-droid.org/en/packages/com.reecedunn.espeak).
2. Määra see eelistatud süsteemimootoriks
    - Mine LineageOS-i põhimenüüsse **Seaded**.
    - Keri alla jaotiseni **Juurdepääsetavus**.
    - Vali **kõnesünteesi väljund** ja **Eelistatud mootor** (vasakul) ning veendu, et valitud on **eSpeak**.
3. Mine tagasi ja vajuta **esita**, et näha, kas see töötab
4. Installi [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/), mis on saadaval F-droidis.
    - Ava see, vali keel, mida soovid kasutada, puuduta häälte allalaadimiseks pilvikooni (vasakul).
    - Vajuta esitusnuppu, et kontrollida, kas see töötab
5. Määra eelistatud mootoriks **RHVoice** (vt 2. sammu)
6. Nüüd peaksid saama RHVoice'i probleemideta kasutada

## Testimine

Hääljuhiste testimiseks võid puudutada OM-i menüüs "Seaded → Hääljuhised" valikut "Testi hääljuhiseid (TTS, tekst kõneks muutmine)" või saad tegelikult alustada navigeerimist, et saada mis tahes häälväljundit. Organic Maps ei anna sulle paigal seistes hääljuhiseid.

![TTS-test](tts_test.png "TTS-test")
