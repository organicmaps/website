---
title: "2026 年 9 月更新：路线优化、替代路线改进、单条轨迹隐藏和间歇性水域"
date: 2026-09-29
slug: "shuqian-guiji-duoxuan-carplay-yibiaopan-yincang-guiji-fenxiang-lianjie-2026-bayue"
taxonomies:
  news: ["releases"]
extra:
  preview_image: 00-intermittent-water.png
---

准备好出发了吗？9 月更新带来了更好的替代路线、优化路线途经点顺序的设置、更清晰的间歇性水域标记，以及用于隐藏单条轨迹的眼睛图标，还有许多其他修复和改进（详见下文）。

通过 <https://get.omaps.org>、[App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium]、[Accrescent][accrescent] 或 [F-Droid][fdroid] 安装或更新 Organic Maps。

如果你错过了之前的更新，可以看看 [6 月](@/news/2026-06-29/610/index.zh-Hans.md)、[7 月](@/news/2026-07-23/620/index.zh-Hans.md)和 [8 月](@/news/2026-08-31/630/index.zh-Hans.md)发布的新功能。感谢让这些更新成为可能的贡献者和用户！

## 如何支持 Organic Maps

- [捐款](@/donate/index.zh-Hans.md)以支持开发工作并支付地图托管费用
- [发送反馈并贡献力量](@/contribute/index.zh-Hans.md)，一起参与这个项目
- 加入 Beta 测试，抢先体验新功能，并在 [iOS][testflight]、[Android][firebase] 和[桌面端][flathub]反馈问题
- 帮忙把消息分享给更多人，一起打造比科技巨头的地图更好的替代方案！

## 版本说明

### 地图

- OpenStreetMap 数据更新至 2026 年 9 月 28 日
- 维基百科数据更新至 2026 年 9 月 21 日
- 修复了可见地图区域跨越 180° 经线（±180° 经度）时的搜索问题 _(Viktor Govako)_
- 间歇性水域现在以点状图案显示，与地图上沙地所用的图案类似 _(Alexander Borsuk)_
- 现在进一步缩小地图时也能看到水库 _(Alexander Borsuk)_
- 地图上不再显示水隧道 _(Alexander Borsuk)_
- 修复了苏州地铁站和入口图标 _(Alexander Borsuk)_
- 修复了地铁地图图层中标签位置偏移的极少数情况 _(Viktor Govako)_

### 路线规划与导航

- 改进了替代路线及其预计到达时间 _(Alexander Borsuk, Viktor Govako)_
- 现在，当导航重新计算路线时，所选的替代路线会被保留 _(Alexander Borsuk)_
- 重新启动应用后，现在会恢复路线途经点的顺序 _(Kiryl Kaveryn)_

### 其他改进

- 营业时间现在将 12:00 显示为“中午”，将 00:00 或 24:00 显示为“午夜” _(Alexander Borsuk)_
- 修复了错误并改进了轨迹录制功能 _(Alexander Borsuk)_
- 修复了 KMB 文件导入问题 _(Alexander Borsuk)_
- 修正了法语和阿斯图里亚斯语翻译 _(Alexander Borsuk)_
- 修正了一处英文拼写错误 _(Carl Morris)_

### iOS

- 添加了用于隐藏单条轨迹的眼睛图标 _(Kiryl Kaveryn)_
- 添加了用于在计划路线中添加或替换途经点的按钮 _(Kiryl Kaveryn)_
- 新增了优化路线中间途经点顺序的设置 _(Kiryl Kaveryn)_
- 在受支持的车载平视显示器（HUD）和 CarPlay 仪表盘中添加了转弯等导航指引 _(Kiryl Kaveryn)_
- 修复了 CarPlay 按钮和搜索功能 _(Alexander Borsuk)_
- 修复了各种错误，并改进了用户界面 _(Kiryl Kaveryn, Alexander Borsuk)_
- 新增了选择和试听已安装导航语音的功能 _(Kiryl Kaveryn, Alexander Borsuk)_
- 恢复了 Spotlight 中的分类搜索功能 _(Kiryl Kaveryn)_

### Android

- 新增了优化路线中间途经点顺序的设置 _(Mikhail Listratsenka)_
- 添加了用于在计划路线中添加或替换途经点的按钮 _(Mikhail Listratsenka)_
- 新增了通过通知停止轨迹录制并保存轨迹的功能 _(Alexander Borsuk)_
- “添加途经点”按钮现在会在现有途经点之后、目的地之前添加一个途经点 _(Mikhail Listratsenka)_
- 改进 OpenStreetMap 编辑器的上传功能 _(Owm)_
- 更新了用户界面设计 _(Mikhail Listratsenka)_
- 书签编辑器和其他对话框现在在导航过程中会保持打开状态 _(Mikhail Listratsenka)_
- 修复了平坦轨迹及从右到左布局的界面中海拔图的渲染问题 _(Mikhail Listratsenka)_
- 修复了地图按钮被系统栏裁切的问题 _(Mikhail Listratsenka)_
- 修复了错误，并改进了对 Android Auto 的支持 _(Andrei Shkrob)_
- 修复了地图渲染过程中发生的崩溃问题 _(Viktor Govako)_

### 桌面

- 将桌面可执行文件和 macOS 应用程序包重命名为 `OrganicMaps` _(Alexander Borsuk)_
- 修复了 Windows 应用中的问题 _(Osyotr, Alexander Borsuk)_
- `--lang` 命令行参数现可覆盖应用的语言设置 _(Alexander Borsuk)_

怀着喜悦与热情，

你的 Organic Maps 团队

{{ <references lang /> }}
