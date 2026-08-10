---
title: Szövegfelolvasó Androidon
slug: szövegfelolvasó-androidon
description: Útmutató a TTS működéséhez Androidon
taxonomies:
  faq:
  - voice-directions
extra:
  order: 10
aliases:
  - /hu/faq/voice/text-to-speech-android-tts/
---

## Összegzés

Az Organic Maps a rendszer text-to-speech (TTS) motorját használja hangutasításokhoz. Az alapértelmezett motorok eszközönként változnak. A lehetőségek között szerepelhet a Google Text-to Speech, az eszközgyártó motorja vagy egy harmadik fél motorja.

Az Organic Maps hivatalos ajánlása az [RHVoice](https://rhvoice.org/), amely egy ingyenes és nyílt forráskódú beszédmotor, amely letölthető a [Google Playről](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) és [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Útmutató

- Nyisd meg a Beállítások alkalmazást az Android-eszközödön
- Válaszd a További beállítások, majd a Kisegítő lehetőségek lehetőséget
- Válaszd ki a kívánt motort, beszédsebességet és hangmagasságot
- **Indítsd újra az Organic Maps alkalmazást**
- Nyisd meg a Beállítások => Hangutasításokat az Organic Maps-ben, és állítsd be
- Indítsd újra az Organic Maps alkalmazást (vagy indítsd újra az eszközt), ha a hang nem működik

Ha nem találod a megfelelő beállítást, nyisd meg a beállítások alkalmazást, és keresd meg a Szövegfelolvasó lehetőséget.

Ui.: Vedd figyelembe, hogy ezek a lépések a használt telefon márkájától függően változnak.

Előfordulhat, hogy az említett opciók nem jelennek meg, ha még nincs TTS telepítve az eszközödre. Kérjük, tekintsd meg az alábbi táblázatot, hogy telepítsd bármelyiket, amely támogatja az anyanyelvedet.

## Képernyőképek

|             |             |
| ----------- | ----------- |
![Beállítások](tts_config_1.png "Beállítások") | ![Accessibility](tts_config_2.png "Hozzáférhetőség")

## Motorok {#engines}

Az alábbiakban egy átfogó lista több motort és az általuk támogatott nyelveket mutatja be (a letöltési hivatkozások a táblázat után találhatók):

{{ tts_table() }}

## Megoldások

Ha problémáid vannak az RHVoice TTS motor inicializálásával LineageOS-en vagy más egyéni ROM-okon, próbálkozz ezzel a megoldással. Előfordulhat, hogy az RHVoice nem inicializálódik megfelelően, és az alkalmazás összeomolhat, különösen, ha korábban nem használtál TTS-motort a telefonon (pl. új telepítés, gyári beállítások visszaállítása stb.). Ha egyéni ROM-ot, például LineageOS-t használsz <ins>a Google Play-szolgáltatások és a Google beszédszolgáltatásai nélkül</ins>, és az RHVoice-ot szeretnéd előnyben részesített TTS-motorként használni, megoldásként kövesd az alábbi utasításokat:

1. Telepítsd az F-Droidon elérhető [eSpeak TTS motort](https://f-droid.org/en/packages/com.reecedunn.espeak)
2. Állítsd be preferált rendszermotorként
    - Nyisd meg a LineageOS fő **Beállítások** részét.
    - Görgess le a **Kisegítő lehetőségek** részhez.
    - Válaszd a **szövegfelolvasó kimenet** és a **Preferált motor** (bal oldalon), és győződj meg arról, hogy az **eSpeak** van kiválasztva.
3. Menj vissza, és nyomd meg a **lejátszás** gombot, hogy ellenőrizd, működik-e
4. Telepítsd az F-droidon elérhető [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) alkalmazást.
    - Nyisd meg, válaszd ki a használni kívánt nyelvet, koppints a felhő ikonra (bal szélen) a hangok letöltéséhez.
    - Nyomd meg a lejátszás gombot, hogy ellenőrizd, működik-e
5. Állítsd be az **RHVoice**-t preferált motorként (lásd a 2. lépést)
6. Most már minden probléma nélkül használhatod az RHVoice-ot

## Tesztelés

A hangutasítások teszteléséhez érintsd meg a „Hangutasítások tesztelése (TTS, Text-To-Speech)“ elemet az OM „Beállítások → Hangutasítások“ menüben, vagy elindíthatsz egy navigációt bármilyen hangkimenet fogadásához. Az Organic Maps nem ad hangutasításokat, amíg egy helyben állsz.

![TTS-teszt](tts_test.png "TTS-teszt")
