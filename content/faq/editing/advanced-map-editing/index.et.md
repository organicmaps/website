---
title: Kuidas teha täpsemat kaarditöötlust?
slug: kuidas-teha-täpsemat-kaarditöötlust
description: Õpetus OpenStreetMapi redigeerimiseks keerukamate tööriistadega, nagu
  ID, Go Map ja Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - map-editing
extra:
  order: 40
aliases:
  - /et/faq/editing/advanced-map-editing/
---

Organic Maps sisaldab lihtsat ja hõlpsasti kasutatavat redaktorit, mida saad kasutada kaardi muutmiseks. Redaktor on aga piiratud ja võimaldab lisada ainult lihtsaid punktifunktsioone, mis tähendab, et puuduvad hoonekontuurid, teed, järved, linnad jne. Kui soovid muuta midagi, mida sisseehitatud redaktoriga muuta ei saa, on see lugemiseks õige KKK leht.

Kuna kõik Organic Mapsis kasutatavad kaardiandmed pärinevad saidilt [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), saad seal kaarti otse värskendada. Seejärel kaasatakse sinu muudatused järgmise kaardivärskendusega Organic Mapsisse.

## OpenStreetMapi redaktorid

OSM-i redigeerimiseks on mitu võimalust. Kui sul on käepärast sülearvuti või lauaarvuti, on parem kasutada brauseris töötavat [ID Editorit](https://www.openstreetmap.org/edit). ID Editor on algajatele lihtne ning suurem ekraan, hiir ja klaviatuur muudavad kaardi redigeerimise lihtsamaks.

Mobiilseadmest kaardi täpsemaks muutmiseks kasuta iOS-i jaoks rakendust [Go Map](https://apps.apple.com/us/app/go-map/id592990211) või Androidi jaoks [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android). Go Map on algajatele lihtne, samas kui Vespucci on suunatud kogenumatele kasutajatele. LearnOSM pakub õpetusi [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) ja [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/) jaoks.

Lihtsamaks ja lõbusamaks muutmiseks võid proovida ka rakendust [Every Door](https://every-door.app/) iOS-i ja Androidi jaoks ning rakendust [StreetComplete](https://streetcomplete.app/) Androidi jaoks.

#### ID Editor

ID-ga OpenStreetMapi redigeerimiseks toimi järgmiselt.

1. Loo uus konto või logi sisse saidil [OpenStreetMap.org](https://www.openstreetmap.org)
2. Sirvi saidil OpenStreetMap.org asukohta, mida soovid muuta, ja klõpsa ülaosas nuppu *Muuda*
3. *Alustage läbivaatust* ja järgi ID Editorit selgitavat lühikest õpetust
4. Redigeeri kaarti
5. Laadi oma muudatused üles

See on kõik, oled nüüd osa OSM-i kogukonnast.

## Mis juhtub minu muudatustega?

Kui vajutad nuppu *Laadi üles*, lisatakse sinu muudatused koheselt avalikku OSM-i andmebaasi. Seega ole toimetamisel tähelepanelik. Organic Mapsis on sinu muudatused nähtavad pärast järgmist igakuist kaardivärskendust.

Sinu e-posti ei avaldata, kuid teised inimesed näevad sinu OSM-i kasutajanime. Kuna OSM pakub võimalust arutada muudatusi, võid saada oma muudatuste kohta küsimusi teistelt OSM-i kaasautoritelt. Sind teavitatakse sellest e-posti aadressi kaudu, mida kasutasid oma OSM-i konto registreerimisel. Kuna OSM on kogukonnaprojekt, mis põhineb koostööl, peaksid sellistele küsimustele alati vastama.

## Kogukond ja Wiki

OpenStreetMap on kogukond. Kui vajad abi või sul on küsimusi, võid küsida [OSM-i foorumis](https://community.openstreetmap.org/c/help-and-support) või heita pilk [OSM Wiki](https://wiki.openstreetmap.org/) dokumentatsioonile.

## Sildid – kuidas OSM-i andmemudel töötab

OpenStreetMapi andmebaas sisaldab selliseid objekte nagu sõlmed, viisid, alad ja seosed, mis eralduvad reaalsetest funktsioonidest. Nendel objektidel on nende edasiseks kirjeldamiseks atribuudid, nn sildid. Silt on võtme-väärtuse kombinatsioon.

Kuna see kõlab keerulisemalt kui see on, toome näite:
Restoran on nt. kaardistatud märkme või piirkonnana sildiga `amenity=restaurant`. Seejärel saab lisateabe saamiseks kasutada täiendavaid silte, nagu `cuisine=*` või `opening_hours=*`.

> Pane tähele, et ID Editor peidab sisemise andmestruktuuri kasutajate eest, et see oleks algajasõbralikum. Kuid Wiki dokumentatsiooni lugemisel on abi andmestruktuuri lühiülevaatest.
ID Editoris näed silte, mida ID sinu eest varjab, kui laiendad külgpaneelil *Märgendid* jaotist *Märgendid*.

## OSM-i märkmed {#osm-note}

Kui sul pole aega või probleem on liiga keeruline, et ise OSM-i andmeid redigeerida, on õige tee OSM-i märkmed ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)). Sellise märkuse saad panna kaardivea asukohta ja kirjeldada probleemi üksikasjalikult. Teised OSM-i vabatahtlikud saavad seejärel aidata ja probleemi lahendada. Saad oma OSM-i konto kaudu meiliteateid, kui neil on lisaküsimusi või kui OSM-i märkus on lahendatud.

1. Loo uus konto või logi sisse saidil [OpenStreetMap.org](https://www.openstreetmap.org)
   > Saad avada ka anonüümseid märkmeid, kuid see pole soovitatav, kuna sa ei saa probleemi lahendamisest või lisaküsimuste tekkimisest teavitust.
2. Suumi kaardil olevale asukohale saidil [OpenStreetMap.org](https://www.openstreetmap.org) ja vajuta nuppu *Lisa kaardile märge* (parempoolses menüüs allservas teine ​​ikoon). Seejärel lohista sinine kaardimarker täpsesse asukohta.
   > Proovi olla nii täpne kui võimalik.
3. Esita kaardiprobleemi üksikasjalik kirjeldus ja vajuta *Lisa märkus*
   > Kauplustele nt. nimeta nimi ja maini, mida seal müüakse või milliseid teenuseid pakutakse.
