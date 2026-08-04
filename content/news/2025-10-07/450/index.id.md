---
title: "Rilis 7 Oktober: batas kecepatan Android Auto, impor GeoJSON, statistik perekaman trek, tampilan tag description OSM, simpan penanda pada trek terpilih di iOS, dan lainnya"
date: 2025-10-07T10:00:00+00:00
taxonomies:
  news: ["releases"]
---

Pembaruan Organic Maps 7 Oktober ini menambahkan tampilan batas kecepatan di Android Auto, impor GeoJSON, statistik perekaman trek, menampilkan tag description OSM (ketik `?description` di kotak pencarian untuk melihatnya), dan menyimpan penanda pada sebuah trek di iOS. Ada juga banyak peningkatan pada antarmuka pengguna, penyuntingan OpenStreetMap, dan berbagai perbaikan bug di semua platform, termasuk perbaikan crash saat memulai aplikasi di sebagian perangkat Android.

Organic Maps hadir berkat ❤️ para kontributor kami, [donasimu](@/donate/index.id.md), dan [dukunganmu](@/contribute/index.id.md).

### Catatan rilis terperinci (termasuk perubahan dari pembaruan kecil sebelumnya)

- BARU! Impor GeoJSON (Sergiy Kozyr)
- Data OpenStreetMap per 4 Oktober
- Data Wikipedia per 1 Oktober
- Dukungan light rail Seattle untuk transportasi umum (tjasz)
- Pemilihan di peta tidak lagi dibatalkan saat menyimpan tempat OSM yang telah disunting (Kiryl Kaveryn)
- Terjemahan diperbarui (kontributor Weblate)

#### Gaya peta

- Menampilkan toko persewaan sepeda yang ditandai amenity=bicycle + rental=shop (David Martinez)
- Menampilkan situs arkeologi bersejarah mulai zoom 12 dan situs bersejarah lainnya mulai zoom 15 dalam gaya Outdoor (Viktor Govako)
- Ikon baru untuk menara pemancar, komunikasi, dan listrik dalam gaya Outdoors (David Martinez)
- Memperbesar ukuran ikon puncak dalam gaya Outdoors (David Martinez)
- Menambahkan varian ikon POI yang belum ada (David Martinez)
- Menambahkan lebih banyak jenis penghalang (Viktor Govako)

#### iOS

- BARU: Simpan penanda pada titik trek yang dipilih (Kiryl Kaveryn)
- BARU: Hapus trek yang sedang direkam tanpa perlu menyimpannya lebih dulu (Kiryl Kaveryn)
- Menampilkan judul daftar penanda dalam beberapa baris di Halaman Tempat (David Martinez)
- Memperbarui gaya tombol login OSM (Kiryl Kaveryn)
- Memperbaiki masalah pembaruan info navigasi (Kiryl Kaveryn)
- Memperbaiki masalah pada perencanaan rute baru (Kiryl Kaveryn)
- Memperbaiki visibilitas tambah/sunting tempat OSM untuk peta yang lebih lama dari 3 bulan (Kiryl Kaveryn)
- Memperbaiki tata letak kontrol segmen opsi transportasi untuk iOS 26 (Kiryl Kaveryn)
- Menyederhanakan animasi pemilihan penanda (Kiryl Kaveryn)
- Memperbaiki masalah pemilihan hasil pencarian (Kiryl Kaveryn)
- Memperbaiki gaya, gestur geser, dan animasi Halaman Informasi Tempat (Kiryl Kaveryn)

#### Android Auto (khusus Google Play)

- BARU: Tampilan batas kecepatan di Android Auto (Andrei Shkrob)
- Memperbaiki peralihan layar dalam mode navigasi Android Auto (Andrei Shkrob)
- Memperbaiki offset panah rute di Android Auto (Andrei Shkrob)
- Memperbaiki masalah saat perangkat tersambung/terputus dari mobil (Andrei Shkrob)
- Menambahkan layanan lokasi Android Auto (Andrei Shkrob)
- Meningkatkan simulator rute Android Auto (Viktor Govako)

#### Android

- BARU: Lihat statistik perekaman trek secara waktu nyata (Kavi Khalique)
- BARU: Menampilkan isi tag `description` OSM (Alexander Borsuk)
- Memperbaiki penanganan pergantian tema (Andrei Shkrob)
- Memperbaiki beberapa crash, termasuk crash saat memulai aplikasi (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Notifikasi kemajuan unduhan kini senyap (Viktor Govako)
- Mengurangi padding ikon pensil (Alexander Borsuk)

#### Desktop

- Memperbaiki curl yang menggantung di Linux (Alexander Borsuk)
- Memperbaiki aplikasi menggantung di macOS saat login ke OSM (Alexander Borsuk)
- Aksi untuk memilih fitur dari menu konteks (Viktor Govako)
- Opsi untuk membatalkan unduhan (Viktor Govako)
- Menampilkan jenis geometri di menu konteks (Viktor Govako)

### Fitur yang baru dirilis dan mungkin kamu lewatkan

- Nomor rute transportasi umum saat memilih halte bus
- Rute hiking dan bersepeda (aktifkan lewat tombol Lapisan di kiri atas)
- Lihat nama penanda di peta dengan mengaktifkannya di Pengaturan aplikasi
- Ikon pensil ✎ memberi cara cepat untuk menyunting penanda

### Pasang Organic Maps

Dapatkan versi Organic Maps terbaru dari [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], dan [F-Droid][fdroid].

Ikuti pengujian beta untuk mencoba fitur awal: [iOS][testflight] / [Android][firebase].

{{ references() }}
