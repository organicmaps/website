---
title: "إصدار 7 أكتوبر: حدود السرعة في Android Auto، استيراد GeoJSON وأكثر"
date: 2025-10-07T10:00:00+00:00
taxonomies:
  news: ["Releases"]
---

يمكن لمستخدمي Android Auto الآن مشاهدة تحذيرات حدود السرعة. تم إضافة استيراد ملفات GeoJSON التي يمكن تحويلها إلى علامات.

إصلاحات وتحسينات متنوعة لـ iOS وAndroid وAndroid Auto وسطح المكتب. انظر التفاصيل أدناه.

ميزات حديثة قد تكون فاتتك:
- شاشة تخطيط مسارات جديدة (iOS)
- وسم OSM `description` على iOS (ابحث `?description`)
- أرقام خطوط النقل العام عند اختيار موقف الحافلة
- مسارات المشي وركوب الدراجات (فعّلها عبر زر الطبقات في أعلى اليسار)
- إظهار أسماء العلامات على الخريطة (فعّل في الإعدادات)
- أيقونة ✎ تمكّنك من تحرير العلامات بسرعة

مشروع Organic Maps ممكن بفضل المساهمين، و[تبرعاتك](@/donate/index.ar.md)، و[دعمك](@/contribute/index.ar.md).

### ملاحظات الإصدار التفصيلية

- بيانات OpenStreetMap جديدة بتاريخ 5 أكتوبر
- تحديث الترجمات (مساهمو Weblate)
- إصلاح سهم الموقع بدون إشارة GNSS (Viktor Govako)

#### أنماط الخريطة (Viktor Govako)

- إعادة تصميم أيقونات نمط "Outdoor"
- إصلاح لون علامات المياه
- عرض المباني عند مستوى تكبير 16
- عرض منصات المشاهدة ونقاط المشاهدة من مستوى تكبير 14
- إصلاحات وتحسينات عامة للخريطة

#### iOS

- إصلاح ألوان نقاط المسار (Alexander Borsuk)
- تحسينات قائمة الضغط الطويل (Alexander Borsuk)
- إصلاح وقت نقطة الوصول عند تغيير نوع الوحدة (Viktor Govako)
- منع تحرير الكائنات المحذوفة (Kiryl Kaveryn)

#### Android

- جديد: استيراد ملفات GeoJSON وتحويلها إلى علامات (Andrei Shkrob، Alexander Borsuk)
- عرض شبكات WiFi والخلوي الأقرب أسفل "موقعي" (إصدار التصحيح فقط) (Kiryl Kaveryn)
- تحديث تسجيل الدخول إلى OSM (Viktor Govako)
- إصلاح رسالة خطأ تنزيل الخريطة (Viktor Govako)
- معالجة GeoIntent أكثر موثوقية (Alexander Borsuk)
- تحسينات واجهة ترحيل البيانات (Alexander Borsuk)
- تحسينات واجهة فئات التصنيف (Alexander Borsuk)
- إزالة خدمات موقع Google (Alexander Borsuk)
- فئة البحث "عنوان المدينة" أصبحت الآن "العنوان" (Alexander Borsuk)
- إصلاح احتمال ظهور شاشة داكنة عند النقر على نتيجة البحث (Viktor Govako)
- تعديلات واجهة في بحث "ما في الجوار" (Viktor Govako)
- إصلاح نوافذ منبثقة لا تحترم السمة الداكنة (Andrei Shkrob)

#### Android Auto

- جديد: حدود السرعة وتحذيرات كاميرات السرعة (Denis Koronchik)
- إصلاح معاينة المسار (Andrei Shkrob)
- تحسينات واجهة البحث (Andrei Shkrob)

#### سطح المكتب

- تحسينات تكييف الخريطة (Andrew Shkrob)
- إصلاح تباين مؤشر الماوس في السمة الداكنة (Andrew Shkrob)

احصل على أحدث إصدار: [App Store][appstore]، [Google Play][googleplay]، [Huawei AppGallery][appgallery]، [Obtainium][obtainium]، [Accrescent][accrescent]، [F-Droid][fdroid].

انضم للاختبار التجريبي: [iOS][testflight] / [Android][firebase].

{{ references() }}
