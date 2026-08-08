---
title: "Perbaikan bug dan peningkatan pada fitur transportasi umum, perhitungan rute, pencarian, dan penanda dalam pembaruan bulan Juli 2026"
date: 2026-07-23
slug: "perbaikan-bug-peningkatan-transportasi-umum-rute-pencarian-penanda-juli-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Seperti yang mungkin sudah kamu ketahui, pembaruan Organic Maps bulan Juli telah dirilis. Unduh di <https://get.omaps.org> atau di [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], dan [F-Droid][fdroid].

Berkat [donasi](@/donate/index.id.md) dan [masukan](@/contribute/index.id.md) darimu, pada bulan Juli kami berfokus pada perbaikan bug dan peningkatan. Kalau kamu belum sempat melihatnya, fitur-fitur berikut dari [rilis bulan Juni sebelumnya](@/news/2026-06-29/610/index.id.md) juga sudah tersedia:
- Rute angkutan umum (jadwal real-time sedang dalam tahap pengembangan)
- Citra satelit
- Rute alternatif untuk berkendara, mendaki, dan bersepeda
- Antarmuka pencarian dan perencanaan rute baru untuk Android
- Dukungan font berukuran besar untuk aksesibilitas di iOS

## Daftar perubahan terperinci

### Peta & tempat

- Data OpenStreetMap diperbarui per 14 Juli
- Catatan yang dilaporkan ke [OpenStreetMap](https://www.openstreetmap.org) kini ditempatkan tepat di lokasi yang kamu pilih, bukan di tengah-tengah jalan atau area tersebut _(Alexander Borsuk)_
- Peningkatan pemilihan lokasi saat mengetuk peta di wilayah yang melintasi antimeridian 180° _(Viktor Govako)_
- Profil ketinggian trek tidak lagi menampilkan grafik yang sudah usang atau kosong setelah trek dihapus _(Kiryl Kaveryn)_

### Angkutan umum

- Nama pemberhentian, transfer, dan stasiun kini dilengkapi garis tepi putih agar tetap mudah dibaca baik pada tema terang maupun gelap _(Viktor Govako)_
- Lapisan jalur kereta bawah tanah akan muncul kembali dengan benar setelah kamu menutup pratinjau rute angkutan umum _(Mikhail Listratsenka)_

### Perutean & navigasi

- Peringatan rute (tol, feri, jalan tidak beraspal, tangga, dan sebagainya) kini ditampilkan untuk semua rute alternatif _(Viktor Govako)_
- Telah diperbaiki masalah hang yang jarang terjadi saat membuat rute _(Viktor Govako)_
- Peningkatan penanganan jalan buntu serta titik awal dan akhir pada jalan dengan pembatasan _(Viktor Govako)_
- Memperbaiki petunjuk belokan yang salah dan yang hilang _(Alexander Borsuk)_

### iOS

- Pengaturan baru “Simpan riwayat pencarian” yang memungkinkan kamu menonaktifkan riwayat tersebut dan menyembunyikannya kalau kamu memilih untuk tidak menyimpannya _(Kiryl Kaveryn)_
- Tombol “Edit” baru untuk menghapus penanda dengan lebih mudah _(Kiryl Kaveryn)_
- Penanda kini disimpan secara otomatis saat kamu meninggalkan layar _(Kiryl Kaveryn)_
- Palet warna kini menyediakan warna-warna bawaan dan memungkinkan kamu memilih warna kustom apa pun _(Kiryl Kaveryn)_
- Telah dilakukan perbaikan pada status kosong grafik ketinggian untuk trek yang telah direkam _(Kiryl Kaveryn)_
- Telah diperbaiki tampilan kemajuan rute yang ditampilkan pada tombol “Mulai” _(Kiryl Kaveryn)_
- Mengubah urutan perhentian rute tidak lagi menyebabkan daftar tersebut bergeser-geser _(Kiryl Kaveryn)_
- Perbaikan antarmuka kecil lainnya _(Kiryl Kaveryn)_

### Android

- Jam operasional kini menampilkan shift terbagi (seperti waktu istirahat makan siang), dimulai dari hari ini, dan menampilkan seluruh minggu tanpa area gulir terpisah _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Bilah pencarian yang lebih rapi dengan tombol hapus dan perintah suara yang digabungkan, ikon hapus yang tidak lagi berpindah-pindah, serta perbaikan tata letak untuk mode lanskap dan rotasi ponsel _(Mikhail Listratsenka)_
- Editor penanda dan trek yang telah dirombak _(Mikhail Listratsenka)_
- Perbaikan dan peningkatan perencanaan rute _(Mikhail Listratsenka)_
- Pemilih warna kini tertutup secara otomatis, dan masalah crash pada Android 5 telah diperbaiki _(Mikhail Listratsenka)_
- Memperbaiki masalah crash _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop

- Daftar peta yang tersedia untuk diunduh kini telah diurutkan berdasarkan abjad _(goncalo109560)_

### Terjemahan

- Perbaikan redaksi dalam bahasa Mandarin _(Chenxi Zhao)_
- Terjemahan bahasa Ukraina yang telah diperbarui _(Nnifria)_
- Telah diperbaiki terjemahan nama wilayah peta dalam bahasa Italia _(Vittorio Bertola)_

## Bergabunglah dengan pengujian beta untuk mencoba fitur awal dan melaporkan masalah:

Petunjuk: versi beta ini memiliki efek bayangan relief baru, data ketinggian yang lebih baik dengan dukungan satuan kaki dan meter, serta fitur-fitur keren lainnya!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Selamat menikmati musim panas!
Tim Organic Maps

{{ references() }}
