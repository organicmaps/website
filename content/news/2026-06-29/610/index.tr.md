---
title: "Uydu görüntüleri, toplu taşıma rotaları, alternatif rotalar, Android için yeni arama ve rota planlama arayüzü, iOS için büyük erişilebilirlik yazı tipleri desteği ve Haziran 2026 güncellemesinde daha fazlası"
date: 2026-06-29
slug: "uydu-goruntuleri-toplu-tasima-rotalari-alternatif-rotalar-yeni-arama-rota-planlama-android-buyuk-yazi-tipleri-ios-haziran-2026"
taxonomies:
  news: ["releases"]
---

Organic Maps Haziran güncellemesinde denemen için birçok heyecan verici yeni özellik ve hata düzeltmesi var, bunlar arasında:
- Uydu görüntüleri
- Toplu taşıma rotaları
- Alternatif rotalar
- Android için yeni arama ve rota planlama arayüzü
- iOS için büyük erişilebilirlik yazı tipleri desteği

Güncellemeyi <https://get.omaps.org> adresinden veya [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ve [F-Droid][fdroid] üzerinden al ve ne düşündüğünü bize söyle!

## Ayrıntılı değişiklik günlüğü

- YENİ! Metro, hafif raylı sistem, otobüs ve tramvayla toplu taşıma rota planlama _(Viktor Govako)_
- YENİ! Alternatif rotalar: en hızlı rotaya ek olarak uygulama artık en kısa rotayı da gösteriyor _(Viktor Govako)_
- YENİ! Yürüyüş ve bisiklet rotalarında yol üzerindeki basamaklar, kapılar ve bariyerler için uyarılar _(Viktor Govako)_
- YENİ! Yer imleri için istediğin rengi seç _(Alexander Borsuk, Mikhail Listratsenka)_
- YENİ! British National Grid (OS Grid), Irish Grid ve Irish Transverse Mercator (ITM) koordinatları desteği _(Alexander Borsuk)_
- DENEYSEL: Organic Maps ayarlarında özel bir raster karo sunucusu URL’siyle uydu görüntülerini etkinleştir. Kendi sunucumuz üzerinde hâlâ çalışıyoruz, bu nedenle URL’sinde `{x}`, `{y}`, `{z}` yer tutucuları bulunan herkese açık bir sunucu bulmanı rica ediyoruz _(Viktor Govako, renderexpert)_
- OpenStreetMap verileri 24 Haziran itibarıyla güncellendi _(Viktor Govako)_
- Wikipedia verileri, İtalyanca makaleler dahil, 20 Haziran itibarıyla güncellendi _(Alexander Borsuk)_
- Organic Maps harita indirme sunucularını geçersiz kılmak için arama penceresine `?map-download-server:https://your-server.com/` yaz. Geçersiz kılmayı kaldırmak için `?no-map-download-server` yaz _(Alexander Borsuk)_

#### Harita çizimi ve stiller

- Plaj, kum, moloz yamaç, çıplak kaya, meyve bahçesi ve bağ alanları için daha güzel desenler; korunan alanlar ve sulak alanlar için taramalar _(Alexander Borsuk)_
- Yollar ve nehirler için daha pürüzsüz kavisli metin etiketleri _(Viktor Govako)_
- Nehirler, dereler ve sulak alanlar karanlık modda daha yüksek kontrasta sahip ve daha görünür _(Alexander Borsuk)_
- Kategori araması ve haritadaki arama sonuçları için yeni ve iyileştirilmiş simgeler _(Anton Makouski)_
- Çok dilli metin şekillendirme ve çizimi iyileştirildi _(Alexander Borsuk)_
- Çeşitli hata düzeltmeleri ve performans iyileştirmeleri _(Viktor Govako)_

#### İzler, yer imleri ve rotalar

- GeoJSON izleri artık içe ve dışa aktarılırken yükseklik ve zaman damgalarını koruyor _(Alexander Borsuk)_
- Bir izi başka bir listeye taşıdıktan sonra oluşan çökme düzeltildi _(Viktor Govako)_
- Miras alanları için web siteleri artık gösteriliyor _(Viktor Govako)_
- Adsız arama sonuçları için işletmeci adları artık gösteriliyor. Örneğin adsız bir ATM artık bankasını gösteriyor _(Anton Makouski)_
- Düzenleyici: apartman binalarıyla ilgili OpenStreetMap düzenlemeleri/changeset’leri için açıklama metni düzeltildi _(titanniya542-spec)_
- Yer imi ve iz açıklamalarında HTML algılama iyileştirildi _(Alexander Borsuk)_

### iOS

- YENİ! Dynamic Type ve büyük yazı tipleri için erişilebilirlik desteği _(Kiryl Kaveryn)_
- YENİ! Üst üste binen izler ve rotalar arasında seçim yapmak için dokun _(Kiryl Kaveryn)_
- Yer imi ve iz açıklamalarının HTML gösterimi iyileştirildi _(Kiryl Kaveryn)_
- Arayüzde daha temiz tablo stili _(Kiryl Kaveryn)_

### Android

- YENİ! Arama arayüzü _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- YENİ! Rota planlama arayüzü _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Yer imi ve iz açıklamalarının HTML gösterimi iyileştirildi _(Mikhail Listratsenka)_
- APK boyutu azaltıldı _(Alexander Borsuk)_
- Kullanılabilir metinden konuşmaya motoru yoksa ses simgesi devre dışı olarak gösteriliyor _(Mikhail Listratsenka)_
- Uzun yer imi ve iz açıklamaları artık “…daha fazla” düğmesi gösteriyor _(Mikhail Listratsenka)_
- Çeşitli arayüz düzeltmeleri ve döndürülen nokta kimlikleri için API düzeltmesi _(Mikhail Listratsenka)_

### Desktop

- Gösterilen koordinat sistemini değiştirme desteği _(Alexander Borsuk)_
- Seçili yerle ilgili bilgiler artık solda gösteriliyor _(Viktor Govako)_
- Bağlam menüsü konumu düzeltildi _(Osyotr)_
- Qt 6.4 ve önceki sürümlerde OpenStreetMap oturum açma ve düzenlemelerinin takılması düzeltildi _(Alexander Borsuk)_
- macOS’te rota sırasında beklenmeyen harita stili değişimi düzeltildi _(Alexander Borsuk)_
- KMZ dosyası dışa aktarıldıktan sonra macOS uygulaması kapatılırken oluşan çökme düzeltildi _(Alexander Borsuk)_

### Çeviriler

- Kantonca adım adım sesli yönlendirme _(Alexander Borsuk)_
- Almanca ve Fransızca çeviriler güncellendi _(Wuzzy, Alexander Borsuk)_
- Çince, Sırpça ve Katalanca için hatalı “onto street” sesli yönlendirme çevirileri düzeltildi _(Alexander Borsuk)_

## Erken özellikleri denemek ve sorun bildirmek için beta testine katıl:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Tüm kullanıcılarımıza ve katkıda bulunanlara, [bağış yapanlara](@/donate/index.tr.md) ve uygulama mağazalarında Organic Maps’e 5 yıldız verenlere minnettarız. Birlikte en iyi harita uygulamasını yapabiliriz!

Sevgilerle,
Organic Maps Ekibi

{{ references() }}
