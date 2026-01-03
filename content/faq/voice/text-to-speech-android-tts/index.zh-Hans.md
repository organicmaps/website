---
title: Android 上的文本转语音
slug: android-上的文本转语音
description: 有关如何在 Android 上使用 TTS 的指南
taxonomies:
  faq: ["语音指导"]
extra:
  order: 10
aliases:
  - /zh-Hans/faq/voice/text-to-speech-android-tts/
---

## 总结

Organic Maps 使用系统文本转语音 (TTS) 引擎来执行语音指令。默认引擎因设备而异。这些选择可以包括 Google 文本转语音、设备制造商的引擎或第三方引擎。

Organic Maps官方推荐的是[RHVoice](https://rhvoice.org/)，这是一个免费开源的语音引擎，可以从[Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android)下载并[F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/)。

## 说明

- 打开 Android 设备上的“设置”应用
- 选择其他设置，然后选择辅助功能
- 选择您喜欢的引擎、语速和音调
- **重新启动有机地图应用程序**
- 打开有机地图中的设置 => 语音指令并进行设置
- 如果语音不起作用，请再次重新启动 Organic Maps 应用程序（或重新启动设备）

如果找不到相关设置，请打开设置应用程序并搜索文本转语音。

P.S：请注意，这些步骤会根据您使用的手机品牌而有所不同。

如果您的设备上尚未安装 TTS，则可能不会显示上述选项。请参阅下表安装其中任何一个支持您的母语的软件。

## 截图

|             |             |
| ----------- | ----------- |
![设置](tts_config_1.png "设置") | ![辅助功能](tts_config_2.png "辅助功能")

## 引擎 {#engines}

下面是一个完整的列表，显示了几种引擎及其支持的语言（下载链接可以在表后面找到）：

{{ tts_table() }}

## 解决方法

如果您在 LineageOS 或其他自定义 ROM 上初始化 RHVoice TTS 引擎时遇到问题，请尝试此解决方法。 RHVoice 可能无法正确初始化，并且应用程序可能会崩溃，特别是如果您之前没有在手机上使用过任何 TTS 引擎（例如，新安装、恢复出厂设置等）。如果您使用的是 LineageOS 等自定义 ROM，<ins>没有 Google Play 服务和 Google 语音服务</ins>，并且希望使用 RHVoice 作为首选 TTS 引擎，请按照以下说明作为解决方法：

1. 安装 F-Droid 上可用的 [eSpeak TTS 引擎](https://f-droid.org/en/packages/com.reecedunn.espeak)
2.将其设置为首选系统引擎
    - 转到 LineageOS 主 **设置**。
    - 向下滚动到**辅助功能**。
    - 选择 **文本转语音输出** 和 **首选引擎**（左侧），并确保选择 **eSpeak**。
3.返回并按**播放**查看是否正常工作
4. 安装 F-droid 上可用的 [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/)。
    - 打开它，选择您要使用的语言，点击云图标（最左侧）下载语音。
    - 按播放按钮验证其是否正常工作
5. 将 **RHVoice** 设置为首选引擎（参见步骤 2）
6. 现在，您应该可以毫无问题地使用 RHVoice

## 测试

为了测试语音指令，您可以点击 OM“设置 → 语音指令”菜单中的“测试语音指令（TTS、文本转语音）”，或者您可以实际启动导航以接收任何语音输出。当您站立不动时，有机地图不会给您任何语音指示。

![TTS 测试](tts_test.png "TTS 测试")
