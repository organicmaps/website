---
title: Testu-hizketa Android-en
description: TTS Android-en funtzionatzeko gida
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
---

## Laburpena

Organic Maps-ek sistemako testu-hizketarako (TTS) motorra erabiltzen du ahots-argibideetarako. Motor lehenetsiak gailuaren arabera aldatzen dira. Aukerak Google Text-to Speech, gailuaren fabrikatzailearen motorra edo hirugarrenen bat izan daitezke.

Organic Maps-en gomendio ofiziala [RHVoice](https://rhvoice.org/) da, hau da, [Google Play]-tik deskargatu daitekeen kode irekiko ahots-motorra (https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) eta [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Argibideak

- Ireki Ezarpenak aplikazioa zure Android gailuan
- Hautatu Ezarpen gehigarriak eta, gero, hautatu Irisgarritasuna
- Aukeratu nahi duzun motorra, hizketa-abiadura eta tonua
- **Berrabiarazi Organic Maps aplikazioa**
- Ireki Ezarpenak => Ahots-argibideak Mapa organikoetan eta konfiguratu
- Berrabiarazi Organic Maps aplikazioa berriro (edo berrabiarazi gailua) ahotsak funtzionatzen ez badu

Ezin baduzu dagokion ezarpena aurkitzen, ireki ezarpenen aplikazioa eta bilatu Text-to-speech.

P.S: Kontuan izan urrats hauek erabiltzen ari zaren telefono-markaren arabera aldatuko direla.

Baliteke aukera horiek ez agertzea zure gailuan TTSrik instalatuta ez baduzu. Mesedez, begiratu beheko taulara zure ama hizkuntza onartzen duen horietako bat instalatzeko.

## Pantaila-argazkiak

|             |             |
| ----------- | ----------- |
![Ezarpenak](tts_config_1.png "Ezarpenak") | ![Erisgarritasuna](tts_config_2.png "Irisgarritasuna")

## Motorrak {#motorrak}

Jarraian, hainbat motor eta onartzen dituzten hizkuntzak erakusten dituen zerrenda zabala dago (deskargarako estekak taularen ondoren aurki daitezke):

{{ tts_table() }}

## Konponbideak

LineageOS edo bestelako ROM pertsonalizatuetan RHVoice TTS motorra hasieratzeko arazoak badituzu, saiatu konponbide hau. Baliteke RHVoice behar bezala ez hasieratzea eta aplikazioa huts egitea, batez ere telefonoan TTS motorrik erabili ez baduzu (adibidez, instalazio berria, fabrika berrezarri, etab.). LineageOS bezalako ROM pertsonalizatu bat erabiltzen ari bazara <ins>Google Play zerbitzurik eta Google Speech Services</ins> gabe, eta RHVoice erabili nahi baduzu TTS motor gisa, jarraitu beheko argibideak konponbide gisa:

1. Instalatu [eSpeak TTS motorra](https://f-droid.org/en/packages/com.reecedunn.espeak) F-Droid-en eskuragarri
2. Ezarri sistema-motor hobetsia gisa
    - Joan LineageOS **Ezarpenak** nagusira.
    - Joan behera **Irisgarritasuna**.
    - Hautatu **testu-hizketarako irteera** eta **Hotsitako motorra** (ezkerreko aldean) eta ziurtatu **eSpeak** hautatuta dagoela.
3. Joan atzera eta sakatu **play** funtzionatzen duen ikusteko
4. Instalatu [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) F-droid-en eskuragarri.
    - Ireki, hautatu erabili nahi duzun hizkuntza, sakatu hodeiaren ikonoa (ezkerrean) ahotsak deskargatzeko.
    - Sakatu erreproduzitzeko botoia funtzionatzen ari den egiaztatzeko
5. Ezarri **RHVoice** hobetsitako motor gisa (ikus 2. urratsa)
6. Orain, RHVoice arazorik gabe erabiltzeko gai izan beharko zenuke

## Probak

Ahots-argibideak probatzeko, OM "Ezarpenak → Ahots-argibideak" menuan "Probatu ahots-jarraibideak (TTS, testu-hizketa)" sakatu edo nabigazio bat has dezakezu edozein ahots-irteera jasotzeko. Organic Maps-ek ez dizu ahots-argibiderik emango geldirik zauden bitartean.

![TTS Test](tts_test.png "TTS Test")
