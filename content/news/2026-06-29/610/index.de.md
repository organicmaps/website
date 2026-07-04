---
title: "Satellitenbilder, ÖPNV-Routen, Alternativrouten, neue Such- und Routenplanungsoberfläche für Android, Unterstützung großer Bedienungshilfen-Schriften für iOS und mehr im Juni-2026-Update"
date: 2026-06-29
slug: "satellitenbilder-oepnv-routen-alternativrouten-neue-suche-routenplanung-android-grosse-schriften-ios-juni-2026"
taxonomies:
  news: ["releases"]
---

Im Juni-Update von Organic Maps gibt es viele spannende neue Funktionen und Fehlerbehebungen zum Ausprobieren, darunter:
- Satellitenbilder
- ÖPNV-Routen
- Alternativrouten
- Neue Such- und Routenplanungsoberfläche für Android
- Unterstützung großer Bedienungshilfen-Schriften für iOS

Hol es dir unter <https://get.omaps.org> oder im [App Store][appstore], bei [Google Play][googleplay], in der [Huawei AppGallery][appgallery], über [Obtainium][obtainium], [Accrescent][accrescent] und [F-Droid][fdroid] und sag uns, was du denkst!

## Ausführliches Änderungsprotokoll

- NEU! Routenplanung mit öffentlichen Verkehrsmitteln per U-Bahn, Stadtbahn, Bus und Straßenbahn _(Viktor Govako)_
- NEU! Alternativrouten: Zusätzlich zur schnellsten Route zeigt die App jetzt auch die kürzeste Route _(Viktor Govako)_
- NEU! Warnungen für Fuß- und Fahrradrouten vor Treppen, Toren und Schranken entlang des Weges _(Viktor Govako)_
- NEU! Wähle eine beliebige Farbe für Lesezeichen _(Alexander Borsuk, Mikhail Listratsenka)_
- NEU! Unterstützung für Koordinaten des British National Grid (OS Grid), Irish Grid und Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTELL: Aktiviere Satellitenbilder in den Organic Maps-Einstellungen mit einer eigenen Rasterkachel-Server-URL. Wir arbeiten noch an unserem eigenen Server, suche daher bitte einen öffentlich verfügbaren Server mit den Platzhaltern `{x}`, `{y}`, `{z}` in der URL _(Viktor Govako, renderexpert)_
- OpenStreetMap-Daten aktualisiert mit Stand vom 24. Juni _(Viktor Govako)_
- Wikipedia-Daten aktualisiert mit Stand vom 20. Juni, einschließlich Artikeln auf Italienisch _(Alexander Borsuk)_
- Gib `?map-download-server:https://your-server.com/` in das Suchfenster ein, um die Karten-Download-Server von Organic Maps zu überschreiben. Gib `?no-map-download-server` ein, um die Überschreibung zu entfernen _(Alexander Borsuk)_

#### Kartendarstellung und Stile

- Schönere Muster für Strand-, Sand-, Schutt-, Fels-, Obstgarten- und Weinbergflächen sowie Schraffuren für Schutzgebiete und Feuchtgebiete _(Alexander Borsuk)_
- Glattere gebogene Textbeschriftungen für Straßen und Flüsse _(Viktor Govako)_
- Flüsse, Bäche und Feuchtgebiete haben im Dunkelmodus höheren Kontrast und sind besser sichtbar _(Alexander Borsuk)_
- Neue und verbesserte Symbole für die Kategoriesuche und Suchergebnisse auf der Karte _(Anton Makouski)_
- Verbesserte mehrsprachige Textformung und Darstellung _(Alexander Borsuk)_
- Verschiedene Fehlerkorrekturen und Leistungsverbesserungen _(Viktor Govako)_

#### Tracks, Lesezeichen und Routen

- GeoJSON-Tracks behalten beim Import und Export jetzt Höhenangaben und Zeitstempel _(Alexander Borsuk)_
- Absturz nach dem Verschieben eines Tracks in eine andere Liste behoben _(Viktor Govako)_
- Webseiten werden jetzt für Kulturdenkmäler angezeigt _(Viktor Govako)_
- Betreibernamen werden jetzt für unbenannte Suchergebnisse angezeigt. Zum Beispiel zeigt ein unbenannter Geldautomat jetzt seine Bank an _(Anton Makouski)_
- Editor: Beschreibungstext für OpenStreetMap-Bearbeitungen/Changesets von Mehrfamilienhäusern korrigiert _(titanniya542-spec)_
- Verbesserte HTML-Erkennung in Beschreibungen von Lesezeichen und Tracks _(Alexander Borsuk)_

### iOS

- NEU! Bedienungshilfen-Unterstützung für Dynamic Type und große Schriften _(Kiryl Kaveryn)_
- NEU! Antippen, um zwischen überlappenden Tracks und Routen zu wählen _(Kiryl Kaveryn)_
- Verbesserte HTML-Darstellung von Beschreibungen für Lesezeichen und Tracks _(Kiryl Kaveryn)_
- Klarere Tabellenformatierung in der Benutzeroberfläche _(Kiryl Kaveryn)_

### Android

- NEU! Suchoberfläche _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NEU! Routenplanungsoberfläche _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Verbesserte HTML-Darstellung von Beschreibungen für Lesezeichen und Tracks _(Mikhail Listratsenka)_
- APK-Größe reduziert _(Alexander Borsuk)_
- Das Sprachsymbol wird als deaktiviert angezeigt, wenn keine Text-to-Speech-Engine verfügbar ist _(Mikhail Listratsenka)_
- Lange Beschreibungen von Lesezeichen und Tracks zeigen jetzt eine Schaltfläche „…mehr“ _(Mikhail Listratsenka)_
- Verschiedene UI-Korrekturen und eine API-Korrektur für zurückgegebene Punkt-IDs _(Mikhail Listratsenka)_

### Desktop

- Unterstützung zum Wechseln des angezeigten Koordinatensystems _(Alexander Borsuk)_
- Informationen zum ausgewählten Ort werden jetzt links angezeigt _(Viktor Govako)_
- Position des Kontextmenüs korrigiert _(Osyotr)_
- Hängenbleiben bei OpenStreetMap-Anmeldung und -Bearbeitungen unter Qt-Versionen 6.4 und älter behoben _(Alexander Borsuk)_
- Unerwarteter Kartenstilwechsel während der Routenführung auf macOS behoben _(Alexander Borsuk)_
- Absturz beim Schließen der macOS-App nach dem Export einer KMZ-Datei behoben _(Alexander Borsuk)_

### Übersetzungen

- Kantonesische Sprachanweisungen für die Turn-by-turn-Navigation _(Alexander Borsuk)_
- Deutsche und französische Übersetzungen aktualisiert _(Wuzzy, Alexander Borsuk)_
- Falsche Sprachanweisungsübersetzungen für „onto street“ auf Chinesisch, Serbisch und Katalanisch korrigiert _(Alexander Borsuk)_

## Mach beim Beta-Test mit, um frühe Funktionen auszuprobieren und Probleme zu melden:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Wir sind all unseren Nutzern und Mitwirkenden dankbar, allen, die [spenden](@/donate/index.de.md) und Organic Maps in den App-Stores mit 5 Sternen bewerten. Gemeinsam können wir die beste Karten-App bauen!

Mit Liebe,
Organic Maps Team

{{ references() }}
