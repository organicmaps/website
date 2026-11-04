// Exercise the rendered checkout with real browser form submission. All requests
// are fulfilled locally so these tests cannot contact a payment service.
const { test, before, after } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const { spawnSync } = require('node:child_process');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const output = path.join(root, 'public');
const origin = 'https://donation.test';
const draftKey = 'organicmaps-donate-checkout-draft-v2';
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg' };
const headerRules = [];
let rule;
for (const line of fs.readFileSync(path.join(root, 'static/_headers'), 'utf8').split('\n')) {
  if (!line.trim() || line.startsWith('#')) continue;
  if (!/^\s/.test(line)) {
    const pattern = line.replace(/[.+?^${}()|[\]\\]/g, '\\$&').replaceAll('*', '.*').replace(':lang', '[^/]+');
    rule = { pattern: new RegExp('^' + pattern + '$'), headers: {} };
    headerRules.push(rule);
  } else {
    const [, key, value] = line.match(/^\s+([^:]+):\s*(.*)$/);
    rule.headers[key.toLowerCase()] = value;
  }
}

function headersFor(pathname) {
  return Object.assign({}, ...headerRules.filter(r => r.pattern.test('https://organicmaps.app' + pathname)).map(r => r.headers));
}

let browser;
before(async () => {
  assert.ok(fs.existsSync(path.join(output, 'donate/index.html')), 'Run zola build before npm run test:browser');
  browser = await chromium.launch();
});
after(async () => { if (browser) await browser.close(); });

async function openPage(t, options = {}) {
  const { cancelPath, ...browserOptions } = options;
  const context = await browser.newContext({ locale: 'en-US', ...browserOptions });
  const posted = [];
  const unexpected = [];
  const errors = [];
  await context.route('**/*', async route => {
    const request = route.request();
    const url = new URL(request.url());
    if (url.hostname === 'donate-api.organicmaps.app' || url.hostname === 'www.paypal.com') {
      posted.push({ host: url.hostname, method: request.method(), fields: Object.fromEntries(new URLSearchParams(request.postData())) });
      // Playwright routes only the first request in an HTTP redirect chain.
      // Represent checkout with a document and link so every navigation is mocked.
      const body = url.hostname === 'www.paypal.com' ? '<p>Mock PayPal</p>'
        : '<p>Mock checkout</p>' + (cancelPath ? `<a id="mock-cancel" href="${origin + cancelPath}">Cancel</a>` : '');
      return route.fulfill({ contentType: 'text/html', body });
    }
    if (url.origin !== origin) {
      unexpected.push(url.href);
      return route.abort();
    }
    const file = path.join(output, decodeURIComponent(url.pathname), url.pathname.endsWith('/') ? 'index.html' : '');
    if (!fs.existsSync(file)) return route.fulfill({ status: 404, body: 'Not found' });
    return route.fulfill({ body: fs.readFileSync(file), contentType: mime[path.extname(file)] || 'application/octet-stream', headers: headersFor(url.pathname) });
  });
  const page = await context.newPage();
  page.on('pageerror', error => errors.push(error.message));
  t.after(async () => {
    await context.close();
    assert.deepEqual(unexpected, [], 'Unexpected external requests');
    assert.deepEqual(errors, [], 'Browser errors');
  });
  return { page, posted };
}

function fields(page) {
  return page.locator('#donate-form').evaluate(form => Object.fromEntries(new FormData(form)));
}

test('app links prefill preset and custom amounts; returning to a preset clears custom state', { timeout: 30000 }, async t => {
  const { page } = await openPage(t);
  await page.goto(origin + '/donate/subscribe/?amount=7.5&interval=monthly&currency=CHF');
  assert.equal((await fields(page)).amount_custom, '7.5');
  assert.equal((await fields(page)).interval, 'month');
  assert.equal((await fields(page)).currency, 'CHF');
  assert.equal(await page.locator('#donate-custom-row').isVisible(), true);
  await page.locator('label[for="amount-2"]').click();
  assert.equal((await fields(page)).amount_custom, '');
  assert.equal(await page.locator('#donate-custom-row').isVisible(), false);
  await page.goto(origin + '/donate/subscribe/?amount=50&interval=yearly&currency=eur');
  assert.equal((await fields(page)).amount, '50');
  assert.equal((await fields(page)).interval, 'year');
  assert.equal(await page.locator('#donate-custom-row').isVisible(), false);
});

