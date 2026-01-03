---
title: Como posso fazer uma edição de mapa mais avançada?
slug: como-posso-fazer-uma-edição-de-mapa-mais-avançada
description: Tutorial para edição do OpenStreetMap com ferramentas mais avançadas
  como ID, Go Map e Vespucci
updated: '2024-06-20'
taxonomies:
  faq: ["Edição de mapas"]
extra:
  order: 40
aliases:
  - /pt-BR/faq/editing/advanced-map-editing/
---

Organic Maps inclui um editor simples e fácil de usar que você pode usar para editar o mapa. O editor é, no entanto, limitado e só permite adicionar recursos de pontos simples, o que significa que não há contornos de edifícios, estradas, lagos, cidades, etc. Se você quiser alterar algo que não pode ser editado com o editor integrado, esta é a página de FAQ certa para ler.

Como todos os dados do mapa usados ​​nos Mapas Orgânicos vêm de [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), você pode atualizar o mapa diretamente lá. Suas modificações serão incluídas nos Mapas Orgânicos na próxima atualização do mapa.

## Editores do OpenStreetMap

Para editar o OSM, existem várias opções. Se você tiver um laptop ou desktop em mãos, é melhor usar o [Editor de ID](https://www.openstreetmap.org/edit) que roda em seu navegador. O ID Editor é fácil para iniciantes, e uma tela maior, mouse e teclado facilitam a edição de mapas.

Para edição avançada de mapas em um dispositivo móvel, use [Go Map](https://apps.apple.com/us/app/go-map/id592990211) para iOS ou [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) para Android. Go Map é fácil para iniciantes, enquanto Vespucci é voltado para usuários mais avançados. LearnOSM fornece tutoriais para [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) e [Vespucci](https://leanosm.org/en/mobile-mapping/vespucci/).

Para edições mais simples e mais divertidas, você também pode experimentar o [aplicativo Every Door](https://every-door.app/) para iOS e Android e o [aplicativo StreetComplete](https://streetcomplete.app/) para Android.

####Editor de IDs

Para editar o OpenStreetMap com ID siga estes passos:

1. Crie uma nova conta ou faça login em [OpenStreetMap.org](https://www.openstreetmap.org)
2. Navegue até o local que deseja editar no OpenStreetMap.org e clique em *Editar* na parte superior
3. *Inicie o Passo a passo* e siga o breve tutorial que explica o ID Editor
4. Edite o mapa
5. Envie suas alterações

É isso, agora você faz parte da comunidade OSM.

## O que acontece com minhas edições?

Assim que você pressionar *Upload*, suas alterações serão adicionadas instantaneamente ao banco de dados público do OSM. Portanto, seja atencioso ao editar. Nos Mapas Orgânicos, suas alterações ficarão visíveis após a próxima atualização mensal do mapa.

Seu e-mail não será publicado, mas outras pessoas poderão ver seu nome de usuário OSM. Como o OSM oferece a possibilidade de discutir alterações, você poderá receber perguntas sobre suas edições de outros contribuidores do OSM. Você será notificado sobre isso através do endereço de e-mail que utilizou para registrar sua conta OSM. Como o OSM é um projeto comunitário que se baseia na colaboração, você deve sempre responder a essas perguntas.

## Comunidade e Wiki

OpenStreetMap é uma comunidade. Se precisar de ajuda ou tiver alguma dúvida, você pode perguntar no [Fórum OSM](https://community.openstreetmap.org/c/help-and-support) ou dar uma olhada na documentação do [OSM Wiki](https://wiki.openstreetmap.org/).

## Tags - Como funciona o modelo de dados OSM

O banco de dados OpenStreetMap contém objetos como nós, caminhos, áreas e relações que abstraem recursos do mundo real. Esses objetos possuem atributos, chamados Tags para descrevê-los melhor. Uma tag é uma combinação de valor-chave.

Como isso parece mais complicado do que é, daremos um exemplo:
Um restaurante é, por ex. mapeado como uma Nota ou Área com a Tag ``` amenity=restaurant```. Outras tags como ```cousine=*``` ou ```opening_hours=*``` podem então ser usadas para obter mais detalhes.

> Observe que o editor de ID oculta a estrutura de dados interna dos usuários para ser mais amigável para iniciantes. Mas, para ler a documentação do Wiki, é útil ter uma breve visão geral da estrutura de dados.
No Editor de ID, você pode ver as tags que o ID está escondendo de você expandindo a seção *Tags* no painel lateral *Recurso de edição*.

## Notas OSM {#osm-note}

Se você não tem tempo ou o problema é muito complicado para editar os dados do OSM você mesmo, as Notas do OSM ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)) são a melhor opção. Você pode colocar essa nota no local do erro do mapa e descrever o problema em detalhes. Outros voluntários do OSM podem então ajudar e resolver o problema. Você receberá notificações por e-mail através da sua conta OSM caso tenham mais dúvidas ou a Nota OSM seja resolvida.

1. Crie uma nova conta ou faça login em [OpenStreetMap.org](https://www.openstreetmap.org)
   > Você também pode abrir Notas anônimas, mas isso não é recomendado, pois você não será notificado quando o problema for resolvido ou houver mais dúvidas.
2. Amplie a localização do mapa em [OpenStreetMap.org](https://www.openstreetmap.org) e pressione *Adicionar uma nota ao mapa* (segundo ícone da parte inferior no menu direito). Em seguida, arraste o marcador azul do mapa para o local exato.
   > Tente ser o mais preciso possível.
3. Forneça uma descrição detalhada do problema do mapa e pressione *Adicionar Nota*
   > Para lojas, por ex. forneça o nome e mencione o que ali é vendido ou quais serviços são oferecidos.
