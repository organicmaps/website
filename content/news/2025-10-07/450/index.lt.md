---
title: "Spalio 7 leidimas: greičio ribojimai Android Auto, GeoJSON importas, įrašomos trasos statistika, OSM description žymos rodymas, žymos išsaugojimas pasirinktoje trasoje iOS ir daugiau"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["releases"]
---

Šis spalio 7 d. Organic Maps atnaujinimas prideda greičio ribojimo rodymą Android Auto, GeoJSON importą, įrašomos trasos statistiką, rodo OSM aprašymo žymas (kad jas pamatytumėte, paieškos laukelyje įveskite `?description`) ir leidžia išsaugoti žymą ant trasos iOS. Taip pat yra daug naudotojo sąsajos ir OpenStreetMap redagavimo patobulinimų bei įvairių klaidų pataisymų visose platformose, įskaitant strigtį paleidžiant kai kuriuose Android įrenginiuose.

Organic Maps įmanomas ❤️ dėka bendradarbių, [jūsų aukų](@/donate/index.lt.md) ir [jūsų palaikymo](@/contribute/index.lt.md).

### Išsamios leidimo pastabos (įskaitant ankstesnio nedidelio atnaujinimo pakeitimus)

- NAUJA! GeoJSON importas (Sergiy Kozyr)
- OpenStreetMap duomenys nuo spalio 4 d.
- Wikipedia duomenys nuo spalio 1 d.
- Sietlo lengvojo geležinkelio palaikymas viešajame transporte (tjasz)
- Neišjungiamas žemėlapio pasirinkimas išsaugant redaguotą OSM vietą (Kiryl Kaveryn)
- Atnaujinti vertimai (Weblate bendradarbiai)

#### Žemėlapio stiliai

- Rodomos dviračių nuomos parduotuvės, pažymėtos amenity=bicycle + rental=shop (David Martinez)
- Istorinės archeologinės vietos rodomos nuo 12 mastelio, kitos istorinės vietos – nuo 15 mastelio Outdoor stiliuje (Viktor Govako)
- Naujos stiebų, ryšio ir elektros bokštų piktogramos Outdoors stiliuje (David Martinez)
- Padidinta viršukalnės piktograma Outdoors stiliuje (David Martinez)
- Pridėti trūkstami POI piktogramų variantai (David Martinez)
- Pridėta daugiau užtvarų tipų (Viktor Govako)

#### iOS

- NAUJA: žymos išsaugojimas pasirinktame trasos taške (Kiryl Kaveryn)
- NAUJA: įrašomos trasos ištrynimas jos prieš tai neišsaugant (Kiryl Kaveryn)
- Kelių eilučių žymų sąrašų pavadinimai vietos puslapyje (David Martinez)
- Atnaujintas OSM prisijungimo mygtukų stilius (Kiryl Kaveryn)
- Pataisytas navigacijos informacijos atnaujinimas (Kiryl Kaveryn)
- Pataisytos naujo maršruto planavimo klaidos (Kiryl Kaveryn)
- Pataisytas OSM vietos pridėjimo / redagavimo matomumas žemėlapiams, senesniems nei 3 mėnesiai (Kiryl Kaveryn)
- Pataisytas transporto parinkčių segmento valdiklio išdėstymas iOS 26 (Kiryl Kaveryn)
- Supaprastintos žymų pasirinkimo animacijos (Kiryl Kaveryn)
- Pataisyta paieškos rezultato pasirinkimo klaida (Kiryl Kaveryn)
- Pataisytas vietos informacijos puslapio stilius, braukimas ir animacijos (Kiryl Kaveryn)

#### Android Auto (tik Google Play)

- NAUJA: greičio ribojimo rodymas Android Auto (Andrei Shkrob)
- Pataisytas ekrano perjungimas Android Auto navigacijos režime (Andrei Shkrob)
- Pataisytas maršruto rodyklės poslinkis Android Auto (Andrei Shkrob)
- Pataisyta klaida prijungiant / atjungiant įrenginį prie automobilio (Andrei Shkrob)
- Pridėta Android Auto vietos nustatymo paslauga (Andrei Shkrob)
- Patobulintas Android Auto maršruto simuliatorius (Viktor Govako)

#### Android

- NAUJA: įrašomos trasos statistikos peržiūra realiuoju laiku (Kavi Khalique)
- NAUJA: rodomas OSM `description` žymos turinys (Alexander Borsuk)
- Pataisytas temos keitimo apdorojimas (Andrei Shkrob)
- Pataisytos kelios strigtys, tarp jų ir paleidimo metu (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Tylūs atsisiuntimo eigos pranešimai (Viktor Govako)
- Sumažinti pieštuko piktogramos tarpai (Alexander Borsuk)

#### Desktop

- Pataisytas užstringantis curl Linux sistemoje (Alexander Borsuk)
- Pataisytas užstrigimas macOS prisijungiant prie OSM (Alexander Borsuk)
- Objekto pasirinkimo veiksmas kontekstiniame meniu (Viktor Govako)
- Atsisiuntimo atšaukimo parinktis (Viktor Govako)
- Geometrijos tipo rodymas kontekstiniame meniu (Viktor Govako)

### Neseniai išleistos funkcijos, kurias galbūt praleidote

- Viešojo transporto maršrutų numeriai pasirinkus autobusų stotelę
- Žygių ir dviračių maršrutai (įjunkite juos Sluoksnių mygtuku kairėje viršuje)
- Žymų pavadinimus žemėlapyje pamatysite juos įjungę programėlės Nustatymuose
- ✎ pieštuko piktograma leidžia greitai redaguoti žymas

### Įdiekite Organic Maps

Atsisiųskite naujausią Organic Maps versiją iš [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ir [F-Droid][fdroid].

Prisijunkite prie beta testavimo, kad naujoves išbandytumėte anksčiau: [iOS][testflight] / [Android][firebase].

{{ references() }}
