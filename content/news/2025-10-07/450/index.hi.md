---
title: "7 अक्टूबर रिलीज़: Android Auto में स्पीड लिमिट, GeoJSON इम्पोर्ट, ट्रैक रिकॉर्डिंग के आँकड़े, OSM description टैग प्रदर्शन, iOS पर चुने गए ट्रैक पर बुकमार्क सहेजना और बहुत कुछ"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["releases"]
---

यह 7 अक्टूबर का Organic Maps अपडेट Android Auto में स्पीड लिमिट प्रदर्शन, GeoJSON इम्पोर्ट और ट्रैक रिकॉर्डिंग के आँकड़े जोड़ता है, OSM description टैग दिखाता है (उन्हें देखने के लिए खोज बॉक्स में `?description` टाइप करो) और iOS पर ट्रैक पर बुकमार्क सहेजता है। सभी प्लेटफ़ॉर्म पर यूज़र इंटरफ़ेस और OpenStreetMap संपादन में कई सुधार तथा कई बग फिक्स भी हैं, जिनमें कुछ Android डिवाइस पर शुरुआत में होने वाले क्रैश का फिक्स शामिल है।

Organic Maps हमारे योगदानकर्ताओं, [तुम्हारे दान](@/donate/index.hi.md) और [तुम्हारे समर्थन](@/contribute/index.hi.md) ❤️ की बदौलत संभव है।

### विस्तृत रिलीज़ नोट्स (पिछले छोटे अपडेट के बदलावों सहित)

- नया! GeoJSON इम्पोर्ट (Sergiy Kozyr)
- 4 अक्टूबर तक का OpenStreetMap डेटा
- 1 अक्टूबर तक का Wikipedia डेटा
- सार्वजनिक परिवहन के लिए Seattle लाइट रेल समर्थन (tjasz)
- संपादित OSM स्थान सहेजते समय मैप चयन निष्क्रिय नहीं होगा (Kiryl Kaveryn)
- अपडेट किए गए अनुवाद (Weblate योगदानकर्ता)

#### मैप स्टाइल

- amenity=bicycle + rental=shop टैग वाली साइकिल किराया दुकानें दिखाना (David Martinez)
- Outdoors स्टाइल में ऐतिहासिक पुरातात्विक स्थल ज़ूम 12 से और अन्य ऐतिहासिक स्थल ज़ूम 15 से दिखाना (Viktor Govako)
- Outdoors स्टाइल में मस्तूल, संचार और बिजली टावरों के लिए नए आइकन (David Martinez)
- Outdoors स्टाइल में चोटी आइकन का आकार बढ़ाया गया (David Martinez)
- छूटे हुए POI आइकन वैरिएंट जोड़े गए (David Martinez)
- और अधिक बैरियर प्रकार जोड़े गए (Viktor Govako)

#### iOS

- नया: चुने गए ट्रैक पॉइंट पर बुकमार्क सहेजना (Kiryl Kaveryn)
- नया: रिकॉर्डिंग ट्रैक को पहले सहेजे बिना हटाना (Kiryl Kaveryn)
- प्लेस पेज में बहु-पंक्ति बुकमार्क सूची शीर्षक दिखाना (David Martinez)
- OSM लॉगिन बटन की स्टाइल अपडेट की गई (Kiryl Kaveryn)
- नेविगेशन जानकारी अपडेट होने की समस्या ठीक की गई (Kiryl Kaveryn)
- नई मार्ग योजना की समस्याएँ ठीक की गईं (Kiryl Kaveryn)
- 3 महीने से पुराने मैप के लिए OSM स्थान जोड़ने/संपादित करने की दृश्यता ठीक की गई (Kiryl Kaveryn)
- iOS 26 के लिए परिवहन विकल्प सेगमेंट कंट्रोल का लेआउट ठीक किया गया (Kiryl Kaveryn)
- बुकमार्क चयन के एनिमेशन सरल किए गए (Kiryl Kaveryn)
- खोज परिणाम चयन की समस्या ठीक की गई (Kiryl Kaveryn)
- प्लेस इनफ़ॉर्मेशन पेज की स्टाइल, स्वाइप और एनिमेशन ठीक किए गए (Kiryl Kaveryn)

#### Android Auto (केवल Google Play)

- नया: Android Auto में स्पीड लिमिट प्रदर्शन (Andrei Shkrob)
- Android Auto नेविगेशन मोड में डिस्प्ले स्विच होने की समस्या ठीक की गई (Andrei Shkrob)
- Android Auto में रूटिंग एरो का ऑफ़सेट ठीक किया गया (Andrei Shkrob)
- डिवाइस के कार से जुड़ने/अलग होने पर आने वाली समस्या ठीक की गई (Andrei Shkrob)
- Android Auto लोकेशन सर्विस जोड़ी गई (Andrei Shkrob)
- Android Auto रूट सिम्युलेटर बेहतर किया गया (Viktor Govako)

#### Android

- नया: ट्रैक रिकॉर्डिंग के आँकड़े रीयल टाइम में देखना (Kavi Khalique)
- नया: OSM `description` टैग की सामग्री दिखाना (Alexander Borsuk)
- थीम बदलने का प्रबंधन ठीक किया गया (Andrei Shkrob)
- शुरुआत में होने वाले क्रैश सहित कई क्रैश ठीक किए गए (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- डाउनलोड प्रगति की सूचनाएँ अब बिना आवाज़ के (Viktor Govako)
- पेंसिल आइकन की पैडिंग कम की गई (Alexander Borsuk)

#### Desktop

- Linux पर अटकने वाला curl ठीक किया गया (Alexander Borsuk)
- OSM में लॉग इन करते समय macOS पर अटकना ठीक किया गया (Alexander Borsuk)
- कॉन्टेक्स्ट मेनू से फ़ीचर चुनने की क्रिया (Viktor Govako)
- डाउनलोड रद्द करने का विकल्प (Viktor Govako)
- कॉन्टेक्स्ट मेनू में ज्यामिति प्रकार दिखाना (Viktor Govako)

### हाल में जारी हुई वे सुविधाएँ जो शायद तुम चूक गए हो

- बस स्टॉप चुनते समय सार्वजनिक परिवहन मार्ग संख्या
- हाइकिंग और साइकिलिंग मार्ग (ऊपर बाएँ Layers बटन से इन्हें चालू करो)
- ऐप सेटिंग्स में चालू करके मैप पर बुकमार्क के नाम देखो
- ✎ पेंसिल आइकन बुकमार्क जल्दी संपादित करने का तरीका देता है

### Organic Maps इंस्टॉल करो

नवीनतम Organic Maps संस्करण [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] और [F-Droid][fdroid] से प्राप्त करो।

शुरुआती सुविधाओं के लिए बीटा परीक्षण में शामिल हो जाओ: [iOS][testflight] / [Android][firebase].

{{ references() }}
