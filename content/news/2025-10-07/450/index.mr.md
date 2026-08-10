---
title: "७ ऑक्टोबर प्रकाशन: Android Auto मध्ये वेग मर्यादा, GeoJSON आयात, ट्रॅक रेकॉर्डिंगची आकडेवारी, OSM description टॅग प्रदर्शन, iOS वर निवडलेल्या ट्रॅकवर बुकमार्क जतन करणे आणि बरेच काही"
date: 2025-10-07T07:20:28+00:00
slug: "android-auto-speed-limit-geojson-support-recording-track-statistics-osm-description-display"
taxonomies:
  news: ["releases"]
---

हे ७ ऑक्टोबरचे Organic Maps अपडेट Android Auto मध्ये वेग मर्यादा प्रदर्शन, GeoJSON आयात आणि ट्रॅक रेकॉर्डिंगची आकडेवारी जोडते, OSM description टॅग दाखवते (ते पाहण्यासाठी शोध बॉक्समध्ये `?description` टाइप करा) आणि iOS वर ट्रॅकवर बुकमार्क जतन करते. सर्व प्लॅटफॉर्मवर वापरकर्ता इंटरफेस आणि OpenStreetMap संपादनामध्ये अनेक सुधारणा तसेच विविध बग दुरुस्त्या आहेत, ज्यात काही Android डिव्हाइसवर सुरुवातीला होणाऱ्या क्रॅशची दुरुस्ती समाविष्ट आहे.

Organic Maps आमच्या योगदानकर्त्यांमुळे, [तुमच्या देणग्यांमुळे](@/donate/index.mr.md) आणि [तुमच्या पाठिंब्यामुळे](@/contribute/index.mr.md) ❤️ शक्य झाले आहे.

### सविस्तर प्रकाशन टिपा (मागील छोट्या अपडेटमधील बदलांसह)

- नवीन! GeoJSON आयात (Sergiy Kozyr)
- ४ ऑक्टोबरपर्यंतचा OpenStreetMap डेटा
- १ ऑक्टोबरपर्यंतचा Wikipedia डेटा
- सार्वजनिक वाहतुकीसाठी Seattle लाइट रेल समर्थन (tjasz)
- संपादित केलेले OSM ठिकाण जतन करताना नकाशा निवड निष्क्रिय न करणे (Kiryl Kaveryn)
- अद्ययावत अनुवाद (Weblate योगदानकर्ते)

#### नकाशा शैली

- amenity=bicycle + rental=shop असे टॅग केलेली सायकल भाड्याची दुकाने दाखवणे (David Martinez)
- Outdoors शैलीमध्ये ऐतिहासिक पुरातत्त्व स्थळे झूम १२ पासून आणि इतर ऐतिहासिक स्थळे झूम १५ पासून दाखवणे (Viktor Govako)
- Outdoors शैलीमध्ये मास्ट, दळणवळण आणि वीज मनोऱ्यांसाठी नवीन आयकॉन (David Martinez)
- Outdoors शैलीमध्ये शिखर आयकॉनचा आकार वाढवला (David Martinez)
- गहाळ POI आयकॉन प्रकार जोडले (David Martinez)
- आणखी अडथळ्यांचे प्रकार जोडले (Viktor Govako)

#### iOS

