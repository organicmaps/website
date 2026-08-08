---
title: "Aplikace nemůže najít mou polohu na mapě nebo ukazuje nesprávnou polohu"
slug: aplikace-nemůže-najít-moji-polohu-na-mapě
description: "Průvodce řešením problémů s polohou a aktuální GPS pozicí na mapě pro zařízení iOS a Android"
updated: "2026-01-04"
taxonomies:
  faq:
  - map
extra:
  order: 10
aliases:
  - /cs/faq/map/can-not-find-position/
---

Ujisti se prosím, že tvoje zařízení má GPS, že jsou povoleny služby určování polohy a že aplikaci Organic Maps jsou udělena oprávnění k poloze.

**Android**

Na svém zařízení otevři Nastavení → Umístění. Je lepší zapnout režim vysoké přesnosti, protože umožňuje přesnou polohu GPS.

Pokud tvoje zařízení Android nedokáže určit tvoji polohu, povol (nebo deaktivuj, pokud je povoleno) možnost „Služby Google Play“ v nastavení aplikace.

Poznámka: Zobrazí se pouze v případě, že máš na svém zařízení Android nainstalované (povolené) služby Google Play. Služby Google Play slouží k přesnějšímu určení polohy. Pokud po deaktivaci této možnosti zaznamenáš problémy s přesností polohy, zapni ji.

**iOS**

Pokud používáš iPhone nebo iPad, zkontroluj nastavení iOS → Soukromí → Služby určování polohy. Pro Organic Maps by mělo být povoleno sdílení geolokačních dat.

**Poznámky:**

* Chceš-li se vyhnout nechtěným datům při roamingu, můžeš v nastavení zařízení vypnout všechna mobilní data, aktivovat letový režim nebo deaktivovat mobilní data pro Organic Maps. Zařízení Android a iOS mohou používat GPS v režimu letu.

* Některá mobilní zařízení nemají vestavěné GPS přijímače, jako je iPod Touch, iPad pouze s WiFi, Amazon Kindle Fire/Kindle Fire HD 7 a některé tablety Android. Na těchto zařízeních budou všechny aplikace zobrazovat tvoji přibližnou polohu zjištěnou pomocí sítě Wi-Fi, pokud jsi připojen k internetu.

* Detekce polohy pomocí satelitů GPS (když jsou WiFi a mobilní sítě vypnuté) může nějakou dobu trvat. Čím déle se GPS nepoužívá, tím déle to trvá. Rychlost zjišťování polohy závisí na zařízení, nikoli na aplikaci. Provoz GPS je ovlivněn i počasím – nejlépe funguje venku, když je jasná obloha. Problémy mohou nastat, když se snažíš najít svou polohu v interiéru, na úzké ulici nebo při řízení auta, když je kolem hodně kovu nebo když je na krytu zařízení kov/magnet.


**Na mapě se zobrazuje nesprávná poloha**

1. Pokud je kolem šipky tvojí polohy na mapě velký poloprůhledný kruh, znamená to, že tvoje poloha je určena s nízkou přesností pomocí WiFi nebo mobilního připojení. Ujisti se, že jsi v nastavení systému povolil "Přesnou" polohu pro Organic Maps, a zkus jít ven, pryč od vysokých budov a stromů, abys zlepšil příjem satelitního signálu GPS.

2. Pokud je tvoje poloha určena nesprávně (například jsi v jednom městě, ale aplikace ukazuje jiné město), pak jsi s největší pravděpodobností v oblasti postižené falešným signálem GPS (GPS spoofing) v důsledku opatření elektronického boje (EW). V takových případech je jediným řešením přesunout se na jiné místo.