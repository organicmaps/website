{% component tts_table(lang) -%}
{#- Rows are alphabetical. Engines within a row follow the order of the English (US) row;
    single-language engines (AhoTTS, Hebrew TTS, neurokone_app) come after the shared ones
    and before Supertonic and Offline Translator.
    An engine with one voice per language is listed on the primary row only: English (US),
    Spanish (ES), Portuguese (PT), French (FR), Dutch (NL), Mandarin (CN). One that ships
    separate regional voices, as Offline Translator does, is listed on every row it covers.
    eSpeak is left off rows whose voice cannot read a plain OSM name tag: ar, ja and chr
    need diacritics, kana or a fully annotated dictionary, and he_rules maps every unpointed
    Hebrew letter to a bare consonant. Also skipped are its accent variants that Android
    does not expose as separate locales (en-029, en-gb-x-*, fr-ch, ru-lv, vi-vn-x-*,
    fa-latn, hyw) and its fictional, historical and auxiliary constructed voices —
    Esperanto and Lojban are the two conlangs kept, from before this list.
    A row may name an engine whose support lands in its next release rather than the
    current one: Offline Translator adds Belarusian, which its catalogue does not list yet. -#}
<div class="tts-table">

{{ trans(key='language-word', lang=lang) }} | {{ trans(key='engines', lang=lang) }}
:--------------------|:----------------------------------------------------------
Afrikaans            | eSpeak
Albanian             | RHVoice, eSpeak, Offline Translator
Amharic              | eSpeak
Arabic               | Vocalizer, Acapela, Nuance, SherpaTTS, Supertonic, Offline Translator
Aragonese            | eSpeak
Armenian             | eSpeak
Assamese             | eSpeak
Azerbaijani          | eSpeak, Offline Translator
Bashkir              | eSpeak
Basque               | Vocalizer, Nuance, eSpeak, AhoTTS, Offline Translator
Belarusian           | RHVoice, eSpeak, Offline Translator
Bengali              | Vocalizer, Google, Nuance, eSpeak, SherpaTTS, TTSLexx, Offline Translator
Bhojpuri             | Vocalizer, Nuance
Bishnupriya Manipuri | eSpeak
Bosnian              | eSpeak, Offline Translator
Bulgarian            | Vocalizer, Nuance, eSpeak, SherpaTTS, Supertonic, Offline Translator
Burmese              | eSpeak
Cantonese            | Vocalizer, Google, Nuance, eSpeak, Offline Translator
Catalan              | Vocalizer, Acapela, Nuance, eSpeak, SherpaTTS, AhoTTS, Offline Translator
Chuvash              | eSpeak
Croatian             | Vocalizer, Nuance, RHVoice, eSpeak, SherpaTTS, Supertonic, Offline Translator
Czech                | Vocalizer, Acapela, Nuance, RHVoice, eSpeak, SherpaTTS, Supertonic, Offline Translator
Danish               | Vocalizer, Google, Acapela, Ivona, Nuance, eSpeak, SherpaTTS, Supertonic, Offline Translator
Dongbei              | Vocalizer
Dutch (BE)           | Vocalizer, Nuance, SherpaTTS, Offline Translator
Dutch (NL)           | Vocalizer, Google, Acapela, Ivona, Nuance, eSpeak, SherpaTTS, Supertonic, Offline Translator
English (AU)         | Vocalizer, Google, Acapela, Nuance, RHVoice
English (IE)         | Vocalizer, Nuance
English (IN)         | Vocalizer, Google, Acapela, Nuance
English (SCT)        | Vocalizer, Nuance, RHVoice, eSpeak
English (UK)         | Vocalizer, Google, Acapela, Yandex, RHVoice, eSpeak, SherpaTTS, Offline Translator
English (US)         | Vocalizer, Google, Acapela, Ivona, Yandex, Nuance, RHVoice, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
English (ZA)         | Vocalizer, Nuance
Esperanto            | RHVoice, eSpeak
Estonian             | eSpeak, SherpaTTS, neurokone_app, Supertonic, Offline Translator
Faroese              | Acapela
Farsi (Persian)      | Vocalizer, Nuance, eSpeak, SherpaTTS, Offline Translator
Finnish              | Vocalizer, Google, Acapela, Nuance, eSpeak, SherpaTTS, Supertonic, Offline Translator
French (BE)          | Vocalizer, eSpeak
French (CA)          | Vocalizer, Nuance
French (FR)          | Vocalizer, Google, Acapela, Ivona, Nuance, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
Galician             | Vocalizer, Nuance, AhoTTS, Offline Translator
Georgian             | RHVoice, eSpeak, SherpaTTS, Offline Translator
German               | Vocalizer, Google, Acapela, Ivona, Nuance, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
Greek                | Vocalizer, Acapela, Nuance, eSpeak, SherpaTTS, Supertonic, Offline Translator
Greenlandic          | eSpeak
Guarani              | eSpeak
Gujarati             | eSpeak, TTSLexx, Offline Translator
Haitian Creole       | eSpeak
Hakka                | eSpeak
Hawaiian             | eSpeak
Hebrew               | Vocalizer, Nuance, Hebrew TTS, Offline Translator
Hindi                | Vocalizer, Nuance, eSpeak, TTSLexx, Supertonic, Offline Translator
Hungarian            | Vocalizer, Google, Nuance, eSpeak, SherpaTTS, Supertonic, Offline Translator
Icelandic            | eSpeak, SherpaTTS, Offline Translator
Indonesian           | Vocalizer, Google, Nuance, eSpeak, TTSLexx, Supertonic, Offline Translator
Irish                | eSpeak, SherpaTTS
Italian              | Vocalizer, Google, Acapela, Ivona, Nuance, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
Japanese             | Vocalizer, Google, Acapela, Nuance, TTSLexx, Supertonic, Offline Translator
Kannada              | Vocalizer, Nuance, eSpeak, TTSLexx, Offline Translator
Kazakh               | eSpeak, SherpaTTS
K’iche’              | eSpeak
Konkani              | eSpeak
Korean               | Vocalizer, Google, Acapela, Nuance, eSpeak, TTSLexx, Supertonic, Offline Translator
Kurdish              | eSpeak
Kyrgyz               | RHVoice, eSpeak
Latgalian            | eSpeak
Latvian              | eSpeak, SherpaTTS, Supertonic, Offline Translator
Lithuanian           | eSpeak, SherpaTTS, Supertonic, Offline Translator
Lojban               | eSpeak
Lule Saami           | eSpeak
Luxembourgish        | eSpeak, SherpaTTS
Macedonian           | RHVoice, eSpeak
Malay                | Vocalizer, Nuance, eSpeak, Offline Translator
Malayalam            | eSpeak, TTSLexx, Offline Translator
Maltese              | eSpeak, SherpaTTS
Mandarin (CN)        | Vocalizer, Acapela, eSpeak, SherpaTTS, TTSLexx, Offline Translator
Mandarin (TW)        | Vocalizer, Google, Nuance, Offline Translator
Māori                | eSpeak
Marathi              | Vocalizer, Nuance, eSpeak, TTSLexx, Offline Translator
Nepali               | RHVoice, eSpeak, SherpaTTS
Nogai                | eSpeak
Norwegian            | Vocalizer, Google, Acapela, Ivona, Nuance, eSpeak, SherpaTTS, Offline Translator
Odia                 | eSpeak
Oromo                | eSpeak
Papiamento           | eSpeak
Polish               | Vocalizer, Google, Acapela, Ivona, Nuance, RHVoice, eSpeak, SherpaTTS, Supertonic, Offline Translator
Portuguese (BR)      | Vocalizer, RHVoice, eSpeak, SherpaTTS, Offline Translator
Portuguese (PT)      | Vocalizer, Google, Acapela, Ivona, Nuance, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
Punjabi              | eSpeak
Quechua              | eSpeak
Romanian             | Vocalizer, Ivona, Nuance, RHVoice, eSpeak, SherpaTTS, Supertonic, Offline Translator
Russian              | Vocalizer, Google, Acapela, Ivona, Yandex, RHVoice, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
Scottish Gaelic      | eSpeak
Serbian              | RHVoice, eSpeak, SherpaTTS, Offline Translator
Setswana             | RHVoice, eSpeak
Shaanxi              | Vocalizer
Shan                 | eSpeak
Shanghainese         | Vocalizer
Sichuanese           | Vocalizer
Sindhi               | eSpeak
Sinhala              | eSpeak
Slovak               | Vocalizer, Nuance, RHVoice, eSpeak, SherpaTTS, Supertonic, Offline Translator
Slovenian            | Vocalizer, eSpeak, SherpaTTS, Supertonic, Offline Translator
Spanish (AR)         | Vocalizer, Nuance, eSpeak, Offline Translator
Spanish (CL)         | Vocalizer, Nuance, eSpeak
Spanish (CO)         | Vocalizer, eSpeak
Spanish (ES)         | Vocalizer, Google, Acapela, Ivona, Nuance, RHVoice, eSpeak, SherpaTTS, TTSLexx, AhoTTS, Supertonic, Offline Translator
Spanish (MX)         | Vocalizer, eSpeak, SherpaTTS, Offline Translator
Swahili              | eSpeak, SherpaTTS, Offline Translator
Swedish              | Vocalizer, Ivona, Nuance, eSpeak, SherpaTTS, Supertonic, Offline Translator
Tagalog              | Offline Translator
Tamil                | Vocalizer, Nuance, eSpeak, TTSLexx, Offline Translator
Tatar                | RHVoice, eSpeak
Telugu               | Vocalizer, eSpeak, TTSLexx, Offline Translator
Thai                 | Vocalizer, Google, Nuance, eSpeak, TTSLexx, Offline Translator
Turkish              | Vocalizer, Google, Acapela, Ivona, Yandex, Nuance, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
Turkmen              | RHVoice, eSpeak
Ukrainian            | Vocalizer, Nuance, RHVoice, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
Urdu                 | eSpeak, TTSLexx, Offline Translator
Uyghur               | eSpeak, Offline Translator
Uzbek                | RHVoice, eSpeak
Valencian            | Vocalizer
Vietnamese           | Vocalizer, Nuance, RHVoice, eSpeak, SherpaTTS, TTSLexx, Supertonic, Offline Translator
Welsh (Cymraeg, GB)  | eSpeak, SherpaTTS

</div>

---

- [Acapela Voices TTS](https://play.google.com/store/apps/details?id=com.acapelagroup.android.tts)
- [AhoTTS](https://play.google.com/store/apps/details?id=com.aholab.ahottsandroid)
- [Amazon Ivona TTS](https://apkpure.com/ivona-text-to-speech-hq/com.ivona.tts/download)
- [eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak/)
- [Google Speech Services](https://play.google.com/store/apps/details?id=com.google.android.tts)
- [Hebrew TTS](https://play.google.com/store/apps/details?id=com.intu.hebrewtts)
- [neurokone_app TTS](https://github.com/TartuNLP/neurokone_app)
- [Offline Translator](https://f-droid.org/en/packages/dev.davidv.translator/)
- [RHVoice TTS](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android)
- [SherpaTTS](https://f-droid.org/en/packages/org.woheller69.ttsengine/)
- [Supertonic TTS](https://f-droid.org/en/packages/com.brahmadeo.supertonic.tts/)
- [TTSLexx](https://play.google.com/store/apps/details?id=sia.netttsengine.ttslexx)
- [Vocalizer (Code Factory)](https://play.google.com/store/apps/details?id=es.codefactory.vocalizertts)
- [Vocalizer 2 (Nuance)](https://nvda.ru/sintezatory-rechi-vocalizer-expressive2-dlja-nvda#)
- [Yandex SpeechKit TTS](https://4pda.to/forum/index.php?showtopic=200728&st=4200#download)
{%- endcomponent tts_table %}
