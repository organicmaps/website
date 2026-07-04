---
title: "Citra satelit, rute transportasi umum, rute alternatif, antarmuka pencarian dan perencanaan rute baru untuk Android, dukungan font aksesibilitas besar untuk iOS, dan lainnya dalam pembaruan Juni 2026"
date: 2026-06-29
slug: "citra-satelit-rute-transportasi-umum-rute-alternatif-pencarian-perencanaan-rute-android-font-aksesibilitas-ios-juni-2026"
taxonomies:
  news: ["releases"]
---

Ada banyak fitur baru yang menarik dan perbaikan bug dalam pembaruan Organic Maps bulan Juni untuk dicoba, termasuk:
- Citra satelit
- Rute transportasi umum
- Rute alternatif
- Antarmuka pencarian dan perencanaan rute baru untuk Android
- Dukungan font aksesibilitas besar untuk iOS

Dapatkan di <https://get.omaps.org> atau di [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], dan [F-Droid][fdroid], dan beri tahu kami pendapatmu!

## Daftar perubahan terperinci

- BARU! Perencanaan rute transportasi umum dengan kereta bawah tanah, LRT, bus, dan trem _(Viktor Govako)_
- BARU! Rute alternatif: selain rute tercepat, aplikasi kini menampilkan rute terpendek _(Viktor Govako)_
- BARU! Peringatan rute berjalan kaki dan bersepeda tentang tangga, gerbang, dan palang di sepanjang jalan _(Viktor Govako)_
- BARU! Pilih warna apa pun untuk penanda _(Alexander Borsuk, Mikhail Listratsenka)_
- BARU! Dukungan untuk koordinat British National Grid (OS Grid), Irish Grid, dan Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EKSPERIMENTAL: aktifkan Citra Satelit di pengaturan Organic Maps dengan URL server tile raster khusus. Kami masih mengerjakan server sendiri, jadi silakan cari server yang tersedia secara terbuka dengan placeholder `{x}`, `{y}`, `{z}` di URL-nya _(Viktor Govako, renderexpert)_
- Data OpenStreetMap diperbarui per 24 Juni _(Viktor Govako)_
- Data Wikipedia diperbarui per 20 Juni, termasuk artikel dalam bahasa Italia _(Alexander Borsuk)_
- Ketik `?map-download-server:https://your-server.com/` di jendela pencarian untuk menimpa server unduhan peta Organic Maps. Ketik `?no-map-download-server` untuk menghapus penimpaan _(Alexander Borsuk)_

#### Rendering dan gaya peta

- Pola yang lebih menarik untuk area pantai, pasir, kerikil lereng, batu gundul, kebun buah, dan kebun anggur, ditambah arsiran area lindung dan lahan basah _(Alexander Borsuk)_
- Label teks melengkung yang lebih halus untuk jalan dan sungai _(Viktor Govako)_
- Sungai, aliran air, dan lahan basah memiliki kontras lebih tinggi dan lebih terlihat dalam mode gelap _(Alexander Borsuk)_
- Ikon baru dan lebih baik untuk pencarian kategori dan hasil pencarian di peta _(Anton Makouski)_
- Pembentukan dan rendering teks multibahasa ditingkatkan _(Alexander Borsuk)_
- Berbagai perbaikan bug dan peningkatan performa _(Viktor Govako)_

#### Trek, penanda, dan rute

- Trek GeoJSON kini menyimpan elevasi dan stempel waktu saat impor dan ekspor _(Alexander Borsuk)_
- Memperbaiki crash setelah memindahkan trek ke daftar lain _(Viktor Govako)_
- Situs web kini ditampilkan untuk situs warisan _(Viktor Govako)_
- Nama operator kini ditampilkan untuk hasil pencarian tanpa nama. Misalnya, ATM tanpa nama kini menampilkan banknya _(Anton Makouski)_
- Editor: memperbaiki teks deskripsi untuk suntingan/changeset OpenStreetMap pada gedung apartemen _(titanniya542-spec)_
- Deteksi HTML dalam deskripsi penanda dan trek ditingkatkan _(Alexander Borsuk)_

### iOS

- BARU! Dukungan aksesibilitas untuk Dynamic Type dan font besar _(Kiryl Kaveryn)_
- BARU! Ketuk untuk memilih antara trek dan rute yang bertumpuk _(Kiryl Kaveryn)_
- Rendering HTML deskripsi penanda dan trek ditingkatkan _(Kiryl Kaveryn)_
- Gaya tabel yang lebih rapi di UI _(Kiryl Kaveryn)_

### Android

- BARU! Antarmuka pencarian _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- BARU! Antarmuka perencanaan rute _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Rendering HTML deskripsi penanda dan trek ditingkatkan _(Mikhail Listratsenka)_
- Ukuran APK dikurangi _(Alexander Borsuk)_
- Ikon suara ditampilkan nonaktif saat tidak ada mesin text-to-speech yang tersedia _(Mikhail Listratsenka)_
- Deskripsi penanda dan trek yang panjang kini menampilkan tombol “…selengkapnya” _(Mikhail Listratsenka)_
- Berbagai perbaikan UI dan perbaikan API untuk ID titik yang dikembalikan _(Mikhail Listratsenka)_

### Desktop

- Dukungan untuk mengganti sistem koordinat yang ditampilkan _(Alexander Borsuk)_
- Informasi tentang tempat yang dipilih kini ditampilkan di sebelah kiri _(Viktor Govako)_
- Memperbaiki posisi menu konteks _(Osyotr)_
- Memperbaiki login dan penyuntingan OpenStreetMap yang macet pada Qt versi 6.4 dan sebelumnya _(Alexander Borsuk)_
- Memperbaiki pergantian gaya peta yang tidak terduga selama perutean di macOS _(Alexander Borsuk)_
- Memperbaiki crash saat menutup aplikasi macOS setelah mengekspor file KMZ _(Alexander Borsuk)_

### Terjemahan

- Panduan suara belokan demi belokan dalam bahasa Kanton _(Alexander Borsuk)_
- Terjemahan Jerman dan Prancis diperbarui _(Wuzzy, Alexander Borsuk)_
- Memperbaiki terjemahan panduan suara “onto street” yang salah untuk bahasa Tionghoa, Serbia, dan Katalan _(Alexander Borsuk)_

## Bergabunglah dengan pengujian beta untuk mencoba fitur awal dan melaporkan masalah:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Kami berterima kasih kepada semua pengguna dan kontributor kami, kepada mereka yang [berdonasi](@/donate/index.id.md) dan memberi Organic Maps 5 bintang di toko aplikasi. Bersama-sama kita dapat membangun aplikasi peta terbaik!

Dengan cinta,
Tim Organic Maps

{{ references() }}
