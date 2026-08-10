---
title: "Temmuz 2026 güncellemesinde toplu taşıma, rota belirleme, arama ve yer imleri ile ilgili hata düzeltmeleri ve iyileştirmeler"
date: 2026-07-23
slug: "hata-duzeltmeleri-iyilestirmeler-toplu-tasima-rota-arama-yer-imleri-temmuz-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Belki de fark etmişsindir, Temmuz ayı Organic Maps güncellemesi yayınlandı. Güncellemeyi <https://get.omaps.org> adresinden veya [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ve [F-Droid][fdroid] mağazalarından indirebilirsin.

[Bağışların](@/donate/index.tr.md) ve [geri bildirimlerin](@/contribute/index.tr.md) sayesinde, Temmuz ayında hata düzeltmeleri ve iyileştirmelere odaklandık. Kaçırmış olma ihtimaline karşı, [önceki Haziran sürümünden](@/news/2026-06-29/610/index.tr.md) aşağıdaki özellikler de kullanıma sunulmuştur:
- Toplu taşıma rotaları (canlı sefer saatleri hazırlık aşamasındadır)
- Uydu görüntüleri
- Araba sürmek, yürüyüş yapmak ve bisiklete binmek için alternatif rotalar
- Android için yeni arama ve rota planlama arayüzü
- iOS’ta büyük erişilebilirlik yazı tipleri desteği

## Ayrıntılı değişiklik günlüğü

### Harita ve yerler

- OpenStreetMap verileri 14 Temmuz itibarıyla güncellendi
- [OpenStreetMap](https://www.openstreetmap.org)’e bildirilen notlar artık tüm caddenin veya bölgenin ortasına değil, tam olarak seçtiğin noktaya yerleştiriliyor _(Alexander Borsuk)_
- 180° antimeridyeni geçen bölgelerde haritaya dokunulduğunda yer seçimi iyileştirildi _(Viktor Govako)_
- Bir iz silindikten sonra iz yükseklik profillerinde artık güncel olmayan veya boş grafikler gösterilmiyor _(Kiryl Kaveryn)_

### Toplu taşıma

- Artık durak, aktarma ve istasyon adlarının etrafında, hem açık hem de koyu temalarda okunabilirliklerini korumak için beyaz bir çerçeve bulunuyor _(Viktor Govako)_
- Toplu taşıma rotası önizlemesini kapattığında metro katmanı doğru şekilde yeniden görüntüleniyor _(Mikhail Listratsenka)_

### Rota belirleme ve navigasyon

- Artık tüm alternatif rotalar için rota uyarıları (ücretli yollar, feribotlar, asfaltsız yollar, merdivenler vb.) gösterilmektedir _(Viktor Govako)_
- Rota oluşturulurken nadiren meydana gelen donma sorunu giderildi _(Viktor Govako)_
- Kısıtlı yollarda çıkmaz yolların ve başlangıç ile bitiş noktalarının daha iyi işlenmesi _(Viktor Govako)_
- Yanlış ve eksik dönüş talimatları düzeltildi _(Alexander Borsuk)_

### iOS

- Arama geçmişini saklamak istemiyorsan bu özelliği devre dışı bırakmana ve gizlemene olanak tanıyan yeni “Arama geçmişini kaydet” ayarı _(Kiryl Kaveryn)_
- Yer imlerini daha kolay silmek için yeni “Düzenle” düğmesi _(Kiryl Kaveryn)_
- Artık ekrandan ayrıldığında yer imleri otomatik olarak kaydediliyor _(Kiryl Kaveryn)_
- Renk paleti artık önceden tanımlanmış renkler sunuyor ve istediğin herhangi bir özel rengi seçmene olanak tanıyor _(Kiryl Kaveryn)_
- Kaydedilmiş bir izin yükseklik grafiğinin boş durumu iyileştirildi _(Kiryl Kaveryn)_
- “Başlat” düğmesinde gösterilen rota ilerleme durumu iyileştirildi _(Kiryl Kaveryn)_
- Rota duraklarının sırasını değiştirmek artık listenin yer değiştirmesine neden olmuyor _(Kiryl Kaveryn)_
- Diğer küçük arayüz iyileştirmeleri _(Kiryl Kaveryn)_

### Android

- Çalışma saatleri artık bölünmüş vardiyaları da gösteriyor (öğle molası gibi), bugünden başlayarak tüm haftayı ayrı bir kaydırma alanı olmadan gösteriyor _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Temizle ve sesli arama düğmelerinin birleştirildiği daha temiz bir arama çubuğu, artık yerinden kaymayan bir temizle simgesi ve yatay mod ile telefon döndürme için düzen düzeltmeleri _(Mikhail Listratsenka)_
- Yeniden tasarlanan yer imi ve iz düzenleyicisi _(Mikhail Listratsenka)_
- Rota planlamasına ilişkin düzeltmeler ve iyileştirmeler _(Mikhail Listratsenka)_
- Renk seçici artık otomatik olarak kapanıyor ve Android 5’te yaşanan çökme sorunu giderildi _(Mikhail Listratsenka)_
- Çökme sorunları giderildi _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop

- İndirilebilen haritaların listesi artık alfabetik sıraya göre düzenlenmiştir _(goncalo109560)_

### Çeviriler

- Çince ifadeler iyileştirildi _(Chenxi Zhao)_
- Ukraynaca çeviriler güncellendi _(Nnifria)_
- Harita bölge adlarının İtalyanca çevirileri düzeltildi _(Vittorio Bertola)_

## Yeni özellikleri erkenden denemek ve sorun bildirmek için beta testine katıl:

İpucu: Beta sürümünde yeni tepe gölgelendirmesi, fit ve metre birimlerini destekleyen geliştirilmiş yükseklik verileri ve diğer harika özellikler bulunuyor!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Mutlu yazlar!
Organic Maps Ekibi

{{ references() }}
