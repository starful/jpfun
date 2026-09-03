import unittest

from app import app


class ApiSmokeTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_api_items_returns_list(self):
        response = self.client.get("/api/items?lang=en")
        self.assertEqual(response.status_code, 200)

        payload = response.get_json()
        self.assertIsInstance(payload, dict)

        list_key = next((k for k, v in payload.items() if isinstance(v, list)), None)
        self.assertIsNotNone(list_key)
        self.assertIn("last_updated", payload)

    def test_robots_and_sitemap_exist(self):
        robots = self.client.get("/robots.txt")
        self.assertEqual(robots.status_code, 200)
        self.assertIn("Sitemap:", robots.get_data(as_text=True))

        sitemap = self.client.get("/sitemap.xml")
        self.assertEqual(sitemap.status_code, 200)
        body = sitemap.get_data(as_text=True)
        self.assertIn("<urlset", body)
        self.assertIn("<loc>", body)
        self.assertIn("xhtml:link", body)

    def test_favicon_and_manifest_routes_exist(self):
        favicon = self.client.get("/favicon.ico")
        self.assertIn(favicon.status_code, (200, 302))

        manifest = self.client.get("/site.webmanifest")
        self.assertEqual(manifest.status_code, 200)
        self.assertIn("icons", manifest.get_data(as_text=True))

    def test_reactions_api_returns_counts(self):
        response = self.client.get("/api/reactions/smoke-test-slug")
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertIn("likes", payload)
        self.assertIn("dislikes", payload)

    def test_item_detail_has_reaction_panel(self):
        items_resp = self.client.get("/api/items?lang=en")
        payload = items_resp.get_json()
        items = payload.get("items") or []
        self.assertTrue(items)
        item_id = items[0]["id"]
        detail = self.client.get(f"/item/{item_id}")
        self.assertEqual(detail.status_code, 200)
        self.assertIn(b"reaction-panel", detail.data)

    def test_item_detail_shows_a8_and_rakuten(self):
        items_resp = self.client.get("/api/items?lang=en")
        payload = items_resp.get_json()
        items = payload.get("items") or []
        self.assertTrue(items)
        item_id = items[0]["id"]
        detail = self.client.get(f"/item/{item_id}")
        self.assertEqual(detail.status_code, 200)
        body = detail.get_data(as_text=True)
        self.assertIn("px.a8.net/svt/ejp", body)
        self.assertIn("a8-banners", body)
        self.assertNotIn("a8-banners__img", body)
        self.assertIn("booking-box", body)
        self.assertIn("hb.afl.rakuten.co.jp/hgc/", body)
        self.assertNotIn("link.coupang.com", body)
        self.assertNotIn("klook.tpo.mx", body)

    def test_item_detail_ko_shows_rakuten_and_a8(self):
        items_resp = self.client.get("/api/items?lang=ko")
        payload = items_resp.get_json()
        items = payload.get("items") or []
        self.assertTrue(items)
        item_id = items[0]["id"]
        detail = self.client.get(f"/item/{item_id}")
        self.assertEqual(detail.status_code, 200)
        body = detail.get_data(as_text=True)
        self.assertIn("hb.afl.rakuten.co.jp/hgc/", body)
        self.assertIn("px.a8.net/svt/ejp", body)
        self.assertNotIn("link.coupang.com", body)
        self.assertNotIn("klook.tpo.mx", body)
        self.assertNotIn("쿠팡 파트너스", body)

    def test_surf_page_lists_shonan_basics_guide(self):
        response = self.client.get("/surf")
        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn("Shonan Surfing Basics", body)
        self.assertIn("guide_shonan_surf_basics_en", body)

    def test_ski_page_lists_pass_comparison_guide(self):
        response = self.client.get("/ski")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Japan Ski Pass Types Explained", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
