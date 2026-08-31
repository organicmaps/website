---
title: "2026年8月のアップデートで、ブックマークとトラックの複数選択、CarPlay ダッシュボード、地図上でのトラックの非表示、読みやすい共有リンクが追加されました"
date: 2026-08-31
slug: "bukkumaku-torakku-fukusu-sentaku-carplay-dasshubodo-torakku-hihyoji-kyoyu-rinku-2026-hachigatsu"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 02-bookmarks-tracks-multi-selection.jpg
---

2026年8月版の Organic Maps は、<https://get.omaps.org> または [App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium] から入手できます（[Accrescent][accrescent] と [F-Droid][fdroid] でも近日中に配信予定です）。

アップデートする理由は？
- 「ブックマークとトラック」での複数選択と、まとめて削除・移動・色変更する操作
- CarPlay のダッシュボード
- 地図上で個々のトラックを非表示にする機能
- 場所、ブックマーク、現在地の読みやすい共有リンク——さらに iOS の AirDrop と、デスクトップの「Share」操作
- アルメニア語とラオス語の音声案内
- 19言語のウィキペディア記事
…そのほかにも、以下のとおり多くの改善、バグ修正、地図データの更新があります。

以前の[6月版](@/news/2026-06-29/610/index.md)と[7月のアップデート](@/news/2026-07-23/620/index.md)のリリースノートもぜひご覧ください。

## 変更履歴（全文）

### 地図と場所

- 2026年8月26日時点の OpenStreetMap データに更新しました _(Viktor Govako)_
- アラビア語、ベンガル語、中国語、英語、フランス語、ドイツ語、ヒンディー語、イタリア語、日本語、韓国語、マラーティー語、ポーランド語、ポルトガル語、ロシア語、スペイン語、タミル語、テルグ語、トルコ語、ウルドゥー語のウィキペディア記事を更新しました _(Alexander Borsuk)_
- 営業時間が正しく表示されない原因となっていた多くの問題を修正しました _(Alexander Borsuk)_
- 野鳥観察小屋（バードハイド）に対応しました _(Batmaclos, Viktor Govako)_
- 地図に舞台、丘、天然アーチを追加し、岩の新しいアイコンも用意しました _(David Martinez)_
- 山頂、洞窟、峠のアイコンのサイズを調整しました _(David Martinez)_
- 保護区、国立公園、湿地は、より薄い色合いで表示されるようになりました _(Alexander Borsuk)_
- アプリのフリーズと、タップやジェスチャーがときどき無視される問題を修正しました _(Alexander Borsuk)_

### 共有、ブックマーク、トラック

- 場所、ブックマーク、現在地を共有すると、役に立つ情報が入った読みやすいリンクが送られるようになりました _(Alexander Borsuk)_
- エクスポートしたブックマークは、元の名前と説明が保持されるようになりました _(Alexander Borsuk)_
- 共有したブックマークリストは、内部のファイル名ではなく表示名が使われるようになりました _(Alexander Borsuk)_
- トラックの記録を開始した直後に起きることがあった標高グラフの表示不具合を修正しました _(Kiryl Kaveryn)_

### ルート検索とナビゲーション

- ルート上の経由地やマーカーをタップすると、計画済みのルートが切り替わるのではなく、その地点が正しく開くようになりました _(Viktor Govako)_
- 公共交通機関のルート検索が速くなりました _(Viktor Govako)_
- 誤ったターン案内を修正しました _(Alexander Borsuk)_
- ルートを再作成した後に出発地点が正しくならない問題を修正しました _(Viktor Govako)_
- ラテライト道路は、ルート検索で質の低い未舗装路面として扱われるようになりました _(Julien Etienne)_
- `access=unknown` のタグが付いた道路は、私道や目的地のみアクセスできる道路と同じように扱われるようになりました _(Julien Etienne)_
- アルメニア語とラオス語の音声案内を追加しました _(Alexander Borsuk)_

### OpenStreetMap エディタ

- 営業時間の欄を空にしても、「保存」や「完了」ボタンが無効なままになることはなくなりました _(Alexander Borsuk)_
- 一部だけ失敗したアップロードは、完全に成功したと報告されるのではなく、再試行されるようになりました _(Alexander Borsuk)_

### 翻訳

