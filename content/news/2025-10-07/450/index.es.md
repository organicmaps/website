---
title: "Lanzamiento de octubre: Límites de velocidad en Android Auto, importación GeoJSON, estadísticas de grabación de rutas, visualización de la etiqueta de descripción OSM, guardar marcadores en la ruta seleccionada en iOS y más"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

Esta actualización de octubre de Organic Maps añade la visualización del límite de velocidad en Android Auto, la importación de GeoJSON, las estadísticas de grabación de rutas, muestra las etiquetas de descripción de OSM (escriba `?description` en el cuadro de búsqueda para verlas) y guarda un marcador en una ruta en iOS. También hay muchas mejoras en la interfaz de usuario, la edición de OpenStreetMap y varias correcciones de errores en todas las plataformas, incluida la corrección del bloqueo al inicio en algunos dispositivos Android.

Organic Maps es posible gracias ❤️ a nuestros colaboradores, [sus donaciones](@/donate/index.es.md) y [su apoyo](@/contribute/index.es.md).

### Notas de lanzamiento detalladas (incluyendo los cambios de la actualización menor anterior)

- ¡NUEVO! Importación de GeoJSON (Sergiy Kozyr)
- Datos de OpenStreetMap del 4 de octubre
- Datos de Wikipedia del 1 de octubre
- Soporte del tren ligero de Seattle para el transporte público (tjasz)
- No desactivar la selección del mapa al guardar un lugar OSM editado (Kiryl Kaveryn)
- Traducciones actualizadas (colaboradores de Weblate)

#### Estilos de mapa

- Mostrar tiendas de alquiler de bicicletas etiquetadas como amenity=bicycle + rental=shop (David Martinez)
- Mostrar sitios arqueológicos históricos desde el zoom 12 y otros sitios históricos desde el zoom 15 en el estilo Exterior (Viktor Govako)
- Nuevos iconos para mástiles, comunicación y torres eléctricas en el estilo Exterior (David Martinez)
- Aumentar el tamaño del icono de pico en el estilo Exterior (David Martinez)
- Añadir variantes de iconos de PDI que faltaban (David Martinez)
- Añadidos más tipos de barreras (Viktor Govako)

#### iOS

- NUEVO: Guardar marcador en el punto de ruta seleccionado (Kiryl Kaveryn)
- NUEVO: Eliminar la ruta de grabación sin guardarla primero (Kiryl Kaveryn)
- Mostrar títulos de lista de marcadores de varias líneas en la Página del lugar (David Martinez)
- Actualizar el estilo de los botones de inicio de sesión de OSM (Kiryl Kaveryn)
- Corregir problema de actualización de información de navegación (Kiryl Kaveryn)
- Corregir problemas de planificación de nuevas rutas (Kiryl Kaveryn)
- Corregir la visibilidad de añadir/editar lugar de OSM para mapas con más de 3 meses (Kiryl Kaveryn)
- Corregir el diseño del control de segmento de opciones de transporte para iOS 26 (Kiryl Kaveryn)
- Simplificar las animaciones de selección de marcadores (Kiryl Kaveryn)
- Corregir problema de selección de resultados de búsqueda (Kiryl Kaveryn)
- Estilo, deslizamiento y animaciones corregidos para la Página de información del lugar (Kiryl Kaveryn)

#### Android Auto (solo Google Play)

- NUEVO: Visualización del límite de velocidad en Android Auto (Andrei Shkrob)
- Corregir el cambio de pantalla en el modo de navegación de Android Auto (Andrei Shkrob)
- Corregir el desplazamiento de la flecha de ruta en Android Auto (Andrei Shkrob)
- Corregir problema cuando un dispositivo se conecta/desconecta de un coche (Andrei Shkrob)
- Añadir servicio de ubicación de Android Auto (Andrei Shkrob)
- Mejorar el simulador de rutas de Android Auto (Viktor Govako)

#### Android

- NUEVO: Ver estadísticas de grabación de rutas en tiempo real (Kavi Khalique)
- NUEVO: Mostrar el contenido de la etiqueta `description` de OSM (Alexander Borsuk)
- Corregir la gestión del cambio de tema (Andrei Shkrob)
- Corregidos varios bloqueos, incluido el del inicio (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Notificaciones silenciosas de progreso de descarga (Viktor Govako)
- Reducir el relleno del icono de lápiz (Alexander Borsuk)

#### Escritorio

- Corregir bloqueo de curl en Linux (Alexander Borsuk)
- Corregir bloqueo en macOS al iniciar sesión en OSM (Alexander Borsuk)
- Acción para seleccionar función desde el menú contextual (Viktor Govako)
- Opción para cancelar la descarga (Viktor Govako)
- Mostrar tipo de geometría en el menú contextual (Viktor Govako)

### Funciones lanzadas recientemente que podría haber perdido

- Números de ruta de transporte público al seleccionar una parada de autobús
- Rutas de senderismo y ciclismo (actívelas con el botón Capas en la esquina superior izquierda)
- Ver nombres de marcadores en el mapa activándolo en la Configuración de la aplicación
- El icono de lápiz ✎ ofrece una forma rápida de editar marcadores

### Instalar Organic Maps

Obtenga la última versión de Organic Maps desde la [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] y [F-Droid][fdroid].

Únase a las pruebas beta para funciones tempranas: [iOS][testflight] / [Android][firebase].

{{ references() }}
