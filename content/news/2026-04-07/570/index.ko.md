---
title: "4월 Organic Maps 업데이트: 등산·자전거 경로의 고도 그래프, 미국 주소 검색 개선, 180도 자오선을 가로지르는 지도"
date: 2026-04-07
slug: "hiking-cycling-routes-elevation-charts-us-address-search-antimeridian-map-wrapping-april-2026-organic-maps-update"
taxonomies:
  news: ["업데이트"]
---

이번 4월 업데이트에서는 오류를 수정하고 여러 기능을 개선했습니다. 등산할 때 얼마나 올라가야 하는지 확인하고, 주소를 더 쉽게 찾고, 지도의 경계에서 화면이 끊기지 않도록 하는 데 특히 집중했습니다. 기여해 주시고 좋은 후기와 [후원](@/donate/index.ko.md), [지원](@/contribute/index.ko.md)을 보내 주신 덕분에 이 세 가지와 그 밖의 여러 기능을 개선할 수 있었습니다.

봄을 맞아 새 등산로에 나서든 남반구의 가을을 즐기며 자전거로 멀리 나가든, 이번 업데이트가 다음 여행을 더 편하고 즐겁게 만들어 주길 바랍니다.

<https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid]에서 4월 업데이트를 다운로드하세요.

## 주요 변경 사항

