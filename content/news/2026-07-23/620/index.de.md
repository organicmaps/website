---
title: "Fehlerbehebungen und Verbesserungen für den öffentlichen Nahverkehr, die Routenplanung, die Suche und die Lesezeichen im Update vom Juli 2026"
date: 2026-07-23
slug: "fehlerbehebungen-verbesserungen-oepnv-routenplanung-suche-lesezeichen-juli-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Wie Sie vielleicht schon bemerkt haben, ist das Juli-Update von Organic Maps erschienen. Sie können es unter <https://get.omaps.org> oder auf [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] und [F-Droid][fdroid] herunterladen.

Dank Ihrer [Spenden](@/donate/index.de.md) und Ihres [Feedbacks](@/contribute/index.de.md) haben wir uns im Juli auf Fehlerbehebungen und Verbesserungen konzentriert. Falls Sie es verpasst haben: Die folgenden Funktionen aus der [vorherigen Juni-Version](@/news/2026-06-29/610/index.de.md) sind ebenfalls verfügbar:
- ÖPNV-Routen (Echtzeit-Fahrpläne sind in Vorbereitung)
- Satellitenbilder
- Alternative Routen zum Autofahren, Wandern und Radfahren
- Neue Such- und Routenplanungsoberfläche für Android
- Unterstützung für große Barrierefreiheits-Schriftarten auf iOS

## Ausführliches Änderungsprotokoll

### Karte & Orte
- OpenStreetMap-Daten mit Stand vom 14. Juli
- Notizen, die an [OpenStreetMap](https://www.openstreetmap.org) gemeldet werden, werden nun genau an der von Ihnen ausgewählten Stelle platziert und nicht mehr in der Mitte der gesamten Straße oder des gesamten Gebiets _(Alexander Borsuk)_
- Verbesserte Ortsauswahl beim Antippen der Karte in Regionen, die den 180°-Antimeridian überqueren _(Viktor Govako)_
- Höhenprofile von Tracks zeigen nach dem Löschen eines Tracks keine veralteten oder leeren Diagramme mehr an _(Kiryl Kaveryn)_

### Öffentliche Verkehrsmittel
- Haltestellen-, Umsteige- und Bahnhofsnamen sind nun weiß umrandet, damit sie sowohl im hellen als auch im dunklen Design gut lesbar bleiben _(Viktor Govako)_
- Die U-Bahn-Ebene wird wieder korrekt angezeigt, nachdem Sie die Vorschau einer ÖPNV-Route geschlossen haben _(Mikhail Listratsenka)_

### Routenplanung und Navigation
- Für alle Alternativrouten werden nun Routenhinweise (Maut, Fähren, unbefestigte Straßen, Stufen usw.) angezeigt _(Viktor Govako)_
- Ein selten auftretendes Einfrieren beim Erstellen einer Route wurde behoben _(Viktor Govako)_
- Verbesserte Behandlung von Sackgassen sowie von Start- und Endpunkten auf Straßen mit Verkehrsbeschränkungen _(Viktor Govako)_
- Falsche und fehlende Abbiegehinweise wurden korrigiert _(Alexander Borsuk)_

### iOS
- Neue Einstellung „Suchverlauf speichern“, mit der Sie den Verlauf deaktivieren und ausblenden können, falls Sie ihn lieber nicht behalten möchten _(Kiryl Kaveryn)_
- Neue Schaltfläche „Bearbeiten“ zum einfacheren Löschen von Lesezeichen _(Kiryl Kaveryn)_
- Lesezeichen werden nun automatisch gespeichert, wenn Sie den Bildschirm verlassen _(Kiryl Kaveryn)_
- Die Farbpalette bietet nun vordefinierte Farben und ermöglicht es Ihnen, eine beliebige benutzerdefinierte Farbe auszuwählen _(Kiryl Kaveryn)_
- Der Leerzustand des Höhendiagramms für einen aufgezeichneten Track wurde verbessert _(Kiryl Kaveryn)_
- Die Anzeige des Routenfortschritts auf der Schaltfläche „Start“ wurde verbessert _(Kiryl Kaveryn)_
- Das Neuanordnen der Haltestellen auf einer Route führt nicht mehr dazu, dass die Liste hin und her springt _(Kiryl Kaveryn)_
- Weitere kleinere Verbesserungen an der Benutzeroberfläche _(Kiryl Kaveryn)_

### Android
- Die Öffnungszeiten zeigen nun geteilte Schichten (z. B. eine Mittagspause), beginnen mit dem heutigen Tag und zeigen die ganze Woche ohne separaten Bildlaufbereich _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Eine übersichtlichere Suchleiste mit einer kombinierten Schaltfläche zum Löschen und zur Sprachsteuerung, einem Symbol zum Löschen, das sich nicht mehr verschiebt, sowie Layout-Korrekturen für Querformat und Drehung des Telefons _(Mikhail Listratsenka)_
- Überarbeiteter Lesezeichen- und Track-Editor _(Mikhail Listratsenka)_
- Korrekturen und Verbesserungen bei der Routenplanung _(Mikhail Listratsenka)_
- Die Farbauswahl wird nun automatisch geschlossen, und ein Absturz unter Android 5 wurde behoben _(Mikhail Listratsenka)_
- Abstürze behoben _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- Die Liste der zum Download verfügbaren Karten ist nun alphabetisch sortiert _(goncalo109560)_

### Übersetzungen
- Verbesserter chinesischer Wortlaut _(Chenxi Zhao)_
- Aktualisierte ukrainische Übersetzungen _(Nnifria)_
- Die italienischen Übersetzungen der Namen der Kartenregionen wurden korrigiert _(Vittorio Bertola)_

## Machen Sie beim Beta-Test mit, um frühe Funktionen auszuprobieren und Probleme zu melden:

Tipp: Die Beta-Version bietet eine neue Geländeschattierung, verbesserte Höhendaten mit Unterstützung für Fuß und Meter sowie weitere coole Funktionen!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Einen schönen Sommer!
Organic Maps Team

{{ references() }}
