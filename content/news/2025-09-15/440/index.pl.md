---
title: "Wydanie 15 września: nowe planowanie trasy i opisy OSM"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["releases"]
---

To drugie wrześniowe wydanie wprowadza przeprojektowany ekran planowania trasy oraz wyświetlanie zawartości tagu OpenStreetMap `description` na iOS. Aby znaleźć miejsca z tym tagiem, wpisz w wyszukiwarce `?description` (podobnie do `?wiki` dla miejsc powiązanych z Wikipedią).

Zawiera także wiele poprawek i ulepszeń dla iOS i Androida (szczegóły poniżej).

I oczywiście przypomnienie o innych ostatnich funkcjach, które mogłeś przeoczyć:
- Numery linii transportu publicznego przy wyborze przystanku
- Szlaki piesze i rowerowe (włącz je przyciskiem Warstwy w lewym górnym rogu)
- Nazwy zakładek na mapie (włącz w Ustawieniach aplikacji)
- Ikona ołówka ✎ umożliwia szybkie edytowanie zakładek

Organic Maps istnieje dzięki współtwórcom, [Twoim darowiznom](@/donate/index.pl.md) i [Twojemu wsparciu](@/contribute/index.md).

### Szczegółowe informacje o wydaniu

- Nowe dane OpenStreetMap z 13 września
- Usunięto bardzo małe wyspy z mapy świata (Viktor Govako)
- Wyświetlanie kodu pocztowego (ZIP) w szczegółach adresu (Viktor Govako)
- Naprawiono nieprawidłowe centrowanie mapy na bieżącej pozycji (Kiryl Kaveryn, Viktor Govako)
- Zachowanie kolorów zakładek przy eksporcie i imporcie GPX (cyber-toad)
- Zaktualizowane tłumaczenia (współtwórcy Weblate)

#### Style map (Viktor Govako)

- Wyświetlanie sklepów oświetleniowych
- Wyświetlanie linii energetycznych od powiększenia 18
- Wyświetlanie nazw referencyjnych elektrowni i stacji elektroenergetycznych
- Wyświetlanie kempingów i miejsc dla kamperów w trybie nawigacji
- Poprawa koloru dróg drugorzędnych w trybie nawigacji
- Rysowanie granic parków narodowych
- Rysowanie stanowisk archeologicznych od powiększenia 12 w stylu Outdoor

#### iOS

- NOWE: wyświetlanie zawartości tagu OSM `description` (aby przetestować, wpisz `?description` w wyszukiwarce) (Kiryl Kaveryn, Viktor Govako)
- NOWE: przeprojektowany ekran planowania trasy (Kiryl Kaveryn)

#### Android

- Nowe ikony rond w Android Auto (Andrei Shkrob)
- Wyświetlanie kategorii wybranej zakładki (Alexander Borsuk)
- Naprawiono opóźnienie przy wyświetlaniu odległości do zakładki (Alexander Borsuk)
- Przebudowany ciemny motyw (Andrei Shkrob)
- Naprawiono aktualizację pozycji w nawigacji na custom ROM-ach (np. Lineage + MicroG) (Viktor Govako)
- Niebieska ikona ołówka (edycja) dla zakładek (Alexander Borsuk)
- Zmniejszono pionową wysokość podglądu informacji o miejscu (Alexander Borsuk)
- Usunięto kąt azymutu do północy z podglądu informacji o miejscu (stuknij niebieską strzałkę z odległością, aby go zobaczyć) (Alexander Borsuk)

Pobierz najnowszą wersję Organic Maps z [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] i [F-Droid][fdroid].

P.S. Dołącz do testów beta, aby wcześniej poznawać nowe funkcje: [iOS][testflight] / [Android][firebase].

{{ references() }}
