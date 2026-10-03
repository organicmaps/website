---
title: "Optimalizace tras, vylepšené alternativní trasy, skrývání jednotlivých stop a nestálé vodní plochy v aktualizaci ze září 2026"
date: 2026-09-29
slug: "vicenasobny-vyber-zalozek-stop-panel-carplay-skryvani-stop-odkazy-srpen-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Jste připraveni vyrazit? Zářijová aktualizace přináší vylepšené alternativní trasy, nastavení pro optimalizaci pořadí zastávek na trase, přehlednější značení nestálých vodních ploch a ikonu oka pro skrytí jednotlivých stop spolu s mnoha dalšími opravami a vylepšeními (viz níže).

Nainstalujte si aplikaci Organic Maps nebo ji aktualizujte prostřednictvím stránky <https://get.omaps.org>, v [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] nebo [F-Droid][fdroid].

Pokud vám unikly naše předchozí aktualizace, podívejte se na funkce, které jsme vydali v [červnu](@/news/2026-06-29/610/index.cs.md), [červenci](@/news/2026-07-23/620/index.cs.md) a [srpnu](@/news/2026-08-31/630/index.cs.md). Velký dík patří našim přispěvatelům a uživatelům, díky nimž byly tyto aktualizace možné!

## Jak podpořit Organic Maps

- [Přispějte](@/donate/index.cs.md) na podporu vývoje a pokrytí nákladů na hostování map
- [Zašlete nám svůj názor a přispějte](@/contribute/index.cs.md) k projektu
- Zapojte se do beta testování, abyste mohli nové funkce vyzkoušet jako jedni z prvních a nahlásit případné problémy na [iOS][testflight], [Androidu][firebase] a [počítačích][flathub]
- Šiřte tuto zprávu a pomozte nám vytvořit lepší alternativu k mapám velkých technologických společností!

## Poznámky k vydání

### Mapa

- Údaje z OpenStreetMap k 28. září 2026
- Údaje z Wikipedie k 21. září 2026
- Opraveno vyhledávání v případech, kdy viditelná oblast mapy překračuje poledník 180° (±180° zeměpisné délky) _(Viktor Govako)_
- Nestálé vodní plochy jsou nyní znázorněny tečkovaným vzorem, podobným tomu, který se používá pro písek _(Alexander Borsuk)_
- Vodní nádrže jsou nyní viditelné při větším oddálení _(Alexander Borsuk)_
- Vodní tunely se již na mapě nezobrazují _(Alexander Borsuk)_
- Opraveny ikony stanic a vchodů do metra v Su-čou _(Alexander Borsuk)_
- Byly opraveny ojedinělé případy, kdy se popisky na vrstvě mapy metra posunuly mimo správnou polohu _(Viktor Govako)_

### Trasování a navigace

- Vylepšené alternativní trasy a jejich odhadované časy příjezdu _(Alexander Borsuk, Viktor Govako)_
- Vybraná alternativní trasa se nyní zachová i při přepočítání trasy navigací _(Alexander Borsuk)_
- Po restartování aplikace se nyní obnovuje pořadí zastávek na trase _(Kiryl Kaveryn)_

### Další vylepšení

- V otevíracích hodinách se nyní místo 12:00 zobrazuje „Poledne“ a místo 00:00 nebo 24:00 „Půlnoc“ _(Alexander Borsuk)_
- Opraveny chyby a vylepšen záznam stop _(Alexander Borsuk)_
- Opraven import souborů KMB _(Alexander Borsuk)_
- Opravené francouzské a asturské překlady _(Alexander Borsuk)_
- Opraven překlep v angličtině _(Carl Morris)_

### iOS

- Byla přidána ikona oka pro skrytí jednotlivých stop _(Kiryl Kaveryn)_
- Byla přidána tlačítka pro přidání nebo nahrazení zastávky v naplánované trase _(Kiryl Kaveryn)_
- Bylo přidáno nastavení pro optimalizaci pořadí mezilehlých zastávek na trase _(Kiryl Kaveryn)_
- Přidány pokyny k manévrům na podporovaných průhledových displejích (HUD) v automobilech a na panelu CarPlay _(Kiryl Kaveryn)_
- Opravena tlačítka CarPlay a vyhledávání _(Alexander Borsuk)_
- Byly opraveny různé chyby a vylepšeno uživatelské rozhraní _(Kiryl Kaveryn, Alexander Borsuk)_
- Přidána podpora pro výběr nainstalovaného navigačního hlasu a poslech jeho ukázky _(Kiryl Kaveryn, Alexander Borsuk)_
- Obnoveno vyhledávání podle kategorií ve Spotlightu _(Kiryl Kaveryn)_

### Android

- Bylo přidáno nastavení pro optimalizaci pořadí mezilehlých zastávek na trase _(Mikhail Listratsenka)_
- Byla přidána tlačítka pro přidání nebo nahrazení zastávky v naplánované trase _(Mikhail Listratsenka)_
- Přidána možnost zastavit záznam stopy a uložit ji přímo z oznámení _(Alexander Borsuk)_
- Tlačítko „Přidat zastávku“ nyní přidá zastávku za stávajícími zastávkami, před cílovou zastávkou _(Mikhail Listratsenka)_
- Vylepšené nahrávání dat z editoru OpenStreetMap _(Owm)_
- Aktualizován design uživatelského rozhraní _(Mikhail Listratsenka)_
- Editor záložek a další dialogová okna nyní zůstávají otevřená i během navigace _(Mikhail Listratsenka)_
- Opraveno vykreslování grafu nadmořské výšky u stop bez výrazných výškových změn a v rozhraních s orientací zprava doleva _(Mikhail Listratsenka)_
- Opraveno ořezávání tlačítek na mapě systémovými lištami _(Mikhail Listratsenka)_
- Opraveny chyby a vylepšena podpora Android Auto _(Andrei Shkrob)_
- Byla opravena chyba způsobující pád aplikace při vykreslování mapy _(Viktor Govako)_

### Počítače

- Spustitelný soubor pro počítače a balíček aplikace pro macOS byly přejmenovány na `OrganicMaps` _(Alexander Borsuk)_
- Byly opraveny chyby v aplikaci pro Windows _(Osyotr, Alexander Borsuk)_
- Argument příkazového řádku `--lang` má nyní přednost před nastavením jazyka aplikace _(Alexander Borsuk)_

S radostí a nadšením,

Váš tým Organic Maps

{{ <references lang /> }}
