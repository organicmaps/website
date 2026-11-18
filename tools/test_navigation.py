#!/usr/bin/env python3
"""Test homepage links, navigation, news media, FAQ and donations with real Zola."""

import json
import re
import shutil
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from itertools import product
from pathlib import Path
from urllib.parse import quote

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


class NewsMedia(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.videos = []
        self.sources = []
        self.audio = []
        self.order = []
        self.layouts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "img" and attrs.get("class", "").startswith("news_image"):
            self.images.append(attrs)
            self.order.append(attrs["src"])
        elif tag == "video":
            self.videos.append(attrs)
        elif tag == "source":
            self.sources.append(attrs)
            self.order.append(attrs["src"])
        elif tag == "audio":
            self.audio.append(attrs)
        elif tag == "div" and attrs.get("class", "").startswith("news_content_image"):
            self.layouts.append(attrs["class"])


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

    def test_homepage_and_faq_destinations(self):
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
            for prefix in ("", "ru/", "uk/"):
                for topic in ("app/contribute-and-follow-updates", "app/project-goal-and-roadmap",
                              "map/3d-terrain-and-ocean-depth"):
                    with self.subTest(language=prefix, topic=topic):
                        parser = MainLinks()
                        parser.feed((public / prefix / "faq" / topic / "index.html").read_text())
                        self.assertIn(f"/{prefix}news/", parser.links)
                        self.assertTrue((public / prefix / "news/index.html").is_file())

            topic_ids = []
            for prefix in ("", "ru/", "uk/"):
                landing = (public / prefix / "faq/index.html").read_text()
                ids = re.findall(r'<h2 id="(faq-[^"]+)">', landing)
                self.assertTrue(ids, prefix)
                self.assertEqual(len(ids), len(set(ids)), prefix)
                topic_ids.append(ids)
            for ids in topic_ids[1:]:
                self.assertCountEqual(ids, topic_ids[0])

            redirects = [line.split() for line in (public / "_redirects").read_text().splitlines()
                         if line.startswith("/uk/faq/")]
            destination = "/uk/faq/мітки-та-треки/"
            self.assertTrue((public / destination.strip("/") / "index.html").is_file())
            for legacy in ("mitki-ta-marshruti", "мітки-та-маршрути"):
                for suffix in ("", "/"):
                    source = f"/uk/faq/{legacy}{suffix}"
                    with self.subTest(legacy=source):
                        self.assertEqual([rule for rule in redirects if rule[0] == source],
                                         [[source, destination, "301"]])

    def test_news_images_and_preview_resolution(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "config.toml", 'base_url = "https://example.org"\n'
                  'taxonomies = [{name = "news"}]\n'
                  '[extra]\nrtl_languages = []\n'
                  '[translations]\nback = "Back"\n'
                  '[languages.de]\ntaxonomies = [{name = "news"}]\n'
                  '[languages.de.translations]\nback = "Zurück"\n')
            for template in ("base.html", "_jsonld_news.html", "_news_preview.html", "_news_media.html", "sitemap.xml",
                             "news/page.html", "news/list.html", "news/date_section.html",
                             "shortcodes/screenshot.html"):
                write(root, f"templates/{template}", (ROOT / "templates" / template).read_text())
            for template in ("top_menu.html", "bottom_menu.html", "language_redirect.html",
                             "faq/faq-breadcrumbs.html", "faq/github_edit_link.html"):
                write(root, f"templates/{template}", "")
            write(root, "templates/index.html", '{% extends "base.html" %}'
                  '{% block content %}{{ resource.content | safe }}{% endblock %}')
            write(root, "templates/news/single.html", "{{ term.name }}")
            write(root, "static/main.css", "")
            image = (ROOT / "tools/fixtures/preview-test.webp").read_bytes()
            jpeg = (ROOT / "tools/fixtures/preview-test.jpg").read_bytes()
            (root / "static/images").mkdir()
            (root / "static/images/map.WEBP").write_bytes(image)
            (root / "content").mkdir()
            (root / "content/home-cover.jpg").write_bytes(jpeg)
            (root / "static/http-assets").mkdir()
            (root / "static/http-assets/cover.jpg").write_bytes(jpeg)
            cases = {
                "auto": ("", "auto", "01-preview.WEBP"),
                "legacy": ("", "legacy", "01-preview.jpg"),
                "chosen": ("extra:\n  preview_image: cover.webp\n", "chosen", "cover.webp"),
                "parent": ("", "custom-slug", "/news/2024-01-01/parent-preview.jpg"),
                "parent-webp": ("", "parent-webp", "/news/2024-01-01/parent-webp-preview.webp"),
                "override": ("extra:\n  preview_image: cover.webp\n", "override", "cover.webp"),
                "site-root": ("extra:\n  preview_image: /images/map.WEBP\n", "site-root", "/images/map.WEBP"),
                "local-http-name": ("extra:\n  preview_image: http-cover.jpg\n", "local-http-name", "http-cover.jpg"),
                "local-http-path": ("extra:\n  preview_image: http-assets/cover.jpg\n", "local-http-path", "/http-assets/cover.jpg"),
                "fallback": ("", "fallback", None),
            }
            for suffix in ("", ".de"):
                write(root, f"content/_index{suffix}.md", '---\ntitle: Home\nextra:\n'
                      '  preview_image: home-cover.jpg\n---\n'
                      '{{ <screenshot src="/images/map.WEBP" alt="Map" /> }}\n')
                write(root, f"content/news/_index{suffix}.md", '---\ntitle: News\n'
                      'render: false\npage_template: news/page.html\n---\n')
                write(root, f"content/news/2024-01-01/_index{suffix}.md", '---\ntitle: News\n'
                      'template: news/date_section.html\nsort_by: date\n---\n')
                for name, (extra, slug, _) in cases.items():
                    slug = slug if not suffix else f"{slug}-de"
                    write(root, f"content/news/2024-01-01/{name}/index{suffix}.md",
                          f'---\ntitle: {name}\ndate: 2024-01-01\nslug: {slug}\n'
                          f'taxonomies:\n  news: ["Releases"]\n{extra}---\nNews.\n')
            parent = root / "content/news/2024-01-01"
            for name in ("parent", "override"):
                (parent / f"{name}-preview.jpg").write_bytes(jpeg)
                (parent / f"{name}-preview.webp").write_bytes(image)
            (parent / "parent-webp-preview.webp").write_bytes(image)
            # The convention has an exact filename, even on case-insensitive filesystems.
            (parent / "auto-preview.JPG").write_bytes(jpeg)
            for name in cases:
                folder = root / "content/news/2024-01-01" / name
                (folder / "00-video.mp4").write_bytes(b"video")
                if name != "fallback":
                    gallery_cover = "01-preview.webp" if name == "legacy" else "01-preview.WEBP"
                    (folder / gallery_cover).write_bytes(image)
                    (folder / "02-detail.webp").write_bytes(image)
                if name in ("chosen", "override"):
                    (folder / "cover.webp").write_bytes(image)
                if name == "legacy":
                    (folder / "01-preview.jpg").write_bytes(jpeg)
                if name == "local-http-name":
                    (folder / "http-cover.jpg").write_bytes(jpeg)

            self.build(root)
            public = root / "public"
            sitemap = (public / "sitemap.xml").read_text()
            namespaces = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9",
                          "i": "http://www.google.com/schemas/sitemaps-image/0.9"}
            sitemap_images = {
                entry.findtext("s:loc", namespaces=namespaces):
                    entry.findtext("i:image/i:loc", namespaces=namespaces)
                for entry in ET.fromstring(sitemap).findall("s:url", namespaces)
            }
            for prefix, suffix in (("", ""), ("/de", "-de")):
                home = (public / prefix.strip("/") / "index.html").read_text()
                self.assertIn('src="/images/map.WEBP"', home)
                self.assertIn('width="2" height="1"', home)
                self.assertIn(f'content="https://example.org{prefix}/home-cover.jpg"', home)
                listing = (public / prefix.strip("/") / "news/index.html").read_text()
                dated = (public / prefix.strip("/") / "news/2024-01-01/index.html").read_text()
                for name, (_, slug, preview) in cases.items():
                    with self.subTest(language=prefix or "en", post=name):
                        path = f"{prefix}/news/2024-01-01/{slug}{suffix}/"
                        html = (public / path.strip("/") / "index.html").read_text()
                        expected = ("https://example.org" + (preview if preview.startswith("/") else path + preview)
                                    if preview else "https://example.org/images/screenshots/prague.jpg")
                        self.assertIn(f'<meta property="og:image" content="{expected}">', html)
                        article = json.loads(re.search(
                            r'<script type="application/ld\+json">(.*?)</script>', html, re.S,
                        ).group(1))
                        if preview:
                            self.assertEqual(article["image"], [expected])
                            gallery_cover = "01-preview.webp" if name == "legacy" else "01-preview.WEBP"
                            for filename in (gallery_cover, "02-detail.webp"):
                                self.assertTrue((public / path.strip("/") / filename).is_file())
                                for output in (html, listing):
                                    self.assertIn(f'class="news_image_landscape" src="{path}{filename}"', output)
                                self.assertIn(f'src="{path}{filename}"', dated)
                                image_tag = re.search(
                                    r'<img\b[^>]*src="' + re.escape(path + filename) + r'"[^>]*>', html,
                                ).group(0)
                                self.assertIn('width="2" height="1"', image_tag)
                                self.assertRegex(image_tag, r'loading="(?:eager|lazy)"')
                                self.assertIn('decoding="async"', image_tag)
                        else:
                            self.assertNotIn("image", article)
                        expected_count = 0 if name == "fallback" else 3 if name in ("chosen", "override", "local-http-name") else 2
                        self.assertEqual(len(re.findall(r'<img class="news_image(?:_landscape)?"', html)), expected_count)
                        if name in ("chosen", "parent", "parent-webp", "override", "site-root", "local-http-name", "local-http-path"):
                            self.assertEqual(sitemap_images["https://example.org" + path], expected)
                        else:
                            self.assertIsNone(sitemap_images["https://example.org" + path])
                        if name == "legacy":
                            self.assertEqual((public / path.strip("/") / "01-preview.jpg").read_bytes(), jpeg)
                            for output in (html, listing, dated):
                                self.assertNotRegex(output, r'<img[^>]*src="' + re.escape(path + '01-preview.jpg') + r'"')
                for name in ("parent", "override"):
                    filename = f"/news/2024-01-01/{name}-preview.jpg"
                    self.assertTrue((public / filename.lstrip("/")).is_file())
                    for output in (listing, dated):
                        self.assertNotRegex(output, r'<img[^>]*src="[^"]*/' + re.escape(name) + r'-preview\.jpg"')

            # Explicit mistakes must fail even when a valid automatic cover exists.
            overridden = parent / "override/index.md"
            original = overridden.read_text()
            for invalid, error in (("missing.webp", "missing.webp"),
                                   ("images/missing.jpg", "images/missing.jpg"),
                                   ("https://example.org/cover.jpg", "get_image_metadata")):
                overridden.write_text(original.replace("preview_image: cover.webp", f"preview_image: {invalid}"))
                self.build(root, expected_error=error)
            overridden.write_text(original)
            (parent / "parent-preview.jpg").write_bytes(b"not a valid image")
            self.build(root, expected_error="get_image_metadata")

    def test_news_media_in_articles_listings_and_date_archives(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "config.toml", 'base_url = "https://example.org"\n'
                  'taxonomies = [{name = "news"}]\n'
                  '[translations]\nback = "Back"\n'
                  '[languages.de]\ntaxonomies = [{name = "news"}]\n'
                  '[languages.de.translations]\nback = "Zurück"\n')
            write(root, "templates/base.html", '{% if page %}{% set resource = page %}'
                  '{% elif section %}{% set resource = section %}'
                  '{% else %}{% set resource = get_section(path="news/_index.md", lang=lang) %}{% endif %}'
                  '{% set resource_path = resource.path %}'
                  '{% block og_type %}{% endblock %}{% block article_meta %}{% endblock %}'
                  '{% block content %}{% endblock %}')
            write(root, "templates/_jsonld_news.html", "")
            write(root, "templates/index.html", '{% extends "base.html" %}')
            write(root, "templates/news/single.html", "{{ term.name }}")
            for template in ("_news_media.html", "news/page.html", "news/list.html",
                             "news/date_section.html", "shortcodes/audio.html"):
                write(root, f"templates/{template}", (ROOT / "templates" / template).read_text())
            for suffix, title, slug, description in (
                ("", 'Maps & mountains', "mixed", 'Ridges & valleys at "sunset" <detail>'),
                (".de", 'Karten & Berge', "gemischt", 'Berge & Täler bei "Sonnenuntergang" <Detail>'),
            ):
                write(root, f"content/_index{suffix}.md", "---\ntitle: Home\n---\n")
                write(root, f"content/news/_index{suffix}.md", '---\ntitle: News\n'
                      'render: false\npage_template: news/page.html\n---\n')
                write(root, f"content/news/2024-01-01/_index{suffix}.md", '---\ntitle: News\n'
                      'template: news/date_section.html\n---\n')
                write(root, f"content/news/2024-01-01/1/index{suffix}.md",
                      f'---\ntitle: {title}\nslug: {slug}\ndate: 2024-01-01\n'
                      'taxonomies:\n  news: ["Releases"]\nextra:\n  media_alt:\n'
                      f'    "01-cover.webp": \'{description}\'\n'
                      '    "04-decoration.png": ""\n---\n'
                      '{{ <audio title="Song" url="/news/2024-01-01/mixed/06-voice.MP3" /> }}\n')
                write(root, f"content/news/2024-01-01/2/index{suffix}.md",
                      '---\ntitle: Portrait\nslug: portrait\ndate: 2024-01-01\n'
                      'taxonomies:\n  news: ["Releases"]\n---\nPortrait.\n')
            folder = root / "content/news/2024-01-01/1"
            fixtures = ROOT / "tools/fixtures"
            (root / "content/news/2024-01-01/2/portrait.png").write_bytes((fixtures / "portrait-test.png").read_bytes())
            files = {
                "00-video.MP4": b"video",
                "01-cover.webp": (fixtures / "preview-test.webp").read_bytes(),
                "01-cover.jpg": (fixtures / "preview-test.jpg").read_bytes(),
                "02-detail.jpeg": (fixtures / "preview-test.jpg").read_bytes(),
                "03-portrait.PNG": (fixtures / "portrait-test.png").read_bytes(),
                "04-decoration.png": (fixtures / "portrait-test.png").read_bytes(),
                "05-spaced #image.webp": (fixtures / "preview-test.webp").read_bytes(),
                "06-voice.MP3": b"audio",
            }
            for name in reversed(files):
                (folder / name).write_bytes(files[name])
            self.build(root)
            for prefix, slug, title, description in (
                ("", "mixed", 'Maps & mountains', 'Ridges & valleys at "sunset" <detail>'),
                ("de/", "gemischt", 'Karten & Berge', 'Berge & Täler bei "Sonnenuntergang" <Detail>'),
            ):
                path = f"/{prefix}news/2024-01-01/{slug}/"
                views = {"article": f"{path.lstrip('/')}index.html",
                         "listing": f"{prefix}news/index.html",
                         "date": f"{prefix}news/2024-01-01/index.html"}
                for view, output in views.items():
                    with self.subTest(language=prefix or "en", view=view):
                        html = (root / "public" / output).read_text()
                        parser = NewsMedia()
                        parser.feed(html)
                        self.assertEqual([src for src in parser.order if src.startswith(path)],
                                         [path + quote(name, safe="") for name in sorted(files)
                                          if name not in ("01-cover.jpg", "06-voice.MP3")])
                        self.assertEqual(len(parser.videos), 1)
                        self.assertIn("controls", parser.videos[0])
                        if view != "article":
                            self.assertEqual(parser.videos[0]["preload"], "metadata")
                        self.assertEqual("autoplay" in parser.videos[0], view == "article")
                        self.assertEqual(parser.sources[0]["type"], "video/mp4")
                        # MP3s are embedded by the article's audio component, once.
                        self.assertEqual(len(parser.audio), 1)
                        images = [image for image in parser.images if image["src"].startswith(path)]
                        self.assertEqual(len(images), 5)
                        for index, image in enumerate(images):
                            self.assertEqual(image["loading"], "eager" if view == "article" and index == 0 else "lazy")
                            self.assertEqual(image["decoding"], "async")
                            portrait = index in (2, 3)
                            self.assertEqual((image["width"], image["height"]), ("1", "2") if portrait else ("2", "1"))
                            self.assertEqual(image["class"], "news_image" if portrait else "news_image_landscape")
                            self.assertEqual(image["alt"], description if index == 0 else "" if index == 3 else title)
                        self.assertNotIn('alt="Ridges & valleys at "sunset"', html)
                        if view == "listing":
                            self.assertCountEqual(parser.layouts, ["news_content_image_noflex", "news_content_image"])
                self.assertEqual((root / "public" / path.lstrip("/") / "05-spaced #image.webp").read_bytes(),
                                 files["05-spaced #image.webp"])
                self.assertEqual((root / "public" / path.lstrip("/") / "01-cover.jpg").read_bytes(),
                                 files["01-cover.jpg"])

            for extension in ("PDF", "svg", "mov", "m4a", "gif", "avif", "webm"):
                with self.subTest(unsupported=extension):
                    unsupported = folder / f"unsupported.{extension}"
                    unsupported.write_bytes(b"unsupported")
                    try:
                        self.build(root, expected_error=f"Unsupported news asset '/news/2024-01-01/1/unsupported.{extension}'")
                    finally:
                        unsupported.unlink()

            source = folder / "index.md"
            original = source.read_text()
            for key in ("01-cover.jpg", "01-cover.WEBP", "stale.webp", "00-video.MP4", "06-voice.MP3"):
                with self.subTest(invalid_alt_key=key):
                    source.write_text(original.replace('"01-cover.webp"', f'"{key}"'))
                    try:
                        self.build(root, expected_error=f"media_alt key '{key}' matches no gallery image")
                    finally:
                        source.write_text(original)

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
              '[extra]\nrtl_languages = []\nlanguage_neutral_taxonomy_terms = ["android-auto", "apple-carplay", "linux"]\n'
              'faq_category_titles = {android-auto = "Android Auto", apple-carplay = "Apple CarPlay"}\n'
              'faq_last_categories = ["linux"]\n'
              'faq_topic_ids = {karte = "map", reisen = "app"}\n'
              '[translations]\nfaq-menu-title = "Help"\nfaq-start-here = "Start here"\nfaq-term-description = "FAQ about {}"\n'
              'faq-browse-topics = "Browse topics:"\nfaq-topics = "FAQ topics"\n'
              '[languages.de]\ntaxonomies = [{name = "faq"}]\n'
              '[languages.de.translations]\nfaq-menu-title = "Hilfe"\nfaq-start-here = "Erste Schritte"\nfaq-term-description = "Fragen zu {}"\n'
              'faq-browse-topics = "Themen:"\nfaq-topics = "FAQ-Themen"\n')
        for template in ("base.html", "page.html", "language_redirect.html", "_jsonld_faq.html", "_news_preview.html",
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
            german_term = (root / "public/de/faq/reisen/index.html").read_text()
            breadcrumbs = RenderedPage(menu_id=None)
            breadcrumbs.feed(german_term)
            self.assertEqual(breadcrumbs.links, [("/de/faq/", "Hilfe", "de"), ("/de/faq/karte/", "Karte", "de")])
            self.assertEqual(german_term.count('aria-current="page"'), 1)

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
            self.assertIn('aria-label="FAQ-Themen"', german)
            self.assertIn('href="/de/faq/app/strecke/#stops"', german)
            breadcrumbs = RenderedPage(menu_id=None)
            breadcrumbs.feed((root / "public/de/faq/app/strecke/index.html").read_text())
            self.assertEqual(breadcrumbs.links, [("/de/faq/", "Hilfe", "de"),
                                                ("/de/faq/reisen/", "Reisen", "de")])

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

    def test_linux_faq_follows_mobile_topics_in_every_listing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.faq_site(root)
            config = root / "config.toml"
            config.write_text(config.read_text().replace(
                "[extra]\n", '[extra]\nfaq_translation_status_languages = ["de"]\n').replace(
                'faq_last_categories = ["linux"]', 'faq_last_categories = ["linux", "aaa-linux-übersetzt"]')
                + '\n[slugify]\ntaxonomies = "safe"\n')
            write(root, "templates/faq/translation_status.html",
                  (ROOT / "templates/faq/translation_status.html").read_text())
            write(root, "content/faq/status.md",
                  '---\ntitle: Status\ntemplate: faq/translation_status.html\n---\n')
            # A configured localized category must move last even when it sorts first.
            for suffix, category in (("", "linux"), (".de", "aaa-linux-übersetzt")):
                write(root, f"content/faq/linux/how-to-use-flatpak/index{suffix}.md",
                      f'---\ntitle: Flatpak\ntaxonomies:\n  faq: ["{category}"]\n'
                      'extra:\n  order: 10\n---\n')
            self.build(root)
            for prefix, categories in (("", ["app", "map", "linux"]),
                                       ("de/", ["karte", "reisen", "aaa-linux-übersetzt"])):
                landing = (root / "public" / prefix / "faq/index.html").read_text()
                links = re.findall(r'<h2[^>]*><a href="([^"]+)"', landing)
                self.assertEqual(links, [f"/{prefix}faq/{category}/" for category in categories])

            for page in ("de/faq/app/strecke/index.html", "de/faq/reisen/index.html",
                         "de/faq/aaa-linux-übersetzt/index.html"):
                output = (root / "public" / page).read_text()
                menu = re.search(r'<nav class="faq-breadcrumbs".*?</nav>', output, re.S).group()
                labels = re.findall(r'class="faq-taxonomy"[^>]*>([^<]+)</(?:a|span)>', menu)
                self.assertEqual(labels, ["Karte", "Reisen", "Aaa linux übersetzt"])

            status = (root / "public/faq/status/index.html").read_text()
            categories = re.findall(r'<tr class="faq_category">\s*<td[^>]*>([^<]+)</td>', status)
            self.assertEqual(categories, ["App", "Map", "Linux"])

    def test_car_display_topics_keep_branding_and_answer_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.faq_site(root)
            topics = {"android-auto": ("app/how-to-use-android-auto", "Android Auto"),
                      "apple-carplay": ("voice/carplay", "Apple CarPlay")}
            for topic, (answer, label) in topics.items():
                for suffix in ("", ".de"):
                    write(root, f"content/faq/{answer}/index{suffix}.md",
                          f'---\ntitle: {label} setup\ntaxonomies:\n  faq: ["{topic}"]\n'
                          'extra:\n  order: 10\n---\n\nConnect a compatible car.\n')
            self.build(root)
            for prefix, section in (("", "Help"), ("de/", "Hilfe")):
                landing = (root / "public" / prefix / "faq/index.html").read_text()
                for topic, (answer, label) in topics.items():
                    with self.subTest(language=prefix, topic=topic):
                        topic_path = f"/{prefix}faq/{topic}/"
                        article_path = f"/{prefix}faq/{answer}/"
                        term = (root / "public" / topic_path.strip("/") / "index.html").read_text()
                        self.assertIn(f"<title>{label} – {section} – Organic Maps</title>", term)
                        self.assertIn(f'href="{topic_path}">{label}</a>', landing)
                        self.assertIn(f'href="{article_path}"', term)
                        article = (root / "public" / article_path.strip("/") / "index.html").read_text()
                        data = [json.loads(value) for value in re.findall(
                            r'<script type="application/ld\+json">(.*?)</script>', article, re.S)]
                        crumbs = next(value for value in data if value["@type"] == "BreadcrumbList")
                        self.assertEqual(crumbs["itemListElement"][1], {
                            "@type": "ListItem", "position": 2, "name": label,
                            "item": "https://example.org" + topic_path})
                        self.assertIn(f'href="{topic_path}" class="faq-taxonomy">{label}</a>', article)

    def test_embedded_faq_rewrites_headings_and_retains_aliases(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "config.toml", 'base_url = "https://example.org"\n'
                  '[slugify]\npaths = "safe"\n[languages.ru]\n')
            write(root, "templates/page.html", '{% set embedded_page = page %}'
                  '{% set faq_page_en = get_page(path="route.md") %}'
                  '{% set html_lang = lang %}{% set faq_bundled_pages = [] %}'
                  '{% include "faq/_embedded_content.html" %}')
            write(root, "templates/faq/_embedded_content.html",
                  (ROOT / "templates/faq/_embedded_content.html").read_text())
            body = '[Jump](#target)\n\n## Heading {#target}\n\n<span id="target"></span>\n'
            write(root, "content/route.md", '---\ntitle: Route\n---\n\n' + body)
            write(root, "content/route.ru.md", '---\ntitle: Маршрут\nslug: маршрут\n---\n\n' + body)
            self.build(root)
            output = (root / "public/ru/маршрут/index.html").read_text()
            self.assertIn('href="#ru-target"', output)
            self.assertIn('<h2 id="ru-target">', output)
            self.assertIn('<span id="target">', output)

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
