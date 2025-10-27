---
title: "7. oktoobri väljalase: Android Auto kiirusepiirangud, GeoJSON import ja muud"
date: 2025-10-07T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

Android Auto kasutajad näevad nüüd kiirusepiirangu hoiatusi. Lisatud on GeoJSON failide import, mida saab markeriteks teisendada.

Mitmesugused parandused ja täiendused iOS-i, Androidi, Android Auto ja Desktopi jaoks. Detailid allpool.

Hiljutised funktsioonid, mida võisid märkamata jätta:
- Uus marsruudi planeerimise ekraan (iOS)
- OSM `description` silt iOS-is (otsi `?description`)
- Ühistranspordi liininumbrid peatusel
- Matka- ja rattarajad (lülita sisse vasakus ülanurgas Kihid nupu alt)
- Kuva markerite nimed kaardil (lülita Sätetes)
- ✎ ikoon võimaldab markereid kiiresti muuta

Organic Maps on võimalik tänu panustajatele, [sinu annetustele](@/donate/index.et.md) ja [toetusele](@/contribute/index.et.md).

### Üksikasjalikud väljalaskemärkused

- Uued OpenStreetMap andmed seisuga 5. oktoober
- Uuendatud tõlked (Weblate'i panustajad)
- Asukohanool ilma GNSS signaalita parandatud (Viktor Govako)

#### Kaardistiilid (Viktor Govako)

- Outdoor-stiili ikoonid ümberkujundatud
- Vee siltide värv parandatud
- Hoonete kuvamine suumil 16
- Vaateplatvormide ja -punktide kuvamine alates suumist 14
- Üldised kaardiparandused ja täiendused

#### iOS

- Marsruudi punktide värvid parandatud (Alexander Borsuk)
- Pika vajutuse menüü täiendused (Alexander Borsuk)
- Saabumisaeg ühiku tüübi muutmisel parandatud (Viktor Govako)
- Kustutatud objektide redigeerimise blokeerimine (Kiryl Kaveryn)

#### Android

- UUS: GeoJSON failide importimine ja markeriteks teisendamine (Andrei Shkrob, Alexander Borsuk)
- Lähedaste WiFi ja mobiilsidevõrkude loend "Minu asukoha" all (ainult debug build) (Kiryl Kaveryn)
- OSM sisselogimine uuendatud (Viktor Govako)
- Kaardi allalaadimise veateate parandus (Viktor Govako)
- Usaldusväärsem GeoIntenti käsitlemine (Alexander Borsuk)
- Andmete migratsiooni UI täiendused (Alexander Borsuk)
- Kategooriate UI täiendused (Alexander Borsuk)
- Google'i asukohateenused eemaldatud (Alexander Borsuk)
- "Linna aadress" otsingukateg ria nüüd "Aadress" (Alexander Borsuk)
- Võimalik must ekraan otsingutulemusele klõpsamisel parandatud (Viktor Govako)
- UI kohandused "Mis on lähedal" otsingus (Viktor Govako)
- Hüpikdialoogi parandus, mis ei austa tumedat teemat (Andrei Shkrob)

#### Android Auto

- UUS: Kiirusepiirangu ja kiiruskaamerate hoiatused (Denis Koronchik)
- Marsruudi eelvaade parandatud (Andrei Shkrob)
- Otsingu UI täiendused (Andrei Shkrob)

#### Desktop

- Kaardi kohandamise täiendused (Andrew Shkrob)
- Hiire kursori kontrast tumedas teemas parandatud (Andrew Shkrob)

Laadi alla uusim versioon: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Liitu beetaga: [iOS][testflight] / [Android][firebase].

{{ references() }}
