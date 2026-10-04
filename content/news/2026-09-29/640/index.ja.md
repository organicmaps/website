---
title: "2026年9月のアップデート：ルートの最適化、代替ルートの改善、個々のトラックの非表示、一時的に水がある水域の表示"
date: 2026-09-29
slug: "ruto-saitekika-daitai-ruto-kaizen-koko-no-torakku-hihyoji-ichijiteki-ni-mizu-ga-aru-suiiki-2026-kugatsu"
aliases: ["/ja/news/2026-09-29/bukkumaku-torakku-fukusu-sentaku-carplay-dasshubodo-torakku-hihyoji-kyoyu-rinku-2026-hachigatsu/"]
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

出かける準備はできた？9月のアップデートでは、代替ルートの改善、経由地を訪れる順序を最適化する設定、一時的に水がある水域のわかりやすい表示、個々のトラックを非表示にする目のアイコンに加え、多くの修正や改善が行われた（詳しくは以下をチェック）。

<https://get.omaps.org>、[App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium]、[Accrescent][accrescent]、または[F-Droid][fdroid]から、Organic Mapsをインストールまたはアップデートしよう。

前のアップデートを見逃していたら、[6月](@/news/2026-06-29/610/index.md)、[7月](@/news/2026-07-23/620/index.md)、[8月](@/news/2026-08-31/630/index.ja.md)にリリースされた新機能もチェックしよう。これらのアップデートを実現してくれた貢献者やユーザーのみんなに感謝！

## Organic Maps を支援する方法

- 開発を支え、地図のホスティング費用を賄うために[寄付しよう](@/donate/index.ja.md)
- [フィードバックを送り、プロジェクトに貢献しよう](@/contribute/index.ja.md)
- ベータテストに参加して、新機能をいち早く試したり、[iOS][testflight]、[Android][firebase]、[デスクトップ][flathub]版での不具合を報告したりしよう
- この情報を広めて、ビッグテックの地図に代わる、より良い選択肢を一緒に作り上げよう！

## リリースノート

### 地図

- 2026年9月28日時点のOpenStreetMapデータ
- 2026年9月21日時点のウィキペディアのデータ
- 表示されている地図領域が180°子午線（経度±180°）をまたぐ場合の検索を修正した _(Viktor Govako)_
- 一時的に水がある水域を、地図上の砂地に使う模様に似た点描模様で表示するようになった _(Alexander Borsuk)_
- さらにズームアウトしても貯水池が表示されるようになった _(Alexander Borsuk)_
- 水路トンネルを地図に表示しなくなった _(Alexander Borsuk)_
- 蘇州地下鉄の駅と入口のアイコンを修正した _(Alexander Borsuk)_
- 地下鉄レイヤー上でラベルの位置がずれてしまうという、ごくまれに発生していた不具合を修正した _(Viktor Govako)_

### 経路設定とナビゲーション

- 代替ルートとその推定到着時刻を改善した _(Alexander Borsuk, Viktor Govako)_
- ナビゲーションがルートを再計算する際、選択された代替ルートが保持されるようになった _(Alexander Borsuk)_
- アプリを再起動した後に経由地の順序が復元されるようになった _(Kiryl Kaveryn)_

### その他の改善点

- 営業時間の表示で、12:00は「正午」、00:00または24:00は「午前0時」と表示されるようになった _(Alexander Borsuk)_
- バグを修正し、トラックの記録機能を改善した _(Alexander Borsuk)_
- KMBファイルのインポートに関する問題を修正した _(Alexander Borsuk)_
- フランス語とアストゥリアス語の翻訳を修正した _(Alexander Borsuk)_
- 英語の誤字を修正した _(Carl Morris)_

### iOS

- 個々のトラックを非表示にするための目のアイコンを追加した _(Kiryl Kaveryn)_
- 計画したルートに経由地を追加または置き換えるためのボタンを追加した _(Kiryl Kaveryn)_
- 経由地を訪れる順序を最適化する設定を追加した _(Kiryl Kaveryn)_
- 対応する車載ヘッドアップディスプレイ（HUD）とCarPlayダッシュボードに、右左折などのナビゲーション案内を追加した _(Kiryl Kaveryn)_
- CarPlayのボタンと検索機能を修正した _(Alexander Borsuk)_
- さまざまなバグを修正し、ユーザーインターフェースを改善した _(Kiryl Kaveryn, Alexander Borsuk)_
- インストール済みのナビゲーション音声を選び、サンプルを試聴できる機能を追加した _(Kiryl Kaveryn, Alexander Borsuk)_
- Spotlightのカテゴリ検索機能を復元した _(Kiryl Kaveryn)_

### Android

- 経由地を訪れる順序を最適化する設定を追加した _(Mikhail Listratsenka)_
- 計画したルートに経由地を追加または置き換えるためのボタンを追加した _(Mikhail Listratsenka)_
- 通知からトラックの記録を停止し、トラックを保存できる機能を追加した _(Alexander Borsuk)_
- 「経由地を追加」ボタンで、既存の経由地の後、目的地の前に経由地を追加するようになった _(Mikhail Listratsenka)_
- OpenStreetMapエディタからのアップロード機能が改善された _(Owm)_
- ユーザーインターフェースのデザインを更新した _(Mikhail Listratsenka)_
- ブックマークエディタやその他のダイアログが、ナビゲーション中も開いたままになるようになった _(Mikhail Listratsenka)_
- 高低差のないトラックと、右から左へ表示するインターフェースでの標高グラフの描画を修正した _(Mikhail Listratsenka)_
- マップボタンがシステムバーに隠れる問題を修正した _(Mikhail Listratsenka)_
- バグを修正し、Android Autoの対応を改善した _(Andrei Shkrob)_
- マップのレンダリング中に発生していたクラッシュを修正した _(Viktor Govako)_

### デスクトップ

- デスクトップ用実行ファイルとmacOSアプリバンドルの名前を`OrganicMaps`に変更した _(Alexander Borsuk)_
- Windowsアプリの不具合を修正した _(Osyotr, Alexander Borsuk)_
- `--lang`というコマンドライン引数が、アプリの言語設定を上書きするようになった _(Alexander Borsuk)_

喜びと情熱を込めて、

Organic Mapsチームより

{{ <references lang /> }}
