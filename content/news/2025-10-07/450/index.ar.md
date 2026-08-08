---
title: "إصدار 7 أكتوبر: حدود السرعة في Android Auto، استيراد GeoJSON، إحصائيات المسار أثناء التسجيل، عرض وسم description في OSM، حفظ علامة على المسار المحدد في iOS، وأكثر"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["releases"]
---

يضيف تحديث Organic Maps الصادر في 7 أكتوبر عرض حدود السرعة في Android Auto واستيراد GeoJSON وإحصائيات المسار أثناء التسجيل، ويعرض وسوم description في OSM (اكتب `?description` في مربع البحث لرؤيتها)، ويحفظ علامة على مسار في iOS. كما توجد تحسينات كثيرة في واجهة المستخدم وفي تحرير OpenStreetMap وإصلاحات متنوعة للأخطاء على جميع المنصات، بما في ذلك إصلاح الانهيار عند بدء التشغيل على بعض أجهزة Android.

مشروع Organic Maps ممكن بفضل ❤️ مساهمينا، و[تبرعاتك](@/donate/index.ar.md)، و[دعمك](@/contribute/index.ar.md).

### ملاحظات الإصدار التفصيلية (بما في ذلك تغييرات التحديث الطفيف السابق)

- جديد! استيراد GeoJSON (Sergiy Kozyr)
- بيانات OpenStreetMap حتى 4 أكتوبر
- بيانات ويكيبيديا حتى 1 أكتوبر
- دعم قطار سياتل الخفيف في النقل العام (tjasz)
- عدم إلغاء التحديد على الخريطة عند حفظ مكان OSM بعد تحريره (Kiryl Kaveryn)
- تحديث الترجمات (مساهمو Weblate)

#### أنماط الخريطة

- عرض متاجر تأجير الدراجات الموسومة amenity=bicycle + rental=shop (David Martinez)
- عرض المواقع الأثرية التاريخية من مستوى التكبير 12 وباقي المواقع التاريخية من مستوى التكبير 15 في نمط Outdoor (Viktor Govako)
- أيقونات جديدة للصواري وأبراج الاتصالات وأبراج الكهرباء في نمط Outdoors (David Martinez)
- تكبير أيقونة القمة في نمط Outdoors (David Martinez)
- إضافة أشكال أيقونات POI الناقصة (David Martinez)
- إضافة المزيد من أنواع الحواجز (Viktor Govako)

#### iOS

- جديد: حفظ علامة على نقطة المسار المحددة (Kiryl Kaveryn)
- جديد: حذف المسار أثناء تسجيله دون الحاجة إلى حفظه أولًا (Kiryl Kaveryn)
- عرض عناوين قوائم العلامات على عدة أسطر في صفحة المكان (David Martinez)
- تحديث نمط أزرار تسجيل الدخول إلى OSM (Kiryl Kaveryn)
- إصلاح مشكلة تحديث معلومات الملاحة (Kiryl Kaveryn)
- إصلاح مشكلات تخطيط المسار الجديد (Kiryl Kaveryn)
- إصلاح ظهور خيار إضافة أو تحرير مكان OSM للخرائط الأقدم من 3 أشهر (Kiryl Kaveryn)
- إصلاح تخطيط عنصر تحديد خيارات النقل في iOS 26 (Kiryl Kaveryn)
- تبسيط حركات تحديد العلامات (Kiryl Kaveryn)
- إصلاح مشكلة تحديد نتيجة البحث (Kiryl Kaveryn)
- إصلاح التنسيق والسحب والحركات في صفحة معلومات المكان (Kiryl Kaveryn)

#### Android Auto (على Google Play فقط)

- جديد: عرض حدود السرعة في Android Auto (Andrei Shkrob)
- إصلاح تبديل الشاشة في وضع الملاحة في Android Auto (Andrei Shkrob)
- إصلاح إزاحة سهم التوجيه في Android Auto (Andrei Shkrob)
- إصلاح مشكلة عند توصيل الجهاز بالسيارة أو فصله عنها (Andrei Shkrob)
- إضافة خدمة الموقع في Android Auto (Andrei Shkrob)
- تحسين محاكي المسار في Android Auto (Viktor Govako)

#### Android

- جديد: عرض إحصائيات المسار أثناء تسجيله في الوقت الفعلي (Kavi Khalique)
- جديد: عرض محتوى وسم `description` في OSM (Alexander Borsuk)
- إصلاح معالجة تغيير السمة (Andrei Shkrob)
- إصلاح عدة انهيارات، بما فيها الانهيار عند بدء التشغيل (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- إشعارات صامتة لتقدم التنزيل (Viktor Govako)
- تقليل الحشو حول أيقونة القلم (Alexander Borsuk)

#### سطح المكتب

- إصلاح تعليق curl على Linux (Alexander Borsuk)
- إصلاح التعليق على macOS عند تسجيل الدخول إلى OSM (Alexander Borsuk)
- إجراء لتحديد عنصر من قائمة السياق (Viktor Govako)
- خيار إلغاء التنزيل (Viktor Govako)
- عرض نوع الشكل الهندسي في قائمة السياق (Viktor Govako)

### ميزات صدرت مؤخرًا وربما فاتتك

- أرقام خطوط النقل العام عند اختيار موقف الحافلة
- مسارات المشي وركوب الدراجات (فعّلها عبر زر الطبقات في أعلى اليسار)
- عرض أسماء العلامات على الخريطة بتفعيل ذلك في إعدادات التطبيق
- أيقونة القلم ✎ تتيح لك طريقة سريعة لتحرير العلامات

### تثبيت Organic Maps

احصل على أحدث إصدار من Organic Maps من [App Store][appstore]، [Google Play][googleplay]، [Huawei AppGallery][appgallery]، [Obtainium][obtainium]، [Accrescent][accrescent] و[F-Droid][fdroid].

انضم إلى الاختبار التجريبي للحصول على الميزات مبكرًا: [iOS][testflight] / [Android][firebase].

{{ references() }}
