---
title: Teks-ke-Ucapan di Android
description: Panduan cara membuat TTS berfungsi di Android
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
---

## Ringkasan

Peta Organik menggunakan mesin sistem text-to-speech (TTS) untuk instruksi suara. Mesin default berbeda-beda menurut perangkat. Pilihannya dapat mencakup Google Text-to Speech, mesin pabrikan perangkat, atau mesin pihak ketiga.

Rekomendasi resmi dari Organic Maps adalah [RHVoice](https://rhvoice.org/), yang merupakan mesin ucapan gratis dan bersumber terbuka yang dapat diunduh dari [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) dan [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Petunjuk

- Buka aplikasi Pengaturan di perangkat Android Anda
- Pilih Pengaturan Tambahan lalu pilih Aksesibilitas
- Pilih mesin, kecepatan bicara, dan nada pilihan Anda
- **Mulai ulang aplikasi Peta Organik**
- Buka Pengaturan => Petunjuk Suara di Peta Organik dan atur
- Mulai ulang aplikasi Peta Organik (atau reboot perangkat) jika suaranya tidak berfungsi

Jika Anda tidak dapat menemukan pengaturan yang relevan, buka aplikasi pengaturan dan cari Text-to-speech.

P.S: Perlu diperhatikan bahwa langkah-langkah ini akan berbeda-beda berdasarkan merek ponsel yang Anda gunakan.

Opsi tersebut mungkin tidak muncul jika Anda belum menginstal TTS di perangkat Anda. Silakan merujuk ke tabel di bawah untuk menginstal salah satu dari mereka yang mendukung bahasa ibu Anda.

## Tangkapan layar

|             |             |
| ----------- | ----------- |
![Pengaturan](tts_config_1.png "Pengaturan") | ![Aksesibilitas](tts_config_2.png "Aksesibilitas")

## Mesin {#mesin}

Di bawah ini adalah daftar lengkap yang menunjukkan beberapa mesin dan bahasa yang didukungnya (tautan unduhan dapat ditemukan setelah tabel):

{{ tts_table() }}

## Solusi

Jika Anda mengalami masalah saat menginisialisasi mesin RHVoice TTS di LineageOS atau ROM khusus lainnya, coba solusi ini. RHVoice mungkin tidak diinisialisasi dengan benar dan aplikasi mungkin mogok, terutama jika Anda belum pernah menggunakan mesin TTS apa pun di ponsel Anda sebelumnya (misalnya, instalasi baru, reset pabrik, dll.). Jika Anda menggunakan ROM khusus seperti LineageOS <ins>tanpa layanan Google Play dan Layanan Ucapan dari Google</ins>, dan Anda ingin menggunakan RHVoice sebagai mesin TTS pilihan Anda, ikuti petunjuk di bawah sebagai solusinya:

1. Instal [mesin eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak) yang tersedia di F-Droid
2. Tetapkan sebagai mesin sistem pilihan
    - Buka **Pengaturan** utama LineageOS.
    - Gulir ke bawah ke **Aksesibilitas**.
    - Pilih **text-to-speech output** dan **Preferred engine** (sisi kiri) dan pastikan **eSpeak** dipilih.
3. Kembali dan tekan **mainkan** untuk melihat apakah ini berfungsi
4. Instal [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) yang tersedia di F-droid.
    - Buka, pilih bahasa yang ingin Anda gunakan, ketuk ikon cloud (paling kiri) untuk mengunduh suara.
    - Tekan tombol putar untuk memverifikasi apakah itu berfungsi
5. Tetapkan **RHVoice** sebagai mesin pilihan (lihat langkah 2)
6. Sekarang, Anda seharusnya dapat menggunakan RHVoice tanpa masalah apa pun

## Pengujian

Untuk menguji instruksi suara, Anda dapat mengetuk "Uji Arah Suara (TTS, Text-To-Speech)" di menu OM "Pengaturan → Petunjuk Suara" atau Anda dapat memulai navigasi untuk menerima keluaran suara apa pun. Peta Organik tidak akan memberi Anda instruksi suara apa pun saat Anda diam.

![Tes TTS](tts_test.png "Tes TTS")
