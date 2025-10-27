---
title: "23 Ekim Sürümü: iOS'ta AB'de varsayılan navigasyon uygulaması olarak Organic Maps, Android'de yol levhalarının görüntülenmesi ve daha fazla iyileştirme ve düzeltme"
date: 2025-10-23T17:20:21+00:00
slug: "23-ekim-sürümü-organic-maps-varsayılan-navigasyon-uygulaması-ab-ios-yol-levhaları-android-iyileştirmeler-düzeltmeler"
taxonomies:
  news: ["Releases"]
---

23 Ekim sürümünde düzeltmeler ve iyileştirmelere odaklandık. Aşağıdaki ayrıntılı listeye göz atın.

Kaçıranlar için, [önceki 7 Ekim güncellemesi](https://organicmaps.app/news/2025-10-07/android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display/
) GeoJSON içe aktarma, kayıt izi istatistikleri, Android Auto'da hız sınırı görüntüleme, OSM açıklama etiketlerini görüntüleme (bunları görmek için arama kutusuna `?description` yazın), iOS'ta bir iz üzerinde yer imi kaydetme ve daha birçok iyileştirme ekledi.

## Tüm Platformlar

- 21 Ekim 2025'ten taze OpenStreetMap verileri (Viktor Govako)
- Haritada metro girişlerinin/çıkışlarının adlarını göster (Viktor Govako)
- Yeni POI türleri ve simgeleri: izleme istasyonları, trafik adacıkları, Kneipp su tedavisi tesisleri, minyatür demiryolları (Viktor Govako), açık hava stilinde kamp alanları, havaalanı terminalleri, kapalı oyun alanları, telekomünikasyon mağazaları, tekne kiralama tesisleri, kayma rampası tesisleri, güncellenmiş atık bertarafı ve çöp sahası simgeleri (David Martinez)
- Slovence uygulama arayüzü çevirileri (Alexander Borsuk) ve navigasyon için TTS sesli yönlendirme (Erik Bucik)
- Bazı cihazlarda/ekranlarda, şehir merkezlerindeki harita artık daha az dağınık (Viktor Govako)
- Yaya navigasyon modunda yürürken kötü pusula sensörlerinde harita dönüşleri düzeltildi (Viktor Govako)
- Bir nehir veya su yolu bölümü seçildikten sonra görüntülenen geliştirilmiş bilgiler (Viktor Govako)
- Tüm dillerde geliştirilmiş eş anlamlılarla daha iyi EV şarj istasyonu araması (Alexander Borsuk)
- Varyant seçiciler ile emoji araması düzeltildi (Alexander Borsuk)
- Bazı tam adres eşleşmesi sorguları için çok fazla arama sonucu görüntülenmesi düzeltildi (Viktor Govako)
- https://umap.openstreetmap.fr/ adresinden GeoJSON içe aktarma artık tüm meta verileri korumalıdır (Shubh Kesharwani)
- Yürüyüş Rotaları harita katmanı için işaretlenmiş yollar için ek renkler desteklenir (Viktor Govako)

## iOS

- AB kullanıcıları iOS Ayarları → Uygulamalar → Varsayılan Uygulamalar → Navigasyon bölümünde Organic Maps'i varsayılan navigasyon uygulaması olarak ayarlayabilir (Kiryl Kaveryn)
- Navigasyon modunda beyaz üzerine beyaz durum çubuğu düzeltildi (Kiryl Kaveryn)
- Navigasyonu Başlat düğmesi boyutu artırıldı (Kiryl Kaveryn)
- iPad'de rota planlarken boş alan kaldırıldı (Kiryl Kaveryn)
- Organic Maps sizden App Store'da değerlendirmenizi isteyebilir. İyi yorumlarınız ekibimizi motive ediyor!

## Android

- Yol levhaları artık navigasyon yönlendirmelerinde görünüyor (Andrei Shkrob)
- İz kaydetme bilgisi iyileştirmeleri (Kavi Khalique)
- Organic Maps bazı eski Intel x86 cihazlarda çalışıyor (Andrei Shkrob)
- Bazı durumlarda çalışmayan TTS sesli yönlendirmeler düzeltildi (Andrei Shkrob)
- Başlangıçta daha iyi açılış ekranı (Andrei Shkrob)

### Android Auto
- İptalden sonra rotayı geri yükle (Andrei Shkrob)
- Bazı cihazlarda çökmeler düzeltildi (Andrei Shkrob)

## Linux/Mac OS

- POI ayrıntıları artık "ad | ref" biçimini gösteriyor (Viktor Govako)
- karanlık mod otomatik olarak sistem ayarlarıyla senkronize oluyor (DeepChirp)

## Dipnotlar

Organic Maps mümkün ❤️ katkıda bulunanlarımız, [bağışlarınız](@/donate/index.tr.md) ve [desteğiniz](@/contribute/index.tr.md) sayesinde.

En son Organic Maps sürümünü [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ve [F-Droid][fdroid]'den edinin.

Not: Erken özellikler için beta testine katılın:
- [iOS][testflight]
- [Android][firebase].

Kullanıcılarımıza ve topluluğumuza sevgiyle
Organic Maps Ekibi

{{ references() }}
