---
title: "2026. aasta juuli värskenduses tehtud veaparandused ja täiustused seoses ühistranspordi, marsruutide planeerimise, otsingu ja järjehoidjatega"
date: 2026-07-23
slug: "veaparandused-taiustused-uhistransport-marsruudid-otsing-jarjehoidjad-juuli-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Nagu te ehk juba märkasite, on Organic Mapsi juulivärskendus väljas. Laadige see alla aadressilt <https://get.omaps.org> või poodidest [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ja [F-Droid][fdroid].

Tänu teie [annetustele](@/donate/index.et.md) ja [tagasisidele](@/contribute/index.et.md) keskendusime juulis veaparandustele ja täiustustele. Juhul, kui see jäi teil märkamata, on saadaval ka järgmised funktsioonid [eelmisest juuni versioonist](@/news/2026-06-29/610/index.et.md):
- Ühistranspordi marsruudid (reaalajas sõiduplaanid on väljatöötamisel)
- Satelliidipildid
- Alternatiivsed marsruudid autoga sõitmiseks, matkamiseks ja jalgrattasõiduks
- Androidi uus otsingu- ja marsruudiplaneerimise kasutajaliides
- iOSi tugi suurtele juurdepääsetavusfontidele

## Üksikasjalik muudatuste logi

### Kaart ja kohad
- OpenStreetMapi andmed on ajakohastatud seisuga 14. juuli
- [OpenStreetMapi](https://www.openstreetmap.org) edastatud märkused paigutatakse nüüd täpselt teie valitud kohale, mitte enam kogu tänava või piirkonna keskele _(Alexander Borsuk)_
- Parandatud kohavalik kaardile koputamisel piirkondades, mis ületavad 180° antimeridiaani _(Viktor Govako)_
- Radade kõrgusprofiilides ei kuvata enam aegunud ega tühje graafikuid pärast raja kustutamist _(Kiryl Kaveryn)_

### Ühistransport
- Peatuste, ümberistumiskohtade ja jaamade nimedel on nüüd valge ääris, et need oleksid loetavad nii heledas kui ka tumedas teemas _(Viktor Govako)_
- Pärast ühistranspordi marsruudi eelvaate sulgemist kuvatakse metrookiht uuesti õigesti _(Mikhail Listratsenka)_

### Marsruudi planeerimine ja navigeerimine
- Kõigi alternatiivsete marsruutide puhul kuvatakse nüüd marsruudihoiatusi (teemaksud, parvlaevad, kruusateed, astmed jne) _(Viktor Govako)_
- Parandati harva esinev süsteemi hangumine marsruudi koostamise ajal _(Viktor Govako)_
- Tõhusam umbteede ning piirangutega teede algus- ja lõpp-punktide käsitlemine _(Viktor Govako)_
- Parandati valesid ja puuduvaid pööramisjuhiseid _(Alexander Borsuk)_

### iOS
- Uus säte „Salvesta otsinguajalugu“, mis võimaldab ajaloo välja lülitada ja peita, kui te seda pigem säilitada ei soovi _(Kiryl Kaveryn)_
- Uus nupp „Muuda“, mis võimaldab järjehoidjaid hõlpsamalt eemaldada _(Kiryl Kaveryn)_
- Järjehoidjad salvestatakse nüüd automaatselt, kui ekraanilt lahkute _(Kiryl Kaveryn)_
- Värvipalett pakub nüüd eeldefineeritud värve ja võimaldab teil valida mistahes kohandatud värvi _(Kiryl Kaveryn)_
- Parandati salvestatud raja kõrgusgraafiku tühja olekut _(Kiryl Kaveryn)_
- Parandati „Start“-nupul kuvatavat marsruudi edenemist _(Kiryl Kaveryn)_
- Marsruudi peatuste järjekorra muutmine ei põhjusta enam nimekirja hüppamist _(Kiryl Kaveryn)_
- Muud väiksemad kasutajaliidese täiustused _(Kiryl Kaveryn)_

### Android
- Lahtiolekuajad näitavad nüüd jagatud vahetusi (näiteks lõunapausi), algavad tänasest päevast ning kuvavad kogu nädala ilma eraldi kerimisalata _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Ülevaatlikum otsinguriba, millel on ühendatud tühjendus- ja häälkäskluse nupp, tühjendusikoon, mis enam ei liigu, ning paigutuse parandused horisontaalrežiimi ja telefoni pööramise jaoks _(Mikhail Listratsenka)_
- Uuendatud järjehoidjate ja radade redaktor _(Mikhail Listratsenka)_
- Marsruudi planeerimise parandused ja täiustused _(Mikhail Listratsenka)_
- Värvivalija sulgub nüüd automaatselt ning parandati Android 5-s esinenud krahh _(Mikhail Listratsenka)_
- Parandatud krahhid _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- Allalaadimiseks saadaval olevate kaartide nimekiri on nüüd tähestikulises järjekorras _(goncalo109560)_

### Tõlked
- Parandatud hiinakeelne sõnastus _(Chenxi Zhao)_
- Ajakohastatud ukrainakeelsed tõlked _(Nnifria)_
- Parandati kaardipiirkondade nimede itaaliakeelseid tõlkeid _(Vittorio Bertola)_

## Liituge beetatestimisega, et proovida varajasi funktsioone ja teatada probleemidest:

Vihje: beetaversioonis on uus reljeefivarjutus, täiustatud kõrgusandmed, mis toetavad nii jalgu kui ka meetreid, ning muud lahedad funktsioonid!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Ilusat suve!
Organic Maps meeskond

{{ references() }}
