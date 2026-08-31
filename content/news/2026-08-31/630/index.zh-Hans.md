---
title: "2026年8月更新带来书签和轨迹多选、CarPlay 仪表盘、在地图上隐藏轨迹以及可读的分享链接"
date: 2026-08-31
slug: "shuqian-guiji-duoxuan-carplay-yibiaopan-yincang-guiji-fenxiang-lianjie-2026-bayue"
taxonomies:
  news: ["releases"]
extra:
  preview_image: "02 Bookmarks and tracks multi-selection move, change color, delete.jpg"
---

你可以通过 <https://get.omaps.org> 或在 [App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium] 下载 2026 年 8 月版的 Organic Maps（[Accrescent][accrescent] 和 [F-Droid][fdroid] 版本也即将上线）。

为什么要更新？
- 在“书签”和“轨迹”中支持多选，可批量删除、移动和更改颜色
- CarPlay 仪表盘
- 在地图上隐藏单个轨迹
- 地点、书签和当前位置的可读分享链接——此外，iOS 支持 AirDrop，桌面版新增“Share”操作
- 亚美尼亚语和老挝语的语音导航
- 19 种语言的维基百科条目
……以及下面列出的许多其他改进、错误修复和更新的地图数据。

也别忘了查看此前的[六月版本](@/news/2026-06-29/610/index.zh-Hans.md)和[七月更新](@/news/2026-07-23/620/index.zh-Hans.md)说明。

## 完整更新日志

### 地图与地点

- 更新了截至 2026 年 8 月 26 日的 OpenStreetMap 数据 _(Viktor Govako)_
- 更新了阿拉伯语、孟加拉语、中文、英语、法语、德语、印地语、意大利语、日语、韩语、马拉地语、波兰语、葡萄牙语、俄语、西班牙语、泰米尔语、泰卢固语、土耳其语和乌尔都语的维基百科条目 _(Alexander Borsuk)_
- 修复了导致营业时间显示不正确的许多问题 _(Alexander Borsuk)_
- 新增了对观鸟屋的支持 _(Batmaclos, Viktor Govako)_
- 在地图上新增了舞台、山丘和天然拱门，并为岩石添加了新图标 _(David Martinez)_
- 调整了山峰、洞穴和山隘图标的尺寸 _(David Martinez)_
- 保护区、国家公园和湿地现在以更浅的色调显示 _(Alexander Borsuk)_
- 修复了应用卡死的问题，以及偶尔导致点击和手势被忽略的问题 _(Alexander Borsuk)_

### 分享、书签与轨迹

- 现在分享地点、书签或当前位置时，会发送一个包含实用信息的可读链接 _(Alexander Borsuk)_
- 导出的书签现在会保留其原始名称和描述 _(Alexander Borsuk)_
- 已分享的书签列表现在使用其显示名称，而不是内部文件名 _(Alexander Borsuk)_
- 修复了开始轨迹录制后可能立即出现的海拔图显示问题 _(Kiryl Kaveryn)_

### 路线规划与导航

- 现在点击路线中的停靠点或标记会正确地将其打开，而不是在已规划的路线之间切换 _(Viktor Govako)_
- 公共交通路线的规划速度现在更快了 _(Viktor Govako)_
- 修复了错误的转向提示 _(Alexander Borsuk)_
- 修复了路线重建后起点不正确的问题 _(Viktor Govako)_
- 在路线规划中，红土路现在被视为路面质量较差的未铺装道路 _(Julien Etienne)_
- 标记为 `access=unknown` 的道路现在会按照仅限私人通行或仅限目的地通行的道路来处理 _(Julien Etienne)_
- 新增了亚美尼亚语和老挝语的语音导航 _(Alexander Borsuk)_

### OpenStreetMap 编辑器

- 清空“营业时间”字段后，“保存”或“完成”按钮不再处于禁用状态 _(Alexander Borsuk)_
- 部分失败的上传现在会重试，而不再被报告为完全成功 _(Alexander Borsuk)_

### 翻译

