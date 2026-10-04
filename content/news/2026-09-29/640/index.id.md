---
title: "Pengoptimalan rute, rute alternatif yang lebih baik, penyembunyian trek satu per satu, dan area yang tidak selalu berair dalam pembaruan September 2026"
date: 2026-09-29
slug: "pengoptimalan-rute-rute-alternatif-sembunyikan-trek-area-tidak-selalu-berair-september-2026"
aliases: ["/id/news/2026-09-29/pemilihan-ganda-penanda-trek-dasbor-carplay-sembunyikan-trek-tautan-berbagi-agustus-2026/"]
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Siap berangkat? Pembaruan September menghadirkan rute alternatif yang lebih baik, pengaturan untuk mengoptimalkan urutan perhentian rute, penandaan yang lebih jelas untuk area yang tidak selalu berair, dan ikon mata untuk menyembunyikan trek satu per satu, bersama dengan banyak perbaikan dan peningkatan lainnya (lihat di bawah).

Instal atau perbarui Organic Maps melalui <https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], atau [F-Droid][fdroid].

Jika kamu melewatkan pembaruan kami sebelumnya, lihat fitur-fitur yang dirilis pada [Juni](@/news/2026-06-29/610/index.id.md), [Juli](@/news/2026-07-23/620/index.id.md), dan [Agustus](@/news/2026-08-31/630/index.id.md). Terima kasih kepada para kontributor dan pengguna kami yang membuat pembaruan ini menjadi mungkin!

## Cara mendukung Organic Maps

- [Berikan donasi](@/donate/index.id.md) untuk mendukung pengembangan dan menutup biaya hosting peta
- [Kirimkan masukanmu dan berkontribusilah](@/contribute/index.id.md) pada proyek ini
- Bergabunglah dalam uji coba beta untuk mencoba fitur-fitur baru lebih awal dan laporkan masalah yang kamu temui di [iOS][testflight], [Android][firebase], dan [desktop][flathub]
- Sebarkan kabar ini dan bantu kami menciptakan alternatif yang lebih baik daripada peta-peta dari perusahaan teknologi raksasa!

## Catatan rilis

### Peta

- Data OpenStreetMap per 28 September 2026
- Data Wikipedia per 21 September 2026
- Telah diperbaiki masalah pencarian saat area peta yang terlihat melintasi meridian 180° (bujur ±180°) _(Viktor Govako)_
- Area yang tidak selalu berair kini ditampilkan dengan pola titik-titik, mirip dengan pola yang digunakan untuk pasir _(Alexander Borsuk)_
- Waduk kini terlihat saat tampilan peta diperkecil lebih jauh _(Alexander Borsuk)_
- Terowongan air tidak lagi ditampilkan di peta _(Alexander Borsuk)_
- Ikon stasiun dan pintu masuk Kereta Bawah Tanah Suzhou telah diperbaiki _(Alexander Borsuk)_
- Telah diperbaiki beberapa kasus langka ketika label bergeser dari posisinya pada lapisan peta metro _(Viktor Govako)_

### Perutean dan navigasi

- Rute alternatif dan perkiraan waktu kedatangannya kini lebih baik _(Alexander Borsuk, Viktor Govako)_
- Rute alternatif yang dipilih kini tetap dipertahankan saat navigasi menghitung ulang rute _(Alexander Borsuk)_
- Urutan perhentian rute kini dipulihkan setelah aplikasi dimulai ulang _(Kiryl Kaveryn)_

### Peningkatan lainnya

- Jam buka kini menampilkan “Tengah hari” untuk pukul 12:00 dan “Tengah malam” untuk pukul 00:00 atau 24:00 _(Alexander Borsuk)_
- Memperbaiki bug dan meningkatkan fitur perekaman trek _(Alexander Borsuk)_
- Masalah impor berkas KMB telah diperbaiki _(Alexander Borsuk)_
- Terjemahan bahasa Prancis dan Asturia telah diperbaiki _(Alexander Borsuk)_
- Memperbaiki kesalahan ketik dalam bahasa Inggris _(Carl Morris)_

### iOS

- Ditambahkan ikon mata untuk menyembunyikan trek satu per satu _(Kiryl Kaveryn)_
- Ditambahkan tombol untuk menambahkan atau mengganti titik perhentian dalam rute yang telah direncanakan _(Kiryl Kaveryn)_
- Ditambahkan pengaturan untuk mengoptimalkan urutan titik perhentian antara titik awal dan tujuan _(Kiryl Kaveryn)_
- Telah ditambahkan petunjuk manuver ke head-up display (HUD) mobil yang didukung dan dasbor CarPlay _(Kiryl Kaveryn)_
- Tombol CarPlay dan fitur pencarian telah diperbaiki _(Alexander Borsuk)_
- Telah memperbaiki berbagai bug dan menyempurnakan antarmuka pengguna _(Kiryl Kaveryn, Alexander Borsuk)_
- Ditambahkan dukungan untuk memilih suara navigasi yang sudah terpasang dan mendengarkan sampelnya _(Kiryl Kaveryn, Alexander Borsuk)_
- Fitur pencarian berdasarkan kategori di Spotlight telah dipulihkan _(Kiryl Kaveryn)_

### Android

- Ditambahkan pengaturan untuk mengoptimalkan urutan titik perhentian antara titik awal dan tujuan _(Mikhail Listratsenka)_
- Ditambahkan tombol untuk menambahkan atau mengganti titik perhentian dalam rute yang telah direncanakan _(Mikhail Listratsenka)_
- Ditambahkan fitur untuk menghentikan perekaman trek dan menyimpan trek tersebut dari notifikasi _(Alexander Borsuk)_
- Tombol “Tambah perhentian” kini menambahkan perhentian setelah perhentian yang sudah ada, sebelum tujuan _(Mikhail Listratsenka)_
- Peningkatan proses unggah dari editor OpenStreetMap _(Owm)_
- Desain antarmuka pengguna telah diperbarui _(Mikhail Listratsenka)_
- Editor penanda dan kotak dialog lainnya kini tetap terbuka selama navigasi _(Mikhail Listratsenka)_
- Perbaikan tampilan grafik ketinggian untuk trek datar dan pada antarmuka yang menggunakan arah kanan-ke-kiri _(Mikhail Listratsenka)_
- Masalah tombol peta yang terpotong oleh bilah sistem telah diperbaiki _(Mikhail Listratsenka)_
- Memperbaiki bug dan meningkatkan dukungan Android Auto _(Andrei Shkrob)_
- Telah diperbaiki masalah crash saat proses rendering peta _(Viktor Govako)_

### Desktop

- Nama file eksekusi desktop dan paket aplikasi macOS telah diubah menjadi `OrganicMaps` _(Alexander Borsuk)_
- Masalah pada aplikasi Windows telah diperbaiki _(Osyotr, Alexander Borsuk)_
- Argumen baris perintah `--lang` kini menggantikan pengaturan bahasa aplikasi _(Alexander Borsuk)_

Dengan penuh kegembiraan dan semangat,

Tim Organic Maps kamu

{{ <references lang /> }}
