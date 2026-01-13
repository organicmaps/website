---
title: "האם כבר התקנתם את גרסת יולי של Organic Maps? היא כוללת שתי תכונות עיקריות שפותחו במימון NGI0 Entrust Fund."
date: 2024-07-15T21:13:23+00:00
slug: july-release-with-improved-usa-address-search-using-tiger-data-and-fixed-text-rendering-for-non-latin-scripts-funded-by-ngi0-entrust-fund
taxonomies:
  news: ["גרסאות"]
---

האם כבר [התקנתם](https://omaps.app/get) את גרסת יולי של Organic Maps? היא מציגה שתי תכונות עיקריות [שמומנו](https://nlnet.nl/project/OrganicMaps/) באמצעות קרן NGI0 Entrust:

1. חיפוש כתובות משופר בארצות הברית, המבוסס על נתוני TIGER (Topologically Integrated Geographic Encoding and Referencing system) (שנערכו מראש על ידי [פרויקט Nominatim](https://nominatim.org/data/)), [שמיושם](https://github.com/organicmaps/organicmaps/issues/2532) על ידי Viktor Havaka. כתובות מאוחסנות, מחופשות ומוצגות כאינטרפולציות (קווים לאורך רחובות עם מספר בית מתחיל ומספר בית מסתיים), לכן אל תצפו לראות מבנים על המפה (הידעתם שאתם יכולים לצייר מבנים ולהוסיף כתובות ב-[OpenStreetMap.org](https://openstreetmap.org/) בעצמכם?).
ישנו אלגוריתם שמחליט מתי להשתמש בנתוני TIGER ומתי להשתמש בנתוני OpenStreetMap הקיימים.
גודל המפה של כל ארה"ב גדל מ-10 ג'יגה-בייט ל-13 ג'יגה-בייט (כולל ויקיפדיה ונתוני גובה, יש כמה [רעיונות](https://github.com/organicmaps/organicmaps/issues/8672) ל[פיצול](https://github.com/organicmaps/organicmaps/issues/5912) כדי לשפר [עדכוני מפה מצטברים](https://github.com/organicmaps/organicmaps/issues/2317)). 2. עיבוד נכון של טקסטים בשפות הודיות (דבנאגרי, בנגלית, גוג'ראטית, גורמוקית, קנדה, מלאילאם, אורייה, טמילית, טלוגו), ערבית (נקו, סורית, מונגולית), תאית ולאו, קמרית, מיאנמרית, טיבטית, האנגולית, עברית, [מיושם](https://github.com/organicmaps/organicmaps/issues/4281) על ידי אלכסנדר בורסוק על ידי שילוב ספריית עיצוב הטקסט [Harfbuzz](https://harfbuzz.github.io/) עם מנוע העיבוד של Organic Maps (המכונה "Drape").

ישנם שיפורים בולטים נוספים, הודות לתורמים היקרים שלנו: * נתוני OpenStreetMap נכון ל-2 ביולי * גופנים חדשים במלאילאם ובבנגלית (אנא הודיעו לנו אם יש גופנים נוספים שצריכים לעדכון) * נגיעה אחת בוחרת כעת כל נקודה במפה, גם אם המפה ריקה -- על ידי סרגיי קוזיר
* שינוי הקשה ארוכה למצב מסך מלא -- מאת Sergiy Kozyr * סימניה שנמחקה בטעות במפה ניתנת כעת לשחזור מיידי (כפתור "שמור" משתנה ל"שחזור") -- מאת Kiryl Kaveryn * הצגת כבישים ראשיים מוקדם יותר במפת התצוגה הכללית של העולם -- מאת Konstantin Pastbin * מקום שנבחר מציג כעת יותר סוגים/קטגוריות/שירותים -- מאת David Martinez
* תווית ברורה יותר לרמת הבניין של POI - מאת Antonin Delpeuch * הצגת שבילים להולכי רגל מחצץ עדין באיכות טובה כקו מקווקו לבן - מאת Konstantin Pastbin * תמיכה בסוגים נוספים של משטחי כבישים/שבילים (לבנים, אבן, ריצוף דשא, אדמה) - מאת Konstantin Pastbin * רמזים ברורים יותר בעת בניית מסלול חיפוש - תודה ל-Viktor Havaka:
* חיפוש הרים מציג גם הרי געש * תוצאות חיפוש טובות יותר עבור מקומות מרוחקים * החיפוש מוצא כעת מקומות עם מספר בשמם * חיפוש תאי אחסון באמצעות מספרי התייחסות Android: * תיקון קישור TTS FAQ בהגדרות * תיקון ייבוא GPX מ-WhatsApp * שמירת קבצים מיוצאים לאחסון המכשיר המקומי -- מאת קיריל רז'דזסטבנסקי iOS (תודה רבה לקיריל קברן):
* השתמשו בכפתור הייבוא בתיבת הדו-שיח "סימניות ומסלולים" כדי לטעון קבצי KML, KMZ, GPX * תיקון ייבוא סימניות ומסלולים באמצעות האפליקציה "קבצים" בהפעלה קרה (ניתן להקיש על קובץ KML, KMZ, GPX או KMB בכל אפליקציה, ואז "לשתף" אותו באמצעות סמל מלבני עם חץ כלפי מעלה בפינה השמאלית התחתונה, ולאחר מכן לבחור בסמל Organic Maps ברשימת כל האפליקציות)
* נוספה לחצן בדיקת קול TTS בהגדרות הניווט -- מאת פביאן וותריץ' * אפשר יומנים בהגדרות כדי לעזור לנו בתיקון באגים * פתח קישורים למדיה חברתית ביישומים המותקנים * הוסר לחצן תנועה לא פעיל מ-CarPlay -- מאת פביאן וותריץ' * הוחלפו תיבות סימון עגולות במלבן מעוגל בעורך הזמן
* תיקון צבע הרקע של מצב כהה בעת ההפעלה -- מאת Evgeny Fayvuzhinsky לינוקס: * תיקון סמל Wayland כללי המוצג במקום סמל Organic Maps במערכות מסוימות -- מאת Ferenc Géczi המתרגמים והמבקרים שלנו סייעו לנו לעדכן את התרגומים לבלארוסית, סינית, הולנדית, אסקרית, הונגרית, פולנית, פורטוגזית, רוסית ואוקראינית.

כמו כן, התחלנו לעדכן את [סעיף השאלות הנפוצות](https://organicmaps.app/faq/) באתר האינטרנט שלנו. כל עזרה [בהוספת מאמרים חדשים](https://github.com/organicmaps/organicmaps.github.io/) ותרגומיהם תתקבל בברכה!

אנא דווחו על כל הבעיות באמצעות כפתור "דווח על באג" באפליקציה, על ידי שליחת דוא"ל אלינו, או (הכי טוב!) על ידי יצירת/עדכון [בעיה](https://github.com/organicmaps/organicmaps/issues/) ב-GitHub שלנו.

נ.ב. כעת אנו עובדים על [תכונת מקליט המסלול](https://github.com/organicmaps/organicmaps/labels/Track%20Recording). כל עזרה עם רעיונות, [בדיקות](https://organicmaps.app/#community), [תרומות](https://organicmaps.app/support-us/) ו[תרומות](https://organicmaps.app/donate/) תתקבל בברכה ❤️

תהנו מנסיעה עם Organic Maps! 🚕 🛤 ✈️ 🏕 👣