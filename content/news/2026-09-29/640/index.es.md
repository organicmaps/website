---
title: "Optimización de rutas, rutas alternativas mejoradas, ocultación de tracks individuales y zonas de agua intermitentes en la actualización de septiembre de 2026"
date: 2026-09-29
slug: "seleccion-multiple-marcadores-tracks-panel-carplay-ocultar-tracks-enlaces-compartir-agosto-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

¿Listo para salir? La actualización de septiembre incluye rutas alternativas mejoradas, una opción para optimizar el orden de las paradas de la ruta, indicaciones más claras para las zonas con agua intermitente y un icono con forma de ojo para ocultar tracks individuales, además de muchas otras correcciones y mejoras (mira más abajo).

Instala o actualiza Organic Maps a través de <https://get.omaps.org>, la [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] o [F-Droid][fdroid].

Si te has perdido nuestras últimas novedades, echa un vistazo a las funciones lanzadas en [junio](@/news/2026-06-29/610/index.es.md), [julio](@/news/2026-07-23/620/index.es.md) y [agosto](@/news/2026-08-31/630/index.es.md). ¡Muchas gracias a nuestros colaboradores y usuarios, que han hecho posible estas actualizaciones!

## Cómo apoyar a Organic Maps

- [Haz una donación](@/donate/index.es.md) para apoyar el desarrollo y cubrir los gastos de alojamiento de los mapas
- [Envíanos tus comentarios y colabora](@/contribute/index.es.md) con el proyecto
- Únete a las pruebas beta para probar las nuevas funciones antes que nadie e informar de cualquier problema en [iOS][testflight], [Android][firebase] y [la versión de escritorio][flathub]
- ¡Corre la voz y ayúdanos a crear una alternativa mejor a los mapas de las grandes empresas tecnológicas!

## Notas de la versión

### Mapa

- Datos de OpenStreetMap a fecha del 28 de septiembre de 2026
- Datos de Wikipedia a fecha del 21 de septiembre de 2026
- Se han corregido los problemas de búsqueda cuando el área visible del mapa cruza el meridiano de 180° (±180° de longitud) _(Viktor Govako)_
- Las zonas de agua intermitentes ahora se muestran con un patrón de puntos, parecido al que se usa para la arena _(Alexander Borsuk)_
- Ahora se ven los embalses cuando alejas más el zoom _(Alexander Borsuk)_
- Los túneles de agua ya no aparecen en el mapa _(Alexander Borsuk)_
- Se han corregido los iconos de las estaciones y entradas del metro de Suzhou _(Alexander Borsuk)_
- Se han solucionado algunos casos poco frecuentes en los que las etiquetas se desplazaban de su posición en la capa del mapa del metro _(Viktor Govako)_

### Rutas y navegación

- Se han mejorado las rutas alternativas y sus horas estimadas de llegada _(Alexander Borsuk, Viktor Govako)_
- Ahora la ruta alternativa seleccionada se mantiene cuando la navegación vuelve a calcular la ruta _(Alexander Borsuk)_
- Ahora se recupera el orden de las paradas de la ruta tras reiniciar la app _(Kiryl Kaveryn)_

### Otras mejoras

- Ahora los horarios de apertura muestran «Mediodía» para las 12:00 y «Medianoche» para las 00:00 o las 24:00 _(Alexander Borsuk)_
- Se han corregido errores y se ha mejorado la grabación de tracks _(Alexander Borsuk)_
- Se ha solucionado el problema con la importación de archivos KMB _(Alexander Borsuk)_
- Traducciones corregidas al francés y al asturiano _(Alexander Borsuk)_
- Se ha corregido un error tipográfico en inglés _(Carl Morris)_

### iOS

- Se ha añadido un icono con forma de ojo para ocultar tracks individuales _(Kiryl Kaveryn)_
- Se han añadido botones para añadir o sustituir una parada en una ruta planificada _(Kiryl Kaveryn)_
- Se ha añadido una opción para optimizar el orden de las paradas intermedias de la ruta _(Kiryl Kaveryn)_
- Se han añadido instrucciones de maniobra a las pantallas de visualización frontal (HUD) compatibles de los coches y al panel de CarPlay _(Kiryl Kaveryn)_
- Se han corregido los botones y la búsqueda de CarPlay _(Alexander Borsuk)_
- Se han corregido varios errores y se ha mejorado la interfaz de usuario _(Kiryl Kaveryn, Alexander Borsuk)_
- Se ha añadido la posibilidad de elegir y escuchar una muestra de una voz de navegación instalada _(Kiryl Kaveryn, Alexander Borsuk)_
- Se ha restablecido la búsqueda por categorías en Spotlight _(Kiryl Kaveryn)_

### Android

- Se ha añadido una opción para optimizar el orden de las paradas intermedias de la ruta _(Mikhail Listratsenka)_
- Se han añadido botones para añadir o sustituir una parada en una ruta planificada _(Mikhail Listratsenka)_
- Se ha añadido la opción de detener la grabación de un track y guardarlo desde la notificación _(Alexander Borsuk)_
- El botón «Añadir parada» ahora añade una parada después de las paradas existentes, antes del destino _(Mikhail Listratsenka)_
- Se han mejorado las subidas desde el editor de OpenStreetMap _(Owm)_
- Se ha actualizado el diseño de la interfaz de usuario _(Mikhail Listratsenka)_
- El editor de marcadores y otros cuadros de diálogo ahora se mantienen abiertos mientras navegas _(Mikhail Listratsenka)_
- Se ha corregido la representación de los gráficos de elevación para tracks planos y en interfaces de derecha a izquierda _(Mikhail Listratsenka)_
- Se ha solucionado el problema por el que las barras del sistema cortaban los botones del mapa _(Mikhail Listratsenka)_
- Se han corregido errores y se ha mejorado la compatibilidad con Android Auto _(Andrei Shkrob)_
- Se ha solucionado un fallo que provocaba que el programa se colgara durante el renderizado del mapa _(Viktor Govako)_

### Escritorio

- Se han cambiado los nombres del ejecutable de escritorio y del paquete de la aplicación para macOS a `OrganicMaps` _(Alexander Borsuk)_
- Se han solucionado algunos problemas en la aplicación para Windows _(Osyotr, Alexander Borsuk)_
- El parámetro de línea de comandos `--lang` ahora tiene prioridad sobre el ajuste de idioma de la aplicación _(Alexander Borsuk)_

Con alegría y pasión,

Tu equipo de Organic Maps

{{ <references lang /> }}
