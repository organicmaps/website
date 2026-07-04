---
title: "Imagens de satélite, rotas de transporte público, rotas alternativas, nova interface de busca e planejamento de rotas para Android, suporte a fontes grandes de acessibilidade no iOS e muito mais na atualização de junho de 2026"
date: 2026-06-29
slug: "imagens-satelite-rotas-transporte-publico-rotas-alternativas-nova-busca-planejamento-android-fontes-grandes-ios-junho-2026"
taxonomies:
  news: ["releases"]
---

Há muitos novos recursos empolgantes e correções de bugs para testar na atualização de junho do Organic Maps, incluindo:
- Imagens de satélite
- Rotas de transporte público
- Rotas alternativas
- Nova interface de busca e planejamento de rotas para Android
- Suporte a fontes grandes de acessibilidade no iOS

Baixe em <https://get.omaps.org> ou na [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid], e conte pra gente o que você achou!

## Registro de alterações detalhado

- NOVO! Planejamento de rotas de transporte público por metrô, VLT, ônibus e bonde _(Viktor Govako)_
- NOVO! Rotas alternativas: além da rota mais rápida, o app agora mostra a rota mais curta _(Viktor Govako)_
- NOVO! Alertas em rotas a pé e de bicicleta sobre escadas, portões e cancelas pelo caminho _(Viktor Govako)_
- NOVO! Escolha qualquer cor para os marcadores _(Alexander Borsuk, Mikhail Listratsenka)_
- NOVO! Suporte a coordenadas British National Grid (OS Grid), Irish Grid e Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTAL: ative as imagens de satélite nas configurações do Organic Maps usando uma URL personalizada de servidor de blocos raster. Ainda estamos trabalhando no nosso próprio servidor, então procure um servidor aberto disponível com os marcadores `{x}`, `{y}`, `{z}` na URL _(Viktor Govako, renderexpert)_
- Dados do OpenStreetMap atualizados até 24 de junho _(Viktor Govako)_
- Dados da Wikipedia atualizados até 20 de junho, incluindo artigos em italiano _(Alexander Borsuk)_
- Digite `?map-download-server:https://your-server.com/` na janela de busca para substituir os servidores de download de mapas do Organic Maps. Digite `?no-map-download-server` para remover a substituição _(Alexander Borsuk)_

#### Renderização e estilos do mapa

- Padrões mais bonitos para áreas de praia, areia, cascalho, rocha exposta, pomar e vinhedo, além de hachuras para áreas protegidas e áreas úmidas _(Alexander Borsuk)_
- Rótulos de texto curvos mais suaves para ruas e rios _(Viktor Govako)_
- Rios, riachos e áreas úmidas têm maior contraste e ficam mais visíveis no modo escuro _(Alexander Borsuk)_
- Ícones novos e melhorados para busca por categoria e resultados de busca no mapa _(Anton Makouski)_
- Melhor composição e renderização de texto multilíngue _(Alexander Borsuk)_
- Várias correções de bugs e melhorias de desempenho _(Viktor Govako)_

#### Trilhas, marcadores e rotas

- Trilhas GeoJSON agora preservam elevação e carimbos de data/hora na importação e exportação _(Alexander Borsuk)_
- Corrigido um travamento depois de mover uma trilha para outra lista _(Viktor Govako)_
- Sites agora são mostrados para locais históricos/patrimoniais _(Viktor Govako)_
- Nomes de operadores agora são exibidos para resultados de busca sem nome. Por exemplo, um caixa eletrônico sem nome agora mostra seu banco _(Anton Makouski)_
- Editor: corrigido o texto de descrição para edições/changesets do OpenStreetMap em prédios de apartamentos _(titanniya542-spec)_
- Melhor detecção de HTML em descrições de marcadores e trilhas _(Alexander Borsuk)_

### iOS

- NOVO! Suporte de acessibilidade para Dynamic Type e fontes grandes _(Kiryl Kaveryn)_
- NOVO! Toque para escolher entre trilhas e rotas sobrepostas _(Kiryl Kaveryn)_
- Melhor renderização HTML das descrições de marcadores e trilhas _(Kiryl Kaveryn)_
- Estilo de tabelas mais limpo na interface _(Kiryl Kaveryn)_

### Android

- NOVO! Interface de busca _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NOVO! Interface de planejamento de rotas _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Melhor renderização HTML das descrições de marcadores e trilhas _(Mikhail Listratsenka)_
- Tamanho do APK reduzido _(Alexander Borsuk)_
- O ícone de voz aparece como desativado quando não há mecanismo de texto para fala disponível _(Mikhail Listratsenka)_
- Descrições longas de marcadores e trilhas agora mostram um botão “…mais” _(Mikhail Listratsenka)_
- Várias correções de interface e uma correção de API para IDs de pontos retornados _(Mikhail Listratsenka)_

### Desktop

- Suporte para alternar o sistema de coordenadas exibido _(Alexander Borsuk)_
- As informações sobre o local selecionado agora são exibidas à esquerda _(Viktor Govako)_
- Corrigida a posição do menu de contexto _(Osyotr)_
- Corrigidos travamentos no login e nas edições do OpenStreetMap em versões do Qt 6.4 e anteriores _(Alexander Borsuk)_
- Corrigida uma troca inesperada do estilo do mapa durante a navegação no macOS _(Alexander Borsuk)_
- Corrigido um travamento ao fechar o app para macOS depois de exportar um arquivo KMZ _(Alexander Borsuk)_

### Traduções

- Orientação por voz curva a curva em cantonês _(Alexander Borsuk)_
- Traduções em alemão e francês atualizadas _(Wuzzy, Alexander Borsuk)_
- Corrigidas traduções incorretas de orientação por voz de “onto street” para chinês, sérvio e catalão _(Alexander Borsuk)_

## Participe dos testes beta para experimentar recursos antecipados e relatar problemas:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Agradecemos a todos os nossos usuários e colaboradores, a quem [doa](@/donate/index.pt-BR.md) e dá 5 estrelas ao Organic Maps nas lojas de apps. Juntos podemos criar o melhor app de mapas!

Com carinho,
A equipe do Organic Maps

{{ references() }}
