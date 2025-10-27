---
title: "Rilascio di ottobre: Limiti di velocità su Android Auto, importazione GeoJSON, statistiche di registrazione traccia, visualizzazione tag descrizione OSM, salvataggio segnalibro sulla traccia selezionata su iOS e altro ancora"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

Questo aggiornamento di ottobre di Organic Maps aggiunge la visualizzazione del limite di velocità in Android Auto, l'importazione di GeoJSON, le statistiche di registrazione traccia, mostra i tag di descrizione OSM (digita `?description` nella casella di ricerca per vederli) e salva un segnalibro su una traccia su iOS. Ci sono anche molti miglioramenti all'interfaccia utente, alla modifica di OpenStreetMap e varie correzioni di bug su tutte le piattaforme, inclusa la correzione del crash all'avvio su alcuni dispositivi Android.

Organic Maps è possibile grazie ❤️ ai nostri contributori, [le vostre donazioni](@/donate/index.it.md) e [il vostro supporto](@/contribute/index.it.md).

### Note di rilascio dettagliate (incluse le modifiche dell'aggiornamento minore precedente)

- NUOVO! Importazione GeoJSON (Sergiy Kozyr)
- Dati OpenStreetMap al 4 ottobre
- Dati Wikipedia al 1° ottobre
- Supporto della metropolitana leggera di Seattle per i trasporti pubblici (tjasz)
- Non disattivare la selezione della mappa quando si salva un luogo OSM modificato (Kiryl Kaveryn)
- Traduzioni aggiornate (contributori Weblate)

#### Stili mappa

- Mostra negozi di noleggio biciclette taggati come amenity=bicycle + rental=shop (David Martinez)
- Mostra siti archeologici storici dallo zoom 12 e altri siti storici dallo zoom 15 nello stile Esterni (Viktor Govako)
- Nuove icone per pali, comunicazioni e torri elettriche nello stile Esterni (David Martinez)
- Aumenta la dimensione dell'icona della vetta nello stile Esterni (David Martinez)
- Aggiungi varianti di icone POI mancanti (David Martinez)
- Aggiunti più tipi di barriere (Viktor Govako)

#### iOS

- NUOVO: Salva segnalibro sul punto traccia selezionato (Kiryl Kaveryn)
- NUOVO: Elimina la traccia di registrazione senza salvarla prima (Kiryl Kaveryn)
- Mostra titoli elenco segnalibri multi-linea nella Pagina del luogo (David Martinez)
- Aggiorna lo stile dei pulsanti di accesso OSM (Kiryl Kaveryn)
- Correggi problema di aggiornamento informazioni di navigazione (Kiryl Kaveryn)
- Correggi problemi di pianificazione nuovo percorso (Kiryl Kaveryn)
- Correggi visibilità aggiunta/modifica luogo OSM per mappe più vecchie di 3 mesi (Kiryl Kaveryn)
- Correggi layout controllo segmento opzioni trasporto per iOS 26 (Kiryl Kaveryn)
- Semplifica animazioni di selezione segnalibri (Kiryl Kaveryn)
- Correggi problema di selezione risultato ricerca (Kiryl Kaveryn)
- Stile, scorrimento e animazioni corretti per la Pagina informazioni luogo (Kiryl Kaveryn)

#### Android Auto (solo Google Play)

- NUOVO: Visualizzazione limite di velocità in Android Auto (Andrei Shkrob)
- Correggi cambio display in modalità navigazione Android Auto (Andrei Shkrob)
- Correggi offset freccia percorso in Android Auto (Andrei Shkrob)
- Correggi problema quando un dispositivo viene connesso/disconnesso a un'auto (Andrei Shkrob)
- Aggiungi servizio di localizzazione Android Auto (Andrei Shkrob)
- Migliora simulatore percorso Android Auto (Viktor Govako)

#### Android

- NUOVO: Visualizza statistiche di registrazione traccia in tempo reale (Kavi Khalique)
- NUOVO: Mostra contenuto tag `description` OSM (Alexander Borsuk)
- Correggi gestione cambio tema (Andrei Shkrob)
- Corretti diversi crash, incluso quello all'avvio (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Notifiche di progresso download silenziose (Viktor Govako)
- Riduci spaziatura icona matita (Alexander Borsuk)

#### Desktop

- Correggi blocco curl su Linux (Alexander Borsuk)
- Correggi blocco su macOS durante l'accesso a OSM (Alexander Borsuk)
- Azione per selezionare funzionalità dal menu contestuale (Viktor Govako)
- Opzione per annullare il download (Viktor Govako)
- Mostra tipo di geometria nel menu contestuale (Viktor Govako)

### Funzionalità rilasciate di recente che potresti aver perso

- Numeri di linea del trasporto pubblico quando si seleziona una fermata dell'autobus
- Percorsi escursionistici e ciclabili (attivarli tramite il pulsante Livelli in alto a sinistra)
- Vedi i nomi dei segnalibri sulla mappa attivandolo nelle Impostazioni dell'app
- L'icona della matita ✎ offre un modo rapido per modificare i segnalibri

### Installa Organic Maps

Ottieni l'ultima versione di Organic Maps dall'[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

Unisciti ai test beta per le funzionalità in anteprima: [iOS][testflight] / [Android][firebase].

{{ references() }}
