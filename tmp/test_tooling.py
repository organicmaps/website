#!/usr/bin/env python3
"""Focused, offline regressions for FAQ metadata, translation, hooks and Telegram."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from deepl_glossary import dictionary_for_probe, load_terms  # noqa: E402
from markdown_frontmatter import strip_frontmatter  # noqa: E402
from telegram_post import (  # noqa: E402
    classify_media,
    convert_markdown_to_telegramv2,
    send_media,
    split_text,
    strip_tera_blocks,
    utf16_len,
    validate_media_set,
    visible_text,
)
from translate_check import ERROR, check_translation, emphasis_faults  # noqa: E402
from translate_md import (  # noqa: E402
    _segments, localize_zola_links, register_ok, tidy, translate_post, translate_text,
)


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

    def test_register_is_checked_in_reader_visible_frontmatter(self):
        source = "---\ntitle: Support\nextra:\n  form:\n    canceled_notice: Your payment was canceled.\n---\n\nOrganic Maps.\n"
        translated = "---\ntitle: Unterstütze uns\nextra:\n  form:\n    canceled_notice: Ihre Zahlung wurde storniert.\n---\n\nOrganic Maps.\n"
        warnings = [p for p in check_translation(source, translated, "de")
                    if p.code == "register-frontmatter"]
        self.assertEqual(len(warnings), 1)
        self.assertIn("extra.form.canceled_notice", warnings[0].message)
        self.assertFalse(any(p.code == "register-frontmatter"
                             for p in check_translation(
                                 source, translated.replace("Ihre", "Deine"), "de")))

    def test_sentence_initial_occitan_address_is_detected(self):
        self.assertFalse(register_ok("Vòstre pagament es estat anullat.", "oc")[0])
        self.assertTrue(register_ok("Ton pagament es estat anullat.", "oc")[0])

    def test_translation_pipeline_preserves_ignored_spans_and_repairs_prose(self):
        source = '''"Hello"... Use `print("hello...")` and ``a ` b``.

Before {{ value | replace(from="}}", to="{done}") }} after.

<!--
## Internal heading
- Internal item
-->

{{ <screenshot
  src="/internal.png"
  alt="Internal alt"
/> }}

~~~text
## Internal code
print("hello...")
~~~

````text
```
Internal code
```
````

Read [ the docs， ](https://example.com/a_(b)?next=...) now.
'''
        expected = source.replace('"Hello"...', '“Hello”…').replace(
            '[ the docs， ](https://example.com/a_(b)?next=...)',
            '[the docs](https://example.com/a_(b)?next=...)，',
        )

        def identity(payloads, *args, **kwargs):
            for payload in payloads:
                ElementTree.fromstring(f"<root>{payload}</root>")
                self.assertNotIn("Internal", payload)
                self.assertNotIn('print(', payload)
                self.assertNotIn('replace(', payload)
                self.assertNotIn('https://', payload)
            return payloads, None

        with patch("translate_md.brands_visible", return_value=False), \
             patch("translate_md.deepl_translate", side_effect=identity):
            self.assertEqual(translate_text(source, "zh-Hans", use_glossary=False), expected)

    def test_soft_line_break_inside_formatting_keeps_api_text_valid_xml(self):
        source = "Before **two\nlines** after.\n\nNext paragraph."
        with patch("translate_md.brands_visible", return_value=False), \
             patch("translate_md.deepl_translate", side_effect=lambda texts, *a, **k: (texts, None)) as request:
            self.assertEqual(translate_text(source, "fr", use_glossary=False), source)
        for payload in request.call_args.args[0]:
            ElementTree.fromstring(f"<root>{payload}</root>")

    def test_frontmatter_cleanup_preserves_code_and_extra_fields(self):
        source = '''---
title: 'Use `print("hello...")`'
extra:
  label: "Leave this field unchanged..."
---

Body.
'''
        with patch("translate_md.brands_visible", return_value=False), \
             patch("translate_md.get_glossary_id", return_value=None), \
             patch("translate_md.deepl_translate", side_effect=lambda texts, *a, **k: (texts, None)):
            translated = translate_post(source, "fr", use_glossary=False)
        self.assertEqual(strip_frontmatter(source)[1], strip_frontmatter(translated)[1])

    def test_links_localize_without_translating_protected_examples(self):
        target = "@/contribute/index.md"
        source = f'[Organic Maps]({target})\n\n`[example]({target})`'
        with patch("translate_md.brands_visible", return_value=False), \
             patch("translate_md.deepl_translate") as request:
            translated = translate_text(source, "fr", use_glossary=False)
        self.assertEqual(translated, f'[Organic Maps](@/contribute/index.fr.md)\n\n`[example]({target})`')
        request.assert_not_called()
        for literal in [f'[docs](https://example.com "Example {target}")',
                        f'<a href="{target}">example</a>']:
            self.assertEqual(localize_zola_links(literal, "fr"), literal)

    def test_tidy_keeps_literal_spans_while_unquoting_brands(self):
        self.assertEqual(
            tidy('"Organic Maps" says "hello"... `print("hello...")`', "fr"),
            'Organic Maps says «hello»… `print("hello...")`',
        )

    def test_section_note_skips_only_body_checks(self):
        source = """---
