"""
JPFun MVP catalog — ski / surf / dive / camp seeds (EN/KO).
"""
from __future__ import annotations

from datetime import date
from typing import Any

LANGS = ("en", "ko")
TODAY = date.today().isoformat()

ACTIVITY_META = {
    "ski":  {"category": "Ski",  "emoji": "⛷️", "label_en": "Ski resort", "label_ko": "스키장"},
    "surf": {"category": "Surf", "emoji": "🏄", "label_en": "Surf spot",  "label_ko": "서핑 스팟"},
    "dive": {"category": "Dive", "emoji": "🤿", "label_en": "Dive site",  "label_ko": "다이빙 포인트"},
    "camp": {"category": "Camp", "emoji": "🏕️", "label_en": "Campground","label_ko": "캠핑장"},
}

# Outdoor seeds — ski stubs kept for CSV; full ski catalog is ski_catalog + seed_resorts.
# Surf / dive / camp: 12 places each for activity maps.
OUTDOOR_SEEDS: list[dict[str, Any]] = [
    # --- Ski ---
    {
        "id": "niseko_grand_hirafu",
        "activity": "ski",
        "region": "hokkaido",
        "names": {"en": "Niseko Grand Hirafu", "ko": "니세코 그란히라후"},
        "lat": 42.857,
        "lng": 140.706,
        "addresses": {
            "en": "Hirafu, Kutchan, Hokkaido, Japan",
            "ko": "일본 홋카이도 굿찬정 히라후",
        },
        "features": "Powder, Resort, Beginner",
        "website": "https://www.grand-hirafu.jp/",
        "blurb_en": "Niseko’s main powder base — village nightlife, English-friendly services, and linked United skiing.",
        "blurb_ko": "니세코의 대표 파우더 베이스. 히라후 마을 분위기와 United 연동 스키.",
    },
    {
        "id": "hakuba_happo_one",
        "activity": "ski",
        "region": "nagano",
        "names": {"en": "Hakuba Happo-one", "ko": "하쿠바 햇포원"},
        "lat": 36.702,
        "lng": 137.862,
        "addresses": {
            "en": "Happo, Hakuba, Nagano, Japan",
            "ko": "일본 나가노현 하쿠바촌 햇포",
        },
        "features": "Olympic, Vertical, Village",
        "website": "https://www.happo-one.jp/",
        "blurb_en": "Olympic-scale vertical in Hakuba Valley with strong Tokyo access and après options.",
        "blurb_ko": "하쿠바 밸리의 올림픽급 버티컬. 도쿄 접근성과 애프터스키가 강점.",
    },
    {
        "id": "gala_yuzawa",
        "activity": "ski",
        "region": "niigata",
        "names": {"en": "GALA Yuzawa Snow Resort", "ko": "가라 유자와"},
        "lat": 36.948,
        "lng": 138.803,
        "addresses": {
            "en": "Yuzawa, Niigata, Japan",
            "ko": "일본 니가타현 유자와마치",
        },
        "features": "Shinkansen, Day trip, Beginner",
        "website": "https://gala.co.jp/",
        "blurb_en": "Ski-in from the Shinkansen — classic Tokyo day-trip powder with onsen town below.",
        "blurb_ko": "신칸센 직결 스키장. 도쿄 당일 스키와 유자와 온천이 한 세트.",
    },
    {
        "id": "nozawa_onsen",
        "activity": "ski",
        "region": "nagano",
        "names": {"en": "Nozawa Onsen Ski Resort", "ko": "노자와온천 스키장"},
        "lat": 36.922,
        "lng": 138.441,
        "addresses": {
            "en": "Nozawaonsen, Nagano, Japan",
            "ko": "일본 나가노현 노자와온천촌",
        },
        "features": "Village, Onsen, Powder",
        "website": "https://www.nozawaski.com/",
        "blurb_en": "Historic onsen village skiing — slopes above public baths and traditional lodging.",
        "blurb_ko": "온천 마을 위 슬로프. 료칸·공동욕장과 파우더가 한곳에.",
    },
    # --- Surf (12) ---
    {
        "id": "shonan_kugenuma",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Shonan Kugenuma Beach", "ko": "쇼난 구게누마 비치"},
        "lat": 35.320,
        "lng": 139.486,
        "addresses": {
            "en": "Kugenuma, Fujisawa, Kanagawa, Japan",
            "ko": "일본 가나가와현 후지사와시 구게누마",
        },
        "features": "Beginner, Train access, Schools",
        "website": "",
        "blurb_en": "Classic Shonan beach break near Tokyo — schools, rentals, and easy Odakyu access.",
        "blurb_ko": "도쿄 근교 쇼난 대표 비치. 스쿨·렌탈과 전철 접근이 편함.",
    },
    {
        "id": "chiba_hebara",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Hebara Beach (Isumi)", "ko": "헤바라 비치 (이스미)"},
        "lat": 35.254,
        "lng": 140.404,
        "addresses": {
            "en": "Hebara, Isumi, Chiba, Japan",
            "ko": "일본 치바현 이스미시 헤바라",
        },
        "features": "Consistent, Intermediate, Pacific",
        "website": "",
        "blurb_en": "Pacific-facing Chiba break popular with Tokyo weekenders — consistent swell windows.",
        "blurb_ko": "도쿄 주말러가 많이 찾는 치바 태평양 스팟. 스웰이 비교적 꾸준함.",
    },
    {
        "id": "okinawa_sunayama",
        "activity": "surf",
        "region": "okinawa",
        "names": {"en": "Sunayama Beach area (Miyako)", "ko": "스나야마 비치 (미야코)"},
        "lat": 24.805,
        "lng": 125.281,
        "addresses": {
            "en": "Hirara, Miyakojima, Okinawa, Japan",
            "ko": "일본 오키나와현 미야코지마 히라라",
        },
        "features": "Island, Scenic, Winter swell",
        "website": "",
        "blurb_en": "Miyako island surfing near iconic sand-hill beach — winter north swell season.",
        "blurb_ko": "미야코 모래언덕 비치 인근 서핑. 겨울 북쪽 스웰 시즌이 핵심.",
    },
    {
        "id": "ibaraki_oaraibaraki",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Oarai Surf Area", "ko": "오아라이 서프 에리어"},
        "lat": 36.313,
        "lng": 140.592,
        "addresses": {
            "en": "Oarai, Ibaraki, Japan",
            "ko": "일본 이바라키현 오아라이정",
        },
        "features": "Point / Beach, Intermediate",
        "website": "",
        "blurb_en": "Ibaraki coast surf with harbor and beach options — popular north of Tokyo.",
        "blurb_ko": "도쿄 북쪽 이바라키 해안 서핑. 하버·비치 옵션이 다양.",
    },
    {
        "id": "shonan_chigasaki",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Chigasaki Southern Beach", "ko": "지가사키 서던 비치"},
        "lat": 35.314,
        "lng": 139.405,
        "addresses": {
            "en": "Chigasaki, Kanagawa, Japan",
            "ko": "일본 가나가와현 지가사키시",
        },
        "features": "Beach break, Beginner+, Culture",
        "website": "",
        "blurb_en": "Shonan’s cultural surf town — Southern Beach vibe, lessons, and JR access from Tokyo.",
        "blurb_ko": "쇼난 서프 문화의 중심 지가사키. 레슨과 JR 접근이 편함.",
    },
    {
        "id": "shonan_tsujido",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Tsujido Beach", "ko": "츠지도 비치"},
        "lat": 35.317,
        "lng": 139.447,
        "addresses": {
            "en": "Tsujido, Fujisawa, Kanagawa, Japan",
            "ko": "일본 가나가와현 후지사와시 츠지도",
        },
        "features": "Beach, Crowds, Rentals",
        "website": "",
        "blurb_en": "Busy Shonan beach break between Kugenuma and Chigasaki — rentals and summer crowds.",
        "blurb_ko": "구게누마·지가사키 사이 쇼난 비치. 렌탈과 여름 인파가 많음.",
    },
    {
        "id": "chiba_kujukuri",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Kujukuri Beach Surf Zone", "ko": "구주쿠리 비치 서프존"},
        "lat": 35.533,
        "lng": 140.450,
        "addresses": {
            "en": "Kujukuri, Chiba, Japan",
            "ko": "일본 치바현 구주쿠리정",
        },
        "features": "Long beach, Beach break, Wind",
        "website": "",
        "blurb_en": "Long Pacific sand beach east of Tokyo — multiple peaks along the Kujukuri coast.",
        "blurb_ko": "도쿄 동쪽 긴 모래사장. 구주쿠리 해안을 따라 피크가 이어짐.",
    },
    {
        "id": "fukushima_nakoso",
        "activity": "surf",
        "region": "tohoku",
        "names": {"en": "Nakoso / Iwaki Surf Coast", "ko": "나코소·이와키 서프 코스트"},
        "lat": 36.850,
        "lng": 140.790,
        "addresses": {
            "en": "Iwaki, Fukushima, Japan",
            "ko": "일본 후쿠시마현 이와키시",
        },
        "features": "Pacific, Intermediate, Local",
        "website": "",
        "blurb_en": "Fukushima Pacific coast surfing around Iwaki / Nakoso — less crowded than Shonan.",
        "blurb_ko": "이와키·나코소 일대 후쿠시마 태평양 서핑. 쇼난보다 한산한 편.",
    },
    {
        "id": "shizuoka_iso",
        "activity": "surf",
        "region": "chubu",
        "names": {"en": "Shizuoka Iso / Suruga Coast", "ko": "시즈오카 이소·스루가 코스트"},
        "lat": 34.975,
        "lng": 138.450,
        "addresses": {
            "en": "Shizuoka City coast, Shizuoka, Japan",
            "ko": "일본 시즈오카현 시즈오카시 해안",
        },
        "features": "Beach / Reef, Typhoon swell",
        "website": "",
        "blurb_en": "Suruga Bay coast surfing with Shizuoka access — typhoon swell and local reef options.",
        "blurb_ko": "스루가만 해안 서핑. 태풍 스웰과 로컬 리프 옵션.",
    },
    {
        "id": "kochi_irisaki",
        "activity": "surf",
        "region": "shikoku",
        "names": {"en": "Kochi Irisaki / Pacific Shikoku", "ko": "고치 이리사키·시코쿠 태평양"},
        "lat": 33.470,
        "lng": 133.570,
        "addresses": {
            "en": "Kochi, Kochi Prefecture, Japan",
            "ko": "일본 고치현 고치시",
        },
        "features": "Powerful swell, Intermediate+, Scenic",
        "website": "",
        "blurb_en": "Shikoku Pacific surfing with strong swell windows — Irisaki and nearby Kochi coast peaks.",
        "blurb_ko": "시코쿠 태평양 서핑. 이리사키 등 고치 해안의 힘있는 스웰.",
    },
    {
        "id": "okinawa_yomitan",
        "activity": "surf",
        "region": "okinawa",
        "names": {"en": "Yomitan / Zakimi Coast", "ko": "요미탄·자키미 코스트"},
        "lat": 26.400,
        "lng": 127.740,
        "addresses": {
            "en": "Yomitan, Okinawa, Japan",
            "ko": "일본 오키나와현 요미탄촌",
        },
        "features": "Reef, Winter north swell, Main island",
        "website": "",
        "blurb_en": "Okinawa main-island west coast surf — winter north swell and reef setups near Yomitan.",
        "blurb_ko": "오키나와 본섬 서쪽 서핑. 요미탄 일대 겨울 북쪽 스웰·리프.",
    },
    {
        "id": "okinawa_ishigaki_surf",
        "activity": "surf",
        "region": "okinawa",
        "names": {"en": "Ishigaki Surf Coast", "ko": "이시가키 서프 코스트"},
        "lat": 24.340,
        "lng": 124.160,
        "addresses": {
            "en": "Ishigaki, Okinawa, Japan",
            "ko": "일본 오키나와현 이시가키시",
        },
        "features": "Island, Reef / Beach, Remote vibe",
        "website": "",
        "blurb_en": "Yaeyama island surfing on Ishigaki — combine with dive days when swell and wind align.",
        "blurb_ko": "야에야마 이시가키 서핑. 스웰·바람이 맞으면 다이빙과 조합하기 좋음.",
    },
    # --- Dive (12) ---
    {
        "id": "okinawa_kerama",
        "activity": "dive",
        "region": "okinawa",
        "names": {"en": "Kerama Islands Dive Area", "ko": "케라마 제도 다이빙"},
        "lat": 26.200,
        "lng": 127.350,
        "addresses": {
            "en": "Kerama Islands, Okinawa, Japan",
            "ko": "일본 오키나와현 케라마 제도",
        },
        "features": "Clear water, Day boat, All levels",
        "website": "",
        "blurb_en": "World-class visibility day-boat diving from Naha / Zamami — turtles and soft coral gardens.",
        "blurb_ko": "나하·자마미 출발 데이보트 다이빙. 투명도와 바다거북으로 유명.",
    },
    {
        "id": "izu_oshima",
        "activity": "dive",
        "region": "chubu",
        "names": {"en": "Izu Oshima Dive Spots", "ko": "이즈 오시마 다이빙"},
        "lat": 34.737,
        "lng": 139.400,
        "addresses": {
            "en": "Oshima, Tokyo, Japan",
            "ko": "일본 도쿄도 오시마정",
        },
        "features": "Volcanic rock, Weekend, Schools",
        "website": "",
        "blurb_en": "Tokyo island diving with volcanic rock reefs — ferry access and local dive shops.",
        "blurb_ko": "화산암 리프의 도쿄 도서 다이빙. 페리와 로컬 샵 접근.",
    },
    {
        "id": "okinawa_ishigaki_manta",
        "activity": "dive",
        "region": "okinawa",
        "names": {"en": "Ishigaki Manta Scramble Area", "ko": "이시가키 만타 스크램블"},
        "lat": 24.336,
        "lng": 124.156,
        "addresses": {
            "en": "Ishigaki, Okinawa, Japan",
            "ko": "일본 오키나와현 이시가키시",
        },
        "features": "Manta, Boat, Intermediate+",
        "website": "",
        "blurb_en": "Famous manta cleaning-station dives off Ishigaki — book boats early in peak season.",
        "blurb_ko": "이시가키 만타 클리닝 스테이션. 성수기에는 보트 예약을 서두르세요.",
    },
    {
        "id": "okinawa_blue_cave",
        "activity": "dive",
        "region": "okinawa",
        "names": {"en": "Onna Blue Cave Dive Area", "ko": "온나 블루케이브 다이빙"},
        "lat": 26.497,
        "lng": 127.853,
        "addresses": {
            "en": "Onna, Okinawa, Japan",
            "ko": "일본 오키나와현 온나촌",
        },
        "features": "Cave light, Snorkel+scuba, Beginner+",
        "website": "",
        "blurb_en": "Onna’s famous blue-cave entries — short boat or shore options with strong tourist demand.",
        "blurb_ko": "온나촌 블루케이브. 숏보트·쇼어 옵션과 관광 수요가 많음.",
    },
    {
        "id": "okinawa_miyako_dive",
        "activity": "dive",
        "region": "okinawa",
        "names": {"en": "Miyako Island Dive Sites", "ko": "미야코지마 다이빙"},
        "lat": 24.805,
        "lng": 125.281,
        "addresses": {
            "en": "Miyakojima, Okinawa, Japan",
            "ko": "일본 오키나와현 미야코지마",
        },
        "features": "Drop-offs, Caves, Clear water",
        "website": "",
        "blurb_en": "Miyako drop-offs and underwater caves — clear water and photogenic walls.",
        "blurb_ko": "미야코 드롭오프·수중 케이브. 투명도와 포토 월이 강점.",
    },
    {
        "id": "okinawa_yonaguni",
        "activity": "dive",
        "region": "okinawa",
        "names": {"en": "Yonaguni Dive Area", "ko": "요나구니 다이빙"},
        "lat": 24.468,
        "lng": 123.004,
        "addresses": {
            "en": "Yonaguni, Okinawa, Japan",
            "ko": "일본 오키나와현 요나구니정",
        },
        "features": "Hammerheads, Advanced, Remote",
        "website": "",
        "blurb_en": "Remote Yaeyama diving — winter hammerhead season and legendary underwater formations.",
        "blurb_ko": "야에야마 최서단 다이빙. 겨울 귀상어 시즌과 수중 지형으로 유명.",
    },
    {
        "id": "izu_ito",
        "activity": "dive",
        "region": "chubu",
        "names": {"en": "Ito / Izu East Coast Dive", "ko": "이토·이즈 동해안 다이빙"},
        "lat": 34.965,
        "lng": 139.102,
        "addresses": {
            "en": "Ito, Shizuoka, Japan",
            "ko": "일본 시즈오카현 이토시",
        },
        "features": "Shore / Boat, Schools, Weekend",
        "website": "",
        "blurb_en": "Izu east-coast diving from Ito — shops, shore entries, and Tokyo weekend access.",
        "blurb_ko": "이토 출발 이즈 동해안 다이빙. 샵·쇼어와 도쿄 주말 접근.",
    },
    {
        "id": "izu_shimoda",
        "activity": "dive",
        "region": "chubu",
        "names": {"en": "Shimoda Dive Area", "ko": "시모다 다이빙"},
        "lat": 34.679,
        "lng": 138.945,
        "addresses": {
            "en": "Shimoda, Shizuoka, Japan",
            "ko": "일본 시즈오카현 시모다시",
        },
        "features": "Reef, Current, Intermediate",
        "website": "",
        "blurb_en": "Southern Izu diving around Shimoda — reefs, currents, and strong local shop scene.",
        "blurb_ko": "시모다 일대 남이즈 다이빙. 리프·조류와 로컬 샵이 탄탄함.",
    },
    {
        "id": "shizuoka_ohsezaki",
        "activity": "dive",
        "region": "chubu",
        "names": {"en": "Ohsezaki Dive Point", "ko": "오세자키 다이빙"},
        "lat": 35.041,
        "lng": 138.788,
        "addresses": {
            "en": "Numazu / Ohsezaki, Shizuoka, Japan",
            "ko": "일본 시즈오카현 누마즈·오세자키",
        },
        "features": "Muck / macro, Shore, Night dive",
        "website": "",
        "blurb_en": "Famous Izu muck and macro site — shore diving with rich critter life and night dives.",
        "blurb_ko": "이즈 대표 머크·매크로 포인트. 쇼어와 나이트 다이빙이 유명.",
    },
    {
        "id": "kagoshima_yakushima",
        "activity": "dive",
        "region": "kyushu",
        "names": {"en": "Yakushima Dive Coast", "ko": "야쿠시마 다이빙 코스트"},
        "lat": 30.335,
        "lng": 130.512,
        "addresses": {
            "en": "Yakushima, Kagoshima, Japan",
            "ko": "일본 가고시마현 야쿠시마",
        },
        "features": "Island, Nature, Intermediate+",
        "website": "",
        "blurb_en": "Kyushu island diving under Yakushima’s world-heritage forests — combine land and sea days.",
        "blurb_ko": "세계유산 숲 아래 야쿠시마 다이빙. 육상·해상 일정을 함께 짜기 좋음.",
    },
    {
        "id": "kagoshima_amami",
        "activity": "dive",
        "region": "kyushu",
        "names": {"en": "Amami Oshima Dive Area", "ko": "아마미오시마 다이빙"},
        "lat": 28.380,
        "lng": 129.500,
        "addresses": {
            "en": "Amami, Kagoshima, Japan",
            "ko": "일본 가고시마현 아마미시",
        },
        "features": "Coral, Whale sharks (season), Remote",
        "website": "",
        "blurb_en": "Amami coral diving between Kyushu and Okinawa — quieter reefs and seasonal megafauna.",
        "blurb_ko": "규슈·오키나와 사이 아마미 산호 다이빙. 한산한 리프와 시즌 메가파우나.",
    },
    {
        "id": "okinawa_minna",
        "activity": "dive",
        "region": "okinawa",
        "names": {"en": "Minna Island / Motobu Dive", "ko": "민나섬·모토부 다이빙"},
        "lat": 26.650,
        "lng": 127.820,
        "addresses": {
            "en": "Motobu / Minna, Okinawa, Japan",
            "ko": "일본 오키나와현 모토부·민나섬",
        },
        "features": "Day trip, Clear water, Beginner+",
        "website": "",
        "blurb_en": "Northern Okinawa day-trip diving from Motobu toward Minna — clear water and easy logistics.",
        "blurb_ko": "모토부에서 민나섬 방면 데이트립 다이빙. 투명도와 동선이 편함.",
    },
    # --- Camp (12) ---
    {
        "id": "fuji_motosu_camp",
        "activity": "camp",
        "region": "chubu",
        "names": {"en": "Lake Motosu Camp Area", "ko": "모토스코 캠프 에리어"},
        "lat": 35.462,
        "lng": 138.687,
        "addresses": {
            "en": "Lake Motosu, Fujikawaguchiko, Yamanashi, Japan",
            "ko": "일본 야마나시현 후지카와구치코 모토스코",
        },
        "features": "Fuji view, Car camp, Lakeside",
        "website": "",
        "blurb_en": "Fuji lakeside camping classic — car-camp sites and iconic Motosu reflections.",
        "blurb_ko": "후지산 호수 캠핑 클래식. 모토스코 역광 뷰와 차박 사이트.",
    },
    {
        "id": "hakuba_camp",
        "activity": "camp",
        "region": "nagano",
        "names": {"en": "Hakuba Alpine Camp Bases", "ko": "하쿠바 알파인 캠프"},
        "lat": 36.698,
        "lng": 137.862,
        "addresses": {
            "en": "Hakuba, Nagano, Japan",
            "ko": "일본 나가노현 하쿠바촌",
        },
        "features": "Mountain, Summer, Glamping",
        "website": "",
        "blurb_en": "Summer alpine camping and glamping near Hakuba trails — winter ski town flips to outdoor base.",
        "blurb_ko": "하쿠바 트레일 근처 여름 알파인 캠프·글램핑. 겨울 스키 타운이 야외 베이스로.",
    },
    {
        "id": "shimanami_camp",
        "activity": "camp",
        "region": "chugoku",
        "names": {"en": "Shimanami Kaido Camp Stops", "ko": "시마나미 해도 캠프 스톱"},
        "lat": 34.270,
        "lng": 133.050,
        "addresses": {
            "en": "Onomichi–Imabari route, Japan",
            "ko": "일본 오노미치–이마바리 시마나미 루트",
        },
        "features": "Cycle camp, Island hops, Sea view",
        "website": "",
        "blurb_en": "Island-hop camping along Japan’s famous cycle route — sea views and bike-friendly sites.",
        "blurb_ko": "시마나미 사이클 루트의 섬 캠핑. 바다 뷰와 자전거 친화 사이트.",
    },
    {
        "id": "fuji_yamanakako_camp",
        "activity": "camp",
        "region": "chubu",
        "names": {"en": "Lake Yamanaka Camp Area", "ko": "야마나카코 캠프 에리어"},
        "lat": 35.418,
        "lng": 138.876,
        "addresses": {
            "en": "Yamanakako, Yamanashi, Japan",
            "ko": "일본 야마나시현 야마나카코촌",
        },
        "features": "Fuji view, Family, Lakeside",
        "website": "",
        "blurb_en": "Largest Fuji Five Lakes camping hub — family sites and wide Motosu-side alternatives.",
        "blurb_ko": "후지 오호 중 가장 큰 캠프 허브. 패밀리 사이트와 넓은 호숫가.",
    },
    {
        "id": "fuji_kawaguchiko_camp",
        "activity": "camp",
        "region": "chubu",
        "names": {"en": "Lake Kawaguchi Camp Area", "ko": "가와구치코 캠프 에리어"},
        "lat": 35.508,
        "lng": 138.755,
        "addresses": {
            "en": "Fujikawaguchiko, Yamanashi, Japan",
            "ko": "일본 야마나시현 후지카와구치코마치",
        },
        "features": "Transit, Fuji view, Glamping",
        "website": "",
        "blurb_en": "Kawaguchiko camping with bus/train access and Fuji views — glamping and car-camp mix.",
        "blurb_ko": "버스·전철 접근이 쉬운 가와구치코 캠핑. 글램핑·차박 믹스.",
    },
    {
        "id": "nagano_tateshina_camp",
        "activity": "camp",
        "region": "nagano",
        "names": {"en": "Tateshina Highland Camp", "ko": "다테시나 고원 캠프"},
        "lat": 36.100,
        "lng": 138.300,
        "addresses": {
            "en": "Tateshina, Nagano, Japan",
            "ko": "일본 나가노현 다테시나",
        },
        "features": "Highland, Forest, Cool summer",
        "website": "",
        "blurb_en": "Nagano highland forest camping — cool summers and classic Japanese auto-camp parks.",
        "blurb_ko": "나가노 고원 숲 캠핑. 시원한 여름과 클래식 오토캠프.",
    },
    {
        "id": "nagano_karuizawa_camp",
        "activity": "camp",
        "region": "nagano",
        "names": {"en": "Karuizawa / Asama Camp Bases", "ko": "가루이자와·아사마 캠프"},
        "lat": 36.348,
        "lng": 138.597,
        "addresses": {
            "en": "Karuizawa, Nagano, Japan",
            "ko": "일본 나가노현 가루이자와정",
        },
        "features": "Resort town, Easy access, Family",
        "website": "",
        "blurb_en": "Camp near Karuizawa resort town — Shinkansen access and forest sites under Mt. Asama.",
        "blurb_ko": "가루이자와 리조트 타운 근처 캠프. 신칸센과 아사마산 아래 숲 사이트.",
    },
    {
        "id": "hokkaido_furano_camp",
        "activity": "camp",
        "region": "hokkaido",
        "names": {"en": "Furano Camp Area", "ko": "후라노 캠프 에리어"},
        "lat": 43.342,
        "lng": 142.383,
        "addresses": {
            "en": "Furano, Hokkaido, Japan",
            "ko": "일본 홋카이도 후라노시",
        },
        "features": "Lavender season, Open sky, Car camp",
        "website": "",
        "blurb_en": "Central Hokkaido camping around Furano — summer lavender season and wide-sky sites.",
        "blurb_ko": "후라노 일대 홋카이도 중부 캠핑. 여름 라벤더와 탁 트인 사이트.",
    },
    {
        "id": "hokkaido_toya_camp",
        "activity": "camp",
        "region": "hokkaido",
        "names": {"en": "Lake Toya Camp Area", "ko": "도야코 캠프 에리어"},
        "lat": 42.580,
        "lng": 140.820,
        "addresses": {
            "en": "Toyako, Hokkaido, Japan",
            "ko": "일본 홋카이도 도야코정",
        },
        "features": "Caldera lake, Onsen nearby, Scenic",
        "website": "",
        "blurb_en": "Caldera-lake camping with nearby onsen towns — strong shoulder-season scenery.",
        "blurb_ko": "칼데라 호수 캠핑과 인근 온천. 어깨 시즌 풍경이 특히 좋음.",
    },
    {
        "id": "kanto_hakone_camp",
        "activity": "camp",
        "region": "kanto",
        "names": {"en": "Hakone / Ashinoko Camp Area", "ko": "하코네·아시노코 캠프"},
        "lat": 35.233,
        "lng": 139.037,
        "addresses": {
            "en": "Hakone, Kanagawa, Japan",
            "ko": "일본 가나가와현 하코네정",
        },
        "features": "Tokyo weekend, Lake, Onsen",
        "website": "",
        "blurb_en": "Tokyo-weekend camping near Hakone and Lake Ashi — pair with onsen and ropeways.",
        "blurb_ko": "도쿄 주말 하코네·아시노코 캠핑. 온천·로프웨이와 조합.",
    },
    {
        "id": "chubu_norikura_camp",
        "activity": "camp",
        "region": "chubu",
        "names": {"en": "Norikura Highland Camp", "ko": "노리쿠라 고원 캠프"},
        "lat": 36.120,
        "lng": 137.580,
        "addresses": {
            "en": "Norikura Highland, Gifu / Nagano border, Japan",
            "ko": "일본 기후·나가노 노리쿠라 고원",
        },
        "features": "Alpine road, Cool, Scenic",
        "website": "",
        "blurb_en": "High-elevation camping near the Norikura skyline road — cool nights and alpine scenery.",
        "blurb_ko": "노리쿠라 스카이라인 근처 고지 캠핑. 선선한 밤과 알파인 풍경.",
    },
    {
        "id": "chugoku_setouchi_camp",
        "activity": "camp",
        "region": "chugoku",
        "names": {"en": "Setouchi Island Camp Stops", "ko": "세토우치 섬 캠프 스톱"},
        "lat": 34.300,
        "lng": 133.200,
        "addresses": {
            "en": "Seto Inland Sea islands, Hiroshima area, Japan",
            "ko": "일본 히로시마 일대 세토내해 섬",
        },
        "features": "Island, Mild climate, Art islands nearby",
        "website": "",
        "blurb_en": "Mild Seto Inland Sea camping — island hops near art islands and ferry routes.",
        "blurb_ko": "온화한 세토내해 섬 캠핑. 아트 섬·페리 루트와 이어짐.",
    },
]