- 日本語訳を含め、[よくある質問](https://organicmaps.app/ja/faq/)を更新しました _(Alexander Borsuk)_
- 「Closed now」の日本語訳を修正しました _(Viktor Govako)_
- 「track」と「disable」の中国語訳を改善しました _(Chenxi Zhao)_

### iOS

- 新機能：「ブックマークとトラック」のリストに複数選択を追加しました。選んだ項目をまとめて削除・移動・色変更できるほか、「すべて選択」と「選択を解除」も使えます _(Kiryl Kaveryn)_
- 新機能：CarPlay のダッシュボードを追加しました _(Kiryl Kaveryn)_
- 場所の共有に AirDrop 対応を追加しました _(Kiryl Kaveryn)_
- CarPlay の複数の不具合を修正しました _(Kiryl Kaveryn, Alexander Borsuk)_
- 地図上でブックマークを選んだときの HTML 説明文の表示を修正しました _(Kiryl Kaveryn)_
- カーナビ用の地図スタイルが有効にならない問題を修正しました _(Kiryl Kaveryn, Alexander Borsuk)_
- 設定を「一般設定」「地図」「ナビゲーション」「ネットワーク」「プライバシー」のセクションに整理し直しました _(Kiryl Kaveryn)_
- キャリブレーションが自動で行われるようになったため、コンパスのキャリブレーション設定を削除しました _(Kiryl Kaveryn)_
- カラーパレットのポップオーバーにカスタムカラーピッカーを復活させました _(Kiryl Kaveryn)_
- 徒歩や自転車のルートプレビューで標高プロファイルをドラッグすると、対応する地点が地図上に表示されるようになりました _(Kiryl Kaveryn)_
- 現在地の矢印が誤った方向を指したり固まったりすることがあったコンパスの不具合を修正しました _(Alexander Borsuk)_
- バックグラウンドで OpenStreetMap へのアップロードが完了したときに起きていたクラッシュを修正しました _(Alexander Borsuk)_

### Android

- 新機能：「ブックマークとトラック」のリストに複数選択モードを追加しました。項目を長押しするか、ツールバーから切り替えると、ブックマークとトラックを自由に組み合わせて色の変更、移動、削除ができます _(Mikhail Listratsenka)_
- 新機能：リストやトラックの詳細画面にある目のアイコンで、個々のトラックを地図から非表示にできるようになりました _(cyber-toad)_
- Android Auto と Android Automotive：Uターン車線の矢印を修正しました _(Andrei Shkrob, Viktor Govako)_
- Android Auto と Android Automotive：昼夜モードの切り替えを修正しました _(Andrei Shkrob)_
- Android Auto と Android Automotive：入力中も検索リストが開いたままになるようになりました _(Viktor Govako)_
- リストを並べ替えると、リストの説明が表示されるようになりました _(Mikhail Listratsenka)_
- ブックマークリストの設定画面のデザインを刷新しました _(Mikhail Listratsenka)_
- カテゴリをタップすると、検索パネルが折りたたまれるようになりました _(Mikhail Listratsenka)_
- 検索欄の内容を消すと、キーボードのフォーカスが検索欄に戻るようになりました _(Mikhail Listratsenka)_
- ルートの標高グラフが、パネルの幅いっぱいに表示されるようになりました _(Mikhail Listratsenka)_
- ズームボタンが画面上部に張り付いたままになることがある問題を修正しました _(Mikhail Listratsenka)_
- すべての Android バージョンで、ダイアログの角が同じように丸く表示されるようになりました _(Mikhail Listratsenka)_
- トラックのエクスポートメニューで起きていたクラッシュを修正しました _(Mikhail Listratsenka)_
- アプリのフリーズを修正しました _(Alexander Borsuk, Viktor Govako)_
- KML ファイルと KMZ ファイルが重複してインポートされる問題と、「ファイルを開けませんでした」というエラーを修正しました _(Alexander Borsuk)_
- ブラジルポルトガル語、メキシコスペイン語、イギリス英語の検索カテゴリを修正しました _(Alexander Borsuk)_
- キーボードの言語がインターフェースの言語と異なる場合でも、検索がキーボードの言語で正しく動作するようになりました _(Alexander Borsuk)_
- アップロードに時間がかかりすぎたり、一部だけ失敗したりしても、OpenStreetMap の編集内容が失われなくなりました _(Alexander Borsuk)_

### デスクトップ

- 場所のページに「Share」を追加し、「Copy Link」「Copy Text」「Email…」を選べるようにしました _(Alexander Borsuk)_
- ダウンロードのスピナーをプログラムで描画するようにしたため、どのディスプレイでも鮮明に表示されます _(Kuzey Bilgin)_

## Organic Maps を支援するには

- 開発を支援し、地図のホスティング費用をまかなうために[寄付をお願いします](@/donate/index.ja.md)
- プロジェクトへ[フィードバックを送り、貢献してください](@/contribute/index.ja.md)
- ベータテストに参加して、[iOS][testflight]、[Android][firebase]、[デスクトップ][flathub]の新機能をいち早く試し、不具合を報告してください
- ぜひ Organic Maps を広めてください！

すべてのユーザーと貢献者の皆さまへ、愛と感謝を込めて、<br/>
Organic Maps チーム

{{ <references lang /> }}
