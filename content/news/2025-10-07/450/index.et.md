---
title: "7. oktoobri väljalase: Android Auto kiirusepiirangud, GeoJSON-i import, raja salvestamise statistika, OSM-i kirjeldussildi kuvamine, järjehoidja salvestamine valitud rajale iOS-is ja palju muud"
date: 2025-10-07T10:00:00+00:00
taxonomies:
  news: ["releases"]
---

See 7. oktoobri Organic Mapsi uuendus lisab kiirusepiirangu kuvamise Android Autos, GeoJSON-i impordi ja raja salvestamise statistika, näitab OSM-i kirjeldussilte (nende nägemiseks kirjuta otsingukasti `?description`) ning salvestab iOS-is järjehoidja rajale. Samuti on palju täiendusi kasutajaliideses ja OpenStreetMapi redigeerimises ning mitmesuguseid veaparandusi kõigil platvormidel, sealhulgas mõnes Android-seadmes käivitamisel tekkinud krahhi parandus.

Organic Maps on võimalik tänu ❤️ meie panustajatele, [sinu annetustele](@/donate/index.et.md) ja [sinu toetusele](@/contribute/index.et.md).

### Üksikasjalikud väljalaskemärkused (koos eelmise väikese uuenduse muudatustega)

- UUS! GeoJSON-i import (Sergiy Kozyr)
- OpenStreetMapi andmed seisuga 4. oktoober
- Wikipedia andmed seisuga 1. oktoober
- Seattle'i kiirtrammi tugi ühistranspordis (tjasz)
- Kaardivalikut ei tühistata enam redigeeritud OSM-i koha salvestamisel (Kiryl Kaveryn)
- Uuendatud tõlked (Weblate'i panustajad)

#### Kaardistiilid

- Jalgrattarendipoodide kuvamine, mis on sildistatud amenity=bicycle + rental=shop (David Martinez)
- Ajalooliste arheoloogiapaikade kuvamine alates suumist 12 ja muude ajalooliste paikade kuvamine alates suumist 15 Outdoor-stiilis (Viktor Govako)
- Uued ikoonid mastidele ning side- ja elektritornidele Outdoors-stiilis (David Martinez)
- Tipu ikooni suuruse suurendamine Outdoors-stiilis (David Martinez)
- Puuduvate POI-ikoonide variantide lisamine (David Martinez)
- Lisatud rohkem tõkketüüpe (Viktor Govako)

#### iOS

- UUS: järjehoidja salvestamine valitud rajapunktile (Kiryl Kaveryn)
- UUS: salvestatava raja kustutamine ilma seda enne salvestamata (Kiryl Kaveryn)
- Mitmerealiste järjehoidjaloendi pealkirjade kuvamine kohalehel (David Martinez)
- OSM-i sisselogimisnuppude stiili uuendamine (Kiryl Kaveryn)
- Navigeerimisteabe uuendamise vea parandus (Kiryl Kaveryn)
- Uue marsruudi planeerimise vigade parandus (Kiryl Kaveryn)
- OSM-i koha lisamise ja muutmise nähtavuse parandus üle 3 kuu vanuste kaartide puhul (Kiryl Kaveryn)
- Transpordivalikute segmentjuhtelemendi paigutuse parandus iOS 26 jaoks (Kiryl Kaveryn)
- Järjehoidjate valiku animatsioonide lihtsustamine (Kiryl Kaveryn)
- Otsingutulemuse valimise vea parandus (Kiryl Kaveryn)
- Koha teabe lehe stiili, pühkimise ja animatsioonide parandus (Kiryl Kaveryn)

#### Android Auto (ainult Google Play)

- UUS: kiirusepiirangu kuvamine Android Autos (Andrei Shkrob)
- Ekraanivahetuse parandus Android Auto navigeerimisrežiimis (Andrei Shkrob)
- Marsruudinoole nihke parandus Android Autos (Andrei Shkrob)
- Parandatud tõrge seadme autoga ühendamisel või lahtiühendamisel (Andrei Shkrob)
- Lisatud Android Auto asukohateenus (Andrei Shkrob)
- Android Auto marsruudisimulaatori täiustamine (Viktor Govako)

#### Android

- UUS: raja salvestamise statistika vaatamine reaalajas (Kavi Khalique)
- UUS: OSM-i `description` sildi sisu kuvamine (Alexander Borsuk)
- Teemavahetuse käsitlemise parandus (Andrei Shkrob)
- Parandatud mitu krahhi, sealhulgas käivitamisel tekkinud krahh (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Vaiksed allalaadimise edenemise teated (Viktor Govako)
- Pliiatsi ikooni polsterduse vähendamine (Alexander Borsuk)

#### Töölaud

- Linuxis hangunud curli parandus (Alexander Borsuk)
- macOS-is OSM-i sisselogimisel tekkinud hangumise parandus (Alexander Borsuk)
- Objekti valimise käsk kontekstimenüüs (Viktor Govako)
- Allalaadimise tühistamise võimalus (Viktor Govako)
- Geomeetria tüübi kuvamine kontekstimenüüs (Viktor Govako)

### Hiljuti ilmunud funktsioonid, mida võisid märkamata jätta

- Ühistranspordi liininumbrid bussipeatuse valimisel
- Matka- ja rattamarsruudid (lülita need sisse vasakus ülanurgas Kihid nupuga)
- Näe järjehoidjate nimesid kaardil, lülitades selle sisse rakenduse Sätetes
- ✎ pliiatsi ikoon võimaldab järjehoidjaid kiiresti muuta

### Paigalda Organic Maps

Hangi uusim Organic Mapsi versioon: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ja [F-Droid][fdroid].

Liitu beetatestimisega, et saada uusi funktsioone varem: [iOS][testflight] / [Android][firebase].

{{ references() }}
