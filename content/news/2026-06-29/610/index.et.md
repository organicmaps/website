---
title: "Satelliidipildid, ühistranspordi marsruudid, alternatiivsed marsruudid, uus otsingu ja marsruudi planeerimise liides Androidile, suurte kirjasuuruste juurdepääsetavuse tugi iOS-is ning palju muud juuni 2026 värskenduses"
date: 2026-06-29
slug: "satelliidipildid-uhistranspordi-marsruudid-alternatiivsed-marsruudid-uus-otsingu-ja-marsruudi-planeerimise-liides-androidile-suurte-kirjasuuruste-juurdepaasetavuse-tugi"
taxonomies:
  news: ["releases"]
---

Organic Mapsi juunikuu värskenduses on palju põnevaid uusi funktsioone ja veaparandusi, mida proovida, sealhulgas:
- Satelliidipildid
- Ühistranspordi marsruudid
- Alternatiivsed marsruudid
- Uus otsingu ja marsruudi planeerimise liides Androidile
- Suurte kirjasuuruste juurdepääsetavuse tugi iOS-is

Saad uuenduse aadressilt <https://get.omaps.org> või [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ja [F-Droid][fdroid], ning anna teada, mida arvad!

## Üksikasjalik muudatuste logi

- UUS! Ühistranspordi marsruutide arvutamine metroo, kergraudtee, bussi ja trammiga _(Viktor Govako)_
- UUS! Alternatiivsed marsruudid: lisaks kiireimale marsruudile näitab rakendus nüüd ka lühimat marsruuti _(Viktor Govako)_
- UUS! Jalgsi- ja jalgrattamarsruutide hoiatused teel olevate treppide, väravate ja tõkkepuude kohta _(Viktor Govako)_
- UUS! Vali järjehoidjatele mis tahes värv _(Alexander Borsuk, Mikhail Listratsenka)_
- UUS! British National Grid (OS Grid), Irish Grid ja Irish Transverse Mercator (ITM) koordinaatide tugi _(Alexander Borsuk)_
- EKSPERIMENTAALNE: luba Organic Maps seadetes satelliidipildid kohandatud rasterkaarditükkide serveri URL-iga. Töötame endiselt oma serveri kallal, seega leia palun avalikult kättesaadav server, mille URL-is on kohatäited `{x}`, `{y}`, `{z}` _(Viktor Govako, renderexpert)_
- OpenStreetMapi andmed uuendatud 24. juuni seisuga _(Viktor Govako)_
- Wikipedia andmed uuendatud 20. juuni seisuga, sealhulgas itaaliakeelsed artiklid _(Alexander Borsuk)_
- Sisesta otsinguaknasse `?map-download-server:https://your-server.com/`, et asendada Organic Maps kaartide allalaadimisserverid. Asenduse eemaldamiseks sisesta `?no-map-download-server` _(Alexander Borsuk)_

#### Kaardi renderdamine ja stiilid

- Ilusamad mustrid ranna-, liiva-, rusukalde-, palja kalju, viljapuuaia- ja viinamarjaistanduse aladele ning kaitsealade ja märgalade viirutus _(Alexander Borsuk)_
- Sujuvamad kumerad tekstisildid teedel ja jõgedel _(Viktor Govako)_
- Jõed, ojad ja märgalad on tumedas režiimis kontrastsemad ja paremini nähtavad _(Alexander Borsuk)_
- Uued ja täiustatud ikoonid kategooriaotsingu ja kaardil kuvatavate otsingutulemuste jaoks _(Anton Makouski)_
- Täiustatud mitmekeelse teksti vormimist ja renderdamist _(Alexander Borsuk)_
- Mitmesugused veaparandused ja jõudluse täiustused _(Viktor Govako)_

#### Rajad, järjehoidjad ja marsruudid

- GeoJSON-rajad säilitavad nüüd importimisel ja eksportimisel kõrgusandmed ja ajatemplid _(Alexander Borsuk)_
- Parandatud krahh pärast raja teisaldamist teise loendisse _(Viktor Govako)_
- Pärandipaikade puhul kuvatakse nüüd veebisaite _(Viktor Govako)_
- Nimetute otsingutulemuste puhul kuvatakse nüüd operaatori nimi. Näiteks näitab nimetu pangaautomaat nüüd panga nime _(Anton Makouski)_
- Redaktor: parandatud kortermajade OpenStreetMap muudatuste/muudatuskogumite kirjeldusteksti _(titanniya542-spec)_
- Täiustatud HTML-i tuvastamist järjehoidjate ja radade kirjeldustes _(Alexander Borsuk)_

### iOS

- UUS! Juurdepääsetavuse tugi Dynamic Type'ile ja suurtele kirjasuurustele _(Kiryl Kaveryn)_
- UUS! Puuduta, et valida kattuvate radade ja marsruutide vahel _(Kiryl Kaveryn)_
- Täiustatud järjehoidjate ja radade kirjelduste HTML-i renderdamist _(Kiryl Kaveryn)_
- Puhtam tabelite kujundus kasutajaliideses _(Kiryl Kaveryn)_

### Android

- UUS! Otsinguliides _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- UUS! Marsruudi planeerimise liides _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Täiustatud järjehoidjate ja radade kirjelduste HTML-i renderdamist _(Mikhail Listratsenka)_
- Vähendatud APK suurust _(Alexander Borsuk)_
- Hääleikoon kuvatakse keelatuna, kui kõnesünteesi mootor pole saadaval _(Mikhail Listratsenka)_
- Pikkade järjehoidjate ja radade kirjelduste puhul kuvatakse nüüd nupp „…veel“ _(Mikhail Listratsenka)_
- Mitmesugused kasutajaliidese parandused ja API parandus tagastatud punktide ID-de jaoks _(Mikhail Listratsenka)_

### Desktop

- Kuvatava koordinaatsüsteemi vahetamise tugi _(Alexander Borsuk)_
- Valitud koha teave kuvatakse nüüd vasakul _(Viktor Govako)_
- Parandatud kontekstimenüü asukoht _(Osyotr)_
- Parandatud OpenStreetMapi sisselogimise ja muudatuste hangumine Qt versioonides 6.4 ja varasemates _(Alexander Borsuk)_
- Parandatud ootamatu kaardistiili vahetumine marsruutimise ajal macOS-is _(Alexander Borsuk)_
- Parandatud krahh macOS-i rakenduse sulgemisel pärast KMZ-faili eksportimist _(Alexander Borsuk)_

### Tõlked

- Kantonikeelsed samm-sammulised hääljuhised _(Alexander Borsuk)_
- Uuendatud saksa ja prantsuse tõlked _(Wuzzy, Alexander Borsuk)_
- Parandatud hiina, serbia ja katalaani keele valed hääljuhiste tõlked fraasile „onto street“ _(Alexander Borsuk)_

## Liitu beetatestimisega, et proovida varajasi funktsioone ja teatada probleemidest:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Oleme tänulikud kõigile meie kasutajatele ja panustajatele, neile, kes [annetavad](@/donate/index.et.md) ja annavad Organic Mapsile rakendustepoodides 5 tärni. Üheskoos saame luua parima kaardirakenduse!

Armastusega,
Organic Maps meeskond

{{ references() }}
