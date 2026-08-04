---
title: "2026年7月更新中针对公共交通、路线规划、搜索和书签的错误修复与改进"
date: 2026-07-23
slug: "cuowu-xiufu-gaijin-gonggong-jiaotong-luxian-guihua-sousuo-shuqian-2026-qiyue"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "news/2026-07-23/620/Barriers on a route.jpg"
---

你可能已经注意到，7 月份的 Organic Maps 更新现已发布。你可以通过 <https://get.omaps.org> 或在 [App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium]、[Accrescent][accrescent] 以及 [F-Droid][fdroid] 下载。

得益于你的[捐款](@/donate/index.zh-Hans.md)和[反馈](@/contribute/index.zh-Hans.md)，我们在 7 月主要专注于错误修复和功能改进。如果你之前错过了，[上一个 6 月版本](@/news/2026-06-29/610/index.zh-Hans.md)中推出的以下功能现已可用：
- 公共交通线路（实时时刻表正在开发中）
- 卫星图像
- 驾车、徒步和骑行的替代路线
- Android 的新搜索和路线规划界面
- iOS 对大号无障碍字体的支持

## 详细更新日志

### 地图与地点
- OpenStreetMap 数据更新至 7 月 14 日
- 报告至 [OpenStreetMap](https://www.openstreetmap.org) 的备注现已放置在你选定的精确位置，而非整条街道或区域的中间 _(Alexander Borsuk)_
- 在跨越 180° 对经线的区域点击地图时，地点选择已得到改进 _(Viktor Govako)_
- 删除轨迹后，轨迹海拔剖面图将不再显示过时或空白的图表 _(Kiryl Kaveryn)_

### 公共交通
- 停靠站、换乘站和车站名称现在带有白色轮廓，以便在浅色和深色主题下均能清晰显示 _(Viktor Govako)_
- 关闭公共交通路线预览后，地铁图层会正确重新显示 _(Mikhail Listratsenka)_

### 路线规划与导航
- 现在，所有替代路线都会显示路线提示（如收费路段、渡轮、未铺装道路、台阶等） _(Viktor Govako)_
- 修复了在构建路线时罕见的卡死问题 _(Viktor Govako)_
- 改进了在限制通行道路上对死胡同以及起点和终点的处理方式 _(Viktor Govako)_
- 修复了错误和缺失的转弯说明 _(Alexander Borsuk)_

### iOS
- 新增“保存搜索记录”设置，如果你不希望保留搜索记录，可以关闭该功能并将其隐藏 _(Kiryl Kaveryn)_
- 新增“编辑”按钮，可更轻松地删除书签 _(Kiryl Kaveryn)_
- 现在，当你离开屏幕时，书签会自动保存 _(Kiryl Kaveryn)_
- 颜色面板现在提供了预设颜色，并允许你选择任何自定义颜色 _(Kiryl Kaveryn)_
- 改进了已记录轨迹的高程图空状态 _(Kiryl Kaveryn)_
- 改进了“开始”按钮上显示的路线进度 _(Kiryl Kaveryn)_
- 重新排序路线停靠点后，列表不再出现跳动现象 _(Kiryl Kaveryn)_
- 其他一些较小的界面改进 _(Kiryl Kaveryn)_

### Android
- 营业时间现在会显示分段班次（例如午休时间），从今天开始排列，并以整周形式展示，无需单独的滚动区域 _(Owm Dubey, Alexander Borsuk, Mikhail Listratsenka)_
- 更简洁的搜索栏，集成了“清除”和“语音”按钮；“清除”图标不再移动；横屏模式下以及旋转手机后的布局已得到修复 _(Mikhail Listratsenka)_
- 重新设计的书签和轨迹编辑器 _(Mikhail Listratsenka)_
- 路线规划的修复和改进 _(Mikhail Listratsenka)_
- 颜色选择器现在会自动关闭，并且修复了在 Android 5 上出现的崩溃问题 _(Mikhail Listratsenka)_
- 修复了崩溃问题 _(Alexander Borsuk, Mikhail Listratsenka)_

### 桌面
- 可供下载的地图列表现已按字母顺序排序 _(goncalo109560)_

### 翻译
- 改进了中文表述 _(Chenxi Zhao)_
- 更新了乌克兰语翻译 _(Nnifria)_
- 修复了地图区域名称的意大利语翻译 _(Vittorio Bertola)_

## 加入 Beta 测试，抢先体验早期功能并报告问题：

提示：该测试版采用了新的山体阴影渲染效果，改进了高程数据（支持英尺和米两种单位），还新增了其他酷炫功能！

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

祝大家夏天快乐！
Organic Maps 团队

{{ references() }}
