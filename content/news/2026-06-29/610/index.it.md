---
title: "Immagini satellitari, percorsi con i mezzi pubblici, percorsi alternativi, nuova interfaccia di ricerca e pianificazione percorsi per Android, supporto ai caratteri grandi per l’accessibilità su iOS e altro nell’aggiornamento di giugno 2026"
date: 2026-06-29
slug: "immagini-satellitari-percorsi-mezzi-pubblici-percorsi-alternativi-nuova-ricerca-pianificazione-android-caratteri-grandi-ios-giugno-2026"
taxonomies:
  news: ["releases"]
---

Nell’aggiornamento di giugno di Organic Maps ci sono tante nuove funzioni interessanti e correzioni di bug da provare, tra cui:
- Immagini satellitari
- Percorsi con i mezzi pubblici
- Percorsi alternativi
- Nuova interfaccia di ricerca e pianificazione percorsi per Android
- Supporto ai caratteri grandi per l’accessibilità su iOS

Scaricalo da <https://get.omaps.org> oppure da [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid], e facci sapere che ne pensi!

## Registro delle modifiche dettagliato

- NUOVO! Pianificazione dei percorsi con i mezzi pubblici: metropolitana, metro leggera, autobus e tram _(Viktor Govako)_
- NUOVO! Percorsi alternativi: oltre al percorso più veloce, l’app ora mostra anche il percorso più breve _(Viktor Govako)_
- NUOVO! Avvisi per percorsi a piedi e in bicicletta su gradini, cancelli e barriere lungo il tragitto _(Viktor Govako)_
- NUOVO! Scegli qualsiasi colore per i segnalibri _(Alexander Borsuk, Mikhail Listratsenka)_
- NUOVO! Supporto alle coordinate British National Grid (OS Grid), Irish Grid e Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- SPERIMENTALE: abilita le immagini satellitari nelle impostazioni di Organic Maps usando l’URL personalizzato di un server di tile raster. Stiamo ancora lavorando al nostro server, quindi trova un server pubblico che abbia i segnaposto `{x}`, `{y}`, `{z}` nell’URL _(Viktor Govako, renderexpert)_
- Dati OpenStreetMap aggiornati al 24 giugno _(Viktor Govako)_
- Dati Wikipedia aggiornati al 20 giugno, inclusi articoli in italiano _(Alexander Borsuk)_
- Digita `?map-download-server:https://your-server.com/` nella finestra di ricerca per sostituire i server di download delle mappe di Organic Maps. Digita `?no-map-download-server` per rimuovere la sostituzione _(Alexander Borsuk)_

#### Rendering e stili della mappa

- Motivi più belli per aree di spiaggia, sabbia, ghiaione, roccia nuda, frutteti e vigneti, oltre ai tratteggi per aree protette e zone umide _(Alexander Borsuk)_
- Etichette di testo curve più fluide per strade e fiumi _(Viktor Govako)_
- Fiumi, torrenti e zone umide hanno più contrasto e sono più visibili in modalità scura _(Alexander Borsuk)_
- Icone nuove e migliorate per la ricerca per categoria e i risultati di ricerca sulla mappa _(Anton Makouski)_
- Migliorata la composizione e la resa del testo multilingue _(Alexander Borsuk)_
- Varie correzioni di errori e miglioramenti delle prestazioni _(Viktor Govako)_

#### Tracce, segnalibri e percorsi

- Le tracce GeoJSON ora mantengono quota e timestamp durante importazione ed esportazione _(Alexander Borsuk)_
- Corretto un arresto anomalo dopo lo spostamento di una traccia in un altro elenco _(Viktor Govako)_
- Ora vengono mostrati i siti web per i luoghi di interesse storico-culturale _(Viktor Govako)_
- Ora vengono mostrati i nomi degli operatori per i risultati di ricerca senza nome. Per esempio, un bancomat senza nome ora mostra la sua banca _(Anton Makouski)_
- Editor: corretto il testo descrittivo per modifiche/changeset OpenStreetMap di condomini _(titanniya542-spec)_
- Migliorato il rilevamento dell’HTML nelle descrizioni di segnalibri e tracce _(Alexander Borsuk)_

### iOS

- NUOVO! Supporto all’accessibilità per Dynamic Type e caratteri grandi _(Kiryl Kaveryn)_
- NUOVO! Tocca per scegliere tra tracce e percorsi sovrapposti _(Kiryl Kaveryn)_
- Migliorata la resa HTML delle descrizioni di segnalibri e tracce _(Kiryl Kaveryn)_
- Stile delle tabelle più pulito nell’interfaccia _(Kiryl Kaveryn)_

### Android

- NUOVO! Interfaccia di ricerca _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NUOVO! Interfaccia di pianificazione dei percorsi _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Migliorata la resa HTML delle descrizioni di segnalibri e tracce _(Mikhail Listratsenka)_
- Dimensione dell’APK ridotta _(Alexander Borsuk)_
- L’icona della voce è mostrata come disattivata quando non è disponibile alcun motore di sintesi vocale _(Mikhail Listratsenka)_
- Le descrizioni lunghe di segnalibri e tracce ora mostrano un pulsante «…altro» _(Mikhail Listratsenka)_
- Varie correzioni dell’interfaccia e una correzione API per gli ID dei punti restituiti _(Mikhail Listratsenka)_

### Desktop

- Supporto al cambio del sistema di coordinate visualizzato _(Alexander Borsuk)_
- Le informazioni sul luogo selezionato ora sono visualizzate a sinistra _(Viktor Govako)_
- Corretta la posizione del menu contestuale _(Osyotr)_
- Corretto il blocco del login e delle modifiche OpenStreetMap su Qt 6.4 e versioni precedenti _(Alexander Borsuk)_
- Corretto un cambio imprevisto dello stile della mappa durante la navigazione su macOS _(Alexander Borsuk)_
- Corretto un arresto anomalo alla chiusura dell’app macOS dopo l’esportazione di un file KMZ _(Alexander Borsuk)_

### Traduzioni

- Indicazioni vocali passo-passo in cantonese _(Alexander Borsuk)_
- Traduzioni tedesche e francesi aggiornate _(Wuzzy, Alexander Borsuk)_
- Corrette traduzioni vocali errate di «onto street» per cinese, serbo e catalano _(Alexander Borsuk)_

## Partecipa ai test beta per provare le funzioni in anticipo e segnalare problemi:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Siamo grati a tutti i nostri utenti e collaboratori, a chi [dona](@/donate/index.it.md) e dà 5 stelle a Organic Maps negli store. Insieme possiamo creare la migliore app di mappe!

Con affetto,
Organic Maps Team

{{ references() }}
