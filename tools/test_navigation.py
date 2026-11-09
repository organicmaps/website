#!/usr/bin/env python3
"""Test homepage links, navigation, FAQ and donation templates with real Zola."""

import json
import re
import shutil
import subprocess
import tempfile
import unittest
from html import unescape
from html.parser import HTMLParser
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESTINATIONS = {
    "news/_index.md": ("News", "Neuigkeiten"),
    "donate/index.md": ("Donate", "Spenden"),
    "contribute/index.md": ("Contribute", "Mitmachen"),
    "faq/_index.md": ("Help", "Hilfe"),
}
CONFIG = ('base_url = "https://example.org"\n'
          '[extra]\nrtl_languages = ["ar"]\n'
          '[languages.de]\n[translations]\nlanguage = "English"\ncontact = "Contact"\n'
          '[languages.de.translations]\nlanguage = "Deutsch"\ncontact = "Kontakt"\n')


def write(root, path, text):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


class RenderedPage(HTMLParser):
    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
                 "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, menu_id="menu"):
        super().__init__()
        self.stack = []
        self.menu_id = menu_id
        self.in_menu = False
        self.href = None
        self.link_language = None
        self.label = []
        self.links = []
        self.form_language = None
        self.heading_language = None
        self.checkout_language = None
        self.card_direction = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        language = attrs.get("lang", self.stack[-1][1] if self.stack else None)
        if tag == "nav":
            self.in_menu = attrs.get("id") == self.menu_id
        if tag == "a" and self.in_menu:
            self.href = attrs["href"]
            self.link_language = language
            self.label = []
        if attrs.get("id") == "donate-form":
            self.form_language = language
        if attrs.get("id") == "donate-card-title":
            self.heading_language = language
        if attrs.get("id") == "donation":
            self.card_direction = attrs.get("dir")
        if tag == "input" and attrs.get("name") == "lang":
            self.checkout_language = attrs["value"]
        if tag not in self.VOID_TAGS:
            self.stack.append((tag, language))

    def handle_data(self, data):
        if self.href is not None:
            self.label.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.href is not None:
            self.links.append((self.href, "".join(self.label).strip(), self.link_language))
            self.href = None
        if tag == "nav":
            self.in_menu = False
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break


class MainLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "main":
            self.in_main = True
        elif tag == "a" and self.in_main:
            href = dict(attrs).get("href")
            if href is not None:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False


