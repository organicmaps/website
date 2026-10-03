---
title: "Ottimizzazione dei percorsi, percorsi alternativi migliorati, possibilità di nascondere le singole tracce e aree con acqua intermittente nell'aggiornamento di settembre 2026"
date: 2026-09-29
slug: "selezione-multipla-segnalibri-tracce-dashboard-carplay-nascondere-tracce-link-condivisione-agosto-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Si parte? L’aggiornamento di settembre introduce percorsi alternativi migliorati, un’impostazione per ottimizzare l’ordine delle tappe del percorso, indicazioni più chiare per le zone con presenza intermittente di acqua e un’icona a forma di occhio per nascondere singole tracce, oltre a tante altre correzioni e miglioramenti (vedi sotto).

Installa o aggiorna Organic Maps tramite <https://get.omaps.org>, l'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] o [F-Droid][fdroid].

Se ti sei perso i nostri aggiornamenti precedenti, dai un’occhiata alle funzionalità rilasciate a [giugno](@/news/2026-06-29/610/index.it.md), [luglio](@/news/2026-07-23/620/index.it.md) e [agosto](@/news/2026-08-31/630/index.it.md). Complimenti ai nostri collaboratori e agli utenti che hanno reso possibili questi aggiornamenti!

## Come sostenere Organic Maps

- [Fai una donazione](@/donate/index.it.md) per sostenere lo sviluppo e coprire i costi di hosting delle mappe
- [Invia i tuoi commenti e contribuisci](@/contribute/index.it.md) al progetto
- Partecipa al beta testing per provare in anteprima le nuove funzionalità e segnalare eventuali problemi su [iOS][testflight], [Android][firebase] e [desktop][flathub]
- Spargi la voce e aiutaci a creare un'alternativa migliore alle mappe delle Big Tech!

## Note di rilascio

### Mappa

- Dati di OpenStreetMap aggiornati al 28 settembre 2026
- Dati di Wikipedia aggiornati al 21 settembre 2026
- Risolto il problema delle ricerche quando l'area visibile della mappa attraversa il meridiano di 180° (longitudine ±180°) _(Viktor Govako)_
- Le aree con presenza intermittente di acqua vengono ora visualizzate con un motivo a puntini, simile a quello usato per la sabbia _(Alexander Borsuk)_
- I bacini idrici ora sono visibili anche riducendo ulteriormente lo zoom _(Alexander Borsuk)_
- I tunnel idrici non compaiono più sulla mappa _(Alexander Borsuk)_
- Corrette le icone delle stazioni e degli ingressi della metropolitana di Suzhou _(Alexander Borsuk)_
- Sono stati risolti alcuni rari casi in cui le etichette si spostavano fuori posizione sul livello della mappa della metropolitana _(Viktor Govako)_

### Percorsi e navigazione

- Migliorati i percorsi alternativi e i relativi orari di arrivo stimati _(Alexander Borsuk, Viktor Govako)_
- Il percorso alternativo selezionato ora viene mantenuto quando la navigazione ricalcola il percorso _(Alexander Borsuk)_
- L’ordine delle tappe del percorso viene ora ripristinato dopo il riavvio dell’app _(Kiryl Kaveryn)_

### Altri miglioramenti

- Gli orari di apertura ora indicano “Mezzogiorno” per le 12:00 e “Mezzanotte” per le 00:00 o le 24:00 _(Alexander Borsuk)_
- Sono stati corretti alcuni bug e migliorata la registrazione della traccia _(Alexander Borsuk)_
- Risolto il problema con l'importazione dei file KMB _(Alexander Borsuk)_
- Traduzioni corrette in francese e asturiano _(Alexander Borsuk)_
- Corretto un errore di battitura in inglese _(Carl Morris)_

### iOS

- Aggiunta un’icona a forma di occhio per nascondere le singole tracce _(Kiryl Kaveryn)_
- Aggiunti dei pulsanti per aggiungere o sostituire una tappa in un percorso pianificato _(Kiryl Kaveryn)_
- Aggiunta un’impostazione per ottimizzare l’ordine delle tappe intermedie del percorso _(Kiryl Kaveryn)_
- Aggiunte istruzioni di manovra ai display head-up (HUD) delle auto compatibili e alla dashboard di CarPlay _(Kiryl Kaveryn)_
- Corretti i pulsanti e la ricerca di CarPlay _(Alexander Borsuk)_
- Abbiamo risolto vari bug e migliorato l'interfaccia utente _(Kiryl Kaveryn, Alexander Borsuk)_
- Aggiunto il supporto per scegliere e ascoltare in anteprima una voce di navigazione già installata _(Kiryl Kaveryn, Alexander Borsuk)_
- Ripristinata la ricerca per categoria in Spotlight _(Kiryl Kaveryn)_

### Android

- Aggiunta un’impostazione per ottimizzare l’ordine delle tappe intermedie del percorso _(Mikhail Listratsenka)_
- Aggiunti dei pulsanti per aggiungere o sostituire una tappa in un percorso pianificato _(Mikhail Listratsenka)_
- È stata aggiunta la possibilità di interrompere la registrazione della traccia e salvarla direttamente dalla notifica _(Alexander Borsuk)_
- Il pulsante “Aggiungi sosta” ora aggiunge una tappa dopo quelle già presenti, prima della destinazione _(Mikhail Listratsenka)_
- Miglioramenti al caricamento dei dati dall'editor di OpenStreetMap _(Owm)_
- Abbiamo aggiornato il design dell'interfaccia utente _(Mikhail Listratsenka)_
- L'editor dei segnalibri e le altre finestre di dialogo ora rimangono aperte durante la navigazione _(Mikhail Listratsenka)_
- Risolto il problema di visualizzazione del grafico di altitudine per le tracce pianeggianti e nelle interfacce con orientamento da destra a sinistra _(Mikhail Listratsenka)_
- Risolto il problema dei pulsanti della mappa che venivano troncati dalle barre di sistema _(Mikhail Listratsenka)_
- Sono stati corretti alcuni bug e migliorato il supporto per Android Auto _(Andrei Shkrob)_
- Risolto un crash durante il rendering della mappa _(Viktor Govako)_

### Desktop

- L’eseguibile per desktop e il pacchetto dell’app per macOS sono stati rinominati in `OrganicMaps` _(Alexander Borsuk)_
- Sono stati risolti alcuni problemi nell'app per Windows _(Osyotr, Alexander Borsuk)_
- L’argomento della riga di comando `--lang` ora ha la precedenza sull’impostazione della lingua dell’app _(Alexander Borsuk)_

Con gioia e passione,

Il tuo team di Organic Maps

{{ <references lang /> }}
