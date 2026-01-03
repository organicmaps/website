---
title: Daha gelişmiş harita düzenlemeyi nasıl yapabilirim?
slug: daha-gelişmiş-harita-düzenlemeyi-nasıl-yapabilirim
description: ID, Go Map ve Vespucci gibi daha gelişmiş araçlarla OpenStreetMap'i düzenleme
  eğitimi
updated: '2024-06-20'
taxonomies:
  faq: ["Harita düzenleme"]
extra:
  order: 40
aliases:
  - /tr/faq/editing/advanced-map-editing/
---

Organik Haritalar, haritayı düzenlemek için kullanabileceğiniz basit ve kullanımı kolay bir düzenleyici içerir. Ancak düzenleyici sınırlıdır ve yalnızca basit nokta özellikleri eklemeye izin verir; bu, bina taslakları, yollar, göller, kasabalar vb. olmadığı anlamına gelir. Yerleşik düzenleyiciyle düzenlenemeyen bir şeyi değiştirmek istiyorsanız, bu, okunacak doğru SSS sayfasıdır.

Organik Haritalar'da kullanılan tüm harita verileri [OpenStreetMap.org (OSM)](https://www.openstreetmap.org) adresinden geldiğinden, haritayı doğrudan buradan güncelleyebilirsiniz. Değişiklikleriniz bir sonraki harita güncellemesiyle birlikte Organik Haritalara dahil edilecektir.

## OpenStreetMap Düzenleyicileri

OSM'yi düzenlemek için çeşitli seçenekler vardır. Elinizde bir dizüstü veya masaüstü bilgisayarınız varsa, tarayıcınızda çalışan [Kimlik Düzenleyiciyi](https://www.openstreetmap.org/edit) kullanmak daha iyidir. Kimlik Düzenleyici yeni başlayanlar için kolaydır ve daha büyük bir ekran, fare ve klavye harita düzenlemeyi kolaylaştırır.

Mobil cihazdan gelişmiş harita düzenleme için iOS için [Haritaya Git](https://apps.apple.com/us/app/go-map/id592990211) veya Android için [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) kullanın. Go Map yeni başlayanlar için kolaydır, Vespucci ise daha ileri düzey kullanıcıları hedefler. LearnOSM, [Haritaya Git](https://learnosm.org/en/mobile-mapping/gomap/) ve [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/) için eğitimler sağlar.

Daha eğlenceli ve daha basit düzenlemeler yapmak için iOS ve Android için [Every Door uygulamasını](https://every-door.app/) ve Android için [StreetComplete uygulamasını](https://streetcomplete.app/) deneyebilirsiniz.

#### Kimlik Düzenleyici

OpenStreetMap'i kimlikle düzenlemek için şu adımları izleyin:

1. Yeni bir hesap oluşturun veya [OpenStreetMap.org](https://www.openstreetmap.org) adresinden oturum açın.
2. OpenStreetMap.org'da düzenlemek istediğiniz konuma göz atın ve üstteki *Düzenle* seçeneğine tıklayın
3. *İzlenecek Yolu başlatın* ve Kimlik Düzenleyiciyi açıklayan kısa eğitimi izleyin
4. Haritayı düzenleyin
5. Değişikliklerinizi yükleyin

İşte bu, artık OSM topluluğunun bir parçasısınız.

## Düzenlemelerime ne olacak?

*Yükle* tuşuna bastığınızda değişiklikleriniz anında genel OSM veritabanına eklenir. Bu nedenle düzenleme yaparken dikkatli olun. Organik Haritalar'da değişiklikleriniz bir sonraki aylık harita güncellemesinden sonra görünür olacaktır.

E-postanız yayınlanmaz ancak OSM kullanıcı adınızı başkaları görebilir. OSM değişiklikleri tartışma olanağı sunduğundan, diğer OSM katılımcılarından düzenlemeleriniz hakkında sorular alabilirsiniz. Bu konuda OSM hesabınızı kaydederken kullandığınız e-posta adresi aracılığıyla bilgilendirileceksiniz. OSM işbirliğine dayanan bir topluluk projesi olduğundan bu tür soruları her zaman yanıtlamalısınız.

## Topluluk ve Wiki

OpenStreetMap bir topluluktur. Yardıma ihtiyacınız varsa veya sorularınız varsa [OSM Forumunda](https://community.openstreetmap.org/c/help-and-support) sorabilirsiniz veya [OSM Wiki](https://wiki.openstreetmap.org/) belgelerine göz atabilirsiniz.

## Etiketler - OSM veri modeli nasıl çalışır?

OpenStreetMap veritabanı, gerçek dünyadaki özelliklerden soyutlayan Düğümler, Yollar, Alanlar ve İlişkiler gibi Nesneleri içerir. Bu Nesnelerin, onları daha ayrıntılı açıklamak için Etiketler adı verilen Nitelikleri vardır. Etiket bir Anahtar-Değer birleşimidir.

Bu, olduğundan daha karmaşık göründüğü için bir örnek vereceğiz:
Bir Restoran ör. ``` amenity=restoran``` Etiketi ile Not veya Alan olarak eşlenir. Daha sonra daha fazla ayrıntı için ```cousine=*``` veya ```opening_hours=*``` gibi diğer Etiketler kullanılabilir.

> Yeni başlayanlara daha uygun olması için kimlik düzenleyicinin dahili veri yapısını kullanıcılardan gizlediğini unutmayın. Ancak Wiki belgelerini okumak için veri yapısına kısa bir genel bakış yararlı olacaktır.
Kimlik Düzenleyicide, *Düzenleme özelliği* yan panelindeki *Etiketler* bölümünü genişleterek kimliğin sizden sakladığı Etiketleri görebilirsiniz.

## OSM Notları {#osm-note}

Zamanınız yoksa veya sorun OSM verilerini kendiniz düzenleyemeyecek kadar karmaşıksa OSM Notları ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) gidilecek yoldur. Harita hatasının olduğu yere böyle bir not yerleştirip sorunu detaylı bir şekilde anlatabilirsiniz. Daha sonra diğer OSM gönüllüleri yardımcı olabilir ve sorunu çözebilir. Başka soruları olması veya OSM Notunun çözülmesi durumunda OSM hesabınız aracılığıyla e-posta bildirimleri alacaksınız.

1. Yeni bir hesap oluşturun veya [OpenStreetMap.org](https://www.openstreetmap.org) adresinden oturum açın.
   > Ayrıca anonim Notlar'ı da açabilirsiniz, ancak sorun çözüldüğünde veya başka sorular olduğunda bildirim almayacağınız için bu önerilmez.
2. [OpenStreetMap.org](https://www.openstreetmap.org) adresinde harita konumunu yakınlaştırın ve *Haritaya not ekle* seçeneğine basın (sağ menüde alttan ikinci simge). Ardından mavi harita işaretçisini tam konuma sürükleyin.
   > Olabildiğince hassas olmaya çalışın.
3. Harita sorununun ayrıntılı bir açıklamasını sağlayın ve *Not Ekle*'ye basın
   > Mağazalar için örn. adı verin ve orada nelerin satıldığını veya hangi hizmetlerin sunulduğunu belirtin.
