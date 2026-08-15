import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

SITE_CONFIG = {
    "project_name":  "jpfun",
    "site_name":     "JPFun",
    "site_url":      os.getenv("SITE_URL", "https://jpfun.net"),
    "tagline":       "Japan leisure map — ski, scuba, surf & camp",
    "data_key":      "items",

    "ga_id":         os.getenv("GA_ID", "G-XXXXXXXXXX"),
    "maps_api_key":  (
        os.getenv("MAPS_API_KEY")
        or os.getenv("JPFUN_GOOGLE_MAPS_API_KEY")
        or ""
    ),
    "maps_id":       os.getenv("MAPS_ID", ""),

    "emoji":         "🎉",
    "accent_color":  "#21C3CA",
    "bg_dot_color":  "#a8e4e8",

    # Primary filters live on /ski|/surf|/dive|/camp (per-activity regions)
    "filter_buttons": [],

    "category_mapping": {
        "Ski":  "Ski Resort",
        "Surf": "Surf Spot",
        "Dive": "Dive Site",
        "Camp": "Campground",
        "Stay": "Stay",
        "Food": "Food",
    },

    "js_category_map": {
        "ski":  "Ski Resort",
        "surf": "Surf Spot",
        "dive": "Dive Site",
        "camp": "Campground",
        "stay": "Stay",
        "food": "Food",
    },

    "schema_type": "SportsActivityLocation",

    "guide_images": [
        "https://images.unsplash.com/photo-1551524559-8af4e6624178?q=80&w=800&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1502680390469-be75c86b3504?q=80&w=800&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1544551763-46a013bb70d5?q=80&w=800&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?q=80&w=800&auto=format&fit=crop",
    ],

    "klook_url": "https://klook.tpo.mx/ED7IfKaq",
    "coupang_travel_url": "https://link.coupang.com/a/f7kmyhVtlt",
    "coupang_shop_url": "https://link.coupang.com/a/f7kqiPbQ04",
    "rakuten_travel_hgc": "55b9427b.a63c2df8.55b9427c.3a0d270c",

    "footer_tagline":  "Japan leisure trip planning — ski, scuba, surf & camp on one map.",
    "footer_year":     "2026",

    "instagram_url":   "",
    "instagram_handle": "",
}