- **경로를 눌러 고도 차이를 확인하세요.** 지도에서 등산이나 자전거 경로를 바로 선택할 수 있습니다. 경로를 누르면 강조 표시되고 고도 프로필을 바로 볼 수 있습니다.
- **미국 주소 200만 건 추가 및 검색 개선.** TIGER 인구조사 데이터에서 추출한 주소를 앱에 추가했습니다. 건물 번호를 더 정확하게 찾을 수 있게 되어 전반적인 검색 결과도 개선되었습니다. 검색을 개선하는 가장 좋은 방법은 빠진 주소를 [OpenStreetMap](https://www.openstreetmap.org)에 추가하는 것입니다.
- **끝없이 이어지는 지도.** 이제 Organic Maps의 지도를 경도 ±180°의 자오선 너머로 부드럽게 움직일 수 있습니다. 화면이 갑자기 초기화되거나 보이지 않는 경계에 막히지 않고 추코트카에서 알래스카로, 뉴질랜드에서 피지로 지도를 끌거나 돌려 보세요. 마침내 태평양이 둥글게 이어집니다.
- **목록의 색상을 한 번에 바꾸세요.** 한 번 눌러 목록의 북마크나 트랙 색상을 모두 바꿀 수 있습니다. 지난 여름에 여행하며 모은 기록을 보기 좋게 정리해 보세요.

## 업데이트 내역

### 모든 플랫폼

- 신규: TIGER 인구조사 데이터에서 추출한 주소 200만 건을 추가해 미국 주소 검색 개선 (Viktor Govako)
- 신규: 등산 및 자전거 경로의 여러 색상 표시를 개선하고, 경로를 눌러 고도 그래프를 볼 수 있게 함 (Viktor Govako)
- 4월 4일 기준 OpenStreetMap 데이터로 업데이트
- 4월 1일 기준 위키백과 데이터로 업데이트
- 다른 앱에 표시되는 값과 더 비슷하도록 트랙 그래프의 누적 상승 및 하강 고도 계산 조정 (Viktor Govako)
- 지도에서 현재 위치를 선택한 뒤 OpenStreetMap에 새 장소를 추가할 수 있음 (Mikhail Listratsenka)
- 푸드코트와 성문 아이콘 추가 (David Martinez)
- 의류 매장 하위 카테고리(여성, 남성, 아동, 웨딩, 스포츠, 속옷)와 사무실 유형 추가 (Viktor Govako)
- 검색 카테고리 업데이트. 제과점에 ‘Bread’ 동의어를 추가하고 샤와르마 요리 종류와 기타 동의어 개선 (Viktor Govako)
- 지도를 끌거나 돌릴 때 경도 ±180°에서 지도가 올바르게 이어지도록 수정 (Alexander Borsuk, Viktor Govako)
- 저속으로 자전거 길 안내를 받을 때 나침반 방향 사용 (HossamSaberr)
- 건물 번호를 이용한 주소 검색 개선 (Viktor Govako)
- 일부 지역 경계 근처에서 경로를 만들 때 발생하던 시스템 오류 수정 (Viktor Govako)
- 도시 이름과 주 이름이 같을 때의 검색 결과 수정 (Viktor Govako)
- 미국 도로 검색 동의어 highway, hwy, freeway, fwy 추가 (Viktor Govako)
- ‘장소 추가’를 누르면 편집기의 십자 표시가 어긋나던 문제 수정 (José Araújo)
- 일출이나 일몰 시각을 기준으로 영업하는 장소의 영업시간 표시 수정 (Alexander Borsuk)
- GPS 트랙을 기록할 때 구간 사이의 지점이 빠지던 문제 수정 (Alexander Borsuk)
- 시간대별 일광 절약 시간제 처리 수정 (Andrei Shkrob)
- 시드니 지하철 노선 색상 수정 (Alexander Borsuk)
- GeoJSON 가져오기 오류 수정 (Alexander Borsuk)
- 안정성 및 성능 개선 (Alexander Borsuk, Viktor Govako)
- 번역 업데이트 (Alexander Borsuk, Viktor Govako, Weblate 기여자)

### iOS

**구형 iPhone 및 iPad 사용자께 안내드립니다.** TestFlight와 App Store의 변경으로 이번 버전부터 iOS 15 이상만 지원합니다. iOS 12, 13, 14에 이미 설치된 Organic Maps는 계속 사용할 수 있지만 새 지도, 기능, 수정 사항은 iOS 15 이상에서만 제공됩니다.

- 신규: 한 번에 목록의 북마크와 트랙 색상을 모두 변경 (Kiryl Kaveryn)
- 북마크 상세 정보에 표와 이미지가 포함된 HTML 콘텐츠의 표시 개선 (Alexander Borsuk, Kiryl Kaveryn)
- 여러 구간으로 구성된 트랙의 고도 그래프에 세로 구분선 추가 (Kiryl Kaveryn)
- 고도 그래프에서 보간된 지점 선택 문제 수정 (Kiryl Kaveryn)
- 팝업 화면의 제스처 개선. 가장 가까운 위치에 멈추고, 가장자리에서 끌어 닫고, 다시 열면 이전 상태를 복원 (Kiryl Kaveryn)
- 추가 지도를 받으라는 메시지가 표시되어도 이용 가능한 경로라면 길 안내를 시작할 수 있음 (Kiryl Kaveryn)
- ‘장소 추가’ 화면의 탐색 막대 버튼을 누르기 쉽게 개선 (Noahdyn)
- 트랙을 내보낼 때 발생하던 비정상 종료 수정 (Alexander Borsuk, Kiryl Kaveryn)
- 장소 정보에서 열었을 때 북마크 및 트랙 목록의 검색 오류 수정 (Kiryl Kaveryn)

### Android

- 신규: 목록의 북마크와 트랙 색상을 모두 한 번에 변경 (Mikhail Listratsenka)
- 신규: 일출·일몰 시각에 따라 라이트 및 다크 테마를 자동 전환하는 화면 모드를 설정에 추가 (Dzmitry Strekha)
- 지도 편집기에 최근 사용한 카테고리 기록 추가 (Mikhail Listratsenka)
- 지도에서 선택한 트램 정류장에 트램 아이콘 표시 (Mikhail Listratsenka)
- 필요한 지도를 모두 받은 경우 다운로드 버튼을 숨김 (Mikhail Listratsenka)
- OpenStreetMap에 지도 수정 사항을 올릴 때의 오류 수정 (Viktor Govako)
- Google Drive 등 다른 앱으로 파일을 공유할 때의 오류 수정 (Alexander Borsuk)
- 최근 앱 목록에서 앱을 다시 열 때 북마크를 중복해서 가져오던 문제 수정 (Alexander Borsuk)
- `openstreetmap.org/search?query=Pizza`와 같은 OpenStreetMap 검색 URL을 열면 Organic Maps에서 검색을 시작 (Rawdyrathaur)
- 여러 비정상 종료 문제 수정 (Alexander Borsuk)

### 데스크톱(Linux 및 macOS)

- 경로 탐색에 참고할 트랙을 선택하는 기능 추가 (Viktor Govako)
- 일부 언어 설정에서 소수점 구분 기호가 달라 북마크나 트랙을 저장하거나 내보낼 때 파일이 손상되던 문제 수정 (Alexander Borsuk)

베타 테스트에서 새 기능을 써 보고 문제를 알려 주세요.
- [iOS][testflight]
- [Android][firebase]

감사의 마음을 담아 ❤️
Organic Maps 팀

{{ <references lang /> }}
