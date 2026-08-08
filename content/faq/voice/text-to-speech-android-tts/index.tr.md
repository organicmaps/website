---
title: Android'de Metinden Konuşmaya
slug: androidde-metinden-konuşmaya
description: TTS'nin Android'de nasıl çalışacağına ilişkin kılavuz
taxonomies:
  faq: ["sesli-yönlendirme"]
extra:
  order: 10
aliases:
  - /tr/faq/voice/text-to-speech-android-tts/
---

## Özet

Organic Maps, sesli talimatlar için sistemin metinden konuşmaya (TTS) motorunu kullanır. Varsayılan motorlar cihaza göre değişir. Seçenekler Google Metin-Konuşma, cihaz üreticisinin motoru veya üçüncü taraf motorunu içerebilir.

Organic Maps'in resmi önerisi, [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) adresinden indirilebilen ücretsiz ve açık kaynaklı bir konuşma motoru olan [RHVoice](https://rhvoice.org/)'dur ve [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Talimatlar

- Android cihazında Ayarlar uygulamasını aç
- Ek Ayarlar'ı ve ardından Erişilebilirlik'i seç
- Tercih ettiğin motoru, konuşma hızını ve perdesini seç
- **Organic Maps uygulamasını yeniden başlat**
- Organic Maps'te Ayarlar => Sesli Talimatlar'ı aç ve kur
- Ses çalışmıyorsa Organic Maps uygulamasını yeniden başlat (veya cihazı yeniden başlat)

İlgili ayarı bulamıyorsan ayarlar uygulamasını aç ve Metinden konuşmaya arama yap.

Not: Bu adımların kullandığın telefon markasına göre değişeceğini unutma.

Cihazında önceden bir TTS kurulu değilse söz konusu seçenekler görünmeyebilir. Ana dilini destekleyen herhangi birini yüklemek için lütfen aşağıdaki tabloya bak.

## Ekran görüntüleri

|             |             |
| ----------- | ----------- |
![Ayarlar](tts_config_1.png "Ayarlar") | ![Erişilebilirlik](tts_config_2.png "Erişilebilirlik")

## Motorlar {#motorlar}

Aşağıda çeşitli motorları ve destekledikleri dilleri gösteren kapsamlı bir liste bulunmaktadır (indirme bağlantıları tablodan sonra bulunabilir):

{{ tts_table() }}

## Geçici Çözümler

RHVoice TTS motorunu LineageOS veya diğer özel ROM'larda başlatma konusunda sorun yaşıyorsan bu geçici çözümü dene. Özellikle telefonunda daha önce herhangi bir TTS motoru kullanmadıysan (ör. yeni kurulum, fabrika ayarlarına sıfırlama vb.) RHVoice düzgün şekilde başlatılamayabilir ve uygulama çökebilir. <ins>Google Play hizmetleri ve Google Konuşma Hizmetleri olmadan</ins> LineageOS gibi özel bir ROM kullanıyorsan ve tercih ettiğin TTS motoru olarak RHVoice'u kullanmak istiyorsan, geçici çözüm olarak aşağıdaki talimatları izle:

1. F-Droid'de bulunan [eSpeak TTS motorunu](https://f-droid.org/en/packages/com.reecedunn.espeak) yükle
2. Tercih edilen sistem motoru olarak ayarla
    - LineageOS ana **Ayarlar**'a git.
    - **Erişilebilirlik** seçeneğine ilerle.
    - **metinden konuşmaya çıkışı** ve **Tercih edilen motor**'u (sol taraf) seç ve **eSpeak**'in seçildiğinden emin ol.
3. Geri dön ve çalışıp çalışmadığını görmek için **oynat**'a bas
4. F-droid'de bulunan [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) uygulamasını yükle.
    - Aç, kullanmak istediğin dili seç, sesleri indirmek için bulut simgesine (en soldaki) dokun.
    - Çalışıp çalışmadığını doğrulamak için oynat düğmesine bas
5. **RHVoice**'u tercih edilen motor olarak ayarla (bkz. adım 2)
6. Artık RHVoice'u sorunsuz bir şekilde kullanabilmelisin

## Test etme

Sesli talimatları test etmek için OM "Ayarlar → Sesli Talimatlar" menüsünde "Sesli Yönleri Test Et (TTS, Metinden Konuşmaya)" seçeneğine dokunabilir veya herhangi bir ses çıkışı almak için gerçekten bir navigasyon başlatabilirsin. Organic Maps sen hareketsiz dururken sana herhangi bir sesli talimat vermez.

![TTS Testi](tts_test.png "TTS Testi")
