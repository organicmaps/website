#!/usr/bin/env python3
"""Build small multilingual sites to test navigation with the real Zola templates."""

import re
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESTINATIONS = {
    "news/_index.md": ("News", "Neuigkeiten"),
    "donate/index.md": ("Donate", "Spenden"),
    "contribute/index.md": ("Contribute", "Mitmachen"),
    "faq/_index.md": ("Help", "Hilfe"),
}
CONFIG = ('base_url = "https://example.org"\n'
          '[languages.de]\n[translations]\nlanguage = "English"\n'
          '[languages.de.translations]\nlanguage = "Deutsch"\n')


def write(root, path, text):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


class RenderedPage(HTMLParser):
    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
                 "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self):
        super().__init__()
        self.stack = []
        self.in_menu = False
        self.href = None
        self.link_language = None
        self.label = []
        self.links = []
        self.form_language = None
        self.heading_language = None
        self.checkout_language = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        language = attrs.get("lang", self.stack[-1][1] if self.stack else None)
        if tag == "nav":
            self.in_menu = attrs.get("id") == "menu"
        if tag == "a" and self.in_menu:
            self.href = attrs["href"]
            self.link_language = language
            self.label = []
        if attrs.get("id") == "donate-form":
            self.form_language = language
        if attrs.get("id") == "donate-card-title":
            self.heading_language = language
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


class NavigationTests(unittest.TestCase):
    def setUp(self):
        self.zola = shutil.which("zola")
        self.assertIsNotNone(self.zola, "Install Zola to run navigation tests")

    def build(self, root, *, expected_error=None):
        result = subprocess.run([self.zola, "build"], cwd=root,
                                capture_output=True, text=True)
        output = result.stdout + result.stderr
        if expected_error is None:
            self.assertEqual(result.returncode, 0, output)
        else:
            self.assertNotEqual(result.returncode, 0, output)
            self.assertIn(expected_error, output)

    def navigation_site(self, root):
        write(root, "config.toml", CONFIG)
        menu = ('<html lang="{{ lang }}">{% set resource = section %}'
                '{% set resource_path = section.path %}'
                '{% include "top_menu.html" %}</html>')
        write(root, "templates/index.html", menu)
        write(root, "templates/section.html", menu)
        write(root, "templates/page.html", "{{ page.title }}")
        for template in ("top_menu.html", "language_selector.html"):
            write(root, f"templates/{template}", (ROOT / "templates" / template).read_text())
        for suffix, title in (("", "Home"), (".de", "Start")):
            write(root, f"content/_index{suffix}.md", f"---\ntitle: {title}\n---\n")

    def test_missing_translations_use_default_language_destinations(self):
        # Each lookup must work when its own translation is absent, while the
        # other destinations must still use their available translations.
        cases = [(), tuple(DESTINATIONS), *((path,) for path in DESTINATIONS)]
        for missing in cases:
            with self.subTest(missing=missing), tempfile.TemporaryDirectory() as tmp:
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

                self.build(root)
                parser = RenderedPage()
                parser.feed((root / "public/de/index.html").read_text())
                self.assertEqual(parser.links[:5], expected)
                for href, _, _ in expected:
                    self.assertTrue((root / "public" / href.strip("/") / "index.html").is_file(), href)

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
        for missing in ((), ("donate/index.md",), ("donate/subscribe/index.md",)):
            with self.subTest(missing=missing), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                write(root, "config.toml", CONFIG)
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
                if "donate/index.md" not in missing:
                    write(root, "content/donate/index.de.md",
                          donate.replace("title: Donate", "title: Spenden\nslug: spenden"))
                if "donate/subscribe/index.md" not in missing:
                    write(root, "content/donate/subscribe/index.de.md",
                          subscribe.replace("Default", "Localized"))

                self.build(root)
                expected_path = "/donate/" if "donate/index.md" in missing else "/de/spenden/"
                for page in ("donate/index.md", "donate/subscribe/index.md"):
                    if page in missing:
                        continue
                    with self.subTest(page=page):
                        path = "/de/spenden/" if page == "donate/index.md" else "/de/donate/subscribe/"
                        output = (root / "public" / path.strip("/") / "index.html").read_text()
                        label = "Default" if "donate/subscribe/index.md" in missing else "Localized"
                        self.assertIn(f'href="{expected_path}#other-ways">{label} alternatives</a>', output)
                        if page == "donate/index.md":
                            self.assertIn(f'>{label} checkout</h2>', output)
                        parser = RenderedPage()
                        parser.feed(output)
                        self.assertEqual(parser.form_language, "en" if label == "Default" else "de")
                        if page == "donate/index.md":
                            self.assertEqual(parser.heading_language, "en" if label == "Default" else "de")
                        self.assertEqual(parser.checkout_language, "de")
                        self.assertTrue((root / "public" / expected_path.strip("/") / "index.html").is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)
