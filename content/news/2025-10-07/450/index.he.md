---
title: "7 באוקטובר: הגבלת מהירות ב-Android Auto, ייבוא GeoJSON, רישום נתוני מסלול, הצגת תגיות תיאור OSM, שמירת סימניות במסלול הנבחר ב-iOS ועוד."
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["גרסאות"]
---

עדכון Organic Maps מ-7 באוקטובר מוסיף תצוגת מגבלת מהירות ב-Android Auto, ייבוא GeoJSON, הקלטת סטטיסטיקות מסלול, הצגת תגיות תיאור OSM (הקלד `?description` בתיבת החיפוש כדי לראותן) ושמירת סימנייה על מסלול ב-iOS. כמו כן, ישנם שיפורים רבים בממשק המשתמש, בעריכת OpenStreetMap ותיקוני באגים שונים בכל הפלטפורמות, כולל תיקון קריסה בעת ההפעלה בחלק ממכשירי Android.

Organic Maps מתאפשר הודות ❤️ לתורמים שלנו, [לתרומות שלכם](@/donate/index.md) ול[תמיכתכם](@/contribute/index.md). ### הערות מפורטות על הגרסה (כולל השינויים הקטנים מהעדכון הקודם)

- חדש! ייבוא GeoJSON (Sergiy Kozyr) - נתוני OpenStreetMap נכון ל-4 באוקטובר - נתוני ויקיפדיה נכון ל-1 באוקטובר - תמיכה ברכבת הקלה של סיאטל בתחבורה ציבורית (tjasz) - אל תשבית את בחירת המפה בעת שמירת מקום OSM שעבר עריכה (Kiryl Kaveryn) - תרגומים מעודכנים (תורמי Weblate)

#### סגנונות מפה - הצגת חנויות להשכרת אופניים המתויגות כ-amenity=bicycle + rental=shop (David Martinez) - הצגת אתרים ארכיאולוגיים היסטוריים מזום 12 ואתרים היסטוריים אחרים מזום 15 בסגנון Outdoor (Viktor Govako) - סמלים חדשים למגדלי תקשורת, חשמל ואנטנות בסגנון Outdoors (David Martinez) - הגדלת גודל הסמל בסגנון Outdoors (David Martinez) - הוספת וריאציות סמלי POI חסרים (David Martinez) - הוספת סוגי מחסומים נוספים (Viktor Govako) #### iOS - חדש: שמירת סימנייה בנקודת מסלול נבחרת (Kiryl Kaveryn) - חדש: מחיקת מסלול ההקלטה ללא שמירה מוקדמת (Kiryl Kaveryn) - הצגת כותרות רשימת סימניות מרובות שורות בדף המקום (David Martinez)
- עדכון סגנון כפתורי הכניסה ל-OSM (קיריל קברין) - תיקון בעיה בעדכון מידע הניווט (קיריל קברין) - תיקון בעיות בתכנון מסלולים חדשים (קיריל קברין) - תיקון נראות הוספה/עריכה של מקומות ב-OSM עבור מפות ישנות מ-3 חודשים (קיריל קברין) - תיקון פריסת בקרת קטעי אפשרויות התחבורה עבור iOS 26 (קיריל קברין)
- פישוט אנימציות בחירת סימניות (Kiryl Kaveryn) - תיקון בעיה בבחירת תוצאות חיפוש (Kiryl Kaveryn) - תיקון עיצוב, החלקה ואנימציות בדף מידע על מקום (Kiryl Kaveryn) #### Android Auto (Google Play בלבד)

- חדש: תצוגת מגבלת מהירות ב-Android Auto (Andrei Shkrob) - תיקון מעבר תצוגה במצב ניווט ב-Android Auto (Andrei Shkrob) - תיקון קיזוז חץ הניווט ב-Android Auto (Andrei Shkrob) - תיקון בעיה בעת חיבור/ניתוק מכשיר לרכב (Andrei Shkrob) - הוספת שירות מיקום Android Auto (Andrei Shkrob) - שיפור סימולטור המסלול ב-Android Auto (Viktor Govako) #### Android - חדש: הצגת סטטיסטיקות מסלול ההקלטה בזמן אמת (Kavi Khalique) - חדש: הצגת תוכן התגית `description` של OSM (Alexander Borsuk) - תיקון טיפול בשינוי ערכת נושא (Andrei Shkrob) - תיקון מספר קריסות, כולל זו בעת ההפעלה (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- התראות שקטות על התקדמות ההורדה (Viktor Govako) - צמצום מרווח סמל העיפרון (Alexander Borsuk) #### שולחן עבודה - תיקון תקיעת curl ב-Linux (Alexander Borsuk) - תיקון תקיעה ב-macOS בעת כניסה ל-OSM (Alexander Borsuk) - פעולה לבחירת תכונה מתפריט ההקשר (Viktor Govako) - אפשרות לביטול ההורדה (Viktor Govako)
- הצגת סוג הגיאומטריה בתפריט ההקשר (ויקטור גובקו) ### תכונות ששוחררו לאחרונה ואולי פספסתם - מספרי קווי תחבורה ציבורית בעת בחירת תחנת אוטובוס - מסלולי טיול ורכיבה על אופניים (הפעילו אותם באמצעות כפתור השכבות בפינה השמאלית העליונה) - צפו בשמות הסימניות במפה על ידי הפעלתן בהגדרות האפליקציה - סמל העיפרון ✎ מאפשר עריכה מהירה של סימניות

### התקן את Organic Maps הורד את הגרסה העדכנית ביותר של Organic Maps מ-[App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] ו-[F-Droid][fdroid].

הצטרפו לבדיקת בטא כדי ליהנות מתכונות מוקדמות: [iOS][testflight] / [Android][firebase].

{{ references() }}