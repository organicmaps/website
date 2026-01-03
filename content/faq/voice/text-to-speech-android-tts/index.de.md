---
title: Text-to-Speech auf Android
slug: text-to-speech-auf-android
description: Anleitung zur Einrichtung von TTS-Sprachanweisungen auf Android
taxonomies:
  faq: ["Sprachführung"]
extra:
  order: 10
aliases:
  - /de/faq/voice/text-to-speech-android-tts/
---

## Zusammenfassung

Organic Maps nutzt die TTS-Engine (Text-to-Speech) des Systems für Sprachanweisungen. Die Standard-Engines variieren je nach Gerät. Zur Auswahl stehen Google Text-to-Speech, die Engine des Geräteherstellers oder die Engine eines Drittanbieters.

Die offizielle Empfehlung von Organic Maps ist [RHVoice](https://rhvoice.org/), eine kostenlose Open-Source-Sprach-Engine, die von [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) heruntergeladen werden kann [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Anleitung

- Öffnen Sie die Einstellungen-App auf Ihrem Android-Gerät
- Wählen Sie „Zusätzliche Einstellungen“ und dann „Barrierefreiheit“.
- Wählen Sie Ihre bevorzugte Engine, Sprechgeschwindigkeit und Tonhöhe
- **Organische Karten-App neu starten**
- Öffnen Sie Einstellungen => Sprachanweisungen in Organic Maps und richten Sie es ein
- Starten Sie die Organic Maps-App erneut (oder starten Sie das Gerät neu), wenn die Stimme nicht funktioniert

Wenn Sie die entsprechende Einstellung nicht finden können, öffnen Sie die Einstellungs-App und suchen Sie nach Text-to-Speech.

P.S.: Beachten Sie, dass diese Schritte je nach der von Ihnen verwendeten Telefonmarke variieren können.

Diese Optionen werden möglicherweise nicht angezeigt, wenn auf Ihrem Gerät noch kein TTS installiert ist. Bitte beachten Sie die Tabelle unten, um eines davon zu installieren, das Ihre Muttersprache unterstützt.

## Screenshots

|             |             |
| ----------- | ----------- |
![Einstellungen](tts_config_1.png "Einstellungen") | ![Barrierefreiheit](tts_config_2.png "Barrierefreiheit")

## Engines {#engines}

Nachfolgend finden Sie eine umfassende Liste mit mehreren Engines und den von ihnen unterstützten Sprachen (Download-Links finden Sie nach der Tabelle):

{{ tts_table() }}

## Problemumgehungen

Wenn Sie Probleme beim Initialisieren der RHVoice TTS-Engine unter LineageOS oder anderen benutzerdefinierten ROMs haben, versuchen Sie diese Problemumgehung. RHVoice wird möglicherweise nicht ordnungsgemäß initialisiert und die App kann abstürzen, insbesondere wenn Sie zuvor noch keine TTS-Engine auf Ihrem Telefon verwendet haben (z. B. Neuinstallation, Zurücksetzen auf Werkseinstellungen usw.). Wenn Sie ein benutzerdefiniertes ROM wie LineageOS <ins>ohne Google Play-Dienste und Sprachdienste von Google</ins> verwenden und RHVoice als Ihre bevorzugte TTS-Engine verwenden möchten, befolgen Sie als Workaround die folgenden Anweisungen:

1. Installieren Sie die [eSpeak TTS-Engine](https://f-droid.org/en/packages/com.reecedunn.espeak), die auf F-Droid verfügbar ist
2. Legen Sie es als bevorzugte System-Engine fest
    - Gehen Sie zu den LineageOS-Haupteinstellungen**.
    - Scrollen Sie nach unten zu **Barrierefreiheit**.
    - Wählen Sie **Text-to-Speech-Ausgabe** und **Bevorzugte Engine** (linke Seite) und stellen Sie sicher, dass **eSpeak** ausgewählt ist.
3. Gehen Sie zurück und drücken Sie **Play**, um zu sehen, ob es funktioniert
4. Installieren Sie [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/), verfügbar auf F-droid.
    - Öffnen Sie es, wählen Sie die Sprache aus, die Sie verwenden möchten, und tippen Sie auf das Cloud-Symbol (ganz links), um Stimmen herunterzuladen.
    - Drücken Sie die Wiedergabetaste, um zu überprüfen, ob es funktioniert
5. **RHVoice** als bevorzugte Engine festlegen (siehe Schritt 2)
6. Jetzt sollten Sie RHVoice problemlos nutzen können

## Testen

Um die Sprachanweisungen zu testen, können Sie im OM-Menü „Einstellungen → Sprachanweisungen“ auf „Sprachanweisungen testen (TTS, Text-To-Speech)“ tippen oder tatsächlich eine Navigation starten, um eine beliebige Sprachausgabe zu erhalten. Organic Maps gibt Ihnen im Stillstand keine Sprachanweisungen.

![TTS-Test](tts_test.png "TTS-Test")
