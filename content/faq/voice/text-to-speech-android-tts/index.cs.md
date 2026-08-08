---
title: Převod textu na řeč v systému Android
slug: převod-textu-na-řeč-v-systému-android
description: Průvodce, jak zajistit, aby TTS fungovalo na Androidu
taxonomies:
  faq:
  - voice-directions
extra:
  order: 10
aliases:
  - /cs/faq/voice/text-to-speech-android-tts/
---

## Shrnutí

Organic Maps používá pro hlasové pokyny systém převodu textu na řeč (TTS). Výchozí motory se liší podle zařízení. Možnosti mohou zahrnovat převod textu na řeč Google, modul výrobce zařízení nebo modul třetí strany.

Oficiální doporučení od Organic Maps je [RHVoice](https://rhvoice.org/), což je bezplatný a otevřený zdroj řeči, který lze stáhnout z [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) a [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Pokyny

- Otevři na svém zařízení Android aplikaci Nastavení
- Vyber Další nastavení a poté vyber Usnadnění
- Vyber si preferovaný motor, rychlost řeči a výšku
- **Restartuj aplikaci Organic Maps**
- Otevři Nastavení => Hlasové pokyny v Organic Maps a nastav je
- Pokud hlas nefunguje, znovu spusť aplikaci Organic Maps (nebo restartuj zařízení).

Pokud nemůžeš najít příslušné nastavení, otevři aplikaci nastavení a vyhledej Převod textu na řeč.

P.S: Upozorňujeme, že tyto kroky se budou lišit v závislosti na značce telefonu, který používáš.

Uvedené možnosti se nemusí zobrazit, pokud v zařízení ještě nemáš nainstalované TTS. Chceš-li nainstalovat kterýkoli z nich, který podporuje tvůj rodný jazyk, podívej se do tabulky níže.

## Snímky obrazovky

|             |             |
| ----------- | ----------- |
![Nastavení](tts_config_1.png "Nastavení") | ![Přístupnost](tts_config_2.png "Přístupnost")

## Motory {#engines}

Níže je uveden úplný seznam několika motorů a jazyků, které podporují (odkazy ke stažení najdeš za tabulkou):

{{ tts_table() }}

## Řešení

Pokud máš potíže s inicializací enginu RHVoice TTS na LineageOS nebo jiných vlastních ROM, vyzkoušej toto řešení. RHVoice se nemusí správně inicializovat a aplikace může selhat, zejména pokud jsi v telefonu dosud nepoužil žádný modul TTS (např. nová instalace, obnovení továrního nastavení atd.). Pokud používáš vlastní ROM, jako je LineageOS <ins>bez služeb Google Play a Speech Services od společnosti Google</ins>, a chceš používat RHVoice jako preferovaný modul TTS, postupuj podle pokynů níže:

1. Nainstaluj [eSpeak TTS engine](https://f-droid.org/en/packages/com.reecedunn.espeak) dostupný na F-Droid
2. Nastav jej jako preferovaný systémový modul
    - Přejdi na hlavní **Nastavení** LineageOS.
    - Přejdi dolů na **Přístupnost**.
    - Vyber **výstup převodu textu na řeč** a **Preferovaný modul** (levá strana) a ujisti se, že je vybrána možnost **eSpeak**.
3. Vrať se a stiskni **přehrát**, abys zjistil, zda to funguje
4. Nainstaluj [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) dostupný na F-droid.
    - Otevři jej, vyber jazyk, který chceš použít, klepnutím na ikonu cloudu (zcela vlevo) stáhni hlasy.
    - Stisknutím tlačítka přehrávání ověř, zda funguje
5. Nastav **RHVoice** jako preferovaný motor (viz krok 2)
6. Nyní bys měl být schopen bez problémů používat RHVoice

## Testování

Chceš-li otestovat hlasové pokyny, můžeš klepnout na „Testovat hlasové pokyny (TTS, Text-To-Speech)“ v nabídce OM „Nastavení → Hlasové pokyny“ nebo můžeš skutečně spustit navigaci a přijímat jakýkoli hlasový výstup. Organic Maps ti neposkytne žádné hlasové pokyny, když budeš stát na místě.

![Test TTS](tts_test.png "Test TTS")
