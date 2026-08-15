"""
Long-form copy for resorts beyond the original 12 priority destinations.
Facts → EN/KO markdown with the same section layout as ski_longform.LONGFORM.
"""
from __future__ import annotations

from typing import Any


def _bullets(lines: list[str]) -> str:
    return "\n".join(f"- {line}" for line in lines)


def _render(name: str, hook: str, slopes: list[str], season: list[str], access: list[str], stay: list[str], tips: list[str], lang: str) -> str:
    if lang == "en":
        return f"""## Overview

{hook}

JPFun maps nearby **Stay** and **Food** pins so you can plan lodging and meals without random map scrolling.

## Slopes & lifts

{_bullets(slopes)}

## Season & snow

{_bullets(season)}

## Getting there

{_bullets(access)}

## Stay & village life

{_bullets(stay)}

## JPFun tips

{_bullets(tips)}
"""
    return f"""## 개요

{hook}

JPFun 지도에는 근처 **숙소(Stay)**·**맛집(Food)** 핀을 표시해 슬로프 후 일정을 빠르게 짤 수 있습니다.

## 슬로프·리프트

{_bullets(slopes)}

## 시즌·적설

{_bullets(season)}

## 오는 길

{_bullets(access)}

## 숙소·마을

{_bullets(stay)}

## JPFun 팁

{_bullets(tips)}
"""


def entry(
    *,
    summary_en: str,
    summary_ko: str,
    name_en: str,
    name_ko: str,
    hook_en: str,
    hook_ko: str,
    slopes_en: list[str],
    slopes_ko: list[str],
    season_en: list[str],
    season_ko: list[str],
    access_en: list[str],
    access_ko: list[str],
    stay_en: list[str],
    stay_ko: list[str],
    tips_en: list[str],
    tips_ko: list[str],
) -> dict[str, str]:
    return {
        "summary_en": summary_en,
        "summary_ko": summary_ko,
        "en": _render(name_en, hook_en, slopes_en, season_en, access_en, stay_en, tips_en, "en"),
        "ko": _render(name_ko, hook_ko, slopes_ko, season_ko, access_ko, stay_ko, tips_ko, "ko"),
    }


