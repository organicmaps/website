---
title: Szövegfelolvasó Androidon
description: Útmutató a TTS működéséhez Androidon
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
---

## Összegzés

Az Organic Maps a rendszer text-to-speech (TTS) motorját használja hangutasításokhoz. Az alapértelmezett motorok eszközönként változnak. A lehetőségek között szerepelhet a Google Text-to Speech, az eszközgyártó motorja vagy egy harmadik fél motorja.

Az Organic Maps hivatalos ajánlása az [RHVoice](https://rhvoice.org/), amely egy ingyenes és nyílt forráskódú beszédmotor, amely letölthető a [Google Playről] (https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) és [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Útmutató

- Nyissa meg a Beállítások alkalmazást Android-eszközén
- Válassza a További beállítások, majd a Kisegítő lehetőségek lehetőséget
- Válassza ki a kívánt motort, beszédsebességet és hangmagasságot
- **Indítsa újra az Organic Maps alkalmazást**
- Nyissa meg a Beállítások => Hangutasításokat az Organikus térképekben, és állítsa be
- Indítsa újra az Organic Maps alkalmazást (vagy indítsa újra az eszközt), ha a hang nem működik

Ha nem találja a megfelelő beállítást, nyissa meg a beállítások alkalmazást, és keresse meg a Szövegfelolvasó lehetőséget.

Ui.: Vegye figyelembe, hogy ezek a lépések a használt telefon márkájától függően változnak.

Előfordulhat, hogy az említett opciók nem jelennek meg, ha még nincs TTS telepítve az eszközére. Kérjük, tekintse meg az alábbi táblázatot, hogy telepítse bármelyiket, amely támogatja az Ön anyanyelvét.

## Képernyőképek

|             |             |
| ----------- | ----------- |
![Beállítások](tts_config_1.png "Beállítások") | ![Accessibility](tts_config_2.png "Hozzáférhetőség")

## Motorok {#motorok}

Az alábbiakban egy átfogó lista több motort és az általuk támogatott nyelveket mutatja be (a letöltési hivatkozások a táblázat után találhatók):

{{ tts_table() }}

## Megoldások

Ha problémái vannak az RHVoice TTS motor inicializálásával LineageOS-en vagy más egyéni ROM-okon, próbálkozzon ezzel a megoldással. Előfordulhat, hogy az RHVoice nem inicializálódik megfelelően, és az alkalmazás összeomolhat, különösen, ha korábban nem használt TTS-motort a telefonon (pl. új telepítés, gyári beállítások visszaállítása stb.). Ha egyéni ROM-ot, például LineageOS-t használ <ins>a Google Play-szolgáltatások és a Google beszédszolgáltatásai nélkül</ins>, és az RHVoice-ot szeretné előnyben részesített TTS-motorként használni, megoldásként kövesse az alábbi utasításokat:

1. Telepítse az F-Droidon elérhető [eSpeak TTS motort] (https://f-droid.org/en/packages/com.reecedunn.espeak)
2. Állítsa be preferált rendszermotorként
    - Nyissa meg a LineageOS fő **Beállítások** részét.
    - Görgessen le a **Kisegítő lehetőségek** részhez.
    - Válassza a **szövegfelolvasó kimenet** és a **Preferált motor** (bal oldalon), és győződjön meg arról, hogy az **eSpeak** van kiválasztva.
3. Menjen vissza, és nyomja meg a **lejátszás** gombot, hogy ellenőrizze, működik-e
4. Telepítse az F-droidon elérhető [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) alkalmazást.
    - Nyissa meg, válassza ki a használni kívánt nyelvet, koppintson a felhő ikonra (bal szélen) a hangok letöltéséhez.
    - Nyomja meg a lejátszás gombot, hogy ellenőrizze, működik-e
5. Állítsa be az **RHVoice**-t preferált motorként (lásd a 2. lépést)
6. Most már minden probléma nélkül használhatja az RHVoice-ot

## Tesztelés

A hangutasítások teszteléséhez érintse meg a "Hangutasítások tesztelése (TTS, Text-To-Speech)" elemet az OM "Beállítások → Hangutasítások" menüben, vagy elindíthat egy navigációt bármilyen hangkimenet fogadásához. Az Organic Maps nem ad hangutasításokat, amíg Ön egy helyben áll.

![TTS-teszt](tts_test.png "TTS-teszt")
