---
title: Teksto į kalbą funkcija „Android“.
slug: teksto-į-kalbą-funkcija-android
description: Vadovas, kaip priversti TTS veikti „Android“.
taxonomies:
  faq:
  - voice-directions
extra:
  order: 10
aliases:
  - /lt/faq/voice/text-to-speech-android-tts/
---

## Santrauka

Organic Maps naudoja sistemos teksto į kalbą (TTS) variklį, kad pateiktų nurodymus balsu. Numatytieji varikliai skiriasi priklausomai nuo įrenginio. Galimi pasirinkimai: „Google“ tekstas į kalbą, įrenginio gamintojo variklis arba trečiosios šalies variklis.

Oficiali Organic Maps rekomendacija yra [RHVoice](https://rhvoice.org/), kuri yra nemokama atvirojo kodo kalbos variklis, kurį galima atsisiųsti iš [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) ir [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instrukcijos

– „Android“ įrenginyje atidaryk nustatymų programą
– Pasirink Papildomi nustatymai, tada – Prieinamumas
- Pasirink pageidaujamą variklį, kalbos greitį ir toną
- **Iš naujo paleisk Organic Maps programą**
- Atidaryk Nustatymai => Balso instrukcijos Organic Maps programėlėje ir nustatyk
- Jei balsas neveikia, iš naujo paleisk „Organic Maps“ programą (arba iš naujo paleisk įrenginį).

Jei nerandi atitinkamo nustatymo, atidaryk nustatymų programą ir ieškok Tekstas į kalbą.

P.S. Atmink, kad šie veiksmai skirsis priklausomai nuo tavo naudojamo telefono prekės ženklo.

Minėtos parinktys gali nebūti rodomos, jei tavo įrenginyje dar neįdiegta TTS. Norėdamas įdiegti bet kurį iš jų, palaikančių tavo gimtąją kalbą, žr. toliau pateiktą lentelę.

## Ekrano nuotraukos

|             |             |
| ------------ | ------------ |
![Nustatymai](tts_config_1.png "Nustatymai") ​​| ![Accessibility](tts_config_2.png "Prieinamumas")

## Varikliai {#engines}

Žemiau pateikiamas išsamus sąrašas, kuriame rodomi keli varikliai ir jų palaikomos kalbos (atsisiuntimo nuorodas rasi po lentele):

{{ tts_table() }}

## Sprendimai

Jei kyla problemų inicijuojant RHVoice TTS variklį LineageOS ar kituose tinkintuose ROM, išbandyk šį sprendimą. „RHVoice“ gali netinkamai inicijuoti ir programa gali sugesti, ypač jei anksčiau savo telefone nenaudojai jokio TTS variklio (pvz., naujai įdiegei, atkūrei gamyklinius nustatymus ir pan.). Jei naudoji tinkintą ROM, pvz., „LineageOS“, <ins>be „Google Play“ paslaugų ir „Google“ kalbėjimo paslaugų</ins> ir nori naudoti „RHVoice“ kaip pageidaujamą TTS variklį, vadovaukis toliau pateiktomis instrukcijomis.

1. Įdiek [eSpeak TTS modulį](https://f-droid.org/en/packages/com.reecedunn.espeak), pasiekiamą F-Droid
2. Nustatyk jį kaip pageidaujamą sistemos variklį
    - Eik į pagrindinį „LineageOS“ **Nustatymai**.
    - Slink žemyn iki **Prieinamumas**.
    – Pasirink **teksto į kalbą išvestis** ir **Preferred engine** (kairėje pusėje) ir įsitikink, kad pasirinkta **eSpeak**.
3. Grįžk atgal ir paspausk **play**, kad pamatytum, ar jis veikia
4. Įdiek [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/), pasiekiamą F-droid.
    - Atidaryk jį, pasirink kalbą, kurią nori naudoti, bakstelėk debesies piktogramą (kairėje), kad atsisiųstum balsus.
    - Paspausk paleidimo mygtuką, kad patikrintum, ar jis veikia
5. Nustatyk **RHVoice** kaip pageidaujamą variklį (žr. 2 veiksmą)
6. Dabar turėtum galėti naudoti RHVoice be jokių problemų

## Testavimas

Norėdamas išbandyti balso instrukcijas, OM meniu „Nustatymai → Balso instrukcijos“ gali bakstelėti „Balso nurodymų tikrinimas (TTS, tekstas į kalbą)“ arba iš tikrųjų gali pradėti navigaciją, kad gautum bet kokią balso išvestį. Organic Maps neduos jokių nurodymų balsu, kol stovi vietoje.

![TTS testas](tts_test.png "TTS testas")
