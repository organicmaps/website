---
title: "Lanzamiento del 15 de septiembre: nueva planificación de rutas y descripciones OSM"
date: 2025-09-15T10:00:00+00:00
---

Esta segunda versión de septiembre trae una pantalla rediseñada de planificación de rutas y la posibilidad de ver el contenido de la etiqueta `description` de OpenStreetMap en iOS. Para encontrar lugares con esta etiqueta, escribe `?description` en la búsqueda (similar a `?wiki`).

También incluye muchas correcciones y mejoras en iOS y Android (detalles abajo).

Funciones recientes que quizá te hayas perdido:
- Números de líneas de transporte público al seleccionar una parada
- Rutas de senderismo y ciclismo (actívalas con el botón Capas arriba a la izquierda)
- Mostrar nombres de marcadores en el mapa (activa en Ajustes)
- El icono ✎ permite editar marcadores rápidamente

Organic Maps es posible gracias a nuestros colaboradores, [tus donaciones](@/donate/index.es.md) y [tu apoyo](@/contribute/index.md).

### Notas detalladas

- Nuevos datos de OpenStreetMap a 13 de septiembre
- Eliminadas islas muy pequeñas del mapa mundial (Viktor Govako)
- Mostrar código postal (ZIP) en los detalles de la dirección (Viktor Govako)
- Corregido centrado incorrecto del mapa en la posición actual (Kiryl Kaveryn, Viktor Govako)
- Conservar colores de marcadores al exportar e importar GPX (cyber-toad)
- Traducciones actualizadas (colaboradores de Weblate)

#### Estilos de mapa (Viktor Govako)

- Mostrar tiendas de iluminación
- Mostrar líneas eléctricas desde zoom 18
- Mostrar referencias de centrales y subestaciones eléctricas
- Mostrar campings y áreas para caravanas en modo navegación
- Corregir color de carreteras secundarias en modo navegación
- Dibujar límites de parques nacionales
- Dibujar sitios arqueológicos desde zoom 12 en estilo Outdoor

#### iOS

- NUEVO: mostrar contenido de la etiqueta OSM `description` (buscar `?description`) (Kiryl Kaveryn, Viktor Govako)
- NUEVO: pantalla de planificación de rutas rediseñada (Kiryl Kaveryn)

#### Android

- Nuevos íconos de rotondas en Android Auto (Andrei Shkrob)
- Mostrar categoría del marcador seleccionado (Alexander Borsuk)
- Corregido retraso al mostrar distancia a un marcador (Alexander Borsuk)
- Tema oscuro reestructurado (Andrei Shkrob)
- Corregida actualización de posición en navegación en ROMs personalizadas (p.ej. Lineage + MicroG) (Viktor Govako)
- Icono de lápiz azul (editar) para marcadores (Alexander Borsuk)
- Reducido espacio vertical en la vista previa de información del lugar (Alexander Borsuk)
- Eliminado ángulo de acimut hacia el norte en la vista previa (toca la flecha azul con la distancia para verlo) (Alexander Borsuk)

Obtén la última versión: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Únete a las betas: [iOS][testflight] / [Android][firebase].

{{ references() }}