# Unique facts per resort id (36 expansion resorts).
_FACTS: dict[str, dict[str, Any]] = {
    "niseko_village": entry(
        summary_en="Niseko Village — quieter United base, Hilton stays, and gondola access to Annupuri powder.",
        summary_ko="니세코 빌리지 — 조용한 유나이트 베이스, 힐튼·곤돌라 접근 가이드.",
        name_en="Niseko Village",
        name_ko="니세코 빌리지",
        hook_en="**Niseko Village** is the quieter corner of **Niseko United**, centered on the Hilton and gondola lifts on the Annupuri face. It suits skiers who want resort hotels, fewer bar crowds than Hirafu, and the same deep Hokkaido powder once you link to the other three areas.",
        hook_ko="**니세코 빌리지**는 **니세코 유나이트** 중 상대적으로 한산한 베이스로, 힐튼과 곤돌라가 중심입니다. 히라후보다 술집·혼잡이 적고 리조트 호텔 중심 일정을 원할 때 좋습니다. 연결권으로 다른 3개 구역 파우더도 즐길 수 있습니다.",
        slopes_en=[
            "Gondola-led access to mid-mountain; greener learning areas near the base.",
            "Intermediate groomers and tree pockets once you ride higher toward Annupuri.",
            "Niseko United multi-area tickets unlock Hirafu / Hanazono / Annupuri connections (season rules vary).",
            "English rental and lesson desks are common at the Village gondola plaza.",
        ],
        slopes_ko=[
            "곤돌라로 중봉 접근이 쉽고, 베이스 근처에 초급 코스가 잘 정비되어 있습니다.",
            "상부로 올라갈수록 중급 정비면·트리런 옵션이 늘며 아누푸리 방면과 연결됩니다.",
            "유나이트 연결권으로 히라후·하나조노·아누푸리 이동이 가능합니다(시즌별 규정 확인).",
            "빌리지 곤돌라 플라자에 영어 렌탈·강습 데스크가 많습니다.",
        ],
        season_en=[
            "Typical season: late November – early May.",
            "Deepest powder usually January–February; cloud decks are common.",
            "Holiday weeks (New Year / Lunar New Year) sell out Village hotels early.",
        ],
        season_ko=[
            "시즌: 보통 11월 말~5월 초.",
            "1~2월 파우더가 두껍고, 흐린 눈구름이 잦습니다.",
            "연말·설 연휴는 빌리지 호텔이 빨리 마감됩니다.",
        ],
        access_en=[
            "From New Chitose (CTS): ~2–2.5 h shuttle or rental car to Village / Higashiyama.",
            "From Hirafu: short taxi or United transport between villages.",
            "From Seoul: fly ICN→CTS, then pre-book airport transfer in winter.",
        ],
        access_ko=[
            "신치토세(CTS)에서 셔틀·렌터카로 약 2~2.5시간.",
            "히라후와는 택시 또는 유나이트 교통편으로 짧게 연결됩니다.",
            "서울→신치토세 비행 후 겨울에는 공항 셔틀을 미리 예약하세요.",
        ],
        stay_en=[
            "Hilton Niseko Village anchors the base with ski-in convenience.",
            "Condos and chalets around Higashiyama offer quieter nights.",
            "For nightlife, plan an evening hop to Hirafu and return by taxi.",
        ],
        stay_ko=[
            "힐튼 니세코 빌리지가 베이스 숙소의 중심입니다.",
            "히가시야마 콘도·샬레는 밤에 더 조용합니다.",
            "밤 분위기가 필요하면 히라후를 다녀오는 일정을 잡으세요.",
        ],
        tips_en=[
            "Compare Village-only tickets vs full United passes before arrival.",
            "Use JPFun Stay pins within shuttle range of the Village gondola.",
            "On whiteout days, book onsen time at Village or nearby Annupuri baths.",
        ],
        tips_ko=[
            "빌리지 단독권과 유나이트 전권 상품을 비교해 예약하세요.",
            "곤돌라 인근 Stay 핀을 기준으로 숙소를 고르면 동선이 짧아집니다.",
            "시야가 나쁜 날은 빌리지·아누푸리 온천으로 일정을 바꾸세요.",
        ],
    ),
    "kiroro": entry(
        summary_en="Kiroro Resort — high snowfall near Otaru, long runs, and family hotel packages.",
        summary_ko="킬로로 — 오타루 인근 다설, 긴 코스·패밀리 호텔 가이드.",
        name_en="Kiroro Resort",
        name_ko="킬로로 리조트",
        hook_en="**Kiroro** sits west of Sapporo toward Otaru and is famous for **heavy, dry snow** and long cruisers. It feels more self-contained than Niseko — ski hotel packages, kids programs, and fewer bar streets — which many families prefer.",
        hook_ko="**킬로로**는 삿포로~오타루 방면의 다설 리조트로, **건조한 적설**과 긴 슬로프가 강점입니다. 니세코보다 자급형 호텔·패밀리 패키지 중심이라 술집 거리보다 리조트 안에서 머무는 일정에 잘 맞습니다.",
        slopes_en=[
            "Large vertical for Hokkaido day resorts — long intermediate highways.",
            "Powder pockets after storms; respect boundary ropes and patrol notes.",
            "Snow park and learning zones near the main hotel village.",
            "Efficient chair / gondola layout keeps queue times reasonable midweek.",
        ],
        slopes_ko=[
            "홋카이도 데이 리조트 중에서도 낙차가 큰 편으로 중급 장거리 코스가 매력입니다.",
            "강설 후 파우더 포켓이 생기며, 경계·패트롤 안내를 반드시 따르세요.",
            "호텔 빌리지 근처에 파크·초급존이 있습니다.",
            "주중에는 리프트 대기가 비교적 짧습니다.",
        ],
        season_en=[
            "Season often stretches late autumn into spring.",
            "Peak powder: January–February cold snaps.",
            "Coastal wind events can lower visibility — build a flexible day plan.",
        ],
        season_ko=[
            "늦은 가을부터 봄까지 시즌이 길게 이어지는 편입니다.",
            "1~2월 한파 시 파우더가 가장 좋습니다.",
            "연안 바람으로 시야가 나빠질 수 있어 여유 일정을 두세요.",
        ],
        access_en=[
            "From CTS: ~1.5–2 h by car toward Otaru mountains.",
            "From Sapporo: day-trip feasible with early start (~1–1.5 h).",
            "Hotel buses or private transfers common for package guests.",
        ],
        access_ko=[
            "CTS에서 오타루 산지로 차로 약 1.5~2시간.",
            "삿포로에서 이른 출발이면 당일 코스로도 가능합니다.",
            "패키지 투숙객은 호텔 버스·전세 차량이 일반적입니다.",
        ],
        stay_en=[
            "Stay on-mountain for ski-in ease and buffet dinners.",
            "Otaru / Asari bases work if you want city dining at night.",
            "Families should book kids rooms and lesson slots together.",
        ],
        stay_ko=[
            "산에서 숙박하면 스키인·저녁 뷔페가 편합니다.",
            "밤에 도시 식사를 원하면 오타루·아사리도 후보입니다.",
            "패밀리는 키즈룸과 강습을 같이 예약하세요.",
        ],
        tips_en=[
            "If Niseko is sold out, Kiroro is a strong powder backup closer to CTS.",
            "Check wind holds on open ridgelines before committing to top lifts.",
            "Pair a ski day with Otaru canal / sushi evening when roads are clear.",
        ],
        tips_ko=[
            "니세코가 마감이면 CTS에 더 가까운 킬로로가 좋은 대안입니다.",
            "능선 리프트는 강풍 운휴를 미리 확인하세요.",
            "도로가 열리면 저녁에 오타루를 묶어보세요.",
        ],
    ),
    "tomamu": entry(
        summary_en="Hoshino Resorts Tomamu — Unkai terrace views, Ice Village, and all-ages ski packages.",
        summary_ko="토마무 — 운해 테라스·아이스빌리지·패밀리 패키지 가이드.",
        name_en="Hoshino Resorts Tomamu",
        name_ko="호시노 리조트 토마무",
        hook_en="**Tomamu** is a Hoshino Resorts destination in central Hokkaido known for the **Unkai Terrace** cloud-sea viewpoint, Ice Village in midwinter, and a compact ski area tied to large hotels. Ideal when non-skiers travel with skiers.",
        hook_ko="**토마무**는 홋카이도 중부의 호시노 리조트로, **운해 테라스**·한겨울 아이스빌리지와 호텔 밀착형 스키장으로 유명합니다. 스키를 타지 않는 동행이 있을 때 일정을 맞추기 좋습니다.",
        slopes_en=[
            "Friendly intermediate terrain and learning zones near the base hotels.",
            "Enough vertical for half-day to full-day sessions without huge transfers.",
            "Night skiing or floodlit activities may run on select dates.",
            "Rental / lesson desks sit inside the resort complex.",
        ],
        slopes_ko=[
            "호텔 베이스 중심의 중급·초급 코스가 친숙합니다.",
            "이동 없이 반나절~하루 스키가 가능한 규모입니다.",
            "야간 스키·야간 액티비티가 일정에 맞춰 운영됩니다.",
            "렌탈·강습은 리조트 단지 안에서 해결됩니다.",
        ],
        season_en=[
            "Ski season: roughly December – March (confirm official calendar).",
            "Unkai Terrace is weather-dependent — go early and have a backup plan.",
            "Ice Village usually opens in peak winter weeks only.",
        ],
        season_ko=[
            "스키 시즌: 대략 12~3월(공식 캘린더 확인).",
            "운해 테라스는 날씨 의존적이라 이른 방문·대체 일정이 필요합니다.",
            "아이스빌리지는 한겨울 한정인 경우가 많습니다.",
        ],
        access_en=[
            "From CTS: ~2–2.5 h by car or resort shuttle along expressways.",
            "JR to Tomamu Station + resort bus is workable without a car.",
            "From Seoul: CTS arrival then resort transfer packages are popular.",
        ],
        access_ko=[
            "CTS에서 고속도로로 약 2~2.5시간 또는 리조트 셔틀.",
            "JR 토마무역 + 리조트 버스로 차량 없이 접근 가능합니다.",
            "서울 출발은 CTS 도착 후 리조트 트랜스퍼 패키지가 흔합니다.",
        ],
        stay_en=[
            "Tower / wing hotels keep everything indoors between ski and dinner.",
            "Book Unkai Terrace tickets with lodging whenever possible.",
            "Dining is resort-centric — reserve peak dinner slots.",
        ],
        stay_ko=[
            "타워·윙 호텔에서 스키와 식사가 단지 안에서 이어집니다.",
            "가능하면 숙박과 운해 티켓을 묶으세요.",
            "식사는 리조트 중심이라 피크 시간 예약을 권장합니다.",
        ],
        tips_en=[
            "Use JPFun for nearby Stay if hotels are full; shuttles may still reach the slopes.",
            "Split days: ski morning + Unkai or Ice Village afternoon.",
            "Wind / fog can cancel terrace visits — watch morning forecasts.",
        ],
        tips_ko=[
            "호텔이 만실이면 JPFun Stay로 셔틀권 숙소를 찾으세요.",
            "오전 스키 + 오후 운해/아이스빌리지 분할 일정이 무난합니다.",
            "안개·강풍 시 테라스가 운휴될 수 있습니다.",
        ],
    ),
    "sahoro": entry(
        summary_en="Sahoro Resort — Tokachi powder, quieter slopes, and onsen hotel base.",
        summary_ko="사호로 — 도카치 파우더·한산한 슬로프·온천 호텔 가이드.",
        name_en="Sahoro Resort",
        name_ko="사호로 리조트",
        hook_en="**Sahoro** in Tokachi offers a calmer alternative to Niseko with reliable powder, forested runs, and a classic ski-hotel + onsen setup. Strong pick for groups who want fewer crowds and easy pacing.",
        hook_ko="**사호로**는 도카치의 조용한 파우더 리조트로, 숲 슬로프와 스키+온천 호텔 조합이 강점입니다. 혼잡을 줄이고 느긋하게 타려는 팀에 잘 맞습니다.",
        slopes_en=[
            "Tree-lined cruisers and soft powder after Pacific-side storms.",
            "Manageable size — easy to learn the map in one morning.",
            "Beginner belts and family slopes near the hotel base.",
            "Advanced chutes exist but stay within marked boundaries.",
        ],
        slopes_ko=[
            "숲길 정비면과 태평양 측 강설 후 소프트 파우더가 매력입니다.",
            "규모가 파악하기 쉬워 오전에 코스맵을 익힐 수 있습니다.",
            "호텔 베이스에 초급·패밀리 코스가 있습니다.",
            "상급 슈트도 있으나 표시된 경계를 지키세요.",
        ],
        season_en=[
            "Core season December – March.",
            "Cold Tokachi air keeps snow dry; temperatures can drop sharply.",
            "Weekdays are notably quiet outside Japanese holidays.",
        ],
        season_ko=[
            "핵심 시즌 12~3월.",
            "도카치 한기로 눈이 건조하고 기온이 급락할 수 있습니다.",
            "일본 연휴를 피하면 주중은 매우 한산합니다.",
        ],
        access_en=[
            "From CTS: ~2.5–3 h drive toward Obihiro / Shintoku.",
            "Obihiro Airport is closer for some international connections.",
            "Rental car recommended for flexible Tokachi sightseeing.",
        ],
        access_ko=[
            "CTS에서 오비히로·신토쿠 방면 약 2.5~3시간.",
            "국제선에 따라 오비히로 공항이 더 가까울 수 있습니다.",
            "도카치 관광을 묶으려면 렌터카가 편합니다.",
        ],
        stay_en=[
            "Sahoro Resort Hotel is the default ski-in base with onsen baths.",
            "Limited village nightlife — evenings are hotel / onsen focused.",
            "Book half-board if you want simple logistics.",
        ],
        stay_ko=[
            "사호로 리조트 호텔이 스키인·온천의 기본 베이스입니다.",
            "마을 밤문화는 적고 저녁은 호텔·온천 중심입니다.",
            "일정을 단순화하려면 반연금이 좋습니다.",
        ],
        tips_en=[
            "Great recovery day resort after intense Niseko powder days.",
            "Pack cold-weather layers — Tokachi mornings can be -15°C.",
            "Check road ice between Shintoku and the resort after storms.",
        ],
        tips_ko=[
            "니세코에서 강하게 탄 뒤 회복일로도 적합합니다.",
            "아침 -15°C까지 내려갈 수 있어 방한층을 챙기세요.",
            "강설 후 신토쿠~스키장 도로 결빙을 확인하세요.",
        ],
    ),
    "sapporo_teine": entry(
        summary_en="Sapporo Teine — city-side skiing, Olympic heritage, and easy Sapporo day trips.",
        summary_ko="삿포로 테이네 — 시내권 스키·올림픽 유산·당일 코스 가이드.",
        name_en="Sapporo Teine",
        name_ko="삿포로 테이네",
        hook_en="**Sapporo Teine** is the classic **city mountain** for Sapporo stays — Olympic history, night skiing options, and a quick hop from downtown hotels. Perfect when you want powder without relocating to a remote village.",
        hook_ko="**삿포로 테이네**는 삿포로에서 가깝게 즐기는 **시내권 스키장**으로, 올림픽 유산과 야간 스키가 강점입니다. 산골 숙소로 옮기지 않고 시티호텔 기반 일정을 짤 때 좋습니다.",
        slopes_en=[
            "Olympic-era steeps plus wider family runs on separate faces.",
            "Night sessions make short winter days productive.",
            "Busy weekends — midweek tickets feel smoother.",
            "Rentals near the base; English support varies by shop.",
        ],
        slopes_ko=[
            "올림픽 당시 급경사와 패밀리용 완만면이 구역별로 나뉩니다.",
            "야간 스키로 짧은 겨울 낮을 보완할 수 있습니다.",
            "주말은 붐비므로 주중권이 여유롭습니다.",
            "베이스 렌탈은 많지만 영어 대응은 매장마다 다릅니다.",
        ],
        season_en=[
            "Usually December – March; lower elevations melt earlier than Niseko.",
            "Fresh snow after Sapporo storms can be excellent for a day or two.",
            "Check freeze-thaw crust in late March.",
        ],
        season_ko=[
            "보통 12~3월, 낮은 고도라 니세코보다 봄이 이릅니다.",
            "삿포로 강설 직후 하루이틀은 컨디션이 좋습니다.",
            "3월 하순은 동결·해빙 크러스트를 확인하세요.",
        ],
        access_en=[
            "From central Sapporo: ~30–50 min by bus / taxi / car.",
            "From CTS: into Sapporo first, then Teine the next morning.",
            "Parking fills on powder mornings — leave early.",
        ],
        access_ko=[
            "삿포로 시내에서 버스·택시·차로 약 30~50분.",
            "CTS 도착 당일은 시내 숙소, 다음날 테이네 일정이 무난합니다.",
            "파우더 아침에는 주차장이 빨리 찹니다.",
        ],
        stay_en=[
            "Stay in Sapporo Susukino / station area for dining and nightlife.",
            "Onsen day trips to Jozankei pair well after Teine.",
            "Skip remote chalets unless you also visit Niseko.",
        ],
        stay_ko=[
            "식사·밤문화는 스스키노·삿포로역 숙소가 편합니다.",
            "테이네 후 조잔케이 온천을 묶기 좋습니다.",
            "니세코까지 가지 않는다면 외딴 샬레는 필수는 아닙니다.",
        ],
        tips_en=[
            "Use Teine for arrival / departure buffer days around CTS flights.",
            "Combine with Sapporo Beer Museum or soup curry nights downtown.",
            "JPFun Stay pins in Sapporo make multi-resort city bases easy.",
        ],
        tips_ko=[
            "CTS 출입국 완충일에 테이네를 넣기 좋습니다.",
            "시내 스프카레·맥주박물관과 조합하세요.",
            "시티 베이스면 여러 스키장을 번갈아 가기 쉽습니다.",
        ],
    ),
    "sapporo_kokusai": entry(
        summary_en="Sapporo Kokusai — powder bowl near Sapporo, tree skiing, and accessible day lifts.",
        summary_ko="삿포로 국제 — 삿포로 근교 파우더·트리런·데이 스키 가이드.",
        name_en="Sapporo Kokusai Ski Resort",
        name_ko="삿포로 국제 스키장",
        hook_en="**Sapporo Kokusai** is a powder favorite just outside the city — steeper bowls, tree skiing, and a day-trip culture from Sapporo hotels. Less resort village, more mountain day.",
        hook_ko="**삿포로 국제**는 시내에서 가까운 파우더·트리런 명소로, 리조트 마을보다 **데이 스키** 느낌이 강합니다. 숙소는 삿포로에 두고 출퇴근하듯 타기 좋습니다.",
        slopes_en=[
            "Steeper pitches and glades after storms — intermediates should warm up carefully.",
            "Groomed routes for cruising when visibility drops.",
            "Queues spike after overnight dumps; arrive for first lifts.",
            "Limited beginner terrain compared with Teine — families check maps first.",
        ],
        slopes_ko=[
            "강설 후 급사면·글레이드가 매력입니다. 중급도 워밍업을 충분히 하세요.",
            "시야가 나쁠 때는 정비면을 중심으로 타세요.",
            "밤새 눈이 오면 오전 대기줄이 깁니다 — ファースト 리프트를 노리세요.",
            "테이네보다 초급면이 적어 패밀리는 코스맵을 먼저 확인하세요.",
        ],
        season_en=[
            "Peak powder weeks in January–February.",
            "Season typically December – late March.",
            "Wind holds possible on exposed ridges.",
        ],
        season_ko=[
            "1~2월 파우더가 피크입니다.",
            "시즌은 대략 12월~3월 하순.",
            "노출된 능선은 강풍 운휴가 있습니다.",
        ],
        access_en=[
            "From Sapporo: ~1 h by car / seasonal bus.",
            "Rendezvous with rental cars from downtown shops.",
            "Chains or winter tires mandatory after storms.",
        ],
        access_ko=[
            "삿포로에서 차·시즌 버스로 약 1시간.",
            "시내 렌터카 숍에서 픽업 후 이동하는 패턴이 흔합니다.",
            "강설 후 체인 또는 윈터타이어가 필수입니다.",
        ],
        stay_en=[
            "Base in Sapporo; few hotels at the mountain itself.",
            "Après in Susukino rather than on-hill bars.",
            "Onsen options in nearby valleys on rest days.",
        ],
        stay_ko=[
            "숙소는 삿포로 시내가 기본이고 산 아래 호텔은 적습니다.",
            "애프터스키는 스스키노에서 즐기세요.",
            "쉬는 날 인근 계곡 온천을 이용하세요.",
        ],
        tips_en=[
            "Pair Teine (city lights / family) with Kokusai (powder day) in one Sapporo trip.",
            "Download a map offline — cell service can dip in the trees.",
            "Watch avalanche / closed-area signage carefully.",
        ],
        tips_ko=[
            "한 번의 삿포로 여행에서 테이네(패밀리)·국제(파우더)를 조합하세요.",
            "트리 구간은 통신이 약할 수 있어 오프라인 맵을 준비하세요.",
            "폐쇄 구역·안전자료 표시를 꼭 확인하세요.",
        ],
    ),
    "asahidake": entry(
        summary_en="Asahidake Ropeway Ski Area — backcountry-leaning Daisetsuzan terrain and onsen village.",
        summary_ko="아사히다케 — 다이세쓰잔 백컨트리형 지형·온천 마을 가이드.",
        name_en="Asahidake Ropeway Ski Area",
        name_ko="아사히다케 로프웨이 스키 에리어",
        hook_en="**Asahidake** is not a mega resort — it is a **ropeway + hiking / ski touring** gateway on Daisetsuzan with volcanic scenery and a hot-spring village. Best for advanced riders comfortable with ungroomed snow and alpine weather.",
        hook_ko="**아사히다케**는 대형 리조트가 아니라 다이세쓰잔의 **로프웨이·스키 투어** 관문으로, 화산 경관과 온천 마을이 매력입니다. 비정비면·산악 날씨에 익숙한 중상급 이상에게 잘 맞습니다.",
        slopes_en=[
            "Limited marked alpine skiing; many guests ski / board tourist tracks from the ropeway.",
            "True adventure skiing needs guidance, beacons, and current mountain reports.",
            "Terrain is steep and wind-affected — conditions change hourly.",
            "Not ideal as a first Japan ski day for complete beginners.",
        ],
        slopes_ko=[
            "정비된 알파인 코스는 적고 로프웨이 관광 트랙 중심입니다.",
            "본격 백컨트리는 가이드·비콘·산악 예보가 필요합니다.",
            "가파르고 바람에 민감해 컨디션이 시간마다 바뀝니다.",
            "완전 초보의 일본 첫 스키일로 추천하지 않습니다.",
        ],
        season_en=[
            "Ropeway and snow access vary — verify seasonal operations.",
            "Deep winter brings serious cold and wind.",
            "Spring can offer stable corn on guided days.",
        ],
        season_ko=[
            "로프웨이·설상 이용은 시즌별로 다르니 공식 일정을 확인하세요.",
            "한겨울은 혹한·강풍이 흔합니다.",
            "봄에는 가이드와 함께 콘 스노를 노리기도 합니다.",
        ],
        access_en=[
            "Fly into Asahikawa or drive from Sapporo (~2.5–3 h).",
            "Buses to Asahidake Onsen are limited — check timetables.",
            "Car rental helpful for weather flexibility.",
        ],
        access_ko=[
            "아사히카와 공항 또는 삿포로에서 차 ~2.5~3시간.",
            "온천 마을행 버스는 제한적이라 시간표를 확인하세요.",
            "날씨 대응을 위해 렌터카가 유리합니다.",
        ],
        stay_en=[
            "Ryokan and pensions in Asahidake Onsen with sulfur baths.",
            "Quiet nights — pack snacks if shops close early.",
            "Book rooms with drying space for wet gear.",
        ],
        stay_ko=[
            "아사히다케 온천의 료칸·펜션이 기본입니다.",
            "밤이 조용하고 상점이 일찍 닫을 수 있습니다.",
            "장비 건조 공간이 있는 방을 고르세요.",
        ],
        tips_en=[
            "Treat Asahidake as a specialty day within a wider Hokkaido itinerary.",
            "Carry goggles for volcanic / whiteout light.",
            "Respect geothermal hazards and stay on allowed routes.",
        ],
        tips_ko=[
            "홋카이도 일정의 스페셜 데이로 넣는 것이 좋습니다.",
            "화산재·화이트아웃에 대비한 고글을 챙기세요.",
            "지열 위험 구역을 피하고 허용 루트만 이용하세요.",
        ],
    ),
    "hakuba_iwatake": entry(
        summary_en="Hakuba Iwatake — sunny faces, gondola views, and family terrain near Hakuba village.",
        summary_ko="하쿠바 이와타케 — 양지·곤돌라 전망·패밀리 지형 가이드.",
        name_en="Hakuba Iwatake Mountain Resort",
        name_ko="하쿠바 이와타케",
        hook_en="**Iwatake** sits on a sunnier Hakuba face with gondola views toward the Northern Alps. It is a strong family and intermediate base that links into the wider Hakuba Valley itinerary without the Happo steeps.",
        hook_ko="**이와타케**는 하쿠바에서도 양지바 슬로프와 북알프스 전망이 좋은 곤돌라 리조트입니다. 해포의 급한 코스 대신 패밀리·중급 중심으로 하쿠바 밸리 일정을 짜기 좋습니다.",
        slopes_en=[
            "Wide groomers and mellow learning areas near the mountain gondola.",
            "Intermediate cruisers with photo-worthy ridgeline views.",
            "Snow park features on select runs in season.",
            "Connect lodging via Hakuba valley shuttles.",
        ],
        slopes_ko=[
            "곤돌라 근처 넓은 정비면·초급존이 잘 갖춰져 있습니다.",
            "중급 크루저와 능선 전망이 인상적입니다.",
            "시즌에 따라 파크 지형이 운영됩니다.",
            "하쿠바 밸리 셔틀로 숙소와 연결됩니다.",
        ],
        season_en=[
            "December – March core; valley snow is less deep than Happo high alpine.",
            "Sunny aspect means faster afternoon softening — ski hardpack mornings.",
            "Foggy Hakuba days still offer usable lower lifts.",
        ],
        season_ko=[
            "핵심 시즌 12~3월, 해포 고산보다 적설은 적을 수 있습니다.",
            "양지라 오후 눈이 빨리 물러집니다 — 오전 하드팩을 노리세요.",
            "안개 낀 날에도 하부 리프트는 비교적 운영됩니다.",
        ],
        access_en=[
            "From Nagano: Alpine / Otari buses into Hakuba (~1 h+).",
            "From Tokyo: Hokuriku Shinkansen to Nagano, then bus.",
            "Valley car rentals help hop between Iwatake, Happo, and Goryu.",
        ],
        access_ko=[
            "나가노에서 알파인/오타리 버스 등으로 하쿠바 진입.",
            "도쿄에서 호쿠리쿠 신칸센→나가노→버스.",
            "이와타케·해포·고류를 오가려면 밸리 렌터카가 편합니다.",
        ],
        stay_en=[
            "Stay in Hakuba village or Kamishiro for restaurant variety.",
            "Some lodges offer Iwatake shuttle stops — confirm winter routes.",
            "Onsen hotels in Hakuba town after sunny days.",
        ],
        stay_ko=[
            "식당 선택지를 위해 하쿠바 마을·가미시로 숙소를 추천합니다.",
            "이와타케 셔틀 정류장이 있는 숙소를 확인하세요.",
            "양지에서 탄 뒤에는 하쿠바 온천 호텔이 좋습니다.",
        ],
        tips_en=[
            "Use Iwatake as a recovery day after Happo powder chase days.",
            "Bring sunscreen — reflection on sunny slopes is strong.",
            "Compare valley lifts passes that include Iwatake.",
        ],
        tips_ko=[
            "해포에서 강하게 탄 다음날 회복일로 적합합니다.",
            "양지 반사광이 세니 선크림을 챙기세요.",
            "이와타케가 포함된 밸리 공통권을 비교하세요.",
        ],
    ),
    "hakuba_cortina": entry(
        summary_en="Hakuba Cortina — powder trees, quieter Hakuba north, and lodge-style stays.",
        summary_ko="하쿠바 코르티나 — 파우더 트리·북하쿠바 한산 지대 가이드.",
        name_en="Hakuba Cortina",
        name_ko="하쿠바 코르티나",
        hook_en="**Hakuba Cortina** (often paired with Norikura) is a powder-oriented pocket north of central Hakuba. Expect fewer crowds, tree skiing, and lodge culture rather than Happo nightlife.",
        hook_ko="**하쿠바 코르티나**(노리쿠라와 함께 묶이는 경우 많음)는 하쿠바 북쪽의 파우더·트리 중심 스키장입니다. 해포만큼 붐비지 않고 로지 숙박 문화가 강합니다.",
        slopes_en=[
            "Tree runs and soft snow after storms — the main draw.",
            "Groomers for warm-ups; advanced riders hunt glades.",
            "Combined tickets with neighboring Norikura may be offered.",
            "Map literacy helps — foggy forests look similar.",
        ],
        slopes_ko=[
            "강설 후 트리런·소프트 스노가 최대 매력입니다.",
            "정비면으로 몸을 풀고 상급은 글레이드를 찾습니다.",
            "인근 노리쿠라와 연결권이 있을 수 있습니다.",
            "안개 낀 숲은 비슷해 보이니 맵을 자주 확인하세요.",
        ],
        season_en=[
            "Deep midwinter storms dump heavily on northern Hakuba.",
            "Season similar to valley peers: Dec – Mar/Apr.",
            "Road closures possible after big dumps — check village alerts.",
        ],
        season_ko=[
            "한겨울 북하쿠바 강설이 두껍습니다.",
            "시즌은 밸리 다른 스키장과 비슷하게 12~3/4월.",
            "폭설 후 도로 통제가 있을 수 있습니다.",
        ],
        access_en=[
            "Further north than Happo — budget extra shuttle time.",
            "Base in Hakuba or Otari depending on lodging packages.",
            "Taxi costs add up; shared transfers are cheaper for groups.",
        ],
        access_ko=[
            "해포보다 북쪽이므로 셔틀 시간을 여유 있게 잡으세요.",
            "숙소 패키지에 따라 하쿠바 또는 오타리 베이스.",
            "택시비가 커질 수 있어 그룹은 공유 트랜스퍼가 낫습니다.",
        ],
        stay_en=[
            "Mountain lodges and pensions near Cortina / Norikura.",
            "Quieter evenings — cook stays or lodge dinners common.",
            "Book early for powder weeks; inventory is limited.",
        ],
        stay_ko=[
            "코르티나·노리쿠라 인근 로지·펜션이 중심입니다.",
            "밤은 조용하고 숙소 식사·셀프 쿠킹이 흔합니다.",
            "파우더 주간은 숙소가 적어 조기 예약이 필요합니다.",
        ],
        tips_en=[
            "Great contrast day vs crowded Happo One.",
            "Carry a transceiver if guided tree skiing is planned.",
            "Confirm which lifts run on low-crowd midweeks.",
        ],
        tips_ko=[
            "붐비는 해포와 대비되는 한산한 하루로 좋습니다.",
            "가이드 트리런이면 비콘을 챙기세요.",
            "주중 한산일에는 일부 리프트만 운영될 수 있습니다.",
        ],
    ),
    "tsugaike_kogen": entry(
        summary_en="Tsugaike Kogen — huge beginner pasture, gondola to alpine views, Hakuba north access.",
        summary_ko="츠가이케 고원 — 초급 대목장·고산 곤돌라·북하쿠바 접근 가이드.",
        name_en="Tsugaike Kogen",
        name_ko="츠가이케 고원",
        hook_en="**Tsugaike Kogen** is famous for a vast **beginner / intermediate pasture** plus a gondola that climbs toward dramatic alpine scenery. Ideal for mixed-ability groups based in northern Hakuba / Otari.",
        hook_ko="**츠가이케 고원**은 넓은 **초·중급 목장형 슬로프**와 고산 전망 곤돌라로 유명합니다. 실력이 섞인 팀이나 북하쿠바·오타리 숙소 일정에 잘 맞습니다.",
        slopes_en=[
            "One of Japan's more generous beginner zones by acreage.",
            "Progressive intermediate terrain as you ride higher.",
            "Alpine gondola sections can close in wind — have a lower-mountain plan.",
            "Family-friendly rental and lesson density near the plaza.",
        ],
        slopes_ko=[
            "일본에서도 면적이 넓은 초급존으로 꼽힙니다.",
            "상부로 갈수록 중급 코스가 이어집니다.",
            "고산 곤돌라는 강풍 운휴가 있어 하부 플랜 B가 필요합니다.",
            "플라자 주변 렌탈·강습이 밀집해 있습니다.",
        ],
        season_en=[
            "Reliable winter coverage on the plateau; alpine snow lasts longer.",
            "Busy with Japanese family weeks in peak season.",
            "Spring: lower pasture softens early in the day.",
        ],
        season_ko=[
            "고원 쪽은 커버가 안정적이고 고산 눈은 더 오래갑니다.",
            "성수기 일본 패밀리 연휴에 붐빕니다.",
            "봄에는 하부 목장면이 오전에 빨리 물러집니다.",
        ],
        access_en=[
            "Buses from Nagano / Hakuba toward Tsugaike / Otari.",
            "Further than Happo from central Hakuba hotels.",
            "Car helpful if hopping Tsugaike ↔ Cortina ↔ Happo.",
        ],
        access_ko=[
            "나가노·하쿠바에서 츠가이케·오타리행 버스.",
            "하쿠바 중심 호텔에서는 해포보다 멀입니다.",
            "츠가이케↔코르티나↔해포를 오가려면 차가 편합니다.",
        ],
        stay_en=[
            "Tsugaike highland hotels and pensions.",
            "Hakuba town stays with morning shuttle if dining variety matters.",
            "Onsen options around Otari on rest days.",
        ],
        stay_ko=[
            "츠가이케 고원 호텔·펜션이 기본입니다.",
            "식당 선택지를 원하면 하쿠바 시내+오전 셔틀도 가능합니다.",
            "쉬는 날 오타리 온천을 이용하세요.",
        ],
        tips_en=[
            "Best Hakuba base day for true beginners in the group.",
            "Ride the gondola for views even on a short ski day.",
            "Buy tickets that match whether you need alpine access.",
        ],
        tips_ko=[
            "팀에 진짜 초보가 있으면 하쿠바에서 가장 무난한 하루입니다.",
            "스키를 짧게 타더라도 곤돌라 전망은 가치가 있습니다.",
            "고산 구간이 필요 없으면 저렴한 하부권도 비교하세요.",
        ],
    ),
    "shiga_kogen": entry(
        summary_en="Shiga Kogen — Japan's largest linked ski area, altitude snow, and multi-day terrain cards.",
        summary_ko="시가 고원 — 일본 최대급 연결 스키장·고도 적설 가이드.",
        name_en="Shiga Kogen",
        name_ko="시가 고원",
        hook_en="**Shiga Kogen** is one of Japan's **largest interconnected ski networks** — multiple areas under one altitude umbrella near Yamanouchi. Perfect for multi-day cards when you want variety without changing hotels each day.",
        hook_ko="**시가 고원**은 야마노우치 인근의 **대규모 연결 스키 네트워크**로, 숙소를 옮기지 않고도 여러 에리어를 도는 멀티데이 일정에 최적입니다.",
        slopes_en=[
            "Linked areas stretch from gentle family zones to steeper Olympic-era slopes.",
            "High elevation helps snow durability into spring.",
            "Study the all-mountain map — lift links save taxi hops.",
            "Busy Japanese weekends; weekdays feel spacious.",
        ],
        slopes_ko=[
            "패밀리존부터 올림픽급 급사면까지 에리어별로 다양합니다.",
            "고도가 높아 봄까지 눈이 잘 유지됩니다.",
            "전체 맵을 보고 리프트 연결로 택시 이동을 줄이세요.",
            "주말은 붐비고 주중은 여유가 있습니다.",
        ],
        season_en=[
            "Long season relative to lower Nagano areas.",
            "Cold dry periods deliver chalky groomers; storms refill powder pockets.",
            "Confirm which satellite areas are open early/late season.",
        ],
        season_ko=[
            "나가노 저고도 대비 시즌이 긴 편입니다.",
            "한랭 건조기에는 촘촘한 정비면, 강설 후 파우더 포켓이 생깁니다.",
            "시즌 초·말에는 일부 위성 에리어만 열릴 수 있습니다.",
        ],
        access_en=[
            "From Nagano: bus toward Yudanaka / Shiga (~1–1.5 h).",
            "Tokyo: Shinkansen to Nagano, then bus.",
            "Car useful for Jigokudani monkey park side trips.",
        ],
        access_ko=[
            "나가노에서 유다나카·시가행 버스 약 1~1.5시간.",
            "도쿄→나가노 신칸센 후 버스.",
            "지고쿠다니 원숭이공원 곁들이기는 렌터카가 편합니다.",
        ],
        stay_en=[
            "Highland hotels near Hasuike / central lifts.",
            "Yamanouchi onsen towns for evening baths and dining.",
            "Package deals often include area tickets.",
        ],
        stay_ko=[
            "하수이케 등 중심 리프트 근처 고원 호텔.",
            "저녁 온천·식사는 야마노우치 온천가가 편합니다.",
            "숙박 패키지에 에리어권이 포함되는 경우가 많습니다.",
        ],
        tips_en=[
            "Buy a multi-day all-Shiga ticket if staying 3+ ski days.",
            "Add Jigokudani on a rest afternoon for non-ski hours.",
            "Altitude sunburn is real — use SPF high.",
        ],
        tips_ko=[
            "3일 이상이면 시가 전체권이 이득인 경우가 많습니다.",
            "쉬는 오후에는 지고쿠다니를 넣으세요.",
            "고도 자외선이 강해 선크림이 필수입니다.",
        ],
    ),
    "madarao_kogen": entry(
        summary_en="Madarao Kogen — soft powder trees between Nagano and Myoko, freeride friendly.",
        summary_ko="마다라오 고원 — 나가노·묘코 사이 소프트 파우더·프리라이드 가이드.",
        name_en="Madarao Kogen",
        name_ko="마다라오 고원",
        hook_en="**Madarao** straddles the Nagano side toward Myoko and is known for **soft snow and tree skiing**. A favorite among riders who want freeride flavor without full backcountry commitment.",
        hook_ko="**마다라오**는 나가노에서 묘코 방면으로 이어지는 고원으로, **소프트 스노·트리 스키**로 유명합니다. 완전 백컨트리 전은 아니지만 프리라이드 감성을 원하는 라이더에게 인기입니다.",
        slopes_en=[
            "Natural tree spacing after dumps — stay within open gates.",
            "Groomers for warm-up; sidecountry etiquette still applies.",
            "Tangram is nearby for a second mountain day.",
            "Less English signage than Hakuba — screenshot maps.",
        ],
        slopes_ko=[
            "적설 후 자연 트리 간격이 좋습니다. 개방 게이트 안에서만 타세요.",
            "워밍업은 정비면, 사이드컨트리 예절은 여전히 필요합니다.",
            "가까운 타하루에 하룻날을 더 잡을 수 있습니다.",
            "하쿠바보다 영어 표지가 적어 맵 캡처를 권장합니다.",
        ],
        season_en=[
            "Heavy Niigata / Myoko storm track helps fill Madarao midwinter.",
            "Season roughly Dec – Mar.",
            "Foggy forest days: stick to ridgeline groomers.",
        ],
        season_ko=[
            "묘코·니가타 기압골 강설이 한겨울 마다라오를 채웁니다.",
            "시즌 대략 12~3월.",
            "안개 낀 숲에서는 능선 정비면을 중심으로 타세요.",
        ],
        access_en=[
            "From Nagano or Myoko road corridors; rental car preferred.",
            "Limited public transport frequency — check winter buses.",
            "Combine with Iiyama / Nozawa logistics carefully.",
        ],
        access_ko=[
            "나가노·묘코 도로축으로 접근, 렌터카가 유리합니다.",
            "대중교통 배차가 적어 겨울 버스를 확인하세요.",
            "이야마·노자와 일정과 겹치면 동선을 신중히 짜세요.",
        ],
        stay_en=[
            "Pensions and lodges on Madarao plateau.",
            "Quiet après — plan hotel dinners.",
            "Some packages include lift vouchers.",
        ],
        stay_ko=[
            "고원 위 펜션·로지가 중심입니다.",
            "애프터스키는 한산해 숙소 식사가 기본입니다.",
            "리프트 할인권이 포함된 패키지도 있습니다.",
        ],
        tips_en=[
            "Powder mornings fill parking — leave early.",
            "If trees are tracked out, pivot to Tangram or Myoko.",
            "Respect private property beyond ropes.",
        ],
        tips_ko=[
            "파우더 아침 주차가 빨리 찹니다.",
            "트리가 추적되면 타하람·묘코로 이동하세요.",
            "로프 밖 사유지 진입을 금지합니다.",
        ],
    ),
    "tangram_ski_circus": entry(
        summary_en="Tangram Ski Circus — funky terrain park energy near Madarao with hotel base.",
        summary_ko="타하람 스키 서커스 — 마다라오 인근 파크·호텔 베이스 가이드.",
        name_en="Tangram Ski Circus",
        name_ko="타하람 스키 서커스",
        hook_en="**Tangram Ski Circus** is a playful mid-size resort beside Madarao, known for hotel packages, varied pitches, and a slightly circus-like mountain branding. Good second area if Madarao trees are tracked.",
        hook_ko="**타하람 스키 서커스**는 마다라오 옆의 중형 리조트로, 호텔 패키지와 다양한 경사가 특징입니다. 마다라오 트리가 추적된 날의 두 번째 스키장으로 좋습니다.",
        slopes_en=[
            "Mix of groomers and steeper shots for intermediates looking to progress.",
            "Park / freestyle features depending on season builds.",
            "Linked vibe with Madarao area lodging.",
            "Compact enough to learn in a day.",
        ],
        slopes_ko=[
            "정비면과 조금 더 급한 코스가 섞여 중급 성장에 좋습니다.",
            "시즌에 따라 파크·프리스타일 지형이 세워집니다.",
            "숙소는 마다라오권과 공유되는 경우가 많습니다.",
            "하루면 맵을 익힐 수 있는 규모입니다.",
        ],
        season_en=[
            "Similar storm cycles to Madarao / Myoko corridor.",
            "Core season Dec – Mar.",
            "Sunny spells create fun soft snow on lower pitches.",
        ],
        season_ko=[
            "마다라오·묘코 축과 비슷한 강설 패턴입니다.",
            "핵심 시즌 12~3월.",
            "맑은 날 하부에서 소프트 스노를 즐기기 좋습니다.",
        ],
        access_en=[
            "Drive from Nagano / Iiyama; share transfers with Madarao guests.",
            "Public buses limited — confirm hotel shuttles.",
            "Tokyo access via Shinkansen + bus/taxi legs.",
        ],
        access_ko=[
            "나가노·이야마에서 차로, 마다라오 투숙객과 트랜스퍼를 공유하기도 합니다.",
            "대중버스는 한정적이라 호텔 셔틀을 확인하세요.",
            "도쿄는 신칸센 후 버스·택시 환승입니다.",
        ],
        stay_en=[
            "Hotel Tangram and nearby lodges.",
            "Onsen baths after cold powder mornings.",
            "Night dining mostly hotel-centric.",
        ],
        stay_ko=[
            "호텔 타하람과 인근 숙소.",
            "파우더 아침 후 온천이 좋습니다.",
            "저녁 식사는 호텔 중심입니다.",
        ],
        tips_en=[
            "Buy flexible tickets if hopping Madarao ↔ Tangram.",
            "Great for intermediate parks without big-city crowds.",
            "Photograph the quirky mountain facilities — kids love it.",
        ],
        tips_ko=[
            "마다라오↔타하람을 오가면 유연한 티켓이 필요합니다.",
            "대도시만큼 붐비지 않는 중급 파크일로 좋습니다.",
            "독특한 시설 포토존이 아이들과도 잘 맞습니다.",
        ],
    ),
    "karuizawa_prince": entry(
        summary_en="Karuizawa Prince Hotel Ski Resort — easy Tokyo weekend skiing and resort hotel base.",
        summary_ko="가루이자와 프린스 — 도쿄 주말 스키·리조트 호텔 가이드.",
        name_en="Karuizawa Prince Hotel Ski Resort",
        name_ko="가루이자와 프린스 호텔 스키장",
        hook_en="**Karuizawa Prince** is the classic **Tokyo weekend ski** escape — Shinkansen access, Prince Hotel lodging, and a compact, friendly hill. Better for short trips and beginners than deep powder pilgrimages.",
        hook_ko="**가루이자와 프린스**는 **도쿄 주말 스키**의 정석으로, 신칸센·프린스 호텔·컴팩트한 코스가 강점입니다. 딥 파우더 순례보다 짧은 여행·초중급에 적합합니다.",
        slopes_en=[
            "Gentle to intermediate terrain, ideal for first-timers and families.",
            "Night skiing options make Friday evening arrivals useful.",
            "Crowds spike on powder Sundays — go midweek if possible.",
            "Rentals inside the Prince complex streamline logistics.",
        ],
        slopes_ko=[
            "초급~중급 중심이라 첫 스키·패밀리에 적합합니다.",
            "야간 스키로 금요일 저녁 도착도 활용 가능합니다.",
            "파우더 일요일은 혼잡 — 가능하면 주중 방문.",
            "프린스 단지 안 렌탈로 동선이 짧습니다.",
        ],
        season_en=[
            "Shorter / thinner snow periods than Hokkaido or Myoko.",
            "Best windows after cold fronts midwinter.",
            "Artificial snow support on key runs in lean winters.",
        ],
        season_ko=[
            "홋카이도·묘코보다 시즌·적설이 짧고 얇을 수 있습니다.",
            "한겨울 한기 유입 직후가 가장 좋습니다.",
            "눈이 부족한 해에는 주요 코스에 인공설이 보완됩니다.",
        ],
        access_en=[
            "Tokyo → Karuizawa Shinkansen ~70 min, then hotel shuttle / taxi.",
            "Ideal without a rental car.",
            "From Seoul: fly to Tokyo, then rail — no CTS needed.",
        ],
        access_ko=[
            "도쿄→가루이자와 신칸센 약 70분 + 호텔 셔틀·택시.",
            "렌터카 없이도 충분합니다.",
            "서울은 도쿄 공항 후 철도로 — 홋카이도 경유 불필요.",
        ],
        stay_en=[
            "Prince Hotel is the seamless ski-in choice.",
            "Karuizawa town offers cafés, outlets, and summer-resort vibes year-round.",
            "Book early for three-day weekends.",
        ],
        stay_ko=[
            "프린스 호텔이 스키인과 가장 잘 맞습니다.",
            "가루이자와 시내는 카페·아울렛 등 사계절 휴양 분위기가 있습니다.",
            "3일 연휴는 조기 예약이 필요합니다.",
        ],
        tips_en=[
            "Pair skiing morning + Karuizawa espresso walk afternoon.",
            "Not a substitute for Niseko powder goals — set expectations.",
            "Use JPFun Stay if Prince is sold out — walkability varies.",
        ],
        tips_ko=[
            "오전 스키 + 오후 가루이자와 산책이 좋은 조합입니다.",
            "니세코급 파우더를 기대하면 실망할 수 있습니다.",
            "프린스 만실 시 Stay 핀으로 도보 거리를 확인하세요.",
        ],
    ),
    "kagura": entry(
        summary_en="Kagura Ski Resort — huge Niigata vertical linked toward Naeba and Mitsumata.",
        summary_ko="카구라 — 나에바·미츠마타 연결의 니가타 대형 낙차 가이드.",
        name_en="Kagura Ski Resort",
        name_ko="카구라 스키장",
        hook_en="**Kagura** is a major Niigata mountain system with long vertical and connections toward **Mitsumata / Naeba** depending on ticket products. Choose it for big-terrain days within the Yuzawa snow belt.",
        hook_ko="**카구라**는 **미츠마타·나에바** 방면과 연결되는 니가타의 대형 스키 네트워크입니다. 유자와 설상벨트의 넓은 지형을 하루 종일 타고 싶을 때 선택하세요.",
        slopes_en=[
            "Long alpine runs and varied aspect terrain.",
            "Tree and powder options after sea-of-Japan storms.",
            "Study linked tickets carefully — names and inclusions change by year.",
            "Beginner slopes exist but the mountain rewards intermediates+.",
        ],
        slopes_ko=[
            "긴 알파인 코스와 여러 방향의 슬로프가 있습니다.",
            "동해안 기압골 강설 후 트리·파우더 옵션이 좋습니다.",
            "연결권 상품명·포함 범위는 해마다 확인하세요.",
            "초급면도 있으나 중급 이상이 더 즐겁습니다.",
        ],
        season_en=[
            "Deep snow belt — expect frequent storm days.",
            "Season often late Nov / Dec through April at elevation.",
            "Fog and wind can close upper lifts temporarily.",
        ],
        season_ko=[
            "다설 벨트로 강설일이 잦습니다.",
            "고도는 11월 말/12월~4월까지 이어지는 경우도 있습니다.",
            "안개·강풍으로 상부 리프트가 잠시 설 수 있습니다.",
        ],
        access_en=[
            "From Tokyo: Joetsu Shinkansen to Echigo-Yuzawa, then bus / taxi.",
            "Same gateway as Gala / Naeba logistics.",
            "Rental cars help for multi-resort Yuzawa trips.",
        ],
        access_ko=[
            "도쿄→에치고유자와 조에쓰 신칸센 후 버스·택시.",
            "갈라·나에바와 같은 관문입니다.",
            "유자와권 다일정이면 렌터카가 편합니다.",
        ],
        stay_en=[
            "Yuzawa onsen hotels or mountain lodges closer to Kagura.",
            "Gala station area lodging if you want rail convenience.",
            "Book early for Japanese ski holiday weeks.",
        ],
        stay_ko=[
            "유자와 온천 호텔 또는 카구라 가까운 로지.",
            "철도 편의는 갈라역 인근 숙소.",
            "일본 스키 연휴는 조기 예약이 필요합니다.",
        ],
        tips_en=[
            "Compare Kagura-only vs Naeba/Kagura combo tickets.",
            "Great powder alternative when Gala queues explode.",
            "Carry layers — temperature swings with elevation are large.",
        ],
        tips_ko=[
            "카구라 단독권과 나에바 연결권을 비교하세요.",
            "갈라 대기열이 길 때 파우더 대안으로 좋습니다.",
            "고도에 따른 기온 차가 커 레이어를 챙기세요.",
        ],
    ),
    "iwappara": entry(
        summary_en="Iwappara Ski Resort — sunny Yuzawa hill for families and easy Shinkansen day trips.",
        summary_ko="이와파라 — 유자와 패밀리·신칸센 당일권 가이드.",
        name_en="Iwappara Ski Resort",
        name_ko="이와파라 스키장",
        hook_en="**Iwappara** is a friendlier, sunnier Yuzawa option compared with steeper neighbors. Popular with families and day-trippers who ride the Joetsu Shinkansen into Echigo-Yuzawa.",
        hook_ko="**이와파라**는 유자와권에서 비교적 양지바·패밀리 친화적인 스키장입니다. 에치고유자와 신칸센 당일권 손님에게 인기입니다.",
        slopes_en=[
            "Broad beginner / intermediate trails with good visibility on sunny days.",
            "Less intimidating than advanced Kagura pitches.",
            "Busy school holidays — arrive early for rentals.",
            "Night skiing sometimes offered — check the weekly schedule.",
        ],
        slopes_ko=[
            "초·중급 중심의 넓은 코스, 맑은 날 시야가 좋습니다.",
            "카구라 상급면보다 부담이 적습니다.",
            "방학에는 렌탈 혼잡 — 일찍 도착하세요.",
            "야간 스키는 주간 스케줄을 확인하세요.",
        ],
        season_en=[
            "Core Yuzawa winter: Dec – Mar.",
            "Snow softer in the afternoon sun — morning edges are sharper.",
            "Lean years rely more on snowmaking on lower runs.",
        ],
        season_ko=[
            "유자와 핵심 시즌 12~3월.",
            "오후 양지에 눈이 물러지니 오전 에징이 좋습니다.",
            "눈이 적은 해에는 하부 인공설 비중이 커집니다.",
        ],
        access_en=[
            "Shinkansen to Echigo-Yuzawa + short bus / taxi.",
            "Same Tokyo access story as Gala Yuzawa.",
            "Walkable lodging near the station reduces logistics stress.",
        ],
        access_ko=[
            "에치고유자와 신칸센 + 짧은 버스·택시.",
            "갈라와 같은 도쿄 접근 패턴입니다.",
            "역세권 숙소면 동선이 단순해집니다.",
        ],
        stay_en=[
            "Yuzawa station hotels and onsen inns.",
            "Family rooms sell out on weekends.",
            "Dinner in town after easy ski days.",
        ],
        stay_ko=[
            "유자와역 호텔·온천여관.",
            "주말 패밀리룸이 빨리 마감됩니다.",
            "가벼운 스키일 뒤에는 시내 저녁이 편합니다.",
        ],
        tips_en=[
            "Pair Iwappara (easy) with Gala (convenient) across a weekend.",
            "Great confidence-building hill before tackling Naeba steeps.",
            "Watch ice on early January mornings.",
        ],
        tips_ko=[
            "주말에 이와파라(쉬운 코스)+갈라(접근)를 조합하세요.",
            "나에바 급사면 전에 자신감을 키우기 좋습니다.",
            "1월 초 아침 아이스에 주의하세요.",
        ],
    ),
    "yuzawa_kogen": entry(
        summary_en="Yuzawa Kogen — ropeway above town, compact slopes, and onsen-base convenience.",
        summary_ko="유자와 고원 — 시내 위 로프웨이·콤팩트 슬로프·온천 베이스.",
        name_en="Yuzawa Kogen",
        name_ko="유자와 고원",
        hook_en="**Yuzawa Kogen** sits above Echigo-Yuzawa via ropeway — a compact hill for travelers who want skiing + onsen town without long transfers. Think short sessions and village time, not all-day big-mountain touring.",
        hook_ko="**유자와 고원**은 로프웨이로 에치고유자와 시내 위에 연결된 콤팩트 스키장입니다. 장거리 산악 투어보다 짧은 스키+온천 마을 일정에 맞습니다.",
        slopes_en=[
            "Limited trail count — ideal for warm-ups or mixed sightseeing days.",
            "Beginner-friendly pitches near the plateau.",
            "Views down to Yuzawa valley on clear days.",
            "Not the choice if you need endless expert terrain.",
        ],
        slopes_ko=[
            "코스 수는 적어 워밍업·관광 병행일에 적합합니다.",
            "고원 근처 초급면이 무난합니다.",
            "맑은 날 유자와 계곡 전망이 좋습니다.",
            "끝없는 상급 지형을 원하면 카구라·나에바가 낫습니다.",
        ],
        season_en=[
            "Shorter effective season than high Kagura elevations.",
            "Best midwinter after fresh snow.",
            "Ropeway wind holds possible.",
        ],
        season_ko=[
            "고도 높은 카구라보다 유효 시즌이 짧을 수 있습니다.",
            "한겨울 신설 직후가 가장 좋습니다.",
            "로프웨이 강풍 운휴에 유의하세요.",
        ],
        access_en=[
            "Walk / short bus from Echigo-Yuzawa Station to ropeway base.",
            "Tokyo day trip feasible with early Shinkansen.",
            "Zero car needed for a ski + onsen day.",
        ],
        access_ko=[
            "에치고유자와역에서 로프웨이 승강장까지 도보·단거리 버스.",
            "이른 신칸센이면 도쿄 당일도 가능합니다.",
            "스키+온천 당일에 차는 필수는 아닙니다.",
        ],
        stay_en=[
            "Stay in Yuzawa onsen hotels steps from dinner streets.",
            "Luggage lockers at the station help day-trippers.",
            "Combine with Gala if you want more vertical next day.",
        ],
        stay_ko=[
            "저녁 거리가 가까운 유자와 온천 호텔에 묵으세요.",
            "당일권은 역 코인로커가 유용합니다.",
            "다음 날 낙차가 필요하면 갈라를 추가하세요.",
        ],
        tips_en=[
            "Use as an arrival-day stretch after the Shinkansen.",
            "Buy single-ride or half-day if full day is too much.",
            "Photograph the valley from the ropeway cabin.",
        ],
        tips_ko=[
            "신칸센 도착일 몸풀기 스키로 좋습니다.",
            "하루가 길면 반일권·回数권을 쓰세요.",
            "로프웨이에서 계곡 사진을 남기세요.",
        ],
    ),
    "joetsu_kokusai": entry(
        summary_en="Joetsu Kokusai — sprawling Niigata terrain for intermediates and busy holiday weeks.",
        summary_ko="조에쓰 국제 — 니가타 광역 지형·연휴 인기 리조트 가이드.",
        name_en="Joetsu Kokusai Ski Resort",
        name_ko="조에쓰 국제 스키장",
        hook_en="**Joetsu Kokusai** is a sprawling Niigata area popular with domestic skiers — lots of trail variety, multiple bases, and strong intermediate grazing. Expect holiday crowds and big parking lots.",
        hook_ko="**조에쓰 국제**는 국내 스키어에게 인기인 광역 니가타 리조트로, 코스 다양성과 중급 크루징이 강점입니다. 연휴에는 혼잡과 넓은 주차장이 일상이 됩니다.",
        slopes_en=[
            "Wide trail network for progressing intermediates.",
            "Some steeper pitches and tree edges after storms.",
            "Study which base / lift cluster matches your lodging.",
            "Weekend queues — midweek tickets shine.",
        ],
        slopes_ko=[
            "중급이 성장하기 좋은 넓은 코스망입니다.",
            "강설 후에는 급한 면과 트리 가장자리도 살아납니다.",
            "숙소와 맞는 베이스·리프트 클러스터를 확인하세요.",
            "주말 대기가 길어 주중권이 빛납니다.",
        ],
        season_en=[
            "Solid coverage in the Joetsu snow belt Dec – Mar.",
            "Heavy dump days can slow road access.",
            "Spring skiing possible on higher remaining trails.",
        ],
        season_ko=[
            "조에쓰 설상벨트에서 12~3월 커버가 안정적입니다.",
            "폭설일에는 도로 접근이 느려질 수 있습니다.",
            "봄에는 남은 상부 코스 위주로 즐기세요.",
        ],
        access_en=[
            "Train + bus combinations from Tokyo / Niigata corridors.",
            "Car preferred for flexible base switching.",
            "Allow buffer time after overnight snow.",
        ],
        access_ko=[
            "도쿄·니가타 축의 철도+버스 조합.",
            "베이스를 바꿔가려면 렌터카가 편합니다.",
            "밤새 눈 온 뒤에는 여유 시간을 두세요.",
        ],
        stay_en=[
            "Hotels and pensions near main gates.",
            "Onsen towns in Minamiuonuma for evenings.",
            "Package buses from Tokyo on peak weekends.",
        ],
        stay_ko=[
            "메인 게이트 근처 호텔·펜션.",
            "저녁은 미나미우오누마 온천권도 후보입니다.",
            "성수기 주말에는 도쿄발 패키지 버스가 있습니다.",
        ],
        tips_en=[
            "Pick lodging that matches the gate you will use most.",
            "If crowds peak, pivot to Maiko for softer tree snow.",
            "Download offline maps of the resort clusters.",
        ],
        tips_ko=[
            "가장 많이 쓸 게이트와 가까운 숙소를 고르세요.",
            "혼잡하면 마이코의 소프트 트리로 이동하세요.",
            "클러스터별 오프라인 맵을 준비하세요.",
        ],
    ),
    "maiko_snow_resort": entry(
        summary_en="Maiko Snow Resort — soft powder, tree skiing, and Niigata free-ride reputation.",
        summary_ko="마이코 — 소프트 파우더·트리 스키·니가타 프리라이드 명성.",
        name_en="Maiko Snow Resort",
        name_ko="마이코 스노우 리조트",
        hook_en="**Maiko** has a cult following for **soft powder and trees** in Niigata. Riders chase storm days here when they want freeride texture closer to Tokyo than Hokkaido.",
        hook_ko="**마이코**는 니가타의 **소프트 파우더·트리**로 마니아층이 두터운 스키장입니다. 홋카이도까지 가지 않고도 프리라이드 질감을 원할 때 강설일을 노립니다.",
        slopes_en=[
            "Tree skiing is the headline after fresh snow.",
            "Groomed runs for warm-ups and storm visibility.",
            "Advanced riders still obey ropes and closed signs.",
            "Compact enough for a focused powder day.",
        ],
        slopes_ko=[
            "신설 후 트리 스키가 최대 매력입니다.",
            "워밍업·악천후 시에는 정비면을 이용하세요.",
            "상급도 로프·폐쇄 표지를 지켜야 합니다.",
            "파우더 하루에 집중하기 좋은 규모입니다.",
        ],
        season_en=[
            "Storm track from the Sea of Japan is the lifeblood.",
            "Best weeks typically January–February.",
            "Foggy tree days require good goggle contrast lenses.",
        ],
        season_ko=[
            "동해 기압골 강설이 핵심입니다.",
            "1~2월이 가장 좋은 주간인 경우가 많습니다.",
            "안개 낀 트리에서는 콘트라스트 렌즈가 유리합니다.",
        ],
        access_en=[
            "Echigo-Yuzawa corridor + local bus / taxi / car.",
            "Same Shinkansen spine as other Yuzawa resorts.",
            "Early trains for first-chair powder.",
        ],
        access_ko=[
            "에치고유자와 축 + 로컬 버스·택시·렌터카.",
            "다른 유자와 스키장과 같은 신칸센 척추입니다.",
            "파우더 첫 리프트를 위해 이른 열차를 타세요.",
        ],
        stay_en=[
            "Yuzawa / Minamiuonuma lodging with morning transfers.",
            "Limited nightlife at the hill — town stays recommended.",
            "Dry rooms for soaked powder clothes.",
        ],
        stay_ko=[
            "유자와·미나미우오누마 숙소 + 오전 트랜스퍼.",
            "산 아래 밤문화는 적어 시내 숙소가 낫습니다.",
            "젖은 파우더복을 말릴 공간이 있는 방을 고르세요.",
        ],
        tips_en=[
            "Watch opening status after heavy dumps — delayed starts happen.",
            "If tracked out by noon, switch to Kagura vertical.",
            "Carry snacks; lunch lines spike on powder days.",
        ],
        tips_ko=[
            "폭설 다음날 오픈이 늦어질 수 있습니다.",
            "정오에 추적되면 카구라 낙차로 이동하세요.",
            "파우더 날은 점심 줄이 기니 간식을 챙기세요.",
        ],
    ),
    "ipponsugi": entry(
        summary_en="Ipponsugi Ski Resort — compact Yuzawa town hill for quick laps and beginners.",
        summary_ko="잇폰스기 — 유자와 시내권 콤팩트·초급 친화 스키장.",
        name_en="Ipponsugi Ski Resort",
        name_ko="잇폰스기 스키장",
        hook_en="**Ipponsugi** is a compact town-adjacent hill in Yuzawa for **quick laps**, beginners, and travelers stacking onsen + light skiing. Not a destination mega-resort — a convenient add-on.",
        hook_ko="**잇폰스기**는 유자와 시내에 가까운 콤팩트 스키장으로, **짧은 랩**·초급·온천+가벼운 스키 일정에 맞습니다. 대형 목적지 리조트라기보다 편리한 추가 옵션입니다.",
        slopes_en=[
            "Short vertical and friendly learning terrain.",
            "Easy to ski a few hours then return to town baths.",
            "Crowds possible on school trips — check calendars.",
            "Rentals available for travelers without gear.",
        ],
        slopes_ko=[
            "짧은 낙차와 초급 친화 지형입니다.",
            "몇 시간 타고 온천으로 돌아가기 좋습니다.",
            "수학여행 시즌에는 혼잡할 수 있습니다.",
            "장비가 없으면 렌탈로 해결할 수 있습니다.",
        ],
        season_en=[
            "Mainly midwinter reliable coverage.",
            "Lower elevation — spring melts earlier than Kagura.",
            "Artificial snow assists key lanes in thin winters.",
        ],
        season_ko=[
            "한겨울 커버가 비교적 안정적입니다.",
            "고도가 낮아 카구라보다 봄이 이릅니다.",
            "눈이 얇은 해에는 주요 레인에 인공설이 돕습니다.",
        ],
        access_en=[
            "Very close to Echigo-Yuzawa logistics.",
            "Taxi minutes from station lodging.",
            "Ideal first afternoon after Tokyo Shinkansen.",
        ],
        access_ko=[
            "에치고유자와 동선에서 매우 가깝습니다.",
            "역세권 숙소에서 택시 몇 분입니다.",
            "도쿄 신칸센 도착 당일 오후에 넣기 좋습니다.",
        ],
        stay_en=[
            "Any Yuzawa station / onsen hotel works.",
            "No need for ski-in lodging.",
            "Focus budget on better dinners in town.",
        ],
        stay_ko=[
            "유자와역·온천 호텔이면 충분합니다.",
            "스키인 숙소가 필수는 아닙니다.",
            "예산은 시내 저녁 식사에 쓰는 편이 낫습니다.",
        ],
        tips_en=[
            "Use for equipment shake-down before a Naeba day.",
            "Half-day tickets often enough.",
            "Combine with Yuzawa brewery / sake tasting evenings.",
        ],
        tips_ko=[
            "나에바 전날 장비 점검용으로 좋습니다.",
            "반일권으로도 충분한 경우가 많습니다.",
            "저녁에 유자와 사케·양조 체험을 묶으세요.",
        ],
    ),
    "zao_onsen": entry(
        summary_en="Zao Onsen Ski Resort — juhyo frost monsters, vast linked terrain, and legendary onsen town.",
        summary_ko="자오 온센 — 주효(수수께끼 나무)·광역 슬로프·온천마을 가이드.",
        name_en="Zao Onsen Ski Resort",
        name_ko="자오 온센 스키장",
        hook_en="**Zao Onsen** in Yamagata is a Tohoku icon — vast linked slopes, sulfur onsen streets, and winter **juhyo** (ice monster) rimed trees on the upper mountain. A complete ski + culture destination.",
        hook_ko="야마가타 **자오 온센**은 광역 연결 슬로프, 유황 온천 거리, 정상부의 **주효(얼음 나무)**로 유명한 도호쿠 대표 스키장입니다. 스키와 온천 문화를 한 번에 담기 좋습니다.",
        slopes_en=[
            "Huge trail network from beginner bowls to advanced pitches.",
            "Upper mountain is the juhyo zone — weather windows matter.",
            "Ropeways and many lifts connect the system — grab a full-area map.",
            "Night skiing and floodlit events appear on select dates.",
        ],
        slopes_ko=[
            "초급 볼부터 상급 급사면까지 코스망이 넓습니다.",
            "정상부 주효 존은 날씨 창이 중요합니다.",
            "로프웨이·다수 리프트로 연결되니 전체 맵을 챙기세요.",
            "야간 스키·야간 이벤트가 일정에 따라 있습니다.",
        ],
        season_en=[
            "Juhyo peak often midwinter when rime builds.",
            "Season roughly Dec – Mar/Apr depending on elevation.",
            "Storm + freeze cycles create unique frost scenery.",
        ],
        season_ko=[
            "주효는 한겨울 상고가 쌓일 때가 피크입니다.",
            "시즌은 고도에 따라 12~3/4월.",
            "강설 후 동결이 독특한 설경을 만듭니다.",
        ],
        access_en=[
            "Fly into Yamagata / Sendai then bus or car to Zao Onsen.",
            "From Tokyo: Yamagata Shinkansen + bus links.",
            "Winter tires essential on the mountain road.",
        ],
        access_ko=[
            "야마가타·센다이 공항 후 버스·렌터카.",
            "도쿄에서는 야마가타 신칸센 + 버스.",
            "산악 도로는 윈터타이어가 필수입니다.",
        ],
        stay_en=[
            "Stay in Zao Onsen town for soak-after-ski magic.",
            "Sulfur baths stain silver — leave jewelry off.",
            "Book early for juhyo photography weeks.",
        ],
        stay_ko=[
            "스키 후 바로 탕에 들어가려면 온천 마을 숙소가 최고입니다.",
            "유황탕은 은제품을 변색시키니 장신구를 빼세요.",
            "주효 포토 시즌은 숙소가 빨리 찹니다.",
        ],
        tips_en=[
            "Reserve a weather window morning for the juhyo ride.",
            "Pair JPFun Stay pins walking distance to public baths.",
            "Bring a buff — sulfur steam + cold wind is harsh on skin.",
        ],
        tips_ko=[
            "주효 관람은 날씨 좋은 오전을 예약하세요.",
            "공동탕 도보권 Stay 핀을 고르면 편합니다.",
            "유황 수증기+한풍에 목이 마르니 버프를 챙기세요.",
        ],
    ),
    "appi_kogen": entry(
        summary_en="Appi Kogen — high-elevation Iwate resort, long season vibe, and full-service hotels.",
        summary_ko="앗피 고원 — 이와테 고산 리조트·긴 시즌·풀서비스 호텔.",
        name_en="Appi Kogen Ski Resort",
        name_ko="앗피 고원 스키장",
        hook_en="**Appi Kogen** in Iwate is a high-elevation Tohoku resort with long cruisers, reliable midwinter snow, and large hotels. It feels like a destination campus rather than a village alley ski scene.",
        hook_ko="이와테 **앗피 고원**은 고도가 높은 도호쿠 리조트로, 긴 크루저·한겨울 적설·대형 호텔이 특징입니다. 골목형 스키 마을보다 리조트 캠퍼스 분위기에 가깝습니다.",
        slopes_en=[
            "Intermediate highways and panoramic upper ridges.",
            "Good progression terrain for advancing beginners.",
            "Wind can affect summit lifts — check the board.",
            "Snow quality often better preserved than lower Pacific-side hills.",
        ],
        slopes_ko=[
            "중급 하이웨이와 조망 좋은 상부 능선이 있습니다.",
            "초급에서 중급으로 올라가는 팀에 적합합니다.",
            "정상 리프트는 강풍 영향을 받으니 게시판을 확인하세요.",
            "태평양 측 저고도보다 설질이 오래가는 편입니다.",
        ],
        season_en=[
            "Solid Dec – Mar; elevation helps late-season leftovers.",
            "Cold snaps bring excellent groomer carve days.",
            "Holiday weeks bring domestic tour buses.",
        ],
        season_ko=[
            "12~3월이 핵심이고 고도 덕분에 시즌 말도 남습니다.",
            "한파 때는 정비면 카빙이 훌륭합니다.",
            "연휴에는 국내 투어버스가 늘어납니다.",
        ],
        access_en=[
            "Morioka Shinkansen access + bus / car to Appi.",
            "From Tokyo: Tohoku Shinkansen to Morioka, then transfer.",
            "Allow time for winter road conditions.",
        ],
        access_ko=[
            "모리오카 신칸센 + 버스·차로 앗피 이동.",
            "도쿄→도호쿠 신칸센 모리오카 환승.",
            "겨울 도로 상황을 고려해 여유를 두세요.",
        ],
        stay_en=[
            "Appi hotels and condominiums on campus.",
            "Half-board packages simplify dinner logistics.",
            "Evenings are quieter — bring entertainment for kids.",
        ],
        stay_ko=[
            "캠퍼스 안 호텔·콘도가 기본입니다.",
            "반연금이 저녁을 단순하게 만듭니다.",
            "밤은 조용하니 아이 오락거리를 챙기세요.",
        ],
        tips_en=[
            "Strong pick when Zao is fully booked.",
            "Clear days = ridge photo laps; storm days = lower trees / groomers.",
            "Confirm which lifts run for your ticket type.",
        ],
        tips_ko=[
            "자오가 만실일 때 좋은 대안입니다.",
            "맑은 날은 능선, 강설일은 하부 트리·정비면.",
            "티켓 종류별 탑승 가능 리프트를 확인하세요.",
        ],
    ),
    "geto_kogen": entry(
        summary_en="Geto Kogen — quiet Iwate powder trees and low-key mountain lodging.",
        summary_ko="게토 고원 — 이와테의 한산한 파우더 트리·로지 숙박.",
        name_en="Geto Kogen Ski Resort",
        name_ko="게토 고원 스키장",
        hook_en="**Geto Kogen** is a quieter Iwate powder mountain with tree skiing and a low-key base. Ideal for riders who find Appi or Zao too busy and want soft snow without spectacle crowds.",
        hook_ko="**게토 고원**은 이와테의 조용한 파우더·트리 스키장입니다. 앗피·자오의 혼잡을 피하고 소프트 스노에 집중하고 싶을 때 좋습니다.",
        slopes_en=[
            "Tree pockets after storms are the main attraction.",
            "Groomers for visibility days and warm-ups.",
            "Smaller lift fleet — learn the map quickly.",
            "Advanced freeride still stays in open, approved zones.",
        ],
        slopes_ko=[
            "강설 후 트리 포켓이 핵심 매력입니다.",
            "시야가 나쁜 날·워밍업은 정비면.",
            "리프트가 많지 않아 맵을 빨리 익힐 수 있습니다.",
            "프리라이드도 개방·허가 구역만 이용하세요.",
        ],
        season_en=[
            "Midwinter dumps from northern systems.",
            "Season compact: focus Dec – Mar.",
            "Weekdays can feel almost private.",
        ],
        season_ko=[
            "북쪽에서 내려오는 한겨울 강설을 노리세요.",
            "시즌은 12~3월에 집중됩니다.",
            "주중은 거의 전세 느낌이 납니다.",
        ],
        access_en=[
            "Kitakami / Morioka rail corridor + car or taxi.",
            "Public transport sparse — lodging transfers matter.",
            "Pair with Appi using a rental car week.",
        ],
        access_ko=[
            "기타카미·모리오카 철도축 + 차·택시.",
            "대중교통이 적어 숙소 트랜스퍼가 중요합니다.",
            "렌터카 일주일에 앗피와 함께 돌기 좋습니다.",
        ],
        stay_en=[
            "Mountain pensions and small hotels.",
            "Quiet nights — plan meals ahead.",
            "Drying rooms essential after tree days.",
        ],
        stay_ko=[
            "산악 펜션·소규모 호텔.",
            "밤이 조용해 식사를 미리 계획하세요.",
            "트리데이 후에는 건조실이 필수입니다.",
        ],
        tips_en=[
            "Check opening status after big snow — delayed starts happen.",
            "Bring high-contrast lenses for flat light in trees.",
            "Great contrast day after a busy Zao visit.",
        ],
        tips_ko=[
            "폭설 후 오픈 지연을 확인하세요.",
            "트리 플랫라이트용 고대비 렌즈를 챙기세요.",
            "붐비는 자오 다음 날 대비 일정으로 좋습니다.",
        ],
    ),
    "alts_bandai": entry(
        summary_en="Alts Bandai — big Fukushima family terrain near Bandai-Azuma landscape.",
        summary_ko="알츠 반다이 — 반다이·아즈마 경관의 대형 패밀리 스키장.",
        name_en="Alts Bandai",
        name_ko="알츠 반다이",
        hook_en="**Alts Bandai** is a large Fukushima resort near the Bandai landscape with terrain for all levels and a strong family reputation. Often combined with Urabandai sightseeing.",
        hook_ko="**알츠 반다이**는 반다이 산세 근처의 대형 후쿠시마 리조트로, 전 레벨 코스와 패밀리 친화성이 강점입니다. 우라반다이 관광과 함께 묶는 경우가 많습니다.",
        slopes_en=[
            "Generous intermediate network and learning areas.",
            "Enough variety for multi-day stays without boredom.",
            "Views toward Bandai on clear days.",
            "Park / family events appear through the season.",
        ],
        slopes_ko=[
            "중급·초급 코스가 넉넉합니다.",
            "다일치에도 질리지 않을 다양성이 있습니다.",
            "맑은 날 반다이 전망이 좋습니다.",
            "시즌 중 파크·패밀리 이벤트가 열립니다.",
        ],
        season_en=[
            "Pacific-side snow can be variable — watch forecasts.",
            "Best windows after cold systems midwinter.",
            "Season roughly Dec – Mar.",
        ],
        season_ko=[
            "태평양 측이라 적설이 가변적 — 예보를 보세요.",
            "한겨울 한기 유입 직후가 좋습니다.",
            "시즌 대략 12~3월.",
        ],
        access_en=[
            "Koriyama / Inawashiro access then bus or car.",
            "Tokyo: Tohoku Shinkansen + local transfer.",
            "Car preferred for Bandai sightseeing loop.",
        ],
        access_ko=[
            "고리야마·이나와시로 접근 후 버스·렌터카.",
            "도쿄→도호쿠 신칸센 + 로컬 환승.",
            "반다이 관광 루프에는 렌터카가 편합니다.",
        ],
        stay_en=[
            "Resort hotels and Urabandai pensions.",
            "Onsen stays around Bandai for nights.",
            "Family rooms book out on Japanese holidays.",
        ],
        stay_ko=[
            "리조트 호텔·우라반다이 펜션.",
            "밤은 반다이권 온천 숙소도 좋습니다.",
            "일본 연휴에 패밀리룸이 마감됩니다.",
        ],
        tips_en=[
            "Pair ski mornings with Goshikinuma pond walks on clear afternoons.",
            "If snow is thin, prioritize higher lifts.",
            "Check which Nekoma / neighboring areas are open if holding combo tickets.",
        ],
        tips_ko=[
            "맑은 오후에는 고시키누마 산책과 조합하세요.",
            "눈이 얇으면 상부 리프트를 우선하세요.",
            "연결권이 있다면 네코마 등 인접 오픈 현황을 확인하세요.",
        ],
    ),
    "takasu_snow_park": entry(
        summary_en="Takasu Snow Park — Gujo powder linked with Dynaland, long vertical days.",
        summary_ko="다카스 스노우파크 — 구조 파우더·다이나랜드 연결·긴 낙차.",
        name_en="Takasu Snow Park",
        name_ko="다카스 스노우파크",
        hook_en="**Takasu Snow Park** in Gujo, Gifu is a powder-leaning hill often linked with neighboring **Dynaland**. Central Japan skiers chase sea-effect bursts here when Hokuriku storms align.",
        hook_ko="기후 구조의 **다카스 스노우파크**는 이웃 **다이나랜드**와 연결되는 파우더형 스키장입니다. 호쿠리쿠 기압골이 맞으면 주부지방에서도 좋은 눈을 노릴 수 있습니다.",
        slopes_en=[
            "Longer vertical and steeper options than Dynaland.",
            "Combined tickets unlock a full-day circuit.",
            "Powder stashes after Hokuriku moisture events.",
            "Beginners may prefer starting on Dynaland faces.",
        ],
        slopes_ko=[
            "다이나랜드보다 낙차·급사면 옵션이 큽니다.",
            "연결권으로 하루 종일 순환 가능합니다.",
            "호쿠리쿠 습설 이벤트 후 파우더 스태시가 생깁니다.",
            "초보는 다이나랜드 면에서 시작하는 편이 낫습니다.",
        ],
        season_en=[
            "Core winter Dec – Mar.",
            "Storm timing matters more than at lake-effect giants.",
            "Freeze-thaw possible — morning hardpack is common.",
        ],
        season_ko=[
            "핵심 시즌 12~3월.",
            "홋카이도만큼 매일이 파우더는 아니니 강설 타이밍이 중요합니다.",
            "동결·해빙으로 오전 하드팩이 흔합니다.",
        ],
        access_en=[
            "Drive from Nagoya / Gifu (~2 h class depending on roads).",
            "Gujo buses limited in winter — car strongly preferred.",
            "Tokyo access is long — better as Chubu-based trip.",
        ],
        access_ko=[
            "나고야·기후에서 차로 약 2시간대(도로 상황 따름).",
            "겨울 버스가 적어 렌터카를 권장합니다.",
            "도쿄에서는 멀어 주부 거점 여행이 낫습니다.",
        ],
        stay_en=[
            "Gujo hotels or Takasu / Dynaland lodging packages.",
            "Onsen stops in Gujo Hachiman area on rest days.",
            "Fuel up dinners in town — mountain dining is limited.",
        ],
        stay_ko=[
            "구조 호텔 또는 다카스·다이나랜드 패키지 숙소.",
            "쉬는 날 구조하치만 온천을 이용하세요.",
            "산 식당이 한정적이라 시내에서 저녁을 해결하세요.",
        ],
        tips_en=[
            "Buy Takasu + Dynaland combo whenever possible.",
            "Start Takasu morning powder, finish Dynaland family runs.",
            "Watch expressway closures after heavy snow.",
        ],
        tips_ko=[
            "가능하면 다카스+다이나랜드 연결권을 사세요.",
            "오전 다카스 파우더 → 오후 다이나랜드 패밀리 코스가 무난합니다.",
            "폭설 후 고속도로 통제를 확인하세요.",
        ],
    ),
    "dynaland": entry(
        summary_en="Dynaland — family Gujo skiing linked to Takasu with gentler terrain.",
        summary_ko="다이나랜드 — 다카스 연결 구조의 패밀리·완만 지형.",
        name_en="Dynaland",
        name_ko="다이나랜드",
        hook_en="**Dynaland** is the family-facing neighbor of Takasu Snow Park — gentler trails, learning zones, and shared ticket opportunities. Perfect when the group mixes kids and powder hunters.",
        hook_ko="**다이나랜드**는 다카스와 이웃한 패밀리형 스키장으로, 완만한 코스·학습존·연결권이 강점입니다. 아이와 파우더 헌터가 섞인 팀에 적합합니다.",
        slopes_en=[
            "Beginner / intermediate focus with friendly fall lines.",
            "Link to Takasu for more advanced afternoon laps.",
            "Park features depending on seasonal build.",
            "Crowds rise on Tokai region weekends.",
        ],
        slopes_ko=[
            "초·중급 중심의 다루기 쉬운 폴라인입니다.",
            "오후에는 다카스로 넘어가 상급 랩을 추가하세요.",
            "시즌에 따라 파크가 세워집니다.",
            "도카이권 주말에 혼잡해집니다.",
        ],
        season_en=[
            "Same weather window as Takasu.",
            "Artificial snow supports key beginner lanes.",
            "Best days after regional cold rain turns to snow.",
        ],
        season_ko=[
            "다카스와 같은 기상 창을 공유합니다.",
            "초급 레인은 인공설이 돕습니다.",
            "지역 한기 유입으로 비에서 눈으로 바뀔 때가 좋습니다.",
        ],
        access_en=[
            "Same Gujo / Nagoya driving corridor as Takasu.",
            "Shared parking and shuttle patterns with neighbor resort.",
            "Avoid late Sunday returns to Nagoya — traffic spikes.",
        ],
        access_ko=[
            "다카스와 같은 구조·나고야 도로축입니다.",
            "이웃 스키장과 주차·셔틀을 공유하는 경우가 많습니다.",
            "일요일 저녁 나고야 귀경 정체를 피하세요.",
        ],
        stay_en=[
            "Family rooms near Dynaland base.",
            "Gujo town stays for restaurants.",
            "Package deals often span both mountains.",
        ],
        stay_ko=[
            "다이나랜드 베이스 패밀리룸.",
            "식당은 구조 시내 숙소가 유리합니다.",
            "패키지가 두 산을 묶는 경우가 많습니다.",
        ],
        tips_en=[
            "Let advanced riders roam Takasu while kids take Dynaland lessons.",
            "Meet at a known plaza before last lifts.",
            "JPFun Stay pins help if mountain hotels are full.",
        ],
        tips_ko=[
            "상급은 다카스, 아이는 다이나랜드 강습으로 분할하세요.",
            "마지막 리프트 전 약속된 플라자에서 집합하세요.",
            "산 호텔이 만실이면 Stay 핀을 활용하세요.",
        ],
    ),
    "hirayu_onsen": entry(
        summary_en="Hirayu Onsen Ski Area — tiny Okuhida hill with big onsen village energy.",
        summary_ko="히라유 온센 — 작은 오쿠히다 스키장과 큰 온천마을.",
        name_en="Hirayu Onsen Ski Area",
        name_ko="히라유 온센 스키장",
        hook_en="**Hirayu Onsen Ski Area** is a compact Okuhida hill attached to a famous onsen village near Takayama / Kamikochi gateways. Ski a few hours, soak all evening — that's the product.",
        hook_ko="**히라유 온센 스키장**은 다카야마·가미코치 관문 근처 오쿠히다의 작은 스키장입니다. 몇 시간 타고 저녁 내내 온천 — 그 조합이 상품입니다.",
        slopes_en=[
            "Very limited trail count — beginners and casual skiers.",
            "Scenic backdrop more than big-mountain challenge.",
            "Ideal weather-backup activity on a Takayama trip.",
            "Rentals suited to travelers without bags of gear.",
        ],
        slopes_ko=[
            "코스가 적어 초급·캐주얼 스키에 맞습니다.",
            "도전보다 경관·온천이 중심입니다.",
            "다카야마 여행의 날씨 백업 액티비티로 좋습니다.",
            "장비가 없는 여행객용 렌탈이 갖춰져 있습니다.",
        ],
        season_en=[
            "Short mountain season — confirm opening before detouring.",
            "Heavy snow can isolate village roads briefly.",
            "Best as midwinter add-on, not a week-long ski base.",
        ],
        season_ko=[
            "시즌이 짧아 우회 전 오픈을 확인하세요.",
            "폭설 시 마을 도로가 잠시 끊길 수 있습니다.",
            "일주일 스키 베이스보다 한겨울 추가 일정에 적합합니다.",
        ],
        access_en=[
            "From Takayama by bus toward Hirayu (~1 h).",
            "Gateway buses toward Kamikochi in other seasons.",
            "Car chains may be required after storms.",
        ],
        access_ko=[
            "다카야마에서 히라유행 버스 약 1시간.",
            "다른 계절에는 가미코치 방면 버스와 관문을 공유합니다.",
            "강설 후 체인이 필요할 수 있습니다.",
        ],
        stay_en=[
            "Ryokan with indoor / outdoor baths are the point.",
            "Kaiseki dinners beat mountain cafeterias.",
            "Book early for weekend onsen demand.",
        ],
        stay_ko=[
            "내탕·노천탕 있는 료칸이 핵심입니다.",
            "산 식당보다 카이세키 저녁이 낫습니다.",
            "주말 온천 수요로 조기 예약하세요.",
        ],
        tips_en=[
            "Do not plan expert powder objectives here.",
            "Use as a scenic / soak day inside a Gifu loop.",
            "Photograph morning steam streets before ski.",
        ],
        tips_ko=[
            "상급 파우더 목적지로 잡지 마세요.",
            "기후 루프 안의 경관·온천 데이로 쓰세요.",
            "스키 전 아침 수증기 골목을 사진에 담으세요.",
        ],
    ),
    "washigatake": entry(
        summary_en="Washigatake Ski Resort — Gujo local hill with night skiing and family day trips.",
        summary_ko="와시가타케 — 구조 로컬·야간 스키·패밀리 당일 코스.",
        name_en="Washigatake Ski Resort",
        name_ko="와시가타케 스키장",
        hook_en="**Washigatake** is a Gujo local favorite with approachable terrain and frequent **night skiing**. Think Tokai-region day trip more than destination powder camp.",
        hook_ko="**와시가타케**는 접근성 좋은 코스와 **야간 스키**로 인기인 구조 로컬 스키장입니다. 목적지형 파우더 캠프보다 도카이권 당일·1박에 가깝습니다.",
        slopes_en=[
            "Family / intermediate trails and learning areas.",
            "Night sessions extend short winter evenings.",
            "Smaller than Takasu — quick to navigate.",
            "Local race / school use can occupy some lanes.",
        ],
        slopes_ko=[
            "패밀리·중급·학습 코스가 중심입니다.",
            "야간 스키로 짧은 겨울 저녁을 늘립니다.",
            "다카스보다 작아 맵 파악이 빠릅니다.",
            "로컬 레이스·학교 사용으로 일부 레인이 막힐 수 있습니다.",
        ],
        season_en=[
            "Dec – Mar core for Gujo hills.",
            "Artificial snow helps early / late season.",
            "Best after regional cold snaps.",
        ],
        season_ko=[
            "구조권 핵심 시즌 12~3월.",
            "시즌 초·말은 인공설이 돕습니다.",
            "지역 한기 유입 직후가 좋습니다.",
        ],
        access_en=[
            "Drive from Nagoya metro area.",
            "Compare travel time vs Takasu for your hotel.",
            "Parking easier on weeknights for night ski.",
        ],
        access_ko=[
            "나고야권에서 차로 접근합니다.",
            "숙소 기준으로 다카스와 이동 시간을 비교하세요.",
            "야간 스키는 평일 저녁 주차가 여유롭습니다.",
        ],
        stay_en=[
            "Gujo city hotels or nearby business stays.",
            "Onsen side trips to Gujo Hachiman.",
            "Night-ski packages with lift + lodging deals.",
        ],
        stay_ko=[
            "구조시 호텔·비즈니스 숙소.",
            "구조하치만 온천을 곁들이세요.",
            "야간권+숙박 패키지도 찾아보세요.",
        ],
        tips_en=[
            "Great evening activity if daytime was sightseeing.",
            "Lights can create flat visual patches — slow down.",
            "If you want powder trees, prioritize Takasu storm days instead.",
        ],
        tips_ko=[
            "낮에 관광했다면 저녁 액티비티로 좋습니다.",
            "조명 아래 플랫 구간이 있으니 속도를 줄이세요.",
            "파우더 트리가 목표면 다카스 강설일을 우선하세요.",
        ],
    ),
    "kusatsu_kokusai": entry(
        summary_en="Kusatsu Onsen Ski Area — sulfur town skiing above Japan's famous yubatake.",
        summary_ko="구사쓰 온센 — 유바타케 위 유황 온천마을의 스키.",
        name_en="Kusatsu Onsen Ski Area",
        name_ko="구사쓰 온센 스키장",
        hook_en="**Kusatsu Onsen Ski Area** sits above one of Japan's most famous hot-spring towns. The skiing is compact; the **yubatake** steam plaza and bath culture are the headline after your runs.",
        hook_ko="**구사쓰 온센 스키장**은 일본 최고 인기 온천마을 위에 있습니다. 스키 규모는 콤팩트하고, **유바타케** 수증기 광장과 온천 문화가 핵심입니다.",
        slopes_en=[
            "Beginner / intermediate focus suitable for casual ski days.",
            "Quick sessions before returning to town baths.",
            "Crowds rise with tourism peaks, not just powder days.",
            "Not a freeride destination.",
        ],
        slopes_ko=[
            "캐주얼한 초·중급 중심입니다.",
            "짧게 타고 마을 온천으로 내려오기 좋습니다.",
            "파우더뿐 아니라 관광 성수기에도 붐빕니다.",
            "프리라이드 목적지는 아닙니다.",
        ],
        season_en=[
            "Midwinter coverage; confirm opening each season.",
            "Town altitude helps snow vs Kanto plains.",
            "Icy mornings after clear nights.",
        ],
        season_ko=[
            "한겨울 커버, 매 시즌 오픈을 확인하세요.",
            "마을 고도가 간토 평야보다 눈을 돕습니다.",
            "맑은 밤 다음 아침은 아이스가 생깁니다.",
        ],
        access_en=[
            "From Tokyo: limited express / bus combinations to Kusatsu.",
            "Car via Expressway + mountain roads.",
            "Luggage forwarding to ryokan simplifies transfers.",
        ],
        access_ko=[
            "도쿄에서 특급·버스 조합으로 구사쓰 진입.",
            "고속도로+산악도로 렌터카도 가능합니다.",
            "료칸으로 짐 배송하면 환승이 편합니다.",
        ],
        stay_en=[
            "Kusatsu ryokan with jumbo bath halls.",
            "Walk the yubatake at night for atmosphere.",
            "Book rooms that include bath tax / towels clarity.",
        ],
        stay_ko=[
            "대형 욕장이 있는 구사쓰 료칸.",
            "밤에 유바타케를 걸어보세요.",
            "입욕세·수건 포함 여부를 확인하세요.",
        ],
        tips_en=[
            "Ski light, bathe heavy — reverse of Niseko priorities.",
            "Sulfur smell is normal; leave silver jewelry off.",
            "Pair with Manza if you want higher elevation snow next day.",
        ],
        tips_ko=[
            "스키는 가볍게, 온천은 진하게 — 니세코와 우선순위가 반대입니다.",
            "유황 냄새는 정상, 은장신구는 빼세요.",
            "다음 날 고도가 필요하면 만자와 조합하세요.",
        ],
    ),
    "manza_onsen": entry(
        summary_en="Manza Onsen Ski Resort — high Gunma elevation, Prince lodging, and storm snow.",
        summary_ko="만자 온센 — 군마 고산·프린스 숙소·강설 가이드.",
        name_en="Manza Onsen Ski Resort",
        name_ko="만자 온센 스키장",
        hook_en="**Manza Onsen** sits at high elevation in Gunma with Prince Hotel infrastructure and a reputation for cold, stormy snow. Stronger snowfield energy than Kusatsu's town hill.",
        hook_ko="**만자 온센**은 군마 고지대의 프린스 호텔형 리조트로, 춥고 거친 강설 이미지가 있습니다. 구사쓰 마을 스키장보다 설산 에너지가 강합니다.",
        slopes_en=[
            "Intermediate and advanced pitches with alpine feel.",
            "Wind and flat light common — goggle choice matters.",
            "Learning areas exist but weather is less forgiving.",
            "Ski-in convenience from Prince complex.",
        ],
        slopes_ko=[
            "알파인 감성의 중·상급면이 있습니다.",
            "바람·플랫라이트가 잦아 고글 선택이 중요합니다.",
            "초급면도 있으나 날씨가 덜 관대합니다.",
            "프린스 단지에서 스키인이 편합니다.",
        ],
        season_en=[
            "Higher elevation preserves snow later than many Kanto hills.",
            "Peak storms midwinter.",
            "Road access can pause after severe weather.",
        ],
        season_ko=[
            "고도가 높아 간토 많은 스키장보다 눈이 오래갑니다.",
            "한겨울 폭풍이 피크입니다.",
            "기상 악화 후 도로가 잠시 통제될 수 있습니다.",
        ],
        access_en=[
            "Car or package bus via Kusatsu / Tsumagoi roads.",
            "Winter driving skills required.",
            "Tokyo overnight buses appear on peak weekends.",
        ],
        access_ko=[
            "구사쓰·쓰마고이 도로축 렌터카 또는 패키지 버스.",
            "겨울 운전 실력이 필요합니다.",
            "성수기 주말 도쿄발 야간버스가 있습니다.",
        ],
        stay_en=[
            "Prince hotels and Manza onsen lodgings.",
            "Sulfur baths after cold ridge days.",
            "Half-board recommended — dining options thin outside hotels.",
        ],
        stay_ko=[
            "프린스 호텔·만자 온천 숙소.",
            "차가운 능선일 후 유황탕이 좋습니다.",
            "호텔 밖 식당이 적어 반연금을 권합니다.",
        ],
        tips_en=[
            "Check road cams before ascending.",
            "If winds shut ridges, ski lower protected runs.",
            "Combine with Kusatsu baths on a recovery evening.",
        ],
        tips_ko=[
            "오르기 전 도로 카메라를 확인하세요.",
            "강풍으로 능선이 닫히면 하부 보호 코스를 타세요.",
            "회복 저녁에는 구사쓰 온천과 조합하세요.",
        ],
    ),
    "kawaba": entry(
        summary_en="Kawaba Ski Resort — Gunma powder trees popular with Tokyo day warriors.",
        summary_ko="카와바 — 도쿄 데이 워리어에게 인기인 군마 파우더 트리.",
        name_en="Kawaba Ski Resort",
        name_ko="카와바 스키장",
        hook_en="**Kawaba** is a Gunma powder/tree favorite for Tokyo-based skiers chasing storm days without flying north. Expect early alarms, packed parking, and soft snow when the forecast hits.",
        hook_ko="**카와바**는 비행기 없이 강설을 노리는 도쿄권 스키어에게 인기인 군마 파우더·트리 스키장입니다. 이른 출발, 가득 찬 주차, 예보가 맞으면 소프트 스노가 보상입니다.",
        slopes_en=[
            "Tree skiing after dumps is the signature.",
            "Groomers for visibility and warm-ups.",
            "Progressive intermediates can level up quickly here.",
            "Respect closed forests — fines and safety risk.",
        ],
        slopes_ko=[
            "적설 후 트리 스키가 시그니처입니다.",
            "시야·워밍업은 정비면.",
            "중급이 빠르게 성장하기 좋은 지형입니다.",
            "폐쇄 숲 진입은 안전·벌금 위험이 있습니다.",
        ],
        season_en=[
            "Focus on midwinter storm cycles.",
            "Coverage variable early/late season.",
            "Weekday powder feels secret; weekends do not.",
        ],
        season_ko=[
            "한겨울 강설 사이클에 집중하세요.",
            "시즌 초·말은 커버가 가변적입니다.",
            "주중 파우더는 한산, 주말은 다릅니다.",
        ],
        access_en=[
            "Drive from Tokyo metro (~2.5–3.5 h depending on traffic).",
            "Leave before dawn on powder alerts.",
            "Bus tours exist on peak weekends.",
        ],
        access_ko=[
            "도쿄권에서 차로 약 2.5~3.5시간(정체 따름).",
            "파우더 경보 날은 새벽 출발이 기본입니다.",
            "성수기 주말 버스 투어도 있습니다.",
        ],
        stay_en=[
            "Local pensions or Numata area hotels.",
            "Many treat it as a day trip from Tokyo.",
            "If staying, dry gear for a second morning.",
        ],
        stay_ko=[
            "로컬 펜션 또는 누마타권 호텔.",
            "도쿄 당일 코스로 오는 사람도 많습니다.",
            "숙박하면 다음날 아침을 위해 장비를 말리세요.",
        ],
        tips_en=[
            "Refresh apps for opening delays after big snow.",
            "Bring cash / IC cards for rural tolls and meals.",
            "If tracked out, look at Minakami area alternatives.",
        ],
        tips_ko=[
            "폭설 후 오픈 지연 앱을 새로고침하세요.",
            "지방 톨게이트·식사를 위해 현금·교통카드를 챙기세요.",
            "추적되면 미나카미권 대안으로 이동하세요.",
        ],
    ),
    "minakami_hotaka": entry(
        summary_en="Minakami Hotaka — Tokyo-access Gunma skiing with river-valley lodging options.",
        summary_ko="미나카미 호타카 — 도쿄 접근형 군마 스키·계곡 숙소.",
        name_en="Minakami Hotaka Ski Resort",
        name_ko="미나카미 호타카 스키장",
        hook_en="**Minakami Hotaka** offers Tokyo-accessible Gunma skiing with lodging options along the Tone river valley. A practical multi-day base when you want more space than a pure day trip.",
        hook_ko="**미나카미 호타카**는 도쿄에서 접근하기 쉬운 군마 스키장으로, 토네강 계곡 숙소와 함께 다일치 베이스로 쓰기 좋습니다.",
        slopes_en=[
            "Varied intermediate terrain with some steeper shots.",
            "Family zones near main bases.",
            "Other Minakami hills nearby for variety.",
            "Weekend queues from Kanto day visitors.",
        ],
        slopes_ko=[
            "중급 중심 + 일부 급한 코스.",
            "메인 베이스 근처에 패밀리존.",
            "미나카미권 다른 스키장과 번갈아 타기 좋습니다.",
            "간토 당일 손님으로 주말 대기가 생깁니다.",
        ],
        season_en=[
            "Dec – Mar typical.",
            "Snow can be wetter than Tohoku interiors.",
            "Best after colder systems.",
        ],
        season_ko=[
            "통상 12~3월.",
            "도호쿠 내륙보다 습설인 날이 있습니다.",
            "더 추운 기압골 직후가 좋습니다.",
        ],
        access_en=[
            "Joetsu Shinkansen / rail to Minakami area + bus / taxi.",
            "Car via Kanetsu Expressway.",
            "Good balance of access vs Kawaba remoteness.",
        ],
        access_ko=[
            "조에쓰 신칸센·철도로 미나카미권 + 버스·택시.",
            "가네쓰 고속도로 렌터카.",
            "카와바보다 접근이 조금 더 수월한 편입니다.",
        ],
        stay_en=[
            "Riverside onsen hotels and pensions in Minakami.",
            "Rafting town energy in other seasons — winter is quieter.",
            "Book rooms with gear storage.",
        ],
        stay_ko=[
            "미나카미 강변 온천 호텔·펜션.",
            "다른 계절 래프팅 타운 분위기는 겨울에 한산해집니다.",
            "장비 보관 공간을 확인하세요.",
        ],
        tips_en=[
            "Build a Minakami sampler across nearby hills if staying 3 nights.",
            "Soaking after ski is half the point here.",
            "Watch expressway exits after storms.",
        ],
        tips_ko=[
            "3박이면 인근 스키장을 번갈아 타세요.",
            "스키 후 온천이 절반의 목적입니다.",
            "폭설 후 고속도로 하차를 주의하세요.",
        ],
    ),
    "hunter_mountain_shiobara": entry(
        summary_en="Hunter Mountain Shiobara — big Tochigi resort with parks and family terrain.",
        summary_ko="헌터마운틴 시오바라 — 도치기 대형 리조트·파크·패밀리.",
        name_en="Hunter Mountain Shiobara",
        name_ko="헌터마운틴 시오바라",
        hook_en="**Hunter Mountain Shiobara** is Tochigi's big-name resort — parks, family slopes, and events packed into a full-service hill near Nasushiobara. A Kanto staple for lessons and group trips.",
        hook_ko="**헌터마운틴 시오바라**는 도치기를 대표하는 대형 리조트로, 파크·패밀리 코스·이벤트가 갖춰진 풀서비스 스키장입니다. 강습·단체에 강한 간토 스테플입니다.",
        slopes_en=[
            "Wide beginner acreage and intermediate cruisers.",
            "Park crews build features through the season.",
            "Enough lifts to spread crowds midweek.",
            "Advanced terrain exists but powder trees are not the main brand.",
        ],
        slopes_ko=[
            "넓은 초급면과 중급 크루저.",
            "시즌 내내 파크 지형이 세워집니다.",
            "주중에는 리프트가 분산되어 여유롭습니다.",
            "상급면도 있으나 파우더 트리가 메인 브랜드는 아닙니다.",
        ],
        season_en=[
            "Snowmaking supports Kanto winters.",
            "Best natural snow after cold dumps.",
            "Busy January–February weekends.",
        ],
        season_ko=[
            "인공설이 간토 겨울을 보완합니다.",
            "자연설은 한기 강설 후가 좋습니다.",
            "1~2월 주말이 가장 붐빕니다.",
        ],
        access_en=[
            "Tohoku Shinkansen to Nasushiobara + bus / taxi.",
            "Car from Tokyo via Tohoku Expressway.",
            "Popular overnight bus products.",
        ],
        access_ko=[
            "도호쿠 신칸센 나스시오바라 + 버스·택시.",
            "도호쿠 고속도로 렌터카.",
            "심야버스 상품도 많습니다.",
        ],
        stay_en=[
            "Shiobara onsen hotels for soak + ski.",
            "Nasushiobara business hotels near the station.",
            "Family rooms disappear on three-day weekends.",
        ],
        stay_ko=[
            "스키+온천은 시오바라 온천 호텔.",
            "역세권은 나스시오바라 비즈니스 호텔.",
            "3일 연휴에 패밀리룸이 사라집니다.",
        ],
        tips_en=[
            "Book lessons early for kids holiday weeks.",
            "If parks are the goal, check feature maps online.",
            "Pair with Nasu sightseeing when snow is thin.",
        ],
        tips_ko=[
            "방학 주간 키즈 강습은 미리 예약하세요.",
            "파크가 목적이면 온라인 지형 맵을 확인하세요.",
            "눈이 얇을 때는 나스 관광과 조합하세요.",
        ],
    ),
    "mt_jeans_nasu": entry(
        summary_en="Mt. Jeans Nasu — friendly Nasu family skiing with easy Kanto access.",
        summary_ko="마운트진스 나스 — 접근성 좋은 나스 패밀리 스키.",
        name_en="Mt. Jeans Nasu",
        name_ko="마운트진스 나스",
        hook_en="**Mt. Jeans Nasu** is a friendly Nasu family ski area with easy Kanto access. Prioritize lessons, first turns, and a relaxed pace over steep powder objectives.",
        hook_ko="**마운트진스 나스**는 간토에서 접근하기 쉬운 나스 패밀리 스키장입니다. 급한 파우더보다 강습·첫 턴·여유로운 페이스에 맞춰져 있습니다.",
        slopes_en=[
            "Beginner-centric trails and gentle progression.",
            "Good visibility teaching terrain on many days.",
            "Smaller map — half-days often enough.",
            "Holiday crowds of learners — patience required.",
        ],
        slopes_ko=[
            "초급 중심 코스와 완만한 성장 곡선.",
            "강습하기 좋은 시야의 날이 많습니다.",
            "맵이 작아 반일로도 충분한 경우가 많습니다.",
            "연휴에는 배우는 손님으로 붐빕니다.",
        ],
        season_en=[
            "Snowmaking important in lean winters.",
            "Natural boosts after cold Kanto storms.",
            "Season shorter than Tohoku high peaks.",
        ],
        season_ko=[
            "눈이 적은 해에는 인공설이 중요합니다.",
            "간토 한기 강설 후 자연설이 붙습니다.",
            "도호쿠 고산보다 시즌이 짧습니다.",
        ],
        access_en=[
            "Nasu / Kuroiso access via rail + bus / taxi.",
            "Car from Tokyo is straightforward.",
            "Combine with Nasu animal kingdom / ranches off-snow.",
        ],
        access_ko=[
            "나스·구로이소 철도 + 버스·택시.",
            "도쿄에서 렌터카 접근이 수월합니다.",
            "스키 외 나스 목장·동물원과 조합하세요.",
        ],
        stay_en=[
            "Nasu resort pensions and hotels.",
            "Onsen inns for evening soak culture.",
            "Families should book kitchenette rooms if picky eaters.",
        ],
        stay_ko=[
            "나스 리조트 펜션·호텔.",
            "저녁 온천은 료칸이 좋습니다.",
            "편식하는 아이가 있으면 주방 있는 방을 고르세요.",
        ],
        tips_en=[
            "Perfect first Japan ski for kids living in Tokyo.",
            "Buy afternoon tickets if mornings are sightseeing.",
            "If group advances quickly, graduate to Hunter Mountain next trip.",
        ],
        tips_ko=[
            "도쿄 거주 아이의 첫 일본 스키로 적합합니다.",
            "오전이 관광이면 오후권을 사세요.",
            "실력이 빨리 늘면 다음엔 헌터마운틴으로 졸업하세요.",
        ],
    ),
    "kirifuri_kogen": entry(
        summary_en="Kirifuri Kogen — scenic Nikko highland skiing for compact family days.",
        summary_ko="키리후리 고원 — 닛코 고원의 경관형 콤팩트 패밀리 스키.",
        name_en="Kirifuri Kogen Ski Resort",
        name_ko="키리후리 고원 스키장",
        hook_en="**Kirifuri Kogen** offers scenic highland skiing above Nikko — compact trails, family energy, and easy pairing with Nikko shrines on a culture + snow trip.",
        hook_ko="**키리후리 고원**은 닛코 위의 경관형 고원 스키장으로, 콤팩트한 코스와 패밀리 분위기, 닛코 신사 관광과의 조합이 매력입니다.",
        slopes_en=[
            "Short vertical, friendly pitches.",
            "Views and photos are part of the product.",
            "Best for casual skiers and kids.",
            "Not built for full-day expert laps.",
        ],
        slopes_ko=[
            "짧은 낙차와 친숙한 경사.",
            "전망·사진도 상품의 일부입니다.",
            "캐주얼 스키어·아이에 적합합니다.",
            "하루 종일 상급 랩용은 아닙니다.",
        ],
        season_en=[
            "Confirm opening — highland but not endless snow.",
            "Midwinter safest for natural cover.",
            "Icy mornings after radiative cooling.",
        ],
        season_ko=[
            "고원이라도 눈이 무한하지 않아 오픈을 확인하세요.",
            "자연 커버는 한겨울이 가장 안전합니다.",
            "야간 복사냉각 후 아침 아이스에 주의.",
        ],
        access_en=[
            "Tobu / JR to Nikko area + bus toward Kirifuri.",
            "Car useful for shrine + ski same day.",
            "Tokyo day trip is ambitious but possible with early start.",
        ],
        access_ko=[
            "도부·JR로 닛코권 + 키리후리행 버스.",
            "신사+스키 당일이면 렌터카가 편합니다.",
            "이른 출발이면 도쿄 당도도 가능하지만 빡빡합니다.",
        ],
        stay_en=[
            "Nikko / Kinugawa hotels and ryokan.",
            "Highland pensions when you want immediate ski access.",
            "Reserve weekends early in autumn-leaf spillover seasons too.",
        ],
        stay_ko=[
            "닛코·기누가와 호텔·료칸.",
            "스키 접근을 우선하면 고원 펜션.",
            "단풍 시즌 연장 주말도 예약이 빠릅니다.",
        ],
        tips_en=[
            "Ski morning, Toshogu afternoon on clear winter days.",
            "Half-day tickets usually enough.",
            "Roads can ice in shaded cedars — drive slow.",
        ],
        tips_ko=[
            "맑은 겨울에는 오전 스키 + 오후 도쇼구가 좋습니다.",
            "반일권으로 충분한 경우가 많습니다.",
            "삼나무 그늘 도로는 미끄러우니 서행하세요.",
        ],
    ),
    "nasu_onsen_family": entry(
        summary_en="Nasu Onsen Family Ski Area — tiny onsen-town hill for absolute beginners.",
        summary_ko="나스 온센 패밀리 — 온천마을 초보 전용에 가까운 작은 스키장.",
        name_en="Nasu Onsen Family Ski Area",
        name_ko="나스 온센 패밀리 스키장",
        hook_en="**Nasu Onsen Family Ski Area** is a tiny hill for absolute beginners and short sessions between onsen soaks. Set expectations: charm and convenience over terrain scale.",
        hook_ko="**나스 온센 패밀리 스키장**은 완전 초보와 온천 사이 짧은 세션용 작은 언덕입니다. 지형 스케일보다 매력·편의에 기대를 맞추세요.",
        slopes_en=[
            "Very few trails — learning and gentle sliding.",
            "Ideal first snow experience for toddlers / first-timers.",
            "Rentals geared to casual visitors.",
            "Experts will finish in an hour — plan other Nasu activities.",
        ],
        slopes_ko=[
            "코스가 매우 적어 학습·완만 슬라이딩용입니다.",
            "유아·첫 눈 경험에 적합합니다.",
            "캐주얼 방문객용 렌탈이 중심입니다.",
            "상급은 한 시간이면 끝나니 다른 나스 일정을 짜세요.",
        ],
        season_en=[
            "Short season; verify operations before traveling.",
            "Relies on cold snaps and snowmaking.",
            "Best as part of a Nasu onsen weekend, not a ski pilgrimage.",
        ],
        season_ko=[
            "시즌이 짧아 출발 전 운영을 확인하세요.",
            "한기와 인공설에 의존합니다.",
            "스키 순례가 아니라 나스 온천 주말의 일부로 보세요.",
        ],
        access_en=[
            "Stay in Nasu Onsen and walk / short taxi.",
            "Same Kanto rail / car approaches as other Nasu hills.",
            "No need for early powder alarms.",
        ],
        access_ko=[
            "나스 온센에 묵고 도보·단거리 택시.",
            "다른 나스 스키장과 같은 간토 철도·차량 접근.",
            "파우더 새벽 출발은 필요 없습니다.",
        ],
        stay_en=[
            "Nasu Onsen ryokan with multiple baths.",
            "Focus spend on rooms and meals, not lift luxury.",
            "Evening stroll streets are the atmosphere.",
        ],
        stay_ko=[
            "욕장이 여러 개인 나스 온센 료칸.",
            "예산은 리프트보다 방·식사에 쓰세요.",
            "저녁 거리 산책이 분위기입니다.",
        ],
        tips_en=[
            "Book Hunter or Mt. Jeans if anyone in the group wants a real ski day.",
            "Great weather-backup when mountain roads to higher resorts close.",
            "Buy the shortest ticket available.",
        ],
        tips_ko=[
            "제대로 된 스키일이 필요하면 헌터·마운트진스를 예약하세요.",
            "고산 도로가 막힐 때 날씨 백업으로 좋습니다.",
            "가장 짧은 티켓을 사세요.",
        ],
    ),
}


def build_extra_longform() -> dict[str, dict[str, str]]:
    return dict(_FACTS)


EXTRA_LONGFORM = build_extra_longform()
