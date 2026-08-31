---
title: "Mehrfachauswahl für Lesezeichen und Tracks, ein CarPlay-Dashboard, das Ausblenden von Tracks auf der Karte und lesbare Links zum Teilen im Update vom August 2026"
date: 2026-08-31
slug: "mehrfachauswahl-lesezeichen-tracks-carplay-dashboard-tracks-ausblenden-links-teilen-august-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "02 Bookmarks and tracks multi-selection move, change color, delete.jpg"
---

Hol dir die Organic Maps-Version vom August 2026 unter <https://get.omaps.org> oder im [App Store][appstore], bei [Google Play][googleplay], in der [Huawei AppGallery][appgallery] und bei [Obtainium][obtainium] ([Accrescent][accrescent] und [F-Droid][fdroid] folgen in Kürze).

Warum aktualisieren?
- Mehrfachauswahl in Lesezeichen und Tracks mit Sammelaktionen zum Löschen, Verschieben und Ändern der Farbe
- CarPlay-Dashboard
- Einzelne Tracks auf der Karte ausblenden
- Lesbare Links zum Teilen von Orten, Lesezeichen und dem aktuellen Standort – dazu AirDrop auf iOS und eine „Share“-Aktion auf dem Desktop
- Sprachführung auf Armenisch und Laotisch
- Wikipedia-Artikel in 19 Sprachen
…und viele weitere Verbesserungen, Fehlerbehebungen und aktualisierte Kartendaten findest du weiter unten.

Vergiss auch nicht, die früheren Versionshinweise für [Juni](@/news/2026-06-29/610/index.de.md) und das [Juli-Update](@/news/2026-07-23/620/index.de.md) zu lesen.

## Vollständiges Änderungsprotokoll

### Karte & Orte

- Aktualisierte OpenStreetMap-Daten mit Stand vom 26. August 2026 _(Viktor Govako)_
- Aktualisierte Wikipedia-Artikel auf Arabisch, Bengali, Chinesisch, Englisch, Französisch, Deutsch, Hindi, Italienisch, Japanisch, Koreanisch, Marathi, Polnisch, Portugiesisch, Russisch, Spanisch, Tamil, Telugu, Türkisch und Urdu _(Alexander Borsuk)_
- Viele Probleme behoben, die dazu führten, dass die Öffnungszeiten falsch angezeigt wurden _(Alexander Borsuk)_
- Unterstützung für Vogelbeobachtungshütten hinzugefügt _(Batmaclos, Viktor Govako)_
- Bühnen, Hügel und Naturbögen zur Karte hinzugefügt sowie ein neues Symbol für Felsen _(David Martinez)_
- Die Größe der Symbole für Gipfel, Höhlen und Gebirgspässe wurde angepasst _(David Martinez)_
- Schutzgebiete, Nationalparks und Feuchtgebiete werden jetzt in helleren Farbtönen dargestellt _(Alexander Borsuk)_
- Ein Einfrieren der App und ein Problem, bei dem Tippen und Gesten gelegentlich ignoriert wurden, wurden behoben _(Alexander Borsuk)_

### Teilen, Lesezeichen & Tracks

- Wenn du einen Ort, ein Lesezeichen oder deinen aktuellen Standort teilst, wird jetzt ein lesbarer Link mit nützlichen Informationen verschickt _(Alexander Borsuk)_
- Exportierte Lesezeichen behalten nun ihre ursprünglichen Namen und Beschreibungen bei _(Alexander Borsuk)_
- Geteilte Lesezeichenlisten verwenden jetzt ihre angezeigten Namen anstelle der internen Dateinamen _(Alexander Borsuk)_
- Ein Problem bei der Anzeige des Höhenprofils behoben, das unmittelbar nach dem Start einer Track-Aufzeichnung auftreten konnte _(Kiryl Kaveryn)_

### Routenplanung und Navigation

