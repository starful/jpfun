import unittest

from app.affiliate import affiliate_context, rakuten_url_for, resolve_ski_region
from app.a8_affiliate import a8_banners_context


class TestJpfunAffiliate(unittest.TestCase):
    def test_resolve_ski_region_furano(self):
        key, keyword, label = resolve_ski_region("furano_en")
        self.assertEqual(key, "furano")
        self.assertIn("富良野", keyword)
        self.assertEqual(label, "Furano")

    def test_en_context_rakuten_only(self):
        ctx = affiliate_context("furano_en", lang="en")
        self.assertTrue(ctx["show_rakuten"])
        self.assertIn("hb.afl.rakuten.co.jp/hgc/", ctx["rakuten_search_url"])
        self.assertIn("Furano", ctx["rakuten_label"])

    def test_ko_context_rakuten_only(self):
        ctx = affiliate_context("furano_ko", lang="ko")
        self.assertTrue(ctx["show_rakuten"])
        self.assertIn("hb.afl.rakuten.co.jp/hgc/", ctx["rakuten_search_url"])

    def test_rakuten_url_encoded(self):
        url = rakuten_url_for("niseko_hanazono_en")
        self.assertIn("hb.afl.rakuten.co.jp/hgc/", url)

    def test_ishigaki_is_not_shiga(self):
        key, keyword, label = resolve_ski_region("okinawa_ishigaki_surf_en")
        self.assertEqual(key, "ishigaki")
        self.assertIn("石垣", keyword)
        self.assertNotIn("志賀", keyword)
        self.assertEqual(label, "Ishigaki")

    def test_surf_without_place_uses_region_not_ski(self):
        from app.affiliate import resolve_travel_region

        key, keyword, label = resolve_travel_region(
            "surf_pending_03_en", activity="surf", region="kanto"
        )
        self.assertEqual(key, "kanto")
        self.assertIn("関東", keyword)
        self.assertNotIn("スキー", keyword)
        self.assertEqual(label, "Kanto")

    def test_ski_pending_maps_resort(self):
        from app.affiliate import resolve_travel_region

        key, keyword, label = resolve_travel_region(
            "ski_pending_01_en", activity="ski", region="nagano"
        )
        self.assertEqual(key, "hakuba")
        self.assertIn("白馬", keyword)
        self.assertEqual(label, "Hakuba")

    def test_ski_a8_includes_ski_tour(self):
        ctx = a8_banners_context(activity="ski", lang="en")
        self.assertTrue(ctx["show_a8_banners"])
        ids = [b["id"] for b in ctx["a8_banners"]]
        self.assertEqual(ids[0], "ski_tour")
        self.assertIn("agoda", ids)
        self.assertIn("tora_esim", ids)

    def test_camp_a8_includes_glamping(self):
        ctx = a8_banners_context(activity="camp", lang="en")
        ids = [b["id"] for b in ctx["a8_banners"]]
        self.assertIn("glamping", ids)
        self.assertIn("hinata_rental", ids)
        hinata = next(b for b in ctx["a8_banners"] if b["id"] == "hinata_rental")
        self.assertIn("4BCE3P+1C87V6+4U5Q+5YJRM", hinata["click_url"])
        self.assertIn("hinata", hinata["label"].lower())


if __name__ == "__main__":
    unittest.main()
