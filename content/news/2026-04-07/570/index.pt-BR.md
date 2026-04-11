---
title: "Rotas de caminhada e ciclismo com gráficos de elevação, busca de endereços nos EUA mais inteligente, continuidade do mapa no antimeridiano e muito mais na atualização de abril do Organic Maps"
date: 2026-04-07
slug: "rotas-caminhadas-ciclismo-graficos-elevacao-pesquisa-enderecos-eua-antimeridiano-mapa-abril-2026-organic-maps-atualizacao"
taxonomies:
  news: ["Releases"]
---

Nesta versão de abril, além de muitas correções de bugs e melhorias, partimos de três verdades simples: quem faz trilha quer saber quanto vai subir, todo mundo quer que a busca por endereços simplesmente funcione, e ninguém deveria ter a sensação de cair para fora da borda do mapa. Graças aos nossos colaboradores, às suas boas avaliações, às [doações](@/donate/index.pt-BR.md) e ao [suporte](@/contribute/index.pt-BR.md), resolvemos essas três questões — e muito mais.

Seja porque a primavera está chamando você para novas trilhas, seja porque o outono no hemisfério sul pede um último pedal longo, esperamos que esta atualização deixe sua próxima viagem um pouco mais fácil e muito mais bonita.

Baixe a atualização de abril em <https://get.omaps.org> ou na [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

## Destaques

