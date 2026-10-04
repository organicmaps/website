---
title: "Eylül 2026 güncellemesinde rota optimizasyonu, geliştirilmiş alternatif rotalar, izleri tek tek gizleme ve dönemsel su alanları"
date: 2026-09-29
slug: "rota-optimizasyonu-alternatif-rotalar-izleri-tek-tek-gizleme-donemsel-su-alanlari-eylul-2026"
aliases: ["/tr/news/2026-09-29/coklu-secim-yer-imleri-izler-carplay-gosterge-paneli-izleri-gizleme-paylasim-baglantilari-agustos-2026/"]
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Yola çıkmaya hazır mısın? Eylül güncellemesi, geliştirilmiş alternatif rotalar, rota duraklarının sırasını optimize etmeye yarayan bir ayar, zaman zaman su bulunan alanlar için daha net işaretlemeler ve izleri tek tek gizlemeye yarayan bir göz simgesiyle birlikte pek çok başka düzeltme ve iyileştirme getiriyor (aşağıya bak).

Organic Maps uygulamasını <https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] veya [F-Droid][fdroid] üzerinden yükle veya güncelle.

Önceki güncellemelerimizi kaçırdıysan, [Haziran](@/news/2026-06-29/610/index.tr.md), [Temmuz](@/news/2026-07-23/620/index.tr.md) ve [Ağustos](@/news/2026-08-31/630/index.tr.md) aylarında yayımlanan özelliklere göz at. Bu güncellemeleri mümkün kılan katkı sağlayanlara ve kullanıcılarımıza teşekkürler!

## Organic Maps’i nasıl destekleyebilirsin

- Geliştirme çalışmalarını desteklemek ve harita barındırma masraflarını karşılamak için [bağış yap](@/donate/index.tr.md)
- [Görüşlerini gönder ve projeye katkıda bulun](@/contribute/index.tr.md)
- Beta testine katıl, yeni özellikleri erkenden dene ve [iOS][testflight], [Android][firebase] ve [masaüstü][flathub] sürümlerindeki sorunları bildir
- Bu haberi yay ve büyük teknoloji şirketlerinin haritalarına daha iyi bir alternatif oluşturmamıza yardımcı ol!

## Sürüm notları

### Harita

- 28 Eylül 2026 tarihi itibarıyla OpenStreetMap verileri
- 21 Eylül 2026 tarihi itibarıyla Vikipedi verileri
- Görünür harita alanı 180° meridyenini (±180° boylam) aştığında arama işlemlerinde yaşanan sorun giderildi _(Viktor Govako)_
- Zaman zaman su bulunan alanlar artık haritada kum için kullanılan desene benzer noktalı bir desenle gösteriliyor _(Alexander Borsuk)_
- Su rezervuarları artık harita daha fazla uzaklaştırıldığında da görülebiliyor _(Alexander Borsuk)_
- Su tünelleri artık haritada gösterilmiyor _(Alexander Borsuk)_
- Suzhou Metrosu istasyon ve giriş simgeleri düzeltildi _(Alexander Borsuk)_
- Metro haritası katmanında etiketlerin yerinden kaydığı nadir durumlar düzeltildi _(Viktor Govako)_

### Rota planlama ve navigasyon

- Alternatif rotalar ve tahmini varış saatleri iyileştirildi _(Alexander Borsuk, Viktor Govako)_
- Navigasyon rotayı yeniden hesapladığında, seçilen alternatif rota artık korunuyor _(Alexander Borsuk)_
- Rota duraklarının sırası artık uygulama yeniden başlatıldıktan sonra geri yükleniyor _(Kiryl Kaveryn)_

### Diğer iyileştirmeler

- Çalışma saatlerinde artık 12:00 yerine “Öğle”, 00:00 veya 24:00 yerine “Gece yarısı” gösteriliyor _(Alexander Borsuk)_
- Hatalar düzeltildi ve iz kaydı iyileştirildi _(Alexander Borsuk)_
- KMB dosyalarının içe aktarılması sorunu giderildi _(Alexander Borsuk)_
- Fransızca ve Asturyasça çeviriler düzeltildi _(Alexander Borsuk)_
- İngilizce metindeki bir yazım hatası düzeltildi _(Carl Morris)_

### iOS

- Tek tek izleri gizlemek için bir göz simgesi eklendi _(Kiryl Kaveryn)_
- Planlanmış bir rotada durak eklemek veya değiştirmek için düğmeler eklendi _(Kiryl Kaveryn)_
- Rotadaki ara durakların sırasını optimize etmek için bir ayar eklendi _(Kiryl Kaveryn)_
- Desteklenen araç baş üstü ekranlarına (HUD) ve CarPlay gösterge paneline manevra talimatları eklendi _(Kiryl Kaveryn)_
- CarPlay düğmeleri ve arama özelliği düzeltildi _(Alexander Borsuk)_
- Çeşitli hatalar düzeltildi ve kullanıcı arayüzü iyileştirildi _(Kiryl Kaveryn, Alexander Borsuk)_
- Yüklü bir navigasyon sesini seçme ve bir örneğini dinleme desteği eklendi _(Kiryl Kaveryn, Alexander Borsuk)_
- Spotlight’ta kategori araması yeniden etkinleştirildi _(Kiryl Kaveryn)_

### Android

- Rotadaki ara durakların sırasını optimize etmek için bir ayar eklendi _(Mikhail Listratsenka)_
- Planlanmış bir rotaya durak eklemek veya değiştirmek için düğmeler eklendi _(Mikhail Listratsenka)_
- Bildirimden iz kaydını durdurma ve izi kaydetme özelliği eklendi _(Alexander Borsuk)_
- “Ara nokta ekle” düğmesi artık mevcut duraklardan sonra ve varış noktasından önce bir durak ekliyor _(Mikhail Listratsenka)_
- OpenStreetMap düzenleyicisinden değişikliklerin yüklenmesi iyileştirildi _(Owm)_
- Kullanıcı arayüzü tasarımı güncellendi _(Mikhail Listratsenka)_
- Yer imi düzenleyicisi ve diğer iletişim kutuları artık navigasyon sırasında açık kalıyor _(Mikhail Listratsenka)_
- Yükseklik değişimi olmayan izlerde ve sağdan sola yerleşimli arayüzlerde yükseklik grafiğinin görüntülenmesi sorunu düzeltildi _(Mikhail Listratsenka)_
- Harita düğmelerinin sistem çubukları tarafından kesilmesi sorunu giderildi _(Mikhail Listratsenka)_
- Hatalar düzeltildi ve Android Auto desteği iyileştirildi _(Andrei Shkrob)_
- Harita işleme sırasında meydana gelen çökme sorunu düzeltildi _(Viktor Govako)_

### Masaüstü

- Masaüstü çalıştırılabilir dosyası ve macOS uygulama paketi `OrganicMaps` olarak yeniden adlandırıldı _(Alexander Borsuk)_
- Windows uygulamasındaki sorunlar giderildi _(Osyotr, Alexander Borsuk)_
- `--lang` komut satırı argümanı artık uygulamanın dil ayarını geçersiz kılıyor _(Alexander Borsuk)_

Sevinç ve coşkuyla,

Organic Maps ekibin

{{ <references lang /> }}
