---
title: Bagaimana saya bisa melakukan pengeditan peta lebih lanjut?
slug: bagaimana-saya-bisa-melakukan-pengeditan-peta-lebih-lanjut
description: Tutorial mengedit OpenStreetMap dengan alat yang lebih canggih seperti
  ID, Go Map dan Vespucci
updated: '2024-06-20'
taxonomies:
  faq:
  - Map Editing
extra:
  order: 40
aliases:
  - /id/faq/editing/advanced-map-editing/
---

Peta Organik menyertakan editor sederhana dan mudah digunakan yang dapat Anda gunakan untuk mengedit peta. Namun editornya terbatas dan hanya mengizinkan penambahan fitur titik sederhana, yang berarti tidak boleh ada garis besar bangunan, jalan, danau, kota, dll. Jika Anda ingin mengubah sesuatu yang tidak dapat diedit dengan editor bawaan, ini adalah halaman FAQ yang tepat untuk dibaca.

Karena semua data peta yang digunakan di Peta Organik berasal dari [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), Anda dapat langsung memperbarui peta di sana. Modifikasi Anda kemudian akan dimasukkan ke dalam Peta Organik pada pembaruan peta berikutnya.

## Editor OpenStreetMap

Untuk mengedit OSM, ada beberapa pilihan. Jika Anda memiliki laptop atau komputer desktop, lebih baik gunakan [ID Editor](https://www.openstreetmap.org/edit) yang berjalan di browser Anda. Editor ID mudah untuk pemula, dan layar, mouse, dan keyboard yang lebih besar membuat pengeditan peta menjadi lebih mudah.

Untuk pengeditan peta tingkat lanjut dari perangkat seluler, gunakan [Go Map](https://apps.apple.com/us/app/go-map/id592990211) untuk iOS atau [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) untuk Android. Go Map mudah untuk pemula, sedangkan Vespucci menargetkan pengguna yang lebih mahir. LearnOSM menyediakan tutorial untuk [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) dan [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Untuk pengeditan yang lebih sederhana dan lebih seru, Anda juga dapat mencoba [aplikasi Every Door](https://every-door.app/) untuk iOS dan Android serta [aplikasi StreetComplete](https://streetcomplete.app/) untuk Android.

#### Penyunting Identitas

Untuk mengedit OpenStreetMap dengan ID ikuti langkah-langkah berikut:

1. Buat akun baru atau masuk ke [OpenStreetMap.org](https://www.openstreetmap.org)
2. Telusuri lokasi yang ingin Anda edit di OpenStreetMap.org dan klik *Edit* di bagian atas
3. *Mulai Panduan* dan ikuti tutorial singkat yang menjelaskan Editor ID
4. Edit peta
5. Unggah perubahan Anda

Itu saja, Anda sekarang menjadi bagian dari komunitas OSM.

## Apa yang terjadi dengan hasil edit saya?

Setelah Anda menekan *Unggah* perubahan Anda akan langsung ditambahkan ke database OSM publik. Jadi berhati-hatilah saat mengedit. Di Peta Organik, perubahan Anda akan terlihat setelah pembaruan peta bulanan berikutnya.

Email Anda tidak dipublikasikan, namun orang lain akan dapat melihat nama pengguna OSM Anda. Karena OSM menawarkan kemungkinan untuk mendiskusikan perubahan, Anda mungkin mendapat pertanyaan tentang hasil edit Anda dari kontributor OSM lainnya. Anda akan diberitahu tentang hal ini melalui alamat email yang Anda gunakan untuk mendaftarkan akun OSM Anda. Karena OSM adalah proyek komunitas yang dibangun berdasarkan kolaborasi, Anda harus selalu menjawab pertanyaan-pertanyaan tersebut.

## Komunitas dan Wiki

OpenStreetMap adalah sebuah komunitas. Jika Anda memerlukan bantuan atau memiliki pertanyaan, Anda dapat bertanya di [Forum OSM](https://community.openstreetmap.org/c/help-and-support) atau lihat dokumentasi [OSM Wiki](https://wiki.openstreetmap.org/).

## Tag - Cara kerja model data OSM

Basis data OpenStreetMap berisi Objek seperti Node, Jalan, Area, dan Relasi yang abstrak dari fitur dunia nyata. Objek-objek ini mempunyai Atribut, yang disebut Tag untuk mendeskripsikannya lebih lanjut. Tag adalah kombinasi Nilai-Kunci.

Karena ini terdengar lebih rumit, kami akan memberikan contoh:
Sebuah Restoran misalnya. dipetakan sebagai Catatan atau Area dengan Tag ``` amenity=restaurant```. Tag lebih lanjut seperti ```sepupu=*``` atau ```jam_buka=*``` kemudian dapat digunakan untuk detail lebih lanjut.

> Perhatikan bahwa editor ID menyembunyikan struktur data internal dari pengguna agar lebih ramah bagi pemula. Namun untuk membaca dokumentasi Wiki, memberikan gambaran singkat tentang struktur data sangat membantu.
Di Editor ID, Anda dapat melihat Tag yang ID sembunyikan dari Anda dengan memperluas bagian *Tag* di panel samping *Fitur Edit*.

## Catatan OSM {#osm-note}

Jika Anda tidak punya waktu atau masalahnya terlalu rumit untuk mengedit sendiri data OSM Catatan OSM ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) adalah cara yang tepat. Anda dapat menempatkan catatan seperti itu di lokasi kesalahan peta dan menjelaskan masalahnya secara rinci. Relawan OSM lainnya kemudian dapat membantu dan memecahkan masalah tersebut. Anda akan mendapatkan notifikasi email melalui akun OSM Anda jika ada pertanyaan lebih lanjut atau Catatan OSM terselesaikan.

1. Buat akun baru atau masuk ke [OpenStreetMap.org](https://www.openstreetmap.org)
   > Anda juga dapat membuka Catatan anonim, namun hal ini tidak disarankan karena Anda tidak akan diberi tahu ketika masalah telah teratasi atau ada pertanyaan lebih lanjut.
2. Perbesar lokasi peta di [OpenStreetMap.org](https://www.openstreetmap.org) dan tekan *Tambahkan catatan ke peta* (ikon kedua dari bawah di menu kanan). Kemudian seret penanda peta biru ke lokasi yang tepat.
   > Cobalah untuk menjadi setepat mungkin.
3. Berikan penjelasan rinci tentang masalah peta dan tekan *Tambahkan Catatan*
   > Untuk toko mis. sebutkan nama dan sebutkan apa yang dijual disana atau jasa apa saja yang ditawarkan.
