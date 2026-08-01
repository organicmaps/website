---
title: "Poprawki błędów i ulepszenia dotyczące transportu publicznego, wyznaczania tras, wyszukiwania oraz zakładek w aktualizacji z lipca 2026 r."
date: 2026-07-23
slug: "poprawki-bledow-ulepszenia-transport-publiczny-trasy-wyszukiwanie-zakladki-lipiec-2026"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

Jak być może już Państwo zauważyli, ukazała się lipcowa aktualizacja Organic Maps. Można ją pobrać ze strony <https://get.omaps.org> lub z serwisów [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] oraz [F-Droid][fdroid].

Dzięki Państwa [darowiznom](@/donate/index.pl.md) oraz [opiniom](@/contribute/index.pl.md) w lipcu skupiliśmy się na usuwaniu błędów i wprowadzaniu ulepszeń. Jeśli przegapili Państwo tę informację, dostępne są również następujące funkcje z [poprzedniej, czerwcowej wersji](@/news/2026-06-29/610/index.pl.md):
- Trasy transportu publicznego (aktualne rozkłady jazdy są w trakcie opracowywania)
- Zdjęcia satelitarne
- Alternatywne trasy do jazdy samochodem, wędrówek pieszych i jazdy na rowerze
- Nowy interfejs wyszukiwania i planowania trasy na Androidzie
- Obsługa dużych czcionek ułatwień dostępu na iOS

## Szczegółowy dziennik zmian

### Mapa i miejsca
- Dane OpenStreetMap zaktualizowane na dzień 14 lipca
- Notatki zgłoszone do [OpenStreetMap](https://www.openstreetmap.org) są teraz umieszczane dokładnie w wybranym przez Państwa miejscu, a nie na środku całej ulicy lub obszaru _(Alexander Borsuk)_
- Ulepszony wybór miejsc po dotknięciu mapy w regionach, które przecinają antypołudnik 180° _(Viktor Govako)_
- Po usunięciu śladu na profilach wysokościowych nie wyświetlają się już nieaktualne lub puste wykresy _(Kiryl Kaveryn)_

### Transport publiczny
- Nazwy przystanków, przesiadek i stacji mają teraz białą obwódkę, dzięki czemu są czytelne zarówno w jasnym, jak i ciemnym motywie _(Viktor Govako)_
- Po zamknięciu podglądu trasy transportu publicznego warstwa metra pojawia się ponownie prawidłowo _(Mikhail Listratsenka)_

### Trasy i nawigacja
- Ostrzeżenia dotyczące tras (opłaty drogowe, promy, drogi nieutwardzone, schody itp.) są teraz wyświetlane dla wszystkich tras alternatywnych _(Viktor Govako)_
- Naprawiono rzadki błąd powodujący zawieszanie się programu podczas wyznaczania trasy _(Viktor Govako)_
- Ulepszona obsługa ślepych uliczek oraz punktów początkowych i końcowych na drogach z ograniczeniami _(Viktor Govako)_
- Poprawiono błędne i brakujące wskazówki dotyczące skrętów _(Alexander Borsuk)_

### iOS
- Nowe ustawienie „Zapisz historię wyszukiwania”, które pozwala wyłączyć historię i ukryć ją, jeśli nie chcą jej Państwo zachowywać _(Kiryl Kaveryn)_
- Nowy przycisk „Edytuj” ułatwiający usuwanie zakładek _(Kiryl Kaveryn)_
- Zakładki są teraz zapisywane automatycznie po opuszczeniu ekranu _(Kiryl Kaveryn)_
- Paleta kolorów zawiera teraz gotowe kolory i umożliwia wybór dowolnego koloru niestandardowego _(Kiryl Kaveryn)_
- Ulepszono pusty stan wykresu wysokości dla zarejestrowanego śladu _(Kiryl Kaveryn)_
- Ulepszono wyświetlanie postępu trasy na przycisku „Start” _(Kiryl Kaveryn)_
- Zmiana kolejności przystanków na trasie nie powoduje już przeskakiwania pozycji na liście _(Kiryl Kaveryn)_
- Inne drobne ulepszenia interfejsu _(Kiryl Kaveryn)_

### Android
- Godziny otwarcia uwzględniają teraz podzielone zmiany (takie jak przerwa obiadowa), zaczynają się od dzisiejszego dnia i są wyświetlane dla całego tygodnia bez osobnego obszaru przewijania _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- Przejrzystszy pasek wyszukiwania z połączonym przyciskiem „Wyczyść” i „Głos”, ikoną „Wyczyść”, która już się nie przesuwa, oraz poprawkami układu w trybie poziomym i po obróceniu telefonu _(Mikhail Listratsenka)_
- Przerobiony edytor zakładek i śladów _(Mikhail Listratsenka)_
- Poprawki i ulepszenia dotyczące planowania tras _(Mikhail Listratsenka)_
- Próbnik kolorów zamyka się teraz automatycznie, a usterka powodująca awarię programu w systemie Android 5 została naprawiona _(Mikhail Listratsenka)_
- Naprawiono awarie _(Alexander Borsuk, Mikhail Listratsenka)_

### Desktop
- Lista map dostępnych do pobrania jest teraz posortowana alfabetycznie _(goncalo109560)_

### Tłumaczenia
- Poprawione chińskie sformułowania _(Chenxi Zhao)_
- Zaktualizowane tłumaczenia na język ukraiński _(Nnifria)_
- Poprawiono włoskie tłumaczenia nazw regionów na mapie _(Vittorio Bertola)_

## Weźcie Państwo udział w beta-testach, aby wypróbować wczesne funkcje i zgłaszać problemy:

Wskazówka: wersja beta zawiera nowe cieniowanie terenu, ulepszone dane dotyczące wysokości z obsługą stóp i metrów oraz inne ciekawe funkcje!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

Miłego lata!
Zespół Organic Maps

{{ references() }}