- Wenn du eine Haltestelle oder eine Markierung auf der Route antippst, wird diese jetzt korrekt geöffnet, anstatt zwischen geplanten Routen zu wechseln _(Viktor Govako)_
- Die Planung von Routen für öffentliche Verkehrsmittel geht jetzt schneller _(Viktor Govako)_
- Falsche Abbiegehinweise wurden korrigiert _(Alexander Borsuk)_
- Ein fehlerhafter Startpunkt nach dem Neuberechnen einer Route wurde behoben _(Viktor Govako)_
- Lateritstraßen werden bei der Routenplanung nun als unbefestigte Straßen mit schlechter Fahrbahnqualität behandelt _(Julien Etienne)_
- Straßen mit dem Tag `access=unknown` werden nun wie Straßen mit privatem oder ausschließlich für Anlieger bestimmtem Zugang behandelt _(Julien Etienne)_
- Sprachführung auf Armenisch und Laotisch hinzugefügt _(Alexander Borsuk)_

### OpenStreetMap-Editor

- Wenn du das Feld „Öffnungszeiten“ leerst, bleibt die Schaltfläche „Speichern“ bzw. „Fertig“ nicht mehr deaktiviert _(Alexander Borsuk)_
- Uploads, die teilweise fehlgeschlagen sind, werden nun erneut versucht, anstatt als vollständig erfolgreich gemeldet zu werden _(Alexander Borsuk)_

### Übersetzungen

