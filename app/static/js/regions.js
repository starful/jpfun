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
    ],
    surf: [
        { key: 'all', label: 'All', countId: 'count-region-all' },
        { key: 'kanto', label: 'Kanto', countId: 'count-region-kanto' },
        { key: 'okinawa', label: 'Okinawa', countId: 'count-region-okinawa' },
    ],
    dive: [
        { key: 'all', label: 'All', countId: 'count-region-all' },
        { key: 'okinawa', label: 'Okinawa', countId: 'count-region-okinawa' },
        { key: 'chubu', label: 'Izu / Chubu', countId: 'count-region-chubu' },
    ],
    camp: [
        { key: 'all', label: 'All', countId: 'count-region-all' },
        { key: 'chubu', label: 'Chubu / Fuji', countId: 'count-region-chubu' },
        { key: 'nagano', label: 'Nagano', countId: 'count-region-nagano' },
        { key: 'chugoku', label: 'Chugoku / Shimanami', countId: 'count-region-chugoku' },
    ],
};

const REGION_RULES = [
    ['hokkaido', /Hokkaido|홋카이도|北海道/i],
    ['nagano', /Nagano|나가노|長野/i],
    ['niigata', /Niigata|니가타|新潟/i],
    ['tohoku', /Tohoku|Yamagata|Iwate|Fukushima|도호쿠|야마가타|이와테|후쿠시마|東北|山形|岩手|福島/i],
    ['kanto', /Kanto|Tokyo|Kanagawa|Chiba|Ibaraki|도쿄|가나가와|치바|이바라키|関東|東京|神奈川|千葉|茨城|Fujisawa|Oarai|Isumi|Oshima/i],
    ['chubu', /Chubu|Yamanashi|Shizuoka|Gifu|중부|야마나시|시즈오카|기후|中部|山梨|静岡|岐阜|Motosu|Fujikawaguchiko|Oshima/i],
    ['chugoku', /Chugoku|Onomichi|Imabari|Hiroshima|Ehime|주고쿠|오노미치|이마바리|中国|尾道|今治/i],
    ['okinawa', /Okinawa|Miyako|Ishigaki|Kerama|오키나와|미야코|이시가키|케라마|沖縄|宮古|石垣/i],
];

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

export function withRegion(item) {
    const explicit = item?.region;
    const key = parseRegionKey(item?.address, explicit);
    item.region = { sido: key, district: null };
    return item;
}

export function matchesRegionFilter(region, regionFilter) {
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