def _category(activity: str) -> str:
    return ACTIVITY_META[activity]["category"]


def article(lang: str, seed: dict[str, Any]) -> str:
    activity = seed["activity"]
    meta = ACTIVITY_META[activity]
    name = seed["names"][lang]
    addr = seed["addresses"][lang]
    website = (seed.get("website") or "").strip()
    website_line = f"website: \"{website}\"\n" if website else "website: \"\"\n"
    cat = _category(activity)

    if lang == "ko":
        blurb = seed["blurb_ko"]
        body = f"""## 개요

**{name}** — {blurb}

JPFun 지도에서 같은 지역의 다른 레저 스팟과 함께 볼 수 있습니다.

## 포인트

- 활동: {meta['label_ko']}
- 지역 키: {seed['region']}
- 특징: {seed.get('features') or meta['label_ko']}

## 여행 팁

- 시즌·날씨·조수(서프/다이브)를 출발 전에 확인하세요.
- 렌탈·스쿨·보트는 성수기 예약을 권장합니다.
- 근처 숙소는 지도의 Stay 핀 또는 Rakuten / Klook로 이어집니다.
"""
        summary = blurb
    else:
        blurb = seed["blurb_en"]
        body = f"""## Overview

**{name}** — {blurb}

Browse it on the JPFun map alongside other leisure spots in the same region.

## Highlights

- Activity: {meta['label_en']}
- Region key: {seed['region']}
- Features: {seed.get('features') or meta['label_en']}

## Trip tips

- Check season, weather, and tides (surf/dive) before you go.
- Book rentals, schools, and boats early in peak months.
- Nearby lodging: map Stay pins or Rakuten / Klook from the detail page.
"""
        summary = blurb

    return f"""---
lang: {lang}
title: "{name}"
lat: {seed['lat']}
lng: {seed['lng']}
activity: "{activity}"
categories: ["{cat}"]
thumbnail: "/static/images/{seed['id']}.jpg"
address: "{addr}"
date: "{TODAY}"
{website_line}summary: "{summary}"
image_prompt: ""
region: "{seed['region']}"
---

{body}
"""
