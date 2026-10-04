---
title: "Otimização de rotas, rotas alternativas aprimoradas, ocultação de trilhas individuais e áreas com presença intermitente de água na atualização de setembro de 2026"
date: 2026-09-29
slug: "otimizacao-rotas-rotas-alternativas-ocultar-trilhas-individuais-areas-agua-intermitente-setembro-2026"
aliases: ["/pt-BR/news/2026-09-29/selecao-multipla-favoritos-trilhas-painel-carplay-ocultar-trilhas-links-compartilhamento-agosto-2026/"]
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Vamos nessa? A atualização de setembro traz rotas alternativas aprimoradas, uma opção para otimizar a ordem das paradas da rota, marcações mais claras para áreas com presença intermitente de água e um ícone de olho para ocultar trilhas individuais, além de várias outras correções e melhorias (veja abaixo).

Instale ou atualize o Organic Maps pelo site <https://get.omaps.org>, pela [App Store][appstore], pelo [Google Play][googleplay], pela [Huawei AppGallery][appgallery], pelo [Obtainium][obtainium], pelo [Accrescent][accrescent] ou pelo [F-Droid][fdroid].

Se você perdeu nossas atualizações anteriores, dê uma olhada nos recursos lançados em [junho](@/news/2026-06-29/610/index.pt-BR.md), [julho](@/news/2026-07-23/620/index.pt-BR.md) e [agosto](@/news/2026-08-31/630/index.pt-BR.md). Muito obrigado aos nossos colaboradores e usuários que tornaram essas atualizações possíveis!

## Como apoiar o Organic Maps

- [Faça uma doação](@/donate/index.pt-BR.md) para apoiar o desenvolvimento e cobrir os custos de hospedagem dos mapas
- [Envie seus comentários e contribua](@/contribute/index.pt-BR.md) com o projeto
- Participe dos testes beta para experimentar novos recursos mais cedo e relatar problemas no [iOS][testflight], no [Android][firebase] e no [desktop][flathub]
- Divulgue e nos ajude a criar uma alternativa melhor aos mapas das grandes empresas de tecnologia!

## Notas de lançamento

### Mapa

- Dados do OpenStreetMap em 28 de setembro de 2026
- Dados da Wikipédia em 21 de setembro de 2026
- Corrigimos as buscas quando a área visível do mapa atravessa o meridiano de 180° (±180° de longitude) _(Viktor Govako)_
- As áreas com presença intermitente de água agora são exibidas com um padrão pontilhado, parecido com o usado para a areia _(Alexander Borsuk)_
- Agora os reservatórios de água ficam visíveis ao diminuir ainda mais o zoom _(Alexander Borsuk)_
- Os túneis de água não aparecem mais no mapa _(Alexander Borsuk)_
- Corrigimos os ícones das estações e entradas do Metrô de Suzhou _(Alexander Borsuk)_
- Corrigimos alguns casos raros em que os rótulos ficavam deslocados na camada do mapa do metrô _(Viktor Govako)_

### Roteamento e navegação

- Melhoramos as rotas alternativas e seus horários estimados de chegada _(Alexander Borsuk, Viktor Govako)_
- Agora, a rota alternativa selecionada é mantida quando a navegação recalcula a rota _(Alexander Borsuk)_
- A ordem das paradas da rota agora é restaurada após reiniciar o app _(Kiryl Kaveryn)_

### Outras melhorias

- O horário de funcionamento agora mostra “Meio-dia” para 12:00 e “Meia-noite” para 00:00 ou 24:00 _(Alexander Borsuk)_
- Corrigimos bugs e melhoramos a gravação de trilhas _(Alexander Borsuk)_
- Corrigimos a importação de arquivos KMB _(Alexander Borsuk)_
- Traduções corrigidas para o francês e o asturiano _(Alexander Borsuk)_
- Corrigimos um erro de digitação em inglês _(Carl Morris)_

### iOS

- Adicionamos um ícone de olho para ocultar trilhas individuais _(Kiryl Kaveryn)_
- Adicionamos botões para adicionar ou substituir uma parada em uma rota planejada _(Kiryl Kaveryn)_
- Adicionamos uma configuração para otimizar a ordem das paradas intermediárias da rota _(Kiryl Kaveryn)_
- Adicionamos instruções de manobra aos visores head-up (HUDs) compatíveis dos carros e ao painel do CarPlay _(Kiryl Kaveryn)_
- Corrigimos os botões e a busca do CarPlay _(Alexander Borsuk)_
- Corrigimos vários bugs e melhoramos a interface do usuário _(Kiryl Kaveryn, Alexander Borsuk)_
- Adicionamos suporte para escolher e ouvir uma amostra de uma voz de navegação instalada _(Kiryl Kaveryn, Alexander Borsuk)_
- Restauramos a busca por categoria no Spotlight _(Kiryl Kaveryn)_

### Android

- Adicionamos uma configuração para otimizar a ordem das paradas intermediárias da rota _(Mikhail Listratsenka)_
- Adicionamos botões para adicionar ou substituir uma parada em uma rota planejada _(Mikhail Listratsenka)_
- Adicionamos a opção de interromper a gravação de uma trilha e salvá-la diretamente pela notificação _(Alexander Borsuk)_
- O botão “Adicionar parada” agora adiciona uma parada depois das paradas já existentes, antes do destino _(Mikhail Listratsenka)_
- Melhorias nos envios pelo editor do OpenStreetMap _(Owm)_
- Atualizamos o design da interface do usuário _(Mikhail Listratsenka)_
- O editor de favoritos e outras caixas de diálogo agora ficam abertos durante a navegação _(Mikhail Listratsenka)_
- Corrigimos a exibição do gráfico de elevação em trilhas planas e em interfaces da direita para a esquerda _(Mikhail Listratsenka)_
- Corrigimos o problema dos botões do mapa ficarem cortados pelas barras do sistema _(Mikhail Listratsenka)_
- Corrigimos alguns bugs e melhoramos o suporte ao Android Auto _(Andrei Shkrob)_
- Corrigimos uma falha durante a renderização do mapa _(Viktor Govako)_

### Desktop

- Renomeamos o executável para desktop e o pacote do aplicativo macOS para `OrganicMaps` _(Alexander Borsuk)_
- Corrigimos alguns problemas no aplicativo para Windows _(Osyotr, Alexander Borsuk)_
- O argumento de linha de comando `--lang` agora tem prioridade sobre a configuração de idioma do aplicativo _(Alexander Borsuk)_

Com alegria e paixão,

Sua equipe do Organic Maps

{{ <references lang /> }}
