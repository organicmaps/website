---
title: "Imágenes por satélite, rutas de transporte público, rutas alternativas, nueva interfaz de búsqueda y planificación de rutas para Android, compatibilidad con fuentes grandes de accesibilidad en iOS y más en la actualización de junio de 2026"
date: 2026-06-29
slug: "imagenes-satelite-rutas-transporte-publico-rutas-alternativas-nueva-busqueda-planificacion-rutas-android-fuentes-grandes-ios-junio-2026"
taxonomies:
  news: ["releases"]
---

Hay muchas funciones nuevas interesantes y correcciones de errores para probar en la actualización de junio de Organic Maps, entre ellas:
- Imágenes por satélite
- Rutas de transporte público
- Rutas alternativas
- Nueva interfaz de búsqueda y planificación de rutas para Android
- Compatibilidad con fuentes grandes de accesibilidad en iOS

¡Consíguela en <https://get.omaps.org> o en [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] y [F-Droid][fdroid], y cuéntanos qué te parece!

## Registro de cambios detallado

- ¡NUEVO! Planificación de rutas en transporte público con metro, tren ligero, autobús y tranvía _(Viktor Govako)_
- ¡NUEVO! Rutas alternativas: además de la ruta más rápida, la app ahora muestra la ruta más corta _(Viktor Govako)_
- ¡NUEVO! Avisos en rutas a pie y en bicicleta sobre escaleras, puertas y barreras elevables en el camino _(Viktor Govako)_
- ¡NUEVO! Elige cualquier color para los marcadores _(Alexander Borsuk, Mikhail Listratsenka)_
- ¡NUEVO! Compatibilidad con coordenadas British National Grid (OS Grid), Irish Grid e Irish Transverse Mercator (ITM) _(Alexander Borsuk)_
- EXPERIMENTAL: activa las imágenes por satélite en los ajustes de Organic Maps con una URL personalizada de servidor de teselas ráster. Todavía estamos trabajando en nuestro propio servidor, así que busca uno disponible públicamente con los marcadores `{x}`, `{y}`, `{z}` en su URL _(Viktor Govako, renderexpert)_
- Datos de OpenStreetMap actualizados al 24 de junio _(Viktor Govako)_
- Datos de Wikipedia actualizados al 20 de junio, incluidos artículos en italiano _(Alexander Borsuk)_
- Escribe `?map-download-server:https://your-server.com/` en la ventana de búsqueda para sustituir los servidores de descarga de mapas de Organic Maps. Escribe `?no-map-download-server` para quitar la sustitución _(Alexander Borsuk)_

#### Renderizado y estilos del mapa

- Patrones más atractivos para zonas de playa, arena, pedrera, roca desnuda, huertos y viñedos, además de tramado para áreas protegidas y humedales _(Alexander Borsuk)_
- Etiquetas de texto curvas más suaves para carreteras y ríos _(Viktor Govako)_
- Ríos, arroyos y humedales tienen más contraste y se ven mejor en modo oscuro _(Alexander Borsuk)_
- Iconos nuevos y mejorados para la búsqueda por categorías y los resultados de búsqueda en el mapa _(Anton Makouski)_
- Mejor modelado y renderizado de texto multilingüe _(Alexander Borsuk)_
- Varias correcciones de errores y mejoras de rendimiento _(Viktor Govako)_

#### Tracks, marcadores y rutas

- Los tracks GeoJSON ahora conservan la elevación y las marcas de tiempo al importar y exportar _(Alexander Borsuk)_
- Corregido un cierre inesperado después de mover un track a otra lista _(Viktor Govako)_
- Ahora se muestran sitios web para lugares patrimoniales _(Viktor Govako)_
- Ahora se muestran los nombres de operadores para resultados de búsqueda sin nombre. Por ejemplo, un cajero automático sin nombre ahora muestra su banco _(Anton Makouski)_
- Editor: corregido el texto descriptivo de ediciones/changesets de OpenStreetMap para edificios de apartamentos _(titanniya542-spec)_
- Mejor detección de HTML en descripciones de marcadores y tracks _(Alexander Borsuk)_

### iOS

- ¡NUEVO! Compatibilidad de accesibilidad con Dynamic Type y fuentes grandes _(Kiryl Kaveryn)_
- ¡NUEVO! Toca para elegir entre tracks y rutas superpuestos _(Kiryl Kaveryn)_
- Mejor renderizado HTML de las descripciones de marcadores y tracks _(Kiryl Kaveryn)_
- Estilo de tablas más limpio en la interfaz _(Kiryl Kaveryn)_

### Android

- ¡NUEVO! Interfaz de búsqueda _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- ¡NUEVO! Interfaz de planificación de rutas _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- Mejor renderizado HTML de las descripciones de marcadores y tracks _(Mikhail Listratsenka)_
- Tamaño del APK reducido _(Alexander Borsuk)_
- El icono de voz se muestra como desactivado cuando no hay ningún motor de texto a voz disponible _(Mikhail Listratsenka)_
- Las descripciones largas de marcadores y tracks ahora muestran un botón «…más» _(Mikhail Listratsenka)_
- Varias correcciones de interfaz y una corrección de API para los ID de puntos devueltos _(Mikhail Listratsenka)_

### Escritorio

- Compatibilidad para cambiar el sistema de coordenadas mostrado _(Alexander Borsuk)_
- La información sobre el lugar seleccionado ahora se muestra a la izquierda _(Viktor Govako)_
- Corregida la posición del menú contextual _(Osyotr)_
- Corregidos bloqueos del inicio de sesión y las ediciones de OpenStreetMap en versiones de Qt 6.4 y anteriores _(Alexander Borsuk)_
- Corregido un cambio inesperado de estilo del mapa durante la navegación en macOS _(Alexander Borsuk)_
- Corregido un cierre inesperado al cerrar la app de macOS después de exportar un archivo KMZ _(Alexander Borsuk)_

### Traducciones

- Indicaciones de voz paso a paso en cantonés _(Alexander Borsuk)_
- Traducciones al alemán y al francés actualizadas _(Wuzzy, Alexander Borsuk)_
- Corregidas traducciones incorrectas de indicaciones de voz «onto street» para chino, serbio y catalán _(Alexander Borsuk)_

## Únete a las pruebas beta para probar funciones anticipadas e informar problemas:

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Agradecemos a todos nuestros usuarios y colaboradores, a quienes [donan](@/donate/index.es.md) y dan 5 estrellas a Organic Maps en las tiendas de apps. ¡Juntos podemos crear la mejor app de mapas!

Con cariño,
El equipo de Organic Maps

{{ references() }}
