---
title: Conversão de texto para fala no Android
slug: conversão-de-texto-para-fala-no-android
description: Guia sobre como fazer o TTS funcionar no Android
taxonomies:
  faq: ["instruções-de-voz"]
extra:
  order: 10
aliases:
  - /pt/faq/voice/text-to-speech-android-tts/
---

## Resumo

Organic Maps usa o mecanismo de conversão de texto em fala (TTS) do sistema para instruções de voz. Os mecanismos padrão variam de acordo com o dispositivo. As opções podem incluir Google Text-to Speech, mecanismo do fabricante do dispositivo ou de terceiros.

A recomendação oficial do Organic Maps é [RHVoice](https://rhvoice.org/), que é um mecanismo de fala gratuito e de código aberto que pode ser baixado do [Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) e [F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## Instruções

- Abre o aplicativo Configurações no teu dispositivo Android
- Seleciona Configurações adicionais e seleciona Acessibilidade
- Escolhe o teu mecanismo, velocidade de fala e tom preferidos
- **Reinicia o aplicativo Organic Maps**
- Abre Configurações => Instruções de voz no Organic Maps e configura-o
- Reinicia o aplicativo Organic Maps novamente (ou reinicia o dispositivo) se a voz não estiver funcionando

Se não conseguires encontrar a configuração relevante, abre o aplicativo de configurações e pesquisa Text-to-speech.

P.S: Observa que essas etapas variam de acordo com a marca do telefone que estás usando.

Essas opções podem não aparecer se ainda não tiveres um TTS instalado no teu dispositivo. Consulta a tabela abaixo para instalar qualquer um deles que suporte o teu idioma nativo.

## Capturas de tela

|             |             |
| ----------- | ----------- |
![Configurações](tts_config_1.png "Configurações") | ![Acessibilidade](tts_config_2.png "Acessibilidade")

## Motores {#engines}

Abaixo está uma lista abrangente mostrando vários mecanismos e os idiomas que eles suportam (links para download podem ser encontrados após a tabela):

{{ tts_table() }}

## Soluções alternativas

Se estiveres tendo problemas para inicializar o mecanismo RHVoice TTS no LineageOS ou em outras ROMs personalizadas, tenta esta solução alternativa. O RHVoice pode não inicializar corretamente e o aplicativo pode travar, especialmente se nunca usaste nenhum mecanismo TTS no teu telefone antes (por exemplo, nova instalação, redefinição de fábrica, etc.). Se estiveres usando uma ROM personalizada como LineageOS <ins>sem Google Play Services e Speech Services do Google</ins> e quiseres usar o RHVoice como o teu mecanismo TTS preferido, segue as instruções abaixo como solução alternativa:

1. Instala o [mecanismo eSpeak TTS](https://f-droid.org/en/packages/com.reecedunn.espeak) disponível no F-Droid
2. Define-o como o mecanismo de sistema preferido
    - Vai para **Configurações** principais do LineageOS.
    - Rola para baixo até **Acessibilidade**.
    - Seleciona **saída de conversão de texto em fala** e **mecanismo preferido** (lado esquerdo) e certifica-te de que **eSpeak** esteja selecionado.
3. Volta e pressiona **play** para ver se está funcionando
4. Instala o [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) disponível no F-droid.
    - Abre-o, seleciona o idioma que desejas usar, toca no ícone da nuvem (extrema esquerda) para baixar as vozes.
    - Pressiona o botão play para verificar se está funcionando
5. Define **RHVoice** como mecanismo preferido (consulta a etapa 2)
6. Agora poderás usar o RHVoice sem problemas

## Teste

Para testar as instruções de voz, podes tocar em «Testar instruções de voz (TTS, Text-To-Speech)» no menu OM «Configurações → Instruções de voz» ou podes realmente iniciar uma navegação para receber qualquer saída de voz. O Organic Maps não fornecerá instruções de voz enquanto estiveres parado.

![Teste TTS](tts_test.png "Teste TTS")
