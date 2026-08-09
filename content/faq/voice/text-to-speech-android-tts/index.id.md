---
title: Teks-ke-Ucapan di Android
slug: teks-ke-ucapan-di-android
description: Panduan cara membuat TTS berfungsi di Android
taxonomies:
  faq:
  - voice-directions
extra:
  order: 10
aliases:
  - /id/faq/voice/text-to-speech-android-tts/
---

## Ringkasan

Organic Maps menggunakan mesin sistem text-to-speech (TTS) untuk instruksi suara. Mesin default berbeda-beda menurut perangkat. Pilihannya dapat mencakup Google Text-to Speech, mesin pabrikan perangkat, atau mesin pihak ketiga.

Rekomendasi resmi dari Organic Maps adalah [RHVoice](https://rhvoice.org/), yang merupakan mesin ucapan gratis dan bersumber terbuka yang dapat diunduh dari [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) dan [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Petunjuk

- Buka aplikasi Pengaturan di perangkat Android kamu
- Pilih Pengaturan Tambahan lalu pilih Aksesibilitas
- Pilih mesin, kecepatan bicara, dan nada pilihan kamu
- **Mulai ulang aplikasi Organic Maps**
- Buka Pengaturan => Petunjuk Suara di Organic Maps dan atur
- Mulai ulang aplikasi Organic Maps (atau reboot perangkat) jika suaranya tidak berfungsi

Jika kamu tidak dapat menemukan pengaturan yang relevan, buka aplikasi pengaturan dan cari Text-to-speech.

P.S: Perlu diperhatikan bahwa langkah-langkah ini akan berbeda-beda berdasarkan merek ponsel yang kamu gunakan.

Opsi tersebut mungkin tidak muncul jika kamu belum menginstal TTS di perangkat kamu. Silakan merujuk ke tabel di bawah untuk menginstal salah satu dari mereka yang mendukung bahasa ibu kamu.

## Tangkapan layar

|             |             |
| ----------- | ----------- |
![Pengaturan](tts_config_1.png "Pengaturan") | ![Aksesibilitas](tts_config_2.png "Aksesibilitas")

## Mesin {#engines}

Di bawah ini adalah daftar lengkap yang menunjukkan beberapa mesin dan bahasa yang didukungnya (tautan unduhan dapat ditemukan setelah tabel):

{{ tts_table() }}

## Solusi

Jika kamu mengalami masalah saat menginisialisasi mesin RHVoice TTS di LineageOS atau ROM khusus lainnya, coba solusi ini. RHVoice mungkin tidak diinisialisasi dengan benar dan aplikasi mungkin mogok, terutama jika kamu belum pernah menggunakan mesin TTS apa pun di ponsel kamu sebelumnya (misalnya, instalasi baru, reset pabrik, dll.). Jika kamu menggunakan ROM khusus seperti LineageOS <ins>tanpa layanan Google Play dan Layanan Ucapan dari Google</ins>, dan kamu ingin menggunakan RHVoice sebagai mesin TTS pilihan kamu, ikuti petunjuk di bawah sebagai solusinya:

1. Instal [mesin eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak) yang tersedia di F-Droid
2. Tetapkan sebagai mesin sistem pilihan
    - Buka **Pengaturan** utama LineageOS.
    - Gulir ke bawah ke **Aksesibilitas**.
    - Pilih **text-to-speech output** dan **Preferred engine** (sisi kiri) dan pastikan **eSpeak** dipilih.
3. Kembali dan tekan **mainkan** untuk melihat apakah ini berfungsi
4. Instal [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) yang tersedia di F-droid.
    - Buka, pilih bahasa yang ingin kamu gunakan, ketuk ikon cloud (paling kiri) untuk mengunduh suara.
    - Tekan tombol putar untuk memverifikasi apakah itu berfungsi
5. Tetapkan **RHVoice** sebagai mesin pilihan (lihat langkah 2)
6. Sekarang, kamu seharusnya dapat menggunakan RHVoice tanpa masalah apa pun

## Pengujian

Untuk menguji instruksi suara, kamu dapat mengetuk “Uji Arah Suara (TTS, Text-To-Speech)” di menu OM “Pengaturan → Petunjuk Suara” atau kamu dapat memulai navigasi untuk menerima keluaran suara apa pun. Organic Maps tidak akan memberi kamu instruksi suara apa pun saat kamu diam.

![Tes TTS](tts_test.png "Tes TTS")
