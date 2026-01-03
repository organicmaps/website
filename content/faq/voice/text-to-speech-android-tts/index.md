---
title: Text-to-Speech (TTS) and voice directions on Android
description: Guide on how to setup TTS voice directions on Android
slug: text-to-speech-tts-and-voice-directions-on-android
aliases:
  - /faq/voice/text-to-speech-android-tts/
taxonomies:
  faq: ["Voice Directions"]
extra:
  order: 10
---

## Summary

Organic Maps uses the system text-to-speech (TTS) engine for voice instructions. The default engines vary by device. The choices can include Google Text-to Speech, device manufacturer's engine or a third-party one.

The official recommendation from Organic Maps is [RHVoice](https://rhvoice.org/), which is a free and open source speech engine that can be downloaded from [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) and [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instructions

- Open the Settings app on your Android device
- Select Additional Settings and then select Accessibility
- Choose your preferred engine, speech rate and pitch
- **Restart Organic Maps app**
- Open Settings => Voice Instructions in Organic Maps and set it up
- Restart Organic Maps app again (or reboot the device) if the voice is not working

If you cannot find the relevant setting, open the settings app and search for Text-to-speech.

P.S: Do note that these steps will vary based on the phone brand you are using.

Said options may not appear if you don't have a TTS already installed on your device. Please refer to the table below to install any one of them that supports your native language.

## Screenshots

|             |             |
| ----------- | ----------- |
![Settings](tts_config_1.png "Settings") | ![Accessibility](tts_config_2.png "Accessibility")

## Engines {#engines}

Below is a comprehensive list showing several engines and the languages they support (download links can be found after the table):

{{ tts_table() }}

## Workarounds

If you’re having trouble initializing the RHVoice TTS engine on LineageOS or other custom ROMs, try this workaround. RHVoice may not initialize properly and the app may crash, especially if you haven’t used any TTS engine on your phone before (e.g., new installation, factory reset, etc.). If you’re using a custom ROM like LineageOS <ins>without Google Play services and Speech Services by Google</ins>, and you want to use RHVoice as your preferred TTS engine, follow the instructions below as a workaround:

1. Install the [eSpeak TTS engine](https://f-droid.org/en/packages/com.reecedunn.espeak) available on F-Droid
2. Set it as the preferred system engine
    - Go to LineageOS main **Settings**.
    - Scroll down to **Accessibility**.
    - Select **text-to-speech output** and **Preferred engine** (left side) and make sure **eSpeak** is selected.
3. Go back and press **play** to see if it is working
4. Install [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) available on F-droid.
    - Open it, select the language you want to use, tap on the cloud icon (far left) to download voices.
    - Press play button to verify if it is working
5. Set **RHVoice** as preferred engine (see step 2)
6. Now, you should be able to use RHVoice without any problems

## Testing

In order to test the voice instructions, you can tap on "Test Voice Directions (TTS, Text-To-Speech)" in OM "Settings → Voice Instructions" menu or you can actually start a navigation to receive any voice output. Organic Maps will not give you any voice instructions while you're standing still.

![TTS Test](tts_test.png "TTS Test")
