---
title: Kaip galiu atlikti sudėtingesnį žemėlapio redagavimą?
slug: kaip-galiu-atlikti-sudėtingesnį-žemėlapio-redagavimą
description: „OpenStreetMap“ redagavimo naudojant pažangesnius įrankius, pvz., ID,
  „Go Map“ ir „Vespucci“ mokymo programa
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
aliases:
  - /lt/faq/editing/advanced-map-editing/
---

Organiniuose žemėlapiuose yra paprastas ir lengvai naudojamas redaktorius, kurį galite naudoti norėdami redaguoti žemėlapį. Tačiau redaktorius yra ribotas ir leidžia pridėti tik paprastų taškų ypatybių, t.

Kadangi visi natūraliuose žemėlapiuose naudojami žemėlapio duomenys gaunami iš [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), čia galite tiesiogiai atnaujinti žemėlapį. Tada jūsų pakeitimai bus įtraukti į natūralius žemėlapius su kitu žemėlapio atnaujinimu.

## OpenStreetMap redaktoriai

OSM redagavimui yra keletas parinkčių. Jei po ranka turite nešiojamąjį ar stalinį kompiuterį, geriau naudokite [ID redaktorių] (https://www.openstreetmap.org/edit), kuris veikia jūsų naršyklėje. ID redaktorius yra paprastas pradedantiesiems, o didesnis ekranas, pelė ir klaviatūra palengvina žemėlapio redagavimą.

Jei norite išplėsti žemėlapio redagavimą mobiliajame įrenginyje, naudokite [Go Map](https://apps.apple.com/us/app/go-map/id592990211), skirtą „iOS“, arba [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android), skirtą „Android“. „Go Map“ yra lengvas pradedantiesiems, o „Vespucci“ skirtas labiau pažengusiems vartotojams. LearnOSM teikia mokymo programas, skirtas [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) ir [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Jei norite paprastesnio ir smagiau redagavimo, taip pat galite išbandyti [Every Door programą] (https://every-door.app/), skirtą „iOS“ ir „Android“, ir [programėlę „StreetComplete“](https://streetcomplete.app/), skirtą „Android“.

#### ID redaktorius

Norėdami redaguoti OpenStreetMap su ID, atlikite šiuos veiksmus:

1. Sukurkite naują paskyrą arba prisijunkite adresu [OpenStreetMap.org](https://www.openstreetmap.org)
2. OpenStreetMap.org suraskite vietą, kurią norite redaguoti, ir viršuje spustelėkite *Redaguoti*
3. *Pradėkite apžvalgą* ir vadovaukitės trumpa pamoka, kurioje paaiškinama ID redaktorius
4. Redaguokite žemėlapį
5. Įkelkite pakeitimus

Viskas, dabar esate OSM bendruomenės dalis.

## Kas atsitiks su mano pakeitimais?

Kai paspausite *Įkelti*, jūsų pakeitimai akimirksniu įtraukiami į viešąją OSM duomenų bazę. Taigi redaguodami būkite atidūs. Natūraliuose žemėlapiuose jūsų pakeitimai bus matomi po kito mėnesio žemėlapio atnaujinimo.

Jūsų el. paštas neskelbiamas, bet kiti žmonės galės matyti jūsų OSM vartotojo vardą. Kadangi OSM suteikia galimybę aptarti pakeitimus, galite sulaukti klausimų apie savo pakeitimus iš kitų OSM bendradarbių. Apie tai jums bus pranešta el. pašto adresu, kurį naudojote registruodami savo OSM paskyrą. Kadangi OSM yra bendruomenės projektas, pagrįstas bendradarbiavimu, visada turėtumėte atsakyti į tokius klausimus.

## Bendruomenė ir Wiki

OpenStreetMap yra bendruomenė. Jei jums reikia pagalbos arba turite klausimų, galite užduoti [OSM forume] (https://community.openstreetmap.org/c/help-and-support) arba peržiūrėti [OSM Wiki] (https://wiki.openstreetmap.org/) dokumentaciją.

## Žymos – kaip veikia OSM duomenų modelis

„OpenStreetMap“ duomenų bazėje yra tokių objektų kaip mazgai, keliai, sritys ir ryšiai, kurie atsiriboja nuo realaus pasaulio funkcijų. Šie objektai turi atributų, vadinamųjų žymų, skirtų toliau juos apibūdinti. Žyma yra rakto ir vertės derinys.

Kadangi tai skamba sudėtingiau nei yra, pateiksime pavyzdį:
Restoranas yra pvz. susietas kaip pastaba arba sritis su žyma `amenity=restaurant`. Tada galima naudoti kitas žymas, pvz., `cuisine=*` arba `opening_hours=*`, kad gautumėte daugiau informacijos.

> Atminkite, kad ID redaktorius slepia vidinę duomenų struktūrą nuo vartotojų, kad būtų patogesnis pradedantiesiems. Tačiau norint skaityti Wiki dokumentaciją, naudinga trumpa duomenų struktūros apžvalga.
ID redagavimo priemonėje galite matyti žymas, kurias ID nuo jūsų slepia, išplėsdami skyrių *Žymos* šoniniame *Redagavimo funkcijos* skydelyje.

## OSM pastabos {#osm-note}

Jei neturite laiko arba problema per daug sudėtinga, kad galėtumėte patys redaguoti OSM duomenis, reikia naudoti OSM pastabas ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)). Galite įdėti tokį užrašą žemėlapio klaidos vietoje ir išsamiai aprašyti problemą. Tada kiti OSM savanoriai gali padėti ir išspręsti problemą. Jei kils daugiau klausimų arba OSM pastaba bus išspręsta, per savo OSM paskyrą gausite pranešimus el. paštu.

1. Sukurkite naują paskyrą arba prisijunkite adresu [OpenStreetMap.org](https://www.openstreetmap.org)
   > Taip pat galite atidaryti anoniminius užrašus, bet tai nerekomenduojama, nes negausite pranešimo, kai problema bus išspręsta arba kils daugiau klausimų.
2. Padidinkite žemėlapio vietą [OpenStreetMap.org] (https://www.openstreetmap.org) ir paspauskite *Pridėti pastabą į žemėlapį* (antra piktograma iš apačios dešiniajame meniu). Tada vilkite mėlyną žemėlapio žymeklį į tikslią vietą.
   > Stenkitės būti kuo tikslesni.
3. Pateikite išsamų žemėlapio problemos aprašymą ir paspauskite *Pridėti pastabą*
   > Parduotuvėms pvz. nurodykite pavadinimą ir paminėkite, kas ten parduodama ar kokios paslaugos siūlomos.