- Die [häufig gestellten Fragen](https://organicmaps.app/faq/) wurden aktualisiert, einschließlich der japanischen Übersetzung _(Alexander Borsuk)_
- Die japanische Übersetzung von „Jetzt geschlossen“ wurde korrigiert _(Viktor Govako)_
- Die chinesischen Übersetzungen von „Track“ und „deaktivieren“ wurden verbessert _(Chenxi Zhao)_

### iOS

- NEU: Die Lesezeichen- und Track-Liste unterstützt jetzt die Mehrfachauswahl – mit Sammelaktionen zum Löschen, Verschieben und Ändern der Farbe ausgewählter Einträge sowie den Optionen „Alle auswählen“ und „Auswahl aufheben“ _(Kiryl Kaveryn)_
- NEU: Ein CarPlay-Dashboard wurde hinzugefügt _(Kiryl Kaveryn)_
- AirDrop-Unterstützung für das Teilen von Orten hinzugefügt _(Kiryl Kaveryn)_
- Mehrere CarPlay-Probleme wurden behoben _(Kiryl Kaveryn, Alexander Borsuk)_
- Die Darstellung von HTML-Beschreibungen wurde korrigiert, wenn ein Lesezeichen auf der Karte ausgewählt wird _(Kiryl Kaveryn)_
- Ein Problem bei der Aktivierung des Kartenstils für die Autonavigation wurde behoben _(Kiryl Kaveryn, Alexander Borsuk)_
- Die Einstellungen wurden in die Bereiche „Allgemeine Einstellungen“, „Karte“, „Navigation“, „Netzwerk“ und „Privatsphäre“ neu gegliedert _(Kiryl Kaveryn)_
- Die Einstellung zur Kompasskalibrierung wurde entfernt, da die Kalibrierung nun automatisch erfolgt _(Kiryl Kaveryn)_
- Die benutzerdefinierte Farbauswahl im Popover der Farbpalette wurde wiederhergestellt _(Kiryl Kaveryn)_
- Der entsprechende Punkt wird jetzt auf der Karte angezeigt, während du in der Vorschau einer Wander- oder Radroute über das Höhenprofil ziehst _(Kiryl Kaveryn)_
- Probleme mit dem Kompass behoben, die dazu führen konnten, dass der Pfeil für die aktuelle Position in die falsche Richtung zeigte oder einfror _(Alexander Borsuk)_
- Ein Absturz wurde behoben, der auftrat, wenn ein OpenStreetMap-Upload im Hintergrund abgeschlossen wurde _(Alexander Borsuk)_

### Android

- NEU: Der Mehrfachauswahlmodus wurde zur Lesezeichen- und Track-Liste hinzugefügt. Du kannst ihn durch langes Drücken auf einen Eintrag oder über die Symbolleiste aufrufen und dann beliebige Kombinationen aus Lesezeichen und Tracks farblich anpassen, verschieben oder löschen _(Mikhail Listratsenka)_
- NEU: Einzelne Tracks können jetzt über das Augensymbol in der Liste oder auf dem Bildschirm mit den Track-Details auf der Karte ausgeblendet werden _(cyber-toad)_
- Android Auto und Android Automotive: Fahrspurpfeile für Wendemanöver korrigiert _(Andrei Shkrob, Viktor Govako)_
- Android Auto und Android Automotive: Fehler beim Umschalten zwischen Tag- und Nachtmodus behoben _(Andrei Shkrob)_
- Android Auto und Android Automotive: Die Suchliste bleibt jetzt während der Eingabe geöffnet _(Viktor Govako)_
- Die Listenbeschreibung wird jetzt angezeigt, wenn die Liste sortiert ist _(Mikhail Listratsenka)_
- Das Design des Einstellungsbildschirms für die Lesezeichenliste wurde aktualisiert _(Mikhail Listratsenka)_
- Der Suchbereich wird jetzt eingeklappt, nachdem du auf eine Kategorie getippt hast _(Mikhail Listratsenka)_
- Der Tastaturfokus springt jetzt wieder zum Suchfeld zurück, nachdem du es geleert hast _(Mikhail Listratsenka)_
- Das Höhenprofil der Route nutzt jetzt die gesamte Breite des Bereichs _(Mikhail Listratsenka)_
- Ein Problem wurde behoben, durch das die Zoom-Schaltflächen oben hängen bleiben konnten _(Mikhail Listratsenka)_
- Die Ecken der Dialogfelder sind jetzt auf allen Android-Versionen einheitlich abgerundet _(Mikhail Listratsenka)_
- Ein Absturz im Menü zum Exportieren von Tracks wurde behoben _(Mikhail Listratsenka)_
- Probleme behoben, bei denen die App einfror _(Alexander Borsuk, Viktor Govako)_
- Das Problem mit doppelten Importen von KML- und KMZ-Dateien sowie der Fehlermeldung „Datei konnte nicht geöffnet werden“ wurde behoben _(Alexander Borsuk)_
- Suchkategorien in brasilianischem Portugiesisch, mexikanischem Spanisch und britischem Englisch korrigiert _(Alexander Borsuk)_
- Die Suche funktioniert jetzt korrekt in der Tastatursprache, wenn diese von der Sprache der Benutzeroberfläche abweicht _(Alexander Borsuk)_
- OpenStreetMap-Bearbeitungen gehen nicht mehr verloren, wenn ein Upload zu lange dauert oder teilweise fehlschlägt _(Alexander Borsuk)_

### Desktop

- Auf der Ortsseite wurde eine „Share“-Aktion mit den Optionen „Copy Link“, „Copy Text“ und „Email…“ hinzugefügt _(Alexander Borsuk)_
- Der Download-Spinner wird jetzt programmgesteuert gezeichnet, sodass er auf jedem Display scharf dargestellt wird _(Kuzey Bilgin)_

## So unterstützt du Organic Maps

- [Spende](@/donate/index.de.md), um die Entwicklung zu unterstützen und die Kosten für das Hosting der Karten zu decken
- [Schick uns dein Feedback und trag zum Projekt bei](@/contribute/index.de.md)
- Mach beim Beta-Test mit, um neue Funktionen vorab zu testen und Probleme für [iOS][testflight], [Android][firebase] und [Desktop][flathub] zu melden
- Erzähl es weiter!

Mit Liebe und Dankbarkeit an alle unsere Nutzer und Mitwirkenden,<br/>
Das Organic Maps-Team

{{ <references lang /> }}
