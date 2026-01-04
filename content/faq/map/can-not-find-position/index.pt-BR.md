---
title: "O aplicativo não consegue encontrar minha posição no mapa ou mostra uma localização incorreta"
slug: o-aplicativo-não-pode-determinar-minha-localização
description: "Guia de solução de problemas para resolver problemas com localização e posição atual do GPS no mapa para dispositivos iOS e Android"
updated: "2026-01-04"
taxonomies:
  faq: ["Mapa"]
extra:
  order: 10
aliases:
  - /pt-BR/faq/map/can-not-find-position/
---

Por favor, verifique se o seu dispositivo tem GPS e as configurações de localização estão ativadas.

**Android**

No seu dispositivo, abra Configurações → Localização. É melhor ligar o modo de alta precisão (GPS assistido, A-GPS).

Se tiver dificuldade em determinar a sua localização com o GPS, ative (desative, se ativada) o "Google Play Services" nas configurações da aplicação.

Nota: só pode ver se tiver o Google Play Services instalado (ativado) no seu dispositivo Android. Os serviços de reprodução do Google são usados para determinar a localização com mais precisão. Se você tiver problemas com a precisão da localização depois de desativar a opção, ative-a.

**iOS**

Se você é um usuário de iPhone ou iPad, Por favor, verifique as configurações do iOS → Privacidade → Serviços de localização. O compartilhamento de dados de geolocalização deve ser ativado para o Organic Maps.

**Notas:**

* Para evitar dados indesejados durante o roaming, você pode desativar todos os dados móveis, ativar um modo de voo ou desativar os dados móveis do Organic Maps nas configurações do dispositivo. Dispositivos Android e iOS podem usar GPS no modo de voo.

* Alguns dispositivos móveis não possuem receptores GPS integrados, como o iPod Touch, o iPad apenas com WiFi, o Kindle Fire Kindle HD 7 da Amazon e alguns tablets Android. Nesses dispositivos, nosso aplicativo mostrará sua localização aproximada, desde que você esteja conectado à Internet.

* Finalmente, por favor se lembre que determinar sua localização com GPS (com rede Wi-Fi e rede móvel desligados) pode demorar algum tempo. Quanto mais tempo tiver decorrido desde a última vez que usou o GPS, mais tempo demora fazer uma nova localização. A velocidade de localização depende do dispositivo e não do aplicativo. A operação GPS também depende das condições metereológicas – funciona melhor em exterior e com o céu limpo. Os problemas surgem usando no interior de edifícios, numa rua estreita ladeada por prédios altos ou dentro de um veículo em movimento.



**Localização incorreta é mostrada no mapa**

1. Se houver um grande círculo semitransparente ao redor da seta de sua localização no mapa, isso significa que sua posição está sendo determinada com baixa precisão, usando conexão WiFi ou celular. Certifique-se de ter ativado a precisão de localização "Precisa" para o Organic Maps nas configurações do sistema e tente ir para fora, longe de edifícios altos e árvores, para melhorar a recepção do sinal de GPS via satélite.

2. Se sua posição for determinada incorretamente (por exemplo, você está em uma cidade, mas o aplicativo mostra outra cidade), é muito provável que você esteja em uma área afetada por um sinal de GPS falso (GPS spoofing) devido a medidas de guerra eletrônica (EW). Nesses casos, a única solução é mudar para outro local.