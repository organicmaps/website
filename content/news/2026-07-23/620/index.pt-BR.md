---
title: "Correções de bugs e melhorias para transporte público, cálculo de rotas, pesquisa e marcadores na atualização de julho de 2026"
date: 2026-07-23
slug: "correcoes-bugs-melhorias-transporte-publico-rotas-busca-marcadores-julho-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Como talvez já tenha percebido, a atualização de julho do Organic Maps já foi lançada. Baixe-a em <https://get.omaps.org> ou no [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

Graças às suas [doações](@/donate/index.pt-BR.md) e aos seus [comentários](@/contribute/index.pt-BR.md), em julho nos concentramos na correção de bugs e em melhorias. Caso ainda não tenha visto, os seguintes recursos da [versão anterior de junho](@/news/2026-06-29/610/index.pt-BR.md) também estão disponíveis:
- Rotas de transporte público (horários em tempo real estão em desenvolvimento)
- Imagens de satélite
- Rotas alternativas para dirigir, fazer trilhas e andar de bicicleta
- Nova interface de pesquisa e planejamento de rotas para o Android
- Suporte a fontes grandes para acessibilidade no iOS

## Registro de alterações detalhado

### Mapa e locais
- Dados do OpenStreetMap atualizados em 14 de julho
- As anotações enviadas para [OpenStreetMap](https://www.openstreetmap.org) agora são posicionadas exatamente no local selecionado, em vez de no meio da rua ou da área como um todo _(Alexander Borsuk)_
- Melhoria na seleção de locais ao tocar no mapa em regiões que cruzam o antimeridiano de 180° _(Viktor Govako)_
- Os perfis de elevação das trilhas não exibem mais gráficos desatualizados ou vazios após a exclusão de uma trilha _(Kiryl Kaveryn)_

### Transporte público
- Os nomes das paradas, baldeações e estações agora têm um contorno branco para permanecerem legíveis tanto no tema claro quanto no escuro _(Viktor Govako)_
- A camada do metrô reaparece corretamente depois que a visualização de uma rota de transporte público é fechada _(Mikhail Listratsenka)_

### Roteamento e navegação
- Agora, os avisos de rota (pedágios, balsas, estradas não pavimentadas, degraus e assim por diante) são exibidos para todas as rotas alternativas _(Viktor Govako)_
- Corrigimos um travamento raro que ocorria durante a criação de uma rota _(Viktor Govako)_
- Melhoria no tratamento de becos sem saída e de pontos de início e fim em vias com restrições _(Viktor Govako)_
- Corrigidas instruções de curva incorretas e ausentes _(Alexander Borsuk)_

### iOS
- Nova configuração “Salvar histórico de pesquisa”, que permite desativar o histórico e ocultá-lo caso prefira não mantê-lo _(Kiryl Kaveryn)_
- Novo botão “Editar” para remover marcadores com mais facilidade _(Kiryl Kaveryn)_
- Os marcadores agora são salvos automaticamente ao sair da tela _(Kiryl Kaveryn)_
- A paleta de cores agora oferece cores predefinidas e permite escolher qualquer cor personalizada _(Kiryl Kaveryn)_
- Melhoramos o estado vazio do gráfico de elevação de uma trilha gravada _(Kiryl Kaveryn)_
- Melhoramos a exibição do andamento da rota no botão “Iniciar” _(Kiryl Kaveryn)_
- Reordenar as paradas da rota não faz mais a lista pular _(Kiryl Kaveryn)_
- Outras melhorias menores na interface _(Kiryl Kaveryn)_

### Android
- Os horários de funcionamento agora mostram turnos divididos (como o intervalo para o almoço), começam pelo dia atual e exibem a semana inteira sem uma área de rolagem separada _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Barra de pesquisa mais organizada, com um botão combinado para limpar e ativar o comando de voz, um ícone de limpeza que não se move mais e correções de layout para o modo paisagem e a rotação do celular _(Mikhail Listratsenka)_
- Editor de marcadores e trilhas reformulado _(Mikhail Listratsenka)_
- Correções e melhorias no planejamento de rotas _(Mikhail Listratsenka)_
- O seletor de cores agora fecha automaticamente, e uma falha no Android 5 foi corrigida _(Mikhail Listratsenka)_
- Corrigidas falhas _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- A lista de mapas disponíveis para download agora está em ordem alfabética _(goncalo109560)_

### Traduções
- Redação em chinês melhorada _(Chenxi Zhao)_
- Traduções atualizadas para o ucraniano _(Nnifria)_
- Corrigidas as traduções em italiano dos nomes das regiões do mapa _(Vittorio Bertola)_

## Participe dos testes beta para experimentar recursos antecipados e relatar problemas:

Dica: a versão beta traz um novo sombreamento de relevo, dados de altitude aprimorados com suporte para pés e metros, além de outros recursos interessantes!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Feliz verão!
A equipe do Organic Maps

{{ references() }}
