---
title: "5 月 Organic Maps 更新：点击公共交通站点即可在地图上查看线路，书签标签不再重叠，越南、马来西亚和中国南部的下载区域更小"
date: 2026-05-08
slug: "dianji-gonggong-jiaotong-zhantai-shuqian-biaoqian-bu-chongdie-yuenan-malaixiya-zhongguo-quyu-chaifen"
taxonomies:
  news: ["releases"]
---

5 月的更新让 Organic Maps 朝着全面支持公共交通又迈进了一步。公交、火车、轮渡或有轨电车站点，是查看途经公共交通线路的入口——因此，现在在站点上点按某条路线，该路线就会以自己的颜色在整张地图上完整显示。实际运营时刻表也将在线提供；如果您还没有为所在地区添加或更新 [OSM 公共交通数据](https://gtfs-osm-matcher.organicmaps.app/)，请别忘了补充！

一如既往，衷心感谢我们的贡献者们，感谢您的好评、[捐赠](@/donate/index.zh-Hans.md)与[支持](@/contribute/index.zh-Hans.md)。

请通过 <https://get.omaps.org> 或 [App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium]、[Accrescent][accrescent] 以及 [F-Droid][fdroid] 获取 5 月更新。

## 亮点

- **点击地图上的公交、有轨电车、火车或轮渡站点**，Organic Maps 即可高亮整条公共交通线路，并可从显示的线路和路线列表中选择具体路线。
- **更清爽的书签标签和更易读的地图。** 新的标签布局让书签标题不再互相挤占，步行区域颜色略微加深，路线颜色经过调校，在浅色与深色主题下对比度更佳。
- **更精细的亚洲地区划分。** 越南和马来西亚现已拆分为更小的地图，便于您只下载所需区域；香港、澳门、海南也已从广东独立出来。

## 发布说明

### 所有平台

- 新增！点击公共交通站点并选择线路编号，即可在地图上高亮整条公共交通线路，类似地铁地图图层的效果（Viktor Govako、Kiryl Kaveryn、Mikhail Listratsenka）
- 新增！地图上的书签标签不再重叠（Viktor Govako）
- 修正了轨迹图表中海拔上升和下降的计算，使数值与其他流行应用更加一致（Viktor Govako）
- 长途公共交通及其他地图关系现在可跨越地图边界拼接为一条连续的线路（Viktor Govako）
- 越南和马来西亚已拆分为更小、可单独下载的区域（Viktor Govako）
- 香港、澳门和海南已从广东独立出来，并更新了相邻边界（Viktor Govako）
- 更新了印度尼西亚、马来西亚、坦桑尼亚、泰国和越南的等高线（Viktor Govako）
- 路线规划：恢复路线时，现在会自动去除您已经经过的中间点（Viktor Govako）
- 新增活火山和水上通道入口图标；船台现在可被搜索（David Martinez）
- 新增水烟馆（alnzrv）
- 新增在建建筑物（Viktor Govako）
- 新增「Lookout」作为观景点的搜索同义词（alnzrv）
- 新增「pkwy」作为美国街道名称的同义词（Viktor Govako）
- 步行区颜色略微加深，提升可读性（Viktor Govako）
- 地图上的多行文字现在会被整洁地裁剪（Viktor Govako）
- 街道名称不再包含重复部分（Viktor Govako）
- 修复 KMB 文件导入问题（Alexander Borsuk）
- 更新了分类、搜索同义词及界面字符串的翻译（Alexander Borsuk、Viktor Govako）
- 翻译了新南威尔士州和北领地的描述（alnzrv）
- 提升了稳定性和性能，包括字体塑形、字形缓存以及路线线条裁剪（Viktor Govako、Alexander Borsuk）

### iOS

- 新增！在导航中的信息面板加入轨迹录制按钮（Kiryl Kaveryn）
- 新增！导航仪表盘新增两个显示层级，可提供更精细的海拔与路线信息（Kiryl Kaveryn）
- 更新了导航仪表盘中的海拔图样式，并正确渲染包含负海拔的轨迹（Kiryl Kaveryn）
- 修复 TestFlight 版本中显示错误书签列表的问题（Alexander Borsuk）
- 加大了「停止」按钮，并增大了导航底部面板按钮的触摸区域：TTS 静音、设置、轨迹录制（Kiryl Kaveryn）
- 优化了地点页面中可展开描述区域的动画（Kiryl Kaveryn）
- 地点页面在海拔图拖动结束时不再关闭，不再意外回弹，使用键盘编辑时标题也会保持可见（Kiryl Kaveryn）
- 修复了系统外观切换时海拔图和环形进度条颜色异常的问题（Kiryl Kaveryn）
- 修复了删除已不存在的轨迹或书签时的崩溃问题（Kiryl Kaveryn）

### Android

- 新增！常驻海拔仪表盘和更精细的路线海拔剖面，并支持正确的 RTL 布局（Eric Jau、Mikhail Listratsenka）
- 设备旋转后保留已保存的路线状态（Mikhail Listratsenka）
- 地点页面中的路线参考线现在单一且统一（Mikhail Listratsenka）
- 底部弹层、按钮及 drawable 资源采用更大的圆角，外观更一致（Mikhail Listratsenka）
- 修复了系统状态栏和导航栏附近的布局错位问题（Mikhail Listratsenka）
- 改进了 Wikipedia 文章的显示，包括更好的排版、系统颜色和深色模式处理（DeshDeepakKant、Mikhail Listratsenka）
- 在海拔图上为多几何轨迹的各段之间添加垂直分隔线（Mikhail Listratsenka）
- 改进了海拔图的滚动行为（Mikhail Listratsenka）
- 从右到左（RTL）布局修复（Mikhail Listratsenka）

### Linux 和 Mac OS

- 新增公共交通线路选择器，可在选中站点时选择具体的交通线路（Viktor Govako）
- 在地点页面中直接显示路线操作按钮（Viktor Govako）
- 移除了地点页面中重复的开放时间（Viktor Govako）
- POI 或地址上的中间路线标记现在会显示该地点的标题（Viktor Govako）
- 正常关闭后地图下载可从中断处继续（Alexander Borsuk）
- Organic Maps 现已可在 OpenGL ES 3.0 驱动上运行（Alexander Borsuk）

加入测试版，抢先体验新功能并反馈问题：
- [iOS][testflight]
- [Android][firebase]

我们热爱我们的用户 ❤️，也热爱我们所做的事

Organic Maps 团队

{{ references() }}
