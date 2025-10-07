---
title: "10月7日发布：Android Auto 速度限制、GeoJSON 导入等"
date: 2025-10-07T10:00:00+00:00
---

Android Auto 用户现在可以看到速度限制警告。新增 GeoJSON 文件导入功能，可转换为书签。

iOS、Android、Android Auto 和桌面版本的各种修复与改进。详见下文。

您可能错过的近期功能：
- 全新路线规划界面（iOS）
- iOS 上的 OSM `description` 标签（搜索 `?description`）
- 选择公交站时显示公交线路号
- 徒步与骑行路线（通过左上角"图层"按钮启用）
- 地图上显示书签名称（在设置中启用）
- ✎ 图标可快速编辑书签

Organic Maps 得益于贡献者、[您的捐赠](@/donate/index.zh-Hans.md) 和 [您的支持](@/contribute/index.zh-Hans.md)。

### 详细更新日志

- 截至 10 月 5 日的最新 OpenStreetMap 数据
- 更新翻译（Weblate 贡献者）
- 修复无 GNSS 信号时的位置箭头（Viktor Govako）

#### 地图样式（Viktor Govako）

- 重新设计"户外"样式图标
- 修复水标签颜色
- 在缩放 16 时显示建筑
- 从缩放 14 起显示观景台和观景点
- 通用地图修复与改进

#### iOS

- 修复路线点颜色（Alexander Borsuk）
- 长按菜单改进（Alexander Borsuk）
- 修复更改单位类型时到达点的时间问题（Viktor Govako）
- 阻止编辑已删除的对象（Kiryl Kaveryn）

#### Android

- 新增：导入 GeoJSON 文件并转换为书签（Andrei Shkrob，Alexander Borsuk）
- 在"我的位置"下方列出最近的 WiFi 和手机网络（仅限调试版本）（Kiryl Kaveryn）
- 更新 OSM 登录功能（Viktor Govako）
- 修复下载地图时的错误消息显示问题（Viktor Govako）
- 更可靠的 GeoIntent 处理（Alexander Borsuk）
- 数据迁移 UI 改进（Alexander Borsuk）
- 分类类别的 UI 改进（Alexander Borsuk）
- 移除 Google 位置服务（Alexander Borsuk）
- "城市地址"搜索类别现在为"地址"（Alexander Borsuk）
- 修复点击搜索结果时可能出现的暗屏问题（Viktor Govako）
- "附近有什么"搜索中的 UI 调整（Viktor Govako）
- 修复弹出式对话框不适应深色主题问题（Andrei Shkrob）

#### Android Auto

- 新增：速度限制和速度摄像头警告（Denis Koronchik）
- 修复路线预览（Andrei Shkrob）
- 搜索 UI 改进（Andrei Shkrob）

#### 桌面版

- 地图调整改进（Andrew Shkrob）
- 修复深色主题下鼠标光标的对比度（Andrew Shkrob）

获取最新版本：[App Store][appstore]、[Google Play][googleplay]、[Huawei AppGallery][appgallery]、[Obtainium][obtainium]、[Accrescent][accrescent]、[F-Droid][fdroid]。

加入测试版：[iOS][testflight] / [Android][firebase]。

{{ references() }}
