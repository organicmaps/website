---
title: "Imagens de satélite, percursos de transportes públicos, percursos alternativos, nova interface de pesquisa e planeamento de percursos para Android, suporte para letras grandes de acessibilidade no iOS e muito mais na atualização de junho de 2026"
date: 2026-06-29
slug: "imagens-satelite-percursos-transportes-publicos-percursos-alternativos-nova-pesquisa-planeamento-android-letras-grandes-ios-junho-2026"
taxonomies:
  news: ["releases"]
---

Há muitas novas funcionalidades entusiasmantes e correções de erros para experimentares na atualização de junho do Organic Maps, incluindo:
- Imagens de satélite
- Percursos de transportes públicos
- Percursos alternativos
- Nova interface de pesquisa e planeamento de percursos para Android
- Suporte para letras grandes de acessibilidade no iOS

Obtém-na em <https://get.omaps.org> ou na [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid], e diz-nos o que achas!

## Registo de alterações detalhado

- NOVO! Planeamento de percursos em transportes públicos por metro, metro ligeiro, autocarro e elétrico _(Viktor Govako)_
- NOVO! Percursos alternativos: além do percurso mais rápido, a aplicação agora mostra o percurso mais curto _(Viktor Govako)_
- NOVO! Avisos em percursos a pé e de bicicleta sobre escadas, portões e cancelas ao longo do caminho _(Viktor Govako)_
- NOVO! Escolhe qualquer cor para os marcadores _(Alexander Borsuk, Mikhail Listratsenka)_
- NOVO! Suporte para coordenadas British National Grid (OS Grid), Irish Grid e Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTAL: ativa as imagens de satélite nas definições do Organic Maps com um URL personalizado de servidor de mosaicos raster. Ainda estamos a trabalhar no nosso próprio servidor, por isso procura um servidor publicamente disponível com os marcadores `{x}`, `{y}`, `{z}` no URL _(Viktor Govako, renderexpert)_
- Dados do OpenStreetMap atualizados a 24 de junho _(Viktor Govako)_
- Dados da Wikipedia atualizados a 20 de junho, incluindo artigos em italiano _(Alexander Borsuk)_
- Escreve `?map-download-server:https://your-server.com/` na janela de pesquisa para substituir os servidores de transferência de mapas do Organic Maps. Escreve `?no-map-download-server` para remover a substituição _(Alexander Borsuk)_

#### Renderização e estilos do mapa

- Padrões mais bonitos para áreas de praia, areia, cascalheira, rocha nua, pomar e vinha, além de hachuras para áreas protegidas e zonas húmidas _(Alexander Borsuk)_
- Etiquetas de texto curvas mais suaves para estradas e rios _(Viktor Govako)_
- Rios, ribeiros e zonas húmidas têm maior contraste e são mais visíveis no modo escuro _(Alexander Borsuk)_
- Ícones novos e melhorados para pesquisa por categoria e resultados de pesquisa no mapa _(Anton Makouski)_
- Melhor composição e renderização de texto multilingue _(Alexander Borsuk)_
- Várias correções de erros e melhorias de desempenho _(Viktor Govako)_

#### Trilhos, marcadores e percursos

- Os trilhos GeoJSON agora mantêm elevação e carimbos de data/hora na importação e exportação _(Alexander Borsuk)_
- Corrigida uma falha depois de mover um trilho para outra lista _(Viktor Govako)_
- Agora são mostrados websites para locais patrimoniais _(Viktor Govako)_
- Agora são mostrados nomes de operadores para resultados de pesquisa sem nome. Por exemplo, um multibanco sem nome agora mostra o respetivo banco _(Anton Makouski)_
- Editor: corrigido o texto de descrição para edições/changesets do OpenStreetMap em edifícios de apartamentos _(titanniya542-spec)_
- Melhor deteção de HTML nas descrições de marcadores e trilhos _(Alexander Borsuk)_

### iOS

- NOVO! Suporte de acessibilidade para Dynamic Type e letras grandes _(Kiryl Kaveryn)_
- NOVO! Toca para escolher entre trilhos e percursos sobrepostos _(Kiryl Kaveryn)_
- Melhor renderização HTML das descrições de marcadores e trilhos _(Kiryl Kaveryn)_
- Estilo de tabelas mais limpo na interface _(Kiryl Kaveryn)_

### Android

- NOVO! Interface de pesquisa _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NOVO! Interface de planeamento de percursos _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Melhor renderização HTML das descrições de marcadores e trilhos _(Mikhail Listratsenka)_
- Tamanho do APK reduzido _(Alexander Borsuk)_
- O ícone de voz é mostrado como desativado quando não há motor de texto-para-fala disponível _(Mikhail Listratsenka)_
- Descrições longas de marcadores e trilhos agora mostram um botão «…mais» _(Mikhail Listratsenka)_
- Várias correções da interface e uma correção da API para IDs de pontos devolvidos _(Mikhail Listratsenka)_

### Desktop

- Suporte para alternar o sistema de coordenadas apresentado _(Alexander Borsuk)_
- A informação sobre o local selecionado agora é apresentada à esquerda _(Viktor Govako)_
- Corrigida a posição do menu de contexto _(Osyotr)_
- Corrigidos bloqueios no início de sessão e nas edições do OpenStreetMap em versões Qt 6.4 e anteriores _(Alexander Borsuk)_
- Corrigida uma mudança inesperada do estilo do mapa durante a navegação no macOS _(Alexander Borsuk)_
- Corrigida uma falha ao fechar a aplicação macOS depois de exportar um ficheiro KMZ _(Alexander Borsuk)_

### Traduções

- Orientação por voz curva a curva em cantonês _(Alexander Borsuk)_
- Traduções alemã e francesa atualizadas _(Wuzzy, Alexander Borsuk)_
- Corrigidas traduções incorretas da orientação por voz «onto street» para chinês, sérvio e catalão _(Alexander Borsuk)_

## Junta-te aos testes beta para experimentar funcionalidades antecipadas e comunicar problemas:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Agradecemos a todos os nossos utilizadores e colaboradores, a quem [faz donativos](@/donate/index.pt.md) e dá 5 estrelas ao Organic Maps nas lojas de aplicações. Juntos podemos criar a melhor aplicação de mapas!

Com carinho,
A equipa do Organic Maps

{{ references() }}
