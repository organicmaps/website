---
title: "Otimização de rotas, rotas alternativas melhoradas, ocultação de trilhos individuais e zonas com presença intermitente de água na atualização de setembro de 2026"
date: 2026-09-29
slug: "otimizacao-rotas-rotas-alternativas-ocultar-trilhos-individuais-zonas-agua-intermitente-setembro-2026"
aliases: ["/pt/news/2026-09-29/selecao-multipla-favoritos-trilhos-painel-carplay-ocultar-trilhos-links-partilha-agosto-2026/"]
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Pronto para partir? A atualização de setembro traz rotas alternativas melhoradas, uma opção para otimizar a ordem das paragens da rota, marcações mais claras para zonas com presença intermitente de água e um ícone de olho para ocultar trilhos individuais, além de muitas outras correções e melhorias (ver abaixo).

Instala ou atualiza o Organic Maps através de <https://get.omaps.org>, da [App Store][appstore], do [Google Play][googleplay], da [Huawei AppGallery][appgallery], do [Obtainium][obtainium], do [Accrescent][accrescent] ou do [F-Droid][fdroid].

Se não viste as nossas atualizações anteriores, dá uma vista de olhos nas funcionalidades lançadas em [junho](@/news/2026-06-29/610/index.pt.md), [julho](@/news/2026-07-23/620/index.pt.md) e [agosto](@/news/2026-08-31/630/index.pt.md). Um grande obrigado aos nossos colaboradores e utilizadores que tornaram estas atualizações possíveis!

## Como apoiar o Organic Maps

- [Faz uma doação](@/donate/index.pt.md) para apoiar o desenvolvimento e cobrir os custos de alojamento dos mapas
- [Envia os teus comentários e contribui](@/contribute/index.pt.md) para o projeto
- Junta-te ao teste beta para experimentares as novas funcionalidades em primeira mão e reportares problemas no [iOS][testflight], [Android][firebase] e [no computador][flathub]
- Passa a palavra e ajuda-nos a criar uma alternativa melhor aos mapas das grandes empresas tecnológicas!

## Notas de lançamento

### Mapa

- Dados do OpenStreetMap a 28 de setembro de 2026
- Dados da Wikipédia a 21 de setembro de 2026
- Corrigimos as pesquisas quando a área visível do mapa atravessa o meridiano de 180° (±180° de longitude) _(Viktor Govako)_
- As zonas com presença intermitente de água são agora apresentadas com um padrão pontilhado, semelhante ao utilizado para a areia _(Alexander Borsuk)_
- Os reservatórios de água já são visíveis quando se afasta mais o zoom _(Alexander Borsuk)_
- Os túneis de água já não aparecem no mapa _(Alexander Borsuk)_
- Corrigimos os ícones das estações e das entradas do metro de Suzhou _(Alexander Borsuk)_
- Corrigimos alguns casos raros em que os rótulos ficavam deslocados na camada do mapa do metro _(Viktor Govako)_

### Planeamento de rotas e navegação

- Melhorámos as rotas alternativas e as respetivas horas de chegada estimadas _(Alexander Borsuk, Viktor Govako)_
- A rota alternativa selecionada é agora mantida quando a navegação recalcula a rota _(Alexander Borsuk)_
- A ordem das paragens da rota é agora restabelecida depois de reiniciar a aplicação _(Kiryl Kaveryn)_

### Outras melhorias

- O horário de funcionamento agora mostra «Meio-dia» para as 12:00 e «Meia-noite» para as 00:00 ou 24:00 _(Alexander Borsuk)_
- Corrigimos alguns erros e melhorámos a gravação de trilhos _(Alexander Borsuk)_
- Corrigida a importação de ficheiros KMB _(Alexander Borsuk)_
- Traduções corrigidas em francês e asturiano _(Alexander Borsuk)_
- Corrigimos uma gralha em inglês _(Carl Morris)_

### iOS

- Adicionámos um ícone de olho para ocultar trilhos individuais _(Kiryl Kaveryn)_
- Adicionámos botões para adicionar ou substituir uma paragem numa rota planeada _(Kiryl Kaveryn)_
- Adicionámos uma opção para otimizar a ordem das paragens intermédias da rota _(Kiryl Kaveryn)_
- Adicionámos instruções de manobra aos ecrãs head-up (HUD) dos carros compatíveis e ao painel do CarPlay _(Kiryl Kaveryn)_
- Corrigimos os botões e a pesquisa do CarPlay _(Alexander Borsuk)_
- Corrigimos vários erros e melhorámos a interface do utilizador _(Kiryl Kaveryn, Alexander Borsuk)_
- Adicionámos a possibilidade de escolher e ouvir uma amostra de uma voz de navegação instalada _(Kiryl Kaveryn, Alexander Borsuk)_
- Restabelecemos a pesquisa por categoria no Spotlight _(Kiryl Kaveryn)_

### Android

- Adicionámos uma opção para otimizar a ordem das paragens intermédias da rota _(Mikhail Listratsenka)_
- Adicionámos botões para adicionar ou substituir uma paragem numa rota planeada _(Mikhail Listratsenka)_
- Adicionámos a possibilidade de parar a gravação de um trilho e guardá-lo a partir da notificação _(Alexander Borsuk)_
- O botão «Adicionar paragem» agora adiciona uma paragem a seguir às paragens já existentes, antes do destino _(Mikhail Listratsenka)_
- Melhorias nos envios a partir do editor do OpenStreetMap _(Owm)_
- Atualizámos o design da interface do utilizador _(Mikhail Listratsenka)_
- O editor de favoritos e outras caixas de diálogo agora ficam abertos durante a navegação _(Mikhail Listratsenka)_
- Corrigida a renderização do gráfico de elevação em trilhos planos e em interfaces da direita para a esquerda _(Mikhail Listratsenka)_
- Corrigido o problema em que os botões do mapa ficavam cortados pelas barras do sistema _(Mikhail Listratsenka)_
- Corrigimos alguns erros e melhorámos a compatibilidade com o Android Auto _(Andrei Shkrob)_
- Corrigimos uma falha que causava o encerramento do programa durante a renderização do mapa _(Viktor Govako)_

### Computador

- Renomeámos o executável para computador e o pacote da aplicação macOS para `OrganicMaps` _(Alexander Borsuk)_
- Corrigimos alguns problemas na aplicação para Windows _(Osyotr, Alexander Borsuk)_
- O argumento de linha de comandos `--lang` tem agora prioridade sobre a definição de idioma da aplicação _(Alexander Borsuk)_

Com alegria e paixão,

A tua equipa do Organic Maps

{{ <references lang /> }}
