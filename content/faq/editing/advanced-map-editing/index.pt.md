---
title: Como posso fazer uma edição de mapa mais avançada?
slug: como-posso-fazer-uma-edição-de-mapa-mais-avançada
description: Tutorial para edição do OpenStreetMap com ferramentas mais avançadas
  como ID, Go Map e Vespucci
updated: '2024-06-20'
taxonomies:
  faq: ["edição-de-mapas"]
extra:
  order: 40
aliases:
  - /pt/faq/editing/advanced-map-editing/
---

Organic Maps inclui um editor simples e fácil de usar que podes usar para editar o mapa. O editor é, no entanto, limitado e só permite adicionar recursos de pontos simples, o que significa que não há contornos de edifícios, estradas, lagos, cidades, etc. Se quiseres alterar algo que não pode ser editado com o editor integrado, esta é a página de FAQ certa para ler.

Como todos os dados do mapa usados ​​no Organic Maps vêm de [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), podes atualizar o mapa diretamente lá. As tuas modificações serão incluídas no Organic Maps na próxima atualização do mapa.

## Editores do OpenStreetMap

Para editar o OSM, existem várias opções. Se tiveres um laptop ou desktop em mãos, é melhor usar o [ID Editor](https://www.openstreetmap.org/edit) que roda no teu navegador. O ID Editor é fácil para iniciantes, e uma tela maior, mouse e teclado facilitam a edição de mapas.

Para edição avançada de mapas em um dispositivo móvel, usa [Go Map](https://apps.apple.com/us/app/go-map/id592990211) para iOS ou [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) para Android. Go Map é fácil para iniciantes, enquanto Vespucci é voltado para usuários mais avançados. LearnOSM fornece tutoriais para [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) e [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Para edições mais simples e mais divertidas, também podes experimentar o [aplicativo Every Door](https://every-door.app/) para iOS e Android e o [aplicativo StreetComplete](https://streetcomplete.app/) para Android.

#### ID Editor

Para editar o OpenStreetMap com ID segue estes passos:

1. Cria uma nova conta ou faz login em [OpenStreetMap.org](https://www.openstreetmap.org)
2. Navega até o local que desejas editar no OpenStreetMap.org e clica em *Editar* na parte superior
3. *Inicia o Passo a passo* e segue o breve tutorial que explica o ID Editor
4. Edita o mapa
5. Envia as tuas alterações

É isso, agora fazes parte da comunidade OSM.

## O que acontece com minhas edições?

Assim que pressionares *Upload*, as tuas alterações serão adicionadas instantaneamente ao banco de dados público do OSM. Portanto, sê atencioso ao editar. No Organic Maps, as tuas alterações ficarão visíveis após a próxima atualização mensal do mapa.

O teu e-mail não será publicado, mas outras pessoas poderão ver o teu nome de usuário OSM. Como o OSM oferece a possibilidade de discutir alterações, poderás receber perguntas sobre as tuas edições de outros contribuidores do OSM. Serás notificado sobre isso através do endereço de e-mail que utilizaste para registrar a tua conta OSM. Como o OSM é um projeto comunitário que se baseia na colaboração, deves sempre responder a essas perguntas.

## Comunidade e Wiki

OpenStreetMap é uma comunidade. Se precisares de ajuda ou tiveres alguma dúvida, podes perguntar no [Fórum OSM](https://community.openstreetmap.org/c/help-and-support) ou dar uma olhada na documentação do [OSM Wiki](https://wiki.openstreetmap.org/).

## Tags - Como funciona o modelo de dados OSM

O banco de dados OpenStreetMap contém objetos como nós, caminhos, áreas e relações que abstraem recursos do mundo real. Esses objetos possuem atributos, chamados Tags para descrevê-los melhor. Uma tag é uma combinação de valor-chave.

Como isso parece mais complicado do que é, daremos um exemplo:
Um restaurante é, por ex. mapeado como uma Nota ou Área com a Tag `amenity=restaurant`. Outras tags como `cuisine=*` ou `opening_hours=*` podem então ser usadas para obter mais detalhes.

> Observa que o ID editor oculta a estrutura de dados interna dos usuários para ser mais amigável para iniciantes. Mas, para ler a documentação do Wiki, é útil ter uma breve visão geral da estrutura de dados.
No ID Editor, podes ver as tags que o ID está escondendo de ti expandindo a seção *Tags* no painel lateral *Recurso de edição*.

## Notas OSM {#osm-note}

Se não tens tempo ou o problema é muito complicado para editar os dados do OSM tu mesmo, as Notas do OSM ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) são a melhor opção. Podes colocar essa nota no local do erro do mapa e descrever o problema em detalhes. Outros voluntários do OSM podem então ajudar e resolver o problema. Receberás notificações por e-mail através da tua conta OSM caso tenham mais dúvidas ou a Nota OSM seja resolvida.

1. Cria uma nova conta ou faz login em [OpenStreetMap.org](https://www.openstreetmap.org)
   > Também podes abrir Notas anônimas, mas isso não é recomendado, pois não serás notificado quando o problema for resolvido ou houver mais dúvidas.
2. Amplia a localização do mapa em [OpenStreetMap.org](https://www.openstreetmap.org) e pressiona *Adicionar uma nota ao mapa* (segundo ícone da parte inferior no menu direito). Em seguida, arrasta o marcador azul do mapa para o local exato.
   > Tenta ser o mais preciso possível.
3. Fornece uma descrição detalhada do problema do mapa e pressiona *Adicionar Nota*
   > Para lojas, por ex. fornece o nome e menciona o que ali é vendido ou quais serviços são oferecidos.
