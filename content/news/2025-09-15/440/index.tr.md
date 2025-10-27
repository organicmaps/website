---
title: "15 Eylül sürümü: yeni rota planlama ve OSM açıklamaları"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

Bu ikinci Eylül sürümü yeniden tasarlanmış bir rota planlama ekranı ve iOS’ta OpenStreetMap `description` etiket içeriğini görüntüleme özelliği getiriyor. Bu etikete sahip yerleri bulmak için aramaya `?description` yazın (`?wiki` gibi).

Ayrıca iOS ve Android için birçok düzeltme ve iyileştirme içerir (ayrıntılar aşağıda).

Kaçırmış olabileceğiniz yakın tarihli özellikler:
- Bir otobüs durağı seçerken toplu taşıma hat numaraları
- Yürüyüş ve bisiklet rotaları (sol üstteki Katmanlar düğmesiyle etkinleştirin)
- Haritada yer imi adlarını göster (Ayarlar’dan etkinleştirin)
- ✎ simgesi yer imlerini hızlıca düzenlemeyi sağlar

Organic Maps katkıcılar, [bağışlarınız](@/donate/index.tr.md) ve [desteğiniz](@/contribute/index.md) sayesinde mümkündür.

### Ayrıntılı sürüm notları

- 13 Eylül tarihli yeni OpenStreetMap verileri
- Dünya haritasından çok küçük adalar kaldırıldı (Viktor Govako)
- Adres ayrıntılarında posta kodu (ZIP) göster (Viktor Govako)
- Geçerli konuma yanlış odaklanma düzeltildi (Kiryl Kaveryn, Viktor Govako)
- GPX dışa/içe aktarırken yer imi renklerini koru (cyber-toad)
- Güncellenmiş çeviriler (Weblate katkıcıları)

#### Harita stilleri (Viktor Govako)

- Aydınlatma mağazalarını göster
- Elektrik hatlarını 18 yakınlaştırmadan itibaren göster
- Elektrik santrali ve trafo merkezi referans adlarını göster
- Gezinme modunda kamp ve karavan alanlarını göster
- Gezinme modunda ikincil yol rengini düzelt
- Ulusal park sınırlarını çiz
- 12 yakınlaştırmadan itibaren arkeolojik alanları Outdoor stilinde çiz

#### iOS

- YENİ: OSM `description` etiket içeriğini göster (ara `?description`) (Kiryl Kaveryn, Viktor Govako)
- YENİ: yeniden tasarlanmış rota planlama ekranı (Kiryl Kaveryn)

#### Android

- Android Auto’da yeni döner kavşak simgeleri (Andrei Shkrob)
- Seçilen yer iminin kategorisini göster (Alexander Borsuk)
- Bir yer imine uzaklığı gösterme gecikmesi düzeltildi (Alexander Borsuk)
- Yeniden yapılandırılmış koyu tema (Andrei Shkrob)
- Özel ROM’larda (örn. Lineage + MicroG) gezinmede konum güncelleme sorunu düzeltildi (Viktor Govako)
- Yer imleri için mavi kalem (düzenle) simgesi (Alexander Borsuk)
- Mekan bilgi önizlemesinin dikey yüksekliği azaltıldı (Alexander Borsuk)
- Önizlemeden kuzeye olan azimut açısı kaldırıldı (mavi oku dokunun) (Alexander Borsuk)

En son sürümü edinin: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Betaya katılın: [iOS][testflight] / [Android][firebase].

{{ references() }}
