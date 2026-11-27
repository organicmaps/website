---
title: 더 복잡한 지도 편집은 어떻게 하나요?
description: ID Editor, Go Map, Vespucci 등 고급 도구로 OpenStreetMap을 편집하는 방법입니다.
updated: "2026-11-23"

taxonomies:
  faq: ["지도 편집"]

extra:
  order: 40
---

Organic Maps에는 간단하고 쓰기 쉬운 지도 편집기가 있습니다. 지도 위의 점으로 표시되는 장소만 편집할 수 있으므로 건물 윤곽, 도로, 호수, 마을 등은 추가할 수 없습니다. Organic Maps의 내장 편집기로 수정할 수 없는 항목을 편집하는 방법을 소개합니다.

Organic Maps의 모든 지도 데이터는 [OpenStreetMap.org(OSM)](https://www.openstreetmap.org)에서 가져오므로 해당 사이트에서 직접 지도를 수정할 수 있습니다. 수정 사항은 다음 지도 업데이트에 반영됩니다.

## OpenStreetMap 편집 도구

OSM을 편집하는 방법은 여러 가지입니다. 노트북이나 데스크톱이 있다면 브라우저에서 작동하는 [ID Editor](https://www.openstreetmap.org/edit)를 사용해 보세요. ID Editor는 처음 쓰는 사람도 쉽게 익힐 수 있고 큰 화면, 마우스, 키보드로 편하게 편집할 수 있습니다.

모바일 기기에서 고급 편집을 하려면 iOS용 [Go Map](https://apps.apple.com/us/app/go-map/id592990211) 또는 Android용 [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android)를 사용하세요. Go Map은 초보자도 쉽게 사용할 수 있고, Vespucci는 숙련된 사용자를 위한 도구입니다. LearnOSM에서 [Go Map](https://learnosm.org/en/mobile-mapping/gomap/)과 [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/) 사용법을 확인할 수 있습니다.

더 간단하고 재미있게 편집하려면 iOS와 Android에서 [Every Door 앱](https://every-door.app/)을, Android에서 [StreetComplete 앱](https://streetcomplete.app/)을 써 보세요.

#### ID Editor

OpenStreetMap을 편집하려면 다음 단계를 따르세요.

1. [OpenStreetMap.org](https://www.openstreetmap.org)에서 계정을 만들거나 로그인하세요.
2. OpenStreetMap.org에서 편집할 위치로 이동하고 화면 상단의 *편집*을 누르세요.
3. *연습 시작하기*를 눌러 ID Editor의 기본 사용법을 익히세요.
4. 지도를 편집하세요.
5. 변경 사항을 업로드하세요.

이제 OSM 커뮤니티의 일원입니다.

## 수정 사항은 어떻게 반영되나요?

*업로드*를 누르면 수정 사항이 공개 OSM 데이터베이스에 즉시 추가되므로 신중하게 편집하세요. Organic Maps에는 다음 월간 지도 업데이트 이후 수정 사항이 표시됩니다.

이메일 주소는 공개되지 않지만 다른 사용자가 OSM 사용자 이름을 볼 수 있습니다. 다른 OSM 기여자가 변경 사항에 대한 토론 기능으로 편집 내용에 대해 질문할 수 있습니다. 알림은 OSM 계정에 등록된 이메일 주소로 전송됩니다. OSM은 함께 만드는 프로젝트이므로 질문을 받으면 답변해 주세요.

## 커뮤니티와 위키

OpenStreetMap은 커뮤니티가 함께 만드는 지도입니다. 도움이 필요하거나 질문이 있다면 [OSM 포럼](https://community.openstreetmap.org/c/help-and-support)에 문의하거나 [OSM 위키](https://wiki.openstreetmap.org/) 문서를 읽어 보세요.

## 태그와 OSM 데이터 구조

OpenStreetMap 데이터베이스는 실제 지형/지물을 노드, 길, 영역, 관계 등의 객체로 표현합니다. 태그는 각 객체의 속성을 설명합니다. 태그 하나는 키와 값의 조합입니다.

복잡하게 느껴진다면 다음 예를 보세요.
음식점은 `amenity=restaurant` 태그가 붙은 노드 또는 영역으로 표시할 수 있습니다. `cuisine=*`이나 `opening_hours=*` 같은 태그로 세부 정보를 추가할 수 있습니다.

> 처음 사용하는 사람을 위해 편집기에서 내부 데이터 구조를 숨깁니다. 이 구조를 간단히 알아 두면 위키 설명서를 읽을 때 도움이 됩니다.
ID Editor에서 편집자가 숨긴 태그를 보려면 사이드 패널에서 *지형/지물 편집* 섹션의 *태그* 항목을 펼치세요.

## OSM 메모 {#osm-note}

시간이 없거나 수정하기에 너무 복잡한 문제라면 OSM 메모([위키](https://wiki.openstreetmap.org/wiki/Notes))를 남기세요. 지도에서 오류가 있는 위치에 메모를 추가하고 문제를 자세히 적으면 OSM 자원봉사자가 해결할 수 있습니다. 추가 질문이 있거나 OSM 메모가 해결되면 OSM 계정을 통해 이메일 알림을 받습니다.

1. [OpenStreetMap.org](https://www.openstreetmap.org)에서 계정을 만들거나 로그인하세요.
   > 익명으로 메모를 남길 수도 있지만 문제가 해결되거나 추가 질문이 있어도 알림을 받을 수 없기 때문에 권장하지 않습니다.
2. [OpenStreetMap.org](https://www.openstreetmap.org)에서 해당 위치를 확대하고 *지도에 '노트'하기*(오른쪽 메뉴에서 아래에서 두 번째 아이콘)를 누르세요. 그런 다음 파란색 마커를 정확한 위치로 끌어 놓으세요.
   > 위치를 가능한 한 정확히 표시하세요.
3. 지도 문제를 자세히 설명하고 *참고 추가*를 누르세요.
   > 상점의 경우 이름과 판매하는 상품 또는 제공하는 서비스를 적으세요.
