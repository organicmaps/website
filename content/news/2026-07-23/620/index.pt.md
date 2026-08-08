---
title: "Correções de erros e melhorias nas funcionalidades de transportes públicos, cálculo de percursos, pesquisa e favoritos na atualização de julho de 2026"
date: 2026-07-23
slug: "correcoes-erros-melhorias-transportes-publicos-percursos-pesquisa-marcadores-julho-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Como já deve ter reparado, a atualização de julho do Organic Maps já está disponível. Pode descarregá-la em <https://get.omaps.org> ou na [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

Graças às suas [doações](@/donate/index.pt.md) e aos seus [comentários](@/contribute/index.pt.md), em julho dedicámo-nos à correção de erros e a melhorias. Caso não tenha visto, as seguintes funcionalidades da [versão anterior de junho](@/news/2026-06-29/610/index.pt.md) também estão disponíveis:
- Percursos de transportes públicos (os horários em tempo real estão em desenvolvimento)
- Imagens de satélite
- Percursos alternativos para conduzir, fazer caminhadas e andar de bicicleta
- Nova interface de pesquisa e planeamento de percursos para o Android
- Suporte para tipos de letra de grande tamanho para acessibilidade no iOS

## Registo de alterações detalhado

### Mapa e locais

- Dados do OpenStreetMap atualizados a 14 de julho
- As notas enviadas para [OpenStreetMap](https://www.openstreetmap.org) são agora colocadas exatamente no local que selecionou, em vez de no meio da rua ou da área _(Alexander Borsuk)_
- Melhoria na seleção de locais ao tocar no mapa em regiões que atravessam o antimeridiano de 180° _(Viktor Govako)_
- Os perfis de elevação dos trilhos já não apresentam gráficos desatualizados ou vazios após a eliminação de um trilho _(Kiryl Kaveryn)_

### Transportes públicos

- Os nomes das paragens, transbordos e estações têm agora um contorno branco para se manterem legíveis tanto no tema claro como no escuro _(Viktor Govako)_
- A camada do metro volta a aparecer corretamente depois de fechar a pré-visualização de um percurso de transportes públicos _(Mikhail Listratsenka)_

### Percursos e navegação

- Os avisos sobre o percurso (portagens, ferries, estradas não pavimentadas, degraus, etc.) são agora apresentados para todos os percursos alternativos _(Viktor Govako)_
- Foi corrigido um bloqueio raro que ocorria durante a criação de um percurso _(Viktor Govako)_
- Melhoria no tratamento de becos sem saída e dos pontos de início e fim em estradas com restrições _(Viktor Govako)_
- Corrigiram-se instruções de viragem incorretas e em falta _(Alexander Borsuk)_

### iOS

- Nova opção «Guardar histórico de pesquisa», que lhe permite desativar o histórico e ocultá-lo, caso prefira não o guardar _(Kiryl Kaveryn)_
- Novo botão «Editar» para remover marcadores com mais facilidade _(Kiryl Kaveryn)_
- Os marcadores passam agora a ser guardados automaticamente quando sai do ecrã _(Kiryl Kaveryn)_
- A paleta de cores oferece agora cores predefinidas e permite-lhe escolher qualquer cor personalizada _(Kiryl Kaveryn)_
- Foi melhorado o estado vazio do gráfico de elevação de um trilho gravado _(Kiryl Kaveryn)_
- Foi melhorada a visualização do progresso do percurso apresentada no botão «Iniciar» _(Kiryl Kaveryn)_
- A reordenação das paragens do percurso já não faz com que a lista salte de um lado para o outro _(Kiryl Kaveryn)_
- Outras pequenas melhorias na interface _(Kiryl Kaveryn)_

### Android

- Os horários de funcionamento passam agora a incluir turnos divididos (como a pausa para o almoço), começam pelo dia atual e apresentam toda a semana sem uma área de deslocamento separada _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Uma barra de pesquisa mais simples, com um botão combinado para limpar e ativar a função de voz, um ícone de limpeza que já não se move e correções de layout para o modo paisagem e a rotação do telemóvel _(Mikhail Listratsenka)_
- Editor de marcadores e trilhos reformulado _(Mikhail Listratsenka)_
- Correções e melhorias no planeamento de percursos _(Mikhail Listratsenka)_
- O seletor de cores fecha agora automaticamente e foi corrigida uma falha no Android 5 _(Mikhail Listratsenka)_
- Corrigidas falhas _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop

- A lista de mapas disponíveis para descarregar está agora ordenada por ordem alfabética _(goncalo109560)_

### Traduções

- Redação em chinês melhorada _(Chenxi Zhao)_
- Traduções atualizadas para o ucraniano _(Nnifria)_
- Corrigidas as traduções para italiano dos nomes das regiões do mapa _(Vittorio Bertola)_

## Junte-se aos testes beta para experimentar funcionalidades antecipadas e comunicar problemas:

Dica: a versão beta inclui um novo sombreado de relevo, dados de altitude melhorados com suporte para pés e metros, e outras funcionalidades fantásticas!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Bom verão!
A equipa do Organic Maps

{{ references() }}