- **Toque em uma trilha e veja a subida.** Agora, as rotas de caminhada e ciclismo podem ser selecionadas diretamente no mapa. Toque em uma rota para destacá-la e ver instantaneamente seu perfil de elevação.
- **Mais dois milhões de endereços nos EUA e uma busca mais inteligente.** Mais endereços, processados a partir da base TIGER Census, agora estão disponíveis no app. Além de uma correspondência mais inteligente de números de casa, isso melhora os resultados da busca em toda parte. E não se esqueça: adicionar endereços ausentes ao [OpenStreetMap](https://www.openstreetmap.org) continua sendo a melhor forma de melhorar a busca.
- **Um mapa sem bordas.** O Organic Maps agora continua suavemente pelo antimeridiano (±180° de longitude). Arraste e gire entre Chukotka e o Alasca, ou entre a Nova Zelândia e Fiji, sem paredes invisíveis nem reposicionamentos estranhos — o Pacífico finalmente parece redondo.
- **Recolora uma categoria inteira de uma só vez.** Mude a cor de todos os marcadores e/ou trilhas dentro de uma categoria com um único toque — um pequeno detalhe que transforma o arquivo bagunçado de viagens do verão passado em algo que você realmente quer abrir.

## Notas de versão

### Todas as plataformas

- NOVO! Busca melhor nos EUA, com mais dois milhões de endereços processados a partir dos dados do TIGER Census (Viktor Govako)
- NOVO! Renderização multicolorida aprimorada para rotas de caminhada e ciclismo; toque em uma rota para selecioná-la e ver seu gráfico de elevação (Viktor Govako)
- Dados do OpenStreetMap atualizados em 4 de abril
- Dados da Wikipédia atualizados em 1º de abril
- Ajustada a aproximação de ganho e perda de elevação nos gráficos de trilhas para corresponder melhor aos valores mostrados em outros aplicativos (Viktor Govako)
- Agora você pode adicionar um novo local ao OpenStreetMap depois de selecionar sua posição atual no mapa (Mikhail Listratsenka)
- Adicionados ícones para praças de alimentação e portões da cidade (David Martinez)
- Adicionadas subcategorias de lojas de roupas: mulheres, homens, crianças, casamento, esportes e roupas íntimas, além de tipos de escritório (Viktor Govako)
- Categorias de pesquisa atualizadas: adicionado "Pão" para padarias, culinária "Shawarma" e outros aprimoramentos de sinônimos (Viktor Govako)
- O mapa agora continua corretamente no antimeridiano (±180° de longitude) ao ser arrastado e girado (Alexander Borsuk, Viktor Govako)
- A navegação para ciclismo agora usa o rumo da bússola em baixas velocidades (HossamSaberr)
- Busca de endereços por número de casa aprimorada (Viktor Govako)
- Corrigido um erro de sistema ao planejar rotas perto de algumas fronteiras regionais (Viktor Govako)
- Corrigidos os resultados da pesquisa quando os nomes da cidade e do estado são iguais (Viktor Govako)
- Adicionados sinônimos de ruas dos EUA: highway, hwy, freeway e fwy (Viktor Govako)
- Corrigido o desalinhamento da mira do editor ao pressionar "Adicionar Local" (José Araújo)
- Corrigida a exibição do horário de funcionamento para locais com deslocamentos em relação ao nascer e ao pôr do sol (Alexander Borsuk)
- Corrigida a gravação de trilha GPS que perdia pontos entre segmentos (Alexander Borsuk)
- Corrigido o tratamento do horário de verão para fusos horários (Andrei Shkrob)
- Corrigidas as cores das linhas do metrô de Sydney (Alexander Borsuk)
- Corrigida a importação de GeoJSON (Alexander Borsuk)
- Estabilidade e desempenho aprimorados (Alexander Borsuk, Viktor Govako)
- Traduções atualizadas (Alexander Borsuk, Viktor Govako, colaboradores do Weblate)

### iOS

**Aviso para quem tem iPhone e iPad mais antigos:** devido a mudanças recentes no TestFlight e na App Store, esta versão oferece suporte apenas ao iOS 15 ou posterior. iOS 12, 13 e 14 não são mais compatíveis. As versões do Organic Maps já instaladas continuarão funcionando em dispositivos antigos, mas novos mapas, recursos e correções passarão a chegar apenas no iOS 15 ou superior.

- NOVO! Altere todas as cores de marcadores e trilhas em uma categoria de uma só vez (Kiryl Kaveryn)
- Exibição aprimorada de conteúdo HTML com tabelas e imagens nos detalhes do marcador (Alexander Borsuk, Kiryl Kaveryn)
- Adicionados separadores verticais para trilhas de vários segmentos no gráfico de elevação (Kiryl Kaveryn)
- Corrigida a seleção de pontos no gráfico de elevação para pontos interpolados (Kiryl Kaveryn)
- Gestos modais aprimorados: ajuste para a etapa mais próxima, fechar ao arrastar da borda e restaurar o estado anterior ao reabrir (Kiryl Kaveryn)
- Agora você pode iniciar uma rota válida mesmo quando for solicitado a baixar mapas adicionais (Kiryl Kaveryn)
- Aumentada a área de toque dos botões na barra de navegação "Adicionar Local" (Noahdyn)
- Corrigida uma falha ao exportar trilhas (Alexander Borsuk, Kiryl Kaveryn)
- Corrigida a pesquisa da lista de marcadores/trilhas ao tocar nela a partir dos Detalhes do Local (Kiryl Kaveryn)

### Android

- NOVO! Altere de uma só vez todas as cores de marcadores e trilhas em uma categoria (Mikhail Listratsenka)
- NOVO! Modo de aparência programada nas Configurações para alternância automática de tema claro/escuro com base no nascer e pôr do sol (Dzmitry Strekha)
- Adicionado o histórico de categorias usadas recentemente no editor de mapas (Mikhail Listratsenka)
- Adicionado um ícone de bonde para paradas de bonde selecionadas no mapa (Mikhail Listratsenka)
- O botão de download agora fica oculto quando todos os mapas já foram baixados (Mikhail Listratsenka)
- Corrigido o envio de edições de mapas para o OpenStreetMap (Viktor Govako)
- Corrigido o compartilhamento de arquivos com o Google Drive e outros aplicativos (Alexander Borsuk)
- Corrigida a reimportação de marcadores ao reabrir o aplicativo a partir dos aplicativos recentes (Alexander Borsuk)
- Abrir URLs de pesquisa do OpenStreetMap, como `openstreetmap.org/search?query=Pizza`, agora inicia a pesquisa no Organic Maps (Rawdyrathaur)
- Corrigidas várias falhas (Alexander Borsuk)

### Desktop (Linux e Mac OS)

- Adicionada a possibilidade de selecionar uma trilha-guia para o roteamento (Viktor Govako)
- Corrigido um problema em que salvar ou exportar marcadores/trilhas produzia arquivos corrompidos em alguns idiomas/regiões devido a separadores decimais dependentes da localidade (Alexander Borsuk)


Participe do beta para testar recursos antecipados e relatar problemas:
- [iOS][testflight]
- [Android][firebase]

Com amor e carinho ❤️
A equipe do Organic Maps

{{ references() }}
