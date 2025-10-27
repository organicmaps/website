---
title: "Lançamento 15 de setembro: novo planeamento de rotas e descrições OSM"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

Esta segunda versão de setembro traz um ecrã redesenhado de planeamento de rotas e a possibilidade de ver o conteúdo da etiqueta OpenStreetMap `description` no iOS. Para encontrar locais com essa etiqueta, digite `?description` na pesquisa (semelhante a `?wiki`).

Inclui também muitas correções e melhorias no iOS e Android (detalhes abaixo).

Funcionalidades recentes que pode ter perdido:
- Números de linhas de transporte público ao selecionar uma paragem
- Rotas de caminhada e ciclismo (ative-as com o botão Camadas no canto superior esquerdo)
- Mostrar nomes dos marcadores no mapa (ativar nas Definições)
- O ícone ✎ permite editar marcadores rapidamente

Organic Maps é possível graças aos nossos contribuidores, [às suas doações](@/donate/index.pt.md) e [ao seu apoio](@/contribute/index.md).

### Notas detalhadas

- Novos dados OpenStreetMap de 13 de setembro
- Remoção de ilhas muito pequenas do mapa-múndi (Viktor Govako)
- Mostrar código postal (ZIP) nos detalhes de endereço (Viktor Govako)
- Correção de centragem incorreta do mapa na posição atual (Kiryl Kaveryn, Viktor Govako)
- Preservar cores dos marcadores ao exportar e importar GPX (cyber-toad)
- Traduções atualizadas (colaboradores Weblate)

#### Estilos de mapa (Viktor Govako)

- Mostrar lojas de iluminação
- Mostrar linhas elétricas a partir do zoom 18
- Mostrar referências de centrais e subestações elétricas
- Mostrar parques de campismo e caravanas em modo navegação
- Corrigir cor de estradas secundárias em modo navegação
- Desenhar limites de parques nacionais
- Desenhar sítios arqueológicos a partir do zoom 12 no estilo Outdoor

#### iOS

- NOVO: mostrar conteúdo da etiqueta OSM `description` (pesquise `?description`) (Kiryl Kaveryn, Viktor Govako)
- NOVO: ecrã de planeamento de rotas redesenhado (Kiryl Kaveryn)

#### Android

- Novos ícones de rotundas no Android Auto (Andrei Shkrob)
- Mostrar categoria do marcador selecionado (Alexander Borsuk)
- Correção de atraso ao mostrar distância para um marcador (Alexander Borsuk)
- Tema escuro reestruturado (Andrei Shkrob)
- Correção de atualização de posição em navegação em ROMs personalizadas (ex. Lineage + MicroG) (Viktor Govako)
- Ícone de lápis azul (editar) para marcadores (Alexander Borsuk)
- Redução da altura vertical da pré-visualização de informação do local (Alexander Borsuk)
- Remoção do ângulo de azimute para norte na pré-visualização (toque na seta azul com distância para ver) (Alexander Borsuk)

Obtenha a versão mais recente: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Junte-se à beta: [iOS][testflight] / [Android][firebase].

{{ references() }}
