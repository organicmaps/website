---
title: "Toque em uma parada de transporte público para ver as rotas no mapa, rótulos de marcadores não se sobrepõem mais, regiões menores para download no Vietnã, na Malásia e no sul da China na atualização de maio do Organic Maps"
date: 2026-05-08
slug: "selecao-de-parada-de-transporte-publico-rotulos-de-marcadores-sem-sobreposicao-vietna-malasia-china-regioes-divididas"
taxonomies:
  news: ["releases"]
---

A atualização de maio aproxima ainda mais o Organic Maps do suporte completo ao transporte público. Uma parada de ônibus, trem, balsa ou bonde é um ponto de partida para as linhas que passam por ela — por isso, ao tocar em uma rota em uma parada, agora exibimos essa linha, em sua própria cor, por todo o mapa. Os horários online também estão a caminho; não se esqueça de [adicionar/atualizar os dados de transporte público do OSM](https://gtfs-osm-matcher.organicmaps.app/) na sua região, caso ainda não tenha feito isso!

Como sempre, muito obrigado aos nossos colaboradores, às suas boas avaliações, [doações](@/donate/index.pt-BR.md) e [apoio](@/contribute/index.pt-BR.md).

Baixe a atualização de maio em <https://get.omaps.org> ou na [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

## Destaques

- **Toque em uma parada de ônibus, bonde, trem ou balsa no mapa,** e o Organic Maps destaca toda a linha de transporte público, que pode ser selecionada na lista de linhas e rotas exibidas.
- **Rótulos de marcadores mais limpos e um mapa mais legível.** O novo posicionamento dos rótulos evita que os títulos dos marcadores se sobreponham, as áreas para pedestres ficaram um pouco mais escuras e as cores das rotas foram ajustadas para melhor contraste tanto no tema claro quanto no escuro.
- **Regiões mais detalhadas na Ásia.** O Vietnã e a Malásia agora estão divididos em mapas menores, para que você possa baixar apenas a área de que precisa, e Hong Kong, Macau e Hainan agora estão separados de Guangdong.

## Notas de versão

### Todas as plataformas

- NOVO! Toque em uma parada de transporte público e selecione um número de linha para destacar toda a rota de transporte público no mapa, como na camada de metrô (Viktor Govako, Kiryl Kaveryn, Mikhail Listratsenka)
- NOVO! Os rótulos dos marcadores no mapa não se sobrepõem mais (Viktor Govako)
- Cálculos de ganho e perda de elevação corrigidos nos gráficos de trilhas para corresponder melhor aos valores de outros aplicativos populares (Viktor Govako)
- O transporte público de longa distância e outras relações do mapa agora são conectados através das fronteiras dos mapas em uma única linha contínua (Viktor Govako)
- Vietnã e Malásia foram divididos em regiões menores que podem ser baixadas individualmente (Viktor Govako)
- Hong Kong, Macau e Hainan foram separados de Guangdong, com as fronteiras vizinhas atualizadas (Viktor Govako)
- Isolinhas (curvas de nível) atualizadas para Indonésia, Malásia, Tanzânia, Tailândia e Vietnã (Viktor Govako)
- Roteamento: rotas retomadas agora descartam pontos intermediários pelos quais você já passou (Viktor Govako)
- Adicionados ícones para vulcões ativos e pontos de acesso a vias aquáticas; rampas de acesso à água agora podem ser pesquisadas (David Martinez)
- Adicionados lounges de narguilé (alnzrv)
- Adicionados edifícios em construção (Viktor Govako)
- Adicionado "Lookout" como sinônimo de busca para mirantes (alnzrv)
- Adicionado "pkwy" como sinônimo de rua nos EUA (Viktor Govako)
- Cores das áreas para pedestres ligeiramente escurecidas para melhor legibilidade (Viktor Govako)
- O texto em múltiplas linhas agora é recortado de forma limpa no mapa (Viktor Govako)
- Nomes de ruas não contêm mais partes duplicadas (Viktor Govako)
- Corrigida a importação de arquivos KMB (Alexander Borsuk)
- Traduções atualizadas em categorias, sinônimos de busca e textos da interface (Alexander Borsuk, Viktor Govako)
- Descrições de Nova Gales do Sul e do Território do Norte traduzidas (alnzrv)
- Estabilidade e desempenho aprimorados, incluindo renderização de fontes, cache de glifos e recorte de linhas de rota (Viktor Govako, Alexander Borsuk)

### iOS

- NOVO! Botão de gravação de trilha adicionado ao painel de informações durante a navegação (Kiryl Kaveryn)
- NOVO! Duas etapas extras no painel de navegação para informações mais detalhadas de altitude/rota (Kiryl Kaveryn)
- Estilo do gráfico de elevação atualizado no painel de navegação, com renderização correta para trilhas que possuem altitudes negativas (Kiryl Kaveryn)
- Corrigida a exibição da lista de marcadores errada na versão do TestFlight (Alexander Borsuk)
- Botão "Parar" maior e alvos de toque ampliados para os botões do painel inferior durante a navegação: silenciar TTS, configurações e gravação de trilha (Kiryl Kaveryn)
- Animação refinada da seção de descrição expansível na página do local (Kiryl Kaveryn)
- A página do local não é mais fechada ao soltar o controle do gráfico de elevação, não salta mais inesperadamente e mantém o título visível ao editar com o teclado aberto (Kiryl Kaveryn)
- Corrigidos problemas de cor no gráfico de elevação e no indicador circular de progresso quando a aparência do sistema muda (Kiryl Kaveryn)
- Corrigidas falhas ao excluir uma trilha ou marcador que não existe mais (Kiryl Kaveryn)

### Android

- NOVO! Painel de altitude persistente e perfil de elevação da rota aprimorado, com layout RTL adequado (Eric Jau, Mikhail Listratsenka)
- O estado da rota salva agora é preservado ao girar o dispositivo (Mikhail Listratsenka)
- Linha de referência de rota única e unificada na página do local (Mikhail Listratsenka)
- Raio de canto maior para painéis inferiores, botões e elementos gráficos, para uma aparência mais consistente (Mikhail Listratsenka)
- Corrigidas falhas de layout ao redor das barras do sistema e da barra de navegação (Mikhail Listratsenka)
- Exibição aprimorada de artigos da Wikipedia com melhor formatação, cores do sistema e tratamento do modo escuro (DeshDeepakKant, Mikhail Listratsenka)
- Adicionados divisores verticais entre os segmentos de trilhas com várias geometrias no gráfico de elevação (Mikhail Listratsenka)
- Comportamento de rolagem do gráfico de elevação aprimorado (Mikhail Listratsenka)
- Correções de layout da direita para a esquerda (RTL) (Mikhail Listratsenka)

### Linux e Mac OS

- Adicionado um seletor de rotas de transporte público para escolher uma linha específica quando uma parada é selecionada (Viktor Govako)
- Botões de ação de rota exibidos diretamente na página do local (Viktor Govako)
- Removidos os horários de funcionamento duplicados da página do local (Viktor Govako)
- Marca de rota intermediária em um POI ou endereço agora mostra o título do local (Viktor Govako)
- Os downloads de mapas são retomados de onde pararam após um encerramento normal (Alexander Borsuk)
- O Organic Maps agora funciona com drivers OpenGL ES 3.0 (Alexander Borsuk)

Participe dos testes beta para experimentar recursos antecipadamente e relatar problemas:
- [iOS][testflight]
- [Android][firebase]

Amamos nossos usuários ❤️ e amamos o que fazemos

A equipe do Organic Maps

{{ references() }}
