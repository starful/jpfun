"""JPFun leisure item generator: queue, fill-half, activity caps, KO min."""
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


def test_item_generator_imports():
    gen = _load("item_generator")
    assert callable(gen.run_batch)
    path = gen._items_csv_path()
    assert path
    assert Path(path).name == "items.csv"


def test_item_fill_half_queues_only_missing_lang(tmp_path, monkeypatch):
    gen = _load("item_generator")
    out = tmp_path / "content"
    out.mkdir()
    (out / "hakuba_cortina_en.md").write_text("en", encoding="utf-8")
    csv_path = tmp_path / "items.csv"
    csv_path.write_text(
        "Name,Name_KO,Id,Activity,Lat,Lng,Address,Features,Website,Region\n"
        "Hakuba Cortina,하쿠바 코르티나,hakuba_cortina,ski,36.7,137.8,"
        "Hakuba,Powder,,nagano\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(gen, "CONTENT_DIR", str(out))
    monkeypatch.setattr(gen, "_items_csv_path", lambda: str(csv_path))
    monkeypatch.setenv("FILL_HALF", "1")
    queued: list[str] = []

    def fake_generate(row, lang):
        queued.append(lang)
        return f"✅ 성공: {lang}"

    monkeypatch.setattr(gen, "generate_item", fake_generate)
    gen.run_batch(limit=10)
    assert queued == ["ko"]


def test_item_fill_half_ignores_zero_activity_caps(tmp_path, monkeypatch):
    gen = _load("item_generator")
    out = tmp_path / "content"
    out.mkdir()
    (out / "hakuba_cortina_en.md").write_text("en", encoding="utf-8")
    csv_path = tmp_path / "items.csv"
    csv_path.write_text(
        "Name,Name_KO,Id,Activity,Lat,Lng,Address,Features,Website,Region\n"
        "Hakuba Cortina,하쿠바 코르티나,hakuba_cortina,ski,36.7,137.8,"
        "Hakuba,Powder,,nagano\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(gen, "CONTENT_DIR", str(out))
    monkeypatch.setattr(gen, "_items_csv_path", lambda: str(csv_path))
    monkeypatch.setenv("FILL_HALF", "1")
    monkeypatch.setenv("SKI_ITEM_LIMIT", "0")
    monkeypatch.setenv("SURF_ITEM_LIMIT", "0")
    monkeypatch.setenv("DIVE_ITEM_LIMIT", "0")
    monkeypatch.setenv("CAMP_ITEM_LIMIT", "0")
    queued: list[str] = []

    def fake_generate(row, lang):
        queued.append(lang)
        return f"✅ 성공: {lang}"

    monkeypatch.setattr(gen, "generate_item", fake_generate)
    gen.run_batch(limit=10)
    assert queued == ["ko"]


def test_item_activity_caps_skip_other_activities(tmp_path, monkeypatch):
    gen = _load("item_generator")
    out = tmp_path / "content"
    out.mkdir()
    csv_path = tmp_path / "items.csv"
    csv_path.write_text(
        "Name,Name_KO,Id,Activity,Lat,Lng,Address,Features,Website,Region\n"
        "Spot A,스팟A,spot_a,surf,35.0,139.0,Kanagawa,Beginner,,kanto\n"
        "Spot B,스팟B,spot_b,ski,36.7,137.8,Hakuba,Powder,,nagano\n"
        "Spot C,스팟C,spot_c,ski,42.8,140.7,Niseko,Powder,,hokkaido\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(gen, "CONTENT_DIR", str(out))
    monkeypatch.setattr(gen, "_items_csv_path", lambda: str(csv_path))
    monkeypatch.delenv("FILL_HALF", raising=False)
    monkeypatch.setenv("SKI_ITEM_LIMIT", "1")
    monkeypatch.setenv("SURF_ITEM_LIMIT", "0")
    monkeypatch.setenv("DIVE_ITEM_LIMIT", "0")
    monkeypatch.setenv("CAMP_ITEM_LIMIT", "0")
    queued: list[str] = []

    def fake_generate(row, lang):
        queued.append(f"{row['Id']}_{lang}")
        return f"✅ 성공: {row['Id']}_{lang}"

    monkeypatch.setattr(gen, "generate_item", fake_generate)
    gen.run_batch(limit=10)
    assert queued == ["spot_b_en", "spot_b_ko"]


def test_ko_item_min_chars_is_stub_floor():
    guards = _load("content_guards")
    assert guards.min_chars_for(kind="item", sibling_exists=False, lang="ko") == 2200
    assert guards.min_chars_for(kind="item", sibling_exists=True, lang="ko") == 2200
    assert guards.min_chars_for(kind="item", sibling_exists=False, lang="en") == 4500


def test_item_prompt_drops_korean_character_quota():
    gen = _load("item_generator")
    block = gen.quality_prompt_block(lang="ko")
    assert "character count" in block.lower() or "Character" in block
    assert "4,000" not in block


def test_saved_pending_ko_items_pass_theme_gate():
    guards = _load("content_guards")
    root = Path(__file__).resolve().parents[1] / "app" / "content"
    for name in (
        "surf_pending_03_ko.md",
        "dive_pending_03_ko.md",
        "camp_pending_02_ko.md",
    ):
        path = root / name
        if not path.is_file():
            continue
        raw = path.read_text(encoding="utf-8")
        ok, errors = guards.validate_generated_markdown(
            raw, kind="item", lang="ko", sibling_exists=True
        )
        assert ok, (name, errors)
