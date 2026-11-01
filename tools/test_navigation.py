#!/usr/bin/env python3
"""Build small multilingual sites to test navigation with the real Zola templates."""

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


class MenuLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_menu = False
        self.href = None
        self.label = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "nav":
            self.in_menu = attrs.get("id") == "menu"
        if tag == "a" and self.in_menu:
            self.href = attrs["href"]
            self.label = []

    def handle_data(self, data):
        if self.href is not None:
            self.label.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.href is not None:
            self.links.append((self.href, "".join(self.label).strip()))
            self.href = None
        if tag == "nav":
            self.in_menu = False


class NavigationTests(unittest.TestCase):
    def test_missing_translations_use_default_language_destinations(self):
        zola = shutil.which("zola")
        self.assertIsNotNone(zola, "Install Zola to run navigation tests")
        # Each lookup must work when its own translation is absent, while the
        # other destinations must still use their available translations.
        cases = [(), tuple(DESTINATIONS), *((path,) for path in DESTINATIONS)]
        for missing in cases:
            with self.subTest(missing=missing), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)

                def write(path, text):
                    target = root / path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(text, encoding="utf-8")

                def content(path, title):
                    write(path, f"---\ntitle: {title}\nextra:\n  menu_title: {title}\n---\n")

                write("config.toml", 'base_url = "https://example.org"\n'
                      '[languages.de]\n[translations]\nlanguage = "English"\n'
                      '[languages.de.translations]\nlanguage = "Deutsch"\n')
                menu = ('{% set resource = section %}'
                        '{% set resource_path = section.path %}'
                        '{% include "top_menu.html" %}')
                write("templates/index.html", menu)
                write("templates/section.html", menu)
                write("templates/page.html", "{{ page.title }}")
                for template in ("top_menu.html", "language_selector.html"):
                    write(f"templates/{template}", (ROOT / "templates" / template).read_text())
                content("content/_index.md", "Home")
                content("content/_index.de.md", "Start")
                expected = [("/de/", "")]
                for path, (english, german) in DESTINATIONS.items():
                    content(f"content/{path}", english)
                    if path not in missing:
                        content(f"content/{path[:-3]}.de.md", german)
                    prefix = "" if path in missing else "/de"
                    expected.append((f"{prefix}/{path.split('/')[0]}/",
                                     english if path in missing else german))

                result = subprocess.run([zola, "build"], cwd=root,
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                parser = MenuLinks()
                parser.feed((root / "public/de/index.html").read_text())
                self.assertEqual(parser.links[:5], expected)
                for href, _ in expected:
                    self.assertTrue((root / "public" / href.strip("/") / "index.html").is_file(), href)


if __name__ == "__main__":
    unittest.main(verbosity=2)
