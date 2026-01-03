---
title: Android'de Metinden Konuşmaya
description: TTS'nin Android'de nasıl çalışacağına ilişkin kılavuz
taxonomies:
  faq: ["Sesli Yönlendirme"]
extra:
  order: 10
---

## Özet

Organik Haritalar, sesli talimatlar için sistemin metinden konuşmaya (TTS) motorunu kullanır. Varsayılan motorlar cihaza göre değişir. Seçenekler Google Metin-Konuşma, cihaz üreticisinin motoru veya üçüncü taraf motorunu içerebilir.

Organik Haritalar'ın resmi önerisi, [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) adresinden indirilebilen ücretsiz ve açık kaynaklı bir konuşma motoru olan [RHVoice](https://rhvoice.org/)'dur ve [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Talimatlar

- Android cihazınızda Ayarlar uygulamasını açın
- Ek Ayarlar'ı ve ardından Erişilebilirlik'i seçin
- Tercih ettiğiniz motoru, konuşma hızını ve perdesini seçin
- **Organik Haritalar uygulamasını yeniden başlatın**
- Organik Haritalar'da Ayarlar => Sesli Talimatlar'ı açın ve kurun
- Ses çalışmıyorsa Organik Haritalar uygulamasını yeniden başlatın (veya cihazı yeniden başlatın)

İlgili ayarı bulamıyorsanız ayarlar uygulamasını açın ve Metinden konuşmaya arama yapın.

Not: Bu adımların kullandığınız telefon markasına göre değişeceğini unutmayın.

Cihazınızda önceden bir TTS kurulu değilse söz konusu seçenekler görünmeyebilir. Ana dilinizi destekleyen herhangi birini yüklemek için lütfen aşağıdaki tabloya bakın.

## Ekran görüntüleri

|             |             |
| ----------- | ----------- |
![Ayarlar](tts_config_1.png "Ayarlar") | ![Erişilebilirlik](tts_config_2.png "Erişilebilirlik")

## Motorlar {#motorlar}

Aşağıda çeşitli motorları ve destekledikleri dilleri gösteren kapsamlı bir liste bulunmaktadır (indirme bağlantıları tablodan sonra bulunabilir):

{{ tts_table() }}

## Geçici Çözümler

RHVoice TTS motorunu LineageOS veya diğer özel ROM'larda başlatma konusunda sorun yaşıyorsanız bu geçici çözümü deneyin. Özellikle telefonunuzda daha önce herhangi bir TTS motoru kullanmadıysanız (ör. yeni kurulum, fabrika ayarlarına sıfırlama vb.) RHVoice düzgün şekilde başlatılamayabilir ve uygulama çökebilir. <ins>Google Play hizmetleri ve Google Konuşma Hizmetleri olmadan</ins> LineageOS gibi özel bir ROM kullanıyorsanız ve tercih ettiğiniz TTS motoru olarak RHVoice'u kullanmak istiyorsanız, geçici çözüm olarak aşağıdaki talimatları izleyin:

1. F-Droid'de bulunan [eSpeak TTS motorunu](https://f-droid.org/en/packages/com.reecedunn.espeak) yükleyin
2. Tercih edilen sistem motoru olarak ayarlayın
    - LineageOS ana **Ayarlar**'a gidin.
    - **Erişilebilirlik** seçeneğine ilerleyin.
    - **metinden konuşmaya çıkışı** ve **Tercih edilen motor**'u (sol taraf) seçin ve **eSpeak**'in seçildiğinden emin olun.
3. Geri dönün ve çalışıp çalışmadığını görmek için **oynat**'a basın
4. F-droid'de bulunan [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) uygulamasını yükleyin.
    - Açın, kullanmak istediğiniz dili seçin, sesleri indirmek için bulut simgesine (en soldaki) dokunun.
    - Çalışıp çalışmadığını doğrulamak için oynat düğmesine basın
5. **RHVoice**'u tercih edilen motor olarak ayarlayın (bkz. adım 2)
6. Artık RHVoice'u sorunsuz bir şekilde kullanabilmelisiniz

## Test etme

Sesli talimatları test etmek için OM "Ayarlar → Sesli Talimatlar" menüsünde "Sesli Yönleri Test Et (TTS, Metinden Konuşmaya)" seçeneğine dokunabilir veya herhangi bir ses çıkışı almak için gerçekten bir navigasyon başlatabilirsiniz. Organik Haritalar siz hareketsiz dururken size herhangi bir sesli talimat vermez.

![TTS Testi](tts_test.png "TTS Testi")
