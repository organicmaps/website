---
title: "Routenoptimierung, verbesserte Alternativrouten, das Ausblenden einzelner Tracks und zeitweise wasserführende Flächen im September-Update 2026"
date: 2026-09-29
slug: "mehrfachauswahl-lesezeichen-tracks-carplay-dashboard-tracks-ausblenden-links-teilen-august-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Bereit zum Aufbruch? Das September-Update bringt verbesserte Alternativrouten, eine Einstellung zur Optimierung der Reihenfolge der Zwischenstopps, deutlichere Markierungen für zeitweise wasserführende Flächen und ein Augensymbol zum Ausblenden einzelner Tracks sowie viele weitere Fehlerbehebungen und Verbesserungen (siehe unten).

Installiere oder aktualisiere Organic Maps über <https://get.omaps.org>, den [App Store][appstore], [Google Play][googleplay], die [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] oder [F-Droid][fdroid].

Falls du unsere bisherigen Updates verpasst hast, schau dir die im [Juni](@/news/2026-06-29/610/index.de.md), [Juli](@/news/2026-07-23/620/index.de.md) und [August](@/news/2026-08-31/630/index.de.md) veröffentlichten Funktionen an. Vielen Dank an unsere Mitwirkenden und Nutzer, die diese Updates möglich gemacht haben!

## So unterstützt du Organic Maps

- [Spende](@/donate/index.de.md), um die Entwicklung zu unterstützen und die Kosten für das Hosting der Karten zu decken
- [Schick uns dein Feedback und unterstütze](@/contribute/index.de.md) das Projekt
- Mach beim Beta-Test mit, um neue Funktionen schon früh auszuprobieren und Probleme auf [iOS][testflight], [Android][firebase] und [dem Desktop][flathub] zu melden
- Sag es weiter und hilf uns, eine bessere Alternative zu den Karten der großen Technologiekonzerne zu entwickeln!

## Versionshinweise

### Karte

- OpenStreetMap-Daten vom 28. September 2026
- Wikipedia-Daten vom 21. September 2026
- Die Suche wurde korrigiert, wenn der sichtbare Kartenbereich den 180°-Meridian (±180° Längengrad) überschreitet _(Viktor Govako)_
- Zeitweise wasserführende Flächen werden nun mit einem gepunkteten Muster dargestellt, ähnlich dem Muster für Sand _(Alexander Borsuk)_
- Wasserreservoirs sind jetzt sichtbar, wenn man weiter herauszoomt _(Alexander Borsuk)_
- Wassertunnel werden auf der Karte nicht mehr angezeigt _(Alexander Borsuk)_
- Die Symbole für die U-Bahn-Stationen und Eingänge in Suzhou wurden korrigiert _(Alexander Borsuk)_
- Es wurden seltene Fälle behoben, bei denen sich Beschriftungen auf der U-Bahn-Kartenebene verschoben haben _(Viktor Govako)_

### Routenplanung und Navigation

- Alternativrouten und ihre voraussichtlichen Ankunftszeiten verbessert _(Alexander Borsuk, Viktor Govako)_
- Die ausgewählte alternative Route bleibt nun erhalten, wenn die Navigation die Route neu berechnet _(Alexander Borsuk)_
- Die Reihenfolge der Zwischenstopps wird nun nach einem Neustart der App wiederhergestellt _(Kiryl Kaveryn)_

### Weitere Verbesserungen

- In den Öffnungszeiten wird nun „Mittag“ für 12:00 Uhr und „Mitternacht“ für 00:00 Uhr bzw. 24:00 Uhr angezeigt _(Alexander Borsuk)_
- Fehler behoben und die Track-Aufzeichnung verbessert _(Alexander Borsuk)_
- Fehler beim Import von KMB-Dateien behoben _(Alexander Borsuk)_
- Korrigierte Übersetzungen ins Französische und Asturische _(Alexander Borsuk)_
- Ein Tippfehler im Englischen wurde korrigiert _(Carl Morris)_

### iOS

- Ein Augensymbol zum Ausblenden einzelner Tracks wurde hinzugefügt _(Kiryl Kaveryn)_
- Schaltflächen zum Hinzufügen oder Ersetzen eines Stopps in einer geplanten Route hinzugefügt _(Kiryl Kaveryn)_
- Es wurde eine Einstellung hinzugefügt, um die Reihenfolge der Zwischenstopps auf der Route zu optimieren _(Kiryl Kaveryn)_
- Manöveranweisungen auf unterstützten Head-up-Displays (HUDs) im Auto und im CarPlay-Dashboard hinzugefügt _(Kiryl Kaveryn)_
- Fehler bei den CarPlay-Schaltflächen und der Suche behoben _(Alexander Borsuk)_
- Verschiedene Fehler wurden behoben und die Benutzeroberfläche verbessert _(Kiryl Kaveryn, Alexander Borsuk)_
- Unterstützung für die Auswahl einer installierten Navigationsstimme und das Anhören einer Sprachprobe hinzugefügt _(Kiryl Kaveryn, Alexander Borsuk)_
- Die Kategoriesuche in Spotlight wurde wiederhergestellt _(Kiryl Kaveryn)_

### Android

- Es wurde eine Einstellung hinzugefügt, um die Reihenfolge der Zwischenstopps auf der Route zu optimieren _(Mikhail Listratsenka)_
- Schaltflächen zum Hinzufügen oder Ersetzen eines Stopps in einer geplanten Route hinzugefügt _(Mikhail Listratsenka)_
- Die Möglichkeit hinzugefügt, die Track-Aufzeichnung direkt über die Benachrichtigung zu beenden und den Track zu speichern _(Alexander Borsuk)_
- Die Schaltfläche „Stopp einfügen“ fügt nun einen Stopp nach den bestehenden Stopps und vor dem Ziel hinzu _(Mikhail Listratsenka)_
- Verbesserte Uploads aus dem OpenStreetMap-Editor _(Owm)_
- Das Design der Benutzeroberfläche wurde aktualisiert _(Mikhail Listratsenka)_
- Der Lesezeichen-Editor und andere Dialoge bleiben jetzt während der Navigation geöffnet _(Mikhail Listratsenka)_
- Darstellung von Höhenprofilen für flache Tracks und in von rechts nach links verlaufenden Benutzeroberflächen korrigiert _(Mikhail Listratsenka)_
- Problem behoben, bei dem die Schaltflächen auf der Karte von den Systembalken abgeschnitten wurden _(Mikhail Listratsenka)_
- Fehler behoben und die Android Auto-Unterstützung verbessert _(Andrei Shkrob)_
- Ein Absturz beim Rendern der Karte wurde behoben _(Viktor Govako)_

### Desktop

- Die ausführbare Datei für den Desktop und das App-Bundle für macOS wurden in `OrganicMaps` umbenannt _(Alexander Borsuk)_
- Probleme in der Windows-App behoben _(Osyotr, Alexander Borsuk)_
- Das Befehlszeilenargument `--lang` hat nun Vorrang vor der Spracheinstellung der App _(Alexander Borsuk)_

Mit Freude und Leidenschaft,

Dein Organic Maps-Team

{{ <references lang /> }}
