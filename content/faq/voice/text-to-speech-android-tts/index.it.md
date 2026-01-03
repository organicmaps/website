---
title: Sintesi vocale (Text-to-speech, TTS) su Android
description: Guida su come far funzionare la sintesi vocale su Android
slug: sintesi-vocale-tts-su-android
aliases:
  - /it/faq/voice/text-to-speech-android-tts/
taxonomies:
  faq: ["Indicazioni vocali"]
extra:
  order: 10
---

## Sommario

Organic Maps utilizza il motore di sintesi vocale (Text-to-speech o semplicemente TTS) del sistema per le indicazioni vocali. I motori di sintesi vocale predefiniti variano a seconda del dispositivo. La scelta può includere Sintesi vocali di Google, il motore del produttore del dispositivo o un motore di terze parti.

La raccomandazione ufficiale di Organic Maps è [RHVoice](https://rhvoice.org/), un motore vocale gratuito ed open source che può essere scaricato da [Google Play Store](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) e [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Istruzioni

- Aprire l'applicazione Impostazioni sul dispositivo Android
- Selezionare Impostazioni aggiuntive, quindi selezionare Accessibilità
- Scegliere il motore di sintesi vocale, la velocità ed il tono di voce preferiti
- **Riavviare l'applicazione Organic Maps**
- Aprire Impostazioni => Istruzioni vocali in Organic Maps e impostarle
- Riavviare di nuovo l'app Organic Maps (o riavviare il dispositivo) se la voce non funziona

Se non si riesce a trovare l'impostazione pertinente, aprire l'app Impostazioni e cercare Assistenza vocale.

N.B.: Tenete presente che questi passaggi variano a seconda della marca del telefono che state utilizzando.

Le suddette opzioni potrebbero non essere presenti se sul dispositivo non è già installato un software di sintesi vocale. Fare riferimento alla tabella seguente per installare uno dei motori TTS che supporta la propria lingua madre.

## Schermate

|             |             |
| ----------- | ----------- |
![Impostazioni](tts_config_1.png "Impostazioni") | ![Accessibilità](tts_config_2.png "Accessibilità")

## Motori di sintesi vocale TTS {#engines}

Di seguito è riportato un elenco completo di diversi motori di sintesi vocale e delle lingue supportate (i link per il download si trovano dopo la tabella):

{{ tts_table() }}

## Risoluzione dei problemi

Se hai problemi ad inizializzare il motore TTS di RHVoice su LineageOS o altre ROM personalizzate, prova questa soluzione. RHVoice potrebbe non inizializzarsi correttamente e l'applicazione potrebbe bloccarsi, soprattutto se non è mai stato usato un motore TTS sul telefono (ad esempio, in caso di nuova installazione, reset di fabbrica, ecc.). Se si utilizza una ROM personalizzata come ad es. LineageOS <ins>senza i servizi Google Play e Speech Services by Google</ins>, e si desidera utilizzare RHVoice come motore TTS preferito, seguire le istruzioni riportate di seguito come soluzione alternativa:

1. Installare il motore [eSpeak TTS] (https://f-droid.org/en/packages/com.reecedunn.espeak) disponibile su F-Droid.
2. Impostarlo come motore TTS di sistema preferito
    - Aprire le **Impostazioni** principali di LineageOS.
    - Scorrere fino a **Accessibilità**.
    - Selezionare **Output sintesi vocale** e **Motore preferito** (lato sinistro) e assicurarsi che sia selezionato **eSpeak**.
3. Tornare indietro e premere **lay** per verificarne il funzionamento.
4. Installare [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) disponibile su F-droid.
    - Aprirlo, selezionare la lingua che si desidera utilizzare e toccare l'icona della nuvola (all'estrema sinistra) per scaricare le voci desiderate.
    - Premere il pulsante play per verificarne il funzionamento.
5. Impostare **RHVoice** come motore di sintesi vocale preferito (vedi punto 2).
6. A questo punto si dovrebbe essere in grado di utilizzare RHVoice senza problemi.

## Test delle indicazioni vocali

Per testare le indicazioni vocali, è possibile toccare in Organic Maps su "Prova indicazioni vocali (TTS, Text-to-speech)" nel menu "Impostazioni" → sotto "Navigazione" → "Istruzioni vocali" oppure semplicemente avviare una navigazione per ricevere le indicazioni vocali. Organic Maps non fornisce indicazioni vocali quando si è in sosta.

![TTS Test](tts_test.png "TTS Test")
