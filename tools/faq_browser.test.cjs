// Serve rendered pages locally to exercise FAQ navigation without network access.
const { test, before, after } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');

const output = path.resolve(__dirname, '../public');
const origin = 'https://organicmaps.app';
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg' };
let browser;

before(async () => {
  assert.ok(fs.existsSync(path.join(output, 'faq/index.html')), 'Run zola build before npm run test:browser');
  browser = await chromium.launch();
});
after(async () => { if (browser) await browser.close(); });

async function openPage(t, locale = 'en-US') {
  const context = await browser.newContext({ locale });
  const unexpected = [];
  const errors = [];
  await context.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (url.origin !== origin) {
      unexpected.push(url.href);
      return route.abort();
    }
    const file = path.join(output, decodeURIComponent(url.pathname), url.pathname.endsWith('/') ? 'index.html' : '');
    if (!fs.existsSync(file)) {
      unexpected.push(url.href);
      return route.fulfill({ status: 404, body: 'Not found' });
    }
    return route.fulfill({ body: fs.readFileSync(file), contentType: mime[path.extname(file)] || 'application/octet-stream' });
  });
  const page = await context.newPage();
  page.on('pageerror', error => errors.push(error.message));
  t.after(async () => {
    await context.close();
    assert.deepEqual(unexpected, [], 'Unexpected requests');
    assert.deepEqual(errors, [], 'Browser errors');
  });
  return page;
}

test('embedded FAQ jumps stay in the bundled document', async t => {
  const page = await openPage(t);
  for (const lang of ['en', 'ru']) {
    const embedded = origin + '/faq/embedded-faq/?lang=' + lang;
    for (const fragment of ['route-stops', 'avoid-roads', 'kml-polygons']) {
      await page.goto(embedded);
      const targetId = (lang === 'en' ? '' : lang + '-') + fragment;
      const link = page.locator('dd[lang="' + lang + '"] a[href="#' + targetId + '"]');
      assert.equal(await link.count(), 1);
      await link.evaluate(element => element.scrollIntoView({ block: 'start' }));
      const documents = [];
      const trackDocument = request => { if (request.isNavigationRequest()) documents.push(request.url()); };
      page.on('request', trackDocument);
      await link.click();
      assert.equal(page.url(), embedded + '#' + targetId);
      const target = page.locator('dd[lang="' + lang + '"] #' + targetId);
      assert.equal(await target.count(), 1);
      await page.evaluate(() => new Promise(requestAnimationFrame));
      assert.ok(Math.abs(await target.evaluate(element => element.getBoundingClientRect().top)) < 2,
        'The fragment must scroll to the visible language');
      assert.deepEqual(documents, [], 'An in-answer jump must not request another document');
      page.off('request', trackDocument);
    }
  }
});

test('explicit English FAQ fragments survive a German browser preference', async t => {
  for (const [pathname, fragment] of [
    ['/faq/map/how-to-create-a-route/', 'route-stops'],
    ['/faq/', 'faq-routes-and-navigation'],
  ]) {
    const page = await openPage(t, 'de-DE');
    const url = origin + pathname + '#' + fragment;
    await page.goto(url);
    assert.equal(page.url(), url);
    assert.equal(await page.locator('html').getAttribute('lang'), 'en');
    assert.equal(await page.locator('#' + fragment).count(), 1);
  }
});

test('ordinary FAQ visits still choose the browser language', async t => {
  const page = await openPage(t, 'de-DE');
  await page.goto(origin + '/faq/', { waitUntil: 'commit' });
  await page.waitForURL(origin + '/de/faq/');
  assert.equal(await page.locator('html').getAttribute('lang'), 'de');
});

test('non-FAQ redirects preserve donation parameters and fragments', async t => {
  const page = await openPage(t, 'de-DE');
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
