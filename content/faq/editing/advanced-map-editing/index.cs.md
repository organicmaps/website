---
title: Jak mohu provádět pokročilejší úpravy map?
slug: jak-mohu-provádět-pokročilejší-úpravy-map
description: Výukový program pro úpravu OpenStreetMap pomocí pokročilejších nástrojů,
  jako je ID, Go Map a Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - map-editing
extra:
  order: 40
aliases:
  - /cs/faq/editing/advanced-map-editing/
---

Organic Maps obsahuje jednoduchý a snadno použitelný editor, který můžeš použít k úpravě mapy. Editor je však omezený a umožňuje přidávat pouze jednoduché bodové prvky, to znamená žádné obrysy budov, silnice, jezera, města atd. Pokud chceš změnit něco, co nelze upravit pomocí zabudovaného editoru, toto je ta správná stránka s často kladenými dotazy.

Protože všechna mapová data použitá v Organic Maps pocházejí z [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), můžeš zde mapu přímo aktualizovat. Tvoje úpravy pak budou zahrnuty do Organic Maps s příští aktualizací map.

## Editory OpenStreetMap

Pro úpravy OSM existuje několik možností. Pokud máš po ruce notebook nebo stolní počítač, je lepší použít [ID Editor](https://www.openstreetmap.org/edit), který běží ve tvém prohlížeči. ID Editor je snadný pro začátečníky a větší obrazovka, myš a klávesnice usnadňují úpravy map.

Pro pokročilé úpravy map z mobilního zařízení použij [Go Map](https://apps.apple.com/us/app/go-map/id592990211) pro iOS nebo [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) pro Android. Go Map je snadné pro začátečníky, zatímco Vespucci cílí na pokročilejší uživatele. LearnOSM poskytuje výukové programy pro [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) a [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Pro jednodušší úpravy a více zábavy můžeš také vyzkoušet [aplikaci Every Door](https://every-door.app/) pro iOS a Android a [aplikaci StreetComplete](https://streetcomplete.app/) pro Android.

#### ID Editor

Chceš-li upravit OpenStreetMap s ID, postupuj takto:

1. Vytvoř si nový účet nebo se přihlas na [OpenStreetMap.org](https://www.openstreetmap.org)
2. Přejdi do umístění, které chceš upravit, na OpenStreetMap.org a klikni na *Upravit* nahoře
3. *Spusť průvodce* a postupuj podle krátkého návodu, který vysvětluje ID Editor
4. Uprav mapu
5. Nahraj změny

To je vše, nyní jsi součástí komunity OSM.

## Co se stane s mými úpravami?

Jakmile stiskneš tlačítko *Nahrát*, tvoje změny se okamžitě přidají do veřejné databáze OSM. Buď tedy při úpravách ohleduplný. V Organic Maps budou tvoje změny viditelné po příští měsíční aktualizaci map.

Tvůj e-mail není zveřejněn, ale ostatní lidé uvidí tvoje uživatelské jméno OSM. Protože OSM nabízí možnost diskutovat o změnách, můžeš dostávat otázky týkající se tvých úprav od ostatních přispěvatelů OSM. Budeš o tom informován prostřednictvím e-mailové adresy, kterou jsi použil pro registraci svého účtu OSM. Protože OSM je komunitní projekt, který staví na spolupráci, měl bys na takové otázky vždy odpovídat.

## Komunita a Wiki

OpenStreetMap je komunita. Pokud potřebuješ pomoc nebo máš nějaké dotazy, můžeš se zeptat na [OSM fóru](https://community.openstreetmap.org/c/help-and-support) nebo se podívat na dokumentaci [OSM Wiki](https://wiki.openstreetmap.org/).

## Tagy – Jak funguje datový model OSM

Databáze OpenStreetMap obsahuje objekty jako Nodes, Ways, Areas a Relations, které abstrahují od funkcí reálného světa. Tyto objekty mají atributy, takzvané značky, které je dále popisují. Značka je kombinace klíče a hodnoty.

Protože to zní složitější, než to je, uvedeme příklad:
Restaurace je např. mapováno jako poznámka nebo oblast se značkou `amenity=restaurant`. Další značky jako `cuisine=*` nebo `opening_hours=*` pak lze použít pro další podrobnosti.

> Všimni si, že editor ID skryje před uživateli vnitřní datovou strukturu, aby byl pro začátečníky přívětivější. Ale pro čtení dokumentace Wiki je užitečný stručný přehled datové struktury.
V ID Editoru můžeš zobrazit značky, které před tebou ID skrývá, rozbalením sekce *Tagy* na bočním panelu *Funkce úprav*.

## Poznámky OSM {#osm-note}

Pokud nemáš čas nebo je problém příliš komplikovaný na to, abys si data OSM upravoval sám, OSM poznámky ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) jsou správnou cestou. Takovou poznámku můžeš umístit do místa chyby mapy a podrobně popsat problém. Ostatní dobrovolníci OSM pak mohou pomoci a problém vyřešit. Budeš dostávat e-mailová upozornění prostřednictvím tvého účtu OSM v případě, že budou mít další otázky nebo bude vyřešena poznámka OSM.

1. Vytvoř si nový účet nebo se přihlas na [OpenStreetMap.org](https://www.openstreetmap.org)
   > Můžeš také otevřít anonymní poznámky, ale to se nedoporučuje, protože nebudeš informován, když je problém vyřešen nebo existují další otázky.
2. Přibliž umístění mapy na [OpenStreetMap.org](https://www.openstreetmap.org) a stiskni *Přidat poznámku do mapy* (druhá ikona zespodu v pravé nabídce). Poté přetáhni modrou značku na mapě na přesné místo.
   > Snaž se být co nejpřesnější.
3. Uveď podrobný popis problému s mapou a stiskni *Přidat poznámku*
   > Pro obchody např. uveď název a uveď, co se tam prodává nebo jaké služby jsou nabízeny.
