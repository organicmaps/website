---
title: "2026년 9월 업데이트: 경유 순서 최적화, 대체 경로 개선, 개별 트랙 숨기기, 간헐적으로 물이 차는 영역"
date: 2026-09-29
slug: "route-optimization-improved-alternative-routes-hide-individual-tracks-visibility-intermittent-water-areas-in-september-2026-update"
taxonomies:
  news: ["업데이트"]
extra:
  preview_image: 00-intermittent-water.png
---

여행을 떠날 준비가 되셨나요? 9월 업데이트에서는 대체 경로가 개선되었고 경유 순서를 최적화하는 설정이 추가되었습니다. 간헐적으로 물이 차는 영역이 더 뚜렷하게 표시되며 눈 모양 아이콘으로 트랙을 하나씩 숨길 수 있습니다. 아래에서 다른 수정 사항과 개선 사항도 확인하세요.

<https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid]에서 Organic Maps를 설치하거나 업데이트하세요.

이전 업데이트를 놓쳤다면 [6월](@/news/2026-06-29/610/index.ko.md), [7월](@/news/2026-07-23/620/index.ko.md), [8월](@/news/2026-08-31/630/index.ko.md)에 추가된 기능을 확인하세요. 업데이트를 함께 만든 기여자와 사용자 여러분께 감사드립니다!

## Organic Maps를 돕는 방법

- [후원](@/donate/index.ko.md)으로 개발과 지도 서버 운영비를 지원해 주세요.
- [의견을 보내거나 개발에 기여해 주세요](@/contribute/index.ko.md).
- [iOS][testflight], [Android][firebase], [데스크톱][flathub]의 베타 테스트에 참여해 새 기능을 먼저 사용하고 문제를 알려 주세요.
- Organic Maps를 주변에 알려 대형 기술 기업의 지도 서비스를 대신할 더 나은 지도를 함께 만들어 주세요!

## 업데이트 내역

### 지도

- 2026년 9월 28일 기준 OpenStreetMap 데이터
- 2026년 9월 21일 기준 위키백과 데이터
- 화면에 보이는 지도 영역이 180도 자오선(경도 ±180°)을 지날 때의 검색 문제 수정 _(Viktor Govako)_
- 간헐적으로 물이 차는 영역에 모래와 비슷한 점무늬 적용 _(Alexander Borsuk)_
- 지도를 더 축소해도 저수지가 보이도록 개선 _(Alexander Borsuk)_
- 물길 터널을 지도에서 숨김 _(Alexander Borsuk)_
- 쑤저우 지하철의 역과 출입구 아이콘 수정 _(Alexander Borsuk)_
- 지하철 지도 레이어에서 드물게 이름의 표시 위치가 어긋나던 문제 수정 _(Viktor Govako)_

### 경로 탐색과 길 안내

- 대체 경로와 도착 예정 시각 계산 개선 _(Alexander Borsuk, Viktor Govako)_
- 길 안내 중 경로를 다시 계산해도 선택한 대체 경로 유지 _(Alexander Borsuk)_
- 앱을 다시 시작한 후 경유 순서 복원 _(Kiryl Kaveryn)_

### 기타 개선 사항

- 영업시간에서 12:00은 ‘정오’, 00:00이나 24:00은 ‘자정’으로 표시 _(Alexander Borsuk)_
- 트랙 기록 오류 수정 및 개선 _(Alexander Borsuk)_
- KMB 파일 가져오기 오류 수정 _(Alexander Borsuk)_
- 프랑스어 및 아스투리아스어 번역 수정 _(Alexander Borsuk)_
- 영어의 오타 수정 _(Carl Morris)_

### iOS

- 트랙을 개별적으로 숨기는 눈 모양 아이콘 추가 _(Kiryl Kaveryn)_
- 계획한 경로에서 경유지를 추가하거나 교체하는 버튼 추가 _(Kiryl Kaveryn)_
- 경유 순서를 최적화하는 설정 추가 _(Kiryl Kaveryn)_
- 지원 차량의 헤드업 디스플레이(HUD)와 CarPlay 대시보드에 진행 방향 안내 추가 _(Kiryl Kaveryn)_
- CarPlay 버튼과 검색 오류 수정 _(Alexander Borsuk)_
- 여러 오류 수정 및 사용자 인터페이스 개선 _(Kiryl Kaveryn, Alexander Borsuk)_
- 설치된 길 안내 음성을 선택하고 미리 듣는 기능 추가 _(Kiryl Kaveryn, Alexander Borsuk)_
- Spotlight에서 카테고리 검색 복원 _(Kiryl Kaveryn)_

### Android

- 경유 순서를 최적화하는 설정 추가 _(Mikhail Listratsenka)_
- 계획한 경로에서 경유지를 추가하거나 교체하는 버튼 추가 _(Mikhail Listratsenka)_
- 알림에서 트랙 기록을 중지하고 저장하는 기능 추가 _(Alexander Borsuk)_
- ‘경유지 추가’를 누르면 기존 경유지 다음이자 목적지 앞에 새 경유지가 추가됨 _(Mikhail Listratsenka)_
- OpenStreetMap 편집기에서 변경 사항 업로드 개선 _(Owm)_
- 사용자 인터페이스 디자인 개선 _(Mikhail Listratsenka)_
- 길 안내 중에도 북마크 편집기와 다른 대화 상자를 열어 둠 _(Mikhail Listratsenka)_
- 고도 변화가 없는 트랙이나 오른쪽에서 왼쪽으로 읽는 화면에서 고도 그래프 표시 오류 수정 _(Mikhail Listratsenka)_
- 시스템 바에 지도 버튼이 가려지던 문제 수정 _(Mikhail Listratsenka)_
- Android Auto 지원 개선 및 오류 수정 _(Andrei Shkrob)_
- 지도 표시 중 발생하던 비정상 종료 수정 _(Viktor Govako)_

### 데스크톱

- 데스크톱 실행 파일과 macOS 앱 번들 이름을 `OrganicMaps`로 변경 _(Alexander Borsuk)_
- Windows 앱 문제 수정 _(Osyotr, Alexander Borsuk)_
- 명령줄 인수 `--lang`이 앱 언어 설정보다 우선 적용됨 _(Alexander Borsuk)_

기쁨과 열정을 담아,

Organic Maps 팀 드림

{{ <references lang /> }}
