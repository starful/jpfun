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


def test_ko_min_chars_is_stub_floor_not_english_quota():
    guards = _load("content_guards")
    assert guards.KO_MIN_CHARS == 2200
    assert guards.min_chars_for(kind="guide", sibling_exists=False, lang="ko") == 2200
    assert guards.min_chars_for(kind="guide", sibling_exists=True, lang="ko") == 2200
    assert guards.min_chars_for(kind="item", sibling_exists=False, lang="ko") == 2200
    assert guards.min_chars_for(kind="guide", sibling_exists=False, lang="en") == guards.GUIDE_MIN_CHARS
    assert guards.min_chars_for(kind="item", sibling_exists=False, lang="en") == guards.ITEM_MIN_CHARS
    assert guards.min_chars_for(kind="guide", sibling_exists=True, lang="en") == guards.SIBLING_FILL_MIN_CHARS


def _ko_item_md(*, include_access: bool = True) -> str:
    pad = "하쿠바 코르티나는 나가노 북부의 파우더 산으로, 트리런을 찾는 스키어가 모인다. " * 25
    access = "신치토세가 아니라 나가노에서 렌터카로 접근하는 경우가 많다." if include_access else "마을 분위기가 조용하다."
    return f"""---
lang: ko
title: "하쿠바 코르티나"
lat: 36.7
lng: 137.8
categories: ["Ski"]
thumbnail: "/static/images/x.jpg"
address: "Hakuba"
date: "2026-09-14"
summary: "파우더와 트리런"
---

## 누가 찾는지

{pad}

## 겨울 시즌의 눈

12월부터 적설이 쌓인다. {pad}

## 장비와 예약 팁

렌탈 장비는 베이스에서 빌리고 주중 예약을 권한다. {access}
"""


def test_ko_item_passes_when_themes_present_even_under_old_3500():
    guards = _load("content_guards")
    raw = _ko_item_md(include_access=True)
    ok, errors = guards.validate_generated_markdown(
        raw, kind="item", lang="ko", sibling_exists=False
    )
    assert ok, errors
    _, body = guards.parse_frontmatter_body(raw)
    assert 2200 <= len(body) < 3500


def test_ko_item_fails_without_access_theme():
    guards = _load("content_guards")
    raw = _ko_item_md(include_access=False)
    ok, errors = guards.validate_generated_markdown(
        raw, kind="item", lang="ko", sibling_exists=False
    )
    assert ok is False
    assert "missing_theme:access" in errors


def test_filled_ko_halves_pass_quality_gate():
    guards = _load("content_guards")
    root = Path(__file__).resolve().parents[1] / "app" / "content" / "guides"
    for name in (
        "guide_beginner_ski_japan_ko.md",
        "guide_karuizawa_camp_weekend_ko.md",
    ):
        raw = (root / name).read_text(encoding="utf-8")
        ok, errors = guards.validate_generated_markdown(
            raw, kind="guide", lang="ko", sibling_exists=True
        )
        assert ok, (name, errors)


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
