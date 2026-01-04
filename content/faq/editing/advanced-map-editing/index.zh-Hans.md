---
title: 如何进行更高级的地图编辑？
slug: 如何进行更高级的地图编辑
description: 使用 ID、Go Map 和 Vespucci 等更高级工具编辑 OpenStreetMap 的教程
updated: '2024-06-20'
taxonomies:
  faq: ["地图编辑"]
extra:
  order: 40
aliases:
  - /zh-Hans/faq/editing/advanced-map-editing/
---

Organic Maps 包含一个简单且易于使用的编辑器，您可以用它来编辑地图。然而，编辑器是有限的，只允许添加简单的点要素，这意味着没有建筑物轮廓、道路、湖泊、城镇等。如果您想更改无法使用内置编辑器编辑的内容，这是正确的常见问题解答页面。

由于 Organic Maps 中使用的所有地图数据均来自 [OpenStreetMap.org (OSM)](https://www.openstreetmap.org)，因此您可以直接在那里更新地图。您的修改将在下次地图更新时包含到有机地图中。

## OpenStreetMap 编辑器

对于编辑 OSM，有多种选项。如果您手头有笔记本电脑或台式计算机，最好使用在浏览器中运行的 [ID 编辑器](https://www.openstreetmap.org/edit)。 ID 编辑器对于初学者来说很简单，更大的屏幕、鼠标和键盘使地图编辑更容易。

要通过移动设备进行高级地图编辑，请使用 [Go Map](https://apps.apple.com/us/app/go-map/id592990211)（适用于 iOS）或 [Vespucci](https://play.google.com/store/apps/details?id=de.blau.android)（适用于 Android）。 Go Map 对于初学者来说很容易，而 Vespucci 则针对更高级的用户。 LearnOSM 提供了 [Go Map](https://learnosm.org/en/mobile-mapping/gomap/) 和 [Vespucci](https://learnosm.org/en/mobile-mapping/vespucci/) 的教程。

如需更简单、更有趣的编辑，您还可以尝试适用于 iOS 和 Android 的 [Every Door 应用程序](https://every-door.app/) 和适用于 Android 的 [StreetComplete 应用程序](https://streetcomplete.app/)。

#### ID 编辑器

要编辑带有 ID 的 OpenStreetMap，请按照以下步骤操作：

1. 创建一个新帐户或登录[OpenStreetMap.org](https://www.openstreetmap.org)
2. 在 OpenStreetMap.org 上浏览到您要编辑的位置，然后单击顶部的*编辑*
3. *开始演练*并按照解释 ID 编辑器的简短教程进行操作
4. 编辑地图
5. 上传您的更改

就是这样，您现在是 OSM 社区的一员了。

## 我的编辑会发生什么情况？

一旦您按下*上传*，您的更改将立即添加到公共 OSM 数据库中。所以编辑的时候一定要慎重。在有机地图中，您的更改将在下一次每月地图更新后可见。

您的电子邮件不会公开，但其他人将能够看到您的 OSM 用户名。由于 OSM 提供了讨论更改的可能性，您可能会从其他 OSM 贡献者那里得到有关您的编辑的问题。您将通过用于注册 OSM 帐户的电子邮件地址收到相关通知。由于 OSM 是一个建立在协作基础上的社区项目，因此您应该始终回答此类问题。

## 社区和维基

OpenStreetMap 是一个社区。如果您需要帮助或有任何问题，可以在 [OSM 论坛](https://community.openstreetmap.org/c/help-and-support) 中提问或查看 [OSM Wiki](https://wiki.openstreetmap.org/) 文档。

## 标签 - OSM 数据模型如何工作

OpenStreetMap 数据库包含从现实世界特征中抽象出来的节点、路径、区域和关系等对象。这些对象具有属性，即所谓的标签来进一步描述它们。标签是键值组合。

由于这听起来比实际更复杂，我们将举一个例子：
餐厅是例如映射为带有标签`amenity=restaurant`的注释或区域。然后可以使用`cuisine=*`或`opening_hours=*`等其他标签来获取更多详细信息。

> 请注意，ID 编辑器向用户隐藏了内部数据结构，以便对初学者更加友好。但对于阅读 Wiki 文档来说，对数据结构进行简要概述是有帮助的。
在 ID 编辑器中，您可以通过展开 *编辑功能* 侧面板中的 *标签* 部分来查看 ID 对您隐藏的标签。

## OSM 注释 {#osm-note}

如果您没有时间或者问题太复杂而无法自己编辑 OSM 数据，OSM Notes（[Wiki](https://wiki.openstreetmap.org/wiki/Notes)）是您的最佳选择。您可以在地图错误的位置放置这样的注释并详细描述问题。其他 OSM 志愿者可以帮助并解决问题。如果他们有进一步的问题或 OSM 说明得到解决，您将通过您的 OSM 帐户收到电子邮件通知。

1. 创建一个新帐户或登录[OpenStreetMap.org](https://www.openstreetmap.org)
   > 您也可以打开匿名注释，但不建议这样做，因为当问题解决或有其他问题时您不会收到通知。
2. 缩放到 [OpenStreetMap.org](https://www.openstreetmap.org) 上的地图位置，然后按 *向地图添加注释*（右侧菜单底部数第二个图标）。然后将蓝色地图标记拖动到确切位置。
   > 尽量做到精确。
3. 提供地图问题的详细描述并按*添加注释*
   > 对于商店，例如提供名称并提及那里出售的商品或提供的服务。
