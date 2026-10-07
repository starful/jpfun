/**
 * Activity + per-activity region helpers for JPFun.
 */

export const ACTIVITIES = ['ski', 'surf', 'dive', 'camp'];

export const REGIONS_BY_ACTIVITY = {
    ski: [
        { key: 'all', label: 'All', countId: 'count-region-all' },
        { key: 'hokkaido', label: 'Hokkaido', countId: 'count-region-hokkaido' },
        { key: 'nagano', label: 'Nagano', countId: 'count-region-nagano' },
        { key: 'niigata', label: 'Niigata', countId: 'count-region-niigata' },
        { key: 'tohoku', label: 'Tohoku', countId: 'count-region-tohoku' },
        { key: 'gifu', label: 'Gifu', countId: 'count-region-gifu' },
        { key: 'gunma', label: 'Gunma', countId: 'count-region-gunma' },
        { key: 'tochigi', label: 'Tochigi', countId: 'count-region-tochigi' },
    ],
    surf: [
        { key: 'all', label: 'All', countId: 'count-region-all' },
        { key: 'kanto', label: 'Kanto', countId: 'count-region-kanto' },
        { key: 'chubu', label: 'Chubu', countId: 'count-region-chubu' },
        { key: 'tohoku', label: 'Tohoku', countId: 'count-region-tohoku' },
        { key: 'kansai', label: 'Kansai', countId: 'count-region-kansai' },
        { key: 'chugoku', label: 'Chugoku', countId: 'count-region-chugoku' },
        { key: 'shikoku', label: 'Shikoku', countId: 'count-region-shikoku' },
        { key: 'kyushu', label: 'Kyushu', countId: 'count-region-kyushu' },
        { key: 'okinawa', label: 'Okinawa', countId: 'count-region-okinawa' },
    ],
    dive: [
        { key: 'all', label: 'All', countId: 'count-region-all' },
        { key: 'okinawa', label: 'Okinawa', countId: 'count-region-okinawa' },
        { key: 'chubu', label: 'Izu', countId: 'count-region-chubu' },
        { key: 'kanto', label: 'Kanto', countId: 'count-region-kanto' },
        { key: 'kansai', label: 'Kansai', countId: 'count-region-kansai' },
        { key: 'chugoku', label: 'Chugoku', countId: 'count-region-chugoku' },
        { key: 'kyushu', label: 'Kyushu', countId: 'count-region-kyushu' },
    ],
    camp: [
        { key: 'all', label: 'All', countId: 'count-region-all' },
        { key: 'hokkaido', label: 'Hokkaido', countId: 'count-region-hokkaido' },
        { key: 'tohoku', label: 'Tohoku', countId: 'count-region-tohoku' },
        { key: 'kanto', label: 'Kanto', countId: 'count-region-kanto' },
        { key: 'chubu', label: 'Chubu', countId: 'count-region-chubu' },
        { key: 'nagano', label: 'Nagano', countId: 'count-region-nagano' },
        { key: 'kansai', label: 'Kansai', countId: 'count-region-kansai' },
        { key: 'chugoku', label: 'Chugoku', countId: 'count-region-chugoku' },
        { key: 'kyushu', label: 'Kyushu', countId: 'count-region-kyushu' },
    ],
};

const REGION_RULES = [
    ['hokkaido', /Hokkaido|홋카이도|北海道/i],
    ['nagano', /Nagano|나가노|長野/i],
    ['niigata', /Niigata|니가타|新潟/i],
    ['tohoku', /Tohoku|Miyagi|Akita|Aomori|Yamagata|Iwate|Fukushima|도호쿠|미야기|아키타|아오모리|야마가타|이와테|후쿠시마|東北|宮城|秋田|青森|山形|岩手|福島/i],
    ['gifu', /Gifu|기후|岐阜/i],
    ['gunma', /Gunma|군마|群馬/i],
    ['tochigi', /Tochigi|도치기|栃木/i],
    ['kanto', /Kanto|Tokyo|Kanagawa|Chiba|Ibaraki|Saitama|Shonan|도쿄|가나가와|치바|이바라키|쇼난|関東|東京|神奈川|千葉|茨城|Fujisawa|Oarai|Isumi|Chigasaki|Tsujido|Kujukuri|Hakone/i],
    ['chubu', /Chubu|Yamanashi|Shizuoka|Aichi|Izu|Hokuriku|Fukui|중부|야마나시|시즈오카|아이치|이즈|中部|山梨|静岡|Motosu|Fujikawaguchiko|Oshima|Ito|Shimoda|Ohsezaki|Iso/i],
    ['kansai', /Kansai|Kyoto|Osaka|Hyogo|Nara|Wakayama|Mie|간사이|교토|오사카|와카야마|미에|関西|京都|大阪|和歌山/i],
    ['chugoku', /Chugoku|Onomichi|Imabari|Hiroshima|Okayama|Tottori|Shimane|Setouchi|주고쿠|오노미치|이마바리|히로시마|세토우치|中国|尾道|今治/i],
    ['shikoku', /Shikoku|Kochi|Tokushima|Ehime|Kagawa|시코쿠|고치|도쿠시마|四国|高知|徳島|Irisaki/i],
    ['kyushu', /Kyushu|Kagoshima|Miyazaki|Oita|Fukuoka|Nagasaki|Kumamoto|큐슈|규슈|가고시마|미야자키|九州|鹿児島|Yakushima|Amami/i],
    ['okinawa', /Okinawa|Miyako|Ishigaki|Kerama|Yonaguni|Yomitan|오키나와|미야코|이시가키|케라마|요나구니|沖縄|宮古|石垣|与那国/i],
];

