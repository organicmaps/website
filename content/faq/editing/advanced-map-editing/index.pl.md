---
title: Jak mogę przeprowadzić bardziej zaawansowaną edycję mapy?
slug: jak-mogę-przeprowadzić-bardziej-zaawansowaną-edycję-mapy
description: Samouczek edycji OpenStreetMap za pomocą bardziej zaawansowanych narzędzi,
  takich jak ID, Go Map i Vespucci
updated: '2024-06-20'
taxonomies:
  faq: ["Edycja mapy"]
extra:
  order: 40
aliases:
  - /pl/faq/editing/advanced-map-editing/
---

Organic Maps zawiera prosty i łatwy w obsłudze edytor, za pomocą którego możesz edytować mapę. Edytor jest jednak ograniczony i pozwala jedynie na dodawanie prostych obiektów punktowych, co oznacza brak obrysów budynków, dróg, jezior, miast itp. Jeśli chcesz zmienić coś, czego nie można edytować za pomocą wbudowanego edytora, to jest to właściwa strona FAQ do przeczytania.

Ponieważ wszystkie dane map używane w Mapach organicznych pochodzą z [OpenStreetMap.org (OSM)](https://www.openstreetmap.org), możesz tam bezpośrednio aktualizować mapę. Twoje modyfikacje zostaną następnie uwzględnione w Mapach organicznych przy następnej aktualizacji map.

## Redaktorzy OpenStreetMap

Istnieje kilka opcji edycji OSM. Jeśli masz pod ręką laptopa lub komputer stacjonarny, lepiej skorzystać z [ID Editor](https://www.openstreetmap.org/edit), który działa w Twojej przeglądarce. Edytor ID jest łatwy dla początkujących, a większy ekran, mysz i klawiatura ułatwiają edycję map.

Do zaawansowanej edycji map na urządzeniu mobilnym użyj [Go Map](https://apps.apple.com/us/app/go-map/id592990211) na iOS lub [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) na Androida. Go Map jest łatwy dla początkujących, podczas gdy Vespucci jest przeznaczony dla bardziej zaawansowanych użytkowników. LearnOSM udostępnia samouczki dotyczące [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) i [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/).

Jeśli chcesz łatwiej edytować i zapewnić więcej zabawy, możesz też wypróbować [aplikację Every Door](https://every-door.app/) na iOS i Androida oraz [aplikację StreetComplete](https://streetcomplete.app/) na Androida.

#### Edytor identyfikatorów

Aby edytować OpenStreetMap z identyfikatorem, wykonaj następujące kroki:

1. Utwórz nowe konto lub zaloguj się na [OpenStreetMap.org](https://www.openstreetmap.org)
2. Przejdź do lokalizacji, którą chcesz edytować na OpenStreetMap.org i kliknij *Edytuj* u góry
3. *Rozpocznij Przewodnik* i postępuj zgodnie z krótkim samouczkiem objaśniającym Edytor ID
4. Edytuj mapę
5. Prześlij swoje zmiany

To wszystko, jesteś teraz częścią społeczności OSM.

## Co się stanie z moimi zmianami?

Po naciśnięciu przycisku *Prześlij* zmiany zostaną natychmiast dodane do publicznej bazy danych OSM. Zachowaj więc ostrożność podczas edycji. W Mapach organicznych Twoje zmiany będą widoczne po kolejnej comiesięcznej aktualizacji map.

Twój e-mail nie zostanie opublikowany, ale inne osoby będą mogły zobaczyć Twoją nazwę użytkownika OSM. Ponieważ OSM oferuje możliwość omówienia zmian, możesz otrzymać pytania dotyczące swoich zmian od innych autorów OSM. Zostaniesz o tym poinformowany na adres e-mail, który podałeś podczas rejestracji konta OSM. Ponieważ OSM jest projektem społecznościowym, który opiera się na współpracy, zawsze powinieneś odpowiadać na takie pytania.

## Społeczność i Wiki

OpenStreetMap jest społecznością. Jeśli potrzebujesz pomocy lub masz jakieś pytania, możesz je zadać na [Forum OSM](https://community.openstreetmap.org/c/help-and-support) lub zajrzeć do dokumentacji [OSM Wiki](https://wiki.openstreetmap.org/).

## Tagi — jak działa model danych OSM

Baza danych OpenStreetMap zawiera obiekty takie jak węzły, drogi, obszary i relacje, które abstrakcyjnie odnoszą się do obiektów ze świata rzeczywistego. Obiekty te posiadają atrybuty, tzw. znaczniki umożliwiające ich dalszy opis. Tag to kombinacja klucz-wartość.

Ponieważ brzmi to bardziej skomplikowanie, niż jest w rzeczywistości, podamy przykład:
Restauracja to m.in. mapowany jako Notatka lub Obszar ze znacznikiem `amenity=restaurant`. Dalsze znaczniki, takie jak `cuisine=*` lub `opening_hours=*` mogą być następnie użyte w celu uzyskania dalszych szczegółów.

> Pamiętaj, że edytor identyfikatorów ukrywa przed użytkownikami wewnętrzną strukturę danych, aby był bardziej przyjazny dla początkujących. Jednak do przeczytania dokumentacji Wiki pomocny jest krótki przegląd struktury danych.
W Edytorze ID możesz zobaczyć Tagi, które ID ukrywa przed Tobą, rozwijając sekcję *Tagi* w panelu bocznym *Funkcja edycji*.

## Notatki OSM {#osm-note}

Jeśli nie masz czasu lub problem jest zbyt skomplikowany, aby samodzielnie edytować dane OSM, najlepszym rozwiązaniem będą OSM Notes ([Wiki](https://wiki.openstreetmap.org/wiki/Notes)). Możesz umieścić taką notatkę w miejscu wystąpienia błędu mapy i szczegółowo opisać problem. Inni wolontariusze OSM mogą następnie pomóc i rozwiązać problem. Będziesz otrzymywać powiadomienia e-mailem za pośrednictwem swojego konta OSM w przypadku dalszych pytań lub rozwiązania notatki OSM.

1. Utwórz nowe konto lub zaloguj się na [OpenStreetMap.org](https://www.openstreetmap.org)
   > Możesz także otwierać anonimowe Notatki, ale nie jest to zalecane, ponieważ nie otrzymasz powiadomienia, gdy problem zostanie rozwiązany lub pojawią się dalsze pytania.
2. Powiększ lokalizację na mapie na [OpenStreetMap.org](https://www.openstreetmap.org) i naciśnij *Dodaj notatkę do mapy* (druga ikona od dołu w prawym menu). Następnie przeciągnij niebieski znacznik mapy do dokładnej lokalizacji.
   > Staraj się być tak precyzyjny, jak tylko potrafisz.
3. Podaj szczegółowy opis problemu z mapą i naciśnij *Dodaj notatkę*
   > Dla sklepów m.in. podaj nazwę i wspomnij, co jest tam sprzedawane lub jakie usługi są oferowane.
