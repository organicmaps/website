---
title: "Correccións de erros e melloras no transporte público, nas rutas, na busca e nos marcadores na actualización de xullo de 2026"
date: 2026-07-23
slug: "correccions-erros-melloras-transporte-publico-rutas-busca-marcadores-xullo-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Como quizá xa puido notar, xa está dispoñible a actualización de xullo de Organic Maps. Descárguea en <https://get.omaps.org> ou nas páxinas [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

Grazas ás súas [doazóns](@/donate/index.gl.md) e [comentarios](@/contribute/index.gl.md), en xullo centrámonos en correccións de erros e melloras. No caso de que o perdese, as seguintes funcións da [versión anterior de xuño](@/news/2026-06-29/610/index.gl.md) tamén están dispoñibles:
- Rutas de transporte público (os horarios en tempo real están en desenvolvemento)
- Imaxes por satélite
- Rutas alternativas para conducir, facer sendeirismo e andar en bicicleta
- Nova interface de busca e planificación de rutas para Android
- Soporte para fontes de accesibilidade de gran tamaño en iOS

## Rexistro de cambios detallado

### Mapa e lugares

- Datos de OpenStreetMap actualizados a 14 de xullo
- As notas enviadas a [OpenStreetMap](https://www.openstreetmap.org) colócanse agora no punto exacto que seleccionou, en lugar de no medio de toda a rúa ou zona _(Alexander Borsuk)_
- Mellorouse a selección de lugar ao tocar o mapa en rexións que cruzan o antimeridiano de 180° _(Viktor Govako)_
- Os perfís de elevación dos tracks xa non amosan gráficos obsoletos ou baleiros despois de eliminar un track _(Kiryl Kaveryn)_

### Transporte público

- Os nomes das paradas, transbordos e estacións agora teñen un contorno branco para manterse lexibles tanto en temas claros como escuros _(Viktor Govako)_
- A capa do metro reaparece correctamente despois de pechar unha vista previa dunha ruta de transporte público _(Mikhail Listratsenka)_

### Rutas e navegación

- Os avisos de ruta (peaxes, ferries, estradas non asfaltadas, escaleiras, etc.) móstranse agora para todas as rutas alternativas _(Viktor Govako)_
- Arranxouse un bloqueo pouco frecuente ao construír unha ruta _(Viktor Govako)_
- Mellor xestión de rúas sen saída e dos puntos de inicio e fin en estradas restrinxidas _(Viktor Govako)_
- Corrixíronse as instrucións de xiro incorrectas e ausentes _(Alexander Borsuk)_

### iOS

- Nova opción «Gardar historial de buscas» que lle permite desactivar o historial e ocultalo se prefire non gardalo _(Kiryl Kaveryn)_
- Novo botón «Editar» para eliminar marcadores máis facilmente _(Kiryl Kaveryn)_
- Os marcadores gárdanse agora automaticamente cando sae da pantalla _(Kiryl Kaveryn)_
- A paleta de cores agora ofrece cores predefinidas e permítelle escoller calquera cor personalizada _(Kiryl Kaveryn)_
- Mellorouse o estado baleiro do gráfico de elevacións dun track gravado _(Kiryl Kaveryn)_
- Mellorouse o progreso da ruta que se mostra no botón «Iniciar» _(Kiryl Kaveryn)_
- Reordenar as paradas da ruta xa non fai que a lista salte _(Kiryl Kaveryn)_
- Outras melloras menores na interface _(Kiryl Kaveryn)_

### Android

- O horario de apertura agora mostra quendas partidas (como o descanso para xantar), comeza polo día actual e amosa toda a semana sen unha área de desprazamento á parte _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Barra de busca máis limpa cun botón combinado de borrado e voz, unha icona de borrado que xa non se move, e correccións de deseño para o modo horizontal e a rotación do teléfono _(Mikhail Listratsenka)_
- Reestruturado o editor de marcadores e tracks _(Mikhail Listratsenka)_
- Correccións e melloras na planificación de rutas _(Mikhail Listratsenka)_
- O selector de cores péchase agora automaticamente e arranxouse un fallo en Android 5 _(Mikhail Listratsenka)_
- Arranxáronse varios peches inesperados _(Alexander Borsuk, Mikhail Listratsenka)_

### Escritorio

- A lista de mapas dispoñibles para descargar está agora ordenada alfabeticamente _(goncalo109560)_

### Traducións

- Mellorada a redacción en chinés _(Chenxi Zhao)_
- Traducións ucraínas actualizadas _(Nnifria)_
- Corrixíronse as traducións italianas dos nomes das rexións do mapa _(Vittorio Bertola)_

## Únase ás probas beta para probar funcións anticipadas e informar de problemas:

Pista: a versión beta ten un novo sombreado do relevo, datos de elevación mellorados con soporte para pés e metros, e outras funcións xeniais!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Feliz verán!
O equipo de Organic Maps

{{ references() }}
