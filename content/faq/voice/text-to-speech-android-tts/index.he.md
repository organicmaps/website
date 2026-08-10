---
title: טקסט-לדיבור (TTS) והנחיות קוליות באנדרואיד
description: "מדריך להגדרת הוראות קוליות TTS באנדרואיד"
slug: text-to-speech-tts-and-voice-directions-on-android
taxonomies:
  faq: ["קול"]
extra:
  order: 10
---

## סיכום

Organic Maps משתמשת במנוע הטקסט-לדיבור (TTS) של המערכת להוראות קוליות. מנועי ברירת המחדל משתנים ממכשיר למכשיר. הבחירות יכולות לכלול את Google Text-to Speech, מנוע של יצרן המכשיר או צד שלישי.

ההמלצה הרשמית מ-Organic Maps היא [RHVoice](https://rhvoice.org/), שהיא מנוע דיבור חופשי ובקוד פתוח שניתן להוריד מ-[Google Play](https://play.google.com/store/apps/details?id=com.github.olga_yakovleva.rhvoice.android) ו-[F-Droid](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/).

## הוראות

- פתחו את אפליקציית ההגדרות במכשיר האנדרואיד שלכם
- בחרו הגדרות נוספות (Additional Settings) ואז בחרו נגישות (Accessibility)
- בחרו את המנוע המועדף עליכם, קצב הדיבור והגובה
- **הפעילו מחדש את אפליקציית Organic Maps**
- פתחו הגדרות => הוראות קוליות ב-Organic Maps והגדירו זאת
- הפעילו מחדש את אפליקציית Organic Maps שוב (או אתחלו את המכשיר) אם הקול לא עובד

אם אינכם מוצאים את ההגדרה הרלוונטית, פתחו את אפליקציית ההגדרות וחפשו Text-to-speech.

נ.ב: שימו לב וצעדים אלה ישתנו בהתאם למותג הטלפון בו אתם משתמשים.

האפשרויות האמורות עשויות שלא להופיע אם אין לכם TTS מותקן כבר במכשיר. אנא עיינו בטבלה למטה להתקנת אחד התומך בשפת האם שלכם.

## צילומי מסך

|             |             |
| ----------- | ----------- |
![Settings](tts_config_1.png "Settings") | ![Accessibility](tts_config_2.png "Accessibility")

## מנועים {#engines}

להלן רשימה מקיפה המציגה מספר מנועים והשפות בהן הם תומכים (קישורי ההורדה מופיעים לאחר הטבלה):

{{ tts_table() }}

## פתרונות עוקפים

אם אתם נתקלים בבעיות באתחול מנוע ה-TTS של RHVoice ב-LineageOS או בגרסאות ROM מותאמות אישית אחרות, נסו את הפתרון העוקף הזה. ייתכן ש-RHVoice לא יאותחל כהלכה והאפליקציה עלולה לקרוס, במיוחד אם לא השתמשתם בעבר במנוע TTS כלשהו בטלפון שלכם (למשל, התקנה חדשה, איפוס להגדרות היצרן וכו'). אם אתם משתמשים ב-ROM מותאם אישית כמו LineageOS <ins>ללא שירותי Google Play וללא Speech Services by Google</ins>, ואתם רוצים להשתמש ב-RHVoice כמנוע ה-TTS המועדף עליכם, עקבו אחר ההוראות שלהלן כפתרון עוקף:

1. התקינו את [מנוע ה-TTS eSpeak](https://f-droid.org/en/packages/com.reecedunn.espeak) הזמין ב-F-Droid
2. הגדירו אותו כמנוע המערכת המועדף
    - עברו אל **ההגדרות** הראשיות (Settings) של LineageOS.
    - גללו מטה אל **נגישות** (Accessibility).
    - בחרו **פלט טקסט-לדיבור** (text-to-speech output) ולאחר מכן **מנוע מועדף** (Preferred engine, בצד שמאל), וודאו ש-**eSpeak** נבחר.
3. חזרו אחורה ולחצו על **הפעלה** (play) כדי לבדוק אם זה עובד
4. התקינו את [RHVoice](https://f-droid.org/en/packages/com.github.olga_yakovleva.rhvoice.android/) הזמין ב-F-Droid.
    - פתחו אותו, בחרו את השפה שבה תרצו להשתמש, הקישו על סמל הענן (בקצה השמאלי) כדי להוריד קולות.
    - לחצו על כפתור ההפעלה כדי לוודא שזה עובד
5. הגדירו את **RHVoice** כמנוע המועדף (ראו שלב 2)
6. כעת אתם אמורים להיות מסוגלים להשתמש ב-RHVoice ללא בעיות

## בדיקה

כדי לבדוק את ההוראות הקוליות, אתם יכולים להקיש על "Test Voice Directions (TTS, Text-To-Speech)" בתפריט "הגדרות → הוראות קוליות" ב-OM או שאתם יכולים להתחיל ניווט בפועל לקבלת פלט קולי כלשהו. Organic Maps לא תיתן לכם הוראות קוליות בזמן שאתם עומדים במקום.

![TTS Test](tts_test.png "TTS Test")
