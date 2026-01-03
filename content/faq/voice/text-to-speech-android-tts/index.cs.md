---
title: Převod textu na řeč v systému Android
slug: převod-textu-na-řeč-v-systému-android
description: Průvodce, jak zajistit, aby TTS fungovalo na Androidu
taxonomies:
  faq:
  - Voice Directions
extra:
  order: 10
aliases:
  - /cs/faq/voice/text-to-speech-android-tts/
---

## Shrnutí

Organic Maps používá pro hlasové pokyny systém převodu textu na řeč (TTS). Výchozí motory se liší podle zařízení. Možnosti mohou zahrnovat převod textu na řeč Google, modul výrobce zařízení nebo modul třetí strany.

Oficiální doporučení od Organic Maps je [RHVoice](https://rhvoice.org/), což je bezplatný a otevřený zdroj řeči, který lze stáhnout z [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) a [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Pokyny

- Otevřete na svém zařízení Android aplikaci Nastavení
- Vyberte Další nastavení a poté vyberte Usnadnění
- Vyberte si preferovaný motor, rychlost řeči a výšku
- **Restartujte aplikaci Organické mapy**
- Otevřete Nastavení => Hlasové pokyny v Organických mapách a nastavte je
- Pokud hlas nefunguje, znovu spusťte aplikaci Organic Maps (nebo restartujte zařízení).

Pokud nemůžete najít příslušné nastavení, otevřete aplikaci nastavení a vyhledejte Převod textu na řeč.

P.S: Upozorňujeme, že tyto kroky se budou lišit v závislosti na značce telefonu, který používáte.

Uvedené možnosti se nemusí zobrazit, pokud v zařízení ještě nemáte nainstalované TTS. Chcete-li nainstalovat kterýkoli z nich, který podporuje váš rodný jazyk, podívejte se do tabulky níže.

## Snímky obrazovky

|             |             |
| ----------- | ----------- |
![Nastavení](tts_config_1.png "Nastavení") | ![Přístupnost](tts_config_2.png "Přístupnost")

## Motory {#engines}

Níže je uveden úplný seznam několika motorů a jazyků, které podporují (odkazy ke stažení naleznete za tabulkou):

{{ tts_table() }}

## Řešení

Pokud máte potíže s inicializací enginu RHVoice TTS na LineageOS nebo jiných vlastních ROM, vyzkoušejte toto řešení. RHVoice se nemusí správně inicializovat a aplikace může selhat, zejména pokud jste v telefonu dosud nepoužili žádný modul TTS (např. nová instalace, obnovení továrního nastavení atd.). Pokud používáte vlastní ROM, jako je LineageOS <ins>bez služeb Google Play a Speech Services od společnosti Google</ins>, a chcete používat RHVoice jako preferovaný modul TTS, postupujte podle pokynů níže:

1. Nainstalujte [eSpeak TTS engine](https://f-droid.org/en/packages/com.reecedunn.espeak) dostupný na F-Droid
2. Nastavte jej jako preferovaný systémový modul
    - Přejděte na hlavní **Nastavení** LineageOS.
    - Přejděte dolů na **Přístupnost**.
    - Vyberte **výstup převodu textu na řeč** a **Preferovaný modul** (levá strana) a ujistěte se, že je vybrána možnost **eSpeak**.
3. Vraťte se a stiskněte **přehrát**, abyste zjistili, zda to funguje
4. Nainstalujte [RHVoice] (https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) dostupný na F-droid.
    - Otevřete jej, vyberte jazyk, který chcete použít, klepnutím na ikonu cloudu (zcela vlevo) stáhněte hlasy.
    - Stisknutím tlačítka přehrávání ověřte, zda funguje
5. Nastavte **RHVoice** jako preferovaný motor (viz krok 2)
6. Nyní byste měli být schopni bez problémů používat RHVoice

## Testování

Chcete-li otestovat hlasové pokyny, můžete klepnout na „Testovat hlasové pokyny (TTS, Text-To-Speech)“ v nabídce OM „Nastavení → Hlasové pokyny“ nebo můžete skutečně spustit navigaci a přijímat jakýkoli hlasový výstup. Organické mapy vám neposkytnou žádné hlasové pokyny, když budete stát na místě.

![Test TTS](tts_test.png "Test TTS")