const REGION_ALIASES = {
    miyagi: 'tohoku', akita: 'tohoku', iwate: 'tohoku', aomori: 'tohoku',
    yamagata: 'tohoku', fukushima: 'tohoku',
    chiba: 'kanto', tokyo: 'kanto', kanagawa: 'kanto', saitama: 'kanto',
    ibaraki: 'kanto', shonan: 'kanto',
    yamanashi: 'chubu', shizuoka: 'chubu', aichi: 'chubu', izu: 'chubu',
    hokuriku: 'chubu', fukui: 'chubu',
    mie: 'kansai', kyoto: 'kansai', osaka: 'kansai', hyogo: 'kansai',
    nara: 'kansai', wakayama: 'kansai',
    hiroshima: 'chugoku', okayama: 'chugoku', tottori: 'chugoku',
    shimane: 'chugoku', yamaguchi: 'chugoku', setouchi: 'chugoku',
    tokushima: 'shikoku', ehime: 'shikoku', kochi: 'shikoku', kagawa: 'shikoku',
    fukuoka: 'kyushu', miyazaki: 'kyushu', kumamoto: 'kyushu',
    kagoshima: 'kyushu', nagasaki: 'kyushu', oita: 'kyushu', saga: 'kyushu',
};

const REGION_COLLAPSE = {
    tochigi: 'kanto',
    gunma: 'kanto',
    gifu: 'chubu',
    nagano: 'chubu',
    niigata: 'chubu',
    kansai: 'chubu',
    shikoku: 'chugoku',
    kyushu: 'chugoku',
    tohoku: 'kanto',
    chugoku: 'kansai',
    kanto: 'chubu',
    okinawa: 'kyushu',
};

export function canonicalizeRegionKey(key) {
    const k = String(key || '').trim().toLowerCase();
    if (!k || k === 'all') return 'other';
    return REGION_ALIASES[k] || k;
}

export function knownRegionKeys(activity) {
    return new Set(
        (REGIONS_BY_ACTIVITY[activity] || [])
            .map(r => r.key)
            .filter(k => k !== 'all' && k !== 'other')
    );
}

export function fitRegionToActivity(activity, key) {
    let current = canonicalizeRegionKey(key);
    const allowed = knownRegionKeys(activity);
    if (!allowed.size) return current;
    const seen = new Set();
    while (!allowed.has(current) && !seen.has(current)) {
        seen.add(current);
        const next = REGION_COLLAPSE[current];
        if (!next || next === current) break;
        current = next;
    }
    return allowed.has(current) ? current : current;
}

export function parseRegionKey(address, explicitRegion) {
    if (explicitRegion && typeof explicitRegion === 'object') {
        const key = explicitRegion.sido || explicitRegion.key;
        if (key && key !== 'all') return String(key).toLowerCase();
    } else if (explicitRegion && explicitRegion !== 'all') {
        return String(explicitRegion).toLowerCase();
    }
    const text = String(address || '');
    for (const [key, re] of REGION_RULES) {
        if (re.test(text)) return key;
    }
    return 'other';
}

export function withRegion(item, activity) {
    const act = activity || itemActivity(item);
    const raw = parseRegionKey(item?.address, item?.region);
    const key = fitRegionToActivity(act, raw);
    item.region = { sido: key, district: null };
    return item;
}

export function matchesRegionFilter(region, regionFilter, activity) {
    if (!regionFilter || regionFilter === 'all') return true;
    if (!region) return false;
    const sido = typeof region === 'string' ? region : region.sido;
    return sido === regionFilter;
}

export function itemActivity(item) {
    const raw = String(item?.activity || '').toLowerCase();
    if (raw) return raw;
    const cats = item?.categories || [];
    for (const c of cats) {
        const s = String(c).toLowerCase();
        if (s.includes('ski')) return 'ski';
        if (s.includes('surf')) return 'surf';
        if (s.includes('dive') || s.includes('scuba')) return 'dive';
        if (s.includes('camp')) return 'camp';
    }
    return '';
}

export function matchesActivityFilter(item, activityFilter) {
    if (!activityFilter || activityFilter === 'all') return true;
    return itemActivity(item) === activityFilter;
}

export function regionsForActivity(activity) {
    return REGIONS_BY_ACTIVITY[activity] || [{ key: 'all', label: 'All', countId: 'count-region-all' }];
}

export function activityPath(activity, region = 'all') {
    if (!region || region === 'all') return `/${activity}`;
    return `/${activity}/${region}`;
}
