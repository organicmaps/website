---
title: "Lanzamento 15 de setembro: novo deseño de rutas e descricións OSM"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

Esta segunda versión de setembro trae unha pantalla de planificación de rutas redeseñada e a posibilidade de ver o contido da etiqueta `description` de OpenStreetMap en iOS. Para atopar lugares con esa etiqueta escribe `?description` na busca (similar a `?wiki`).

Inclúe tamén moitas correccións e melloras en iOS e Android (detalles abaixo).

Funcionalidades recentes que quizais non viseches:
- Números de liñas de transporte público ao seleccionar unha parada
- Rutas de sendeirismo e ciclismo (actívaas co botón Capas arriba á esquerda)
- Amosar nomes dos marcadores no mapa (activa en Axustes)
- A icona ✎ permite editar marcadores rapidamente

Organic Maps é posible grazas ás persoas colaboradoras, [ás túas doazóns](@/donate/index.gl.md) e [ao teu apoio](@/contribute/index.md).

### Notas detalladas

- Novos datos de OpenStreetMap a 13 de setembro
- Eliminadas illas moi pequenas do mapa mundial (Viktor Govako)
- Amosar código postal (ZIP) nos detalles do enderezo (Viktor Govako)
- Corrixido centrado incorrecto do mapa na posición actual (Kiryl Kaveryn, Viktor Govako)
- Conservar cores dos marcadores ao exportar/importar GPX (cyber-toad)
- Traducións actualizadas (colaboradores Weblate)

#### Estilos do mapa (Viktor Govako)

- Amosar tendas de iluminación
- Amosar liñas eléctricas dende o zoom 18
- Amosar nomes de referencia de centrais e subestacións
- Amosar cámpings e áreas para caravanas en modo navegación
- Corrixir cor de estradas secundarias en modo navegación
- Debuxar límites de parques nacionais
- Debuxar sitios arqueolóxicos dende o zoom 12 no estilo Outdoor

#### iOS

- NOVO: amosar contido da etiqueta OSM `description` (busca `?description`) (Kiryl Kaveryn, Viktor Govako)
- NOVO: pantalla de planificación de rutas redeseñada (Kiryl Kaveryn)

#### Android

- Novas iconas de rotondas en Android Auto (Andrei Shkrob)
- Amosar categoría do marcador seleccionado (Alexander Borsuk)
- Corrixido atraso ao amosar distancia a un marcador (Alexander Borsuk)
- Tema escuro reestruturado (Andrei Shkrob)
- Corrixida actualización de posición en navegación en ROMs personalizadas (ex. Lineage + MicroG) (Viktor Govako)
- Icona lápis azul (editar) para marcadores (Alexander Borsuk)
- Reducida altura vertical da previsualización de información do lugar (Alexander Borsuk)
- Eliminado ángulo de acimut cara ao norte da previsualización (toca frecha azul coa distancia) (Alexander Borsuk)

Obtén a última versión: [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid].

Únete á beta: [iOS][testflight] / [Android][firebase].

{{ references() }}
