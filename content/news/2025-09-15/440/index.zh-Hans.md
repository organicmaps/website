---
title: "9月15日发布：全新路线规划与 OSM 描述"
date: 2025-09-15T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

本月第二次九月更新带来重新设计的路线规划界面，并在 iOS 上支持查看 OpenStreetMap 的 `description` 标签内容。要查找带有该标签的地点，在搜索框输入 `?description`（类似输入 `?wiki`）。

同时还包含大量 iOS 与 Android 的修复和改进（见下文）。

你可能错过的近期功能：
- 选择公交站时显示公共交通线路号
- 徒步与骑行路线（通过左上方“图层”按钮开启）
- 在地图上显示书签名称（在设置中开启）
- ✎ 图标可快速编辑书签

Organic Maps 得益于贡献者、[你的捐赠](@/donate/index.zh-Hans.md) 与 [你的支持](@/contribute/index.md)。

### 详细更新日志

- 截至 9 月 13 日的最新 OpenStreetMap 数据
- 移除世界地图上的极小岛屿 (Viktor Govako)
- 在地址详情显示邮政编码 (ZIP) (Viktor Govako)
- 修复定位到当前位置时的地图居中错误 (Kiryl Kaveryn, Viktor Govako)
- 导出/导入 GPX 时保留书签颜色 (cyber-toad)
- 更新翻译 (Weblate 贡献者)

#### 地图样式 (Viktor Govako)

- 显示照明商店
- 从缩放 18 起显示电力线路
- 显示电站与变电站参考名称
- 导航模式下显示露营地与房车营地
- 修复导航模式下次级公路颜色
- 绘制国家公园边界
- 在 Outdoor 样式中自缩放 12 起绘制考古遗址

#### iOS

- 新增：显示 OSM `description` 标签内容（搜索 `?description`）(Kiryl Kaveryn, Viktor Govako)
- 新增：重设计路线规划界面 (Kiryl Kaveryn)

#### Android

- Android Auto 新的环岛图标 (Andrei Shkrob)
- 显示所选书签类别 (Alexander Borsuk)
- 修复显示到书签距离的延迟 (Alexander Borsuk)
- 重构深色主题 (Andrei Shkrob)
- 修复在定制 ROM（如 Lineage + MicroG）导航中的位置更新问题 (Viktor Govako)
- 书签使用蓝色铅笔（编辑）图标 (Alexander Borsuk)
- 减少地点信息预览垂直高度 (Alexander Borsuk)
- 从预览移除指向北方的方位角（点蓝色箭头查看） (Alexander Borsuk)

获取最新版本： [App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium]、[Accrescent][accrescent]、[F-Droid][fdroid]。

加入测试版： [iOS][testflight] / [Android][firebase]。

{{ references() }}
