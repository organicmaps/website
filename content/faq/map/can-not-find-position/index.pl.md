---
title: "Aplikacja nie może znaleźć mojej pozycji na mapie lub pokazuje nieprawidłową lokalizację"
slug: aplikacja-nie-może-określić-mojej-lokalizacji
description: "Przewodnik rozwiązywania problemów z lokalizacją i aktualną pozycją GPS na mapie dla urządzeń iOS i Android"
updated: "2026-01-04"
taxonomies:
  faq: ["Mapa"]
extra:
  order: 10
aliases:
  - /pl/faq/map/can-not-find-position/
---

Upewnij się, że Twoje urządzenie ma GPS i ustawienia lokalizacji są włączone.

**Android**

Na twoim urządzeniu otwórz Ustawienia → Lokalizacja. Lepiej jest włączyć tryb wysokiej dokładności.

Jeśli masz trudności z określeniem swojej lokalizacji za pomocą GPS, włącz (wyłącz, jeśli włączone) "Usługi Google Play" w ustawieniach aplikacji.

Uwaga: możesz je zobaczyć tylko wtedy, gdy masz zainstalowane (i włączone) usługi Google Play na twoim urządzeniu z Androidem. Usługi Google Play są używane do dokładniejszego określenia lokalizacji, jeśli masz problemy z dokładnością lokalizacji po wyłączeniu opcji, włącz ją.

**iOS**

Jeśli jesteś użytkownikiem iPhone'a lub iPada, sprawdź ustawienia iOS → Prywatność → Usługi lokalizacji. Udostępnianie danych geolokalizacyjnych powinno być włączone dla Organic Maps.

**Uwagi:**

* Aby uniknąć niechcianych opłat podczas roamingu, możesz wyłączyć wszystkie dane mobilne, aktywować tryb samolotowy lub wyłączyć dane mobilne dla Organic Maps w ustawieniach urządzenia. Urządzenia z Androidem i iOS mogą korzystać z GPS w trybie lotu.

* Niektóre urządzenia mobilne nie mają wbudowanych odbiorników GPS, takich jak iPod Touch, iPad tylko z Wi-Fi, Amazon Kindle Fire / Kindle Fire HD 7 i niektóre tablety z Androidem. Na tych urządzeniach nasza aplikacja będzie pokazywać przybliżoną lokalizację, o ile jesteś podłączony do Internetu.

* Na koniec pamiętaj, że określanie lokalizacji z GPS (z WiFi i danymi mobilnymi wyłączonymi) może zająć trochę czasu. Im dłużej GPS nie jest używany, tym więcej czasu zajmuje. Szybkość określania lokalizacji zależy od urządzenia, a nie od aplikacji. Pogoda wpływa na funkcjonowanie GPS - najlepiej działa na zewnątrz, gdy niebo jest czyste. Mogą pojawić się problemy podczas próby zlokalizowania się w domu, na wąskiej ulicy lub podczas prowadzenia samochodu.


**Na mapie pokazana jest nieprawidłowa lokalizacja**

1. Jeśli wokół strzałki lokalizacji na mapie znajduje się duży półprzezroczysty okrąg, oznacza to, że Twoja pozycja jest określana z niską dokładnością, przy użyciu połączenia WiFi lub komórkowego. Upewnij się, że w ustawieniach systemowych włączyłeś "Dokładną" lokalizację dla Organic Maps i spróbuj wyjść na zewnątrz, z dala od wysokich budynków i drzew, aby poprawić odbiór sygnału satelitarnego GPS.

2. Jeśli Twoja pozycja jest określana nieprawidłowo (na przykład jesteś w jednym mieście, ale aplikacja pokazuje inne miasto), najprawdopodobniej znajdujesz się w obszarze dotkniętym fałszywym sygnałem GPS (GPS spoofing) z powodu środków walki elektronicznej (EW). W takich przypadkach jedynym rozwiązaniem jest przeniesienie się w inne miejsce.