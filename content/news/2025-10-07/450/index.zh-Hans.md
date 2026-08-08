---
title: "10月7日发布：Android Auto 限速显示、GeoJSON 导入、轨迹录制统计、OSM description 标签显示、在 iOS 上为选中的轨迹保存书签等"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["releases"]
---

这次 10 月 7 日的 Organic Maps 更新新增了 Android Auto 中的限速显示、GeoJSON 导入、轨迹录制统计，可显示 OSM description 标签（在搜索框中输入 `?description` 即可查看），并支持在 iOS 上为轨迹保存书签。此外，所有平台都带来了大量用户界面和 OpenStreetMap 编辑方面的改进以及各种错误修复，包括修复了部分 Android 设备上的启动崩溃问题。

Organic Maps 得以存在，要感谢 ❤️ 我们的贡献者、[你的捐赠](@/donate/index.zh-Hans.md)和[你的支持](@/contribute/index.zh-Hans.md)。

### 详细更新日志（包含上一个小版本更新的变更）

- 新增！导入 GeoJSON (Sergiy Kozyr)
- 截至 10 月 4 日的 OpenStreetMap 数据
- 截至 10 月 1 日的 Wikipedia 数据
- 公共交通支持西雅图轻轨 (tjasz)
- 保存已编辑的 OSM 地点时不再取消地图上的选中状态 (Kiryl Kaveryn)
- 更新翻译 (Weblate 贡献者)

#### 地图样式

- 显示标记为 amenity=bicycle + rental=shop 的自行车租赁店 (David Martinez)
- 在 Outdoor 样式中从缩放级别 12 起显示考古遗址，从缩放级别 15 起显示其他历史遗迹 (Viktor Govako)
- Outdoors 样式中桅杆、通信塔和电力塔的新图标 (David Martinez)
- 增大 Outdoors 样式中山峰图标的尺寸 (David Martinez)
- 补充缺失的 POI 图标变体 (David Martinez)
- 添加了更多障碍物类型 (Viktor Govako)

#### iOS

- 新增：在选中的轨迹点上保存书签 (Kiryl Kaveryn)
- 新增：无需先保存即可删除正在录制的轨迹 (Kiryl Kaveryn)
- 在地点页面中以多行显示书签列表标题 (David Martinez)
- 更新 OSM 登录按钮样式 (Kiryl Kaveryn)
- 修复导航信息更新问题 (Kiryl Kaveryn)
- 修复新版路线规划的问题 (Kiryl Kaveryn)
- 修复地图超过 3 个月时 OSM 添加/编辑地点入口的可见性 (Kiryl Kaveryn)
- 修复 iOS 26 上出行方式分段控件的布局 (Kiryl Kaveryn)
- 简化书签选择动画 (Kiryl Kaveryn)
- 修复搜索结果选择问题 (Kiryl Kaveryn)
- 修复了地点信息页面的样式、滑动和动画 (Kiryl Kaveryn)

#### Android Auto（仅限 Google Play）

- 新增：Android Auto 中的限速显示 (Andrei Shkrob)
- 修复 Android Auto 导航模式下的显示切换 (Andrei Shkrob)
- 修复 Android Auto 中路线箭头的偏移 (Andrei Shkrob)
- 修复设备与汽车连接/断开时的问题 (Andrei Shkrob)
- 新增 Android Auto 定位服务 (Andrei Shkrob)
- 改进 Android Auto 路线模拟器 (Viktor Govako)

#### Android

- 新增：实时查看轨迹录制统计 (Kavi Khalique)
- 新增：显示 OSM `description` 标签内容 (Alexander Borsuk)
- 修复主题切换的处理 (Andrei Shkrob)
- 修复了多个崩溃问题，包括启动时的崩溃 (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- 下载进度通知改为静默 (Viktor Govako)
- 减小铅笔图标的内边距 (Alexander Borsuk)

#### 桌面版

- 修复 Linux 上 curl 卡死的问题 (Alexander Borsuk)
- 修复 macOS 上登录 OSM 时卡死的问题 (Alexander Borsuk)
- 可从右键菜单中选择地图要素 (Viktor Govako)
- 新增取消下载的选项 (Viktor Govako)
- 在右键菜单中显示几何类型 (Viktor Govako)

### 你可能错过的近期功能

- 选择公交站时显示公共交通线路号
- 徒步与骑行路线（通过左上角的“图层”按钮开启）
- 在应用设置中开启后，即可在地图上查看书签名称
- ✎ 铅笔图标可快速编辑书签

### 安装 Organic Maps

从 [App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium]、[Accrescent][accrescent] 和 [F-Droid][fdroid] 获取最新版 Organic Maps。

加入测试版，抢先体验新功能：[iOS][testflight] / [Android][firebase]。

{{ references() }}
