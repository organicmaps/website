---
title: Daha gelişmiş harita düzenlemeyi nasıl yapabilirim?
slug: daha-gelişmiş-harita-düzenlemeyi-nasıl-yapabilirim
description: ID, Go Map ve Vespucci gibi daha gelişmiş araçlarla OpenStreetMap'i düzenleme
  eğitimi
updated: '2024-06-20'
taxonomies:
  faq: ["harita-düzenleme"]
extra:
  order: 40
aliases:
  - /tr/faq/editing/advanced-map-editing/
---

Organic Maps, haritayı düzenlemek için kullanabileceğin basit ve kullanımı kolay bir düzenleyici içerir. Ancak düzenleyici sınırlıdır ve yalnızca basit nokta özellikleri eklemeye izin verir; bu, bina taslakları, yollar, göller, kasabalar vb. olmadığı anlamına gelir. Yerleşik düzenleyiciyle düzenlenemeyen bir şeyi değiştirmek istiyorsan, bu, okunacak doğru SSS sayfasıdır.

Organic Maps'te kullanılan tüm harita verileri [OpenStreetMap.org (OSM)](https://www.openstreetmap.org) adresinden geldiğinden, haritayı doğrudan buradan güncelleyebilirsin. Değişikliklerin bir sonraki harita güncellemesiyle birlikte Organic Maps'e dahil edilecektir.

## OpenStreetMap Düzenleyicileri

OSM'yi düzenlemek için çeşitli seçenekler vardır. Elinde bir dizüstü veya masaüstü bilgisayarın varsa, tarayıcında çalışan [ID Editor'ü](https://www.openstreetmap.org/edit) kullanmak daha iyidir. ID Editor yeni başlayanlar için kolaydır ve daha büyük bir ekran, fare ve klavye harita düzenlemeyi kolaylaştırır.

Mobil cihazdan gelişmiş harita düzenleme için iOS için [Haritaya Git](https://apps.apple.com/us/app/go-map/id592990211) veya Android için [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) kullan. Go Map yeni başlayanlar için kolaydır, Vespucci ise daha ileri düzey kullanıcıları hedefler. LearnOSM, [Haritaya Git](https://learnosm.org/en/mobile-mapping/gomap/) ve [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/) için eğitimler sağlar.

Daha eğlenceli ve daha basit düzenlemeler yapmak için iOS ve Android için [Every Door uygulamasını](https://every-door.app/) ve Android için [StreetComplete uygulamasını](https://streetcomplete.app/) deneyebilirsin.

#### ID Editor

OpenStreetMap'i ID ile düzenlemek için şu adımları izle:

1. Yeni bir hesap oluştur veya [OpenStreetMap.org](https://www.openstreetmap.org) adresinden oturum aç.
2. OpenStreetMap.org'da düzenlemek istediğin konuma göz at ve üstteki *Düzenle* seçeneğine tıkla
3. *İzlenecek Yolu başlatın* ve ID Editor'ü açıklayan kısa eğitimi izle
4. Haritayı düzenle
5. Değişikliklerini yükle

İşte bu, artık OSM topluluğunun bir parçasısın.

## Düzenlemelerime ne olacak?

*Yükle* tuşuna bastığında değişikliklerin anında genel OSM veritabanına eklenir. Bu nedenle düzenleme yaparken dikkatli ol. Organic Maps'te değişikliklerin bir sonraki aylık harita güncellemesinden sonra görünür olacaktır.

E-postan yayınlanmaz ancak OSM kullanıcı adını başkaları görebilir. OSM değişiklikleri tartışma olanağı sunduğundan, diğer OSM katılımcılarından düzenlemelerin hakkında sorular alabilirsin. Bu konuda OSM hesabını kaydederken kullandığın e-posta adresi aracılığıyla bilgilendirileceksin. OSM işbirliğine dayanan bir topluluk projesi olduğundan bu tür soruları her zaman yanıtlamalısın.

## Topluluk ve Wiki

OpenStreetMap bir topluluktur. Yardıma ihtiyacın varsa veya soruların varsa [OSM Forumunda](https://community.openstreetmap.org/c/help-and-support) sorabilirsin veya [OSM Wiki](https://wiki.openstreetmap.org/) belgelerine göz atabilirsin.

## Etiketler - OSM veri modeli nasıl çalışır?

OpenStreetMap veritabanı, gerçek dünyadaki özelliklerden soyutlayan Düğümler, Yollar, Alanlar ve İlişkiler gibi Nesneleri içerir. Bu Nesnelerin, onları daha ayrıntılı açıklamak için Etiketler adı verilen Nitelikleri vardır. Etiket bir Anahtar-Değer birleşimidir.

Bu, olduğundan daha karmaşık göründüğü için bir örnek vereceğiz:
Bir Restoran ör. `amenity=restaurant` Etiketi ile Not veya Alan olarak eşlenir. Daha sonra daha fazla ayrıntı için `cuisine=*` veya `opening_hours=*` gibi diğer Etiketler kullanılabilir.

> Yeni başlayanlara daha uygun olması için ID düzenleyicinin dahili veri yapısını kullanıcılardan gizlediğini unutma. Ancak Wiki belgelerini okumak için veri yapısına kısa bir genel bakış yararlı olacaktır.
ID Editor'de, *Düzenleme özelliği* yan panelindeki *Etiketler* bölümünü genişleterek ID'nin senden sakladığı Etiketleri görebilirsin.

## OSM Notları {#osm-note}

Zamanın yoksa veya sorun OSM verilerini kendin düzenleyemeyecek kadar karmaşıksa OSM Notları ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) gidilecek yoldur. Harita hatasının olduğu yere böyle bir not yerleştirip sorunu detaylı bir şekilde anlatabilirsin. Daha sonra diğer OSM gönüllüleri yardımcı olabilir ve sorunu çözebilir. Başka soruları olması veya OSM Notunun çözülmesi durumunda OSM hesabın aracılığıyla e-posta bildirimleri alacaksın.

1. Yeni bir hesap oluştur veya [OpenStreetMap.org](https://www.openstreetmap.org) adresinden oturum aç.
   > Ayrıca anonim Notlar'ı da açabilirsin, ancak sorun çözüldüğünde veya başka sorular olduğunda bildirim almayacağın için bu önerilmez.
2. [OpenStreetMap.org](https://www.openstreetmap.org) adresinde harita konumunu yakınlaştır ve *Haritaya not ekle* seçeneğine bas (sağ menüde alttan ikinci simge). Ardından mavi harita işaretçisini tam konuma sürükle.
   > Olabildiğince hassas olmaya çalış.
3. Harita sorununun ayrıntılı bir açıklamasını sağla ve *Not Ekle*'ye bas
   > Mağazalar için örn. adı ver ve orada nelerin satıldığını veya hangi hizmetlerin sunulduğunu belirt.
