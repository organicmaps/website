// Progressive enhancement for /donate/subscribe/. The form works without this file:
// plain POST to donate-api, which redirects to Mollie hosted checkout.
(function () {
  'use strict';

  var form = document.getElementById('donate-form');
  if (!form) return;

  // URLSearchParams is unavailable in old Android browsers.
  function queryParam(name) {
    var query = window.location.search.substring(1).split('&');
    for (var i = 0; i < query.length; i++) {
      var pair = query[i].split('=');
      try {
        if (decodeURIComponent(pair[0]) === name) return decodeURIComponent((pair[1] || '').replace(/\+/g, ' '));
      } catch (e) {
        // Malformed percent-encoding: skip this parameter instead of aborting the enhancement.
      }
    }
    return null;
  }

  var pageLang = document.documentElement.lang || 'en';
  var currencySelect = document.getElementById('currency');
  var customInput = document.getElementById('amount-custom');
  var emailInput = document.getElementById('email');
  var nameInput = document.getElementById('donor-name');
  var emailWarning = document.getElementById('email-warning');
  var amountError = document.getElementById('amount-error');
  var submitButton = document.getElementById('donate-submit');
  var defaultSubmitLabel = submitButton.textContent;
  var presetInputs = form.querySelectorAll('input[name="amount"]');
  var intervalInputs = form.querySelectorAll('input[name="interval"]');
  var DRAFT_KEY = 'organicmaps-donate-checkout-draft-v2';
  // This limits restoration, not browser storage retention: sessionStorage has no expiry.
  var DRAFT_RESTORE_WINDOW = 30 * 60 * 1000;
  // The preset labels are static markup, so resolve them once instead of re-querying the form
  // on every refresh (interval change, currency change, page load).
  var presetLabels = [];
  for (var i = 0; i < presetInputs.length; i++) {
    presetLabels.push(form.querySelector('label[for="' + presetInputs[i].id + '"]'));
  }

  // Preset amounts per interval, in EUR-equivalent units. Index 1 is the default.
  var PRESETS = { once: [5, 10, 25, 50], month: [3, 5, 10], year: [25, 35, 70] };
  // Per-currency rules mirrored from donate-api config.ts (CURRENCIES): inclusive min/max in
  // major units and the decimals Mollie accepts. `whole` marks a currency the donor may only
  // enter in whole units — PayPal has no sub-unit for HUF or TWD, and Mollie rounds such an
  // amount *up*, so a fraction would charge more than the form promised (TWD is PayPal-only,
  // so there it is every donor). It is a separate flag from `decimals`, which stays 2 for
  // both because that is what Mollie's `value` string carries.
  // `factor` is a rough units-per-EUR that only scales the suggested presets — precision is
  // irrelevant there, and it has no server counterpart. This is a convenience copy, never a
  // second source of truth: donate-api validates every amount again, so drift here only makes
  // the inline range message wrong.
  var CURRENCIES = {
    EUR: { factor: 1, min: 2, max: 10000, decimals: 2 },
    USD: { factor: 1, min: 2, max: 11000, decimals: 2 },
    GBP: { factor: 1, min: 2, max: 9000, decimals: 2 },
    CHF: { factor: 1, min: 2, max: 10000, decimals: 2 },
    AED: { factor: 4, min: 8, max: 40000, decimals: 2 },
    AUD: { factor: 1.5, min: 3, max: 17000, decimals: 2 },
    BRL: { factor: 6, min: 12, max: 60000, decimals: 2 },
    CAD: { factor: 1.5, min: 3, max: 15000, decimals: 2 },
    CZK: { factor: 25, min: 50, max: 250000, decimals: 2 },
    DKK: { factor: 7.5, min: 15, max: 75000, decimals: 2 },
    HKD: { factor: 8, min: 15, max: 85000, decimals: 2 },
    HUF: { factor: 400, min: 800, max: 4000000, decimals: 2, whole: true },
    ILS: { factor: 4, min: 8, max: 40000, decimals: 2 },
    ISK: { factor: 150, min: 300, max: 1500000, decimals: 0 },
    JPY: { factor: 150, min: 300, max: 1600000, decimals: 0 },
    MXN: { factor: 20, min: 40, max: 200000, decimals: 2 },
    MYR: { factor: 5, min: 10, max: 50000, decimals: 2 },
    NOK: { factor: 11, min: 20, max: 115000, decimals: 2 },
    NZD: { factor: 2, min: 3, max: 18000, decimals: 2 },
    PHP: { factor: 60, min: 120, max: 600000, decimals: 2 },
    PLN: { factor: 4, min: 8, max: 45000, decimals: 2 },
    RON: { factor: 5, min: 10, max: 50000, decimals: 2 },
    SEK: { factor: 11, min: 20, max: 115000, decimals: 2 },
    SGD: { factor: 1.5, min: 3, max: 15000, decimals: 2 },
    THB: { factor: 40, min: 75, max: 380000, decimals: 2 },
    TWD: { factor: 35, min: 70, max: 340000, decimals: 2, whole: true },
    ZAR: { factor: 20, min: 40, max: 200000, decimals: 2 }
  };
  // Fallback formatting for engines without Intl.NumberFormat. '#' marks where the amount
  // goes, so placement belongs to the currency rather than to a symbol several currencies
  // share ('$' for USD/CAD/AUD/NZD, 'kr' for DKK/SEK/NOK/ISK).
  var SYMBOLS = {
    EUR: '€#', USD: '$#', GBP: '£#', PLN: '# zł', CAD: '$#', AUD: '$#', NZD: '$#', JPY: '¥#',
    SGD: 'S$#', CZK: '# Kč', DKK: '# kr', SEK: '# kr', NOK: '# kr', ISK: '# kr', HUF: '# Ft',
    RON: '# lei', ILS: '₪#', AED: '# AED', HKD: 'HK$#', MXN: 'MX$#', MYR: 'RM#', PHP: '₱#',
    THB: '฿#', TWD: 'NT$#', ZAR: 'R#', BRL: 'R$#', CHF: '# CHF'
  };
  // Default currency: ?currency=, else the region of the browser's primary language
  // (en-US, de-CH, pt-BR, …), else what the page language implies, else EUR.
  // An ISO 4217 code is its ISO 3166 region plus one letter, so this derives from CURRENCIES
  // and a new currency gets region detection for free. EUR belongs to no single region;
  // Liechtenstein is the one country that uses another's currency here.
  var REGION_CURRENCY = { LI: 'CHF' };
  for (var cur in CURRENCIES) if (cur !== 'EUR') REGION_CURRENCY[cur.slice(0, 2)] = cur;
  // Only where the language names exactly one country, and that country's currency is one
  // Mollie takes. Deliberately absent: ar/de/en/es/fr/nl/pt span several, and the currencies
  // uk/ru/tr/hi/id/fa-IR would imply are not on the list at all.
  var LANG_CURRENCY = { af: 'ZAR', cs: 'CZK', cy: 'GBP', he: 'ILS', hu: 'HUF', ja: 'JPY', pl: 'PLN', sv: 'SEK' };

  // Mirrors donate-api requiresWholeUnits(): zero-decimal currencies, plus the two PayPal
  // rounds up.
  function wholeUnitsOnly(info) {
    return info.decimals === 0 || info.whole === true;
  }

  function selectedInterval() {
    for (var i = 0; i < intervalInputs.length; i++) if (intervalInputs[i].checked) return intervalInputs[i].value;
    return 'once';
  }

  // The custom field wins when it is filled (same precedence as donate-api), so nothing else
  // may stay selected.
  function uncheckPresets() {
    for (var i = 0; i < presetInputs.length; i++) presetInputs[i].checked = false;
  }

  function checkedPreset() {
    for (var i = 0; i < presetInputs.length; i++) if (presetInputs[i].checked) return i;
    return -1;
  }

  // The amount the form would submit: the custom field wins when filled (same precedence as
  // donate-api), otherwise the checked preset. May be invalid text — see parseAmount().
  function selectedAmount() {
    var custom = customInput.value.trim();
    if (custom !== '') return custom;
    var i = checkedPreset();
    return i === -1 ? '' : presetInputs[i].value;
  }

  // First code point of each digit block a donor of this site's languages might type:
  // Arabic-Indic (ar), Extended Arabic-Indic (fa-IR), Devanagari (hi, mr), Telugu, Malayalam.
  var DIGIT_ZEROS = [0x0660, 0x06f0, 0x0966, 0x0c66, 0x0d66];

  // Rewrites any of those digits as 0-9. Intl formats the presets in the donor's own digits —
  // fa-IR shows ۱۰, mr shows १० — so without this the figure on the button is one the custom
  // field would reject. Mirrors latinizeDigits() in donate-api config.ts: the two must accept
  // the same text, so change them together. All five blocks are BMP, hence charCodeAt.
  function latinizeDigits(text) {
    var out = '';
    for (var i = 0; i < text.length; i++) {
      var cp = text.charCodeAt(i);
      var digit = null;
      for (var j = 0; j < DIGIT_ZEROS.length; j++) {
        if (cp >= DIGIT_ZEROS[j] && cp <= DIGIT_ZEROS[j] + 9) {
          digit = String(cp - DIGIT_ZEROS[j]);
          break;
        }
      }
      out += digit === null ? text.charAt(i) : digit;
    }
    return out;
  }

  // Mirrors donate-api parseAmount(): "4.99", "4,99", "10", the same in the donor's own
  // digits; NaN for anything else. U+066B is the Arabic decimal separator, the ٫ in ۷٫۵۰.
  // Group separators stay rejected in every script, exactly as on the server.
  function parseAmount(text) {
    var cleaned = latinizeDigits(String(text).trim()).replace('\u066B', '.').replace(',', '.');
    return /^\d{1,7}(\.\d{1,2})?$/.test(cleaned) ? parseFloat(cleaned) : NaN;
  }

  // Building an Intl.NumberFormat costs far more than formatting with one, and every visible
  // preset plus the submit label is reformatted on each refresh — so keep one formatter per
  // (currency, fraction digits). A cached null means this engine rejected that pair: the
  // fallback below handles it and we never retry the constructor.
  var formatters = {};

  function formatAmount(num, currency) {
    var whole = num % 1 === 0;
    if (window.Intl && typeof window.Intl.NumberFormat === 'function') {
      var key = currency + (whole ? '|0' : '|2');
      var formatter = formatters[key];
      if (formatter === undefined) {
        try {
          formatter = new window.Intl.NumberFormat(pageLang, {
            style: 'currency',
            currency: currency,
            minimumFractionDigits: whole ? 0 : 2,
            maximumFractionDigits: 2
          });
        } catch (e) {
          formatter = null; // Locale or currency unknown to this engine.
        }
        formatters[key] = formatter;
      }
      if (formatter) return formatter.format(num);
    }
    var text = whole ? String(num) : num.toFixed(2);
    return (SYMBOLS[currency] || '# ' + currency).replace('#', text);
  }

  function scalePreset(base, currency) {
    var factor = (CURRENCIES[currency] || CURRENCIES.EUR).factor;
    var value = base * factor;
    if (factor === 1) return value;
    // Snap scaled presets to friendly figures.
    if (value >= 1000) return Math.round(value / 100) * 100;
    if (value >= 100) return Math.round(value / 10) * 10;
    return Math.round(value);
  }

  function refreshPresets() {
    var presets = PRESETS[selectedInterval()];
    var currency = currencySelect.value;
    var keep = checkedPreset();
    for (var i = 0; i < presetInputs.length; i++) {
      var input = presetInputs[i];
      var label = presetLabels[i];
      var visible = i < presets.length;
      input.hidden = !visible;
      if (label) label.hidden = !visible;
      if (visible) {
        var value = scalePreset(presets[i], currency);
        input.value = String(value);
        if (label) label.textContent = formatAmount(value, currency);
      } else {
        input.checked = false;
      }
    }
    // Keep the donor's pick across currency/interval changes; otherwise the middle preset.
    if (customInput.value.trim() === '') {
      presetInputs[keep >= 0 && keep < presets.length ? keep : 1].checked = true;
    }
  }

  function refreshPlaceholder() {
    // scalePreset leaves 7.5 alone for the 1:1 currencies and snaps it to an integer elsewhere.
    var example = scalePreset(7.5, currencySelect.value);
    customInput.placeholder = example % 1 === 0 ? String(example) : example.toFixed(2);
    // Offer the keyboard that matches what will be accepted: no decimal separator where a
    // fraction would only be rejected.
    var info = CURRENCIES[currencySelect.value] || CURRENCIES.EUR;
    customInput.setAttribute('inputmode', wholeUnitsOnly(info) ? 'numeric' : 'decimal');
  }

  function refreshSubmitLabel() {
    var num = parseAmount(selectedAmount());
    var pattern = submitButton.getAttribute('data-label-' + selectedInterval());
    submitButton.textContent =
      isNaN(num) || !pattern ? defaultSubmitLabel : pattern.replace('{amount}', formatAmount(num, currencySelect.value));
  }

  function refreshEmailWarning() {
    var show = selectedInterval() !== 'once' && emailInput.value.trim() === '';
    emailWarning.hidden = !show;
    // Hidden elements referenced by aria-describedby are still read out, so only reference
    // the warning while it is shown.
    emailInput.setAttribute('aria-describedby', show ? 'email-why email-warning' : 'email-why');
  }

  function showAmountError(message) {
    amountError.textContent = message;
    amountError.hidden = false;
  }

  // Emptied, not merely hidden: #amount-custom describes itself with this element, and a hidden
  // element referenced by aria-describedby is still read out as the field's description — so a
  // message left behind would follow the field around for the rest of the visit.
  function hideAmountError() {
    amountError.textContent = '';
    amountError.hidden = true;
  }

  // Client-side mirror of donate-api's amount validation, so an out-of-range amount is reported
  // inline instead of on the API's error page (which loses the form).
  function validateAmount() {
    var currency = currencySelect.value;
    var info = CURRENCIES[currency] || CURRENCIES.EUR;
    var num = parseAmount(selectedAmount());
    var invalid = amountError.getAttribute('data-invalid') || '';
    if (isNaN(num) || (wholeUnitsOnly(info) && num % 1 !== 0)) {
      showAmountError(invalid);
      return false;
    }
    if (num < info.min || num > info.max) {
      showAmountError(
        (amountError.getAttribute('data-range') || invalid)
          .replace('{min}', formatAmount(info.min, currency))
          .replace('{max}', formatAmount(info.max, currency))
      );
      return false;
    }
    hideAmountError();
    return true;
  }

  function refresh() {
    refreshPresets();
    refreshPlaceholder();
    refreshSubmitLabel();
    refreshEmailWarning();
  }

  function hasCurrency(code) {
    for (var i = 0; i < currencySelect.options.length; i++) if (currencySelect.options[i].value === code) return true;
    return false;
  }

  function regionCurrency() {
    // Primary language only: the region of a secondary language says little about the donor.
    var parts = String(navigator.language || '').split(/[-_]/);
    // The region may follow a script subtag (zh-Hant-TW).
    for (var i = 1; i < parts.length; i++) {
      var code = parts[i].toUpperCase();
      if (code.length === 2 && REGION_CURRENCY[code]) return REGION_CURRENCY[code];
    }
    return null;
  }

  // A canceled Mollie checkout returns with a fixed marker. Restore the draft within this
  // tab, then consume it; no donor-entered values need to travel in the return URL. Remove
  // expired drafts on any form visit, since sessionStorage does not expire entries itself.
  var returnDraft = null;
  var canceledCheckout = queryParam('checkout') === 'canceled';
  try {
    var savedDraft = sessionStorage.getItem(DRAFT_KEY);
    if (savedDraft) {
      var parsedDraft = JSON.parse(savedDraft);
      var restorable = parsedDraft && typeof parsedDraft.expiresAt === 'number' && parsedDraft.expiresAt > Date.now();
      if (!restorable || canceledCheckout) sessionStorage.removeItem(DRAFT_KEY);
      if (restorable && canceledCheckout) returnDraft = parsedDraft;
    }
  } catch (e) {
    // Malformed data or disabled storage must not break the form.
    try { sessionStorage.removeItem(DRAFT_KEY); } catch (ignored) {}
  }

  // Ordinary links still prefill from query parameters (the app's place-page buttons use these).
  var qInterval = queryParam('interval');
  if (returnDraft && typeof returnDraft.interval === 'string') qInterval = returnDraft.interval;
  // Public links may use the human-readable names; the form and API use month/year.
  if (qInterval === 'monthly') qInterval = 'month';
  if (qInterval === 'yearly') qInterval = 'year';
  if (qInterval === 'month' || qInterval === 'year' || qInterval === 'once') {
    for (var i = 0; i < intervalInputs.length; i++) intervalInputs[i].checked = intervalInputs[i].value === qInterval;
  }
  var qCurrency = queryParam('currency') || '';
  if (returnDraft && typeof returnDraft.currency === 'string') qCurrency = returnDraft.currency;
  qCurrency = qCurrency.toUpperCase();
  var defaultCurrency = hasCurrency(qCurrency) ? qCurrency : regionCurrency() || LANG_CURRENCY[pageLang] || 'EUR';
  // REGION_CURRENCY follows CURRENCIES, which mirrors the server, but the <select> is the only
  // list this form can actually submit — never assign a code it does not offer.
  if (hasCurrency(defaultCurrency)) currencySelect.value = defaultCurrency;
  refresh();
  var qAmount = queryParam('amount');
  if (returnDraft && typeof returnDraft.amount === 'string') qAmount = returnDraft.amount;
  if (qAmount) {
    var preset = null;
    for (var i = 0; i < presetInputs.length; i++) {
      if (!presetInputs[i].hidden && presetInputs[i].value === qAmount) preset = presetInputs[i];
    }
    // Checking a radio clears the rest of its group, so one assignment covers either branch.
    if (preset) preset.checked = true;
    else {
      customInput.value = qAmount;
      uncheckPresets();
    }
    refreshSubmitLabel();
  }

  if (returnDraft) {
    if (typeof returnDraft.email === 'string' && returnDraft.email) emailInput.value = returnDraft.email;
    if (typeof returnDraft.name === 'string' && returnDraft.name) nameInput.value = returnDraft.name;
    refreshEmailWarning();
  }

  function onPresetChange() {
    customInput.value = '';
    hideAmountError();
    refreshSubmitLabel();
  }

  for (var i = 0; i < intervalInputs.length; i++) intervalInputs[i].addEventListener('change', refresh);
  for (var i = 0; i < presetInputs.length; i++) presetInputs[i].addEventListener('change', onPresetChange);
  currencySelect.addEventListener('change', function () {
    refresh();
    // A range error on screen refers to the previous currency's bounds.
    if (!amountError.hidden) validateAmount();
  });
  customInput.addEventListener('input', function () {
    if (customInput.value.trim() !== '') uncheckPresets();
    else if (checkedPreset() === -1) presetInputs[1].checked = true; // never leave nothing chosen
    hideAmountError();
    refreshSubmitLabel();
  });
  emailInput.addEventListener('input', refreshEmailWarning);

  form.addEventListener('submit', function (event) {
    if (!validateAmount()) {
      event.preventDefault();
      customInput.focus();
      return;
    }
    try {
      sessionStorage.setItem(
        DRAFT_KEY,
        JSON.stringify({
          amount: selectedAmount(),
          interval: selectedInterval(),
          currency: currencySelect.value,
          email: emailInput.value,
          name: nameInput.value,
          expiresAt: Date.now() + DRAFT_RESTORE_WINDOW
        })
      );
    } catch (e) {
      // Storage can be disabled; checkout still works without draft restoration.
    }
    submitButton.disabled = true;
    var loading = submitButton.getAttribute('data-label-loading');
    if (loading) submitButton.textContent = loading;
  });

  // "Back" from Mollie restores the page from the back/forward cache with the button still
  // disabled and labelled "Redirecting…"; make the form usable again.
  window.addEventListener('pageshow', function (event) {
    if (event.persisted) {
      submitButton.disabled = false;
      refreshSubmitLabel();
    }
  });
})();
