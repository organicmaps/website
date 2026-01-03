---
title: Jak mohu provádět pokročilejší úpravy map?
slug: jak-mohu-provádět-pokročilejší-úpravy-map
description: Výukový program pro úpravu OpenStreetMap pomocí pokročilejších nástrojů,
  jako je ID, Go Map a Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
aliases:
  - /cs/faq/editing/advanced-map-editing/
---

Organické mapy obsahují jednoduchý a snadno použitelný editor, který můžete použít k úpravě mapy. Editor je však omezený a umožňuje přidávat pouze jednoduché bodové prvky, to znamená žádné obrysy budov, silnice, jezera, města atd. Pokud chcete změnit něco, co nelze upravit pomocí zabudovaného editoru, toto je ta správná stránka s často kladenými dotazy.

Protože všechna mapová data použitá v Organic Maps pocházejí z [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), můžete zde mapu přímo aktualizovat. Vaše úpravy pak budou zahrnuty do organických map s příští aktualizací map.

## Editory OpenStreetMap

Pro úpravy OSM existuje několik možností. Pokud máte po ruce notebook nebo stolní počítač, je lepší použít [ID Editor](https://www.openstreetmap.org/edit), který běží ve vašem prohlížeči. Editor ID je snadný pro začátečníky a větší obrazovka, myš a klávesnice usnadňují úpravy map.

Pro pokročilé úpravy map z mobilního zařízení použijte [Go Map](https://apps.apple.com/us/app/go-map/id592990211) pro iOS nebo [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) pro Android. Go Map je snadné pro začátečníky, zatímco Vespucci cílí na pokročilejší uživatele. LearnOSM poskytuje výukové programy pro [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) a [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Pro jednodušší úpravy a více zábavy můžete také vyzkoušet [aplikaci Every Door](https://every-door.app/) pro iOS a Android a [aplikaci StreetComplete](https://streetcomplete.app/) pro Android.

#### Editor ID

Chcete-li upravit OpenStreetMap s ID, postupujte takto:

1. Vytvořte si nový účet nebo se přihlaste na [OpenStreetMap.org](https://www.openstreetmap.org)
2. Přejděte do umístění, které chcete upravit, na OpenStreetMap.org a klikněte na *Upravit* nahoře
3. *Spusťte průvodce* a postupujte podle krátkého návodu, který vysvětluje editor ID
4. Upravte mapu
5. Nahrajte změny

To je vše, nyní jste součástí komunity OSM.

## Co se stane s mými úpravami?

Jakmile stisknete tlačítko *Nahrát*, vaše změny se okamžitě přidají do veřejné databáze OSM. Buďte tedy při úpravách ohleduplní. V organických mapách budou vaše změny viditelné po příští měsíční aktualizaci map.

Váš e-mail není zveřejněn, ale ostatní lidé uvidí vaše uživatelské jméno OSM. Protože OSM nabízí možnost diskutovat o změnách, můžete dostávat otázky týkající se vašich úprav od ostatních přispěvatelů OSM. Budete o tom informováni prostřednictvím e-mailové adresy, kterou jste použili pro registraci svého účtu OSM. Protože OSM je komunitní projekt, který staví na spolupráci, měli byste na takové otázky vždy odpovídat.

## Komunita a Wiki

OpenStreetMap je komunita. Pokud potřebujete pomoc nebo máte nějaké dotazy, můžete se zeptat na [OSM fóru](https://community.openstreetmap.org/c/help-and-support) nebo se podívat na dokumentaci [OSM Wiki](https://wiki.openstreetmap.org/).

## Tagy – Jak funguje datový model OSM

Databáze OpenStreetMap obsahuje objekty jako Nodes, Ways, Areas a Relations, které abstrahují od funkcí reálného světa. Tyto objekty mají atributy, takzvané značky, které je dále popisují. Značka je kombinace klíče a hodnoty.

Protože to zní složitější, než to je, uvedeme příklad:
Restaurace je např. mapováno jako poznámka nebo oblast se značkou ``` amenity=restaurant```. Další značky jako ```cousine=*``` nebo ```opening_hours=*``` pak lze použít pro další podrobnosti.

> Všimněte si, že editor ID skryje před uživateli vnitřní datovou strukturu, aby byl pro začátečníky přívětivější. Ale pro čtení dokumentace Wiki je užitečný stručný přehled datové struktury.
V Editoru ID můžete zobrazit značky, které před vámi ID skrývá, rozbalením sekce *Tagy* na bočním panelu *Funkce úprav*.

## Poznámky OSM {#osm-note}

Pokud nemáte čas nebo je problém příliš komplikovaný na to, abyste si data OSM upravovali sami, OSM poznámky ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) jsou správnou cestou. Takovou poznámku můžete umístit do místa chyby mapy a podrobně popsat problém. Ostatní dobrovolníci OSM pak mohou pomoci a problém vyřešit. Budete dostávat e-mailová upozornění prostřednictvím vašeho účtu OSM v případě, že budou mít další otázky nebo bude vyřešena poznámka OSM.

1. Vytvořte si nový účet nebo se přihlaste na [OpenStreetMap.org](https://www.openstreetmap.org)
   > Můžete také otevřít anonymní poznámky, ale to se nedoporučuje, protože nebudete informováni, když je problém vyřešen nebo existují další otázky.
2. Přibližte umístění mapy na [OpenStreetMap.org] (https://www.openstreetmap.org) a stiskněte *Přidat poznámku do mapy* (druhá ikona zespodu v pravé nabídce). Poté přetáhněte modrou značku na mapě na přesné místo.
   > Snažte se být co nejpřesnější.
3. Uveďte podrobný popis problému s mapou a stiskněte *Přidat poznámku*
   > Pro obchody např. uveďte název a uveďte, co se tam prodává nebo jaké služby jsou nabízeny.
