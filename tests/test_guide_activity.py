"""Guides without YAML activity still map onto /surf /ski /dive /camp."""
import unittest

from app import _normalize_guide_activity


class GuideActivityTest(unittest.TestCase):
    def test_explicit_yaml_wins(self):
        self.assertEqual(
            _normalize_guide_activity("surf", "guide_other", "", ""),
            "surf",
        )
        self.assertEqual(
            _normalize_guide_activity("scuba", "guide_x", "", ""),
            "dive",
        )
        self.assertEqual(
            _normalize_guide_activity("leisure", "guide_shonan_surf_basics", "", ""),
            "leisure",
        )

    def test_infer_from_id_when_yaml_missing(self):
        self.assertEqual(
            _normalize_guide_activity("", "guide_shonan_surf_basics", "Basics", ""),
            "surf",
        )
        self.assertEqual(
            _normalize_guide_activity("", "guide_ski_pass_comparison", "Passes", ""),
            "ski",
        )
        self.assertEqual(
            _normalize_guide_activity("", "guide_scuba_cert_japan", "OWD", ""),
            "dive",
        )
        self.assertEqual(
            _normalize_guide_activity("", "guide_fuji_camp_booking", "Fuji", ""),
            "camp",
        )
