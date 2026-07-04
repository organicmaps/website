---
title: "卫星影像、公共交通路线、备选路线、Android 全新搜索和路线规划界面、iOS 大号辅助功能字体支持，以及 2026 年 6 月更新中的更多内容"
date: 2026-06-29
slug: weixing-yingxiang-gonggong-jiaotong-luxian-beixuan-luxian-android-xin-sousuo-luxian-guihua-jiekou-ios-da-ziti-fuzhu
taxonomies:
  news: ["releases"]
---

Organic Maps 六月更新中有许多值得一试的精彩新功能和错误修复，包括：
- 卫星影像
- 公共交通路线
- 备选路线
- Android 全新搜索和路线规划界面
- iOS 大号辅助功能字体支持

请在 <https://get.omaps.org> 或 [App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium]、[Accrescent][accrescent] 和 [F-Droid][fdroid] 获取更新，并告诉我们你的想法！

## 详细更新日志

- 新增！支持地铁、轻轨、公交和有轨电车的公共交通路线规划 _(Viktor Govako)_
- 新增！备选路线：除了最快路线，应用现在还会显示最短路线 _(Viktor Govako)_
- 新增！步行和骑行路线会提示沿途的台阶、闸门和抬杆道闸 _(Viktor Govako)_
- 新增！可为书签选择任意颜色 _(Alexander Borsuk, Mikhail Listratsenka)_
- 新增！支持 British National Grid (OS Grid)、Irish Grid 和 Irish Transverse Mercator (ITM) 坐标 _(Alexander Borsuk)_
- 实验性：可在 Organic Maps 设置中通过自定义栅格瓦片服务器 URL 启用卫星影像。我们仍在搭建自己的服务器，因此请先寻找一个公开可用且 URL 中包含 `{x}`、`{y}`、`{z}` 占位符的服务器 _(Viktor Govako, renderexpert)_
- OpenStreetMap 数据已更新至 6 月 24 日 _(Viktor Govako)_
- Wikipedia 数据已更新至 6 月 20 日，包括意大利语文章 _(Alexander Borsuk)_
- 在搜索窗口输入 `?map-download-server:https://your-server.com/` 可覆盖 Organic Maps 的地图下载服务器。输入 `?no-map-download-server` 可移除该覆盖设置 _(Alexander Borsuk)_

#### 地图渲染和样式

- 海滩、沙地、碎石坡、裸岩、果园和葡萄园区域的图案更美观，并为保护区和湿地加入了阴影线 _(Alexander Borsuk)_
- 道路和河流的弯曲文字标签更加平滑 _(Viktor Govako)_
- 河流、溪流和湿地在深色模式下对比度更高，也更醒目 _(Alexander Borsuk)_
- 改进并新增了分类搜索和地图搜索结果的图标 _(Anton Makouski)_
- 改进了多语言文本塑形和渲染 _(Alexander Borsuk)_
- 多项错误修复和性能改进 _(Viktor Govako)_

#### 轨迹、书签和路线

- GeoJSON 轨迹现在会在导入和导出时保留海拔和时间戳 _(Alexander Borsuk)_
- 修复了将轨迹移动到另一个列表后发生的崩溃 _(Viktor Govako)_
- 文化遗产地点现在会显示网站 _(Viktor Govako)_
- 未命名搜索结果现在会显示运营方名称。例如，未命名的 ATM 现在会显示其所属银行 _(Anton Makouski)_
- 编辑器：修正了公寓楼 OpenStreetMap 编辑/变更集的说明文字 _(titanniya542-spec)_
- 改进了书签和轨迹描述中的 HTML 检测 _(Alexander Borsuk)_

### iOS

- 新增！支持 Dynamic Type 和大号字体辅助功能 _(Kiryl Kaveryn)_
- 新增！轻点即可在重叠的轨迹和路线之间选择 _(Kiryl Kaveryn)_
- 改进了书签和轨迹描述中的 HTML 渲染 _(Kiryl Kaveryn)_
- 界面中的表格样式更简洁 _(Kiryl Kaveryn)_

### Android

- 新增！搜索界面 _(Kavi Khalique, Mikhail Listratsenka, Alexander Borsuk)_
- 新增！路线规划界面 _(Rishan, Mikhail Listratsenka, Alexander Borsuk)_
- 改进了书签和轨迹描述中的 HTML 渲染 _(Mikhail Listratsenka)_
- 减小了 APK 体积 _(Alexander Borsuk)_
- 当没有可用的文本转语音引擎时，语音图标会显示为禁用状态 _(Mikhail Listratsenka)_
- 较长的书签和轨迹描述现在会显示“…更多”按钮 _(Mikhail Listratsenka)_
- 多项界面修复，并修复了返回的点 ID 的 API 问题 _(Mikhail Listratsenka)_

### 桌面

- 支持切换显示的坐标系 _(Alexander Borsuk)_
- 所选地点的信息现在会显示在左侧 _(Viktor Govako)_
- 修复了上下文菜单位置 _(Osyotr)_
- 修复了 Qt 6.4 及更早版本中 OpenStreetMap 登录和编辑会卡住的问题 _(Alexander Borsuk)_
- 修复了 macOS 上路线规划期间地图样式意外切换的问题 _(Alexander Borsuk)_
- 修复了导出 KMZ 文件后关闭 macOS 应用时发生的崩溃 _(Alexander Borsuk)_

### 翻译

- 粤语逐步语音导航 _(Alexander Borsuk)_
- 更新了德语和法语翻译 _(Wuzzy, Alexander Borsuk)_
- 修正了中文、塞尔维亚语和加泰罗尼亚语中 “onto street” 语音导航提示的错误翻译 _(Alexander Borsuk)_

## 加入 Beta 测试，抢先体验早期功能并报告问题：

- [iOS][testflight]
- [Android][firebase]
- [Flathub/Flatpak][flathub]

我们感谢所有用户和贡献者，也感谢那些[捐款](@/donate/index.zh-Hans.md)并在应用商店给 Organic Maps 打 5 星的人。我们一起可以打造最好的地图应用！

满怀爱意，
Organic Maps 团队

{{ references() }}
