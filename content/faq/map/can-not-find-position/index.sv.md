---
title: Appen kan inte hitta min position på kartan
description: Felsökningsguide för att lösa problem med platsbestämning för iOS- och
  Android-enheter
updated: '2024-06-20'
taxonomies:
  faq:
  - Map
extra:
  order: 10
---

Se till att din enhet har GPS, att platstjänster är aktiverade och att platsbehörigheter ges till organiska kartor.

**Android**

Öppna Inställningar → Plats på din enhet. Det är bättre att slå på högprecisionsläget, eftersom det möjliggör exakt GPS-position.

Om din Android-enhet inte kan fastställa din plats, aktivera (eller inaktivera, om aktiverat) alternativet "Google Play Services" i appinställningarna.

Obs: du kan bara se det om du har Google Play-tjänster installerade (aktiverade) på din Android-enhet. Google play-tjänster används för att bestämma plats mer exakt. Om du upplever problem med platsnoggrannheten efter att du inaktiverat alternativet, aktivera det.

**iOS**

Om du använder iPhone eller iPad, kontrollera iOS-inställningar → Sekretess → Platstjänster. Geolokaliseringsdatadelning bör aktiveras för organiska kartor.

**Anmärkningar:**

* För att undvika oönskad data under roaming kan du stänga av all mobildata, aktivera ett flygläge eller inaktivera mobildata för organiska kartor i dina enhetsinställningar. Android- och iOS-enheter kan använda GPS i flygläget.

* Vissa mobila enheter har inte inbyggda GPS-mottagare, som iPod Touch, iPad med endast WiFi, Amazon Kindle Fire/Kindle Fire HD 7 och vissa Android-surfplattor. På dessa enheter kommer alla appar att visa din ungefärliga plats som identifierats med hjälp av ett Wi-Fi-nätverk, så länge du är ansluten till internet.

* Platsdetektering med GPS-satelliter (när WiFi och mobilnät är inaktiverade) kan ta lite tid. Ju längre GPS:en inte har använts, desto längre tid tar det. Hastigheten för platsdetektering beror på enheten, inte appen. GPS-driften påverkas också av vädret – den fungerar bäst utomhus när himlen är klar. Problem kan uppstå när du försöker lokalisera dig inomhus, på en smal gata, eller när du kör bil, med mycket metall runt eller med en metall/magnet på enhetens hölje.
