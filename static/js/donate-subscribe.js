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

  // Subscriptions are limited to these currencies (kept in sync with donate-api config.ts).
  var SUB_CURRENCIES = ['EUR', 'USD', 'GBP'];
  // Preset amounts per interval, scaled per currency below. Index 1 is the default.
  var PRESETS = { once: [5, 10, 25, 50], month: [3, 5, 10], year: [25, 35, 70] };
  var CURRENCY_FACTOR = { JPY: 100, PLN: 4 };
  var NO_DECIMALS = { JPY: true };
  var SYMBOLS = { EUR: '€', USD: '$', GBP: '£', PLN: 'zł', CAD: '$', AUD: '$', NZD: '$', JPY: '¥', SGD: '$' };

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
    return currency === 'JPY' || currency === 'PLN' ? value + ' ' + symbol : symbol + value;
  }

  function refreshPresets(keepChecked) {
    var interval = selectedInterval();
    var currency = currencySelect.value;
    var factor = CURRENCY_FACTOR[currency] || 1;
    var presets = PRESETS[interval];
    for (var i = 0; i < presetInputs.length; i++) {
      var input = presetInputs[i];
      var label = form.querySelector('label[for="' + input.id + '"]');
      if (i < presets.length) {
        var value = presets[i] * factor;
        if (NO_DECIMALS[currency]) value = Math.round(value);
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

  function refreshCurrencies() {
    var interval = selectedInterval();
    var subscription = interval !== 'once';
    for (var i = 0; i < currencySelect.options.length; i++) {
      var option = currencySelect.options[i];
      var onceOnly = option.hasAttribute('data-once-only');
      option.disabled = subscription && onceOnly;
      option.hidden = subscription && onceOnly;
    }
    if (subscription && SUB_CURRENCIES.indexOf(currencySelect.value) === -1) currencySelect.value = 'EUR';
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
    refreshCurrencies();
    refreshPresets(keepChecked);
    refreshSubmitLabel();
    refreshEmailWarning();
  }

  // Prefill from query parameters (the app's place-page buttons link with these).
  var qInterval = queryParam('interval');
  if (qInterval === 'month' || qInterval === 'year' || qInterval === 'once') {
    for (var i = 0; i < intervalInputs.length; i++) intervalInputs[i].checked = intervalInputs[i].value === qInterval;
  }
  var qCurrency = (queryParam('currency') || '').toUpperCase();
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
