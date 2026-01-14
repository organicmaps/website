---
title: "מימון המונים אורגני ועדכון ספטמבר"
date: 2023-09-30T22:50:03+00:00
slug: "organic-maps-crowdfunding-and-september-update"
taxonomies:
  news: ["גרסאות"]
---

הודעה קצרה לפני הפרטים על שחרור Organic Maps בספטמבר.
אנו מחפשים מתנדבים שיעזרו לנו בתחומים שונים. הרבה עבודה מעניינת ומאתגרת (האם כבר בדקתם [1800+ בעיות ב-Github](https://github.com/organicmaps/organicmaps/issues/)? 💪) מחכה לכם בדרך הקוד הפתוח, שנבנה על ידי הקהילה, אל המפות הטובות, המהירות 🚀 והקלות לשימוש 👴 👵 🧒, והממוקדות בפרטיות. רוצים [לעזור לנו ](https://organicmaps.app/support-us/) בפיתוח האפליקציה והאתר, בשיווק, ביחסי ציבור, במימון, בתמיכה במשתמשים או בכל דרך אחרת? כתבו לנו ל-hello@organicmaps.app.

אם נגייס מספיק כסף, נוכל להאיץ משמעותית את הפיתוח על ידי העסקת צוות במשרה מלאה ותגמול התורמים הפעילים ביותר. אם נגייס יותר משתמשים, נקבל יותר תרומות. [תרום](https://organicmaps.app/donate/) והפיץ את הבשורה 💸! נקרא לזה **מימון המונים אורגני** 💰

בעדכון של ספטמבר יש כמה תכונות חדשות. אתם יכולים למדוד מרחקים בקלות ולבנות מסלולים בקו ישר באותו אופן שבו אתם בונים מסלולים אחרים, ואפילו יותר פשוט, בלחיצה אחת! קראנו לזה "תכנון מסלול מסוק", אבל אז החלטנו לשנות את השם ל"סרגל" כדי למנוע בלבול.
תכונה חדשה נוספת באנדרואיד היא הנחיות קוליות ברקע. עכשיו Organic Maps יכול לדבר איתכם מהכיס שלכם 🙂 * נתוני מפות OSM חדשים נכון ל-20 בספטמבר * נוסף סוג מסלול חדש "Ruler" (הידוע גם כ-Helicopter Routing) למדידת מרחקים ישרים במהירות, תודה רבה ל-Sergiy [@strump](https://github.com/strump) שהביא אותו לחיים!
* הגדרת מפרידי עשרוניים וקבוצות בהתאם למקם המערכת, תודה ל-Gonzalo [@gpesquero](https://github.com/gpesquero) * הסרת הזום המעצבן במצב תכנון מסלול * כניסות לחניונים ניתנות לחיפוש כעת * שיפור התאמת הרחובות ורלוונטיות התוצאות (תודה ל-Viktar [@vng](https://github.com/vng) על כל השיפורים בחיפוש!)
* חיפוש אחר מוצרי מכולת וכלי בית * ניתן להוסיף מערות בעורך * שיפור בתרגומים לערבית, פולנית וספרדית Android * קול רקע והוראות, תודה ל-Roman [@rtsisyk](https://github.com/rtsisyk) * תיקון תיבת הדו-שיח "המתן..." בעת ההפעלה ב-Android 13 עם מפות רבות שהורדו לכרטיס SD (תודה שוב ל-Viktar!)
* תוקן המרחק בלוח התצוגה המקדימה של המסלול (תודה שוב ל-Sergiy!) * תוקן סמל החץ הכחול בכפתור המיקום במכשירי Android 5 ו-6, תודה ל-Michał [@RicoElectrico](https://github.com/RicoElectrico) * בדיקת קול בתפריט ההגדרות (שוב, תודה ל-Gonzalo!)
* תוקן פרמטר ה-API backurl * אל תעצור את המוזיקה כאשר המסך מסתובב (שוב תודה ל-Roman!) * תוקן באג עם הצבע הבלתי נראה של מסלולי GPX מיובאים iOS * תוקן Open/Closed שהופיע לעיתים בצבע אפור Ferenc [@Ferenc-](https://github.com/Ferenc-) ביצע שיפורים ב-Linux: * הוספת תמיכה במיקום באמצעות GeoClue2
* שימוש ב-OpenGL ES 3.0 במקום OpenGL שולחני עיצוב המפה נעשה בעיקר על ידי קונסטנטין [@pastk](https://github.com/pastk), David [@dvdmrtnz](https://github.com/dvdmrtnz), Harry [@RedAuburn](https://github.com/RedAuburn) ו-[@map-per](https://github.com/map-per):
* סמלים חדשים או מעודכנים עבור מפעל, יקב, ספרייה, בית בושת, תחנת תיקון אופניים, השכרת אופניים, חניון אופניים, סאונה, לוטו, סוכנות הימורים, עיסוי, תפירה, ספרים, חניון תת-קרקעי, חניית נכים, שער, מכירת שקיות לאיסוף צואה, חנות סיטונאית, ישיבה בחוץ, מלאכת יד, טחנת קמח, קייטרינג, מיזוג אוויר, חנות מפתחות ומנעולן. רשימה ארוכה, לא?
* נוספו בדיקת רכב, מרחץ ציבורי, מועדון חשפנות, הימורים, מחסום אופניים, נתיבי מים (ביוב, תעלה, חפיר, שפכים), אקווריום, נקודת כינוס, מרכז משחקים למבוגרים, אולם משחקים, כנסיות מורמוניות, מרכז מבקרים, מכרה תעשייתי, חפצים היסטוריים (תותח, עוגן, אבן, מטוס, טנק, מוקש, הריסות, קטר). רשימה עוד יותר ארוכה!
* נוספו גשרים ומנהרות עבור שבילי אופניים, מדרכות, שבילים, מסילות, שבילי רכיבה, מדרגות * תצוגה שונה של barrier=ditch לעומת waterway=ditch * הופחתה העדיפות של שמות נהרות (וקווים אחרים בעלי חשיבות נמוכה יותר) במצב ניווט * כווננו שמות כבישים ועדיפות של שלטי כביש * תוקנה תצוגת סמלים עבור מבני חניה * הופחתה הנראות של סמלים של חניות קטנות ופרטיות, הוסרה מילוי שטח עבור חניות תת-קרקעיות
* הפחתנו את נראות הידרנטים * הצגנו מספרי בתים מעל סמלים וכיתובים של נקודות עניין עיקריות, ולא הצגנו מספרי בתים עבור מבנים קטנים מדי עבור רמת הזום הנוכחית * לא הצגנו סמלי כוכבים עבור כיכרות * כיוונו את גופן מספרי הבתים ואת סדר העדיפויות של הציור * הוספנו קווי כבישים מהירים להולכי רגל, שבילים לרכיבה על סוסים ושבילי אופניים עבור זום מפורט (z18-) במצב ניווט
* מנהרות להולכי רגל אינן נראות במצב ניווט אנו אסירי תודה לכל מי [עוזר לנו](https://organicmaps.app/support-us/) ו[תורם](https://organicmaps.app/donate/). Organic Maps לא הייתה מתאפשרת ללא המשתמשים והתורמים שלנו ♥️ 🙏 🤟