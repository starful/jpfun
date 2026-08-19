"""Smoke tests: Hub pipeline can import jpfun guide_generator helpers."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "script"
if str(SCRIPT) not in sys.path:
    sys.path.insert(0, str(SCRIPT))


def _load(name: str):
    path = SCRIPT / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_topic_queue_and_guards_import():
    csv_mod = _load("topic_queue_csv")
    guards = _load("content_guards")
    assert callable(csv_mod.resolve)
    assert callable(guards.validate_generated_markdown)
    ok, errors = guards.validate_generated_markdown("no frontmatter", kind="guide", lang="en")
    assert ok is False
    assert "missing_frontmatter" in errors


def test_guide_generator_imports():
    gen = _load("guide_generator")
    assert callable(gen.run_batch)
    path = gen._guides_csv_path()
    assert path
    assert Path(path).name == "guides.csv"


def test_fill_half_queues_only_missing_lang(tmp_path, monkeypatch):
    gen = _load("guide_generator")
    out = tmp_path / "guides"
    out.mkdir()
    (out / "guide_ski_pass_comparison_en.md").write_text("en", encoding="utf-8")
    csv_path = tmp_path / "guides.csv"
    csv_path.write_text(
        "id,topic_en,topic_ko,keywords,activity\n"
        "guide_ski_pass_comparison,Ski pass,스키패스,ski pass,ski\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(gen, "OUTPUT_DIR", str(out))
    monkeypatch.setattr(gen, "_guides_csv_path", lambda: str(csv_path))
    monkeypatch.setenv("FILL_HALF", "1")
    queued: list[str] = []

    def fake_generate(row, lang):
        queued.append(lang)
        return f"✅ 성공: {lang}"

    monkeypatch.setattr(gen, "generate_guide", fake_generate)
    gen.run_batch(limit=10)
    assert queued == ["ko"]


def test_ensure_activity_frontmatter_inserts_after_lang():
    gen = _load("guide_generator")
    raw = """---
lang: en
title: "Hello"
summary: "s"
date: "2026-08-19"
---

Body
"""
    out = gen._ensure_activity_frontmatter(raw, "surf")
    assert "activity: surf\n" in out
    assert out.index("activity:") < out.index("title:")
    again = gen._ensure_activity_frontmatter(out, "ski")
    assert again.count("activity:") == 1
    assert "activity: surf" in again
