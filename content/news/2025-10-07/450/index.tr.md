---
title: "7 Ekim sürümü: Android Auto hız sınırları, GeoJSON içe aktarma, iz kaydı istatistikleri, OSM açıklama etiketi gösterimi, iOS'ta seçili izin üzerine yer imi kaydetme ve daha fazlası"
date: 2025-10-07T10:00:00+00:00
taxonomies:
  news: ["releases"]
---

Bu 7 Ekim Organic Maps güncellemesi Android Auto'ya hız sınırı gösterimini, GeoJSON içe aktarmayı ve iz kaydı istatistiklerini ekliyor, OSM açıklama etiketlerini gösteriyor (görmek için arama kutusuna `?description` yaz) ve iOS'ta bir izin üzerine yer imi kaydediyor. Ayrıca tüm platformlarda kullanıcı arayüzünde ve OpenStreetMap düzenlemesinde birçok iyileştirme ile bazı Android cihazlarda açılışta yaşanan çökmenin düzeltilmesi dahil çeşitli hata düzeltmeleri var.

Organic Maps katkıcılarımız, [bağışların](@/donate/index.tr.md) ve [desteğin](@/contribute/index.tr.md) sayesinde ❤️ mümkün oluyor.

### Ayrıntılı sürüm notları (önceki küçük güncellemenin değişiklikleri dahil)

- YENİ! GeoJSON içe aktarma (Sergiy Kozyr)
- 4 Ekim tarihli OpenStreetMap verileri
- 1 Ekim tarihli Wikipedia verileri
- Toplu taşıma için Seattle hafif raylı sistem desteği (tjasz)
- Düzenlenen bir OSM mekanı kaydedilirken harita seçimi artık kaldırılmıyor (Kiryl Kaveryn)
- Güncellenmiş çeviriler (Weblate katkıcıları)

#### Harita stilleri

- amenity=bicycle + rental=shop olarak etiketlenmiş bisiklet kiralama dükkanlarını göster (David Martinez)
- Outdoor stilinde arkeolojik alanları 12, diğer tarihi alanları 15 yakınlaştırmadan itibaren göster (Viktor Govako)
- Outdoors stilinde direkler, iletişim ve elektrik kuleleri için yeni simgeler (David Martinez)
- Outdoors stilinde zirve simgesinin boyutu büyütüldü (David Martinez)
- Eksik POI simge çeşitleri eklendi (David Martinez)
- Daha fazla bariyer türü eklendi (Viktor Govako)

#### iOS

- YENİ: Seçili iz noktasına yer imi kaydet (Kiryl Kaveryn)
- YENİ: Kaydedilen izi önce kaydetmeden sil (Kiryl Kaveryn)
- Mekan Sayfasında çok satırlı yer imi listesi başlıkları göster (David Martinez)
- OSM giriş düğmelerinin stili güncellendi (Kiryl Kaveryn)
- Navigasyon bilgisi güncelleme sorunu düzeltildi (Kiryl Kaveryn)
- Yeni rota planlama sorunları düzeltildi (Kiryl Kaveryn)
- 3 aydan eski haritalarda OSM mekan ekleme/düzenleme görünürlüğü düzeltildi (Kiryl Kaveryn)
- iOS 26 için ulaşım seçenekleri segment denetiminin düzeni düzeltildi (Kiryl Kaveryn)
- Yer imi seçim animasyonları basitleştirildi (Kiryl Kaveryn)
- Arama sonucu seçme sorunu düzeltildi (Kiryl Kaveryn)
- Mekan Bilgi Sayfasının stili, kaydırması ve animasyonları düzeltildi (Kiryl Kaveryn)

#### Android Auto (yalnızca Google Play)

- YENİ: Android Auto'da hız sınırı gösterimi (Andrei Shkrob)
- Android Auto navigasyon modunda ekran değiştirme düzeltildi (Andrei Shkrob)
- Android Auto'da rota okunun kayması düzeltildi (Andrei Shkrob)
- Cihaz arabaya bağlandığında veya bağlantısı kesildiğinde oluşan sorun düzeltildi (Andrei Shkrob)
- Android Auto Konum Servisi eklendi (Andrei Shkrob)
- Android Auto rota simülatörü iyileştirildi (Viktor Govako)

#### Android

- YENİ: İz kaydı istatistiklerini gerçek zamanlı görüntüle (Kavi Khalique)
- YENİ: OSM `description` etiketinin içeriğini göster (Alexander Borsuk)
- Tema değişikliğinin işlenmesi düzeltildi (Andrei Shkrob)
- Açılıştaki çökme dahil birkaç çökme düzeltildi (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Sessiz indirme ilerlemesi bildirimleri (Viktor Govako)
- Kalem simgesinin iç boşluğu azaltıldı (Alexander Borsuk)

#### Masaüstü

- Linux'ta takılan curl düzeltildi (Alexander Borsuk)
- macOS'ta OSM'ye giriş yaparken oluşan takılma düzeltildi (Alexander Borsuk)
- Bağlam menüsünden nesne seçme eylemi (Viktor Govako)
- İndirmeyi iptal etme seçeneği (Viktor Govako)
- Bağlam menüsünde geometri türünü göster (Viktor Govako)

### Kaçırmış olabileceğin yakın tarihli özellikler

- Bir otobüs durağı seçerken toplu taşıma hat numaraları
- Yürüyüş ve bisiklet rotaları (sol üstteki Katmanlar düğmesiyle aç)
- Uygulama Ayarları'ndan etkinleştirerek yer imi adlarını haritada gör
- ✎ kalem simgesi yer imlerini hızlıca düzenlemeyi sağlar

### Organic Maps'i yükle

En son Organic Maps sürümünü şuralardan edin: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ve [F-Droid][fdroid].

Yeni özellikleri erken denemek için beta testine katıl: [iOS][testflight] / [Android][firebase].

{{ references() }}
