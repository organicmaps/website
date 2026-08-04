---
title: "Release 15. September: Neue Routenplanung und OSM-Beschreibungen"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["releases"]
---

Dieses zweite September-Release bringt einen neu gestalteten Routenplanungsbildschirm und die Anzeige des OpenStreetMap-`description`-Tags auf iOS. Um Orte mit diesem Tag zu finden, gib `?description` in die Suche ein (ähnlich wie `?wiki`).

Außerdem enthält es viele Fehlerbehebungen und Verbesserungen für iOS und Android (Details unten).

Neuere Funktionen, die du vielleicht verpasst hast:
- Liniennummern der öffentlichen Verkehrsmittel beim Auswählen einer Haltestelle
- Wander- und Fahrradrouten (über die Schaltfläche Ebenen links oben aktivieren)
- Lesezeichennamen auf der Karte anzeigen (in den Einstellungen aktivieren)
- Das ✎ Stiftsymbol ermöglicht schnelles Bearbeiten von Lesezeichen

Organic Maps ist dank unserer Mitwirkenden, [deiner Spenden](@/donate/index.de.md) und [deiner Unterstützung](@/contribute/index.md) möglich.

### Detaillierte Versionshinweise

- Neue OpenStreetMap-Daten vom 13. September
- Sehr kleine Inseln von der Weltkarte entfernt (Viktor Govako)
- Postleitzahl (ZIP) in Adressdetails anzeigen (Viktor Govako)
- Falsche Kartenzentrierung auf aktueller Position behoben (Kiryl Kaveryn, Viktor Govako)
- Lesezeichenfarben beim Export/Import von GPX beibehalten (cyber-toad)
- Aktualisierte Übersetzungen (Weblate-Mitwirkende)

#### Kartenstile (Viktor Govako)

- Beleuchtungsgeschäfte anzeigen
- Stromleitungen ab Zoom 18 anzeigen
- Referenznamen für Kraftwerke und Umspannwerke anzeigen
- Camping- und Stellplätze im Navigationsmodus anzeigen
- Farbe von Nebenstraßen im Navigationsmodus korrigieren
- Grenzen von Nationalparks zeichnen
- Archäologische Stätten ab Zoom 12 im Outdoor-Stil zeichnen

#### iOS

- NEU: Anzeige des OSM-`description`-Tags (Suche nach `?description`) (Kiryl Kaveryn, Viktor Govako)
- NEU: Überarbeiteter Routenplanungsbildschirm (Kiryl Kaveryn)

#### Android

- Neue Kreisverkehr-Symbole in Android Auto (Andrei Shkrob)
- Kategorie des ausgewählten Lesezeichens anzeigen (Alexander Borsuk)
- Verzögerung bei Anzeige der Entfernung zu einem Lesezeichen behoben (Alexander Borsuk)
- Dunkles Thema überarbeitet (Andrei Shkrob)
- Positionsaktualisierung im Navigationsmodus auf Custom-ROMs behoben (z.B. Lineage + MicroG) (Viktor Govako)
- Blaues Stift-Symbol (Bearbeiten) für Lesezeichen (Alexander Borsuk)
- Vertikale Höhe der Ortsinfo-Vorschau reduziert (Alexander Borsuk)
- Azimut-Winkel nach Norden aus der Vorschau entfernt (tippe auf den blauen Pfeil mit der Entfernung, um ihn zu sehen) (Alexander Borsuk)

Hol dir die neueste Organic Maps-Version aus dem [App Store][appstore], [Google Play][googleplay], der [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] und [F-Droid][fdroid].

P.S. Tritt den Betatests bei, um neue Funktionen früher zu erhalten: [iOS][testflight] / [Android][firebase].

{{ references() }}
