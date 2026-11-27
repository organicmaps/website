---
title: "2026년 6월 업데이트: 위성 영상, 대중교통 경로, 대체 경로, 새 Android 검색·경로 계획 화면, iOS 큰 글자 지원"
date: 2026-06-29
slug: satellite-imagery-public-transport-routes-alternate-routes-new-search-and-route-planning-interface-for-android-large-accessibility-fonts
taxonomies:
  news: ["업데이트"]
---

Organic Maps 6월 업데이트에서는 오류를 수정하고 다음과 같은 새 기능을 추가했습니다.
- 위성 영상
- 대중교통 경로
- 대체 경로
- Android의 새로운 검색 및 경로 계획 화면
- iOS의 접근성 설정에서 큰 글자 크기 지원

<https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid]에서 다운로드하고 의견을 알려 주세요!

## 자세한 변경 내역

- 신규: 지하철, 경전철, 버스, 트램을 이용하는 대중교통 경로 안내 _(Viktor Govako)_
- 신규: 가장 빠른 경로 외에 가장 짧은 경로를 대체 경로로 표시 _(Viktor Govako)_
- 신규: 도보 및 자전거 경로에 계단, 출입문, 차단기 주의 표시 _(Viktor Govako)_
- 신규: 북마크 색상을 자유롭게 선택 _(Alexander Borsuk, Mikhail Listratsenka)_
- 신규: 영국 국가 격자(OS Grid), 아일랜드 격자(Irish Grid), 아일랜드 횡메르카토르(ITM) 좌표 지원 _(Alexander Borsuk)_
- 실험 기능: Organic Maps 설정의 ‘위성 이미지’에서 사용자 지정 래스터 타일 서버 URL을 입력해 위성 영상을 켤 수 있습니다. 자체 서버는 준비 중이므로 URL에 `{x}`, `{y}`, `{z}` 자리표시자가 포함된 공개 서버를 찾아 이용해 주세요. _(Viktor Govako, renderexpert)_
- 6월 24일 기준 OpenStreetMap 데이터로 업데이트 _(Viktor Govako)_
- 이탈리아어 문서를 포함해 6월 20일 기준 위키백과 데이터로 업데이트 _(Alexander Borsuk)_
- 검색란에 `?map-download-server:https://your-server.com/`을 입력하면 Organic Maps의 기본 지도 다운로드 서버를 바꿀 수 있습니다. `?no-map-download-server`를 입력하면 기본 서버로 되돌립니다. _(Alexander Borsuk)_

#### 지도 표시 및 스타일

- 해변, 모래, 돌비탈, 노출된 암반, 과수원, 포도밭의 무늬와 보호 구역 및 습지 빗금 개선 _(Alexander Borsuk)_
- 도로와 강을 따라 휘어진 이름을 더 자연스럽게 표시 _(Viktor Govako)_
- 다크 모드에서 강, 개울, 습지의 대비를 높여 더 잘 보이도록 개선 _(Alexander Borsuk)_
- 카테고리 검색과 지도 위 검색 결과에 새 아이콘 및 개선된 아이콘 적용 _(Anton Makouski)_
- 여러 언어의 문자 모양과 표시 개선 _(Alexander Borsuk)_
- 다양한 오류 수정 및 성능 개선 _(Viktor Govako)_

#### 트랙, 북마크 및 경로

- GeoJSON 트랙을 가져오거나 내보낼 때 고도와 기록 시각 유지 _(Alexander Borsuk)_
- 트랙을 다른 목록으로 옮긴 뒤 발생하던 비정상 종료 수정 _(Viktor Govako)_
- 문화유산의 웹사이트 표시 _(Viktor Govako)_
- 이름이 없는 검색 결과에 운영 기관 이름 표시. 예를 들어 이름이 없는 ATM에 은행 이름을 표시 _(Anton Makouski)_
- 편집기에서 OpenStreetMap 아파트 건물 편집 및 변경 모음의 설명 수정 _(titanniya542-spec)_
- 북마크와 트랙 설명의 HTML 감지 개선 _(Alexander Borsuk)_

### iOS

- 신규: 접근성 기능인 Dynamic Type과 큰 글자 크기 지원 _(Kiryl Kaveryn)_
- 신규: 겹쳐 있는 트랙과 경로를 눌러 원하는 항목 선택 _(Kiryl Kaveryn)_
- 북마크 및 트랙 설명의 HTML 표시 개선 _(Kiryl Kaveryn)_
- 앱 화면의 표 스타일 정리 _(Kiryl Kaveryn)_

### Android

- 신규: 검색 화면 _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- 신규: 경로 계획 화면 _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- 북마크 및 트랙 설명의 HTML 표시 개선 _(Mikhail Listratsenka)_
- APK 크기 감소 _(Alexander Borsuk)_
- 텍스트 음성 변환 엔진이 없으면 음성 아이콘을 비활성 상태로 표시 _(Mikhail Listratsenka)_
- 긴 북마크 및 트랙 설명에 ‘더 보기…’ 버튼 표시 _(Mikhail Listratsenka)_
- 여러 화면 오류와 API에서 반환하는 지점 ID 수정 _(Mikhail Listratsenka)_

### 데스크톱

- 지도에 표시하는 좌표계 전환 지원 _(Alexander Borsuk)_
- 선택한 장소의 정보를 왼쪽에 표시 _(Viktor Govako)_
- 상황에 맞는 메뉴의 위치 수정 _(Osyotr)_
- Qt 6.4 이하에서 OpenStreetMap 로그인 및 편집 중 멈추던 문제 수정 _(Alexander Borsuk)_
- macOS에서 길 안내 중 지도 스타일이 예기치 않게 바뀌던 문제 수정 _(Alexander Borsuk)_
- KMZ 파일을 내보낸 후 macOS 앱을 닫을 때 발생하던 비정상 종료 수정 _(Alexander Borsuk)_

### 번역

- 광둥어 음성 길 안내 추가 _(Alexander Borsuk)_
- 독일어 및 프랑스어 번역 업데이트 _(Wuzzy, Alexander Borsuk)_
- 중국어, 세르비아어, 카탈루냐어에서 도로로 진입할 때 나오는 음성 안내 번역 수정 _(Alexander Borsuk)_

## 베타 테스트에서 새 기능을 써 보고 문제를 알려 주세요

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

모든 사용자와 기여자, [후원해 주신 분들](@/donate/index.ko.md), 앱 스토어에서 Organic Maps에 별 5개를 주신 분들께 감사드립니다. 더 좋은 지도 앱을 함께 만들어요!

감사의 마음을 담아,
Organic Maps 팀

{{ <references lang /> }}
