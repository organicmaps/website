---
title: "Versione 15 settembre: nuova pianificazione percorso e descrizioni OSM"
date: 2025-09-15T10:00:00+00:00
---

Questa seconda versione di settembre introduce una schermata di pianificazione dei percorsi ridisegnata e la possibilità di visualizzare il contenuto del tag OpenStreetMap `description` su iOS. Per trovare i luoghi con questo tag, digita `?description` nella ricerca (simile a `?wiki`).

Include anche molte correzioni e miglioramenti per iOS e Android (dettagli sotto).

Funzionalità recenti che potresti aver perso:
- Numeri delle linee del trasporto pubblico selezionando una fermata
- Percorsi escursionistici e ciclabili (attivali con il pulsante Livelli in alto a sinistra)
- Mostra i nomi dei segnaposto sulla mappa (attiva nelle Impostazioni)
- L’icona ✎ consente di modificare rapidamente i segnaposto

Organic Maps è possibile grazie ai nostri contributori, [alle tue donazioni](@/donate/index.it.md) e [al tuo supporto](@/contribute/index.md).

### Note di rilascio dettagliate

- Nuovi dati OpenStreetMap al 13 settembre
- Rimosse piccolissime isole dalla mappa mondiale (Viktor Govako)
- Mostra CAP (ZIP) nei dettagli dell’indirizzo (Viktor Govako)
- Corretto centraggio errato della mappa sulla posizione attuale (Kiryl Kaveryn, Viktor Govako)
- Conserva i colori dei segnaposto durante export/import GPX (cyber-toad)
- Traduzioni aggiornate (contributor Weblate)

#### Stili mappa (Viktor Govako)

- Mostra negozi di illuminazione
- Mostra linee elettriche dallo zoom 18
- Mostra riferimenti di centrali e sottostazioni elettriche
- Mostra campeggi e aree caravan in modalità navigazione
- Correggi colore strade secondarie in modalità navigazione
- Disegna confini dei parchi nazionali
- Disegna siti archeologici dallo zoom 12 nello stile Outdoor

#### iOS

- NUOVO: mostra contenuto del tag OSM `description` (cerca `?description`) (Kiryl Kaveryn, Viktor Govako)
- NUOVO: schermata di pianificazione percorso ridisegnata (Kiryl Kaveryn)

#### Android

- Nuove icone rotatorie in Android Auto (Andrei Shkrob)
- Mostra categoria del segnaposto selezionato (Alexander Borsuk)
- Corretto ritardo nel mostrare distanza a un segnaposto (Alexander Borsuk)
- Tema scuro ristrutturato (Andrei Shkrob)
- Corretto aggiornamento posizione in navigazione su ROM personalizzate (es. Lineage + MicroG) (Viktor Govako)
- Icona matita blu (modifica) per segnaposti (Alexander Borsuk)
- Ridotta altezza verticale anteprima informazioni luogo (Alexander Borsuk)
- Rimosso angolo dell’azimut verso nord dall’anteprima (tocca la freccia blu con distanza per vederlo) (Alexander Borsuk)

Scarica l’ultima versione: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Partecipa alla beta: [iOS][testflight] / [Android][firebase].

{{ references() }}
