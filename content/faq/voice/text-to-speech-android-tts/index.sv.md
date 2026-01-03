---
title: Text-till-tal på Android
description: Guide om hur du får TTS att fungera på Android
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
---

## Sammanfattning

Organic Maps använder systemets text-till-tal-motor (TTS) för röstinstruktioner. Standardmotorerna varierar beroende på enhet. Alternativen kan inkludera Google Text-to Speech, enhetstillverkarens motor eller en tredjepartsmotor.

Den officiella rekommendationen från Organic Maps är [RHVoice](https://rhvoice.org/), som är en gratis talmotor med öppen källkod som kan laddas ner från [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) och [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instruktioner

- Öppna appen Inställningar på din Android-enhet
- Välj Ytterligare inställningar och välj sedan Tillgänglighet
- Välj önskad motor, talhastighet och tonhöjd
- **Starta om appen Organic Maps**
- Öppna Inställningar => Röstinstruktioner i organiska kartor och ställ in det
- Starta om appen Organic Maps igen (eller starta om enheten) om rösten inte fungerar

Om du inte kan hitta den relevanta inställningen, öppna inställningsappen och sök efter Text-till-tal.

P.S: Observera att dessa steg kommer att variera beroende på vilket telefonmärke du använder.

Nämnda alternativ kanske inte visas om du inte redan har en TTS installerad på din enhet. Se tabellen nedan för att installera någon av dem som stöder ditt modersmål.

## Skärmdumpar

|             |             |
| ----------- | ----------- |
![Inställningar](tts_config_1.png "Inställningar") | ![Tillgänglighet](tts_config_2.png "Tillgänglighet")

## Motorer {#motorer}

Nedan finns en omfattande lista som visar flera motorer och de språk de stöder (nedladdningslänkar finns efter tabellen):

{{ tts_table() }}

## Lösningar

Om du har problem med att initiera RHVoice TTS-motorn på LineageOS eller andra anpassade ROM, prova den här lösningen. RHVoice kanske inte initieras ordentligt och appen kan krascha, särskilt om du inte har använt någon TTS-motor på din telefon tidigare (t.ex. nyinstallation, fabriksåterställning, etc.). Om du använder en anpassad ROM som LineageOS <ins>utan Google Play-tjänster och taltjänster från Google</ins> och du vill använda RHVoice som din föredragna TTS-motor, följ instruktionerna nedan som en lösning:

1. Installera [eSpeak TTS-motorn](https://f-droid.org/en/packages/com.reecedunn.espeak) tillgänglig på F-Droid
2. Ställ in den som den föredragna systemmotorn
    - Gå till LineageOS huvud **Inställningar**.
    - Scrolla ner till **Tillgänglighet**.
    - Välj **text-till-tal-utdata** och **Önskad motor** (vänster sida) och se till att **eSpeak** är valt.
3. Gå tillbaka och tryck på **spela** för att se om det fungerar
4. Installera [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) tillgängligt på F-droid.
    - Öppna den, välj det språk du vill använda, tryck på molnikonen (längst till vänster) för att ladda ner röster.
    - Tryck på play-knappen för att kontrollera om det fungerar
5. Ställ in **RHVoice** som önskad motor (se steg 2)
6. Nu bör du kunna använda RHVoice utan problem

## Testning

För att testa röstinstruktionerna kan du trycka på "Testa röstanvisningar (TTS, text-till-tal)" i OM-menyn "Inställningar → Röstinstruktioner" eller så kan du faktiskt starta en navigering för att ta emot röstutdata. Organiska kartor ger dig inga röstinstruktioner medan du står still.

![TTS-test](tts_test.png "TTS-test")