render: false
title: Frequently Asked Questions
description: Questions about Organic Maps
extra:
  menu_title: Help
---

### This page is replaced with taxonomy "faq" from templates/faq/list.html
"""
        problems = check_translation(source, source, "de")
        self.assertEqual(
            {p.message for p in problems if p.code == "untranslated-frontmatter"},
            {f"'{key}' is identical to the English source"
             for key in ("title", "description", "extra.menu_title")},
        )

        translated = (source
                      .replace("title: Frequently Asked Questions", "title: Häufige Fragen")
                      .replace("description: Questions about Organic Maps", "description: Fragen zu Organic Maps")
                      .replace("menu_title: Help", "menu_title: Hilfe"))
        self.assertEqual(check_translation(source, translated, "de"), [])

        formal = translated.replace("description: Fragen", "description: Ihre Fragen")
        self.assertEqual(
            [p.code for p in check_translation(source, formal, "de")],
            ["register-frontmatter"],
        )

        declared = translated.replace(
            "  menu_title: Hilfe",
            '  menu_title: Help\n  translation_keeps_source: ["extra.menu_title"]',
        )
        self.assertEqual(check_translation(source, declared, "de"), [])

        stale = declared.replace("menu_title: Help", "menu_title: Hilfe")
        self.assertEqual(
            [(p.level, p.code) for p in check_translation(source, stale, "de")],
            [(ERROR, "translation-keeps-source")],
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
        for fence in ["```bash\necho hello\n```", "~~~bash\necho hello\n~~~",
                      "````\n```\nInternal\n```\n````"]:
            with self.subTest(fence=fence):
                payloads, _ = _segments(f"Before\n{fence}\nAfter")
                self.assertEqual(payloads, ["Before", "After"])
        self.assertEqual(_segments("Before\n~~~bash\nInternal")[0], ["Before"])

    def test_probe_builds_unknown_and_variant_targets(self):
        terms = load_terms()
        af, af_target = dictionary_for_probe(terms, "af")
        pt_br, pt_target = dictionary_for_probe(terms, "pt-BR")
        self.assertEqual((af_target, len(af)), ("af", 1))
        self.assertEqual((pt_target, len(pt_br)), ("pt", 1))


class FaqMetadataTests(unittest.TestCase):
    def test_faq_category_order_is_unique(self):
        seen = {}
        for path in sorted((ROOT / "content/faq").rglob("index*.md")):
            _, meta = strip_frontmatter(path.read_text(encoding="utf-8"))
            categories = meta.get("taxonomies", {}).get("faq", [])
            if not categories:
                continue
            order = meta.get("extra", {}).get("order")
            self.assertIsInstance(order, int, str(path.relative_to(ROOT)))
            for category in categories:
                key = (path.name, category, order)
                self.assertIsNone(seen.get(key),
                                  f"{path.relative_to(ROOT)} shares {category!r} order {order} "
                                  f"with {seen.get(key)}")
                seen[key] = path.relative_to(ROOT)


class TelegramToolingTests(unittest.TestCase):
    def test_current_tera_components_are_removed_from_posts(self):
        text = (
            "Before\n\n{{ <screenshot\n"
            "  src='/image.jpg'\n"
            "  alt='Map'\n"
            "/> }}\n\nAfter"
        )
        self.assertEqual(strip_tera_blocks(text), "Before\n\n\n\nAfter")

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
