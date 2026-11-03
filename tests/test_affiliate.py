import unittest

from app.affiliate import affiliate_context, rakuten_url_for, resolve_ski_region
from urllib.parse import quote_plus

from app.a8_affiliate import a8_banners_context
from app.amazon_affiliate import amazon_context


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

    def test_ski_a8_agoda_only(self):
        ctx = a8_banners_context(activity="ski", lang="en", lat=36.7, lng=137.8)
        self.assertTrue(ctx["show_a8_banners"])
        ids = [b["id"] for b in ctx["a8_banners"]]
        self.assertEqual(ids, ["agoda"])
        self.assertTrue(ctx["show_agoda_cta"])
        self.assertNotIn("a8.net", ctx["agoda_cta"]["click_url"])

    def test_camp_a8_agoda_only(self):
        ctx = a8_banners_context(activity="camp", lang="en")
        ids = [b["id"] for b in ctx["a8_banners"]]
        self.assertEqual(ids, ["agoda"])
        for banner in ctx["a8_banners"]:
            self.assertNotIn("px.a8.net", banner["click_url"])
            self.assertEqual(banner["pixel_url"], "")

    def test_a8_agoda_only_for_all_activities(self):
        for act in ("", "surf", "ski", "camp", "glamping"):
            ctx = a8_banners_context(activity=act, lang="ko")
            self.assertEqual([b["id"] for b in ctx["a8_banners"]], ["agoda"])

    def test_amazon_default_and_kinds(self):
        cases = {
            "": "アウトドア グッズ",
            "surf": "アウトドア グッズ",
            "ski": "スキー ウェア",
            "camp": "キャンプ用品",
            "glamping": "グランピング グッズ",
        }
        for kind, kw in cases.items():
            ctx = amazon_context(kind=kind, lang="en")
            self.assertTrue(ctx["show_amazon"])
            url = ctx["amazon_cta"]["click_url"]
            self.assertIn("amazon.co.jp/s", url)
            self.assertIn("tag=starful06-22", url)
            self.assertIn(quote_plus(kw), url)

    def test_amazon_label_lang(self):
        ko = amazon_context(kind="camp", lang="ko")["amazon_cta"]["label"]
        en = amazon_context(kind="camp", lang="en")["amazon_cta"]["label"]
        self.assertIn("Amazon", ko)
        self.assertNotEqual(ko, en)


if __name__ == "__main__":
    unittest.main()
