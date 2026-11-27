// Load the app-bundled document from disk: HTTP redirects cannot repair its links.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');

test('bundled Android Auto links work offline in every included language', async t => {
  const file = path.resolve(__dirname, '../public/faq/embedded-faq/index.html');
  assert.ok(fs.existsSync(file), 'Run zola build before npm run test:browser');
  const browser = await chromium.launch();
  t.after(() => browser.close());
  const context = await browser.newContext({ locale: 'en-US', offline: true });
  const page = await context.newPage();
  const url = pathToFileURL(file);
  const fragment = 'app-how-to-use-android-auto';
  await page.goto(url.href);
  assert.equal(await page.locator('a[href]:not([href^="#"]):not([href^="https://"]):not([href^="mailto:"])').count(), 0,
    'A link in an app asset must be a bundled fragment or an absolute URL');
  const requirements = page.locator('#app-which-ios-and-android-versions-are-supported');
  // Titles declare the languages independently of the links being checked.
  const languages = await requirements.locator('dt h3[lang]').evaluateAll(
    headings => headings.map(heading => heading.lang));
  assert.ok(languages.length > 0, 'The bundled language inventory must be present');

  for (const lang of languages) {
    url.searchParams.set('lang', lang);
    await page.goto(url.href);
    const link = requirements.locator('dd[lang="' + lang + '"] a[href="#' + fragment + '"]');
    assert.equal(await link.count(), 1);
    await link.click();
    assert.equal(page.url(), url.href + '#' + fragment);
    assert.equal(await page.locator('[id="' + fragment + '"]').count(), 1);
    assert.equal(await page.locator('#' + fragment + ' dd[lang="' + lang + '"]').isVisible(), true);
    await page.evaluate(() => new Promise(requestAnimationFrame));
    assert.ok(Math.abs(await page.locator('#' + fragment).evaluate(
      element => element.getBoundingClientRect().top)) < 2, lang);
  }
});
