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
