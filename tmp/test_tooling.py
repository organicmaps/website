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
sys.path.insert(0, str(ROOT))

from deepl_glossary import dictionary_for_probe, load_terms  # noqa: E402
from telegram_post import (  # noqa: E402
    classify_media,
    convert_markdown_to_telegramv2,
    send_media,
    split_text,
    utf16_len,
    validate_media_set,
    visible_text,
)
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
            [sys.executable, "-c", code], cwd=ROOT, capture_output=True, text=True
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
                [sys.executable, str(ROOT / "translate_check.py"),
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
