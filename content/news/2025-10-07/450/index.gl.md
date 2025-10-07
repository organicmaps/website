---
title: "Lanzamento de outubro: Límites de velocidade en Android Auto, importación GeoJSON, estatísticas de gravación de rutas, visualización da etiqueta de descrición OSM, gardar marcadores na ruta seleccionada en iOS e máis"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
---

Esta actualización de outubro de Organic Maps engade a visualización do límite de velocidade en Android Auto, a importación de GeoJSON, as estatísticas de gravación de rutas, mostra as etiquetas de descrición de OSM (escriba `?description` na caixa de busca para velas) e garda un marcador nunha ruta en iOS. Tamén hai moitas melloras na interface de usuario, a edición de OpenStreetMap e varias correccións de erros en todas as plataformas, incluída a corrección do bloqueo ao inicio nalgúns dispositivos Android.

Organic Maps é posible grazas ❤️ aos nosos colaboradores, [as súas doazóns](@/donate/index.gl.md) e [o seu apoio](@/contribute/index.gl.md).

### Notas de lanzamento detalladas (incluíndo os cambios da actualización menor anterior)

- NOVO! Importación de GeoJSON (Sergiy Kozyr)
- Datos de OpenStreetMap do 4 de outubro
- Datos de Wikipedia do 1 de outubro
- Soporte do tren lixeiro de Seattle para o transporte público (tjasz)
- Non desactivar a selección do mapa ao gardar un lugar OSM editado (Kiryl Kaveryn)
- Traducións actualizadas (colaboradores de Weblate)

#### Estilos de mapa

- Mostrar tendas de alugueiro de bicicletas etiquetadas como amenity=bicycle + rental=shop (David Martinez)
- Mostrar sitios arqueolóxicos históricos desde o zoom 12 e outros sitios históricos desde o zoom 15 no estilo Exterior (Viktor Govako)
- Novas iconas para mastros, comunicación e torres eléctricas no estilo Exterior (David Martinez)
- Aumentar o tamaño da icona de pico no estilo Exterior (David Martinez)
- Engadir variantes de iconas de PDI que faltaban (David Martinez)
- Engadidos máis tipos de barreiras (Viktor Govako)

#### iOS

- NOVO: Gardar marcador no punto de ruta seleccionado (Kiryl Kaveryn)
- NOVO: Eliminar a ruta de gravación sen gardala primeiro (Kiryl Kaveryn)
- Mostrar títulos de lista de marcadores de varias liñas na Páxina do lugar (David Martinez)
- Actualizar o estilo dos botóns de inicio de sesión de OSM (Kiryl Kaveryn)
- Corrixir problema de actualización de información de navegación (Kiryl Kaveryn)
- Corrixir problemas de planificación de novas rutas (Kiryl Kaveryn)
- Corrixir a visibilidade de engadir/editar lugar de OSM para mapas con máis de 3 meses (Kiryl Kaveryn)
- Corrixir o deseño do control de segmento de opcións de transporte para iOS 26 (Kiryl Kaveryn)
- Simplificar as animacións de selección de marcadores (Kiryl Kaveryn)
- Corrixir problema de selección de resultados de busca (Kiryl Kaveryn)
- Estilo, deslizamento e animacións corrixidos para a Páxina de información do lugar (Kiryl Kaveryn)

#### Android Auto (só Google Play)

- NOVO: Visualización do límite de velocidade en Android Auto (Andrei Shkrob)
- Corrixir o cambio de pantalla no modo de navegación de Android Auto (Andrei Shkrob)
- Corrixir o desprazamento da frecha de ruta en Android Auto (Andrei Shkrob)
- Corrixir problema cando un dispositivo se conecta/desconecta dun coche (Andrei Shkrob)
- Engadir servizo de localización de Android Auto (Andrei Shkrob)
- Mellorar o simulador de rutas de Android Auto (Viktor Govako)

#### Android

- NOVO: Ver estatísticas de gravación de rutas en tempo real (Kavi Khalique)
- NOVO: Mostrar o contido da etiqueta `description` de OSM (Alexander Borsuk)
- Corrixir a xestión do cambio de tema (Andrei Shkrob)
- Corrixidos varios bloqueos, incluído o do inicio (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Notificacións silenciosas de progreso de descarga (Viktor Govako)
- Reducir o recheo da icona de lapis (Alexander Borsuk)

#### Escritorio

- Corrixir bloqueo de curl en Linux (Alexander Borsuk)
- Corrixir bloqueo en macOS ao iniciar sesión en OSM (Alexander Borsuk)
- Acción para seleccionar función desde o menú contextual (Viktor Govako)
- Opción para cancelar a descarga (Viktor Govako)
- Mostrar tipo de xeometría no menú contextual (Viktor Govako)

### Funcións lanzadas recentemente que podería ter perdido

- Números de ruta de transporte público ao seleccionar unha parada de autobús
- Rutas de sendeirismo e ciclismo (actíveas co botón Capas na esquina superior esquerda)
- Ver nomes de marcadores no mapa activándoo na Configuración da aplicación
- A icona de lapis ✎ ofrece unha forma rápida de editar marcadores

### Instalar Organic Maps

Obteña a última versión de Organic Maps desde a [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] e [F-Droid][fdroid].

Únase ás probas beta para funcións temperás: [iOS][testflight] / [Android][firebase].

{{ references() }}
