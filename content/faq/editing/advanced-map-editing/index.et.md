---
title: Kuidas teha täpsemat kaarditöötlust?
slug: kuidas-teha-täpsemat-kaarditöötlust
description: Õpetus OpenStreetMapi redigeerimiseks keerukamate tööriistadega, nagu
  ID, Go Map ja Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
aliases:
  - /et/faq/editing/advanced-map-editing/
---

Organic Maps sisaldab lihtsat ja hõlpsasti kasutatavat redaktorit, mida saate kasutada kaardi muutmiseks. Redaktor on aga piiratud ja võimaldab lisada ainult lihtsaid punktifunktsioone, mis tähendab, et puuduvad hoonekontuurid, teed, järved, linnad jne. Kui soovite muuta midagi, mida sisseehitatud redaktoriga muuta ei saa, on see lugemiseks õige KKK leht.

Kuna kõik orgaanilistes kaartides kasutatavad kaardiandmed pärinevad saidilt [OpenStreetMap.org (OSM)] (https://www.openstreetmap.org), saate seal kaarti otse värskendada. Seejärel kaasatakse teie muudatused järgmise kaardivärskendusega orgaanilistesse kaartidesse.

## OpenStreetMapi redaktorid

OSM-i redigeerimiseks on mitu võimalust. Kui teil on käepärast sülearvuti või lauaarvuti, on parem kasutada brauseris töötavat [ID-redaktorit](https://www.openstreetmap.org/edit). ID-redaktor on algajatele lihtne ning suurem ekraan, hiir ja klaviatuur muudavad kaardi redigeerimise lihtsamaks.

Mobiilseadmest kaardi täpsemaks muutmiseks kasutage iOS-i jaoks rakendust [Go Map](https://apps.apple.com/us/app/go-map/id592990211) või Androidi jaoks [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android). Go Map on algajatele lihtne, samas kui Vespucci on suunatud kogenumatele kasutajatele. LearnOSM pakub õpetusi [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) ja [Vespucci] (https://learnosm.org/en/mobile-mapping/vespucci/) jaoks.

Lihtsamaks ja lõbusamaks muutmiseks võite proovida ka rakendust [Every Door](https://every-door.app/) iOS-i ja Androidi jaoks ning rakendust [StreetComplete](https://streetcomplete.app/) Androidi jaoks.

#### ID-redaktor

ID-ga OpenStreetMapi redigeerimiseks toimige järgmiselt.

1. Looge uus konto või logige sisse saidil [OpenStreetMap.org](https://www.openstreetmap.org)
2. Sirvige saidil OpenStreetMap.org asukohta, mida soovite muuta, ja klõpsake ülaosas nuppu *Muuda*
3. *Alustage läbivaatust* ja järgige ID-redaktorit selgitavat lühikest õpetust
4. Redigeerige kaarti
5. Laadige oma muudatused üles

See on kõik, olete nüüd osa OSM-i kogukonnast.

## Mis juhtub minu muudatustega?

Kui vajutate nuppu *Laadi üles*, lisatakse teie muudatused koheselt avalikku OSM-i andmebaasi. Seega olge toimetamisel tähelepanelik. Orgaanilistes kaartides on teie muudatused nähtavad pärast järgmist igakuist kaardivärskendust.

Teie e-posti ei avaldata, kuid teised inimesed näevad teie OSM-i kasutajanime. Kuna OSM pakub võimalust arutada muudatusi, võite saada oma muudatuste kohta küsimusi teistelt OSM-i kaasautoritelt. Teid teavitatakse sellest e-posti aadressi kaudu, mida kasutasite oma OSM-i konto registreerimisel. Kuna OSM on kogukonnaprojekt, mis põhineb koostööl, peaksite sellistele küsimustele alati vastama.

## Kogukond ja Wiki

OpenStreetMap on kogukond. Kui vajate abi või teil on küsimusi, võite küsida [OSM-i foorumis](https://community.openstreetmap.org/c/help-and-support) või heita pilk [OSM Wiki](https://wiki.openstreetmap.org/) dokumentatsioonile.

## Sildid – kuidas OSM-i andmemudel töötab

OpenStreetMapi andmebaas sisaldab selliseid objekte nagu sõlmed, viisid, alad ja seosed, mis eralduvad reaalsetest funktsioonidest. Nendel objektidel on nende edasiseks kirjeldamiseks atribuudid, nn sildid. Silt on võtme-väärtuse kombinatsioon.

Kuna see kõlab keerulisemalt kui see on, toome näite:
Restoran on nt. kaardistatud märkme või piirkonnana sildiga `amenity=restaurant`. Seejärel saab lisateabe saamiseks kasutada täiendavaid silte, nagu `cuisine=*` või `avamistunnid=*`.

> Pange tähele, et ID-redaktor peidab sisemise andmestruktuuri kasutajate eest, et see oleks algajasõbralikum. Kuid Wiki dokumentatsiooni lugemisel on abi andmestruktuuri lühiülevaatest.
ID-redaktoris näete silte, mida ID teie eest varjab, kui laiendate külgpaneelil *Märgendid* jaotist *Märgendid*.

## OSM-i märkmed {#osm-note}

Kui teil pole aega või probleem on liiga keeruline, et ise OSM-i andmeid redigeerida, on õige tee OSM-i märkmed ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)). Sellise märkuse saate panna kaardivea asukohta ja kirjeldada probleemi üksikasjalikult. Teised OSM-i vabatahtlikud saavad seejärel aidata ja probleemi lahendada. Saate oma OSM-i konto kaudu meiliteateid, kui neil on lisaküsimusi või kui OSM-i märkus on lahendatud.

1. Looge uus konto või logige sisse saidil [OpenStreetMap.org](https://www.openstreetmap.org)
   > Saate avada ka anonüümseid märkmeid, kuid see pole soovitatav, kuna te ei saa probleemi lahendamisest või lisaküsimuste tekkimisest teavitust.
2. Suumige kaardil olevale asukohale saidil [OpenStreetMap.org] (https://www.openstreetmap.org) ja vajutage nuppu *Lisa kaardile märge* (parempoolses menüüs allservas teine ​​ikoon). Seejärel lohistage sinine kaardimarker täpsesse asukohta.
   > Proovige olla nii täpne kui võimalik.
3. Esitage kaardiprobleemi üksikasjalik kirjeldus ja vajutage *Lisa märkus*
   > Kauplustele nt. nimetage nimi ja mainige, mida seal müüakse või milliseid teenuseid pakutakse.