- नवीन: निवडलेल्या ट्रॅक बिंदूवर बुकमार्क जतन करणे (Kiryl Kaveryn)
- नवीन: रेकॉर्डिंग ट्रॅक आधी जतन न करता हटवणे (Kiryl Kaveryn)
- ठिकाण पृष्ठावर बहु-ओळी बुकमार्क यादी शीर्षके दाखवणे (David Martinez)
- OSM लॉगिन बटणांची शैली अद्ययावत केली (Kiryl Kaveryn)
- नेव्हिगेशन माहिती अद्ययावत होण्याची समस्या दुरुस्त केली (Kiryl Kaveryn)
- नवीन मार्ग नियोजनातील समस्या दुरुस्त केल्या (Kiryl Kaveryn)
- ३ महिन्यांपेक्षा जुन्या नकाशांसाठी OSM ठिकाण जोडण्याची/संपादित करण्याची दृश्यमानता दुरुस्त केली (Kiryl Kaveryn)
- iOS 26 साठी वाहतूक पर्याय सेगमेंट कंट्रोलची मांडणी दुरुस्त केली (Kiryl Kaveryn)
- बुकमार्क निवडीची ॲनिमेशन सोपी केली (Kiryl Kaveryn)
- शोध परिणाम निवडीची समस्या दुरुस्त केली (Kiryl Kaveryn)
- ठिकाण माहिती पृष्ठाची शैली, स्वाइप आणि ॲनिमेशन दुरुस्त केली (Kiryl Kaveryn)

#### Android Auto (फक्त Google Play)

- नवीन: Android Auto मध्ये वेग मर्यादा प्रदर्शन (Andrei Shkrob)
- Android Auto नेव्हिगेशन मोडमध्ये डिस्प्ले बदलण्याची समस्या दुरुस्त केली (Andrei Shkrob)
- Android Auto मध्ये मार्गदर्शक बाणाचा ऑफसेट दुरुस्त केला (Andrei Shkrob)
- डिव्हाइस कारला जोडले/तोडले जाते तेव्हाची समस्या दुरुस्त केली (Andrei Shkrob)
- Android Auto लोकेशन सेवा जोडली (Andrei Shkrob)
- Android Auto मार्ग सिम्युलेटर सुधारला (Viktor Govako)

#### Android

- नवीन: ट्रॅक रेकॉर्डिंगची आकडेवारी रिअल टाइममध्ये पाहणे (Kavi Khalique)
- नवीन: OSM `description` टॅगमधील मजकूर दाखवणे (Alexander Borsuk)
- थीम बदलाची हाताळणी दुरुस्त केली (Andrei Shkrob)
- सुरुवातीच्या क्रॅशसह अनेक क्रॅश दुरुस्त केले (Andrei Shkrob, Viktor Govako, Alexander Borsuk)
- डाउनलोड प्रगतीच्या सूचना आता आवाजाशिवाय (Viktor Govako)
- पेन्सिल आयकॉनचे पॅडिंग कमी केले (Alexander Borsuk)

#### Desktop

- Linux वर अडकणारा curl दुरुस्त केला (Alexander Borsuk)
- OSM मध्ये लॉग इन करताना macOS वर अडकणे दुरुस्त केले (Alexander Borsuk)
- संदर्भ मेनूमधून वस्तू निवडण्याची क्रिया (Viktor Govako)
- डाउनलोड रद्द करण्याचा पर्याय (Viktor Govako)
- संदर्भ मेनूमध्ये भूमिती प्रकार दाखवणे (Viktor Govako)

### अलीकडे प्रकाशित झालेली वैशिष्ट्ये जी तुमच्या नजरेतून सुटली असतील

- बस थांबा निवडताना सार्वजनिक वाहतूक मार्ग क्रमांक
- भटकंती आणि सायकल मार्ग (वरच्या डाव्या कोपऱ्यातील लेअर्स बटणाने ते चालू करा)
- ॲप सेटिंग्जमध्ये चालू करून नकाशावर बुकमार्कची नावे पहा
- ✎ पेन्सिल आयकॉन बुकमार्क पटकन संपादित करण्याचा जलद मार्ग देते

### Organic Maps इंस्टॉल करा

नवीनतम Organic Maps आवृत्ती [App Store][appstore], [Google Play][googleplay], [Huawei AppGallery][appgallery], [Obtainium][obtainium], [Accrescent][accrescent] आणि [F-Droid][fdroid] वरून मिळवा.

लवकर वैशिष्ट्ये मिळवण्यासाठी बीटा चाचणीत सामील व्हा: [iOS][testflight] / [Android][firebase].

{{ references() }}
