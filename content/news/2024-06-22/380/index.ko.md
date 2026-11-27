---
title: "6월 대규모 업데이트와 후속 OSM 지도 업데이트 배포"
date: 2024-06-22T14:08:52+00:00
slug: june-release-with-uk-and-us-postal-zip-code-search-street-name-announcements-and-gpx-export
aliases: ["/ko/news/2024-06-22/the-major-june-update-and-a-follow-up-osm-data-only-update-with-a-hotfix-for-the-ios-app-hanging-were-successfully-published-and-are-available-in-all-app-stores-and-on-our-github/"]
taxonomies:
  news: ["업데이트"]
---

6월 대규모 업데이트와 OSM 지도 데이터만 갱신하는 후속 업데이트(iOS 앱이 멈추는 문제의 긴급 수정 포함)를 배포했습니다. [모든 앱 스토어](https://omaps.app/get)와 [GitHub](https://github.com/organicmaps/organicmaps/releases/)에서 받을 수 있습니다.

Viktar Havaka 덕분에 이제 미국과 영국 우편번호를 검색할 수 있습니다! 주소 데이터는 TIGER 데이터베이스와 영국 국가지리원(Ordnance Survey)에서 가져와 OpenStreetMap 검색에 쓰이는 [Nominatim 프로젝트](https://nominatim.org/)로 전처리했습니다.

Will Bradley가 길 안내 중 도로 이름을 읽어 주는 기능을 추가했습니다. Organic Maps 설정에서 켜 보시고 문제를 발견하면 알려 주세요.

Kiryl Kaveryn 덕분에 오랫동안 기다려 온 iOS iCloud 동기화도 이용할 수 있습니다. Organic Maps 설정에서 활성화하세요. 설정 중 모든 북마크와 트랙을 먼저 백업할 수 있습니다. 문제가 생기면 알려 주세요.

기존 KML(KMZ) 외에 GPX로도 북마크와 트랙을 내보낼 수 있습니다. 오랫동안 개발해 온 트랙 기록 기능을 완성하면 더욱 유용해질 것입니다. cyber-toad에게 감사드립니다!

늘 기여해 주시고 [후원](@/donate/index.ko.md), [지원](@/contribute/index.ko.md), 좋은 후기를 보내 주시는 모든 분께 감사드립니다. 여러분 덕분에 개발팀이 힘을 얻습니다!

공통 변경 사항과 수정 사항:
* 6월 13일 기준 최신 OpenStreetMap 데이터
* 미국 및 영국 우편번호 검색 -- Viktar Havaka
* 음성(TTS) 길 안내에서 도로 이름을 읽어 주는 기능(설정에서 켜 주세요) -- Will Bradley
* 북마크와 트랙을 GPX 형식으로 내보내기 -- cyber-toad, Kiryl Kaveryn
* 음식점, 바, 음식 서비스 업체의 메뉴 웹 링크를 추가, 편집, 표시 -- Arthur Gayot, Kiryl Kaveryn
* 피트니스 센터의 장소 정보에 누락된 주소 표시
* ‘pastry’와 ‘cakes’ 검색어 추가
* 물음표가 들어 있는 위키백과 링크 수정

Android:
* 북마크와 트랙을 기기에 내보내기
* 길 안내 중 다음 방향 전환을 항상 표시
* 길 안내 알림에 종료 버튼 추가
* OSM 사용자 프로필 설정 화면 개선 -- Harry Bond
* 오른쪽에서 왼쪽으로 읽는 언어에서 자 도구와 대중교통 모드의 경유지 표시 수정

Android Auto:
* 차량 센서의 나침반 및 위치 데이터 사용 -- Andrew Shkrob
* 기본 화면과 카테고리 화면 업데이트 -- Andrew Shkrob

iOS:
* iCloud로 북마크 및 트랙 동기화(설정에서 켜 주세요) -- Kiryl Kaveryn
* CarPlay에 연결된 상태에서도 지도 사용 가능 -- Oleg Montak
* CarPlay 다크 모드의 글자 색상 수정
* 더 다양한 TTS 음성 옵션
* 방향 전환 안내가 나올 때 팟캐스트의 음량을 낮추는 대신 재생 일시 중지
* 지도에 장소를 추가할 때 사라지던 일부 버튼 복원
* 북마크를 편집한 뒤 장소 정보가 갱신되지 않던 문제 수정
* 자정 이후에도 편집기의 영업시간 외 시간대 설정 버튼이 작동하도록 수정

모바일 Linux 및 데스크톱 버전:
* 선택한 장소의 상세 정보 창 개선

체코어, 독일어, 포르투갈어 번역을 업데이트했습니다.

🚀 🚀 🚀 🚀 🚀
