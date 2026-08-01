---
title: "Correcciones de errores y mejoras en el transporte público, el cálculo de rutas, la búsqueda y los marcadores en la actualización de julio de 2026"
date: 2026-07-23
slug: "correcciones-errores-mejoras-transporte-publico-rutas-busqueda-marcadores-julio-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Como quizá ya haya notado, ya está disponible la actualización de julio de Organic Maps. Puede descargarla en <https://get.omaps.org> o en [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] y [F-Droid][fdroid].

Gracias a sus [donaciones](@/donate/index.es.md) y a sus [comentarios](@/contribute/index.es.md), en julio nos hemos centrado en la corrección de errores y en mejoras. Por si se lo ha perdido, también están disponibles las siguientes funciones de la [versión anterior de junio](@/news/2026-06-29/610/index.es.md):
- Rutas de transporte público (se están elaborando los horarios en tiempo real)
- Imágenes por satélite
- Rutas alternativas para ir en coche, hacer senderismo y montar en bicicleta
- Nueva interfaz de búsqueda y planificación de rutas para Android
- Compatibilidad con fuentes grandes para accesibilidad en iOS

## Registro de cambios detallado

### Mapa y lugares
- Datos de OpenStreetMap actualizados a 14 de julio
- Las notas enviadas a [OpenStreetMap](https://www.openstreetmap.org) ahora se colocan exactamente en el lugar que haya seleccionado, en lugar de en el centro de toda la calle o zona _(Alexander Borsuk)_
- Se ha mejorado la selección de lugares al pulsar en el mapa en regiones que cruzan el antimeridiano de 180° _(Viktor Govako)_
- Los perfiles de altitud de los tracks ya no muestran gráficos obsoletos o vacíos tras eliminar un track _(Kiryl Kaveryn)_

### Transporte público
- Los nombres de las paradas, los transbordos y las estaciones ahora tienen un contorno blanco para que se puedan leer tanto en el tema claro como en el oscuro _(Viktor Govako)_
- La capa del metro vuelve a aparecer correctamente tras cerrar la vista previa de una ruta de transporte público _(Mikhail Listratsenka)_

### Rutas y navegación
- Ahora se muestran avisos de ruta (peajes, transbordadores, carreteras sin asfaltar, escalones, etc.) para todas las rutas alternativas _(Viktor Govako)_
- Se ha corregido un fallo poco frecuente que provocaba que el programa se colgara al crear una ruta _(Viktor Govako)_
- Mejora en la gestión de callejones sin salida y de los puntos de inicio y fin en vías con restricciones _(Viktor Govako)_
- Se han corregido las indicaciones de giro incorrectas y que faltaban _(Alexander Borsuk)_

### iOS
- Nueva opción «Guardar historial de búsqueda» que le permite desactivar el historial y ocultarlo si prefiere no conservarlo _(Kiryl Kaveryn)_
- Nuevo botón «Editar» para eliminar marcadores más fácilmente _(Kiryl Kaveryn)_
- Ahora los marcadores se guardan automáticamente al salir de la pantalla _(Kiryl Kaveryn)_
- La paleta de colores ofrece ahora colores predefinidos y le permite elegir cualquier color personalizado _(Kiryl Kaveryn)_
- Se ha mejorado el estado vacío del gráfico de altitud de un track grabado _(Kiryl Kaveryn)_
- Se ha mejorado la visualización del progreso de la ruta que aparece en el botón «Inicio» _(Kiryl Kaveryn)_
- Al reordenar las paradas de una ruta, la lista ya no da saltos _(Kiryl Kaveryn)_
- Otras mejoras menores en la interfaz _(Kiryl Kaveryn)_

### Android
- Los horarios de apertura ahora muestran turnos partidos (como la pausa para comer), empiezan por el día actual y muestran la semana completa sin un área de desplazamiento aparte _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Una barra de búsqueda más limpia, con un botón combinado de borrado y voz, un icono de borrado que ya no se mueve, y correcciones de diseño para el modo horizontal y la rotación del teléfono _(Mikhail Listratsenka)_
- Editor de marcadores y tracks rediseñado _(Mikhail Listratsenka)_
- Correcciones y mejoras en la planificación de rutas _(Mikhail Listratsenka)_
- El selector de colores ahora se cierra automáticamente y se ha solucionado un error que provocaba un bloqueo en Android 5 _(Mikhail Listratsenka)_
- Se han corregido varios cierres inesperados _(Alexander Borsuk, Mikhail Listratsenka)_

### Escritorio
- La lista de mapas disponibles para descargar ya está ordenada alfabéticamente _(goncalo109560)_

### Traducciones
- Redacción en chino mejorada _(Chenxi Zhao)_
- Traducciones al ucraniano actualizadas _(Nnifria)_
- Se han corregido las traducciones al italiano de los nombres de las regiones de los mapas _(Vittorio Bertola)_

## Únase a las pruebas beta para probar funciones anticipadas e informar problemas:

Consejo: ¡la versión beta incluye un nuevo sombreado de relieve, datos de altitud mejorados con opciones en pies y metros, y otras funciones interesantes!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

¡Feliz verano!
El equipo de Organic Maps

{{ references() }}
