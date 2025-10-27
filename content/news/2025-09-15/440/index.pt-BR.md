---
title: "Lançamento 15 de setembro: nova tela de rotas e descrições OSM"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

Esta segunda versão de setembro traz uma tela redesenhada de planejamento de rotas e a visualização do conteúdo da tag `description` do OpenStreetMap no iOS. Para achar lugares com essa tag, digite `?description` na busca (semelhante a `?wiki`).

Inclui também várias correções e melhorias no iOS e Android (detalhes abaixo).

Recursos recentes que você pode ter perdido:
- Números das linhas de transporte público ao selecionar um ponto de ônibus
- Rotas de trilha e ciclismo (ative pelo botão Camadas no canto superior esquerdo)
- Mostrar nomes dos marcadores no mapa (ative em Configurações)
- O ícone ✎ permite editar marcadores rapidamente

Organic Maps é possível graças aos nossos contribuidores, [às suas doações](@/donate/index.pt-BR.md) e [ao seu apoio](@/contribute/index.md).

### Notas detalhadas

- Novos dados OpenStreetMap de 13 de setembro
- Remoção de ilhas muito pequenas do mapa-múndi (Viktor Govako)
- Mostrar CEP (ZIP) nos detalhes do endereço (Viktor Govako)
- Correção do centramento incorreto do mapa na posição atual (Kiryl Kaveryn, Viktor Govako)
- Preservar cores dos marcadores ao exportar e importar GPX (cyber-toad)
- Traduções atualizadas (colaboradores Weblate)

#### Estilos de mapa (Viktor Govako)

- Mostrar lojas de iluminação
- Mostrar linhas de energia a partir do zoom 18
- Mostrar referências de usinas e subestações
- Mostrar campings e áreas para trailers no modo navegação
- Corrigir cor de vias secundárias no modo navegação
- Desenhar limites de parques nacionais
- Desenhar sítios arqueológicos a partir do zoom 12 no estilo Outdoor

#### iOS

- NOVO: mostrar conteúdo da tag OSM `description` (busque `?description`) (Kiryl Kaveryn, Viktor Govako)
- NOVO: tela de planejamento de rotas redesenhada (Kiryl Kaveryn)

#### Android

- Novos ícones de rotatória no Android Auto (Andrei Shkrob)
- Mostrar categoria do marcador selecionado (Alexander Borsuk)
- Corrigido atraso ao mostrar distância até um marcador (Alexander Borsuk)
- Tema escuro reestruturado (Andrei Shkrob)
- Correção da atualização de posição na navegação em ROMs personalizadas (ex. Lineage + MicroG) (Viktor Govako)
- Ícone de lápis azul (editar) para marcadores (Alexander Borsuk)
- Redução da altura vertical da prévia de informações do lugar (Alexander Borsuk)
- Remoção do ângulo de azimute para o norte da prévia (toque na seta azul com a distância para ver) (Alexander Borsuk)

Obtenha a versão mais recente: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Participe do beta: [iOS][testflight] / [Android][firebase].

{{ references() }}
