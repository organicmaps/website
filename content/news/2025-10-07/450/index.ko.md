---
title: "10월 7일 업데이트: Android Auto 제한 속도, GeoJSON 가져오기, 트랙 기록 통계, OSM 설명, iOS 트랙에 북마크 저장"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["업데이트"]
---

Organic Maps의 10월 7일 업데이트에서는 Android Auto 제한 속도 표시, GeoJSON 가져오기, 트랙 기록 통계, OSM 설명 태그 표시(검색란에 `?description` 입력), iOS에서 트랙에 북마크 저장을 지원합니다. 사용자 화면과 OpenStreetMap 편집 기능을 개선했으며 일부 Android 기기에서 시작할 때 비정상 종료되던 문제를 비롯해 모든 플랫폼에서 여러 오류를 수정했습니다.

기여자 여러분과 보내 주시는 [후원](@/donate/index.ko.md), [지원](@/contribute/index.ko.md) 덕분에 Organic Maps를 만들 수 있습니다 ❤️.

### 자세한 업데이트 내역(이전 소규모 업데이트 포함)

- 신규: GeoJSON 가져오기 (Sergiy Kozyr)
- 10월 4일 기준 OpenStreetMap 데이터
- 10월 1일 기준 위키백과 데이터
- 대중교통에 시애틀 경전철 지원 (tjasz)
- 편집한 OSM 장소를 저장해도 지도에서 해당 장소의 선택 상태를 유지 (Kiryl Kaveryn)
- 번역 업데이트 (Weblate contributors)

#### 지도 스타일

- amenity=bicycle + rental=shop 태그가 있는 자전거 대여점 표시 (David Martinez)
- 야외 활동 스타일에서 고고학 유적은 확대 수준 12부터, 그 밖의 사적은 확대 수준 15부터 표시 (Viktor Govako)
- 야외 활동 스타일에 마스트, 통신탑, 송전탑의 새 아이콘 적용 (David Martinez)
- 야외 활동 스타일에서 봉우리 아이콘 확대 (David Martinez)
- 누락된 관심 지점 아이콘의 변형 추가 (David Martinez)
- 더 다양한 차단 시설 유형 추가 (Viktor Govako)

#### iOS

- 신규: 트랙에서 선택한 지점에 북마크 저장 (Kiryl Kaveryn)
- 신규: 기록 중인 트랙을 저장하지 않고 삭제 가능 (Kiryl Kaveryn)
- 장소 정보에 여러 줄로 된 북마크 목록 이름 표시 (David Martinez)
- OSM 로그인 버튼 스타일 업데이트 (Kiryl Kaveryn)
- 길 안내 정보 갱신 문제 수정 (Kiryl Kaveryn)
- 새 경로 계획 기능의 문제 수정 (Kiryl Kaveryn)
- 3개월보다 오래된 지도에서 OSM 장소 추가 및 편집 버튼 표시 문제 수정 (Kiryl Kaveryn)
- iOS 26에서 이동 수단 선택 버튼의 배치 수정 (Kiryl Kaveryn)
- 북마크 선택 애니메이션 간소화 (Kiryl Kaveryn)
- 검색 결과 선택 문제 수정 (Kiryl Kaveryn)
- 장소 정보의 스타일, 스와이프 동작, 애니메이션 수정 (Kiryl Kaveryn)

#### Android Auto(Google Play 버전 전용)

- 신규: Android Auto에서 제한 속도 표시 (Andrei Shkrob)
- Android Auto의 길 안내 모드에서 화면 전환 수정 (Andrei Shkrob)
- Android Auto 경로 안내 화살표의 위치 보정 (Andrei Shkrob)
- 기기를 차량에 연결하거나 연결을 해제할 때 발생하던 문제 수정 (Andrei Shkrob)
- Android Auto 위치 서비스 추가 (Andrei Shkrob)
- Android Auto 경로 시뮬레이터 개선 (Viktor Govako)

#### Android

- 신규: 트랙 기록 중 통계를 실시간으로 확인 (Kavi Khalique)
- 신규: OSM `description` 태그의 내용 표시 (Alexander Borsuk)
- 테마 변경 처리 수정 (Andrei Shkrob)
- 앱을 시작할 때를 비롯한 여러 비정상 종료 문제 수정 (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- 다운로드 진행 알림을 소리 없이 표시 (Viktor Govako)
- 연필 아이콘의 여백 축소 (Alexander Borsuk)

#### 데스크톱

- Linux에서 curl이 멈추던 문제 수정 (Alexander Borsuk)
- macOS에서 OSM 로그인 중 앱이 멈추던 문제 수정 (Alexander Borsuk)
- 상황에 맞는 메뉴에 지형지물 선택 동작 추가 (Viktor Govako)
- 다운로드 취소 옵션 추가 (Viktor Govako)
- 상황에 맞는 메뉴에 도형 유형 표시 (Viktor Govako)

### 놓쳤을 수 있는 최근 기능

- 버스 정류장을 선택하면 대중교통 노선 번호 표시
- 등산 및 자전거 경로(왼쪽 위 레이어 버튼에서 켜거나 끌 수 있음)
- 앱 설정을 통한 지도에 북마크 이름 표시
- ✎ 연필 아이콘을 눌러 북마크를 빠르게 편집

### Organic Maps 설치

[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid]에서 최신 Organic Maps를 다운로드하세요.

베타 테스트에서 새 기능을 먼저 사용해 보세요. [iOS][testflight] / [Android][firebase]

{{ <references lang /> }}
