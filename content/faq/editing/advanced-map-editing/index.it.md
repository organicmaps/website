---
title: Come posso apportare modifiche più avanzate alla mappa?
description: Tutorial per modificare OpenStreetMap con strumenti più avanzati come
  ID, Go Map e Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
---

Organic Maps include un editor semplice e facile da usare che puoi utilizzare per modificare la mappa. L'editor, tuttavia, è limitato e consente solo di aggiungere semplici elementi puntuali, ovvero nessun contorno di edifici, strade, laghi, città, ecc. Se vuoi cambiare qualcosa che non può essere modificato con l'editor integrato, questa è la pagina FAQ giusta da leggere.

Poiché tutti i dati della mappa utilizzati in Organic Maps provengono da [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), puoi aggiornare direttamente la mappa lì. Le tue modifiche verranno quindi incluse nelle mappe organiche con il prossimo aggiornamento della mappa.

## Editor di OpenStreetMap

Per modificare OSM ci sono diverse opzioni. Se hai un laptop o un computer desktop a portata di mano, è meglio utilizzare l'[ID Editor](https://www.openstreetmap.org/edit) che viene eseguito nel tuo browser. L'editor ID è facile per i principianti e uno schermo, un mouse e una tastiera più grandi semplificano la modifica della mappa.

Per la modifica avanzata della mappa da un dispositivo mobile, utilizza [Go Map](https://apps.apple.com/us/app/go-map/id592990211) per iOS o [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) per Android. Go Map è facile per i principianti, mentre Vespucci si rivolge agli utenti più avanzati. LearnOSM fornisce tutorial per [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) e [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Per modifiche più semplici e più divertenti, puoi anche provare l'[app Every Door](https://every-door.app/) per iOS e Android e l'[app StreetComplete](https://streetcomplete.app/) per Android.

#### Editore ID

Per modificare OpenStreetMap con ID segui questi passaggi:

1. Crea un nuovo account o accedi a [OpenStreetMap.org](https://www.openstreetmap.org)
2. Individua la posizione che desideri modificare su OpenStreetMap.org e fai clic su *Modifica* in alto
3. *Avvia la procedura dettagliata* e segui il breve tutorial che spiega l'editor ID
4. Modifica la mappa
5. Carica le tue modifiche

Questo è tutto, ora fai parte della comunità OSM.

## Cosa succede con le mie modifiche?

Dopo aver premuto *Carica* le modifiche verranno immediatamente aggiunte al database OSM pubblico. Quindi sii attento durante la modifica. Nelle mappe organiche, le modifiche saranno visibili dopo il prossimo aggiornamento mensile della mappa.

La tua email non verrà pubblicata, ma altre persone potranno vedere il tuo nome utente OSM. Poiché OSM offre la possibilità di discutere le modifiche, potresti ricevere domande sulle tue modifiche da altri contributori OSM. Riceverai una notifica a riguardo tramite l'indirizzo e-mail che hai utilizzato per registrare il tuo account OSM. Poiché OSM è un progetto comunitario che si basa sulla collaborazione, dovresti sempre rispondere a queste domande.

## Comunità e Wiki

OpenStreetMap è una comunità. Se hai bisogno di aiuto o hai domande puoi chiedere nel [Forum OSM](https://community.openstreetmap.org/c/help-and-support) o dare un'occhiata alla documentazione [OSM Wiki](https://wiki.openstreetmap.org/).

## Tag - Come funziona il modello dati OSM

Il database OpenStreetMap contiene oggetti come nodi, percorsi, aree e relazioni che astraggono dalle caratteristiche del mondo reale. Questi Oggetti hanno Attributi, i cosiddetti Tag per descriverli ulteriormente. Un tag è una combinazione chiave-valore.

Poiché sembra più complicato di quello che è, forniremo un esempio:
Un ristorante è ad es. mappato come una nota o un'area con il tag ``` amenity=restaurant```. Ulteriori tag come ```cousine=*``` o ```opening_hours=*``` possono essere utilizzati per ulteriori dettagli.

> Tieni presente che l'editor ID nasconde la struttura dei dati interni agli utenti per essere più adatto ai principianti. Ma per leggere la documentazione del Wiki è utile avere una breve panoramica della struttura dei dati.
Nell'editor ID, puoi vedere i tag che l'ID ti nasconde espandendo la sezione *Tag* nel pannello laterale *Funzione di modifica*.

## Note OSM {#osm-note}

Se non hai tempo o il problema è troppo complicato, puoi modificare tu stesso i dati OSM, le note OSM ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) sono la strada da percorrere. Puoi inserire una nota di questo tipo nella posizione dell'errore della mappa e descrivere il problema in dettaglio. Altri volontari OSM possono quindi aiutare e risolvere il problema. Riceverai notifiche via e-mail tramite il tuo account OSM nel caso in cui abbiano ulteriori domande o la nota OSM venga risolta.

1. Crea un nuovo account o accedi a [OpenStreetMap.org](https://www.openstreetmap.org)
   > Puoi anche aprire Note anonime, ma questo non è consigliato poiché non riceverai una notifica quando il problema verrà risolto o ci saranno ulteriori domande.
2. Ingrandisci la posizione della mappa su [OpenStreetMap.org](https://www.openstreetmap.org) e premi *Aggiungi una nota alla mappa* (seconda icona dal basso nel menu a destra). Quindi trascina l'indicatore blu della mappa sulla posizione esatta.
   > Cerca di essere il più preciso possibile.
3. Fornisci una descrizione dettagliata del problema della mappa e premi *Aggiungi nota*
   > Per negozi, ad es. fornire il nome e menzionare cosa viene venduto lì o quali servizi vengono offerti.
