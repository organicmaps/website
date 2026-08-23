---
title: もっと高度な地図編集をするには？
description: ID Editor、Go Map、Vespucci など、より高度なツールで OpenStreetMap を編集するためのチュートリアル
slug: 高度な地図編集
updated: "2026-08-23"
taxonomies:
  faq: ["地図編集"]
extra:
  order: 40
aliases:
  - /ja/faq/editing/advanced-map-editing/
---

Organic Maps には、地図を編集できるシンプルで使いやすいエディタが用意されています。ただしこのエディタは機能が限られており、単純な点の地物しか追加できません。つまり、建物の輪郭や道路、湖、街などは追加できません。組み込みのエディタでは編集できないものを変更したい場合は、この FAQ ページが役に立ちます。

Organic Maps で使われている地図データはすべて [OpenStreetMap.org（OSM）](https://www.openstreetmap.org) から提供されているため、地図はそちらで直接更新できます。変更した内容は、次回の地図更新で Organic Maps にも反映されます。

## OpenStreetMap のエディタ

OSM を編集する方法はいくつかあります。ノートパソコンやデスクトップパソコンが手元にあるなら、ブラウザ上で動く [ID Editor](https://www.openstreetmap.org/edit) を使うのがおすすめです。ID Editor は初心者にも扱いやすく、画面が大きくマウスとキーボードが使えるぶん、地図の編集がはかどります。

モバイル端末で高度な地図編集を行うには、iOS 向けの [Go Map](https://apps.apple.com/us/app/go-map/id592990211) か、Android 向けの [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android) を使いましょう。Go Map は初心者向け、Vespucci はより上級者向けです。LearnOSM には [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) と [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/) のチュートリアルがあります。

もっと手軽に楽しく編集したい場合は、iOS と Android 向けの [Every Door アプリ](https://every-door.app/)や、Android 向けの [StreetComplete アプリ](https://streetcomplete.app/)も試してみてください。

#### ID Editor

ID Editor を使って OpenStreetMap を編集する手順は次のとおりです。

1. [OpenStreetMap.org](https://www.openstreetmap.org) でアカウントを新規作成するか、ログインします
2. OpenStreetMap.org で編集したい場所を表示し、上部の *編集* をクリックします
3. *ウォークスルーを開始* して、ID Editor を説明する短いチュートリアルに従います
4. 地図を編集します
5. 変更をアップロードします

これで完了です。あなたも OSM コミュニティの一員になりました。

## 編集した内容はどうなりますか？

*アップロード* を押すと、変更はただちに OSM の公開データベースに反映されます。編集するときは、周りへの配慮を忘れないようにしましょう。Organic Maps では、変更内容は次回の月次地図更新のあとに表示されます。

メールアドレスは公開されませんが、OSM のユーザー名はほかの人にも見えます。OSM には変更内容について話し合う仕組みがあるため、ほかの OSM 貢献者から編集について質問が届くことがあります。その通知は、OSM アカウントの登録に使ったメールアドレスに送られます。OSM は協力によって成り立つコミュニティプロジェクトですから、こうした質問には必ず答えるようにしましょう。

## コミュニティと Wiki

OpenStreetMap はコミュニティです。助けが必要なときや質問があるときは、[OSM フォーラム](https://community.openstreetmap.org/c/help-and-support)で尋ねるか、[OSM Wiki](https://wiki.openstreetmap.org/) のドキュメントをご覧ください。

## タグ - OSM のデータモデルの仕組み

OpenStreetMap のデータベースには、現実世界の地物を抽象化したノード、ウェイ、エリア、リレーションといったオブジェクトが含まれています。これらのオブジェクトには、内容をさらに説明するための属性、いわゆるタグが付きます。タグはキーと値の組み合わせです。

これは実際よりも複雑に聞こえるので、例を挙げましょう。
たとえばレストランは、`amenity=restaurant` というタグを付けたノードまたはエリアとして地図に登録します。さらに `cuisine=*` や `opening_hours=*` などのタグを使えば、より詳しい情報を加えられます。

> ID Editor は初心者にも扱いやすいよう、内部のデータ構造をユーザーから隠しています。ただし Wiki のドキュメントを読むうえでは、データ構造の概要を知っておくと役立ちます。
ID Editor では、*地物を編集* サイドパネルの *タグ* セクションを開くと、エディタが隠しているタグを確認できます。

## OSM ノート {#osm-note}

自分で OSM のデータを編集する時間がない場合や、問題が複雑すぎる場合は、OSM ノート（[Wiki](https://wiki.openstreetmap.org/wiki/Notes)）を使いましょう。地図に誤りがある場所にノートを置き、問題を詳しく説明できます。すると、ほかの OSM ボランティアが手を貸して問題を解決してくれます。追加の質問があったときや OSM ノートが解決されたときは、OSM アカウント経由でメール通知が届きます。

1. [OpenStreetMap.org](https://www.openstreetmap.org) でアカウントを新規作成するか、ログインします
   > 匿名でノートを作成することもできますが、問題が解決したときや追加の質問があったときに通知が届かないため、おすすめしません。
2. [OpenStreetMap.org](https://www.openstreetmap.org) で地図上のその場所までズームし、*地図にメモを追加*（右側メニューの下から 2 番目のアイコン）を押します。そのあと、青い地図マーカーを正確な位置までドラッグします。
   > できるだけ正確に合わせてください。
3. 地図の問題を詳しく説明し、*メモを追加* を押します
   > たとえば店舗なら、店名を挙げ、そこで何が売られているか、どんなサービスが提供されているかを書き添えてください。
