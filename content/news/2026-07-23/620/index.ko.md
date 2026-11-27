---
title: "2026년 7월 업데이트: 대중교통, 경로 탐색, 검색, 북마크 개선 및 오류 수정"
date: 2026-07-23
slug: bugfixes-and-improvements-for-public-transport-routing-search-and-bookmarks-july-2026
taxonomies:
  news: ["업데이트"]
extra:
  preview_image: "Barriers on a route.jpg"
---

Organic Maps 7월 업데이트가 나왔습니다. <https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid]에서 다운로드하세요.

보내 주신 [후원금](@/donate/index.ko.md)과 [의견](@/contribute/index.ko.md) 덕분에 7월에는 오류 수정과 기능 개선에 집중했습니다. [지난 6월 업데이트](@/news/2026-06-29/610/index.ko.md)에서 선보인 다음 기능도 이용할 수 있습니다.
- 대중교통 경로(실시간 시간표는 개발 중)
- 위성 영상
- 자동차, 도보, 자전거 대체 경로
- Android의 새로운 검색 및 경로 계획 화면
- iOS의 접근성 설정에서 큰 글자 크기 지원

## 자세한 변경 내역

### 지도와 장소

- 7월 14일 기준 OpenStreetMap 데이터로 업데이트
- [OpenStreetMap](https://www.openstreetmap.org)에 메모를 보내면 도로나 영역 전체의 중앙 대신 선택한 지점에 정확히 표시 _(Alexander Borsuk)_
- 지도에서 180도 자오선을 지나는 지역을 눌렀을 때 장소 선택 개선 _(Viktor Govako)_
- 트랙을 삭제한 후 고도 프로필에 이전 그래프나 빈 그래프가 표시되던 문제 수정 _(Kiryl Kaveryn)_

### 대중교통

- 라이트 및 다크 테마에서 정류장, 환승 지점, 역 이름을 읽기 쉽도록 흰색 테두리 적용 _(Viktor Govako)_
- 대중교통 경로 미리 보기를 닫은 뒤 지하철 레이어가 다시 표시되도록 수정 _(Mikhail Listratsenka)_

### 경로 탐색과 길 안내

- 모든 대체 경로에 유료 도로, 페리, 비포장도로, 계단 등 경로 관련 주의 사항 표시 _(Viktor Govako)_
- 경로를 만드는 동안 드물게 앱이 멈추던 문제 수정 _(Viktor Govako)_
- 막다른길 및 통행이 제한된 도로 위의 출발지와 목적지 처리 개선 _(Viktor Govako)_
- 진행 방향 안내가 틀리거나 누락되던 문제 수정 _(Alexander Borsuk)_

### iOS

- 검색 기록 저장을 끄고 기록을 숨길 수 있는 ‘검색 기록 저장’ 설정 추가 _(Kiryl Kaveryn)_
- 북마크를 쉽게 삭제할 수 있는 편집 버튼 추가 _(Kiryl Kaveryn)_
- 화면을 나갈 때 북마크를 자동 저장 _(Kiryl Kaveryn)_
- 색상 팔레트에서 기본 제공 색상과 원하는 사용자 지정 색상을 선택할 수 있음 _(Kiryl Kaveryn)_
- 기록한 트랙에 고도 데이터가 없을 때 그래프의 표시 개선 _(Kiryl Kaveryn)_
- 시작 버튼에 표시되는 경로 진행 상태 개선 _(Kiryl Kaveryn)_
- 경유 순서를 바꿀 때 목록이 갑자기 움직이던 문제 수정 _(Kiryl Kaveryn)_
- 그 외 소규모 화면 개선 _(Kiryl Kaveryn)_

### Android

- 점심시간처럼 영업시간이 나뉘는 경우도 표시하며, 오늘부터 일주일의 영업시간을 별도의 스크롤 영역 없이 표시 _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- 지우기와 음성 입력 버튼을 합쳐 검색창을 정리하고 지우기 아이콘 위치가 움직이지 않도록 수정. 가로 모드와 화면 회전 시 배치 개선 _(Mikhail Listratsenka)_
- 북마크 및 트랙 편집기를 새로 구성 _(Mikhail Listratsenka)_
- 경로 계획 개선 및 오류 수정 _(Mikhail Listratsenka)_
- 색상 선택 화면을 자동으로 닫도록 변경하고 Android 5의 비정상 종료 수정 _(Mikhail Listratsenka)_
- 비정상 종료 수정 _(Alexander Borsuk, Mikhail Listratsenka)_

### 데스크톱

- 다운로드할 수 있는 지도 목록을 알파벳순으로 정렬 _(goncalo109560)_

### 번역

- 중국어 문구 개선 _(Chenxi Zhao)_
- 우크라이나어 번역 업데이트 _(Nnifria)_
- 지도 지역 이름의 이탈리아어 번역 수정 _(Vittorio Bertola)_

## 베타 테스트에서 새 기능을 써 보고 문제를 알려 주세요

베타 버전에는 새 지형 음영, 피트와 미터를 지원하는 개선된 고도 데이터 등 여러 기능이 들어 있습니다!

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

즐거운 여름 보내세요!
Organic Maps 팀

{{ <references lang /> }}
