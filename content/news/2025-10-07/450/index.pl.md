---
title: "Wydanie październikowe: Limity prędkości w Android Auto, import GeoJSON, statystyki nagrywania ścieżek, wyświetlanie tagów opisów OSM, zapisywanie zakładek na wybranej ścieżce w iOS i więcej"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["Releases"]
---

Ta październikowa aktualizacja Organic Maps dodaje wyświetlanie limitów prędkości w Android Auto, import GeoJSON, statystyki nagrywania ścieżek, pokazuje tagi opisów OSM (wpisz `?description` w polu wyszukiwania, aby je zobaczyć) i zapisuje zakładkę na ścieżce w iOS. Dostępnych jest również wiele ulepszeń interfejsu użytkownika, edycji OpenStreetMap i różne poprawki błędów na wszystkich platformach, w tym naprawa awarii podczas uruchamiania na niektórych urządzeniach Android.

Organic Maps istnieje dzięki ❤️ naszym współtwórcom, [Twoim darowiznom](@/donate/index.pl.md) i [Twojemu wsparciu](@/contribute/index.pl.md).

### Szczegółowe informacje o wydaniu (w tym zmiany z poprzedniej mniejszej aktualizacji)

- NOWOŚĆ! Import GeoJSON (Sergiy Kozyr)
- Dane OpenStreetMap z 4 października
- Dane Wikipedii z 1 października
- Wsparcie dla Seattle light rail dla transportu publicznego (tjasz)
- Nie dezaktywuj wyboru mapy podczas zapisywania edytowanego miejsca OSM (Kiryl Kaveryn)
- Zaktualizowane tłumaczenia (współtwórcy Weblate)

#### Style map

- Wyświetlanie wypożyczalni rowerów oznaczonych jako amenity=bicycle + rental=shop (David Martinez)
- Wyświetlanie historycznych stanowisk archeologicznych od powiększenia 12 i innych miejsc historycznych od powiększenia 15 w stylu Outdoor (Viktor Govako)
- Nowe ikony dla masztów, komunikacji i wież energetycznych w stylu Outdoor (David Martinez)
- Zwiększenie rozmiaru ikony szczytu w stylu Outdoor (David Martinez)
- Dodanie brakujących wariantów ikon POI (David Martinez)
- Dodano więcej typów barier (Viktor Govako)

#### iOS

- NOWOŚĆ: Zapisywanie zakładki w wybranym punkcie ścieżki (Kiryl Kaveryn)
- NOWOŚĆ: Usuwanie nagranej ścieżki bez wcześniejszego zapisywania (Kiryl Kaveryn)
- Wyświetlanie wieloliniowych tytułów list zakładek na stronie Miejsce (David Martinez)
- Aktualizacja stylu przycisków logowania OSM (Kiryl Kaveryn)
- Naprawa problemu z aktualizacją informacji nawigacyjnych (Kiryl Kaveryn)
- Naprawa problemów z planowaniem nowej trasy (Kiryl Kaveryn)
- Naprawa widoczności dodawania/edycji miejsca OSM dla map starszych niż 3 miesiące (Kiryl Kaveryn)
- Naprawa układu kontrolki segmentu opcji transportu dla iOS 26 (Kiryl Kaveryn)
- Uproszczenie animacji wyboru zakładek (Kiryl Kaveryn)
- Naprawa problemu z wyborem wyniku wyszukiwania (Kiryl Kaveryn)
- Naprawiony styl, przesuwanie i animacje dla strony Informacje o miejscu (Kiryl Kaveryn)

#### Android Auto (tylko Google Play)

- NOWOŚĆ: Wyświetlanie limitu prędkości w Android Auto (Andrei Shkrob)
- Naprawa przełączania wyświetlacza w trybie nawigacji Android Auto (Andrei Shkrob)
- Naprawa przesunięcia strzałki trasy w Android Auto (Andrei Shkrob)
- Naprawa problemu podczas podłączania/odłączania urządzenia do samochodu (Andrei Shkrob)
- Dodanie usługi lokalizacji Android Auto (Andrei Shkrob)
- Ulepszenie symulatora trasy Android Auto (Viktor Govako)

#### Android

- NOWOŚĆ: Wyświetlanie statystyk nagrywania ścieżki w czasie rzeczywistym (Kavi Khalique)
- NOWOŚĆ: Wyświetlanie zawartości tagu `description` OSM (Alexander Borsuk)
- Naprawa obsługi zmiany motywu (Andrei Shkrob)
- Naprawiono kilka awarii, w tym tę podczas uruchamiania (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- Ciche powiadomienia o postępie pobierania (Viktor Govako)
- Zmniejszenie wypełnienia ikony ołówka (Alexander Borsuk)

#### Desktop

- Naprawa zawieszania curl w Linuksie (Alexander Borsuk)
- Naprawa zawieszania na macOS podczas logowania do OSM (Alexander Borsuk)
- Akcja wyboru funkcji z menu kontekstowego (Viktor Govako)
- Opcja anulowania pobierania (Viktor Govako)
- Wyświetlanie typu geometrii w menu kontekstowym (Viktor Govako)

### Niedawno wydane funkcje, które mogłeś przeoczyć

- Numery linii transportu publicznego przy wyborze przystanku autobusowego
- Szlaki piesze i rowerowe (włącz je przez przycisk Warstwy w lewym górnym rogu)
- Zobacz nazwy zakładek na mapie, włączając to w Ustawieniach aplikacji
- Ikona ołówka ✎ oferuje szybki sposób edycji zakładek

### Zainstaluj Organic Maps

Pobierz najnowszą wersję Organic Maps z [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] i [F-Droid][fdroid].

Dołącz do testowania beta dla wczesnych funkcji: [iOS][testflight] / [Android][firebase].

{{ references() }}
