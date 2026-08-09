---
title: "A aplicação não consegue encontrar a minha posição no mapa ou mostra uma localização incorreta"
slug: a-aplicação-não-consegue-determinar-a-minha-localização
description: "Guia de resolução de problemas para resolver problemas com a localização e a posição GPS atual no mapa para dispositivos iOS e Android"
updated: "2026-01-04"
taxonomies:
  faq: ["mapa"]
extra:
  order: 10
aliases:
  - /pt/faq/map/can-not-find-position/
---

Por favor, verifica se o teu dispositivo tem GPS e as configurações de localização estão ativadas.

**Android**

No teu dispositivo, abre Configurações → Localização. É recomendável ligar o modo de alta precisão (GPS assistido ou A-GPS).

Se tiveres dificuldade em determinar a tua localização com o GPS, ativa (ou desativa, se já estiver ativado) o «Google Play Services» nas configurações da aplicação.

Nota: só podes usar a localização com maior precisão ver se tiveres o Google Play Services instalado (ativado) no teu dispositivo Android. Os serviços do Google são usados para determinar a localização com mais precisão. Se tiveres problemas com a precisão da localização depois de desativares a opção, ativa-a novamente.

**iOS**

Se tens um iPhone ou iPad, Por favor, verifica as configurações do iOS → Privacidade → Serviços de localização. A partilha de dados de geolocalização tem de ser ativada para o Organic Maps.

**Notas:**

* Para evitar usar dados em roaming, podes desativar todos os dados móveis, ativar o modo de voo ou desativar os dados móveis do Organic Maps nas configurações do dispositivo. Os dispositivos Android e iOS podem usar o GPS no modo de voo.

* Alguns dispositivos móveis não têm receptores GPS integrados, como o iPod Touch, o iPad (apenas em Wi-Fi), o Kindle Fire Kindle HD 7 da Amazon e alguns tablets Android. Nesses dispositivos, a nossa aplicação mostrará a tua localização aproximada, desde que estejas ligado à Internet.

* Finalmente, por favor lembra-te que determinar a localização com o GPS (com a rede Wi-Fi e a rede móvel desligados) pode demorar algum tempo. Quanto mais tempo tiver decorrido desde a última vez que usaste o GPS, mais tempo demora a fazer uma nova localização. A velocidade de localização depende do dispositivo e não da aplicação. A operação do GPS também depende das condições metereológicas – funciona melhor em exteriores e com o céu limpo. Os problemas surgem ao usar no interior de edifícios, numa rua estreita ladeada por prédios altos ou dentro de um veículo em movimento.


**É mostrada uma localização incorreta no mapa**

1. Se houver um grande círculo semitransparente à volta da seta da tua localização no mapa, significa que a tua posição é determinada com baixa precisão, utilizando ligação WiFi ou móvel. Certifica-te de que ativaste a precisão de localização «Precisa» para o Organic Maps nas definições do sistema e tenta ir para o exterior, longe de edifícios altos e árvores, para melhorar a receção do sinal GPS por satélite.

2. Se a tua posição for determinada incorretamente (por exemplo, estás numa cidade, mas a aplicação mostra outra cidade), é muito provável que estejas numa área afetada por um sinal GPS falso (spoofing de GPS) devido a medidas de guerra eletrónica (EW). Nesses casos, a única solução é mudar para outro local.