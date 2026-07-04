---
title: "Műholdképek, tömegközlekedési útvonalak, alternatív útvonalak, új keresési és útvonaltervezési felület Androidon, nagy akadálymentesítési betűméretek támogatása iOS-en és további újdonságok a 2026. júniusi frissítésben"
date: 2026-06-29
slug: "muholdkepek-tomegkozlekedesi-utvonalak-alternativ-utvonalak-uj-kereses-utvonaltervezes-android-nagy-betumeretek-ios-2026-junius"
taxonomies:
  news: ["releases"]
---

Az Organic Maps júniusi frissítésében sok izgalmas új funkció és hibajavítás vár kipróbálásra, többek között:
- Műholdképek
- Tömegközlekedési útvonalak
- Alternatív útvonalak
- Új keresési és útvonaltervezési felület Androidon
- Nagy akadálymentesítési betűméretek támogatása iOS-en

Szerezd be a <https://get.omaps.org> címen vagy az [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] és [F-Droid][fdroid] áruházakból, és mondd el, mit gondolsz róla!

## Részletes változásnapló

- ÚJ! Tömegközlekedési útvonaltervezés metróval, könnyűvasúttal, busszal és villamossal _(Viktor Govako)_
- ÚJ! Alternatív útvonalak: a leggyorsabb útvonal mellett az alkalmazás most a legrövidebb útvonalat is megmutatja _(Viktor Govako)_
- ÚJ! Figyelmeztetések gyalogos és kerékpáros útvonalakon lépcsőkről, kapukról és sorompókról az út mentén _(Viktor Govako)_
- ÚJ! Bármilyen színt választhatsz a könyvjelzőkhöz _(Alexander Borsuk, Mikhail Listratsenka)_
- ÚJ! British National Grid (OS Grid), Irish Grid és Irish Transverse Mercator (ITM) koordináták támogatása _(Alexander Borsuk)_
- KÍSÉRLETI: engedélyezd a műholdképeket az Organic Maps beállításaiban egy egyéni raszteres csempeszerver URL-jével. Még dolgozunk a saját szerverünkön, ezért egyelőre keress nyilvánosan elérhető szervert, amelynek URL-jében szerepelnek a `{x}`, `{y}`, `{z}` helyőrzők _(Viktor Govako, renderexpert)_
- OpenStreetMap-adatok frissítve június 24-i állapot szerint _(Viktor Govako)_
- Wikipedia-adatok frissítve június 20-i állapot szerint, olasz nyelvű cikkekkel együtt _(Alexander Borsuk)_
- Írd be a keresőablakba: `?map-download-server:https://your-server.com/`, hogy felülírd az Organic Maps térképletöltő szervereit. A felülírás eltávolításához írd be: `?no-map-download-server` _(Alexander Borsuk)_

#### Térképmegjelenítés és stílusok

- Szebb minták strandokhoz, homokhoz, kőtörmelékhez, csupasz sziklához, gyümölcsösökhöz és szőlőkhöz, valamint sraffozás védett területekhez és vizes élőhelyekhez _(Alexander Borsuk)_
- Simább ívelt szövegcímkék utakhoz és folyókhoz _(Viktor Govako)_
- A folyók, patakok és vizes élőhelyek nagyobb kontrasztot kaptak, és jobban láthatók sötét módban _(Alexander Borsuk)_
- Új és továbbfejlesztett ikonok kategóriakereséshez és térképen megjelenő keresési találatokhoz _(Anton Makouski)_
- Javított többnyelvű szövegformálás és megjelenítés _(Alexander Borsuk)_
- Különféle hibajavítások és teljesítményjavítások _(Viktor Govako)_

#### Nyomvonalak, könyvjelzők és útvonalak

- A GeoJSON-nyomvonalak importáláskor és exportáláskor mostantól megőrzik a magasságot és az időbélyegeket _(Alexander Borsuk)_
- Javítva egy összeomlás, amely egy nyomvonal másik listába mozgatása után történt _(Viktor Govako)_
- Az örökségi helyszínekhez mostantól webhelyek is megjelennek _(Viktor Govako)_
- A névtelen keresési találatoknál mostantól megjelennek az üzemeltetőnevek. Például egy névtelen ATM most megmutatja a bankját _(Anton Makouski)_
- Szerkesztő: javítva a lakóházakhoz kapcsolódó OpenStreetMap-szerkesztések/changesetek leíró szövege _(titanniya542-spec)_
- Javított HTML-felismerés könyvjelzők és nyomvonalak leírásaiban _(Alexander Borsuk)_

### iOS

- ÚJ! Akadálymentesítési támogatás Dynamic Type-hoz és nagy betűméretekhez _(Kiryl Kaveryn)_
- ÚJ! Koppints az egymást fedő nyomvonalak és útvonalak közötti választáshoz _(Kiryl Kaveryn)_
- Javított HTML-megjelenítés könyvjelzők és nyomvonalak leírásaihoz _(Kiryl Kaveryn)_
- Letisztultabb táblázatstílus a felületen _(Kiryl Kaveryn)_

### Android

- ÚJ! Keresési felület _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- ÚJ! Útvonaltervezési felület _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Javított HTML-megjelenítés könyvjelzők és nyomvonalak leírásaihoz _(Mikhail Listratsenka)_
- Csökkentett APK-méret _(Alexander Borsuk)_
- A hangikon letiltottként jelenik meg, ha nincs elérhető szövegfelolvasó motor _(Mikhail Listratsenka)_
- A hosszú könyvjelző- és nyomvonalleírások mostantól „…tovább” gombot mutatnak _(Mikhail Listratsenka)_
- Különféle UI-javítások és API-javítás a visszaadott pontazonosítókhoz _(Mikhail Listratsenka)_

### Desktop

- A megjelenített koordinátarendszer váltásának támogatása _(Alexander Borsuk)_
- A kiválasztott hely adatai mostantól bal oldalon jelennek meg _(Viktor Govako)_
- Javítva a helyi menü pozíciója _(Osyotr)_
- Javítva az OpenStreetMap-bejelentkezés és -szerkesztés lefagyása Qt 6.4 és korábbi verziókon _(Alexander Borsuk)_
- Javítva a váratlan térképstílus-váltás útvonaltervezés közben macOS-en _(Alexander Borsuk)_
- Javítva egy összeomlás a macOS-alkalmazás bezárásakor KMZ-fájl exportálása után _(Alexander Borsuk)_

### Fordítások

- Kantoni lépésről lépésre hangnavigáció _(Alexander Borsuk)_
- Frissített német és francia fordítások _(Wuzzy, Alexander Borsuk)_
- Javítva az „onto street” hangutasítás hibás fordítása kínai, szerb és katalán nyelven _(Alexander Borsuk)_

## Csatlakozz a bétateszteléshez, próbáld ki korán az új funkciókat, és jelentsd a hibákat:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Hálásak vagyunk minden felhasználónknak és közreműködőnknek, azoknak, akik [adományoznak](@/donate/index.hu.md), és 5 csillagot adnak az Organic Mapsnek az alkalmazás-áruházakban. Együtt megépíthetjük a legjobb térképes alkalmazást!

Szeretettel,
Az Organic Maps csapat

{{ references() }}