test('custom amounts validate inline, including blank and native digits', { timeout: 30000 }, async t => {
  const { page, posted } = await openPage(t);
  await page.goto(origin + '/donate/?currency=EUR');
  await page.locator('#amount-other').click();
  await page.locator('#donate-submit').click();
  assert.equal(await page.locator('#amount-error').isVisible(), true);
  assert.equal(await page.locator('#amount-custom').evaluate(e => e === document.activeElement), true);
  await page.locator('#amount-custom').fill('٧٫٥٠');
  assert.match(await page.locator('#donate-submit').textContent(), /€7\.50/);
  await page.selectOption('#currency', 'JPY');
  await page.locator('#donate-submit').click();
  assert.equal(await page.locator('#amount-error').isVisible(), true);
  assert.deepEqual(posted, []);
  await page.selectOption('#currency', 'EUR');
  assert.equal(await page.locator('#amount-error').isVisible(), false);
  await page.locator('label[for="interval-once"]').click();
  assert.equal(await page.locator('#email-warning').isVisible(), false);
  await page.locator('label[for="interval-month"]').click();
  assert.equal(await page.locator('#email-warning').isVisible(), true);
});

test('canceled checkout restores the submitted draft once without donor data in its URL', { timeout: 30000 }, async t => {
  const cancelPath = '/de/donate/?checkout=canceled#donation';
  const { page, posted } = await openPage(t, { cancelPath });
  await page.goto(origin + '/de/donate/?amount=7.5&interval=monthly&currency=CHF');
  await page.locator('#email').fill('donor@example.invalid');
  await page.locator('#donor-name').fill('Test Donor');
  const submitted = await fields(page);
  await Promise.all([page.waitForURL('https://donate-api.organicmaps.app/checkout'), page.locator('#donate-submit').click()]);
  await Promise.all([page.waitForURL(origin + cancelPath), page.locator('#mock-cancel').click()]);
  assert.deepEqual(posted[0], { host: 'donate-api.organicmaps.app', method: 'POST', fields: submitted });
  assert.deepEqual(await fields(page), submitted);
  assert.equal(await page.locator('#donate-canceled').isVisible(), true);
  assert.equal(await page.locator('#donate-custom-row').isVisible(), true);
  assert.equal(await page.locator('#donate-submit').isEnabled(), true);
  assert.equal(await page.evaluate(key => sessionStorage.getItem(key), draftKey), null);
});

test('malformed and expired drafts do not break a cancellation return', { timeout: 30000 }, async t => {
  for (const draft of ['{broken', JSON.stringify({ amount: '999', expiresAt: 1 })]) {
    const { page } = await openPage(t);
    await page.addInitScript(({ key, value }) => sessionStorage.setItem(key, value), { key: draftKey, value: draft });
    await page.goto(origin + '/donate/?checkout=canceled');
    assert.equal((await fields(page)).amount, '35');
    assert.equal(await page.locator('#donate-submit').isEnabled(), true);
    assert.equal(await page.evaluate(key => sessionStorage.getItem(key), draftKey), null);
  }
});

test('without JavaScript, presets and custom amounts submit one consistent EUR currency', { timeout: 30000 }, async t => {
  const { page, posted } = await openPage(t, { javaScriptEnabled: false });
  await page.goto(origin + '/donate/');
  assert.equal(await page.locator('#currency').isDisabled(), true);
  assert.equal((await fields(page)).currency, 'EUR');
  assert.deepEqual(await page.locator('#donate-form').evaluate(form => new FormData(form).getAll('currency')), ['EUR']);
  assert.equal(await page.locator('#donate-custom-row').isVisible(), true);
  await page.locator('#amount-custom').fill('7.50');
  await page.locator('label[for="interval-once"]').click();
  await Promise.all([page.waitForURL('https://donate-api.organicmaps.app/checkout'), page.locator('#donate-submit').click()]);
  assert.equal(posted[0].fields.currency, 'EUR');
  assert.equal(posted[0].fields.amount_custom, '7.50');
  assert.equal(posted[0].fields.interval, 'once');
});

test('all languages render both landing pages; fragments reveal payment details', { timeout: 60000 }, async t => {
  const { page } = await openPage(t);
  const langs = ['en', ...fs.readdirSync(path.join(root, 'content/donate')).filter(n => /^index\..+\.md$/.test(n)).map(n => n.slice(6, -3))];
  for (const lang of langs) {
    const prefix = lang === 'en' ? '' : '/' + lang;
    for (const endpoint of ['/donate/', '/donate/subscribe/']) {
      await page.goto(origin + prefix + endpoint);
      const values = await fields(page);
      assert.equal(values.lang, lang);
      assert.equal(values.return_to, endpoint === '/donate/' ? 'donate' : 'subscribe');
      assert.equal(await page.locator('#donate-recurrence').isVisible(), true);
      assert.doesNotMatch(await page.locator('#donate-submit').textContent(), /\{amount\}/);
      assert.equal(await page.locator('#donate-form').evaluate(form => new FormData(form).getAll('currency').length), 1);
      if (endpoint === '/donate/') {
        assert.equal(await page.locator('.donate-impact li').count(), 3);
        assert.equal(await page.locator('a[href^="https://t.me/tribute/"]').count(), lang === 'ru' ? 1 : 0);
      }
    }
  }
  await page.goto(origin + '/donate/#crypto-table');
  assert.equal(await page.locator('#crypto').evaluate(e => e.open), true);
  await page.goto(origin + '/donate/#bank-transfer');
  await page.locator('#bank-transfer summary').click();
  assert.equal(await page.locator('#bank-transfer').evaluate(e => e.open), false);
  await page.locator('.donate-methods a[href="#bank-transfer"]').click();
  assert.equal(await page.locator('#bank-transfer').evaluate(e => e.open), true);
  await page.setViewportSize({ width: 320, height: 780 });
  for (const lang of ['en', 'ar', 'ml']) {
    await page.goto(origin + (lang === 'en' ? '' : '/' + lang) + '/donate/#crypto');
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
  }
});

