// Exercise the rendered website and the app's local FAQ file in Chromium.
const { test, before, after } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');
const { assetResponse } = require('./browser_assets.cjs');

const output = path.resolve(__dirname, '../public');
const origin = 'https://organicmaps.app';
const embeddedFile = pathToFileURL(path.join(output, 'faq/embedded-faq/index.html')).href;
let browser;

before(async () => {
  assert.ok(fs.existsSync(path.join(output, 'faq/index.html')), 'Run zola build before npm run test:browser');
  browser = await chromium.launch();
});
after(async () => { if (browser) await browser.close(); });

async function openPage(t, { locale = 'en-US', offline = false, javaScriptEnabled = true } = {}) {
  const context = await browser.newContext({ locale, offline, javaScriptEnabled });
  const unexpected = [];
  const errors = [];
  if (!offline) {
    await context.route('**/*', async route => {
      const url = new URL(route.request().url());
      if (url.origin !== origin) {
        unexpected.push(url.href);
        return route.abort();
      }
      const asset = assetResponse(output, url.pathname);
      if (!asset) {
        unexpected.push(url.href);
        return route.fulfill({ status: 404, body: 'Not found' });
      }
      return route.fulfill(asset);
    });
  }
  const page = await context.newPage();
  page.on('pageerror', error => errors.push(error.message));
  t.after(async () => {
    await context.close();
    assert.deepEqual(unexpected, [], 'Unexpected requests');
    assert.deepEqual(errors, [], 'Browser errors');
  });
  return page;
}

test('the bundled FAQ has a target for every local link in every language', async t => {
  // Inspect the whole file before language selection hides inactive targets.
  const page = await openPage(t, { offline: true, javaScriptEnabled: false });
  await page.goto(embeddedFile);
  const problems = await page.evaluate(() => {
    const problems = [];
    const targets = new Map();
    for (const element of document.querySelectorAll('[id]')) {
      const lang = element.closest('dd[lang]')?.lang;
      const languages = targets.get(element.id) || [];
      languages.push(lang);
      targets.set(element.id, languages);
    }
    for (const link of document.querySelectorAll('a[href]')) {
      const href = link.getAttribute('href');
      if (href === '#' || /^(https?:\/\/|mailto:)/.test(href)) continue;
      if (!href.startsWith('#')) {
        problems.push('Relative link ' + href);
        continue;
      }
      const lang = link.closest('[lang]')?.lang;
      const matches = targets.get(decodeURIComponent(href.slice(1))) || [];
      const reachable = matches.filter(targetLang => !targetLang || targetLang === lang);
      if (reachable.length !== 1) problems.push(lang + ' ' + href + ' has ' + reachable.length + ' targets');
    }

    const requirements = document.getElementById('app-which-ios-and-android-versions-are-supported');
    const titles = requirements.querySelectorAll('dt h3[lang]');
    if (!titles.length) problems.push('The device requirements answer has no languages');
    for (const { lang } of titles) {
      const links = requirements.querySelectorAll('dd[lang="' + lang + '"] a[href="#app-how-to-use-android-auto"]');
      if (links.length !== 1) problems.push(lang + ' requires a local Android Auto link');
    }
    return problems;
  });
  assert.deepEqual(problems, []);
});

test('offline FAQ jumps scroll to the selected language', async t => {
  const page = await openPage(t, { offline: true });
  for (const lang of ['en', 'ru', 'uk']) {
    const embedded = embeddedFile + '?lang=' + lang;
    await page.goto(embedded);
    const prefix = lang === 'en' ? '' : lang + '-';
    for (const [source, targetId] of [
      ['map-how-to-create-a-route', prefix + 'route-stops'],
      ['map-how-to-create-a-route', 'map-can-not-find-position'],
      ['editing-map-errors', prefix + 'osm-note'],
    ]) {
      await page.locator('#' + source + ' dd[lang="' + lang + '"] a[href="#' + targetId + '"]').click();
      assert.equal(page.url(), embedded + '#' + targetId);
      assert.equal(await page.locator('#' + targetId).count(), 1);
      await page.waitForFunction(id => {
        const element = document.getElementById(id);
        const bounds = element.getBoundingClientRect();
        return bounds.top >= -2 && bounds.top < innerHeight && bounds.bottom > 0;
      }, targetId);
    }
  }
});

test('embedded FAQ handles legacy fragments and malformed language requests', async t => {
  const page = await openPage(t, { offline: true });
  for (const [url, target] of [
    ['?lang=de#id-editor', 'dd[lang="de"] #id-editor'],
    ['?lang=uk#osm-note', 'dd[lang="uk"] #uk-osm-note'],
  ]) {
    await page.goto(embeddedFile + url);
    assert.equal(await page.locator(target).isVisible(), true);
    await page.waitForFunction(selector => {
      const bounds = document.querySelector(selector).getBoundingClientRect();
      return bounds.top >= -2 && bounds.top < innerHeight && bounds.bottom > 0 && scrollY > 0;
    }, target);
  }
  await page.goto(embeddedFile + '?lang=%');
  assert.ok(await page.locator('dd[lang="en"]:visible').count() > 0);
});

