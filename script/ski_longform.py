"""
Long-form resort copy (EN/KO) for priority ski destinations.
Used by ski_catalog.resort_article when a resort id is listed here.
"""
from __future__ import annotations

LONGFORM: dict[str, dict[str, str]] = {
    "niseko_grand_hirafu": {
        "summary_en": "Niseko Grand Hirafu — powder slopes, Hirafu village stays, and lift-pass tips for Japan ski trips.",
        "summary_ko": "니세코 그란히라후 — 파우더 슬로프, 히라후 숙소, 리프트권·접근 정보.",
        "en": """## Overview

Niseko Grand Hirafu is the busiest base in **Niseko United** — four linked areas on Mt. Niseko Annupuri. Hirafu village packs restaurants, bars, and walkable lodging, which is why it tops search lists for Korean and international skiers chasing Hokkaido powder.

OKSki maps the resort with curated **Stay** and **Food** pins nearby so you can plan après-ski without scrolling random map results.

## Slopes & lifts

- **Terrain:** Wide groomers, tree runs, and frequent fresh snow; strong options from first-timers to advanced riders.
- **Vertical:** Roughly 950 m top-to-base — one of the bigger drops in the region.
- **Niseko United pass:** A multi-area ticket covers Grand Hirafu, Hanazono, Annupuri, and Niseko Village (check current season rules on the official site).
- **Beginners:** Dedicated learning zones near the base; English signage and rental shops are easy to find in Hirafu.

## Season & snow

- **Typical season:** Late November through early May (exact dates vary each year).
- **Best powder window:** January–February cold snaps; book early for New Year and Lunar New Year weeks.
- **Weather tip:** Niseko gets cloudy "sea-effect" snow — great for powder, so build a flexible schedule for visibility.

## Getting there

- **From New Chitose Airport (CTS):** Shuttle bus or rental car, about 2–2.5 hours to Hirafu (winter roads can be icy — 4WD or chains may be required).
- **From Sapporo:** Train to Kutchan, then bus or taxi to Hirafu (~2 hours total depending on connections).
- **From Seoul:** Fly ICN → CTS (direct or via Tokyo), then pre-book airport shuttle or private transfer; winter flights fill quickly.

## Stay & village life

- **Hirafu Upper/Middle/Lower:** Upper = closer to lifts; Middle = balance of walkability and nightlife; Lower = often better value.
- **Onsen:** Several public baths and hotel spas in Kutchan and Hirafu — ideal after a cold day on the hill.
- **Dining:** Ramen, izakaya, and cafés cluster along Hirafu-zaka; peak dinner hours are 18:00–20:00.

## OKSki tips

- Compare **single-area vs. Niseko United** lift products before you arrive.
- Use the map **Stay** pins for lodges within shuttle range of the gondola.
- Pair skiing with a rest day if you hit a whiteout — Annupuri hot springs are a short drive away.
""",
        "ko": """## 개요

니세코 그란히라후는 **니세코 유나이트(Niseko United)** 4개 리조트 중 가장 활기찬 베이스입니다. 히라후 마을에는 숙소·식당·바가 밀집해 있어, 홋카이도 파우더를 노리는 한국·해외 스키어가 가장 많이 찾는 지역입니다.

OKSki 지도에는 스키장 근처 **숙소(Stay)**·**맛집(Food)** 핀을 따로 표시해, 슬로프 후 일정을 빠르게 짤 수 있습니다.

## 슬로프·리프트

- **지형:** 넓은 완만 슬로프부터 트리런·오프피스테까지 다양하며, 강설 후 파우더가 잘 살아납니다.
- **낙차:** 약 950m 수준으로 니세코 안에서도 체감 낙차가 큰 편입니다.
- **유나이트권:** 그란히라후·하나조노·아누푸리·니세코 빌리지를 연결하는 상품이 있으니 시즌별 규정을 공식 사이트에서 확인하세요.
- **초보자:** 베이스 근처 학습 코스와 렌탈·강습이 영어로 진행되는 곳이 많습니다.

## 시즌·적설

- **시즌:** 보통 11월 말~5월 초(매년 개장·폐장일 상이).
- **파우더 피크:** 1~2월 한파 구간. 연말·설 연휴는 숙소·셔틀을 최소 2~3개월 전에 잡는 것이 안전합니다.
- **날씨:** 연안에서 불어오는 눈 구름으로 흐린 날이 많지만, 그만큼 분체눈이 쌓이는 대표 코스입니다.

## 오는 길

- **신치토세 공항(CTS):** 히라후까지 셔틀·렌터카 약 2~2.5시간. 겨울 도로는 결빙·적설에 유의하세요.
- **삿포로:** JR로 굿찬 역까지 이동 후 버스·택시 환승(약 2시간 전후).
- **서울:** 인천→신치토세 직항 또는 경유 후, 공항 셔틀·전세 차량을 미리 예약하는 것이 일반적입니다.

## 숙소·마을

- **히라후 상·중·하:** 상단은 리프트 접근, 중단은 식당·난바와 균형, 하단은 가성비 숙소가 많은 편입니다.
- **온천:** 굿찬·히라후에 노천탕·호텔 스파가 있어 하루 종료 후 회복에 좋습니다.
- **식사:** 히라후자카 일대에 라멘·이자카야가 몰려 있으며, 저녁 18~20시가 가장 붐빕니다.

## OKSki 팁

- **단일 리조트권 vs 유나이트권** 가격·사용 범위를 출발 전 비교하세요.
- 지도 **Stay** 핀으로 곤돌라 셔틀 범위 숙소를 먼저 좁혀 보세요.
- 백날(시야 불량)이면 아누푸리 온천·근교 드라이브로 하루 쉬어 가는 일정도 추천합니다.
""",
    },
    "niseko_hanazono": {
        "summary_en": "Niseko Hanazono — family terrain, Burton park, and quieter base-area stays near Niseko United.",
        "summary_ko": "니세코 하나조노 — 패밀리 코스, 버튼 파크, 유나이트권과 숙소 팁.",
        "en": """## Overview

Niseko Hanazono sits on the northeast flank of Mt. Niseko Annupuri and is known for modern lifts, a strong **family** focus, and the **Burton**-branded terrain park. It feels slightly calmer than central Hirafu while still linking into the wider Niseko United network.

Use OKSki **Stay** and **Food** pins to find lodging and meals without relying on generic map clutter.

## Slopes & lifts

- **Terrain:** Groomed cruisers, tree skiing zones, and a dedicated park line — good mix for groups with different skill levels.
- **Access:** Gondola and chair network feeds into Niseco United; confirm which lifts are open on low-snow or wind-hold days.
- **Lessons:** Hanazono runs English-friendly ski school programs — book peak-week lessons early.
- **Crowds:** Often a bit quieter than Hirafu base at midday, but holiday weeks still fill up.

## Season & snow

- **Typical season:** Aligns with Niseko United (late Nov – early May).
- **Powder days:** Same Hokkaido storm track as Hirafu — follow avalanche and tree-run rules posted on-site.
- **Families:** Mornings after fresh snow can be cold for kids; plan shorter sessions and hot-chocolate breaks.

## Getting there

- **From CTS airport:** Same as Hirafu — bus or car to Kutchan/Hanazono area (~2–2.5 h).
- **Village shuttles:** Many Hanazono-area hotels run loops to Hirafu and lifts; ask at check-in.
- **From Seoul:** Fly to CTS, then shuttle; some packages include Hanazono drop-off.

## Stay & dining

- **Lodging:** Condo-style and hotel stays near Hanazono base; Hirafu nightlife is 10–15 minutes by shuttle.
- **Food:** Base cafés and hotel restaurants; for variety, shuttle to Hirafu for dinner.
- **Gear:** Rental and tuning at base — compare sizes online during busy weeks.

## OKSki tips

- If your group splits between park riders and beginners, Hanazono is an efficient home base.
- Check **Niseko United** pass inclusions — Hanazono is fully part of the network.
- Use map **Food** pins for après spots on your return route from the hill.
""",
        "ko": """## 개요

니세코 하나조노는 니세코 앗누리산 북동쪽에 위치하며, 최신 리프트·**패밀리** 코스·**버튼(Burton)** 파크로 알려져 있습니다. 히라후 중심가보다 한산한 편이면서도 **니세코 유나이트** 네트워크와 연결됩니다.

OKSki **Stay**·**Food** 핀으로 숙소와 식사를 미리 좁혀 두면 일정이 수월합니다.

## 슬로프·리프트

- **지형:** 완만한 크루저, 트리존, 파크 라인이 갖춰져 있어 동행인 실력이 달라도 무난합니다.
- **연결:** 곤돌라·체어를 통해 유나이트 다른 구역으로 이동 가능(강풍·적설 시 운행 변동 확인).
- **강습:** 영어 강습 프로그램이 잘 갖춰져 있어 성수기에는 사전 예약이 필요합니다.
- **혼잡도:** 한낮에는 히라후 베이스보다 여유로운 경우가 많으나, 연휴에는 동일하게 붐빕니다.

## 시즌·적설

- **시즌:** 유나이트와 동일(11월 말~5월 초 전후).
- **파우더:** 히라후와 같은 강설 패턴 — 트리런·백컨트리 규정을 현장 안내에 따르세요.
- **가족:** 신설 후 오전은 체감 온도가 낮으니 짧은 세션과 실내 휴식을 섞는 것이 좋습니다.

## 오는 길

- **신치토세 공항:** 히라후와 동일하게 셔틀·렌터카 2~2.5시간.
- **숙소 셔틀:** 하나조노·히라후를 오가는 호텔 셔틀이 많으니 체크인 시 시간표를 받으세요.
- **서울:** 인천→신치토세 후 셔틀; 패키지에 하나조노 하차가 포함되는 경우도 있습니다.

## 숙소·식사

- **숙소:** 베이스 인근 콘도·호텔형 숙박이 중심; 히라후 난바는 셔틀 10~15분.
- **식사:** 베이스 카페·호텔 레스토랑; 저녁은 히라후로 나가면 선택지가 넓어집니다.
- **렌탈:** 베이스에서 보드·스키 대여 가능 — 인기 사이즈는 온라인 사전 예약을 권장합니다.

## OKSki 팁

- 파크파와 초보자가 함께라면 하나조노를 거점으로 잡기 좋습니다.
- **유나이트권**에 하나조노가 포함되는지 시즌별로 다시 확인하세요.
- 지도 **Food** 핀으로 슬로프 복귀 동선의 식사처를 미리 저장해 두세요.
""",
    },
    "niseko_annupuri": {
        "summary_en": "Niseko Annupuri — local Japanese vibe, onsen towns, and linked Niseko United skiing.",
        "summary_ko": "니세코 아누푸리 — 로컬 분위기, 온천·유나이트 스키 가이드.",
        "en": """## Overview

Niseko Annupuri is the **west gateway** to Niseko United and feels more local than Hirafu — smaller village scale, Japanese diners, and onsen inns. Skiers who want powder without Hirafu nightlife noise often base here.

OKSki highlights nearby **Stay** (onsen lodges) and **Food** spots on the map for easy trip planning.

## Slopes & lifts

- **Terrain:** Long intermediate cruisers and access to Annupuri summit routes; strong choice for confident intermediates.
- **Character:** Less flashy than Hanazono, more "classic Japan ski town" atmosphere.
- **United access:** Lift from Annupuri connects toward Grand Hirafu and Hanazono on good-weather days — plan buffer time for traverses.
- **Trees:** Popular side-country lines exist; obey boundary ropes and daily avalanche reports.

## Season & snow

- **Season:** Same broad window as the rest of Niseko United.
- **Wind:** West-facing lifts can hold on windy days while other areas run — check the live status board.
- **Onsen culture:** Many guests ski half-day and soak at night — factor that into lift-ticket choices.

## Getting there

- **From CTS:** Drive or bus toward Niseko town / Annupuri (~2–2.5 h).
- **Train:** JR Niseko or Kutchan stations, then taxi or hotel shuttle.
- **From Seoul:** Same air route to CTS; Annupuri lodging often includes pickup if arranged in advance.

## Stay & onsen

- **Ryokan & hotels:** Onsen-inn packages with half-board are common — great value for couples and families.
- **Dining:** Local soba, curry, and izakaya; fewer international chains than Hirafu.
- **Nightlife:** Quiet; shuttle to Hirafu if you want bars.

## OKSki tips

- Pair Annupuri skiing with **Kutchan or Niseko onsen** on a travel day.
- Buy **Niseko United** if you plan to explore Hirafu or Hanazono more than once.
- Map **Stay** pins help find ryokan within walking distance of Annupuri lifts.
""",
        "ko": """## 개요

니세코 아누푸리는 **니세코 유나이트 서쪽** 관문으로, 히라후보다 로컬 감성이 강합니다. 작은 마을 규모, 일본식 식당, 온천 여관이 많아 난바보다 조용한 숙박을 원하는 스키어에게 인기입니다.

OKSki 지도의 **Stay**·**Food** 핀으로 온천 숙소와 식사처를 빠르게 찾을 수 있습니다.

## 슬로프·리프트

- **지형:** 긴 중급 크루저와 정상부 라인이 특징이며, 중급 이상에게 만족도가 높습니다.
- **분위기:** 하나조노만큼 화려하지 않고, 전통적인 일본 스키 마을 느낌이 납니다.
- **유나이트:** 맑은 날 그란히라후·하나조노 방향으로 이동 가능 — 이동·대기 시간을 일정에 넣으세요.
- **트리·사이드:** 인기 구역이 있으나 로프·당일 avalanche 정보를 반드시 확인하세요.

## 시즌·적설

- **시즌:** 니세코 유나이트와 동일.
- **바람:** 서측 리프트가 먼저 멈추는 날이 있어, 당일 운행 표를 확인하는 것이 유리합니다.
- **온천:** 반나절 스키 후 온천이 일상인 여행객이 많아, 리프트권 종류를 그에 맞게 선택하세요.

## 오는 길

- **신치토세 공항:** 니세코·아누푸리 방향 셔틀·렌터카 2~2.5시간.
- **기차:** JR 니세코·굿찬 역 후 택시·숙소 픽업.
- **서울:** 신치토세까지 항공 후, 숙소 사전 픽업을 요청하면 편합니다.

## 숙소·온천

- **료칸·호텔:** 온천+조식·석식 패키지가 흔해 가족·커플에게 가성비가 좋습니다.
- **식사:** 소바·카레·이자카야 중심; 히라후만큼 국제 체인은 적습니다.
- **야간:** 조용함 — 바를 원하면 히라후 셔틀을 이용하세요.

## OKSki 팁

- 스키와 **굿찬·니세코 온천**을 같은 날에 묶는 일정이 잘 맞습니다.
- 히라후·하나조노를 여러 번 갈 계획이면 **유나이트권**이 유리합니다.
- 지도 **Stay** 핀으로 리프트 도보권 료칸을 먼저 비교해 보세요.
- 주말·연휴에는 아누푸리 베이스 주차가 빨리 찰 수 있으니, 숙소 셔틀·택시 예약을 함께 준비하세요.
""",
    },
    "hakuba_happo_one": {
        "summary_en": "Hakuba Happo-one — Olympic-scale vertical, Hakuba Valley access, and Tokyo-friendly trip planning.",
        "summary_ko": "하쿠바 해포 — 올림픽 규모 낙차, 밸리권·도쿄·서울 접근 가이드.",
        "en": """## Overview

Hakuba Happo-one hosted alpine events at the **1998 Nagano Winter Olympics** and remains the flagship resort of the **Hakuba Valley**. With roughly 1,070 m of vertical and long groomed runs, it is a top pick for skiers who want big-mountain skiing within reach of Tokyo — and a frequent add-on for Korean travelers combining Tokyo and snow.

OKSki maps Happo-one with **Stay** and **Food** pins around Hakuba village for post-ski planning.

## Slopes & lifts

- **Scale:** One of Japan's largest single-resort vertical drops — multiple peaks and long descent routes.
- **Levels:** Beginner zones near the base; advanced terrain higher up, including Olympic-course heritage areas (check seasonal opening).
- **Hakuba Valley ticket:** Multi-resort passes link Happo-one, Goryu, 47, and others — worthwhile if you stay 3+ days.
- **Crowds:** Weekends from Tokyo spike traffic; weekday skiing is noticeably calmer.

## Season & snow

- **Typical season:** Late November – early May (lift-dependent).
- **Snow quality:** Nagano powder after cold fronts; spring corn snow in March–April on sunny aspects.
- **Safety:** Mountain weather changes fast — carry layers and check lift closures at the base board.

## Getting there

- **From Tokyo:** JR Hokuriku Shinkansen to Nagano or Toyama area, then bus or train to Hakuba (~4–5 h door-to-door depending on routing).
- **Overnight bus:** Budget option from Shinjuku to Hakuba — saves a hotel night if you can sleep on the bus.
- **From Seoul:** Fly to Narita/Haneda, stay in Tokyo or go direct to Nagano by train; winter luggage forwarding to Hakuba hotels is common.

## Stay & village

- **Hakuba Happo village:** Hotels, pensions, and rental shops walking distance from lifts.
- **Onsen:** Echoland and Wadano areas have foot-baths and ryokan — short taxi from Happo base.
- **Food:** Tonkatsu, ramen, and craft beer pubs; reserve popular restaurants on Saturday nights.

## OKSki tips

- Buy **Valley-wide pass** if you plan to sample Goryu or 47 for park riding.
- Book **Shinkansen + bus** tickets together in peak season.
- Use map **Stay** pins in Echoland/Wadano if Happo base hotels are sold out.
""",
        "ko": """## 개요

하쿠바 해포는 **1998 나가노 동계올림픽** 알파인 경기장이었으며, **하쿠바 밸리(Hakuba Valley)** 의 대표 리조트입니다. 낙차 약 1,070m와 긴 슬로프로, 도쿄에서 당일·1박2일로 오기 좋은 대형 스키장입니다. 한국에서 도쿄+스키를 묶는 일정에도 자주 등장합니다.

OKSki는 해포 주변 **Stay**·**Food** 핀으로 하쿠바 마을 숙소·식사를 한눈에 볼 수 있습니다.

## 슬로프·리프트

- **규모:** 일본 단일 리조트 중 낙차가 큰 편 — 여러 봉우리와 긴 하산 코스가 특징입니다.
- **난이도:** 베이스 초급존과 상부 중·상급 라인, 올림픽 유산 구간(시즌별 개방 확인)이 있습니다.
- **밸리권:** 해포·고류·47 등을 묶는 패스가 있어 3일 이상 체류 시 유리합니다.
- **혼잡:** 도쿄에서 오는 주말 이용객이 많아, 평일 스키가 훨씬 여유롭습니다.

## 시즌·적설

- **시즌:** 11월 말~5월 초 전후(리프트별 상이).
- **눈질:** 한파 뒤 나가노 분체눈; 3~4월에는 햇볕 코스에서 스프링 슬러시·콘스노도 즐길 수 있습니다.
- **안전:** 산악 기상 변화가 빠르니 방풍·보온 레이어와 당일 리프트 운행 공지를 확인하세요.

## 오는 길

- **도쿄:** 북陆 신칸센 나가노 등 경유 후 버스·전철로 하쿠바(문到門 4~5시간 전후).
- **야간 버스:** 신주쿠→하쿠바 심야버스는 숙박비를 아끼는 선택지입니다.
- **서울:** 나리타·하네다 입국 후 도쿄 1박 또는 나가노 직행; 호텔로 수하물 배송 서비스를 쓰는 여행객도 많습니다.

## 숙소·마을

- **해포 마을:** 리프트 도보권 호텔·펜션·렌탈이 밀집합니다.
- **온천:** 에코랜드·와다노에 족욕·료칸 — 해포 베이스에서 택시로 이동.
- **식사:** 돈카츠·라멘·맥주 펍; 토요일 저녁 인기 식당은 예약을 권장합니다.

## OKSki 팁

- 고류·47 파크를 갈 계획이면 **밸리 통합권**을 비교하세요.
- 성수기 **신칸센+버스**는 한 번에 예약하면 매진을 피하기 쉽습니다.
- 해포 숙소가 매진이면 지도 **Stay** 핀으로 에코랜드·와다노 숙소를 검토하세요.
""",
    },
    "rusutsu": {
        "summary_en": "Rusutsu Resort — Hokkaido family skiing, amusement-park base, and powder beyond Niseko.",
        "summary_ko": "루스츠 리조트 — 홋카이도 패밀리 스키, 파우더·숙소·접근 가이드.",
        "en": """## Overview

Rusutsu Resort is a large **Hokkaido** ski area east of Niseko, popular with families and groups who want on-mountain hotels, amusement-park facilities in summer, and reliable powder without Hirafu crowds.

OKSki maps Rusutsu with **Stay** and **Food** pins around the base villages so you can plan lodging and meals in one view.

## Slopes & lifts

- **Terrain:** Three linked peaks (West, East, Mt. Isola) with long cruisers and tree zones; good spread from kids' slopes to advanced lines.
- **Vertical:** Among the bigger Hokkaido resorts — enough variety for multi-day trips.
- **Lifts:** Modern gondola and chair network; West Mountain is often the main hub for families.
- **Lessons:** English kids' programs and rental centers at the base — book holiday weeks early.

## Season & snow

- **Typical season:** Late November – early May (check official calendar).
- **Powder:** Same Hokkaido storm track as Niseko; cold January days deliver light, dry snow.
- **Wind holds:** Exposed lifts can pause on storm days — have a backup onsen or indoor plan.

## Getting there

- **From New Chitose (CTS):** Car or bus roughly 2–2.5 hours; winter tires or 4WD recommended.
- **From Niseko/Hirafu:** About 1 hour by car — doable as a side trip or split stay.
- **From Seoul:** Fly to CTS, then pre-book shuttle; fewer direct packages than Niseko but growing Korean visitor base.

## Stay & resort life

- **Ski-in options:** Tower hotels and lodges at the base — convenient with kids and gear.
- **Onsen:** In-resort baths and nearby rural hot springs after skiing.
- **Dining:** Hotel buffets, curry, and ramen; fewer standalone bars than Hirafu — quieter evenings.

## OKSki tips

- Compare **single-mountain vs. full-area** lift products if you only ski 1–2 days.
- Pair Rusutsu with **Niseko** in one Hokkaido week if you want two powder zones.
- Use map **Stay** pins for West vs. East base — pick the side closest to your main lifts.
""",
        "ko": """## 개요

루스츠 리조트는 니세코 동쪽 **홋카이도** 대형 스키장으로, 온산 호텔·패밀리 시설·히라후보다 한산한 파우더를 원하는 가족·단체 여행에 인기입니다.

OKSki 지도의 **Stay**·**Food** 핀으로 베이스 마을 숙소와 식사를 한 번에 계획할 수 있습니다.

## 슬로프·리프트

- **지형:** 서·동·이솔라 봉우리 3구역이 연결되어 있으며, 완만 크루저와 트리존이 고르게 있습니다.
- **낙차:** 홋카이도 안에서도 체감 규모가 크고, 2~3일 체류에 적합합니다.
- **리프트:** 곤돌라·체어가 현대적이며, 가족은 서산(West) 베이스를 많이 이용합니다.
- **강습:** 어린이 영어 강습·렌탈이 베이스에 있어 연휴는 조기 예약이 필요합니다.

## 시즌·적설

- **시즌:** 11월 말~5월 초 전후(공식 일정 확인).
- **파우더:** 니세코와 같은 강설 패턴; 1월 한파에 건조한 분체눈이 잘 나옵니다.
- **강풍:** 노출 리프트는 폭풍 시 운휴 — 온천·실내 일정을 예비로 두세요.

## 오는 길

- **신치토세(CTS):** 차량·버스 약 2~2.5시간; 겨울 타이어·4WD 권장.
- **니세코/히라후:** 차로 약 1시간 — 분할 숙박·당일 이동도 가능.
- **서울:** 신치토세 항공 후 셔틀 예약; 니세코만큼 패키지는 적지만 한국인 이용이 늘고 있습니다.

## 숙소·리조트

- **스키인:** 베이스 타워 호텔·롯지가 많아 아이·장비 이동이 편합니다.
- **온천:** 리조트 내외 온천으로 하루를 마무리하기 좋습니다.
- **식사:** 호텔 뷔페·카레·라멘 중심; 히라후만큼 난바는 없고 저녁이 조용한 편입니다.

## OKSki 팁

- 1~2일만 스키할 경우 **구역별 리프트권**과 전구역권을 비교하세요.
- **니세코+루스츠**를 한 주에 묶으면 홋카이도 파우더를 두 번 즐길 수 있습니다.
- 지도 **Stay** 핀으로 서산·동산 베이스 중 리프트에 가까운 쪽을 고르세요.
- 성수기에는 **공항 셔틀·렌터카**를 니세코 일정과 함께 한 번에 예약하면 이동 스트레스가 줄어듭니다.
""",
    },
    "furano": {
        "summary_en": "Furano Ski Resort — central Hokkaido scenery, Prince hotels, and dry powder away from the coast.",
        "summary_ko": "후라노 스키장 — 홋카이도 내륙 뷰, 프린스 호텔·파우더 가이드.",
        "en": """## Overview

Furano Ski Resort sits in **central Hokkaido** — famous for lavender fields in summer and dry, light snow in winter. Linked with the Prince Hotel base, it attracts skiers who want scenic runs and a smaller-town feel than Sapporo suburbs.

OKSki shows Furano on the map with **Stay** and **Food** pins for Furano town and Kitanomine base.

## Slopes & lifts

- **Terrain:** Two zones (Kitanomine and Furano Zone) with groomed cruisers and ungroomed options after storms.
- **Views:** Clear-day panoramas over the Furano basin — bring a camera on the summit lift.
- **Levels:** Strong beginner hills near Prince Hotel; steeper pitches on the Furano Zone side.
- **Ropeways:** Gondola access to upper mountain — lines build on holiday mornings.

## Season & snow

- **Typical season:** Late November – early May.
- **Snow character:** Continental powder — often drier than coastal Niseko on cold days.
- **Cold snaps:** January temperatures can drop sharply; quality base layers are essential.

## Getting there

- **From CTS airport:** ~2 hours by car via Chitose–Eniwa–Furano road; rental car most flexible.
- **From Sapporo:** Limited winter buses and trains via Asahikawa — check seasonal timetables.
- **From Seoul:** Fly to CTS or Asahikawa (seasonal); many visitors rent a car for Furano + Biei drives.

## Stay & town

- **Prince Furano:** Ski-in convenience, buffets, and onsen — book New Year early.
- **Furano town:** Cafés, curry shops, and local hotels a short drive from lifts.
- **Side trips:** Biei blue pond and farm roads are popular rest-day drives (winter road conditions vary).

## OKSki tips

- If hotels at Kitanomine are full, use **Stay** pins in Furano town and drive 10–15 minutes.
- Combine skiing with a **non-ski day** in Biei when weather is whiteout.
- Check which zone your lift ticket covers — two-base tickets differ by product.
""",
        "ko": """## 개요

후라노 스키장은 **홋카이도 내륙**에 있으며, 여름 라벤더·겨울 건조한 분체누로 유명합니다. 프린스 호텔 베이스와 연계되어 삿포로 근교보다 한적한 마을 스키를 원하는 이들에게 인기입니다.

OKSki는 후라노·기타노미네 베이스 주변 **Stay**·**Food** 핀을 지도에 표시합니다.

## 슬로프·리프트

- **지형:** 기타노미네·후라노 존 두 구역; 완만 크루저와 강설 후 비압설 코스가 있습니다.
- **뷰:** 맑은 날 후라노 분지 전망이 뛰어나 정상 리프트에서 사진을 많이 찍습니다.
- **난이도:** 프린스 호텔 인근 초급장이 넓고, 후라노 존 쪽에 급경사가 있습니다.
- **곤돌라:** 연휴 오전에는 대기가 길어질 수 있어 이른 시작을 권장합니다.

## 시즌·적설

- **시즌:** 11월 말~5월 초 전후.
- **눈질:** 내륙형 분체눈 — 한파 때 니세코 해안보다 건조하게 느껴지는 날이 많습니다.
- **한파:** 1월 영하가 깊어지니 보온·방풍 레이어를 충분히 준비하세요.

## 오는 길

- **신치토세:** 렌터카로 약 2시간; 자유 일정에는 차량이 가장 편합니다.
- **삿포로:** 아사히카와 경유 버스·기차(시즌 한정) — 시간표를 미리 확인하세요.
- **서울:** 신치토세 또는 아사히카와 입국 후 렌터카; 후라노+비에이 드라이브와 묶는 경우가 많습니다.

## 숙소·마을

- **프린스 후라노:** 스키인·뷔페·온천 일체형 — 연말·설 연휴는 조기 예약.
- **후라노 시내:** 리프트에서 차로 10분 내 카페·카레·로컬 호텔.
- **근교:** 비에이·팜로드는 휴스키 데이에 인기(겨울 도로·폐쇄 구간 확인).

## OKSki 팁

- 기타노미네 숙소가 매진이면 **Stay** 핀으로 시내 숙박 후 차량 이동을 검토하세요.
- 백날에는 **비에이 드라이브**로 스키를 쉬어 가는 일정이 잘 맞습니다.
- 리프트권이 **어느 베이스를 포함하는지** 상품별로 다시 확인하세요.
- 겨울 **렌터카 예약**은 눈 타이어 옵션까지 포함해 미리 확정하는 것이 안전합니다.
""",
    },
    "hakuba_goryu": {
        "summary_en": "Hakuba Goryu — Escal Plaza base, family tree runs, and Hakuba Valley lift links.",
        "summary_ko": "하쿠바 고류 — 에스칼 플라자, 패밀리·트리런, 밸리권 가이드.",
        "en": """## Overview

Hakuba Goryu (part of **Hakuba Valley**) centers on **Escal Plaza** — a modern base with restaurants, rentals, and easy access to Kamishiro area lodging. It is a favorite for families and tree-run fans who want a calmer vibe than Happo-one on busy weekends.

OKSki maps **Stay** and **Food** options around Goryu and nearby Hakuba stations.

## Slopes & lifts

- **Terrain:** Groomed runs plus well-known tree skiing zones (follow resort rules and daily patrol guidance).
- **Escal Plaza:** Central hub — tickets, gear, and food in one building.
- **Linked areas:** Valley pass can include Happo-one, 47, and others — great for 3+ day trips.
- **Beginners:** Wide lower slopes; advanced riders head to upper mountain and gladed sections.

## Season & snow

- **Season:** Aligns with Hakuba Valley (late Nov – early May).
- **Powder:** Nagano storms after cold fronts; trees hold snow days after groomers get tracked out.
- **Visibility:** Fog can sit in the trees — ski with a buddy and carry a map.

## Getting there

- **From Tokyo:** Shinkansen to Nagano, then bus/train to Hakuba (~4–5 h total).
- **Local:** Shuttle from Hakuba Station to Escal Plaza — many lodges offer pickup.
- **From Seoul:** Fly to Tokyo, train to Nagano; some skiers stay in Kamishiro pensions.

## Stay & dining

- **Kamishiro:** Pensions and small hotels with host-style hospitality.
- **Food:** Plaza restaurants, ramen, and izakaya; Echoland nightlife is a short bus ride.
- **Gear:** Full rental at Escal — size reservations help on peak Saturdays.

## OKSki tips

- Tree skiing requires **awareness of boundaries** — ask patrol about daily openings.
- If Happo-one is crowded, Goryu often feels more relaxed on the same snow cycle.
- Use **Stay** pins near Hakuba Station if you rely on public transport daily.
""",
        "ko": """## 개요

하쿠바 고류는 **하쿠바 밸리**의 한 축으로, **에스칼 플라자(Escal Plaza)** 베이스가 중심입니다. 렌탈·식당이 한곳에 모여 있어 가족·트리런 이용객이 주말 해포보다 여유롭게 찾는 경우가 많습니다.

OKSki **Stay**·**Food** 핀으로 고류·하쿠바 역 주변 숙소를 비교할 수 있습니다. 단기 체류라도 역 근처 숙박은 셔틀 시간을 줄여 줍니다.

## 슬로프·리프트

- **지형:** 완만 슬로프와 알려진 트리존(당일 패트롤 안내·구역 규정 준수).
- **에스칼 플라자:** 리프트권·렌탈·식사 허브.
- **밸리 연결:** 해포·47 등과 통합권 이용 가능 — 3일 이상 체류 시 유리.
- **난이도:** 하단은 초급 친화, 상부·글레이드는 중급 이상에게 인기.

## 시즌·적설

- **시즌:** 밸리 전체와 동일(11월 말~5월 초).
- **파우더:** 한파 뒤 나가노 강설; 트리는 압설 후 며칠 더 품질이 유지되기도 합니다.
- **시야:** 안개 시 트리에서 시야가 짧아지니 동행·지도를 준비하세요.

## 오는 길

- **도쿄:** 나가노 신칸센 후 버스·전철(총 4~5시간 전후).
- **현지:** 하쿠바 역→에스칼 셔틀; 펜션 픽업을 요청하면 편합니다.
- **서울:** 도쿄 입국 후 나가노 경유; 가미시로 펜션 숙박이 흔합니다.

## 숙소·식사

- **가미시로:** 소규모 펜션·가족형 호스피탈리티.
- **식사:** 플라자 내 식당·라멘; 에코랜드 난바는 버스로 이동.
- **렌탈:** 에스칼에서 일괄 대여 — 토요일 성수기는 사이즈 예약 권장.

## OKSki 팁

- 트리 스키는 **경계·당일 개방 구역**을 패트롤에 확인하세요.
- 해포가 붐빌 때 고류가 같은 눈 사이클에서 한산한 편입니다.
- 대중교통 위주면 **Stay** 핀으로 하쿠바 역 인근 숙소를 우선 보세요.
- 주말 **에스칼 플라자 주차**는 오전 일찍 찾는 것이 좋습니다.
- **밸리 통합권**은 인터넷 사전 구매가 줄을 줄여 줄 때가 많습니다.
""",
    },
    "hakuba_47": {
        "summary_en": "Hakuba 47 — terrain parks, halfpipes, and freestyle skiing in Hakuba Valley.",
        "summary_ko": "하쿠바 47 — 테린파크·프리스타일, 밸리 파우더 가이드.",
        "en": """## Overview

**Hakuba 47 Winter Sports Park** is the freestyle hub of **Hakuba Valley** — terrain parks, jumps, and halfpipe events draw riders from across Asia. It connects with Goryu via the **Hakuba Universal** lift link on many days, so you can park-ride in the morning and cruise Goryu trees in the afternoon.

OKSki highlights **Stay** and **Food** near 47 base and Kamishiro for group trips.

## Slopes & lifts

- **Parks:** Multiple park lines with varying jump sizes — check feature maps at the lift ticket desk.
- **Powder:** Beyond the park, upper mountain steeps and trees reward advanced skiers after storms.
- **47 + Goryu:** Combined ticket common — plan traverses time between bases.
- **Events:** Hosts international comps some seasons — book lodging early those weekends.

## Season & snow

- **Season:** Late November – early May (park features depend on snow depth).
- **Spring:** March–April park laps on softer snow — popular with snowboard schools.
- **Safety:** Wear a helmet in the park; respect closure ropes on unfinished features.

## Getting there

- **Routing:** Same as Hakuba Valley — Tokyo → Nagano → Hakuba bus.
- **Base:** 47 ticket office and parking at the Kamishiro side — arrive early on powder mornings.
- **From Seoul:** Tokyo entry + train; many freestyle camps run bilingual lessons.

## Stay & après

- **Lodging:** Kamishiro pensions or Echoland condos — short drive or shuttle to 47.
- **Food:** Base cafés and burger spots; Hakuba beer after park sessions.
- **Rentals:** Park-specific boards and helmets available for rent.

## OKSki tips

- Start with **small features** if you are new to park riding — progression parks are marked.
- Buy **Valley or 47+Goryu** pass if you split time between park and trees.
- Map **Food** pins for quick lunch between lap sessions — midday lines grow fast.
""",
        "ko": """## 개요

**하쿠바 47 윈터 스포츠 파크**는 **하쿠바 밸리**의 프리스타일 중심지입니다. 테린파크·점프·하프파이프로 아시아 라이더가 모이며, **유니버설** 연결로 고류 트리와 오전·오후 분할 스키가 가능합니다.

OKSki **Stay**·**Food** 핀으로 47·가미시로 숙소·식사를 빠르게 고를 수 있습니다. 프리스타일 캠프 시즌에는 숙소가 빨리 찹니다.

## 슬로프·리프트

- **파크:** 난이도별 파크 라인 — 리프트 매표소에서 당일 feature 맵 확인.
- **파우더:** 파크 밖 상부 급경사·트리는 강설 뒤 상급자에게 인기.
- **47+고류:** 연합권이 흔해 베이스 간 이동 시간을 일정에 넣으세요.
- **대회:** 시즌별 국제 대회 시 숙소가 빨리 찹니다.

## 시즌·적설

- **시즌:** 11월 말~5월 초(파크 오픈은 적설량에 따라 변동).
- **봄:** 3~4월 연질 눈 파크 연습·캠프 수요가 많습니다.
- **안전:** 파크에서는 헬멧 착용, 미완성 feature 로프 준수.

## 오는 길

- **경로:** 밸리 공통 — 도쿄→나가노→하쿠바 버스.
- **베이스:** 가미시로 쪽 매표·주차 — 파우더 아침은 일찍 도착.
- **서울:** 도쿄 입국 후 기차; 양어 캠프·강습이 있는 시즌이 많습니다.

## 숙소·식사

- **숙박:** 가미시로 펜션·에코랜드 콘도 — 셔틀·차량 10분 내외.
- **식사:** 베이스 카페·버거; 파크 후 하쿠바 맥주 펍.
- **렌탈:** 파크용 보드·헬멧 대여 가능.

## OKSki 팁

- 파크 초보라면 **프로그레션 라인**부터 시작하세요.
- 파크와 트리를 나눠 탄다면 **47+고류·밸리권**을 비교하세요.
- 점심 피크 전에 지도 **Food** 핀으로 가까운 식당을 정해 두면 대기를 줄일 수 있습니다.
- 파크 이용 시 **보호대·헬멧** 대여 여부를 베이스에서 미리 확인하세요.
- 고류와 **왕복 셔틀 시간**을 미리 적어 두면 오후 이동이 수월합니다.
- **리프트 마감 시간**도 함께 확인하세요.
""",
    },
    "nozawa_onsen": {
        "summary_en": "Nozawa Onsen — historic hot-spring village, traditional lodging, and Nagano powder.",
        "summary_ko": "노자와 온센 — 온천 마을·료칸 숙박, 나가노 파우더 가이드.",
        "en": """## Overview

Nozawa Onsen combines **600-year-old hot-spring culture** with a full-scale ski mountain — narrow stone streets, free public baths (soto-yu), and ryokan stays define the experience. Korean and Taiwanese skiers often choose it for authentic Japan atmosphere plus reliable snow.

OKSki maps **Stay** (ryokan) and **Food** (soba, onsen eggs) in the village at the foot of the slopes.

## Slopes & lifts

- **Terrain:** Long runs from the summit; good mix for intermediates; steep sections near the top.
- **Village proximity:** Slopes end near town — walk to lunch and afternoon onsen.
- **Night skiing:** Select evenings in peak season — check the official schedule.
- **Crowds:** Popular during Chinese New Year and Japanese holidays — book ryokan months ahead.

## Season & snow

- **Season:** Late November – early May.
- **Snow:** Heavy Nagano dumps; village roads can be icy — proper footwear for walking at night.
- **Onsen etiquette:** Rinse before entering; tattoos may require private baths — ask your ryokan.

## Getting there

- **From Tokyo:** Hokuriku Shinkansen to Iiyama or Nagano, then bus to Nozawa (~4–5 h).
- **From Seoul:** Fly to Tokyo, train north; some tour packages include Nozawa + Snow Monkey side trips.
- **Local:** Village is compact — many guests walk; ski buses link outlying ryokan.

## Stay & culture

- **Ryokan:** Half-board packages with kaiseki dinners — core Nozawa experience.
- **Soto-yu:** Thirteen public baths; pick up a village bath map at tourist info.
- **Food:** Nozawana pickles, onsen tamago, and hearth soba — try Ogama cooking eggs in spring water.

## OKSki tips

- Reserve **ryokan with private bath** if you have tattoo concerns.
- Ski morning, **onsen afternoon** — classic two-session day.
- Use **Stay** pins to compare in-village vs. hillside lodges for slope access.
""",
        "ko": """## 개요

노자와 온센은 **600년 역사의 온천 마을**과 대형 스키장이 한곳에 있습니다. 돌길·공동 온천(外湯)·료칸 숙박이 여행의 중심이며, 한국·대만 스키어에게 ‘일본 감성+눈’ 조합으로 인기입니다.

OKSki는 마을 기슭 **Stay**(료칸)·**Food**(소바·온천달걀) 핀을 지도에 표시합니다. 료칸 조식·석식 시간은 체크인 때 확인하세요.

## 슬로프·리프트

- **지형:** 정상에서 이어지는 긴 코스; 중급자에게 만족도 높고 상부는 급경사.
- **마을 접근:** 슬로프 하단이 마을과 가까워 점심·온천 이동이 쉽습니다.
- **야간:** 성수기 일부 요일 야간 영업 — 공식 스케줄 확인.
- **혼잡:** 설·골든위크·연휴는 료칸을 몇 달 전에 잡는 것이 안전합니다.

## 시즌·적설

- **시즌:** 11월 말~5월 초.
- **강설:** 나가노 폭설 후 파우더; 밤 마을 길은 결빙 — 미끄럼 방지 신발 권장.
- **온천 예절:** 입욕 전 샤워; 타투는 료칸 사설탕 문의.

## 오는 길

- **도쿄:** 이나마·나가노 신칸센 후 버스(4~5시간 전후).
- **서울:** 도쿄 입국 후 북쪽 기차; 스노우몽키+노자와 패키지도 흔합니다.
- **현지:** 마을은 도보 중심; 외곽 료칸은 스키 버스 이용.

## 숙소·문화

- **료칸:** 조석식 카이세키 패키지가 대표 경험입니다.
- **外湯:** 13곳 공동탕 — 관광안내소에서 지도 수령.
- **먹거리:** 노자와나·온천달걀·화로 소바 — 오가마 족욕·달걀 삶기 체험.

## OKSki 팁

- 타투가 있으면 **사설탕 료칸**을 먼저 검색하세요.
- 오전 스키·오후 온천 **2타임 일정**이 가장 잘 맞습니다.
- **Stay** 핀으로 마을 중심 vs 경사장 가까운 숙소를 비교하세요.
- 마을 **外湯 투어**는 저녁 일정으로 2~3곳만 골라 다니면 피로가 덜합니다.
- **노자와나 피클**과 온천달걀은 마을 슈퍼·식당에서 쉽게 구할 수 있습니다.
- 스키 **장갑 두 켤레**를 챙기면 젖은 장갑을 말릴 여유가 생깁니다.
""",
    },
    "gala_yuzawa": {
        "summary_en": "Gala Yuzawa — station-linked skiing from Tokyo, ideal for beginners and day trips.",
        "summary_ko": "갈라 유자와 — 역 직결 스키, 도쿄 당일·초보자 가이드.",
        "en": """## Overview

Gala Yuzawa is the classic **Tokyo day-trip ski hill** — the gondola leaves from **Gala Yuzawa Station** on the Joetsu Shinkansen, so you can ski without renting a car. Beginners and short-stay visitors from Korea often pair it with 1–2 nights in Tokyo or Yuzawa town.

OKSki maps **Stay** and **Food** in Yuzawa for overnight extensions beyond a single ski day.

## Slopes & lifts

- **Scale:** Compact compared to Hakuba or Niseko — enough for one full day or learning weekend.
- **Beginners:** Wide nursery slopes near the station building; rental and lesson desks in English.
- **Advanced:** Upper mountain steeps on powder days — do not underestimate the hill when snow is deep.
- **Link:** Walking distance from Yuzawa town hotels and Echigo-Yuzawa Station amenities.

## Season & snow

- **Season:** Mid-December – early May (often opens after other Niigata areas).
- **Wet snow:** Coastal Niigata can be heavier and wetter than Hokkaido — wax accordingly.
- **Rain line:** Lower elevations see rain sometimes — check live cameras before leaving Tokyo.

## Getting there

- **From Tokyo:** Joetsu Shinkansen to Gala Yuzawa Station (~75–90 min) — among the fastest ski access from the capital.
- **Same-day:** Morning train up, evening train back — popular with Tokyo residents.
- **From Seoul:** Fly to Tokyo, Shinkansen same day possible with early arrival.

## Stay & town

- **Yuzawa:** Sake museums, onsen hotels, and ramen — stay if you want two ski days without rushing.
- **Food:** Station building cafeterias and slope-side restaurants.
- **Gear:** Rent on-site — travel light from Tokyo hotels.

## OKSki tips

- Buy **Shinkansen + lift** packages in peak season when offered.
- If Gala is rainy, **Kagura or Naeba** are nearby alternatives on the same trip.
- Use **Stay** pins only if you extend beyond a day trip — otherwise Tokyo base works.
""",
        "ko": """## 개요

갈라 유자와는 **도쿄 당일 스키**의 대표 코스입니다. **上越新幹線 갈라 유자와 역**에서 곤돌라가 바로 올라가 렌터카 없이 스키가 가능합니다. 한국에서 도쿄 1~2박과 묶는 초보·단기 여행에 자주 쓰입니다.

OKSki **Stay**·**Food** 핀은 하루 이상 묵을 때 유자와 시내 숙박·식사에 유용합니다. 도쿄 왕복 당일 스키는 짐을 최소화하는 것이 좋습니다.

## 슬로프·리프트

- **규모:** 하쿠바·니세코보다 소형 — 당일 1회전 또는 입문 주말에 적합.
- **초보:** 역사 인근 넓은 초급장; 영어 렌탈·강습 데스크.
- **상급:** 강설 시 상부 급경사 — 규모 대비 난이도를 과소평가하지 마세요.
- **연결:** 에치고유자와 역·유자와 온천가와 도보·단거리 이동.

## 시즌·적설

- **시즌:** 12월 중순~5월 초(개장이 다른 니가타보다 늦은 해도 있음).
- **습설:** 니가타 해안은 홋카이도보다 무겁고 습한 눈 — 왁스·장비 점검.
- **비선:** 저고도는 비가 올 수 있어 도쿄 출발 전 라이브 카메라 확인.

## 오는 길

- **도쿄:** 조에츠 신칸센 갈라 유자와 역(약 75~90분) — 수도권에서 가장 빠른 스키 중 하나.
- **당일:** 오전 상행·저녁 하행 — 도쿄 거주자에게 인기.
- **서울:** 도쿄 일찍 도착 시 당일 신칸센+스키도 가능.

## 숙소·마을

- **유자와:** 사케 박물관·온천 호텔·라멘 — 2일 스키 시 숙박 추천.
- **식사:** 역사·슬로프 레스토랑.
- **렌탈:** 현장 대여 — 도쿄 호텔에서 가볍게 이동.

## OKSki 팁

- 성수기 **신칸센+리프트** 패키지가 있으면 함께 구매하세요.
- 비 오면 **카구라·나에바** 등 인근 리조트 대안을 검토하세요.
- 당일만 한다면 숙소는 도쿄, 2일 이상이면 **Stay** 핀으로 유자와 숙박을 보세요.
- 도쿄 출발 전 **갈라 역 실시간 운행·적설**을 확인하면 당일 취소를 줄일 수 있습니다.
- 초보라면 **오전 첫 곤돌라**에 맞추면 강습·렌탈 대기가 짧습니다.
""",
    },
    "naeba": {
        "summary_en": "Naeba Ski Resort — Prince hotels, Fuji Rock summer fame, and Yuzawa family skiing.",
        "summary_ko": "나에바 스키장 — 프린스 호텔, 유자와 패밀리·축제 가이드.",
        "en": """## Overview

Naeba Ski Resort anchors the **Yuzawa highland** with Prince Hotel lodging, long cruisers, and the famous **Fuji Rock** festival site in summer. Families and groups from Tokyo and Korea use it for 2–3 night ski trips with onsen and shopping at Echigo-Yuzawa Station.

OKSki shows Naeba with **Stay** and **Food** pins across the Prince base and Yuzawa town.

## Slopes & lifts

- **Terrain:** Wide groomed runs from the Prince base; good for mixed-ability groups.
- **Vertical:** Respectable drop for Honshu — enough for a full day without repeating the same lift.
- **Dragondola:** Iconic gondola link toward Kagura area on connected ticket days (verify season operations).
- **Kids:** Dedicated learning zones and ski school — busy during Japanese school holidays.

## Season & snow

- **Season:** Late November – early May.
- **Snow:** Niigata coastal storms; powder days followed by spring slush in March.
- **Events:** Snow festivals and night skiing select dates — check the events calendar.

## Getting there

- **From Tokyo:** Joetsu Shinkansen to Echigo-Yuzawa, then shuttle or taxi to Naeba (~2 h total from Tokyo).
- **Luggage:** Coin lockers and forwarding at Yuzawa Station — convenient for Seoul–Tokyo–ski itineraries.
- **From Seoul:** Tokyo fly-in + train; some skiers bus directly to Prince Hotel in winter.

## Stay & amenities

- **Prince Naeba:** Ski-in hotel, pools, and buffets — flagship stay.
- **Yuzawa town:** Cheaper hotels and izakaya near the station for rail-focused trips.
- **Onsen:** Doroyu and other baths a short drive — classic après combo.

## OKSki tips

- Compare **Naeba-only vs. Kagura linked** tickets if you want more terrain.
- Station-area **Stay** saves money; Prince saves time on the snow.
- Book Prince early for **Fuji Rock weekend overflow crowds** in winter (still popular for ski).
""",
        "ko": """## 개요

나에바 스키장은 **유자와 고원**의 중심으로, 프린스 호텔·긴 크루저·여름 **후지 록** 장소로 알려져 있습니다. 도쿄·한국에서 2~3박 스키+온천을 묶는 패밀리·단체 여행에 자주 등장합니다.

OKSki는 프린스 베이스·유자와 시내 **Stay**·**Food** 핀을 함께 보여 줍니다. 역 주변은 식당·편의점이 많아 첫날 밤에 유리합니다.

## 슬로프·리프트

- **지형:** 프린스 베이스에서 펼쳐지는 넓은 완만 슬로프 — 동행인 실력이 달라도 무난.
- **낙차:** 본州 기준 충분한 체감 낙차로 하루 종일 다른 리프트를 탈 수 있습니다.
- **드래곤도라:** 시즌에 따라 **카구라** 연결(연합권·운행 여부 확인).
- **어린이:** 학습장·스키스쿨 — 일본 방학 시즌에 붐빕니다.

## 시즌·적설

- **시즌:** 11월 말~5월 초.
- **눈:** 니가타 폭설과 3월 이후 슬러시; 이벤트·야간 스키 일정은 달력 확인.
- **축제:** 겨울 스노우 이벤트가 있는 해도 있어 미리 공지를 봅니다.

## 오는 길

- **도쿄:** 에치고유자와 신칸센 후 셔틀·택시(도쿄에서 약 2시간).
- **짐:** 유자와 역 코인락커·배송 서비스 — 서울→도쿄→스키 일정에 유리.
- **서울:** 도쿄 항공 후 기차; 겨울 프린스 직행 버스 패키지도 있습니다.

## 숙소·편의

- **프린스 나에바:** 스키인·풀·뷔페 일체형.
- **유자와 시내:** 역 근처 가성비 호텔·이자카야.
- **온천:** 도로유 등 근교 온천 — 스키 후 half-day 코스.

## OKSki 팁

- 지형을 넓히려면 **나에바+카구라** 연합권을 비교하세요.
- 역 근처 **Stay**는 비용, 프린스는 슬로프 시간을 살립니다.
- 인기 주말·연휴는 **프린스 조기 예약**을 권장합니다.
- **에치고유자와 역**에서 짐 보관 후 당일 스키만 하는 일정도 자주 쓰입니다.
- 프린스 숙박 시 **조식 시간**을 스키 시작 전에 맞춰 두세요.
- **카구라 연결** 운행일은 시즌마다 다릅니다.
""",
    },
    "myoko_suginohara": {
        "summary_en": "Myoko Suginohara — one of Japan's longest runs, deep Niigata powder, and family-friendly base.",
        "summary_ko": "묘코 스기노하라 — 장거리 코스, 니가타 파우더·패밀리 가이드.",
        "en": """## Overview

Myoko Suginohara is known for **one of Japan's longest continuous ski runs** and deep **Niigata powder** on Mt. Myoko. Less hectic than Tokyo-adjacent Gala or Naeba, it suits skiers who want long cruisers, family slopes, and easy access from Nagano or Niigata airports.

OKSki maps **Stay** and **Food** around Suginohara base and Akakura onsen town.

## Slopes & lifts

- **Long run:** Famous top-to-bottom cruiser — plan leg-saving warm-up laps first.
- **Terrain:** Mix of groomers, tree pockets, and moderate steeps; strong for intermediates.
- **Lifts:** Efficient chair network; weekday skiing feels spacious.
- **Myoko area:** Other Myoko resorts (Akakura, etc.) nearby — multi-day explorers rent a car.

## Season & snow

- **Season:** Late November – early May.
- **Snowfall:** Among the snowiest regions in Japan — storms can close roads briefly.
- **Avalanche awareness:** Off-piste rules strict — read daily patrol boards.

## Getting there

- **From Tokyo:** Hokuriku Shinkansen to Joetsu-Myoko or Nagano, then bus/taxi (~3–4 h).
- **From Niigata Airport:** Closer than Tokyo — seasonal shuttles to Myoko.
- **From Seoul:** Fly to Niigata or Tokyo; winter tires essential if driving.

## Stay & onsen

- **Suginohara base:** Hotels and pensions walking distance to lifts.
- **Akakura:** Traditional onsen street 15–20 minutes away — popular evening trip.
- **Food:** Local ramen, mountain curry, and hotel dinners.

## OKSki tips

- Save energy for the **full-length descent** — it is longer than it looks on the map.
- Combine with **Akakura onsen** on a rest or half-day.
- Use **Stay** pins to choose slope-side vs. onsen-town lodging for your group style.
""",
        "ko": """## 개요

묘코 스기노하라는 **일본에서 가장 긴 연속 코스** 중 하나와 **묘코의 니가타 파우더**로 유명합니다. 갈라·나에바보다 한산해 긴 크루저·패밀리 스키·나가노·니가타 공항 접근을 원하는 이들에게 맞습니다.

OKSki는 스기노하라 베이스·아카쿠라 온천가 **Stay**·**Food** 핀을 지도에 표시합니다. 렌터카가 있으면 온천가 저녁 식사 선택지가 넓어집니다.

## 슬로프·리프트

- **장거리:** 정상에서 한 번에 내려오는 대표 코스 — 첫 랩은 워밍업으로 짧게 시작하세요.
- **지형:** 완만 슬로프·트리·중급 급경사가 고르게 있습니다.
- **리프트:** 체어 효율이 좋고 평일은 여유롭습니다.
- **묘코 일대:** 아카쿠라 등 인근 리조트 — 렌터카로 2~3일 순회하기 좋습니다.

## 시즌·적설

- **시즌:** 11월 말~5월 초.
- **강설:** 일본에서 강설량이 많은 지역 — 폭설 시 도로 통제가 잠깐 있을 수 있습니다.
- **오프피스테:** 규정이 엄격 — 당일 패트롤 공지를 확인하세요.

## 오는 길

- **도쿄:** 호쿠리쿠 신칸센 조에츠묘코·나가노 후 버스·택시(3~4시간).
- **니가타 공항:** 도쿄보다 가깝 — 시즌 셔틀 확인.
- **서울:** 니가타 또는 도쿄 입국; 자가 운전 시 겨울 타이어 필수.

## 숙소·온천

- **스기노하라 베이스:** 리프트 도보권 호텔·펜션.
- **아카쿠라:** 온천 거리 15~20분 — 저녁 온천 코스로 인기.
- **식사:** 라멘·산 카레·호텔 디너.

## OKSki 팁

- **풀코스 하산**은 지도보다 길게 느껴지니 체력 분배하세요.
- 휴식일에 **아카쿠라 온천**과 묶기 좋습니다.
- 슬로프 바로 앞 vs 온천 마을 숙소는 **Stay** 핀으로 그룹 성향에 맞게 고르세요.
- 폭설 예보 시 **도로 통제 뉴스**를 확인하고 여유 일정을 두세요.
- **아카쿠라 온천가** 택시비는 숙소 프론트에서 대략 견적을 받을 수 있습니다.
- **장거리 코스** 전에 워밍업 랩을 충분히 하세요.
""",
    },
}

try:
    from ski_longform_extra import EXTRA_LONGFORM
except ImportError:  # package-style import fallback
    from .ski_longform_extra import EXTRA_LONGFORM  # type: ignore

LONGFORM = {**LONGFORM, **EXTRA_LONGFORM}

LONGFORM_IDS = frozenset(LONGFORM.keys())
