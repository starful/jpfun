import unittest

from app.affiliate import affiliate_context, rakuten_url_for, resolve_ski_region


class AffiliateTest(unittest.TestCase):
    def test_resolve_regions(self):
        self.assertEqual(resolve_ski_region("niseko_grand_hirafu_en")[0], "niseko")
        self.assertEqual(resolve_ski_region("hakuba_happo_one_ko")[0], "hakuba")
        self.assertEqual(resolve_ski_region("gala_yuzawa_en")[0], "yuzawa")
        self.assertEqual(resolve_ski_region("unknown_resort_en")[0], "ski")

    def test_en_context_klook_and_rakuten(self):
        ctx = affiliate_context("furano_en", lang="en")
        self.assertTrue(ctx["show_klook"])
        self.assertTrue(ctx["show_rakuten"])
        self.assertFalse(ctx["show_coupang"])
        self.assertIn("klook.tpo.mx", ctx["klook_url"])
        self.assertIn("hb.afl.rakuten.co.jp/hgc/55b9427b", ctx["rakuten_search_url"])
        self.assertIn("Furano", ctx["rakuten_label"])

    def test_ko_context_coupang_only(self):
        ctx = affiliate_context("furano_ko", lang="ko")
        self.assertTrue(ctx["show_coupang"])
        self.assertFalse(ctx["show_klook"])
        self.assertFalse(ctx["show_rakuten"])
        self.assertIn("f7kmyhVtlt", ctx["coupang_travel_url"])
        self.assertIn("f7kqiPbQ04", ctx["coupang_shop_url"])
        self.assertIn("쿠팡 파트너스", ctx["coupang_disclosure"])

    def test_rakuten_url_encoded(self):
        url = rakuten_url_for("niseko_hanazono_en")
        self.assertIn("f_query%3D", url)
        self.assertIn("hgc/55b9427b", url)


if __name__ == "__main__":
    unittest.main()
