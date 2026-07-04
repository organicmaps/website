---
title: "Imaxes de satélite, rutas de transporte público, rutas alternativas, nova interface de busca e planificación de rutas para Android, compatibilidade con fontes grandes de accesibilidade para iOS e máis na actualización de xuño de 2026"
date: 2026-06-29
slug: "imaxes-satelite-rutas-transporte-publico-rutas-alternativas-nova-interface-busca-planificacion-rutas-android-fontes-grandes-accesibilidade"
taxonomies:
  news: ["releases"]
---

Hai moitas funcións novas interesantes e correccións de erros para probar na actualización de xuño de Organic Maps, incluíndo:
- Imaxes de satélite
- Rutas de transporte público
- Rutas alternativas
- Nova interface de busca e planificación de rutas para Android
- Compatibilidade con fontes grandes de accesibilidade para iOS

Conséguea en <https://get.omaps.org> ou na [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid], e cóntanos que che parece!

## Rexistro de cambios detallado

- NOVO! Planificación de rutas en transporte público con metro, tren lixeiro, autobús e tranvía _(Viktor Govako)_
- NOVO! Rutas alternativas: ademais da ruta máis rápida, a aplicación agora mostra a ruta máis curta _(Viktor Govako)_
- NOVO! Avisos nas rutas a pé e en bicicleta sobre escaleiras, portas e barreiras ao longo do camiño _(Viktor Govako)_
- NOVO! Escolle calquera cor para os marcadores _(Alexander Borsuk, Mikhail Listratsenka)_
- NOVO! Compatibilidade coas coordenadas British National Grid (OS Grid), Irish Grid e Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTAL: Activa as imaxes de satélite na configuración de Organic Maps cun URL personalizado dun servidor de teselas ráster. Aínda estamos a traballar no noso propio servidor, así que procura un dispoñible publicamente con marcadores de posición `{x}`, `{y}`, `{z}` no seu URL _(Viktor Govako, renderexpert)_
- Datos de OpenStreetMap actualizados a 24 de xuño _(Viktor Govako)_
- Datos da Wikipedia actualizados a 20 de xuño, incluídos artigos en italiano _(Alexander Borsuk)_
- Escribe `?map-download-server:https://your-server.com/` na xanela de busca para substituír os servidores de descarga de mapas de Organic Maps. Escribe `?no-map-download-server` para eliminar a substitución _(Alexander Borsuk)_

#### Representación do mapa e estilos

- Patróns máis atractivos para zonas de praia, area, pedregal, rocha espida, pomares e viñedos, ademais de raiados para áreas protexidas e zonas húmidas _(Alexander Borsuk)_
- Etiquetas de texto curvas máis suaves para estradas e ríos _(Viktor Govako)_
- Os ríos, regatos e zonas húmidas teñen máis contraste e son máis visibles no modo escuro _(Alexander Borsuk)_
- Iconas novas e melloradas para a busca por categorías e os resultados de busca no mapa _(Anton Makouski)_
- Composición e representación de texto multilingüe melloradas _(Alexander Borsuk)_
- Varias correccións de erros e melloras de rendemento _(Viktor Govako)_

#### Tracks, marcadores e rutas

- Os tracks GeoJSON agora conservan a elevación e as marcas de tempo ao importar e exportar _(Alexander Borsuk)_
- Corrixiuse un fallo despois de mover un track a outra lista _(Viktor Govako)_
- Agora móstranse os sitios web dos lugares patrimoniais _(Viktor Govako)_
- Agora móstranse os nomes dos operadores nos resultados de busca sen nome. Por exemplo, un caixeiro automático sen nome agora mostra o seu banco _(Anton Makouski)_
- Editor: corrixiuse o texto de descrición para as edicións/conxuntos de cambios de OpenStreetMap de edificios de apartamentos _(titanniya542-spec)_
- Mellorouse a detección de HTML nas descricións de marcadores e tracks _(Alexander Borsuk)_

### iOS

- NOVO! Compatibilidade de accesibilidade con Dynamic Type e fontes grandes _(Kiryl Kaveryn)_
- NOVO! Toca para escoller entre tracks e rutas solapados _(Kiryl Kaveryn)_
- Mellorouse a representación de HTML nas descricións de marcadores e tracks _(Kiryl Kaveryn)_
- Estilo de táboas máis limpo na IU _(Kiryl Kaveryn)_

### Android

- NOVO! Interface de busca _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- NOVO! Interface de planificación de rutas _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Mellorouse a representación de HTML nas descricións de marcadores e tracks _(Mikhail Listratsenka)_
- Reduciuse o tamaño do APK _(Alexander Borsuk)_
- A icona de voz móstrase como desactivada cando non hai ningún motor de texto a voz dispoñible _(Mikhail Listratsenka)_
- As descricións longas de marcadores e tracks agora mostran un botón «…máis» _(Mikhail Listratsenka)_
- Varias correccións da IU e unha corrección da API para os IDs de puntos devoltos _(Mikhail Listratsenka)_

### Escritorio

- Compatibilidade para cambiar o sistema de coordenadas mostrado _(Alexander Borsuk)_
- Agora a información sobre o lugar seleccionado móstrase á esquerda _(Viktor Govako)_
- Corrixiuse a posición do menú contextual _(Osyotr)_
- Corrixiuse o bloqueo do inicio de sesión e das edicións de OpenStreetMap nas versións de Qt 6.4 e anteriores _(Alexander Borsuk)_
- Corrixiuse un cambio inesperado do estilo do mapa durante a planificación de rutas en macOS _(Alexander Borsuk)_
- Corrixiuse un fallo ao pechar a aplicación de macOS despois de exportar un ficheiro KMZ _(Alexander Borsuk)_

### Traducións

- Guía de voz paso a paso en cantonés _(Alexander Borsuk)_
- Traducións ao alemán e ao francés actualizadas _(Wuzzy, Alexander Borsuk)_
- Corrixíronse as traducións incorrectas da guía de voz «onto street» para chinés, serbio e catalán _(Alexander Borsuk)_

## Únete ás probas beta para probar funcións anticipadas e informar de problemas:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Agradecemos a todos os nosos usuarios e colaboradores, ás persoas que [doan](@/donate/index.gl.md) e que dan 5 estrelas a Organic Maps nas tendas de aplicacións. Xuntos podemos crear a mellor aplicación de mapas!

Con agarimo,
O equipo de Organic Maps

{{ references() }}
