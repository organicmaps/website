---
title: "Organic Maps 2026年11月更新：3D地形、海の深さ、ポリゴンのインポート、ルートの反転"
date: 2026-11-11
slug: "3d-chikei-umi-no-fukasa-porigon-no-inpoto-ruto-no-hanten-2026-juichigatsu"
aliases: ["/ja/news/2026-11-11/3d-terrain-hillshading-ocean-depths-imported-area-polygons-on-the-map-route-reversal-november-2026/"]
taxonomies:
  news: ["Releases"]
---

3D地形や海の深さを探索し、ルートを反転したり、インポートしたポリゴンやトラックの方向矢印を表示したりできるようになりました。Androidには詳しい公共交通案内、新しい速度表示、トラック記録ウィジェットを追加。すべての改善点は以下で紹介します。

[get.omaps.org](https://get.omaps.org)でOrganic Mapsを入手して、周りにも紹介してみてください。ユーザー、貢献者、寄付者、支援者のみなさんに感謝します！

## リリースノート

### 地図と場所

- 新機能！3D地形、海の深さ、メートル・フィート表示の等高線、地図上の任意の地点の標高 _(Viktor Govako, Alexander Borsuk)_
- 2026年11月10日時点のOpenStreetMapデータ
- 2026年11月1日時点のWikipedia記事
- 水域の色を改善し、川を太く表示。水域ラベルに控えめな縁取りを追加 _(David Martinez, Viktor Govako)_
- 季節的な河川、運河、排水路などの水路の表示を改善 _(Alexander Borsuk)_
- 路面電車、モノレール、ケーブルカー、狭軌鉄道の橋の輪郭を追加 _(Alexander Borsuk)_
- 理容店、ピラティススタジオ、窓の施工業者、水道施設、屋根付き貯水槽を追加 _(Viktor Govako)_
- 北極付近の水域の欠落など、塗りつぶし領域の隙間を修正 _(Viktor Govako)_
- 翻字を修正 _(Alexander Borsuk)_
- 性能を向上し、メモリ使用量を削減 _(Viktor Govako)_
- 地図スタイルの切り替え時のクラッシュと描画エラーを修正 _(Mikhail Listratsenka)_
- ダウンロード地域の境界を修正 _(Viktor Govako, Alexander Borsuk)_
- 検索候補で元の綴り、アクセント、大文字・小文字を保持 _(Alexander Borsuk)_
- 美容室や理容店の検索結果から無関係な美容サロンを除外 _(Viktor Govako)_

### ブックマーク、トラック、ポリゴン

- 新機能！色付きの輪郭、塗りつぶし、穴を持つKML・KMZ・GeoJSONポリゴンのインポートと表示 _(Alexander Borsuk, Viktor Govako)_
- トラックの方向矢印を追加 _(Alexander Borsuk)_
- 選択したトラックを強調表示 _(Alexander Borsuk)_
- リストからトラックを開くと始点を選択 _(Alexander Borsuk)_
- ブックマークとトラックの名前を言語に応じて正しく並べ替え _(Alexander Borsuk)_
- 再読み込み後にブックマークリストの名前、説明、画像を更新 _(Kiryl Kaveryn, Alexander Borsuk)_
- 保存したKMLルートで経由地と移動手段を保持。GPX・GeoJSONのエクスポートでは経由地をウェイポイントとして追加 _(Alexander Borsuk)_
- 編集したトラックの削除時や、開いたままの削除ダイアログに戻った際のクラッシュを修正 _(Viktor Govako)_
- クラッシュ後に復元できるよう、記録中のトラックを毎分保存 _(Viktor Govako)_
- 更新概要での地図の重複カウントと過大なダウンロードサイズを修正 _(Alexander Borsuk)_

### ルートとナビゲーション

- 新機能！車・自転車・徒歩で回避設定を個別に指定 _(Alexander Borsuk, Mikhail Listratsenka)_
- AndroidとiOSでルート地点のアイコンを接続し、「目的地を追加」のラベルを明確化 _(Kiryl Kaveryn, Mikhail Listratsenka)_
- ルートの計算に失敗しても目的地を追加可能に _(Kiryl Kaveryn)_
- ルート計算アルゴリズムを改善 _(Viktor Govako)_
- ルートの再計算を改善 _(Alexander Borsuk)_
- 地図と情報パネルでルートの所要時間が異なる問題を修正 _(Alexander Borsuk)_
- 古い速度取締カメラ警告と制限速度の更新遅延を修正 _(Alexander Borsuk)_
- 保存したルートの問題を修正 _(Alexander Borsuk)_
- ルートの復元を改善 _(Alexander Borsuk, Mikhail Listratsenka)_
- 公共交通の到着予測、徒歩での乗り継ぎ、駅入口のマーカーを改善 _(Alexander Borsuk)_

### OpenStreetMapエディター

- カテゴリー検索を改善 _(Alexander Borsuk)_
- 料理の種類の名前を言語に応じて正しく並べ替え _(Alexander Borsuk)_
- カテゴリーの並べ替えを修正 _(Alexander Borsuk)_

### 翻訳

- ウェールズ語を追加：アプリ画面、場所の種類、検索カテゴリー、ダウンロード地域名 _(Carl Morris, Alexander Borsuk)_
- システムの言語選択肢を追加：Android（アストゥリアス語、ガリシア語、クロアチア語、アルメニア語、アイスランド語、ラオ語、アルバニア語）とiOS（アストゥリアス語、カナダフランス語、ガリシア語、クロアチア語、アイスランド語） _(Alexander Borsuk)_
- スロベニア語の検索カテゴリーを修正 _(Alexander Borsuk)_
- ウクライナ語、チェコ語、スウェーデン語、韓国語の翻訳を改善。ほかの言語の表現やブランド名の綴りを修正 _(Nnifria, Alexander Borsuk, bilykralik16, Jonatan Nyberg, Dmitry Gribenchuk, M)_
- 距離と時間の単位、公共交通の乗り場ラベルを修正 _(Alexander Borsuk)_
- アラビア語とチェコ語の音声案内を改善。カタルーニャ語、デンマーク語、ガリシア語のナビゲーション距離を修正 _(Alexander Borsuk, Anquanna)_
- ノルウェー語ブークモールの地名と、編集した名前のアップロードを修正 _(Alexander Borsuk)_
- 「このアプリについて」のリンクから適切な言語のグループを表示 _(Alexander Borsuk)_

### iOS

- 新機能！すべての経由地を含むルートを反転するボタンを追加 _(Kiryl Kaveryn)_
- プランナーから始点や目的地を含む任意のルート地点を削除可能に _(Kiryl Kaveryn)_
- ナビゲーション音声の並べ替えを改善し、不足していた試聴用フレーズを追加 _(Alexander Borsuk, Kiryl Kaveryn)_
- ダークモードで定規の距離と押下中のルート地点ラベルの読みやすさを改善 _(Alexander Borsuk)_
- 公共交通プレビューを改善：記号の追加、路線色の明確化、路線番号の折り返し、右から左へのレイアウトの改善 _(Alexander Borsuk, Kiryl Kaveryn)_
- 右から左へのレイアウトでコンパスボタンを修正 _(Kiryl Kaveryn)_
- 場所の詳細が閉じても残る、ドラッグ中にずれる、別の地図リンクを開くと消える問題を修正 _(Kiryl Kaveryn)_
- 場所の詳細の読み込み完了前に地図のダウンロードで内容が更新される際のクラッシュを修正 _(Kiryl Kaveryn)_
- 場所の詳細でメインの操作を強調表示 _(Kiryl Kaveryn)_
- メニューと設定のリンクを修正。項目へのスクロールと強調表示も改善 _(Kiryl Kaveryn)_
- 初めてナビゲーションを開始する際、大きな文字で表示した確認ボタンを修正 _(Kiryl Kaveryn)_
- 経由地数の上限での地点の置き換えと、保存したトラックの置き換えラベルを修正 _(Kiryl Kaveryn)_
- 地図への復帰時、トラックの始点選択時、平坦な区間や拡大表示での標高グラフを修正 _(Kiryl Kaveryn)_
- CarPlayのブックマークリストが編集や再読み込み後に更新され、収まる項目をすべて表示し、削除した項目にも対応 _(Kiryl Kaveryn, Alexander Borsuk)_
- プレビューでルート設定のインジケーターが切れる問題を修正 _(Kiryl Kaveryn)_
- バックグラウンドを含め、ダウンロードのキャンセル、再試行、再開を改善 _(Viktor Govako)_

### Android

- 新機能！Android Autoを含め、速度と制限速度の表示を刷新 _(Andrei Shkrob)_
- 新機能！全画面の公共交通案内：乗車駅・停留所、乗り換え、出口、展開できる途中駅・停留所のリスト _(Paal Williams)_
- 新機能！トラック記録の開始、経過時間・距離・標高の表示ができるホーム画面ウィジェット _(Mikhail Listratsenka)_
- 新機能！すべての経由地を含むルートを反転するボタンを追加 _(Mikhail Listratsenka)_
- 新機能！平均海面（MSL）を基準とした標高の表示と記録 _(Alexander Borsuk)_
- トラックの記録開始時にバッテリー制限の確認を促す一度限りの通知を追加。システム設定へのショートカット付き。詳しくは<https://dontkillmyapp.com> _(Harsh Mishra, Alexander Borsuk)_
- プランナーから始点や目的地を含む任意のルート地点を削除可能に _(Mikhail Listratsenka)_
- 画面の問題を修正し、場所の詳細でルートのメイン操作を強調表示 _(Mikhail Listratsenka)_
- Android Autoのクラッシュを修正 _(Andrei Shkrob, Mikhail Listratsenka)_
- 「検索」をもう一度タップした場合やナビゲーションを停止した場合、カテゴリー検索の結果を消去 _(Mikhail Listratsenka)_
- 国フォルダーのアイコンから地域を表示。古い検索結果が開いたフォルダーを置き換える問題を修正 _(Mikhail Listratsenka)_
- プライバシー設定に「ブックマークとトラックのバックアップ」を追加し、Androidのバックアップ設定を開けるように _(Mikhail Listratsenka)_
- ライト・ダークテーマでブックマークとトラックの説明の読みやすさを改善 _(Mikhail Listratsenka)_
- 24時間にわたる営業時間の編集を修正 _(Alexander Borsuk)_
- 夏時間の切り替えをまたぐ場合の到着時刻を修正 _(Alexander Borsuk)_
- エディターの通りやセルフサービスの項目を2回タップした際のクラッシュを修正 _(Kevin Coughlin)_
- ほかのアプリから共有された、見つからない、または未対応のブックマークファイルによるクラッシュや不完全なインポートを修正 _(Darafei Praliaskouski)_
- グラフィックスコンテキストの変化に伴うVulkanの描画エラーとクラッシュを修正 _(Alexander Borsuk)_

### デスクトップ

- 画面と場所の種類を翻訳。代替言語と右から左へのレイアウトを改善 _(Alexander Borsuk)_
- 場所の詳細で非ラテン文字を含むリンクや説明のプレビューを修正 _(Alexander Borsuk)_
- OpenStreetMapエディターで料理の種類の保存と場所の削除を修正 _(Alexander Borsuk)_
- 検索中に地図ダウンロード画面を閉じた際のクラッシュを修正 _(Alexander Borsuk)_
- ウィンドウのサイズ変更時の地図描画を修正 _(Alexander Borsuk)_
- 位置情報の更新を改善し、位置情報エラー後の「現在地」ボタンを修正 _(Alexander Borsuk, Vladislav Shadiuk)_

<https://beta.omaps.app>で新機能を試して、テストに協力してみてください。

Organic Mapsの利用と支援に感謝します！

Organic Mapsチームより

{{ <references lang /> }}
