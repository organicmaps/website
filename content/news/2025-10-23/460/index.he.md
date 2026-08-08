---
title: "23 באוקטובר: Organic Maps כאפליקציית ניווט ברירת המחדל באיחוד האירופי ב-iOS, תצוגת שלטי דרכים ב-Android, שיפורים ותיקונים נוספים"
date: 2025-10-23T17:20:21+00:00
slug: "october-23-release-organic-maps-default-navigation-app-eu-ios-road-shields-displaying-android-improvements-fixes"
taxonomies:
  news: ["גרסאות"]
---

בגרסה שפורסמה ב-23 באוקטובר התמקדנו בתיקונים ושיפורים. ראו את הרשימה המפורטת להלן.

למי שפספס, [העדכון הקודם מ-7 באוקטובר](https://organicmaps.app/news/2025-10-07/android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display/
) הוסיף ייבוא GeoJSON, רישום סטטיסטיקות מסלול, תצוגת מגבלת מהירות ב-Android Auto, תצוגת תגיות תיאור OSM (הקלידו `?description` בתיבת החיפוש כדי לראותן), שמירת סימניה על מסלול ב-iOS, ושיפורים רבים אחרים.

## כל הפלטפורמות

- נתוני OpenStreetMap מעודכנים מ-21 באוקטובר 2025 (Viktor Govako)
- הצגת שמות כניסות/יציאות הרכבת התחתית במפה (Viktor Govako)
- סוגי POI וסמלים חדשים: תחנות ניטור, איי תנועה, מתקני טיפול במים Kneipp, רכבות מיניאטוריות (Viktor Govako), אתרי קמפינג בסגנון חוץ, טרמינלים בשדות תעופה, אזורי משחק מקורים, חנויות טלקומוניקציה, מתקני השכרת סירות, מתקני שיט, סמלים מעודכנים לפינוי פסולת ומזבלות (David Martinez)
- תרגום ממשק האפליקציה לסלובנית (Alexander Borsuk) והנחיות קוליות TTS לניווט (Erik Bucik)
- בחלק מהמכשירים/מסכים, המפה במרכזי הערים פחות עמוסה כעת (Viktor Govako)
- תיקון סיבוב המפה בחיישני מצפן לקויים בעת הליכה במצב ניווט להולכי רגל (Viktor Govako)
- שיפור המידע המוצג לאחר בחירת קטע נהר או נתיב מים (Viktor Govako)
- חיפוש טוב יותר של תחנות טעינה לרכבים חשמליים עם מילים נרדפות משופרות בכל השפות (Alexander Borsuk)
- תיקון חיפוש אמוג'י עם בוררי וריאציות (Alexander Borsuk)
- תיקון תוצאות חיפוש רבות מדי המוצגות עבור חלק משאילתות התאמת כתובות מלאות (Viktor Govako)
- ייבוא GeoJSON מ-https://umap.openstreetmap.fr/ אמור כעת לשמור את כל המטא-נתונים (Shubh Kesharwani)
- צבעים נוספים נתמכים עבור שבילים מסומנים בשכבת המפה "מסלולי טיול" (Viktor Govako)

## iOS

- משתמשים באיחוד האירופי יכולים להגדיר את Organic Maps כאפליקציית הניווט המוגדרת כברירת מחדל בהגדרות iOS → אפליקציות → אפליקציות ברירת מחדל → ניווט (Kiryl Kaveryn)
- תוקן סרגל מצב לבן על לבן במצב ניווט (Kiryl Kaveryn)
- הגדלנו את גודל כפתור 'התחל ניווט' (Kiryl Kaveryn)
- הסרנו את הרווח הריק בעת תכנון מסלול ב-iPad (Kiryl Kaveryn)
- Organic Maps עשויה לבקש מכם לדרג אותה ב-App Store. הביקורות הטובות שלכם מהוות מוטיבציה לצוות שלנו!

## Android

- כעת מופיעים שלטי דרך בכיווני הניווט (Andrei Shkrob)
- שיפורים במידע על הקלטת מסלולים (Kavi Khalique)
- Organic Maps פועלת במכשירים ישנים יותר עם מעבד Intel x86 (Andrei Shkrob)
- תוקן תקלה שבה הוראות קוליות TTS לא פעלו במקרים מסוימים (Andrei Shkrob)
- מסך פתיחה משופר בעת ההפעלה (Andrei Shkrob)

### Android Auto
- שחזור המסלול לאחר ביטול (Andrei Shkrob)
- תוקנו קריסות במכשירים מסוימים (Andrei Shkrob)

## Linux/Mac OS

- פרטי POI מוצגים כעת בפורמט "שם | ref" (Viktor Govako)
- מצב כהה מסתנכרן אוטומטית עם הגדרות המערכת (DeepChirp)

## הערות שוליים

Organic Maps מתאפשר הודות ❤️ לתורמים שלנו, [לתרומות שלכם](@/donate/index.he.md) ול[תמיכתכם](@/contribute/index.he.md).

הורידו את הגרסה האחרונה של Organic Maps מ-[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ו-[F-Droid][fdroid].

נ.ב. הצטרפו לבדיקות בטא כדי ליהנות מתכונות חדשות:
- [iOS][testflight]
- [Android][firebase].

באהבה למשתמשים ולקהילה שלנו
צוות Organic Maps

{{ references() }}