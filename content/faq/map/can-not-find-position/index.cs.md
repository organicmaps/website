---
title: "Aplikace nemůže najít mou polohu na mapě nebo ukazuje nesprávnou polohu"
slug: aplikace-nemůže-najít-moji-polohu-na-mapě
description: "Průvodce řešením problémů s polohou a aktuální GPS pozicí na mapě pro zařízení iOS a Android"
updated: "2026-01-04"
taxonomies:
  faq:
  - Map
extra:
  order: 10
aliases:
  - /cs/faq/map/can-not-find-position/
---

Ujistěte se prosím, že vaše zařízení má GPS, že jsou povoleny služby určování polohy a že organickým mapám jsou udělena oprávnění k poloze.

**Android**

Na svém zařízení otevřete Nastavení → Umístění. Je lepší zapnout režim vysoké přesnosti, protože umožňuje přesnou polohu GPS.

Pokud vaše zařízení Android nedokáže určit vaši polohu, povolte (nebo deaktivujte, pokud je povoleno) možnost „Služby Google Play“ v nastavení aplikace.

Poznámka: Zobrazí se pouze v případě, že máte na svém zařízení Android nainstalované (povolené) služby Google Play. Služby Google Play slouží k přesnějšímu určení polohy. Pokud po deaktivaci této možnosti zaznamenáte problémy s přesností polohy, zapněte ji.

**iOS**

Pokud používáte iPhone nebo iPad, zkontrolujte nastavení iOS → Soukromí → Služby určování polohy. Pro organické mapy by mělo být povoleno sdílení geolokačních dat.

**Poznámky:**

* Chcete-li se vyhnout nechtěným datům při roamingu, můžete v nastavení zařízení vypnout všechna mobilní data, aktivovat letový režim nebo deaktivovat mobilní data pro organické mapy. Zařízení Android a iOS mohou používat GPS v režimu letu.

* Některá mobilní zařízení nemají vestavěné GPS přijímače, jako je iPod Touch, iPad pouze s WiFi, Amazon Kindle Fire/Kindle Fire HD 7 a některé tablety Android. Na těchto zařízeních budou všechny aplikace zobrazovat vaši přibližnou polohu zjištěnou pomocí sítě Wi-Fi, pokud jste připojeni k internetu.

* Detekce polohy pomocí satelitů GPS (když jsou WiFi a mobilní sítě vypnuté) může nějakou dobu trvat. Čím déle se GPS nepoužívá, tím déle to trvá. Rychlost zjišťování polohy závisí na zařízení, nikoli na aplikaci. Provoz GPS je ovlivněn i počasím – nejlépe funguje venku, když je jasná obloha. Problémy mohou nastat, když se snažíte najít svou polohu v interiéru, na úzké ulici nebo při řízení auta, když je kolem hodně kovu nebo když je na krytu zařízení kov/magnet.


**Na mapě se zobrazuje nesprávná poloha**

1. Pokud je kolem šipky vaší polohy na mapě velký poloprůhledný kruh, znamená to, že vaše poloha je určena s nízkou přesností pomocí WiFi nebo mobilního připojení. Ujistěte se, že jste v nastavení systému povolili "Přesnou" polohu pro Organic Maps, a zkuste jít ven, pryč od vysokých budov a stromů, abyste zlepšili příjem satelitního signálu GPS.

2. Pokud je vaše poloha určena nesprávně (například jste v jednom městě, ale aplikace ukazuje jiné město), pak jste s největší pravděpodobností v oblasti postižené falešným signálem GPS (GPS spoofing) v důsledku opatření elektronického boje (EW). V takových případech je jediným řešením přesunout se na jiné místo.