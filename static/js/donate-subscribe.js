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
      if (decodeURIComponent(pair[0]) === name) return decodeURIComponent(pair[1] || '');
    }
    return null;
  }

  var currencySelect = document.getElementById('currency');
  var customInput = document.getElementById('amount-custom');
  var emailInput = document.getElementById('email');
  var emailWarning = document.getElementById('email-warning');
  var amountError = document.getElementById('amount-error');
  var submitButton = document.getElementById('donate-submit');
  var presetInputs = form.querySelectorAll('input[name="amount"]');
  var intervalInputs = form.querySelectorAll('input[name="interval"]');
  var langInput = form.querySelector('input[name="lang"]');

  // Preset amounts per interval, in EUR-equivalent units. Index 1 is the default.
  var PRESETS = { once: [5, 10, 25, 50], month: [3, 5, 10], year: [25, 35, 70] };
  // Rough units-per-EUR, kept in sync with donate-api config.ts bounds. Precision is
  // irrelevant — this only scales the suggested preset buttons.
  var CURRENCY_FACTOR = {
    EUR: 1, USD: 1, GBP: 1, CHF: 1,
    AED: 4, AUD: 1.5, BRL: 6, CAD: 1.5, CZK: 25, DKK: 7.5, HKD: 8, HUF: 400,
    ILS: 4, ISK: 150, JPY: 150, MXN: 20, MYR: 5, NOK: 11, NZD: 2, PHP: 60,
    PLN: 4, RON: 5, SEK: 11, SGD: 1.5, THB: 40, TWD: 35, ZAR: 20
  };
  var SYMBOLS = {
    EUR: '€', USD: '$', GBP: '£', PLN: 'zł', CAD: '$', AUD: '$', NZD: '$', JPY: '¥',
    SGD: 'S$', CZK: 'Kč', DKK: 'kr', SEK: 'kr', NOK: 'kr', ISK: 'kr', HUF: 'Ft',
    RON: 'lei', ILS: '₪', AED: 'AED', HKD: 'HK$', MXN: 'MX$', MYR: 'RM', PHP: '₱',
    THB: '฿', TWD: 'NT$', ZAR: 'R', BRL: 'R$', CHF: 'CHF'
  };
  // Default currency when the page language implies one and no ?currency= was passed.
  var LANG_CURRENCY = { pl: 'PLN', cs: 'CZK', hu: 'HUF', sv: 'SEK' };

  function selectedInterval() {
    for (var i = 0; i < intervalInputs.length; i++) if (intervalInputs[i].checked) return intervalInputs[i].value;
    return 'once';
  }

  function selectedAmount() {
    var custom = customInput.value.replace(',', '.');
    if (custom !== '' && !isNaN(parseFloat(custom))) return custom;
    for (var i = 0; i < presetInputs.length; i++) if (presetInputs[i].checked) return presetInputs[i].value;
    return '';
  }

  function formatAmount(value, currency) {
    var symbol = SYMBOLS[currency] || currency;
    // Symbol-first for currencies where that is customary, amount-first otherwise.
    if ('€$£₪₱¥'.indexOf(symbol.charAt(0)) !== -1 || symbol === 'HK$' || symbol === 'MX$' ||
        symbol === 'NT$' || symbol === 'S$' || symbol === 'R$' || symbol === 'RM' || symbol === 'R') {
      return symbol + value;
    }
    return value + ' ' + symbol;
  }

  function scalePreset(base, currency) {
    var factor = CURRENCY_FACTOR[currency] || 1;
    var value = base * factor;
    if (factor === 1) return value;
    // Snap scaled presets to friendly figures.
    if (value >= 1000) return Math.round(value / 100) * 100;
    if (value >= 100) return Math.round(value / 10) * 10;
    return Math.round(value);
  }

  function refreshPresets(keepChecked) {
    var interval = selectedInterval();
    var currency = currencySelect.value;
    var presets = PRESETS[interval];
    for (var i = 0; i < presetInputs.length; i++) {
      var input = presetInputs[i];
      var label = form.querySelector('label[for="' + input.id + '"]');
      if (i < presets.length) {
        var value = scalePreset(presets[i], currency);
        input.value = String(value);
        input.hidden = false;
        if (label) {
          label.hidden = false;
          label.textContent = String(value);
        }
      } else {
        input.hidden = true;
        input.checked = false;
        if (label) label.hidden = true;
      }
    }
    if (!keepChecked && customInput.value === '') {
      presetInputs[1].checked = true; // middle preset is the default
    }
  }

  function refreshSubmitLabel() {
    var interval = selectedInterval();
    var amount = selectedAmount();
    if (!amount) return;
    var pattern = submitButton.getAttribute('data-label-' + interval);
    if (pattern) submitButton.textContent = pattern.replace('{amount}', formatAmount(amount, currencySelect.value));
  }

  function refreshEmailWarning() {
    emailWarning.hidden = !(selectedInterval() !== 'once' && emailInput.value.trim() === '');
  }

  function refresh(keepChecked) {
    refreshPresets(keepChecked);
    refreshSubmitLabel();
    refreshEmailWarning();
  }

  // Anti-bot page-load timestamp: humans need more than 3 seconds to fill the form.
  var tsInput = document.createElement('input');
  tsInput.type = 'hidden';
  tsInput.name = 'ts';
  tsInput.value = String(new Date().getTime());
  form.appendChild(tsInput);

  // Prefill from query parameters (the app's place-page buttons link with these).
  var qInterval = queryParam('interval');
  if (qInterval === 'month' || qInterval === 'year' || qInterval === 'once') {
    for (var i = 0; i < intervalInputs.length; i++) intervalInputs[i].checked = intervalInputs[i].value === qInterval;
  }
  var qCurrency = (queryParam('currency') || '').toUpperCase();
  if (!qCurrency && langInput && LANG_CURRENCY[langInput.value]) qCurrency = LANG_CURRENCY[langInput.value];
  if (qCurrency) {
    for (var j = 0; j < currencySelect.options.length; j++) {
      if (currencySelect.options[j].value === qCurrency) currencySelect.value = qCurrency;
    }
  }
  refresh(false);
  var qAmount = queryParam('amount');
  if (qAmount) {
    var matched = false;
    for (var k = 0; k < presetInputs.length; k++) {
      if (!presetInputs[k].hidden && presetInputs[k].value === qAmount) {
        presetInputs[k].checked = true;
        matched = true;
      }
    }
    if (!matched) {
      customInput.value = qAmount;
      for (var m = 0; m < presetInputs.length; m++) presetInputs[m].checked = false;
    }
    refreshSubmitLabel();
  }

  for (var n = 0; n < intervalInputs.length; n++) {
    intervalInputs[n].addEventListener('change', function () {
      refresh(false);
    });
  }
  currencySelect.addEventListener('change', function () {
    refresh(false);
  });
  for (var p = 0; p < presetInputs.length; p++) {
    presetInputs[p].addEventListener('change', function () {
      customInput.value = '';
      amountError.hidden = true;
      refreshSubmitLabel();
    });
  }
  customInput.addEventListener('input', function () {
    if (customInput.value !== '') {
      for (var q = 0; q < presetInputs.length; q++) presetInputs[q].checked = false;
    }
    amountError.hidden = true;
    refreshSubmitLabel();
  });
  emailInput.addEventListener('input', refreshEmailWarning);

  form.addEventListener('submit', function (event) {
    var amount = selectedAmount();
    var value = parseFloat(String(amount).replace(',', '.'));
    if (!amount || isNaN(value) || value <= 0) {
      event.preventDefault();
      amountError.hidden = false;
      customInput.focus();
      return;
    }
    submitButton.disabled = true;
    var loading = submitButton.getAttribute('data-label-loading');
    if (loading) submitButton.textContent = loading;
  });
})();
