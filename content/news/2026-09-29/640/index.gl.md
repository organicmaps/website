---
title: "Optimización da ruta, rutas alternativas melloradas, ocultación de tracks individuais e zonas de auga intermitente na actualización de setembro de 2026"
date: 2026-09-29
slug: "seleccion-multiple-marcadores-tracks-panel-carplay-ocultar-tracks-ligazons-compartir-agosto-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

Todo listo para saír? A actualización de setembro trae rutas alternativas melloradas, un axuste para optimizar a orde das paradas da ruta, marcas máis claras para as zonas de auga intermitente e unha icona de ollo para ocultar tracks individuais, xunto con moitas outras correccións e melloras (ver máis abaixo).

Instala ou actualiza Organic Maps a través de <https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ou [F-Droid][fdroid].

Se perdiches as nosas actualizacións anteriores, bota unha ollada ás funcións publicadas en [xuño](@/news/2026-06-29/610/index.gl.md), [xullo](@/news/2026-07-23/620/index.gl.md) e [agosto](@/news/2026-08-31/630/index.gl.md). Moitas grazas aos nosos colaboradores e usuarios que fixeron posibles estas actualizacións!

## Como apoiar Organic Maps

- [Doa](@/donate/index.gl.md) para apoiar o desenvolvemento e cubrir os custos de aloxamento do mapa
- [Envía os teus comentarios e contribúe](@/contribute/index.gl.md) ao proxecto
- Participa nas probas beta para probar as novas funcións canto antes e informar de problemas en [iOS][testflight], [Android][firebase] e [escritorio][flathub].
- Espalla a nova e axúdanos a construír unha alternativa mellor aos mapas das grandes empresas tecnolóxicas!

## Notas de versión

### Mapa

- Datos de OpenStreetMap a 28 de setembro de 2026
- Datos de Wikipedia a 21 de setembro de 2026
- Solucionouse o problema das buscas cando a área visible do mapa cruzaba o meridiano 180° (lonxitude ±180°) _(Viktor Govako)_
- As áreas de auga intermitentes móstranse agora cun patrón de puntos, similar ao empregado para a area _(Alexander Borsuk)_
- Os encoros son agora visibles cando afastas máis a vista do mapa _(Alexander Borsuk)_
- Os túneles de auga xa non aparecen no mapa _(Alexander Borsuk)_
- Corrixíronse as iconas das estacións e das entradas do metro de Suzhou _(Alexander Borsuk)_
- Solucionáronse casos raros nos que as etiquetas se desprazaban da súa posición na capa do mapa do metro _(Viktor Govako)_

### Planificación de rutas e navegación

- Melloráronse as rutas alternativas e as súas horas estimadas de chegada _(Alexander Borsuk, Viktor Govako)_
- A ruta alternativa seleccionada consérvase agora cando a navegación recalcula a ruta _(Alexander Borsuk)_
- A orde das paradas da ruta restáurase agora despois de reiniciar a aplicación _(Kiryl Kaveryn)_

### Outras melloras

- Os horarios de apertura agora amosan «Mediodía» para as 12:00 e «Medianoite» para as 00:00 ou 24:00 _(Alexander Borsuk)_
- Solucionáronse erros e mellorouse a gravación de tracks _(Alexander Borsuk)_
- Solucionouse a importación de ficheiros KMB _(Alexander Borsuk)_
- Traducións corrixidas ao francés e asturiano _(Alexander Borsuk)_
- Corrixiuse un erro tipográfico en inglés _(Carl Morris)_

### iOS

- Engadiuse unha icona de ollo para ocultar tracks individuais _(Kiryl Kaveryn)_
- Engadíronse botóns para engadir ou substituír unha parada nunha ruta planificada _(Kiryl Kaveryn)_
- Engadiuse un axuste para optimizar a orde das paradas intermedias da ruta _(Kiryl Kaveryn)_
- Engadíronse instrucións de manobra ás pantallas head-up (HUD) dos vehículos compatibles e ao cadro de instrumentos de CarPlay _(Kiryl Kaveryn)_
- Corrixíronse os botóns e a busca de CarPlay _(Alexander Borsuk)_
- Arranxáronse varios erros e mellorouse a interface de usuario _(Kiryl Kaveryn, Alexander Borsuk)_
- Engadiuse a posibilidade de escoller unha voz de navegación instalada e escoitar unha mostra dela _(Kiryl Kaveryn, Alexander Borsuk)_
- Restaurada a busca por categoría en Spotlight _(Kiryl Kaveryn)_

### Android

- Engadiuse unha configuración para optimizar a orde das paradas intermedias da ruta _(Mikhail Listratsenka)_
- Engadíronse botóns para engadir ou substituír unha parada nunha ruta planificada _(Mikhail Listratsenka)_
- Engadiuse a posibilidade de deter a gravación dun track e gardalo desde a notificación _(Alexander Borsuk)_
- O botón «Engadir parada» engade agora unha parada despois das paradas existentes, antes do destino _(Mikhail Listratsenka)_
- Melloras nas subidas desde o editor de OpenStreetMap _(Owm)_
- Actualizouse o deseño da interface de usuario _(Mikhail Listratsenka)_
- O editor de marcadores e outros cadros de diálogo agora permanecen abertos durante a navegación _(Mikhail Listratsenka)_
- Corrixiuse a representación do gráfico de elevación para tracks planos e en interfaces de dereita a esquerda _(Mikhail Listratsenka)_
- Corrixiuse o problema que facía que as barras do sistema recortasen os botóns do mapa _(Mikhail Listratsenka)_
- Arranxáronse erros e mellorouse o soporte de Android Auto _(Andrei Shkrob)_
- Solucionouse un fallo da aplicación durante a representación do mapa _(Viktor Govako)_

### Escritorio

- Renomeouse o executábel de escritorio e o paquete de aplicacións para macOS a `OrganicMaps` _(Alexander Borsuk)_
- Solucionáronse problemas na aplicación de Windows _(Osyotr, Alexander Borsuk)_
- O argumento de liña de comandos `--lang` agora anula o idioma da aplicación _(Alexander Borsuk)_

Con ledicia e paixón,

O teu equipo de Organic Maps

{{ <references lang /> }}
