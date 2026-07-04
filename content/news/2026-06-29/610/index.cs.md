---
title: "Satelitní snímky, trasy veřejnou dopravou, alternativní trasy, nové rozhraní vyhledávání a plánování tras pro Android, podpora velkých písem pro zpřístupnění v iOS a další novinky v červnové aktualizaci 2026"
date: 2026-06-29
slug: satelitni-snimky-trasy-verejnou-dopravou-alternativni-trasy-nove-rozhrani-vyhledavani-planovani-tras-android-velka-pisma
taxonomies:
  news: ["releases"]
---

V červnové aktualizaci Organic Maps je k vyzkoušení spousta zajímavých nových funkcí a oprav chyb, včetně:
- Satelitní snímky
- Trasy veřejnou dopravou
- Alternativní trasy
- Nové rozhraní vyhledávání a plánování tras pro Android
- Podpora velkých písem pro zpřístupnění v iOS

Získej ji na adrese <https://get.omaps.org> nebo v obchodech [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] a [F-Droid][fdroid] a dej nám vědět, co si myslíš!

## Podrobný seznam změn

- NOVÉ! Plánování tras veřejnou dopravou metrem, městskou rychlodráhou, autobusem a tramvají _(Viktor Govako)_
- NOVÉ! Alternativní trasy: kromě nejrychlejší trasy aplikace nyní zobrazuje i nejkratší trasu _(Viktor Govako)_
- NOVÉ! Upozornění na schody, brány a závory na pěších a cyklistických trasách _(Viktor Govako)_
- NOVÉ! Pro záložky lze vybrat libovolnou barvu _(Alexander Borsuk, Mikhail Listratsenka)_
- NOVÉ! Podpora souřadnicových systémů British National Grid (OS Grid), Irish Grid a Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTÁLNÍ: Satelitní snímky zapneš v nastavení Organic Maps zadáním vlastní adresy URL serveru rastrových dlaždic. Na vlastním serveru stále pracujeme, proto prosím najdi veřejně dostupný server, jehož URL obsahuje zástupné symboly `{x}`, `{y}`, `{z}` _(Viktor Govako, renderexpert)_
- Data OpenStreetMap aktualizována k 24. červnu _(Viktor Govako)_
- Data Wikipedie aktualizována k 20. červnu, včetně článků v italštině _(Alexander Borsuk)_
- Zadáním `?map-download-server:https://your-server.com/` do vyhledávacího okna přepíšeš servery Organic Maps pro stahování map. Zadáním `?no-map-download-server` toto přepsání odebereš _(Alexander Borsuk)_

#### Vykreslování mapy a styly

- Hezčí vzory pro pláže, písek, suť, holou skálu, sady a vinice, a také šrafování chráněných území a mokřadů _(Alexander Borsuk)_
- Plynulejší zakřivené textové popisky silnic a řek _(Viktor Govako)_
- Řeky, potoky a mokřady mají v tmavém režimu vyšší kontrast a jsou viditelnější _(Alexander Borsuk)_
- Nové a vylepšené ikony pro vyhledávání kategorií a výsledky vyhledávání na mapě _(Anton Makouski)_
- Vylepšené tvarování a vykreslování vícejazyčného textu _(Alexander Borsuk)_
- Různé opravy chyb a vylepšení výkonu _(Viktor Govako)_

#### Záznamy tras, záložky a plánované trasy

- Záznamy tras ve formátu GeoJSON nyní při importu a exportu zachovávají nadmořskou výšku a časové značky _(Alexander Borsuk)_
- Opraven pád po přesunutí záznamu trasy do jiného seznamu _(Viktor Govako)_
- U památek se nyní zobrazují webové stránky _(Viktor Govako)_
- U nepojmenovaných výsledků vyhledávání se nyní zobrazují názvy provozovatelů. Například nepojmenovaný bankomat nyní zobrazí svou banku _(Anton Makouski)_
- Editor: opraven text popisu pro úpravy/sady změn bytových domů v OpenStreetMap _(titanniya542-spec)_
- Vylepšená detekce HTML v popisech záložek a záznamů tras _(Alexander Borsuk)_

### iOS

- NOVÉ! Podpora zpřístupnění pro Dynamic Type a velká písma _(Kiryl Kaveryn)_
- NOVÉ! Klepnutím lze vybírat mezi překrývajícími se záznamy tras a plánovanými trasami _(Kiryl Kaveryn)_
- Vylepšené vykreslování HTML v popisech záložek a záznamů tras _(Kiryl Kaveryn)_
- Čistší stylování tabulek v uživatelském rozhraní _(Kiryl Kaveryn)_

### Android

- NOVÉ! Rozhraní vyhledávání _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NOVÉ! Rozhraní plánování tras _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Vylepšené vykreslování HTML v popisech záložek a záznamů tras _(Mikhail Listratsenka)_
- Zmenšena velikost APK _(Alexander Borsuk)_
- Ikona hlasu se zobrazuje jako neaktivní, když není k dispozici žádný modul převodu textu na řeč _(Mikhail Listratsenka)_
- U dlouhých popisů záložek a záznamů tras se nyní zobrazuje tlačítko „…více“ _(Mikhail Listratsenka)_
- Různé opravy uživatelského rozhraní a oprava API pro vracená ID bodů _(Mikhail Listratsenka)_

### Desktop

- Podpora přepínání zobrazovaného souřadnicového systému _(Alexander Borsuk)_
- Informace o vybraném místě se nyní zobrazují vlevo _(Viktor Govako)_
- Opravena poloha kontextové nabídky _(Osyotr)_
- Opraveno zasekávání přihlášení do OpenStreetMap a úprav ve verzích Qt 6.4 a starších _(Alexander Borsuk)_
- Opraveno neočekávané přepínání stylu mapy během navigace na macOS _(Alexander Borsuk)_
- Opraven pád při zavírání aplikace pro macOS po exportu souboru KMZ _(Alexander Borsuk)_

### Překlady

- Hlasová navigace krok za krokem v kantonštině _(Alexander Borsuk)_
- Aktualizované německé a francouzské překlady _(Wuzzy, Alexander Borsuk)_
- Opraveny nesprávné překlady hlasového pokynu „na ulici“ pro čínštinu, srbštinu a katalánštinu _(Alexander Borsuk)_

## Zapoj se do beta testování, vyzkoušej si nové funkce v předstihu a nahlas problémy:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Děkujeme všem našim uživatelům a přispěvatelům, i těm, kteří [darují](@/donate/index.cs.md) a udělují Organic Maps 5 hvězdiček v obchodech s aplikacemi. Společně můžeme vytvořit nejlepší mapovou aplikaci!

S láskou,
Tým Organic Maps

{{ references() }}
