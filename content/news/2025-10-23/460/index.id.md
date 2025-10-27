---
title: "Rilis 23 Oktober: Organic Maps sebagai aplikasi navigasi default di UE pada iOS, tampilan perisai jalan di Android, dan lebih banyak perbaikan dan peningkatan"
date: 2025-10-23T17:20:21+00:00
slug: "rilis-23-oktober-organic-maps-aplikasi-navigasi-default-ue-ios-perisai-jalan-android-perbaikan-peningkatan"
taxonomies:
  news: ["Releases"]
---

Dalam rilis 23 Oktober kami fokus pada perbaikan dan peningkatan. Periksa daftar terperinci di bawah ini.

Bagi yang terlewat, [pembaruan 7 Oktober sebelumnya](https://organicmaps.app/news/2025-10-07/android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display/
) menambahkan impor GeoJSON, statistik perekaman trek, tampilan batas kecepatan di Android Auto, tampilan tag deskripsi OSM (ketik `?description` di kotak pencarian untuk melihatnya), menyimpan bookmark pada trek di iOS, dan banyak peningkatan lainnya.

## Semua Platform

- Data OpenStreetMap segar dari 21 Oktober 2025 (Viktor Govako)
- Tampilkan nama pintu masuk/keluar subway di peta (Viktor Govako)
- Jenis POI dan ikon baru: stasiun pemantauan, pulau lalu lintas, fasilitas terapi air Kneipp, kereta api miniatur (Viktor Govako), tempat berkemah dalam gaya luar ruangan, terminal bandara, area bermain dalam ruangan, toko telekomunikasi, fasilitas penyewaan perahu, fasilitas peluncuran, ikon pembuangan sampah dan tempat pembuangan akhir yang diperbarui (David Martinez)
- Terjemahan antarmuka aplikasi Slovenia (Alexander Borsuk) dan panduan suara TTS untuk navigasi (Erik Bucik)
- Di beberapa perangkat/layar, peta di pusat kota sekarang lebih tidak berantakan (Viktor Govako)
- Perbaikan rotasi peta pada sensor kompas yang buruk saat berjalan dalam mode navigasi pejalan kaki (Viktor Govako)
- Informasi yang ditingkatkan ditampilkan setelah memilih sungai atau segmen jalur air (Viktor Govako)
- Pencarian stasiun pengisian EV yang lebih baik dengan sinonim yang ditingkatkan dalam semua bahasa (Alexander Borsuk)
- Perbaikan pencarian emoji dengan pemilih varian (Alexander Borsuk)
- Perbaikan terlalu banyak hasil pencarian yang ditampilkan untuk beberapa kueri pencocokan alamat lengkap (Viktor Govako)
- Mengimpor GeoJSON dari https://umap.openstreetmap.fr/ sekarang seharusnya mempertahankan semua metadata (Shubh Kesharwani)
- Warna tambahan didukung untuk jalur bertanda untuk lapisan peta Rute Pendakian (Viktor Govako)

## iOS

- Pengguna UE dapat mengatur Organic Maps sebagai aplikasi navigasi default di Pengaturan iOS → Aplikasi → Aplikasi Default → Navigasi (Kiryl Kaveryn)
- Perbaikan bilah status putih-pada-putih dalam mode navigasi (Kiryl Kaveryn)
- Peningkatan ukuran tombol Mulai Navigasi (Kiryl Kaveryn)
- Menghapus ruang kosong saat merencanakan rute di iPad (Kiryl Kaveryn)
- Organic Maps mungkin meminta Anda untuk menilainya di App Store. Ulasan baik Anda memotivasi tim kami!

## Android

- Perisai jalan sekarang muncul dalam petunjuk navigasi (Andrei Shkrob)
- Peningkatan informasi perekaman trek (Kavi Khalique)
- Organic Maps berfungsi pada beberapa perangkat Intel x86 yang lebih lama (Andrei Shkrob)
- Perbaikan petunjuk suara TTS yang tidak berfungsi dalam beberapa kasus (Andrei Shkrob)
- Layar splash yang lebih baik saat startup (Andrei Shkrob)

### Android Auto
- Pulihkan rute setelah pembatalan (Andrei Shkrob)
- Perbaikan crash pada beberapa perangkat (Andrei Shkrob)

## Linux/Mac OS

- Detail POI sekarang menampilkan format "nama | ref" (Viktor Govako)
- mode gelap secara otomatis sinkron dengan pengaturan sistem (DeepChirp)

## Catatan kaki

Organic Maps dimungkinkan berkat ❤️ kontributor kami, [donasi Anda](@/donate/index.id.md), dan [dukungan Anda](@/contribute/index.id.md).

Dapatkan versi Organic Maps terbaru dari [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], dan [F-Droid][fdroid].

P.S. Bergabunglah dengan pengujian beta untuk fitur awal:
- [iOS][testflight]
- [Android][firebase].

Dengan cinta untuk pengguna dan komunitas kami
Tim Organic Maps

{{ references() }}
