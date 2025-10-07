---
title: "Lançamento de outubro: Limites de velocidade no Android Auto, importação GeoJSON, estatísticas de gravação de trilha, exibição da tag de descrição OSM, salvar marcador na trilha selecionada no iOS e mais"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
---

Esta atualização de outubro do Organic Maps adiciona exibição de limite de velocidade no Android Auto, importação de GeoJSON, estatísticas de gravação de trilha, mostra tags de descrição do OSM (digite `?description` na caixa de pesquisa para vê-las) e salva um marcador em uma trilha no iOS. Também há muitas melhorias na interface do usuário, edição do OpenStreetMap e várias correções de bugs em todas as plataformas, incluindo a correção da falha na inicialização em alguns dispositivos Android.

O Organic Maps é possível graças ❤️ aos nossos colaboradores, [suas doações](@/donate/index.pt-BR.md) e [seu apoio](@/contribute/index.pt-BR.md).

### Notas de lançamento detalhadas (incluindo as alterações da atualização menor anterior)

- NOVO! Importação de GeoJSON (Sergiy Kozyr)
- Dados do OpenStreetMap de 4 de outubro
- Dados da Wikipédia de 1º de outubro
- Suporte ao metrô leve de Seattle para transporte público (tjasz)
- Não desativar a seleção do mapa ao salvar um local OSM editado (Kiryl Kaveryn)
- Traduções atualizadas (colaboradores do Weblate)

#### Estilos de mapa

- Mostrar lojas de aluguel de bicicletas marcadas como amenity=bicycle + rental=shop (David Martinez)
- Mostrar sítios arqueológicos históricos a partir do zoom 12 e outros sítios históricos a partir do zoom 15 no estilo Outdoor (Viktor Govako)
- Novos ícones para mastros, comunicação e torres elétricas no estilo Outdoor (David Martinez)
- Aumentar o tamanho do ícone de pico no estilo Outdoor (David Martinez)
- Adicionar variantes de ícones de PDI ausentes (David Martinez)
- Adicionados mais tipos de barreiras (Viktor Govako)

#### iOS

- NOVO: Salvar marcador no ponto de trilha selecionado (Kiryl Kaveryn)
- NOVO: Excluir a trilha de gravação sem salvá-la primeiro (Kiryl Kaveryn)
- Mostrar títulos de lista de marcadores de várias linhas na Página do local (David Martinez)
- Atualizar o estilo dos botões de login do OSM (Kiryl Kaveryn)
- Corrigir problema de atualização de informações de navegação (Kiryl Kaveryn)
- Corrigir problemas de planejamento de nova rota (Kiryl Kaveryn)
- Corrigir a visibilidade de adicionar/editar local do OSM para mapas com mais de 3 meses (Kiryl Kaveryn)
- Corrigir o layout do controle de segmento de opções de transporte para iOS 26 (Kiryl Kaveryn)
- Simplificar as animações de seleção de marcadores (Kiryl Kaveryn)
- Corrigir problema de seleção de resultado de pesquisa (Kiryl Kaveryn)
- Estilo, deslizamento e animações corrigidos para a Página de informações do local (Kiryl Kaveryn)

#### Android Auto (somente Google Play)

- NOVO: Exibição de limite de velocidade no Android Auto (Andrei Shkrob)
- Corrigir a troca de exibição no modo de navegação do Android Auto (Andrei Shkrob)
- Corrigir o deslocamento da seta de rota no Android Auto (Andrei Shkrob)
- Corrigir problema quando um dispositivo é conectado/desconectado a um carro (Andrei Shkrob)
- Adicionar serviço de localização do Android Auto (Andrei Shkrob)
- Melhorar o simulador de rota do Android Auto (Viktor Govako)

#### Android

- NOVO: Ver estatísticas de gravação de trilha em tempo real (Kavi Khalique)
- NOVO: Mostrar o conteúdo da tag `description` do OSM (Alexander Borsuk)
- Corrigir o gerenciamento de mudança de tema (Andrei Shkrob)
- Corrigidas várias falhas, incluindo a na inicialização (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Notificações silenciosas de progresso de download (Viktor Govako)
- Reduzir o preenchimento do ícone de lápis (Alexander Borsuk)

#### Desktop

- Corrigir o travamento do curl no Linux (Alexander Borsuk)
- Corrigir o travamento no macOS ao fazer login no OSM (Alexander Borsuk)
- Ação para selecionar recurso do menu de contexto (Viktor Govako)
- Opção para cancelar o download (Viktor Govako)
- Mostrar tipo de geometria no menu de contexto (Viktor Govako)

### Recursos lançados recentemente que você pode ter perdido

- Números de rota de transporte público ao selecionar um ponto de ônibus
- Rotas de caminhada e ciclismo (ative-as através do botão Camadas no canto superior esquerdo)
- Ver nomes de marcadores no mapa ativando-o nas Configurações do aplicativo
- O ícone de lápis ✎ oferece uma maneira rápida de editar marcadores

### Instalar o Organic Maps

Obtenha a versão mais recente do Organic Maps na [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

Participe dos testes beta para recursos antecipados: [iOS][testflight] / [Android][firebase].

{{ references() }}
