---
title: "9월 15일 업데이트: 새 경로 계획 화면과 OSM 장소 설명"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["업데이트"]
---

9월의 두 번째 업데이트에서는 iOS에서 경로 계획 화면을 새로 디자인하고 OpenStreetMap `description` 태그의 내용을 볼 수 있게 했습니다. 설명 태그가 있는 장소를 찾으려면 위키백과 문서가 있는 장소를 검색할 때 `?wiki`를 입력하는 것처럼 검색란에 `?description`을 입력하세요.

iOS와 Android 모두에서 여러 오류를 수정하고 기능을 개선했습니다. 자세한 내용은 아래에서 확인하세요.

놓쳤을 수 있는 다른 최근 기능도 확인해 보세요.
- 버스 정류장을 선택하면 대중교통 노선 번호 표시
- 등산 및 자전거 경로(왼쪽 위 레이어 버튼에서 켜거나 끌 수 있음)
- 앱 설정에서 켜면 지도에 북마크 이름 표시
- ✎ 연필 아이콘을 눌러 북마크를 빠르게 편집

기여자 여러분과 보내 주시는 [후원](@/donate/index.ko.md), [지원](@/contribute/index.ko.md) 덕분에 Organic Maps를 만들 수 있습니다.

### 자세한 업데이트 내역

- 9월 13일 기준 최신 OpenStreetMap 데이터
- 세계 지도에서 작은 섬 제거 (Viktor Govako)
- 주소 상세 정보에 우편번호 표시 (Viktor Govako)
- 지도의 중앙이 현재 위치에 맞춰지지 않던 문제 수정 (Kiryl Kaveryn, Viktor Govako)
- GPX를 내보내거나 가져올 때 북마크 색상 유지 (cyber-toad)
- 번역 업데이트 (Weblate 기여자)

#### 지도 스타일 (Viktor Govako)

- 조명 매장 표시
- 확대 수준 18부터 송전선 표시
- 발전소와 변전소의 참조 이름 표시
- 길 안내 중 캠핑장과 캠핑카 사이트 표시
- 길 안내 중 보조 간선도로 색상 수정
- 국립공원 경계 표시
- 야외 활동 스타일에서 확대 수준 12부터 고고학 유적 표시

#### iOS

- 신규: OSM `description` 태그의 내용을 표시(검색란에 `?description`을 입력해 확인) (Kiryl Kaveryn, Viktor Govako)
- 신규: 경로 계획 화면을 새로 디자인 (Kiryl Kaveryn)

#### Android

- Android Auto에 새 회전교차로 아이콘 적용 (Andrei Shkrob)
- 북마크한 장소를 선택하면 해당 장소의 카테고리 표시 (Alexander Borsuk)
- 북마크한 장소까지의 거리가 늦게 표시되던 문제 수정 (Alexander Borsuk)
- 다크 테마 구현 개선 (Andrei Shkrob)
- microG를 사용하는 LineageOS 등의 커스텀 ROM에서 길 안내 중 위치 갱신 오류 수정 (Viktor Govako)
- 북마크 편집용 연필 아이콘을 파란색으로 변경 (Alexander Borsuk)
- 장소 정보 미리 보기의 세로 공간을 줄임 (Alexander Borsuk)
- 장소 정보 미리 보기에서 북쪽 기준 방위각 제거. 거리가 표시된 파란색 화살표를 누르면 방위각을 확인할 수 있음 (Alexander Borsuk)

[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid]에서 최신 Organic Maps를 다운로드하세요.

베타 테스트에서 새 기능을 먼저 사용해 보세요. [iOS][testflight] / [Android][firebase]

{{ <references lang /> }}
