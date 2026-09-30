from app.activities import TRAITS_BY_ACTIVITY, traits_for
from app.traits import detect_traits, matches_trait_filter, normalize_trait


class TestTraits:
    def test_traits_for_ski_has_powder(self):
        keys = [t["key"] for t in traits_for("ski", "en")]
        assert keys == ["all", "beginner", "family", "powder", "onsen", "daytrip"]

    def test_traits_for_surf_ko_labels(self):
        labels = [t["label"] for t in traits_for("surf", "ko")]
        assert "초보" in labels
        assert "리프·포인트" in labels

    def test_traits_for_dive_and_camp(self):
        assert [t["key"] for t in TRAITS_BY_ACTIVITY["dive"]] == [
            "all", "beginner", "reef", "wall", "video",
        ]
        assert [t["key"] for t in TRAITS_BY_ACTIVITY["camp"]] == [
            "all", "glamping", "carcamp", "beginner", "onsen",
        ]

    def test_detect_beginner_and_video(self):
        item = {
            "title": "초보자도 안전한 얕은 산호 정원",
            "summary": "Beginner reef dive near Naha.",
            "youtube_id": "abc123",
        }
        traits = detect_traits(item)
        assert "beginner" in traits
        assert "reef" in traits
        assert "video" in traits

    def test_matches_and_normalize(self):
        item = {"title": "Glamping park under Fuji", "summary": "글램핑 베이스", "youtube_id": ""}
        assert matches_trait_filter(item, "glamping")
        assert not matches_trait_filter(item, "carcamp")
        assert matches_trait_filter(item, "all")
        assert normalize_trait("camp", "glamping") == "glamping"
        assert normalize_trait("camp", "powder") == "all"