test('explicit English FAQ fragments survive a German browser preference', async t => {
  for (const [pathname, fragment] of [
    ['/faq/map/how-to-create-a-route/', 'route-stops'],
    ['/faq/', 'faq-routes-and-navigation'],
  ]) {
    const page = await openPage(t, { locale: 'de-DE' });
    const url = origin + pathname + '#' + fragment;
    await page.goto(url);
    assert.equal(page.url(), url);
    assert.equal(await page.locator('html').getAttribute('lang'), 'en');
    assert.equal(await page.locator('#' + fragment).count(), 1);
    assert.equal(await page.evaluate(() => localStorage.getItem('lang')), null);
    await page.goto(origin + pathname, { waitUntil: 'commit' });
    await page.waitForURL(url => url.pathname.startsWith('/de/faq/'));
    assert.equal(await page.locator('html').getAttribute('lang'), 'de');
    if (pathname === '/faq/') assert.equal(page.url(), origin + '/de/faq/');
    assert.equal(await page.evaluate(() => localStorage.getItem('lang')), 'de');
  }
});

test('language choices follow section jumps and browser history', async t => {
  const page = await openPage(t);
  await page.goto(origin + '/faq/map/how-to-create-a-route/');
  const russian = page.locator('.lang-menu-link[lang="ru"]');
  const translatedPath = await russian.getAttribute('href');
  await page.locator('main a[href$="#route-stops"]').click();
  await page.waitForFunction(() => document.querySelector('.lang-menu-link[lang="ru"]').hash === '#route-stops');
  assert.equal(await russian.getAttribute('href'), translatedPath + '#route-stops');
  await page.goBack();
  await page.waitForFunction(() => document.querySelector('.lang-menu-link[lang="ru"]').hash === '');
  assert.equal(await russian.getAttribute('href'), translatedPath);
  await page.goForward();
  await page.waitForFunction(() => document.querySelector('.lang-menu-link[lang="ru"]').hash === '#route-stops');
  const destination = new URL(await russian.getAttribute('href'), origin).href;
  await page.locator('label[for="lang-menu-trigger"]').click();
  await Promise.all([page.waitForURL(destination), russian.click()]);
  assert.equal(await page.locator('html').getAttribute('lang'), 'ru');
  assert.equal(new URL(page.url()).hash, '#route-stops');
  assert.equal(await page.locator('#route-stops').isVisible(), true);
  assert.equal(await page.evaluate(() => localStorage.getItem('lang')), 'ru');
});

test('language choices keep shared FAQ topics and heading targets', async t => {
  const page = await openPage(t);
  const fragment = '#faq-routes-and-navigation';
  await page.goto(origin + '/faq/?from=help');
  await page.locator('main nav a[href="' + fragment + '"]').click();
  for (const lang of ['ru', 'uk', 'en', 'de']) {
    const path = (lang === 'en' ? '' : '/' + lang) + '/faq/';
    const destination = origin + path + '?from=help' + (lang === 'de' ? '' : fragment);
    await page.locator('label[for="lang-menu-trigger"]').click();
    await Promise.all([
      page.waitForURL(destination),
      page.locator('.lang-menu-link[lang="' + lang + '"]').click(),
    ]);
    if (lang !== 'de') {
      assert.ok(await page.locator(fragment).isVisible());
      await page.waitForFunction(hash => {
        const top = document.querySelector(hash).getBoundingClientRect().top;
        return top >= -2 && top < innerHeight;
      }, fragment);
    }
  }

  const settings = '#android-location-settings';
  await page.goto(origin + '/faq/map/can-not-find-position/' + settings);
  await page.locator('label[for="lang-menu-trigger"]').click();
  await page.locator('.lang-menu-link[lang="ru"]').click();
  assert.equal(await page.locator('html').getAttribute('lang'), 'ru');
  assert.equal(new URL(page.url()).hash, settings);
  assert.ok(await page.locator(settings).isVisible());
});

test('non-FAQ redirects preserve donation parameters and fragments', async t => {
  const page = await openPage(t, { locale: 'de-DE' });
  const parameters = '?amount=10&currency=CHF#other-ways';
  await page.goto(origin + '/donate/' + parameters, { waitUntil: 'commit' });
  await page.waitForURL(origin + '/de/donate/' + parameters);
  assert.equal(await page.locator('#currency').inputValue(), 'CHF');
  assert.equal(await page.locator('#other-ways').count(), 1);
});

test('published FAQ section fragments remain valid', async t => {
  const page = await openPage(t);
  for (const [answer, fragments] of [
    ['voice/text-to-speech-tts-and-voice-directions-on-android', ['summary', 'instructions', 'screenshots', 'engines', 'testing', 'workarounds']],
    ['editing/advanced-map-editing', ['openstreetmap-editors', 'id-editor', 'tags-how-the-osm-data-model-works', 'community-and-wiki', 'what-happens-with-my-edits', 'osm-note']],
  ]) {
    await page.goto(origin + '/faq/' + answer + '/');
    for (const fragment of fragments) {
      assert.equal(await page.locator('#' + fragment).count(), 1, fragment);
    }
  }
});