test('declared main-page CSP permits payment forms and includes Mollie redirect hosts', { timeout: 30000 }, async t => {
  const { page, posted } = await openPage(t);
  for (const endpoint of ['/donate/', '/de/donate/']) {
    const response = await page.goto(origin + endpoint);
    assert.match(response.headers()['content-security-policy'], /frame-ancestors 'none'/);
    assert.match(response.headers()['content-security-policy'], /form-action[^;]*https:\/\/\*\.mollie\.com/);
  }
  await Promise.all([page.waitForURL('https://donate-api.organicmaps.app/checkout'), page.locator('#donate-submit').click()]);
  await page.goto(origin + '/donate/');
  const popup = page.waitForEvent('popup');
  await page.locator('.donate-methods form button').click();
  await (await popup).waitForLoadState();
  assert.deepEqual(posted.map(p => p.host), ['donate-api.organicmaps.app', 'www.paypal.com']);
});

test('English checkout keeps its text direction inside an Arabic page', { timeout: 30000 }, async t => {
  const { page } = await openPage(t, { javaScriptEnabled: false });
  await page.goto(origin + '/ar/donate/');
  const direction = selector => page.locator(selector).evaluate(e => getComputedStyle(e).direction);
  assert.equal(await direction('#donate-form'), 'rtl');

  // Use the rendered English card to exercise fallback labels inside an RTL document.
  await page.evaluate(html => {
    const english = new DOMParser().parseFromString(html, 'text/html');
    document.getElementById('donation').replaceWith(english.getElementById('donation'));
  }, fs.readFileSync(path.join(output, 'donate/index.html'), 'utf8'));
  assert.equal(await page.locator('html').getAttribute('dir'), 'rtl');
  assert.equal(await page.locator('#donate-form').evaluate(form => form.closest('[lang]').lang), 'en');
  assert.equal(await direction('#donate-form'), 'ltr');
  assert.equal(await direction('#amount-custom'), 'ltr');
});

test('the real donation template rejects missing, duplicate and reordered layout markers', { timeout: 30000 }, () => {
  const fixture = fs.mkdtempSync(path.join(os.tmpdir(), 'donate-markers-'));
  try {
    for (const dir of ['templates', 'content/donate/subscribe', 'static/js']) fs.mkdirSync(path.join(fixture, dir), { recursive: true });
    fs.writeFileSync(path.join(fixture, 'config.toml'), 'base_url = "https://example.invalid"\n');
    fs.copyFileSync(path.join(root, 'templates/donate.html'), path.join(fixture, 'templates/donate.html'));
    fs.writeFileSync(path.join(fixture, 'templates/base.html'), '{% set resource = page %}{% block content %}{% endblock %}');
    fs.writeFileSync(path.join(fixture, 'templates/_donate_form.html'), '');
    fs.writeFileSync(path.join(fixture, 'static/js/donate-subscribe.js'), '');
    fs.writeFileSync(path.join(fixture, 'content/donate/subscribe/index.md'), '---\ntitle: Support\nextra:\n  form:\n    form_title: Donate\n---\n');
    const impact = '<!-- donation-impact -->';
    const methods = '<!-- donation-methods -->';
    const valid = `Intro\n\n${impact}\n\nImpact\n\n${methods}\n\nMethods`;
    for (const body of [valid, valid.replace(impact, ''), valid.replace(methods, ''), valid + '\n' + impact,
      valid + '\n' + methods, `Intro\n\n${methods}\n\nMethods\n\n${impact}\n\nImpact`]) {
      fs.writeFileSync(path.join(fixture, 'content/donate/index.md'), '---\ntitle: Donate\ntemplate: donate.html\n---\n\n' + body);
      const result = spawnSync(process.env.ZOLA_BIN || 'zola', ['--root', fixture, 'build', '--force'], { encoding: 'utf8', timeout: 10000 });
      if (result.error) throw result.error;
      if (body === valid) assert.equal(result.status, 0, result.stdout + result.stderr);
      else {
        assert.notEqual(result.status, 0);
        assert.match(result.stdout + result.stderr, /exactly once, in that order/);
      }
    }
  } finally {
    fs.rmSync(fixture, { recursive: true, force: true });
  }
});
