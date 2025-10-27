---
title: "Versión del 23 de octubre: Organic Maps como aplicación de navegación predeterminada en la UE en iOS, visualización de escudos de carreteras en Android y más mejoras y correcciones"
date: 2025-10-23T17:20:21+00:00
slug: "versión-23-octubre-organic-maps-aplicación-navegación-predeterminada-ue-ios-escudos-carreteras-android-mejoras-correcciones"
taxonomies:
  news: ["Releases"]
---

En la versión del 23 de octubre nos centramos en correcciones y mejoras. Consulta la lista detallada a continuación.

Para aquellos que se lo perdieron, la [actualización anterior del 7 de octubre](https://organicmaps.app/news/2025-10-07/android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display/
) agregó importación de GeoJSON, estadísticas de grabación de rutas, visualización del límite de velocidad en Android Auto, visualización de etiquetas de descripción de OSM (escribe `?description` en el cuadro de búsqueda para verlas), guardar un marcador en una ruta en iOS y muchas otras mejoras.

## Todas las plataformas

- Datos frescos de OpenStreetMap del 21 de octubre de 2025 (Viktor Govako)
- Mostrar nombres de entradas/salidas de metro en el mapa (Viktor Govako)
- Nuevos tipos e iconos de POI: estaciones de monitoreo, isletas de tráfico, instalaciones de cura de agua Kneipp, ferrocarriles en miniatura (Viktor Govako), parcelas de camping en estilo al aire libre, terminales de aeropuerto, áreas de juego interiores, tiendas de telecomunicaciones, instalaciones de alquiler de embarcaciones, instalaciones de rampa de deslizamiento, iconos actualizados de eliminación de residuos y vertederos (David Martinez)
- Traducciones de la interfaz de la aplicación en esloveno (Alexander Borsuk) y orientación de voz TTS para navegación (Erik Bucik)
- En algunos dispositivos/pantallas, el mapa en los centros de las ciudades ahora está menos saturado (Viktor Govako)
- Corregidas las rotaciones del mapa en sensores de brújula defectuosos al caminar en modo de navegación peatonal (Viktor Govako)
- Mejora de la información mostrada después de seleccionar un río o segmento de vía fluvial (Viktor Govako)
- Mejor búsqueda de estaciones de carga de vehículos eléctricos con sinónimos mejorados en todos los idiomas (Alexander Borsuk)
- Corregida la búsqueda de emojis con selectores de variantes (Alexander Borsuk)
- Corregidos demasiados resultados de búsqueda mostrados para algunas consultas de coincidencia completa de dirección (Viktor Govako)
- La importación de GeoJSON desde https://umap.openstreetmap.fr/ ahora debería preservar todos los metadatos (Shubh Kesharwani)
- Se admiten colores adicionales para senderos marcados para la capa de mapa de Rutas de Senderismo (Viktor Govako)

## iOS

- Los usuarios de la UE pueden configurar Organic Maps como la aplicación de navegación predeterminada en Ajustes de iOS → Apps → Apps predeterminadas → Navegación (Kiryl Kaveryn)
- Corregida la barra de estado blanco sobre blanco en modo de navegación (Kiryl Kaveryn)
- Aumentado el tamaño del botón Iniciar navegación (Kiryl Kaveryn)
- Eliminado el espacio vacío al planificar una ruta en iPad (Kiryl Kaveryn)
- Organic Maps puede pedirte que lo valores en la App Store. ¡Tus buenas reseñas motivan a nuestro equipo!

## Android

- Los escudos de carreteras ahora aparecen en las direcciones de navegación (Andrei Shkrob)
- Mejoras en la información de grabación de rutas (Kavi Khalique)
- Organic Maps funciona en algunos dispositivos Intel x86 más antiguos (Andrei Shkrob)
- Corregidas las indicaciones de voz TTS que no funcionaban en algunos casos (Andrei Shkrob)
- Mejor pantalla de inicio al arrancar (Andrei Shkrob)

### Android Auto
- Restaurar la ruta después de la cancelación (Andrei Shkrob)
- Corregidos los bloqueos en algunos dispositivos (Andrei Shkrob)

## Linux/Mac OS

- Los detalles de POI ahora muestran el formato "nombre | ref" (Viktor Govako)
- el modo oscuro se sincroniza automáticamente con la configuración del sistema (DeepChirp)

## Notas al pie

Organic Maps es posible gracias ❤️ a nuestros colaboradores, [tus donaciones](@/donate/index.es.md) y [tu apoyo](@/contribute/index.es.md).

Obtén la última versión de Organic Maps desde la [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] y [F-Droid][fdroid].

P.D. Únete a las pruebas beta para obtener funciones anticipadas:
- [iOS][testflight]
- [Android][firebase].

Con amor para nuestros usuarios y comunidad
El equipo de Organic Maps

{{ references() }}
