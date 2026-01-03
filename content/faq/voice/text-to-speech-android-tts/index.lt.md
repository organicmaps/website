---
title: Teksto į kalbą funkcija „Android“.
slug: teksto-į-kalbą-funkcija-android
description: Vadovas, kaip priversti TTS veikti „Android“.
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
aliases:
  - /lt/faq/voice/text-to-speech-android-tts/
---

## Santrauka

Natūralūs žemėlapiai naudoja sistemos teksto į kalbą (TTS) variklį, kad pateiktų nurodymus balsu. Numatytieji varikliai skiriasi priklausomai nuo įrenginio. Galimi pasirinkimai: „Google“ tekstas į kalbą, įrenginio gamintojo variklis arba trečiosios šalies variklis.

Oficiali organinių žemėlapių rekomendacija yra [RHVoice](https://rhvoice.org/), kuri yra nemokama atvirojo kodo kalbos variklis, kurį galima atsisiųsti iš [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) ir [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instrukcijos

– „Android“ įrenginyje atidarykite nustatymų programą
– Pasirinkite Papildomi nustatymai, tada – Prieinamumas
- Pasirinkite pageidaujamą variklį, kalbos greitį ir toną
- **Iš naujo paleiskite natūralių žemėlapių programą**
- Atidarykite Nustatymai => Balso instrukcijos organiniuose žemėlapiuose ir nustatykite
- Jei balsas neveikia, iš naujo paleiskite „Organic Maps“ programą (arba iš naujo paleiskite įrenginį).

Jei nerandate atitinkamo nustatymo, atidarykite nustatymų programą ir ieškokite Tekstas į kalbą.

P.S. Atminkite, kad šie veiksmai skirsis priklausomai nuo jūsų naudojamo telefono prekės ženklo.

Minėtos parinktys gali nebūti rodomos, jei jūsų įrenginyje dar neįdiegta TTS. Norėdami įdiegti bet kurį iš jų, palaikančių jūsų gimtąją kalbą, žr. toliau pateiktą lentelę.

## Ekrano nuotraukos

|             |             |
| ------------ | ------------ |
![Nustatymai](tts_config_1.png "Nustatymai") ​​| ![Accessibility](tts_config_2.png "Prieinamumas")

## Varikliai {#engines}

Žemiau pateikiamas išsamus sąrašas, kuriame rodomi keli varikliai ir jų palaikomos kalbos (atsisiuntimo nuorodas rasite po lentele):

{{ tts_table() }}

## Sprendimai

Jei kyla problemų inicijuojant RHVoice TTS variklį LineageOS ar kituose tinkintuose ROM, išbandykite šį sprendimą. „RHVoice“ gali netinkamai inicijuoti ir programa gali sugesti, ypač jei anksčiau savo telefone nenaudojote jokio TTS variklio (pvz., naujai įdiegėte, atkūrėte gamyklinius nustatymus ir pan.). Jei naudojate tinkintą ROM, pvz., „LineageOS“, <ins>be „Google Play“ paslaugų ir „Google“ kalbėjimo paslaugų</ins> ir norite naudoti „RHVoice“ kaip pageidaujamą TTS variklį, vadovaukitės toliau pateiktomis instrukcijomis.

1. Įdiekite [eSpeak TTS modulį] (https://f-droid.org/en/packages/com.reecedunn.espeak), pasiekiamą F-Droid
2. Nustatykite jį kaip pageidaujamą sistemos variklį
    - Eikite į pagrindinį „LineageOS“ **Nustatymai**.
    - Slinkite žemyn iki **Prieinamumas**.
    – Pasirinkite **teksto į kalbą išvestis** ir **Preferred engine** (kairėje pusėje) ir įsitikinkite, kad pasirinkta **eSpeak**.
3. Grįžkite atgal ir paspauskite **play**, kad pamatytumėte, ar jis veikia
4. Įdiekite [RHVoice] (https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/), pasiekiamą F-droid.
    - Atidarykite jį, pasirinkite kalbą, kurią norite naudoti, bakstelėkite debesies piktogramą (kairėje), kad atsisiųstumėte balsus.
    - Paspauskite paleidimo mygtuką, kad patikrintumėte, ar jis veikia
5. Nustatykite **RHVoice** kaip pageidaujamą variklį (žr. 2 veiksmą)
6. Dabar turėtumėte galėti naudoti RHVoice be jokių problemų

## Testavimas

Norėdami išbandyti balso instrukcijas, OM meniu „Nustatymai → Balso instrukcijos“ galite bakstelėti „Balso nurodymų tikrinimas (TTS, tekstas į kalbą)“ arba iš tikrųjų galite pradėti navigaciją, kad gautumėte bet kokią balso išvestį. Natūralūs žemėlapiai neduos jokių nurodymų balsu, kol stovite vietoje.

![TTS testas](tts_test.png "TTS testas")
