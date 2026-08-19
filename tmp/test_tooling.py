#!/usr/bin/env python3
"""Focused, offline regressions for translation, hooks and Telegram tooling."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from deepl_glossary import dictionary_for_probe, load_terms  # noqa: E402
from social_post import (  # noqa: E402
    PostError,
    dump_post,
    load_post,
    resolve_media,
    social_dir_for,
    text_fields,
)
from telegram_post import (  # noqa: E402
    classify_media,
    convert_markdown_to_telegramv2,
    send_media,
    split_text,
    utf16_len,
    validate_media_set,
    visible_text,
)
from telegram_post_all import creatives_for, find_creatives_root  # noqa: E402
from translate_check import ERROR, check_translation, emphasis_faults  # noqa: E402
from translate_md import _segments, register_ok, tidy  # noqa: E402

try:  # Pillow is only needed to render, not to check the slide script
    import social_build  # noqa: E402
except ImportError:  # pragma: no cover
    social_build = None


class FakeResponse:
    def __init__(self, payload: dict):
        self.payload = payload

    def json(self) -> dict:
        return self.payload


class TranslationToolingTests(unittest.TestCase):
    def test_translation_imports_do_not_require_requests(self):
        code = """
import importlib.abc, sys
class Block(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == 'requests' or fullname.startswith('requests.'):
            raise ModuleNotFoundError("No module named 'requests'")
sys.meta_path.insert(0, Block())
import translate_check, translate_md
"""
        result = subprocess.run(
            [sys.executable, "-c", code], cwd=ROOT / "tools",
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_only_declared_currency_references_may_be_omitted(self):
        source = (ROOT / "content/donate/index.md").read_text(encoding="utf-8")
        cases = (("ru", "stripe_uah"), ("uk", "stripe_rub"))
        for lang, omitted in cases:
            translated = (ROOT / f"content/donate/index.{lang}.md").read_text(
                encoding="utf-8"
            )
            errors = [
                p for p in check_translation(source, translated, lang)
                if p.level == ERROR
            ]
            self.assertEqual(errors, [], lang)

            undeclared = translated.replace(
                f'  translation_omits_refs: ["{omitted}"]\n', ""
            )
            self.assertIn(
                "structure",
                {p.code for p in check_translation(source, undeclared, lang)},
            )

            invalid = translated.replace(omitted, "github", 1)
            self.assertIn(
                "ref-omission-invalid",
                {p.code for p in check_translation(source, invalid, lang)},
            )

    def test_estonian_page_uses_informal_singular(self):
        text = (ROOT / "content/news/2025-12-31/500/index.et.md").read_text(
            encoding="utf-8"
        )
        self.assertEqual(register_ok(text, "et"), (True, "et: informal as expected"))

    def test_quoted_speech_does_not_set_the_audience_register(self):
        quoted = 'Mesajı: "Hepinize teşekkür ederim".'
        self.assertEqual(register_ok(quoted, "tr"), (True, "tr: register not applicable"))

    def test_link_punctuation_moves_after_balanced_target(self):
        self.assertEqual(
            tidy("[下载，](https://example.com/a_(b))", "zh-Hans"),
            "[下载](https://example.com/a_(b))，",
        )

    def test_code_span_inside_bold_is_valid_emphasis(self):
        self.assertEqual(
            emphasis_faults("**`[label](target)` takes no space.**"), []
        )

    def test_fenced_code_never_enters_translation_payload(self):
        payloads, _ = _segments("Before\n```bash\necho hello\n```\nAfter")
        self.assertEqual(payloads, ["Before", "After"])

    def test_probe_builds_unknown_and_variant_targets(self):
        terms = load_terms()
        af, af_target = dictionary_for_probe(terms, "af")
        pt_br, pt_target = dictionary_for_probe(terms, "pt-BR")
        self.assertEqual((af_target, len(af)), ("af", 1))
        self.assertEqual((pt_target, len(pt_br)), ("pt", 1))


class TelegramToolingTests(unittest.TestCase):
    def test_parenthesized_url_is_complete_and_escaped(self):
        converted = convert_markdown_to_telegramv2(
            "[x](https://example.com/a_(b))"
        )
        self.assertEqual(converted, r"[x](https://example.com/a_(b\))")
        self.assertEqual(visible_text(converted), "x")

    def test_utf16_hard_split_respects_limit(self):
        chunks = split_text("😀" * 4097)
        self.assertEqual("".join(chunks), "😀" * 4097)
        self.assertTrue(
            all(utf16_len(visible_text(chunk)) <= 4096 for chunk in chunks)
        )

    def test_audio_classification_and_album_rules(self):
        self.assertEqual(classify_media(Path("clip.mp3")), "audio")
        self.assertEqual(classify_media(Path("clip.m4a")), "audio")
        self.assertIsNone(classify_media(Path("clip.wav")))
        self.assertIsNone(validate_media_set([Path("a.mp3"), Path("b.m4a")]))
        self.assertIsNone(validate_media_set([Path("a.jpg"), Path("b.mp4")]))
        self.assertIn(
            "audio files only",
            validate_media_set([Path("a.mp3"), Path("b.jpg")]) or "",
        )
        self.assertIn(
            "at most 10",
            validate_media_set([Path(f"{i}.jpg") for i in range(11)]) or "",
        )

    def test_single_audio_uses_send_audio(self):
        with tempfile.TemporaryDirectory() as folder:
            audio = Path(folder) / "clip.mp3"
            audio.write_bytes(b"audio")
            with patch(
                "telegram_post.requests.post",
                return_value=FakeResponse({"ok": True, "result": {}}),
            ) as request:
                result = send_media("token", "chat", [audio])
        self.assertTrue(result["ok"])
        self.assertTrue(request.call_args.args[0].endswith("/sendAudio"))
        self.assertIn("audio", request.call_args.kwargs["files"])

    def test_audio_album_uses_homogeneous_media_group(self):
        with tempfile.TemporaryDirectory() as folder:
            paths = [Path(folder) / "one.mp3", Path(folder) / "two.m4a"]
            for path in paths:
                path.write_bytes(b"audio")
            with patch(
                "telegram_post.requests.post",
                return_value=FakeResponse({"ok": True, "result": []}),
            ) as request:
                result = send_media("token", "chat", paths)
        self.assertTrue(result["ok"])
        self.assertTrue(request.call_args.args[0].endswith("/sendMediaGroup"))
        media = json.loads(request.call_args.kwargs["data"]["media"])
        self.assertEqual([entry["type"] for entry in media], ["audio", "audio"])

    def test_media_api_failure_is_returned(self):
        with tempfile.TemporaryDirectory() as folder:
            audio = Path(folder) / "clip.mp3"
            audio.write_bytes(b"audio")
            with patch(
                "telegram_post.requests.post",
                return_value=FakeResponse({"ok": False, "description": "rejected"}),
            ):
                result = send_media("token", "chat", [audio])
        self.assertFalse(result["ok"])


class StagedHookTests(unittest.TestCase):
    def run_git(self, folder: Path, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["git", *args], cwd=folder, capture_output=True, text=True, check=True
        )

    def test_cached_checks_ignore_unstaged_masking_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            self.run_git(folder, "init", "-q")
            self.run_git(folder, "config", "user.name", "Test")
            self.run_git(folder, "config", "user.email", "test@example.com")

            sample = folder / "sample.md"
            source = folder / "content/example/index.md"
            translated = folder / "content/example/index.ru.md"
            source.parent.mkdir(parents=True)
            sample.write_text("[good](https://example.com)\n", encoding="utf-8")
            source.write_text("Organic Maps works.\n", encoding="utf-8")
            translated.write_text("Organic Maps работает.\n", encoding="utf-8")
            self.run_git(folder, "add", ".")
            self.run_git(folder, "commit", "-qm", "baseline")

            # Broken staged syntax hidden by a corrected working-tree version.
            sample.write_text("[bad] (https://example.com)\n", encoding="utf-8")
            self.run_git(folder, "add", "sample.md")
            sample.write_text("[good](https://example.com)\n", encoding="utf-8")
            syntax = subprocess.run(
                [sys.executable, str(ROOT / "tools/translate_check.py"),
                 "--cached", "--syntax", "sample.md"],
                cwd=folder, capture_output=True, text=True,
            )
            self.assertEqual(syntax.returncode, 1, syntax.stdout + syntax.stderr)

            # Broken staged translation hidden by the correct working tree.
            translated.write_text("Карты работают.\n", encoding="utf-8")
            self.run_git(folder, "add", "content/example/index.ru.md")
            translated.write_text("Organic Maps работает.\n", encoding="utf-8")
            regression = subprocess.run(
                [sys.executable, str(ROOT / ".githooks/regression_check.py"),
                 "content/example/index.md", "content/example/index.ru.md", "ru"],
                cwd=folder, capture_output=True, text=True,
            )
            self.assertEqual(
                regression.returncode, 1, regression.stdout + regression.stderr
            )

            # Correct staged translation must not be blamed for an unstaged break.
            self.run_git(folder, "add", "content/example/index.ru.md")
            translated.write_text("Карты работают.\n", encoding="utf-8")
            regression = subprocess.run(
                [sys.executable, str(ROOT / ".githooks/regression_check.py"),
                 "content/example/index.md", "content/example/index.ru.md", "ru"],
                cwd=folder, capture_output=True, text=True,
            )
            self.assertEqual(
                regression.returncode, 0, regression.stdout + regression.stderr
            )


SAMPLE_POST = """\
release = "2026-07-23-620"
source = "content/news/2026-07-23/620"
lang = "en"
formats = ["4x5"]

[[slides]]
type = "cover"
kicker = "Organic Maps"
title = "July Update"
subtitle = "One sentence."

[[slides]]
type = "feature"
eyebrow = "Routing"
title = "Warnings on every route"
body = "Tolls and ferries are flagged."
media = "Barriers on a route.jpg"
device = "desktop"
theme = "green"

[[slides]]
type = "list"
title = "Smoother day to day"
items = ["Opening hours", "Cleaner search bar"]
theme = "light"

[[slides]]
type = "cta"
title = "Get the July update"
url = "get.omaps.org"
badges = ["apple-appstore", "googleplay"]
"""


class SocialPostTests(unittest.TestCase):
    def write_post(self, folder: Path, text: str = SAMPLE_POST) -> Path:
        path = folder / "post.toml"
        path.write_text(text, encoding="utf-8")
        return path

    def test_dumped_post_parses_back_identically(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_post(Path(tmp))
            post = load_post(path)
            path.write_text(dump_post(post), encoding="utf-8")
            self.assertEqual(load_post(path), post)

    def test_only_prose_is_offered_for_translation(self):
        with tempfile.TemporaryDirectory() as tmp:
            post = load_post(self.write_post(Path(tmp)))
            translatable = {
                value
                for slide in post["slides"]
                for _, _, value in text_fields(slide)
            }
            self.assertIn("Warnings on every route", translatable)
            self.assertIn("Opening hours", translatable)
            # A translated file path, theme, badge or short URL would break the
            # render or point the reader somewhere else.
            for identifier in (
                "Barriers on a route.jpg", "desktop", "green",
                "get.omaps.org", "apple-appstore",
            ):
                self.assertNotIn(identifier, translatable)

    def test_a_broken_slide_script_is_rejected_before_rendering(self):
        cases = {
            "unknown type": SAMPLE_POST.replace('type = "cover"', 'type = "hero"'),
            "no title": SAMPLE_POST.replace('title = "July Update"\n', ""),
            "unknown theme": SAMPLE_POST.replace('theme = "light"', 'theme = "teal"'),
            "unknown badge": SAMPLE_POST.replace('"googleplay"', '"playstore"'),
            "no slides": 'release = "x"\n',
        }
        for name, text in cases.items():
            with self.subTest(name), tempfile.TemporaryDirectory() as tmp:
                path = self.write_post(Path(tmp), text)
                with self.assertRaises(PostError):
                    load_post(path)

    def test_media_is_found_in_the_news_folder_it_came_from(self):
        with tempfile.TemporaryDirectory() as tmp:
            post = load_post(self.write_post(Path(tmp)))
            found = resolve_media(post, Path(tmp), "Barriers on a route.jpg")
            self.assertEqual(
                found,
                ROOT / "content/news/2026-07-23/620/Barriers on a route.jpg",
            )
            with self.assertRaises(PostError):
                resolve_media(post, Path(tmp), "nothing-here.jpg")

    def test_a_news_folder_maps_to_its_social_folder(self):
        self.assertEqual(
            social_dir_for(ROOT / "content/news/2026-07-23/620"),
            ROOT / "social/2026-07-23-620",
        )


class CreativeSelectionTests(unittest.TestCase):
    """Which images each Telegram channel is handed."""

    def make_export(self, root: Path, langs: tuple[str, ...]) -> Path:
        export = root / "export"
        for lang in langs:
            folder = export / lang / "4x5"
            folder.mkdir(parents=True)
            for name in ("01-cover.png", "02-feature.png"):
                (folder / name).write_bytes(b"png")
        # The contact sheet sits beside the format folder precisely so it is
        # never posted as one of the slides.
        for lang in langs:
            (export / lang / "sheet-4x5.png").write_bytes(b"png")
        return export

    def test_a_channel_gets_its_own_language(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = self.make_export(Path(tmp), ("en", "ru"))
            picked = creatives_for(export, "ru", "4x5")
            self.assertEqual([p.name for p in picked],
                             ["01-cover.png", "02-feature.png"])
            self.assertTrue(all(p.parent.parent.name == "ru" for p in picked))

    def test_an_unrendered_language_falls_back_to_english(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = self.make_export(Path(tmp), ("en",))
            picked = creatives_for(export, "tr", "4x5")
            self.assertTrue(picked)
            self.assertTrue(all(p.parent.parent.name == "en" for p in picked))

    def test_nothing_rendered_means_nothing_picked(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = self.make_export(Path(tmp), ("de",))
            self.assertEqual(creatives_for(export, "tr", "4x5"), [])
            self.assertEqual(creatives_for(None, "de", "4x5"), [])
            # A format that was not rendered is not silently swapped either.
            self.assertEqual(creatives_for(export, "de", "9x16"), [])

    def test_a_post_without_creatives_reports_none(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(find_creatives_root(Path(tmp), None))


@unittest.skipIf(social_build is None, "Pillow is not installed")
class SlideRenderingTests(unittest.TestCase):
    def render(self, slide: dict, fmt: str = "4x5", **kwargs) -> str:
        post = {"slides": [slide], "source": "content/news/2026-07-23/620"}
        return social_build.render_html(
            post, slide, ROOT / "social/2026-07-23-620", fmt, 1, 1, **kwargs
        )

    def test_copy_is_escaped_rather_than_injected(self):
        html = self.render({"type": "list", "title": 'Tracks & "routes" <b>'})
        self.assertIn("Tracks &amp; &quot;routes&quot; &lt;b&gt;", html)
        self.assertNotIn("<b>", html)

    def test_a_bleeding_phone_keeps_its_pixel_override(self):
        html = self.render({
            "type": "feature", "title": "Pick any color",
            "media": "Colors for bookmarks and tracks.jpg",
            "device": "phone", "bleed": 120,
        })
        self.assertIn("--bleed:120px", html)
        self.assertIn("slide feature bleed", html)

    def test_the_platform_decides_the_frame(self):
        cases = [
            ({"eyebrow": "iOS · Bookmarks"}, "iphone"),
            ({"eyebrow": "iOS · Метки"}, "iphone"),          # survives translation
            ({"eyebrow": "Android"}, "android"),
            ({"eyebrow": "Routing"}, "phone"),               # no platform named
            ({}, "phone"),
            # An explicit device is never second-guessed.
            ({"eyebrow": "iOS · Bookmarks", "device": "phone"}, "iphone"),
            ({"eyebrow": "iOS · Bookmarks", "device": "android"}, "android"),
            ({"eyebrow": "Android", "device": "desktop"}, "desktop"),
        ]
        for slide, expected in cases:
            with self.subTest(slide):
                self.assertEqual(social_build.device_of(dict(slide)), expected)

    def test_a_phone_of_any_platform_bleeds_off_the_canvas(self):
        for eyebrow, frame in (("iOS", "iphone"), ("Android", "android")):
            slide = {"type": "feature", "title": "x", "eyebrow": eyebrow,
                     "media": "Colors for bookmarks and tracks.jpg"}
            html = self.render(slide)
            self.assertIn(f'class="device {frame}"', html)
            self.assertIn("slide feature bleed", html)
            # The frame is sized from the screenshot's own pixels.
            self.assertIn("--shot:884/1920", html)
            # A platform frame puts its camera cutout back.
            self.assertIn('class="cutout"', html)

    def test_an_unknown_device_gets_no_cutout(self):
        for device in ("phone", "desktop", "plain"):
            slide = {"type": "feature", "title": "x", "device": device,
                     "media": "Colors for bookmarks and tracks.jpg"}
            self.assertNotIn("cutout", self.render(slide), device)

    def test_right_to_left_languages_are_marked_as_such(self):
        slide = {"type": "list", "title": "قائمة"}
        self.assertIn("dir='rtl'", self.render(slide, rtl=True))
        self.assertNotIn("dir='rtl'", self.render(slide))


if __name__ == "__main__":
    unittest.main(verbosity=2)
