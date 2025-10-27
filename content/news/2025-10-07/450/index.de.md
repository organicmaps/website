---
title: "Oktober-Release: Geschwindigkeitsbegrenzungen in Android Auto, GeoJSON-Import, Aufnahmestatistiken, Anzeige von OSM-Beschreibungs-Tags, Lesezeichen auf ausgewählter Strecke auf iOS speichern und mehr"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

Dieses Oktober-Update von Organic Maps fügt die Anzeige von Geschwindigkeitsbegrenzungen in Android Auto, GeoJSON-Import, Aufnahmestatistiken hinzu, zeigt OSM-Beschreibungs-Tags an (gib `?description` in das Suchfeld ein, um sie zu sehen) und speichert ein Lesezeichen auf einer Strecke auf iOS. Es gibt auch viele Verbesserungen der Benutzeroberfläche, der OpenStreetMap-Bearbeitung und verschiedene Fehlerbehebungen auf allen Plattformen, einschließlich der Behebung des Absturzes beim Start auf einigen Android-Geräten.

Organic Maps ist dank ❤️ unserer Mitwirkenden, [deiner Spenden](@/donate/index.de.md) und [deiner Unterstützung](@/contribute/index.de.md) möglich.

### Detaillierte Versionshinweise (einschließlich der Änderungen des vorherigen kleinen Updates)

- NEU! GeoJSON-Import (Sergiy Kozyr)
- OpenStreetMap-Daten vom 4. Oktober
- Wikipedia-Daten vom 1. Oktober
- Unterstützung der Stadtbahn Seattle für öffentliche Verkehrsmittel (tjasz)
- Kartenauswahl beim Speichern eines bearbeiteten OSM-Ortes nicht deaktivieren (Kiryl Kaveryn)
- Aktualisierte Übersetzungen (Weblate-Mitwirkende)

#### Kartenstile

- Fahrradverleihgeschäfte anzeigen, die als amenity=bicycle + rental=shop gekennzeichnet sind (David Martinez)
- Historische archäologische Stätten ab Zoom 12 und andere historische Stätten ab Zoom 15 im Outdoor-Stil anzeigen (Viktor Govako)
- Neue Symbole für Masten, Kommunikations- und Stromtürme im Outdoor-Stil (David Martinez)
- Gipfelsymbolsgröße im Outdoor-Stil erhöhen (David Martinez)
- Fehlende POI-Symbolvarianten hinzufügen (David Martinez)
- Weitere Barrieretypen hinzugefügt (Viktor Govako)

#### iOS

- NEU: Lesezeichen am ausgewählten Streckenpunkt speichern (Kiryl Kaveryn)
- NEU: Aufnahmestrecke löschen, ohne sie vorher zu speichern (Kiryl Kaveryn)
- Mehrzeilige Lesezeichenlistentitel auf der Ortsinformationsseite anzeigen (David Martinez)
- OSM-Anmeldeschaltflächenstil aktualisieren (Kiryl Kaveryn)
- Problem bei der Aktualisierung von Navigationsinformationen beheben (Kiryl Kaveryn)
- Probleme bei der Planung neuer Routen beheben (Kiryl Kaveryn)
- Sichtbarkeit von OSM-Ort hinzufügen/bearbeiten für Karten älter als 3 Monate beheben (Kiryl Kaveryn)
- Layout der Transportoptionssegmentsteuerung für iOS 26 beheben (Kiryl Kaveryn)
- Lesezeichenauswahlanimationen vereinfachen (Kiryl Kaveryn)
- Problem bei der Auswahl von Suchergebnissen beheben (Kiryl Kaveryn)
- Stil, Wischen und Animationen für Ortsinformationsseite behoben (Kiryl Kaveryn)

#### Android Auto (nur Google Play)

- NEU: Geschwindigkeitsbegrenzungsanzeige in Android Auto (Andrei Shkrob)
- Displaywechsel im Android Auto-Navigationsmodus beheben (Andrei Shkrob)
- Routenpfeil-Versatz in Android Auto beheben (Andrei Shkrob)
- Problem beheben, wenn ein Gerät mit einem Auto verbunden/getrennt wird (Andrei Shkrob)
- Android Auto Standortdienst hinzufügen (Andrei Shkrob)
- Android Auto Routensimulator verbessern (Viktor Govako)

#### Android

- NEU: Aufnahmestatistiken in Echtzeit anzeigen (Kavi Khalique)
- NEU: OSM `description`-Tag-Inhalt anzeigen (Alexander Borsuk)
- Themenwechselbehandlung beheben (Andrei Shkrob)
- Mehrere Abstürze behoben, einschließlich des Absturzes beim Start (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Stille Download-Fortschrittsbenachrichtigungen (Viktor Govako)
- Stiftsymbol-Abstand reduzieren (Alexander Borsuk)

#### Desktop

- Hängendes curl unter Linux beheben (Alexander Borsuk)
- Hängen auf macOS beim Anmelden bei OSM beheben (Alexander Borsuk)
- Aktion zum Auswählen von Funktionen aus dem Kontextmenü (Viktor Govako)
- Option zum Abbrechen des Downloads (Viktor Govako)
- Geometrietyp im Kontextmenü anzeigen (Viktor Govako)

### Kürzlich veröffentlichte Funktionen, die du verpasst haben könntest

- Liniennummern des öffentlichen Verkehrs beim Auswählen einer Bushaltestelle
- Wander- und Fahrradrouten (über die Schaltfläche Ebenen oben links aktivieren)
- Lesezeichennamen auf der Karte anzeigen, indem du es in den App-Einstellungen aktivierst
- Das ✎ Stiftsymbol bietet eine schnelle Möglichkeit, Lesezeichen zu bearbeiten

### Organic Maps installieren

Hol dir die neueste Version von Organic Maps aus dem [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] und [F-Droid][fdroid].

Tritt den Betatests für frühe Funktionen bei: [iOS][testflight] / [Android][firebase].

{{ references() }}
