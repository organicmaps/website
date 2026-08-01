---
title: "Correzioni di bug e miglioramenti relativi al trasporto pubblico, al calcolo dei percorsi, alla ricerca e ai segnalibri nell'aggiornamento di luglio 2026"
date: 2026-07-23
slug: "correzioni-bug-miglioramenti-trasporto-pubblico-percorsi-ricerca-segnalibri-luglio-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Come avrà forse già notato, è disponibile l'aggiornamento di luglio di Organic Maps. Può scaricarlo all'indirizzo <https://get.omaps.org> oppure su [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

Grazie alle sue [donazioni](@/donate/index.it.md) e ai suoi [commenti](@/contribute/index.it.md), nel mese di luglio ci siamo concentrati sulla correzione di bug e su alcuni miglioramenti. Nel caso se lo fosse perso, sono disponibili anche le seguenti funzionalità della [precedente versione di giugno](@/news/2026-06-29/610/index.it.md):
- Percorsi con i mezzi pubblici (gli orari in tempo reale sono in fase di sviluppo)
- Immagini satellitari
- Percorsi alternativi per auto, escursioni a piedi e in bicicletta
- Nuova interfaccia di ricerca e pianificazione del percorso per Android
- Supporto per i caratteri di grandi dimensioni per l'accessibilità su iOS

## Registro delle modifiche dettagliato

### Mappa e luoghi
- Dati OpenStreetMap aggiornati al 14 luglio
- Le note segnalate a [OpenStreetMap](https://www.openstreetmap.org) vengono ora posizionate nel punto esatto che ha selezionato, anziché al centro dell'intera strada o area _(Alexander Borsuk)_
- Miglioramento della selezione dei luoghi quando si tocca la mappa in regioni che attraversano l'antimeridiano di 180° _(Viktor Govako)_
- I profili altimetrici delle tracce non mostrano più grafici obsoleti o vuoti dopo l'eliminazione di una traccia _(Kiryl Kaveryn)_

### Trasporto pubblico
- I nomi delle fermate, degli interscambi e delle stazioni sono ora contornati da una linea bianca per garantire la leggibilità sia con il tema chiaro che con quello scuro _(Viktor Govako)_
- Il livello della metropolitana ricompare correttamente dopo aver chiuso l'anteprima di un percorso con i mezzi pubblici _(Mikhail Listratsenka)_

### Percorsi e navigazione
- Gli avvisi relativi al percorso (pedaggi, traghetti, strade non asfaltate, gradini e così via) vengono ora visualizzati per tutti i percorsi alternativi _(Viktor Govako)_
- Risolto un raro blocco del sistema durante la creazione di un percorso _(Viktor Govako)_
- Miglioramento della gestione dei vicoli ciechi e dei punti di inizio e fine sulle strade soggette a limitazioni _(Viktor Govako)_
- Corrette le indicazioni di svolta errate e mancanti _(Alexander Borsuk)_

### iOS
- Nuova impostazione «Salva cronologia ricerche» che le consente di disattivare la cronologia e nasconderla se preferisce non conservarla _(Kiryl Kaveryn)_
- Nuovo pulsante «Modifica» per rimuovere più facilmente i segnalibri _(Kiryl Kaveryn)_
- I segnalibri vengono ora salvati automaticamente quando esce dalla schermata _(Kiryl Kaveryn)_
- La tavolozza dei colori offre ora colori predefiniti e le consente di scegliere qualsiasi colore personalizzato _(Kiryl Kaveryn)_
- Miglioramento dello stato vuoto del grafico di altitudine per una traccia registrata _(Kiryl Kaveryn)_
- È stata migliorata la visualizzazione dell'avanzamento del percorso sul pulsante «Avvia» _(Kiryl Kaveryn)_
- Il riordino delle fermate del percorso non provoca più salti nell'elenco _(Kiryl Kaveryn)_
- Altri miglioramenti minori all'interfaccia _(Kiryl Kaveryn)_

### Android
- Gli orari di apertura ora mostrano i turni spezzati (come la pausa pranzo), iniziano da oggi e visualizzano l'intera settimana senza un'area di scorrimento separata _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Una barra di ricerca più pulita, con un pulsante combinato per la cancellazione e il comando vocale, un'icona di cancellazione che non si sposta più e correzioni del layout per la modalità orizzontale e la rotazione del telefono _(Mikhail Listratsenka)_
- Editor dei segnalibri e delle tracce rinnovato _(Mikhail Listratsenka)_
- Correzioni e miglioramenti alla pianificazione del percorso _(Mikhail Listratsenka)_
- Il selettore di colori ora si chiude automaticamente ed è stato risolto un errore che causava il crash su Android 5 _(Mikhail Listratsenka)_
- Risolti alcuni crash _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- L'elenco delle mappe disponibili per il download è ora ordinato in ordine alfabetico _(goncalo109560)_

### Traduzioni
- Formulazione in cinese migliorata _(Chenxi Zhao)_
- Traduzioni in ucraino aggiornate _(Nnifria)_
- Corrette le traduzioni in italiano dei nomi delle regioni delle mappe _(Vittorio Bertola)_

## Partecipi ai test beta per provare le funzioni in anticipo e segnalare problemi:

Suggerimento: la versione beta presenta una nuova tecnica di ombreggiatura del rilievo, dati altimetrici migliorati con supporto per i piedi e i metri e altre fantastiche funzionalità!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Buona estate!
Organic Maps Team

{{ references() }}
