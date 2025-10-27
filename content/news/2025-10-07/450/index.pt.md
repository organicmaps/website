---
title: "Lançamento de outubro: Limites de velocidade no Android Auto, importação GeoJSON, estatísticas de gravação de percurso, visualização da etiqueta de descrição OSM, guardar marcador no percurso selecionado no iOS e mais"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

Esta atualização de outubro do Organic Maps adiciona a visualização do limite de velocidade no Android Auto, importação de GeoJSON, estatísticas de gravação de percurso, mostra as etiquetas de descrição do OSM (escreva `?description` na caixa de pesquisa para as ver) e guarda um marcador num percurso no iOS. Também existem muitas melhorias na interface do utilizador, edição do OpenStreetMap e várias correções de erros em todas as plataformas, incluindo a correção da falha no arranque em alguns dispositivos Android.

O Organic Maps é possível graças ❤️ aos nossos colaboradores, [as suas doações](@/donate/index.pt.md) e [o seu apoio](@/contribute/index.pt.md).

### Notas de lançamento detalhadas (incluindo as alterações da atualização menor anterior)

- NOVO! Importação de GeoJSON (Sergiy Kozyr)
- Dados do OpenStreetMap de 4 de outubro
- Dados da Wikipédia de 1 de outubro
- Suporte do comboio ligeiro de Seattle para transportes públicos (tjasz)
- Não desativar a seleção do mapa ao guardar um local OSM editado (Kiryl Kaveryn)
- Traduções atualizadas (colaboradores Weblate)

#### Estilos de mapa

- Mostrar lojas de aluguer de bicicletas etiquetadas como amenity=bicycle + rental=shop (David Martinez)
- Mostrar sítios arqueológicos históricos a partir do zoom 12 e outros sítios históricos a partir do zoom 15 no estilo Exterior (Viktor Govako)
- Novos ícones para mastros, comunicação e torres elétricas no estilo Exterior (David Martinez)
- Aumentar o tamanho do ícone de pico no estilo Exterior (David Martinez)
- Adicionar variantes de ícones de PDI em falta (David Martinez)
- Adicionados mais tipos de barreiras (Viktor Govako)

#### iOS

- NOVO: Guardar marcador no ponto de percurso selecionado (Kiryl Kaveryn)
- NOVO: Eliminar o percurso de gravação sem o guardar primeiro (Kiryl Kaveryn)
- Mostrar títulos de lista de marcadores de várias linhas na Página do local (David Martinez)
- Atualizar o estilo dos botões de início de sessão do OSM (Kiryl Kaveryn)
- Corrigir problema de atualização de informações de navegação (Kiryl Kaveryn)
- Corrigir problemas de planeamento de nova rota (Kiryl Kaveryn)
- Corrigir a visibilidade de adicionar/editar local do OSM para mapas com mais de 3 meses (Kiryl Kaveryn)
- Corrigir o layout do controlo de segmento de opções de transporte para iOS 26 (Kiryl Kaveryn)
- Simplificar as animações de seleção de marcadores (Kiryl Kaveryn)
- Corrigir problema de seleção de resultado de pesquisa (Kiryl Kaveryn)
- Estilo, deslizamento e animações corrigidos para a Página de informações do local (Kiryl Kaveryn)

#### Android Auto (apenas Google Play)

- NOVO: Visualização de limite de velocidade no Android Auto (Andrei Shkrob)
- Corrigir a mudança de visualização no modo de navegação do Android Auto (Andrei Shkrob)
- Corrigir o deslocamento da seta de rota no Android Auto (Andrei Shkrob)
- Corrigir problema quando um dispositivo é ligado/desligado a um carro (Andrei Shkrob)
- Adicionar serviço de localização do Android Auto (Andrei Shkrob)
- Melhorar o simulador de rota do Android Auto (Viktor Govako)

#### Android

- NOVO: Ver estatísticas de gravação de percurso em tempo real (Kavi Khalique)
- NOVO: Mostrar o conteúdo da etiqueta `description` do OSM (Alexander Borsuk)
- Corrigir a gestão de mudança de tema (Andrei Shkrob)
- Corrigidas várias falhas, incluindo a no arranque (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Notificações silenciosas de progresso de transferência (Viktor Govako)
- Reduzir o preenchimento do ícone de lápis (Alexander Borsuk)

#### Computador

- Corrigir o bloqueio do curl no Linux (Alexander Borsuk)
- Corrigir o bloqueio no macOS ao iniciar sessão no OSM (Alexander Borsuk)
- Ação para selecionar funcionalidade do menu de contexto (Viktor Govako)
- Opção para cancelar a transferência (Viktor Govako)
- Mostrar tipo de geometria no menu de contexto (Viktor Govako)

### Funcionalidades lançadas recentemente que pode ter perdido

- Números de rota de transporte público ao selecionar uma paragem de autocarro
- Rotas de caminhada e ciclismo (ative-as através do botão Camadas no canto superior esquerdo)
- Ver nomes de marcadores no mapa ativando-o nas Definições da aplicação
- O ícone de lápis ✎ oferece uma forma rápida de editar marcadores

### Instalar o Organic Maps

Obtenha a versão mais recente do Organic Maps na [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

Participe nos testes beta para funcionalidades antecipadas: [iOS][testflight] / [Android][firebase].

{{ references() }}
