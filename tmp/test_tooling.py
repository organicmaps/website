#!/usr/bin/env python3
"""Focused, offline regressions for translation, hooks and Telegram tooling."""

import argparse
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from deepl_glossary import dictionary_for_probe, load_terms  # noqa: E402
from telegram_post import (  # noqa: E402
    RTL_LANGS,
    build_rich_markdown,
    classify_media,
    convert_markdown_to_telegramv2,
    find_raw_html,
    is_rtl_lang,
    rich_media_id,
    send_media,
    send_rich_message,
    split_text,
    strip_tera_blocks,
    utf16_len,
    validate_media_set,
    validate_rich_message,
    visible_text,
)
from telegram_post_all import format_flags  # noqa: E402
from translate_check import ERROR, check_translation, emphasis_faults  # noqa: E402
from translate_md import _segments, register_ok, tidy  # noqa: E402


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
        cases = (("uk", "stripe_rub"),)
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

    def test_nested_frontmatter_prose_and_placeholders_are_checked(self):
        source = """---
title: Support
description: Donation form
template: donate-subscribe.html
extra:
  preview_image: donate/donate.png
  form:
    interval_label: How often?
    submit_once: Donate {amount}
    error_range: Between {min} and {max}
---

Organic Maps.
"""
        translated = """---
title: 支援
description: 寄付フォーム
template: donate-subscribe.html
extra:
  preview_image: donate/donate.png
  form:
    interval_label: How often?
    submit_once: 寄付する {sum}
    error_range: "{min} から {max}"
---

Organic Maps。
"""
        problems = check_translation(source, translated, "ja")
        self.assertTrue(
            any(
                "extra.form.interval_label" in p.message
                for p in problems
                if p.code == "untranslated-frontmatter"
            ),
            problems,
        )
        self.assertEqual(
            [p.message for p in problems if p.code == "placeholder-mismatch"],
            ["'extra.form.submit_once' must keep the placeholder(s) verbatim"],
        )

    def test_source_keep_declarations_are_verified(self):
        source = """---
title: Privacy
extra:
  menu_title: Privacy
---

Organic Maps.
"""
        valid = """---
title: プライバシー
extra:
  menu_title: Privacy
  translation_keeps_source: ["extra.menu_title"]
---

Organic Maps。
"""
        self.assertNotIn(
            "untranslated-frontmatter",
            {p.code for p in check_translation(source, valid, "ja")},
        )

        stale = valid.replace("menu_title: Privacy", "menu_title: プライバシー")
        self.assertIn(
            "translation-keeps-source",
            {p.code for p in check_translation(source, stale, "ja")},
        )

        unknown = valid.replace("extra.menu_title", "extra.missing")
        self.assertIn(
            "translation-keeps-source",
            {p.code for p in check_translation(source, unknown, "ja")},
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
    def test_current_tera_components_are_removed_from_posts(self):
        text = (
            "Before\n\n{{ <screenshot\n"
            "  src='/image.jpg'\n"
            "  alt='Map'\n"
            "/> }}\n\nAfter"
        )
        self.assertEqual(strip_tera_blocks(text), "Before\n\n\n\nAfter")

    def test_line_break_tag_becomes_a_line_break(self):
        # Zola renders <br/>; MarkdownV2 has no HTML and would escape it, which
        # printed a literal "<br/>" in every channel of the 2026-08-31 release.
        converted = convert_markdown_to_telegramv2(
            "With love and gratitude,<br/>\nOrganic Maps Team"
        )
        self.assertEqual(
            converted, "With love and gratitude,\nOrganic Maps Team"
        )
        self.assertEqual(convert_markdown_to_telegramv2("a<br>b"), "a\nb")
        self.assertEqual(
            convert_markdown_to_telegramv2("a<br /><br/>b"), "a\n\nb"
        )
        # A tag inside a code span is content, not markup.
        self.assertEqual(
            convert_markdown_to_telegramv2("`<br/>`"), "`<br/>`"
        )

    def test_raw_html_is_reported_but_autolinks_are_not(self):
        found = find_raw_html(
            "<pre>\ntext <u>a</u> <https://omaps.app/> `<i>` <br/>"
        )
        self.assertEqual(
            found, [("<pre>", 1), ("<u>", 2), ("</u>", 2)]
        )

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


class RichMessageTests(unittest.TestCase):
    """Bot API 10.1 rich messages: one GFM message instead of escaped chunks."""

    def test_structure_survives_and_media_becomes_blocks(self):
        markdown = build_rich_markdown(
            "# Title\n\n## Section\n\n- item\n\nSigned,<br/>\nThe Team",
            [Path("a.jpg"), Path("clip.mp4")],
        )
        self.assertEqual(
            markdown,
            "# Title\n\n## Section\n\n- item\n\nSigned,  \nThe Team\n\n"
            "![](tg://photo?id=m0-a)\n\n![](tg://video?id=m1-clip)",
        )

    def test_line_break_becomes_a_hard_break_not_a_soft_one(self):
        # Rich Markdown joins consecutive lines like CommonMark, so a bare
        # newline would silently turn the signature into one run-on line.
        self.assertEqual(build_rich_markdown("a<br/>\nb"), "a  \nb")
        self.assertEqual(build_rich_markdown("a<br>b"), "a  \nb")
        self.assertEqual(build_rich_markdown("a<br/>"), "a")

    def test_media_ids_are_unique_and_use_the_allowed_alphabet(self):
        ids = [
            rich_media_id(Path(name), i)
            for i, name in enumerate(["a.jpg", "a.png", "01-car dash.jpg"])
        ]
        self.assertEqual(len(set(ids)), 3)
        for value in ids:
            self.assertRegex(value, r"^[A-Za-z0-9_-]{1,64}$")
        long_id = rich_media_id(Path("x" * 200 + ".jpg"), 7)
        self.assertTrue(long_id.startswith("m7-"))
        self.assertEqual(len(long_id), 64)

    def test_rtl_languages_match_the_site_template(self):
        template = (ROOT / "templates" / "base.html").read_text(encoding="utf-8")
        declared = re.search(r"set rtl_langs = \[(.*?)\]", template, re.S)
        self.assertIsNotNone(declared)
        self.assertEqual(
            set(re.findall(r'"([^"]+)"', declared.group(1))), set(RTL_LANGS)
        )
        self.assertTrue(is_rtl_lang("ar"))
        self.assertTrue(is_rtl_lang("fa-IR"))
        self.assertFalse(is_rtl_lang("ru"))
        self.assertFalse(is_rtl_lang("en"))

    def test_payload_carries_markdown_media_and_direction(self):
        posted = {}

        def fake_post(url, data=None, files=None, **kwargs):
            posted.update(url=url, data=data, files=files)
            return FakeResponse({"ok": True, "result": {"message_id": 1}})

        with tempfile.TemporaryDirectory() as tmp:
            photo = Path(tmp) / "shot.jpg"
            photo.write_bytes(b"\xff\xd8\xff")
            with patch("telegram_post.requests.post", fake_post):
                result = send_rich_message(
                    "TOKEN", "@chan", "Hello", [photo], is_rtl=True
                )

        self.assertTrue(result["ok"])
        self.assertTrue(posted["url"].endswith("/sendRichMessage"))
        self.assertEqual(posted["data"]["chat_id"], "@chan")
        payload = json.loads(posted["data"]["rich_message"])
        self.assertEqual(
            payload["markdown"], "Hello\n\n![](tg://photo?id=m0-shot)"
        )
        self.assertEqual(
            payload["media"],
            [
                {
                    "id": "m0-shot",
                    "media": {"type": "photo", "media": "attach://file0"},
                }
            ],
        )
        self.assertIs(payload["is_rtl"], True)
        self.assertEqual(posted["files"]["file0"][0], "shot.jpg")

    def test_direction_and_media_are_omitted_when_absent(self):
        posted = {}

        def fake_post(url, data=None, files=None, **kwargs):
            posted.update(data=data)
            return FakeResponse({"ok": True})

        with patch("telegram_post.requests.post", fake_post):
            send_rich_message("TOKEN", "@chan", "Hello")
        payload = json.loads(posted["data"]["rich_message"])
        self.assertNotIn("is_rtl", payload)
        self.assertNotIn("media", payload)

    def test_limits_are_refused_before_anything_is_published(self):
        self.assertIsNone(validate_rich_message("Hello", []))
        self.assertIn("empty", validate_rich_message("  \n", []))
        self.assertIn(
            "over Telegram's limit", validate_rich_message("x" * 32769, [])
        )
        self.assertIn(
            "unsupported media file(s): notes.txt",
            validate_rich_message("Hello", [Path("notes.txt")]),
        )

        def explode(*args, **kwargs):
            raise AssertionError("an invalid rich message must not be sent")

        with patch("telegram_post.requests.post", explode):
            result = send_rich_message("TOKEN", "@chan", "x" * 32769)
        self.assertFalse(result["ok"])

    def test_code_is_content_not_markup(self):
        # The MarkdownV2 path protects code; the rich path must too, or a post
        # documenting HTML loses the very tag it is documenting.
        self.assertEqual(
            build_rich_markdown("Use `<br/>` for a break"),
            "Use `<br/>` for a break",
        )
        self.assertEqual(
            build_rich_markdown("```html\n<br/>\n```"), "```html\n<br/>\n```"
        )
        self.assertEqual(
            build_rich_markdown("`<br>` then a<br/>\nb"), "`<br>` then a  \nb"
        )

    def test_tags_in_code_are_not_reported_and_line_numbers_hold(self):
        found = find_raw_html("```html\n<div>x</div>\n```\n<marquee>y</marquee>")
        self.assertEqual(found, [("<marquee>", 4), ("</marquee>", 4)])

    def test_length_is_refused_under_either_reading_of_the_limit(self):
        # "32768 UTF-8 characters" reads as code points but may mean bytes.
        under_both = "a" * 32768
        self.assertIsNone(validate_rich_message(under_both, []))
        over_bytes_only = "я" * 20000  # 20000 characters, 40000 UTF-8 bytes
        self.assertIn(
            "over Telegram's limit",
            validate_rich_message(over_bytes_only, []),
        )

    def test_resume_hint_carries_the_flags_that_set_the_format(self):
        def flags(**kwargs):
            defaults = {"rich": False, "allow_plain_fallback": False}
            return format_flags(argparse.Namespace(**{**defaults, **kwargs}))

        self.assertEqual(flags(), "")
        self.assertEqual(flags(rich=True), " --rich")
        self.assertEqual(
            flags(allow_plain_fallback=True), " --allow-plain-fallback"
        )

    def test_an_oversized_post_is_refused_before_any_channel_is_posted(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / "index.md").write_text(
                "---\ntitle: Too long\n---\n\n" + "word " * 8000,
                encoding="utf-8",
            )
            run = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools/telegram_post_all.py"),
                    str(folder),
                    "--rich",
                    "--dry-run",
                    "--yes",
                ],
                capture_output=True,
                text=True,
            )
        self.assertEqual(run.returncode, 1, run.stdout + run.stderr)
        self.assertIn("Telegram would reject", run.stderr)
        self.assertNotIn("Would send", run.stdout)

    def test_supported_html_is_reported_only_outside_rich_mode(self):
        text = "<u>a</u> and <marquee>b</marquee>"
        self.assertEqual(
            [tag for tag, _ in find_raw_html(text)],
            ["<u>", "</u>", "<marquee>", "</marquee>"],
        )
        self.assertEqual(
            [tag for tag, _ in find_raw_html(text, rich=True)],
            ["<marquee>", "</marquee>"],
        )


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
