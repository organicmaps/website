---
title: Wie kann ich eine erweiterte Kartenbearbeitung durchführen?
slug: wie-kann-ich-eine-erweiterte-kartenbearbeitung-durchführen
description: Tutorial zum Bearbeiten von OpenStreetMap mit fortgeschritteneren Tools
  wie ID, Go Map und Vespucci
updated: '2024-06-20'
taxonomies:
  faq: ["Kartenbearbeitung"]
extra:
  order: 40
aliases:
  - /de/faq/editing/advanced-map-editing/
---

Organic Maps enthält einen einfachen und benutzerfreundlichen Editor, mit dem Sie die Karte bearbeiten können. Der Editor ist jedoch eingeschränkt und erlaubt nur das Hinzufügen einfacher Punktmerkmale, also keine Gebäudeumrisse, Straßen, Seen, Städte usw. Wenn Sie etwas ändern möchten, das mit dem eingebauten Editor nicht bearbeitet werden kann, ist dies die richtige FAQ-Seite zum Lesen.

Da alle in Organic Maps verwendeten Kartendaten von [OpenStreetMap.org (OSM)](https://www.openstreetmap.org) stammen, können Sie die Karte direkt dort aktualisieren. Ihre Änderungen werden dann mit dem nächsten Kartenupdate in Organic Maps übernommen.

## OpenStreetMap-Editoren

Für die Bearbeitung von OSM gibt es mehrere Möglichkeiten. Wenn Sie einen Laptop oder Desktop-Computer zur Hand haben, verwenden Sie besser den [ID-Editor](https://www.openstreetmap.org/edit), der in Ihrem Browser ausgeführt wird. Der ID-Editor ist für Anfänger einfach zu bedienen und ein größerer Bildschirm, eine größere Maus und eine größere Tastatur erleichtern die Kartenbearbeitung.

Für die erweiterte Kartenbearbeitung von einem Mobilgerät aus verwenden Sie [Go Map](https://apps.apple.com/us/app/go-map/id592990211) für iOS oder [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) für Android. Go Map ist für Anfänger einfach, während Vespucci sich an fortgeschrittenere Benutzer richtet. LearnOSM bietet Tutorials für [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) und [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Für einfachere Bearbeitungen mit mehr Spaß können Sie auch die [Every Door-App](https://every-door.app/) für iOS und Android und die [StreetComplete-App](https://streetcomplete.app/) für Android ausprobieren.

#### ID-Editor

Um OpenStreetMap mit ID zu bearbeiten, gehen Sie folgendermaßen vor:

1. Erstellen Sie ein neues Konto oder melden Sie sich bei [OpenStreetMap.org](https://www.openstreetmap.org) an.
2. Navigieren Sie zu dem Ort, den Sie auf OpenStreetMap.org bearbeiten möchten, und klicken Sie oben auf *Bearbeiten*
3. *Starten Sie die Komplettlösung* und folgen Sie dem kurzen Tutorial, das den ID-Editor erklärt
4. Bearbeiten Sie die Karte
5. Laden Sie Ihre Änderungen hoch

Das war's, Sie sind jetzt Teil der OSM-Community.

## Was passiert mit meinen Änderungen?

Sobald Sie auf *Hochladen* klicken, werden Ihre Änderungen sofort zur öffentlichen OSM-Datenbank hinzugefügt. Seien Sie also bei der Bearbeitung rücksichtsvoll. In organischen Karten werden Ihre Änderungen nach dem nächsten monatlichen Kartenupdate sichtbar.

Ihre E-Mail wird nicht veröffentlicht, aber andere Personen können Ihren OSM-Benutzernamen sehen. Da OSM die Möglichkeit bietet, Änderungen zu diskutieren, erhalten Sie möglicherweise Fragen zu Ihren Änderungen von anderen OSM-Mitwirkenden. Sie werden hierüber über die E-Mail-Adresse benachrichtigt, die Sie für die Registrierung Ihres OSM-Kontos verwendet haben. Da OSM ein Community-Projekt ist, das auf Zusammenarbeit aufbaut, sollten Sie solche Fragen immer beantworten.

## Community und Wiki

OpenStreetMap ist eine Community. Wenn Sie Hilfe benötigen oder Fragen haben, können Sie diese im [OSM-Forum](https://community.openstreetmap.org/c/help-and-support) stellen oder einen Blick in die Dokumentation des [OSM-Wikis](https://wiki.openstreetmap.org/) werfen.

## Tags – Wie das OSM-Datenmodell funktioniert

Die OpenStreetMap-Datenbank enthält Objekte wie Knoten, Wege, Flächen und Beziehungen, die von realen Merkmalen abstrahieren. Diese Objekte verfügen über Attribute, sogenannte Tags, um sie näher zu beschreiben. Ein Tag ist eine Schlüssel-Wert-Kombination.

Da dies komplizierter klingt als es ist, geben wir ein Beispiel:
Ein Restaurant ist z.B. als Notiz oder Bereich mit dem Tag „amenity=restaurant“ zugeordnet. Weitere Tags wie „cousine=*“ oder „opening_hours=*“ können dann für weitere Details verwendet werden.

> Beachten Sie, dass der ID-Editor die interne Datenstruktur vor den Benutzern verbirgt, um die Benutzerfreundlichkeit zu erhöhen. Aber zum Lesen der Wiki-Dokumentation ist ein kurzer Überblick über die Datenstruktur hilfreich.
Im ID-Editor können Sie die Tags sehen, die die ID vor Ihnen verbirgt, indem Sie den Abschnitt *Tags* im Seitenbereich *Funktion bearbeiten* erweitern.

## OSM-Notizen {#osm-note}

Wenn Sie keine Zeit haben oder das Problem zu kompliziert ist, um die OSM-Daten selbst zu bearbeiten, sind OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) die richtige Wahl. Sie können einen solchen Hinweis an der Stelle des Kartenfehlers platzieren und das Problem detailliert beschreiben. Andere OSM-Freiwillige können dann helfen und das Problem lösen. Sie erhalten über Ihr OSM-Konto E-Mail-Benachrichtigungen, falls weitere Fragen bestehen oder der OSM-Hinweis gelöst ist.

1. Erstellen Sie ein neues Konto oder melden Sie sich bei [OpenStreetMap.org](https://www.openstreetmap.org) an.
   > Sie können auch anonyme Notizen öffnen. Dies wird jedoch nicht empfohlen, da Sie nicht benachrichtigt werden, wenn das Problem gelöst ist oder weitere Fragen bestehen.
2. Zoomen Sie auf den Kartenstandort auf [OpenStreetMap.org](https://www.openstreetmap.org) und drücken Sie *Notiz zur Karte hinzufügen* (zweites Symbol von unten im rechten Menü). Ziehen Sie dann die blaue Kartenmarkierung an die genaue Position.
   > Versuchen Sie, so präzise wie möglich zu sein.
3. Geben Sie eine detaillierte Beschreibung des Kartenproblems ein und klicken Sie auf *Notiz hinzufügen*
   > Für Geschäfte z.B. Geben Sie den Namen an und erwähnen Sie, was dort verkauft oder welche Dienstleistungen angeboten werden.