class NavigationTests(unittest.TestCase):
    def setUp(self):
        self.zola = shutil.which("zola")
        self.assertIsNotNone(self.zola, "Install Zola to run navigation tests")

    def build(self, root, *, expected_error=None, output_dir=None):
        command = [self.zola, "build"]
        if output_dir is not None:
            command.extend(["--output-dir", str(output_dir)])
        result = subprocess.run(command, cwd=root,
                                capture_output=True, text=True)
        output = result.stdout + result.stderr
        if expected_error is None:
            self.assertEqual(result.returncode, 0, output)
        else:
            self.assertNotEqual(result.returncode, 0, output)
            self.assertIn(expected_error, output)

    def test_homepages_link_news_and_language_chat(self):
        references = (ROOT / "templates/shortcodes/references.md").read_text()
        chats = dict(re.findall(
            r"(?m)^\[(telegram(?:_chat(?:_[a-z]+)?)?)\]:\s+(\S+)", references,
        ))
        with tempfile.TemporaryDirectory() as output:
            public = Path(output) / "public"
            self.build(ROOT, output_dir=public)
            for home in sorted((ROOT / "content").glob("_index*.md")):
                lang = "en" if home.name == "_index.md" else home.name[7:-3]
                with self.subTest(lang=lang):
                    prefix = "" if lang == "en" else lang
                    parser = MainLinks()
                    parser.feed((public / prefix / "index.html").read_text())
                    group = chats.get(f"telegram_chat_{lang.split('-')[0]}", chats["telegram_chat"])
                    self.assertCountEqual(
                        [href for href in parser.links if href in chats.values()],
                        [chats["telegram"], group],
                    )

    def navigation_site(self, root):
        write(root, "config.toml", CONFIG)
        menu = ('<html lang="{{ lang }}">{% set resource = section %}'
                '{% set resource_path = section.path %}'
                '{% include "top_menu.html" %}{% include "bottom_menu.html" %}</html>')
        write(root, "templates/index.html", menu)
        write(root, "templates/section.html", menu)
        write(root, "templates/page.html", "{{ page.title }}")
        for template in ("top_menu.html", "bottom_menu.html", "language_selector.html"):
            write(root, f"templates/{template}", (ROOT / "templates" / template).read_text())
        for suffix, title in (("", "Home"), (".de", "Start")):
            write(root, f"content/_index{suffix}.md", f"---\ntitle: {title}\n---\n")

    def faq_site(self, root, *, brand="Organic Maps", answer_title="Plan a route"):
        write(root, "config.toml", 'base_url = "https://example.org"\n'
              f'title = {json.dumps(brand)}\n'
              'taxonomies = [{name = "faq"}]\n'
              '[extra]\nrtl_languages = []\nlanguage_neutral_taxonomy_terms = ["linux"]\n'
              '[translations]\nfaq-menu-title = "Help"\nfaq-start-here = "Start here"\nfaq-term-description = "FAQ about {}"\n'
              '[languages.de]\ntaxonomies = [{name = "faq"}]\n'
              '[languages.de.translations]\nfaq-menu-title = "Hilfe"\nfaq-start-here = "Erste Schritte"\nfaq-term-description = "Fragen zu {}"\n')
        for template in ("base.html", "page.html", "language_redirect.html", "_jsonld_faq.html",
                         "faq/list.html", "faq/single.html", "faq/_questions.html", "faq/faq-breadcrumbs.html"):
            write(root, f"templates/{template}", (ROOT / "templates" / template).read_text())
        # Unrelated menus have their own fixtures; keep this one on FAQ rendering.
        for template in ("top_menu.html", "bottom_menu.html", "faq/github_edit_link.html"):
            write(root, f"templates/{template}", "")
        write(root, "static/main.css", "")
        write(root, "content/faq/_index.md",
              '---\nrender: false\ntitle: Answers\nextra:\n  menu_title: Support\n'
              '  start_here: ["faq/app/route/index.md"]\n---\n')
        write(root, "content/faq/_index.de.md", '---\nrender: false\ntitle: Hilfe\n---\n')
        write(root, "content/faq/app/route/index.md",
              f'---\ntitle: {json.dumps(answer_title)}\ntaxonomies:\n  faq: ["app"]\n'
              'extra:\n  order: 10\n---\n\n## Add stops {#stops}\n\nChoose a stop.\n')
        write(root, "content/faq/app/route/index.de.md",
              '---\ntitle: Route planen\nslug: strecke\ntaxonomies:\n  faq: ["reisen"]\n'
              'extra:\n  order: 10\n---\n\n## Zwischenziele {#stops}\n\nWähle ein Ziel.\n')
        for suffix, title, category in (("", "Find a place", "map"), (".de", "Ort finden", "karte")):
            write(root, f"content/faq/map/place/index{suffix}.md",
                  f'---\ntitle: {title}\ntaxonomies:\n  faq: ["{category}"]\n'
                  'extra:\n  order: 10\n---\n')

    def test_faq_listings_link_related_questions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.faq_site(root)
            self.build(root)
            for listing in ("faq/index.html", "faq/app/index.html"):
                with self.subTest(listing=listing):
                    parser = MainLinks()
                    parser.feed((root / "public" / listing).read_text())
                    self.assertIn("/faq/app/route/#stops", parser.links)
            self.assertIn('id="stops"', (root / "public/faq/app/route/index.html").read_text())
            for listing in ("de/faq/index.html", "de/faq/reisen/index.html"):
                with self.subTest(listing=listing):
                    parser = MainLinks()
                    parser.feed((root / "public" / listing).read_text())
                    self.assertIn("/de/faq/app/strecke/", parser.links)
                    self.assertFalse(any("#stops" in href for href in parser.links))
            self.assertNotIn("Erste Schritte", (root / "public/de/faq/index.html").read_text())

            english = (root / "public/faq/app/route/index.html").read_text()
            breadcrumbs = RenderedPage(menu_id=None)
            breadcrumbs.feed(english)
            self.assertEqual(breadcrumbs.links, [("/faq/", "Support", "en"), ("/faq/app/", "App", "en")])
            english_term = (root / "public/faq/app/index.html").read_text()
            self.assertEqual(english_term.count('aria-current="page"'), 1)
            self.assertIn('aria-hidden="true"> › </span>', english_term)
            german_term = (root / "public/de/faq/reisen/index.html").read_text()
            breadcrumbs = RenderedPage(menu_id=None)
            breadcrumbs.feed(german_term)
            self.assertEqual(breadcrumbs.links, [("/de/faq/", "Hilfe", "de"), ("/de/faq/karte/", "Karte", "de")])
            self.assertEqual(german_term.count('aria-current="page"'), 1)
            self.assertIn('aria-hidden="true"> • </span>', german_term)

            article = root / "content/faq/app/route/index.md"
            article.write_text(article.read_text().replace("Plan a route", "Plan your journey"))
            write(root, "content/faq/_index.de.md", '---\nrender: false\ntitle: Hilfe\n'
                  'extra:\n  start_here: ["faq/app/route/index.md"]\n---\n')
            self.build(root)
            landing = (root / "public/faq/index.html").read_text()
            start_here = re.search(r"<h2>Start here</h2>(.*?)</ul>", landing, re.S).group(1)
            self.assertIn('href="/faq/app/route/">Plan your journey</a>', start_here)
            self.assertNotIn(">Plan a route</a>", landing)
            german = (root / "public/de/faq/index.html").read_text()
            start_here = re.search(r"<h2>Erste Schritte</h2>(.*?)</ul>", german, re.S).group(1)
            self.assertIn('href="/de/faq/app/strecke/">Route planen</a>', start_here)
            self.assertNotIn("/faq/app/route/", start_here)

    def test_faq_answer_titles_use_configured_brand(self):
        cases = (("Trail Atlas", "Plan a route", "Plan a route – Trail Atlas"),
                 ("", "Plan a route", "Plan a route – Organic Maps"),
                 ("Organic Maps", "How does ORGANIC MAPS work?", "How does ORGANIC MAPS work?"))
        for brand, title, expected in cases:
            with self.subTest(brand=brand, title=title), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.faq_site(root, brand=brand, answer_title=title)
                self.build(root)
                output = (root / "public/faq/app/route/index.html").read_text()
                self.assertIn(f"<title>{expected}</title>", output)

    def test_embedded_faq_rewrites_heading_targets_without_changing_examples(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "config.toml", 'base_url = "https://example.org"\n'
                  '[slugify]\npaths = "safe"\n[languages.ru]\n')
            write(root, "templates/page.html", '{% set embedded_page = page %}'
                  '{% set html_lang = lang %}{% include "faq/_embedded_content.html" %}')
            write(root, "templates/faq/_embedded_content.html",
                  (ROOT / "templates/faq/_embedded_content.html").read_text())
            body = ('[Jump](#target)\n\n## Heading {#target}\n\n'
                    '`<h2 id="target">`\n\n<span id="target"></span>\n')
            write(root, "content/route.md", '---\ntitle: Route\n---\n\n' + body)
            write(root, "content/route.ru.md", '---\ntitle: Маршрут\nslug: маршрут\n---\n\n' + body)
            self.build(root)
            output = (root / "public/ru/маршрут/index.html").read_text()
            self.assertIn('href="#ru-target"', output)
            self.assertIn('<h2 id="ru-target">', output)
            self.assertIn('<span id="target">', output)
            code = re.search(r"<code>(.*?)</code>", output, re.S).group(1)
            self.assertEqual(unescape(code), '<h2 id="target">')

    def test_missing_translations_use_default_language_destinations(self):
        # Each lookup must work when its own translation is absent, while the
        # other destinations must still use their available translations.
        cases = [(), tuple(DESTINATIONS), *((path,) for path in DESTINATIONS)]
        for missing in cases:
            # Resource kinds must not depend on the checkout directory's name.
            with self.subTest(missing=missing), tempfile.TemporaryDirectory(prefix="navigation_index-") as tmp:
                root = Path(tmp)

                def content(path, title):
                    write(root, path, f"---\ntitle: {title}\nextra:\n  menu_title: {title}\n---\n")

                self.navigation_site(root)
                expected = [("/de/", "", "de")]
                for path, (english, german) in DESTINATIONS.items():
                    content(f"content/{path}", english)
                    if path not in missing:
                        content(f"content/{path[:-3]}.de.md", german)
                    prefix = "" if path in missing else "/de"
                    expected.append((f"{prefix}/{path.split('/')[0]}/",
                                     english if path in missing else german,
                                     "en" if path in missing else "de"))
                # An ordinary page can contain "_index" in its filename and have a translated slug.
                content("content/guide_index.md", "Guide")
                write(root, "content/guide_index.de.md",
                      '---\ntitle: Anleitung\nslug: anleitung\nextra:\n  menu_title: Anleitung\n---\n')
                guide = ("/de/anleitung/", "Anleitung", "de")

                self.build(root)
                parser = RenderedPage()
                parser.feed((root / "public/de/index.html").read_text())
                self.assertEqual(parser.links[:5], expected)
                for href, _, _ in [*expected, guide]:
                    self.assertTrue((root / "public" / href.strip("/") / "index.html").is_file(), href)
                footer = RenderedPage(menu_id="bottom-menu")
                footer.feed((root / "public/de/index.html").read_text())
                self.assertCountEqual([link for link in footer.links if link[0].startswith("/")],
                                      [*expected[1:4], guide])
                # The API link's tooltip is English on every page.
                self.assertIn(("https://omaps.app/api", "API", "en"), footer.links)

    def test_language_selector_declares_name_languages(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.navigation_site(root)
            menu = ('<html lang="{{ lang }}"><nav id="menu">{% set resource = section %}'
                    '{% include "language_selector.html" %}</nav></html>')
            write(root, "templates/index.html", menu)
            self.build(root)
            for path, foreign, label in (("", "de", "Deutsch"), ("de/", "en", "English")):
                with self.subTest(path=path):
                    parser = RenderedPage()
                    parser.feed((root / "public" / path / "index.html").read_text())
                    prefix = "/de" if foreign == "de" else ""
                    self.assertEqual(parser.links, [(f"{prefix}/", label, foreign)])

    def test_missing_default_destinations_stop_the_build(self):
        for missing, kind in (("news/_index.md", "Section"), ("donate/index.md", "Page")):
            with self.subTest(missing=missing), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.navigation_site(root)
                for path, (english, german) in DESTINATIONS.items():
                    if path != missing:
                        write(root, f"content/{path}",
                              f"---\ntitle: {english}\nextra:\n  menu_title: {english}\n---\n")
                    write(root, f"content/{path[:-3]}.de.md",
                          f"---\ntitle: {german}\nextra:\n  menu_title: {german}\n---\n")
                self.build(root, expected_error=f"{kind} `{missing}` not found.")

    def test_donation_pages_select_companions_and_form_language(self):
        cases = ((), ("donate/index.md",), ("donate/subscribe/index.md",))
        for lang, missing in product(("de", "ar"), cases):
            with self.subTest(lang=lang, missing=missing), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                config = CONFIG.replace("languages.de", f"languages.{lang}")
                if lang == "ar":
                    config = config.replace('language = "Deutsch"', 'language = "العربية"')
                    config = config.replace('contact = "Kontakt"', 'contact = "اتصل بنا"')
                write(root, "config.toml", config)
                write(root, "templates/base.html", '<html lang="{{ lang }}">{% set resource = page %}'
                      '{% block header %}{% endblock %}{% block content %}{% endblock %}</html>')
                write(root, "static/js/donate-subscribe.js", "")
                for template in ("donate.html", "donate-subscribe.html", "_donate_form.html", "language_selector.html"):
                    write(root, f"templates/{template}", (ROOT / "templates" / template).read_text())
                donate = ('---\ntitle: Donate\ntemplate: donate.html\n---\n'
                          'Intro\n\n<!-- donation-impact -->\n\nImpact\n\n'
                          '<!-- donation-methods -->\n\nMethods\n')
                # Keep every field required by the real checkout, varying only the labels under test.
                subscribe = (ROOT / "content/donate/subscribe/index.md").read_text()
                subscribe = re.sub(r"(?m)^    form_title:.*$", "    form_title: Default checkout", subscribe)
                subscribe = re.sub(r"(?m)^    other_ways:.*$", "    other_ways: Default alternatives", subscribe)
                write(root, "content/donate/index.md", donate)
                write(root, "content/donate/subscribe/index.md", subscribe)
                donate_title = "Spenden" if lang == "de" else "تبرع"
                donate_slug = "spenden" if lang == "de" else "support"
                donate_path = f"/{lang}/{donate_slug}/"
                # A Latin brand name can precede an RTL checkout heading.
                localized_title = "Localized checkout" if lang == "de" else "Organic Maps — تبرع"
                if "donate/index.md" not in missing:
                    write(root, f"content/donate/index.{lang}.md",
                          donate.replace("title: Donate", f"title: {donate_title}\nslug: {donate_slug}"))
                if "donate/subscribe/index.md" not in missing:
                    write(root, f"content/donate/subscribe/index.{lang}.md",
                          subscribe.replace("Default", "Localized").replace("Localized checkout", localized_title))

                self.build(root)
                expected_path = "/donate/" if "donate/index.md" in missing else donate_path
                label = "Default" if "donate/subscribe/index.md" in missing else "Localized"
                form_lang = "en" if label == "Default" else lang
                for page in ("donate/index.md", "donate/subscribe/index.md"):
                    if page in missing:
                        continue
                    with self.subTest(page=page):
                        path = donate_path if page == "donate/index.md" else f"/{lang}/donate/subscribe/"
                        output = (root / "public" / path.strip("/") / "index.html").read_text()
                        self.assertIn(f'href="{expected_path}#other-ways">{label} alternatives</a>', output)
                        if page == "donate/index.md":
                            title = "Default checkout" if label == "Default" else localized_title
                            self.assertIn(f'>{title}</h2>', output)
                        parser = RenderedPage()
                        parser.feed(output)
                        self.assertEqual(parser.form_language, form_lang)
                        if page == "donate/index.md":
                            self.assertEqual(parser.heading_language, form_lang)
                            self.assertEqual(parser.card_direction, "rtl" if form_lang == "ar" else "ltr")
                        self.assertEqual(parser.checkout_language, lang)
                        self.assertTrue((root / "public" / expected_path.strip("/") / "index.html").is_file())

    def test_donation_layout_markers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "config.toml", 'base_url = "https://example.invalid"\n[extra]\nrtl_languages = []\n')
            write(root, "templates/donate.html", (ROOT / "templates/donate.html").read_text())
            write(root, "templates/base.html", '{% set resource = page %}{% block content %}{% endblock %}')
            write(root, "templates/_donate_form.html", "")
            write(root, "static/js/donate-subscribe.js", "")
            write(root, "content/donate/subscribe/index.md",
                  '---\ntitle: Support\nextra:\n  form:\n    form_title: Donate\n---\n')
            impact = "<!-- donation-impact -->"
            methods = "<!-- donation-methods -->"
            valid = f"Intro\n\n{impact}\n\nImpact\n\n{methods}\n\nMethods"
            cases = {
                "valid": valid,
                "missing impact": valid.replace(impact, ""),
                "missing methods": valid.replace(methods, ""),
                "duplicate impact": valid + "\n" + impact,
                "duplicate methods": valid + "\n" + methods,
                "reordered": f"Intro\n\n{methods}\n\nMethods\n\n{impact}\n\nImpact",
            }
            for name, body in cases.items():
                with self.subTest(layout=name):
                    write(root, "content/donate/index.md",
                          '---\ntitle: Donate\ntemplate: donate.html\n---\n\n' + body)
                    self.build(root, expected_error=None if name == "valid" else "exactly once, in that order")


if __name__ == "__main__":
    unittest.main(verbosity=2)
