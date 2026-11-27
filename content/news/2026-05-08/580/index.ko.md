---
title: "5월 Organic Maps 업데이트: 정류장을 눌러 노선 보기, 북마크 이름 겹침 해결, 베트남·말레이시아·중국 남부 지도 세분화"
date: 2026-05-08
slug: "public-transport-stop-selection-not-overlapping-bookmark-labels-vietnam-malaysia-china-region-splits"
taxonomies:
  news: ["업데이트"]
---

5월 업데이트로 Organic Maps의 대중교통 지원이 한 걸음 더 나아갔습니다. 이제 버스, 기차, 페리 또는 트램 정류장에서 노선을 누르면 해당 노선의 색상으로 전체 운행 구간이 지도에 표시됩니다. 실제 온라인 시간표도 준비 중입니다. 아직 참여하지 않으셨다면 [지역의 OSM 대중교통 데이터를 추가하거나 업데이트해 주세요](https://gtfs-osm-matcher.organicmaps.app/)!

늘 함께해 주시는 기여자와 좋은 후기, [후원](@/donate/index.ko.md), [지원](@/contribute/index.ko.md)을 보내 주신 분들께 감사드립니다.

<https://get.omaps.org>, [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent], [F-Droid][fdroid]에서 5월 업데이트를 다운로드하세요.

## 주요 변경 사항

- **지도에서 버스, 트램, 기차 또는 페리 정류장을 누르세요.** 표시된 노선 목록에서 하나를 선택하면 Organic Maps가 지도에 전체 노선을 강조해 보여 줍니다.
- **북마크 이름과 지도가 더 잘 보입니다.** 북마크 이름이 빽빽하게 겹치지 않도록 배치 방식을 바꿨습니다. 보행자 구역은 조금 더 진하게 표시하고 라이트 및 다크 테마에서 경로가 잘 보이도록 색상을 조정했습니다.
- **아시아의 지도 지역을 세분화했습니다.** 베트남과 말레이시아 지도를 더 작은 지역으로 나눠 필요한 지역만 받을 수 있습니다. 홍콩, 마카오, 하이난의 지도도 광둥성과 분리했습니다.

## 업데이트 내역

### 모든 플랫폼

- 신규: 대중교통 정류장을 누르고 노선 번호를 선택하면 지하철 지도 레이어처럼 지도에 전체 노선이 강조 표시됨 (Viktor Govako, Kiryl Kaveryn, Mikhail Listratsenka)
- 신규: 지도에서 북마크 이름이 겹치지 않도록 개선 (Viktor Govako)
- 다른 지도 앱과 비슷한 값이 나오도록 트랙 그래프의 누적 상승 및 하강 고도 계산을 조정 (Viktor Govako)
- 장거리 대중교통 노선과 그 밖의 지도 관계를 지도 경계를 넘어 하나로 이어진 선으로 표시 (Viktor Govako)
- 베트남과 말레이시아를 개별적으로 다운로드할 수 있는 작은 지역으로 나눔 (Viktor Govako)
- 홍콩, 마카오, 하이난을 광둥성과 분리하고 인접 지역 경계 업데이트 (Viktor Govako)
- 인도네시아, 말레이시아, 탄자니아, 태국, 베트남의 등고선 업데이트 (Viktor Govako)
- 경로를 재개할 때 이미 지난 경유지 제외 (Viktor Govako)
- 활화산과 물길 접근 지점 아이콘 추가, 보트 진수로 검색 지원 (David Martinez)
- 물담배 라운지 추가 (alnzrv)
- 공사 중인 건물 추가 (Viktor Govako)
- 전망대 검색 동의어로 ‘Lookout’ 추가 (alnzrv)
- 미국 도로 검색 동의어로 ‘pkwy’ 추가 (Viktor Govako)
- 가독성을 높이기 위해 보행자 구역 색상을 조금 더 진하게 변경 (Viktor Govako)
- 지도에서 여러 줄의 텍스트가 깔끔하게 잘리도록 개선 (Viktor Govako)
- 도로명의 일부가 중복되던 문제 수정 (Viktor Govako)
- KMB 파일 가져오기 오류 수정 (Alexander Borsuk)
- 카테고리, 검색 동의어, 사용자 인터페이스 번역 업데이트 (Alexander Borsuk, Viktor Govako)
- 뉴사우스웨일스와 노던 준주의 설명 번역 (alnzrv)
- 문자 모양 처리, 글리프 캐싱, 경로선 자르기 등에서 안정성과 성능 개선 (Viktor Govako, Alexander Borsuk)

### iOS

- 신규: 길 안내 중 정보 패널에 트랙 기록 버튼 추가 (Kiryl Kaveryn)
- 신규: 길 안내 대시보드에 두 단계의 표시 크기를 추가해 고도와 경로 정보를 더 자세히 확인 (Kiryl Kaveryn)
- 길 안내 대시보드의 고도 그래프 스타일을 업데이트하고 고도가 음수인 트랙을 올바르게 표시 (Kiryl Kaveryn)
- TestFlight 버전에서 잘못된 북마크 목록이 표시되던 문제 수정 (Alexander Borsuk)
- 중지 버튼을 키우고 길 안내 하단 패널의 음성 음소거, 설정, 트랙 기록 버튼을 누르기 쉽게 개선 (Kiryl Kaveryn)
- 장소 정보에서 설명을 펼칠 때 나오는 애니메이션 개선 (Kiryl Kaveryn)
- 고도 그래프 탐색을 끝낼 때 장소 정보 화면이 닫히거나 갑자기 튀지 않도록 하고, 키보드를 연 채 편집할 때도 제목이 보이게 수정 (Kiryl Kaveryn)
- 시스템 화면 모드가 바뀔 때 고도 그래프와 원형 진행 표시의 색상 문제 수정 (Kiryl Kaveryn)
- 이미 사라진 트랙이나 북마크를 삭제할 때 발생하던 비정상 종료 수정 (Kiryl Kaveryn)

### Android

- 신규: 계속 표시되는 고도 대시보드와 개선된 경로 고도 프로필. 오른쪽에서 왼쪽으로 읽는 언어의 화면 배치도 지원 (Eric Jau, Mikhail Listratsenka)
- 기기를 회전해도 저장된 경로 상태 유지 (Mikhail Listratsenka)
- 장소 정보의 경로 안내선을 하나로 통일 (Mikhail Listratsenka)
- 하단 시트, 버튼, 그래픽 요소의 모서리를 더 둥글게 해 화면 디자인의 일관성 개선 (Mikhail Listratsenka)
- 시스템 바와 내비게이션 바 주변의 화면 배치 문제 수정 (Mikhail Listratsenka)
- 위키백과 문서의 서식, 시스템 색상, 다크 모드 표시 개선 (DeshDeepakKant, Mikhail Listratsenka)
- 여러 구간으로 구성된 트랙의 고도 그래프에 세로 구분선 추가 (Mikhail Listratsenka)
- 고도 그래프의 스크롤 동작 개선 (Mikhail Listratsenka)
- 오른쪽에서 왼쪽으로 읽는 화면의 배치 수정 (Mikhail Listratsenka)

### Linux 및 macOS

- 정류장을 선택한 뒤 특정 노선을 고를 수 있는 대중교통 노선 선택 기능 추가 (Viktor Govako)
- 장소 정보 화면에 경로 관련 버튼을 바로 표시 (Viktor Govako)
- 장소 정보에서 중복된 영업시간 제거 (Viktor Govako)
- 관심 지점이나 주소의 경유지 표지에 장소 이름 표시 (Viktor Govako)
- 앱을 정상 종료한 뒤 다시 열면 지도를 이어서 다운로드 (Alexander Borsuk)
- OpenGL ES 3.0 드라이버에서 Organic Maps 실행 지원 (Alexander Borsuk)

베타 테스트에서 새 기능을 써 보고 문제를 알려 주세요.
- [iOS][testflight]
- [Android][firebase]

사용자 여러분과 지도 만드는 일을 사랑합니다 ❤️

Organic Maps 팀

{{ <references lang /> }}
