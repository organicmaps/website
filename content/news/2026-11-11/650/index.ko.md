---
title: "Organic Maps 2026년 11월 업데이트: 3D 지형, 바다 수심, 가져온 영역, 경로 반전"
date: 2026-11-11
slug: "3d-terrain-hillshading-ocean-depths-imported-area-polygons-on-the-map-route-reversal-november-2026"
taxonomies:
  news: ["업데이트"]
---

3D 지형과 바다 수심을 살펴보고, 경로의 방향을 뒤집고, 가져온 영역과 트랙 진행 방향 화살표를 확인할 수 있습니다. Android에는 상세 대중교통 안내, 새 속도 표시, 트랙 기록 위젯이 추가되었습니다. 아래에서 모든 개선 사항을 확인하세요.

[get.omaps.org](https://get.omaps.org)에서 Organic Maps를 다운로드하고 주변에도 알려 주세요. 모든 사용자, 기여자, 후원자, 응원해 주시는 분들께 감사드립니다!

## 업데이트 내역

### 지도와 장소

- 신규: 3D 지형, 바다 수심, 미터와 피트 단위의 등고선, 지도 어디서나 고도 확인 _(Viktor Govako, Alexander Borsuk)_
- 2026년 11월 10일 기준 OpenStreetMap 데이터
- 2026년 11월 1일 기준 위키백과 문서
- 물 색상을 개선하고 강의 폭을 넓혔으며 물 지형의 이름에 옅은 테두리 추가 _(David Martinez, Viktor Govako)_
- 간헐적으로 흐르는 하천, 운하, 배수로 등 물길의 표시 개선 _(Alexander Borsuk)_
- 트램, 모노레일, 푸니쿨라, 협궤 철도의 교량 윤곽 추가 _(Alexander Borsuk)_
- 이발소, 필라테스 스튜디오, 창호 시공 업체, 상수도 시설, 덮개가 있는 저수 시설 추가 _(Viktor Govako)_
- 북극 부근의 물 영역 누락 등 색을 채운 영역에 생기던 빈틈 수정 _(Viktor Govako)_
- 문자 표기 변환 오류 수정 _(Alexander Borsuk)_
- 성능 향상 및 메모리 사용량 감소 _(Viktor Govako)_
- 지도 스타일을 바꿀 때 발생하던 비정상 종료 및 렌더링 오류 수정 _(Mikhail Listratsenka)_
- 지도 다운로드 지역의 경계 수정 _(Viktor Govako, Alexander Borsuk)_
- 검색 추천에 원래 철자, 발음 구별 기호, 대소문자 유지 _(Alexander Borsuk)_
- 미용실과 이발소 검색 결과에서 관련 없는 뷰티 살롱 제외 _(Viktor Govako)_

### 북마크, 트랙 및 영역

- 신규: KML, KMZ, GeoJSON 영역을 가져와 색이 있는 윤곽선, 채우기, 내부의 빈 영역을 지도에 표시 _(Alexander Borsuk, Viktor Govako)_
- 트랙의 진행 방향을 나타내는 화살표 추가 _(Alexander Borsuk)_
- 선택한 트랙을 강조 표시 _(Alexander Borsuk)_
- 목록에서 트랙을 열면 트랙의 시작점을 선택 _(Alexander Borsuk)_
- 언어에 맞게 북마크와 트랙 이름 정렬 _(Alexander Borsuk)_
- 새로 불러올 때 북마크 목록의 이름, 설명, 이미지 갱신 _(Kiryl Kaveryn, Alexander Borsuk)_
- KML로 저장한 경로에 경유지와 이동 수단을 유지하고 GPX 및 GeoJSON을 내보낼 때 경유지를 웨이포인트로 포함 _(Alexander Borsuk)_
- 편집한 트랙을 삭제하거나 삭제 창으로 돌아갈 때 발생하던 비정상 종료 수정 _(Viktor Govako)_
- 비정상 종료 시 복구할 수 있도록 기록 중인 트랙을 1분마다 저장 _(Viktor Govako)_
- 업데이트 요약에서 지도 개수를 중복으로 세고 다운로드 크기를 실제보다 크게 표시하던 문제 수정 _(Alexander Borsuk)_

### 경로 탐색과 길 안내

- 신규: 자동차, 자전거, 도보 경로에서 피할 도로 유형을 각각 설정 _(Alexander Borsuk, Mikhail Listratsenka)_
- Android와 iOS에서 경로 지점 아이콘을 서로 연결하고 ‘목적지 추가’ 문구를 알기 쉽게 개선 _(Kiryl Kaveryn, Mikhail Listratsenka)_
- 경로 계산에 실패하더라도 목적지 추가 가능 _(Kiryl Kaveryn)_
- 경로 탐색 알고리즘 개선 _(Viktor Govako)_
- 경로 재계산 개선 _(Alexander Borsuk)_
- 지도와 정보 패널에 표시되는 경로 소요 시간이 일치하지 않던 문제 수정 _(Alexander Borsuk)_
- 이전 구간의 과속 단속 카메라 경고가 남아 있거나 제한 속도가 늦게 갱신되던 문제 수정 _(Alexander Borsuk)_
- 저장한 경로 관련 문제 수정 _(Alexander Borsuk)_
- 경로 복원 개선 _(Alexander Borsuk, Mikhail Listratsenka)_
- 대중교통 도착 예정 시각, 도보 연결 구간, 역 출입구 표지 개선 _(Alexander Borsuk)_

### OpenStreetMap 편집기

- 카테고리 검색 개선 _(Alexander Borsuk)_
- 언어에 맞게 요리 종류 이름 정렬 _(Alexander Borsuk)_
- 카테고리 정렬 오류 수정 _(Alexander Borsuk)_

### 번역

- 앱 화면, 장소 유형, 검색 카테고리, 다운로드 지역 이름에 웨일스어 추가 _(Carl Morris, Alexander Borsuk)_
- 시스템 언어 옵션 추가: Android(아스투리아스어, 갈리시아어, 크로아티아어, 아르메니아어, 아이슬란드어, 라오어, 알바니아어), iOS(아스투리아스어, 캐나다 프랑스어, 갈리시아어, 크로아티아어, 아이슬란드어) _(Alexander Borsuk)_
- 슬로베니아어 검색 카테고리 수정 _(Alexander Borsuk)_
- 우크라이나어, 체코어, 스웨덴어, 한국어 번역을 개선하고 다른 언어의 문구와 브랜드 표기 수정 _(Nnifria, Alexander Borsuk, bilykralik16, Jonatan Nyberg, Dmitry Gribenchuk, M)_
- 거리 및 시간 단위와 대중교통 승강장 표기 수정 _(Alexander Borsuk)_
- 아랍어, 체코어 음성 안내 개선 및 카탈루냐어, 덴마크어, 갈리시아어 길 안내의 거리 표기 수정 _(Alexander Borsuk, Anquanna)_
- 노르웨이어 보크몰의 장소 이름과 편집한 이름 업로드 수정 _(Alexander Borsuk)_
- 앱 정보 페이지의 링크가 해당 언어의 그룹을 열도록 수정 _(Alexander Borsuk)_

### iOS

- 신규: 모든 경유지를 포함해 경로 방향을 뒤집는 버튼 추가 _(Kiryl Kaveryn)_
- 경로 계획 화면에서 출발지와 목적지를 포함해 모든 지점 삭제 가능 _(Kiryl Kaveryn)_
- 길 안내 음성 목록의 정렬을 개선하고 누락된 미리 듣기 문장 추가 _(Alexander Borsuk, Kiryl Kaveryn)_
- 다크 모드에서 자 도구의 거리와 누른 경로 지점의 이름이 더 잘 보이도록 수정 _(Alexander Borsuk)_
- 대중교통 경로 미리 보기에 기호를 추가하고 노선 색상을 선명하게 조정했으며 노선 번호 줄바꿈과 오른쪽에서 왼쪽으로 읽는 화면 배치를 개선 _(Alexander Borsuk, Kiryl Kaveryn)_
- 오른쪽에서 왼쪽으로 읽는 화면의 나침반 버튼 수정 _(Kiryl Kaveryn)_
- 닫은 뒤에도 장소 정보가 남아 있거나, 드래그할 때 움직이거나, 다른 지도 링크를 열면 사라지던 문제 수정 _(Kiryl Kaveryn)_
- 장소 정보를 불러오는 중 지도 다운로드로 정보가 갱신될 때 발생하던 비정상 종료 수정 _(Kiryl Kaveryn)_
- 장소 정보에서 주요 동작 버튼을 강조 표시 _(Kiryl Kaveryn)_
- 메뉴 및 설정 링크를 수정해 해당 옵션으로 스크롤하고 강조 표시 _(Kiryl Kaveryn)_
- 큰 글자를 사용할 때 처음 길 안내를 시작하는 화면의 확인 버튼 수정 _(Kiryl Kaveryn)_
- 경유지 수가 한도에 도달했을 때 경로 지점을 바꾸는 동작과 저장된 트랙의 교체 문구 수정 _(Kiryl Kaveryn)_
- 지도로 돌아가거나 트랙의 시작점을 선택하거나 평탄한 구간 또는 확대된 구간을 볼 때 고도 프로필 표시 수정 _(Kiryl Kaveryn)_
- CarPlay 북마크 목록이 편집하거나 다시 불러온 뒤 갱신되며, 화면에 들어가는 항목을 모두 표시하고 삭제된 항목을 올바르게 처리 _(Kiryl Kaveryn, Alexander Borsuk)_
- 미리 보기에서 경로 설정 표시가 잘리던 문제 수정 _(Kiryl Kaveryn)_
- 백그라운드를 포함해 다운로드 취소, 재시도, 이어받기 개선 _(Viktor Govako)_

### Android

- 신규: Android Auto를 포함해 현재 속도와 제한 속도 표시를 새롭게 디자인 _(Andrei Shkrob)_
- 신규: 탑승, 환승, 하차 지점과 펼쳐 볼 수 있는 경유 정류장 목록을 전체 화면으로 제공하는 대중교통 안내 _(Paal Williams)_
- 신규: 트랙 기록을 시작하고 경과 시간, 거리, 고도를 확인하는 홈 화면 위젯 _(Mikhail Listratsenka)_
- 신규: 모든 경유지를 포함해 경로 방향을 뒤집는 버튼 추가 _(Mikhail Listratsenka)_
- 신규: 평균 해수면(MSL)을 기준으로 고도를 표시하고 기록 _(Alexander Borsuk)_
- 트랙 기록을 시작할 때 배터리 제한을 확인하도록 한 번 안내하고 시스템 설정 바로가기 제공. <https://dontkillmyapp.com> 참고 _(Harsh Mishra, Alexander Borsuk)_
- 경로 계획 화면에서 출발지와 목적지를 포함해 모든 지점 삭제 가능 _(Mikhail Listratsenka)_
- 화면 표시 문제를 수정하고 장소 정보의 주요 경로 버튼을 강조 _(Mikhail Listratsenka)_
- Android Auto 비정상 종료 수정 _(Andrei Shkrob, Mikhail Listratsenka)_
- 검색 버튼을 다시 누르거나 길 안내를 종료하면 카테고리 검색 결과를 지우도록 수정 _(Mikhail Listratsenka)_
- 국가 폴더 아이콘을 누르면 하위 지역이 열리고 이전 검색 결과가 열린 폴더를 덮어쓰지 않도록 수정 _(Mikhail Listratsenka)_
- 개인정보 보호 설정에 Android 백업 설정을 여는 ‘북마크 및 트랙 백업’ 추가 _(Mikhail Listratsenka)_
- 라이트 및 다크 테마에서 북마크와 트랙 설명의 가독성 개선 _(Mikhail Listratsenka)_
- 24시간에 걸친 영업시간 편집 문제 수정 _(Alexander Borsuk)_
- 일광 절약 시간제 전환을 거치는 경로의 도착 시각 수정 _(Alexander Borsuk)_
- 편집기에서 도로나 셀프서비스 옵션을 두 번 눌렀을 때 발생하던 비정상 종료 수정 _(Kevin Coughlin)_
- 다른 앱이 공유한 북마크 파일이 없거나 지원되지 않을 때 발생하던 비정상 종료와 불완전한 가져오기 수정 _(Darafei Praliaskouski)_
- 그래픽 컨텍스트가 변경될 때 Vulkan에서 발생하던 렌더링 오류 및 비정상 종료 수정 _(Alexander Borsuk)_

### 데스크톱

- 앱 화면과 장소 유형을 번역하고 번역이 없을 때의 언어 선택 및 오른쪽에서 왼쪽으로 읽는 화면 배치를 개선 _(Alexander Borsuk)_
- 장소 정보에서 라틴 문자 이외의 문자가 포함된 링크와 설명 미리 보기 수정 _(Alexander Borsuk)_
- OpenStreetMap 편집기에서 요리 종류 선택을 저장하고 장소를 삭제하는 동작 수정 _(Alexander Borsuk)_
- 검색 중 지도 다운로드 창을 닫을 때 발생하던 비정상 종료 수정 _(Alexander Borsuk)_
- 창 크기를 조절할 때 지도 렌더링 문제 수정 _(Alexander Borsuk)_
- 위치 정보 갱신을 개선하고 위치 오류 발생 후 ‘내 위치’ 버튼이 작동하지 않던 문제 수정 _(Alexander Borsuk, Vladislav Shadiuk)_

<https://beta.omaps.app>에서 새 기능을 먼저 써 보고 베타 테스트에 참여하세요.

Organic Maps를 사용하고 응원해 주셔서 감사합니다!

Organic Maps 팀 드림

{{ <references lang /> }}
