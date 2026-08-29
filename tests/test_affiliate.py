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


if __name__ == "__main__":
    unittest.main()