- 更新了[常见问题解答](https://organicmaps.app/faq/)，其中包括日语翻译 _(Alexander Borsuk)_
- 更正了“现已关门”的日语翻译 _(Viktor Govako)_
- 改进了“轨迹”和“停用”的中文翻译 _(Chenxi Zhao)_

### iOS

- 新功能：在“书签”和“轨迹”列表中新增了多选，可对选中的项目批量删除、移动和更改颜色，并新增了“全选”和“取消全选” _(Kiryl Kaveryn)_
- 新功能：新增了 CarPlay 仪表盘 _(Kiryl Kaveryn)_
- 新增了通过 AirDrop 分享地点的功能 _(Kiryl Kaveryn)_
- 修复了多个 CarPlay 问题 _(Kiryl Kaveryn, Alexander Borsuk)_
- 修复了在地图上选中书签时 HTML 描述的显示问题 _(Kiryl Kaveryn)_
- 修复了车载导航地图样式无法启用的问题 _(Kiryl Kaveryn, Alexander Borsuk)_
- 将设置重新整理为“常规设置”、“地图”、“导航”、“网络”和“隐私”几个部分 _(Kiryl Kaveryn)_
- 移除了指南针校准设置，因为校准现在会自动完成 _(Kiryl Kaveryn)_
- 恢复了调色板弹出窗口中的自定义颜色选择器 _(Kiryl Kaveryn)_
- 现在，当你在步行或骑行路线预览中拖动海拔剖面图时，地图上会显示相应的点 _(Kiryl Kaveryn)_
- 修复了可能导致当前位置箭头指向错误方向或卡住的指南针问题 _(Alexander Borsuk)_
- 修复了在后台完成 OpenStreetMap 上传时发生的崩溃 _(Alexander Borsuk)_

### Android

- 新功能：在“书签”和“轨迹”列表中新增了多选模式。长按某一项或使用工具栏即可进入该模式，随后可对任意组合的书签和轨迹更改颜色、移动或删除 _(Mikhail Listratsenka)_
- 新功能：现在可以通过列表或轨迹详情页面中的眼睛图标，将单个轨迹从地图上隐藏 _(cyber-toad)_
- Android Auto 和 Android Automotive：修复了掉头车道的箭头 _(Andrei Shkrob, Viktor Govako)_
- Android Auto 和 Android Automotive：修复了日间/夜间模式的切换 _(Andrei Shkrob)_
- Android Auto 和 Android Automotive：现在输入时搜索列表会保持打开状态 _(Viktor Govako)_
- 对列表排序后，现在会显示列表描述 _(Mikhail Listratsenka)_
- 更新了书签列表设置界面的设计 _(Mikhail Listratsenka)_
- 现在点击某个类别后，搜索面板会折叠起来 _(Mikhail Listratsenka)_
- 清除搜索框内容后，键盘焦点现在会返回搜索框 _(Mikhail Listratsenka)_
- 路线海拔图现在会占满面板的整个宽度 _(Mikhail Listratsenka)_
- 修复了可能导致缩放按钮卡在顶部的问题 _(Mikhail Listratsenka)_
- 现在所有 Android 版本中的对话框圆角都保持一致 _(Mikhail Listratsenka)_
- 修复了轨迹导出菜单中的崩溃 _(Mikhail Listratsenka)_
- 修复了应用卡死的问题 _(Alexander Borsuk, Viktor Govako)_
- 修复了 KML 和 KMZ 文件重复导入的问题，以及“无法打开文件”的错误 _(Alexander Borsuk)_
- 修复了巴西葡萄牙语、墨西哥西班牙语和英式英语的搜索类别 _(Alexander Borsuk)_
- 当键盘语言与界面语言不同时，搜索现在能以键盘语言正常工作 _(Alexander Borsuk)_
- 当上传耗时过长或部分失败时，OpenStreetMap 的编辑内容将不再丢失 _(Alexander Borsuk)_

### 桌面

- 在地点页面中新增了“Share”操作，包含“Copy Link”、“Copy Text”和“Email…”选项 _(Alexander Borsuk)_
- 下载动画图标现在由程序绘制，因此在任何显示器上都保持清晰 _(Kuzey Bilgin)_

## 如何支持 Organic Maps

- [捐款](@/donate/index.zh-Hans.md)以支持开发工作并支付地图托管费用
- 向项目[提交你的反馈并贡献力量](@/contribute/index.zh-Hans.md)
- 加入 [iOS][testflight]、[Android][firebase] 和[桌面版][flathub] 的 Beta 测试，抢先体验新功能并反馈问题
- 把 Organic Maps 介绍给更多人！

谨向所有用户和贡献者致以爱与感激，<br/>
Organic Maps 团队

{{ <references lang /> }}
