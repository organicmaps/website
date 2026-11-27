{% component tts_table(lang) -%}
{% set languages = load_data(path="templates/shortcodes/tts_languages.toml") -%}
<div class="tts-table">

{{ trans(key='language-word', lang=lang) }} | {{ trans(key='engines', lang=lang) }}
:--------------------|:----------------------------------------------------------
{% for row in languages.rows -%}
{{ row | get(key=lang, default=row.en) }} | {{ row.engines }}
{% endfor %}

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
- [RuVoice TTS](https://github.com/kost-t-human/ruvoice-tts/releases/)
- [SherpaTTS](https://f-droid.org/en/packages/org.woheller69.ttsengine/)
- [Supertonic TTS](https://f-droid.org/en/packages/com.brahmadeo.supertonic.tts/)
- [TTSLexx](https://play.google.com/store/apps/details?id=sia.netttsengine.ttslexx)
- [Vocalizer (Code Factory)](https://play.google.com/store/apps/details?id=es.codefactory.vocalizertts)
- [Vocalizer 2 (Nuance)](https://nvda.ru/sintezatory-rechi-vocalizer-expressive2-dlja-nvda#)
- [Yandex SpeechKit TTS](https://4pda.to/forum/index.php?showtopic=200728&st=4200#download)
{%- endcomponent tts_table %}
