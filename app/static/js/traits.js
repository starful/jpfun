/**
 * Non-region style filters (title/summary keyword tags).
 * Chip sets differ per activity — keep in sync with activities.TRAITS_BY_ACTIVITY.
 */

export const TRAITS_BY_ACTIVITY = {
    ski: [
        { key: 'all', label: 'All', countId: 'count-trait-all' },
        { key: 'beginner', label: 'Beginner', countId: 'count-trait-beginner' },
        { key: 'family', label: 'Family', countId: 'count-trait-family' },
        { key: 'powder', label: 'Powder', countId: 'count-trait-powder' },
        { key: 'onsen', label: 'Onsen', countId: 'count-trait-onsen' },
        { key: 'daytrip', label: 'Day trip', countId: 'count-trait-daytrip' },
    ],
    surf: [
        { key: 'all', label: 'All', countId: 'count-trait-all' },
        { key: 'beginner', label: 'Beginner', countId: 'count-trait-beginner' },
        { key: 'reef', label: 'Reef / Point', countId: 'count-trait-reef' },
        { key: 'daytrip', label: 'Day trip', countId: 'count-trait-daytrip' },
    ],
    dive: [
        { key: 'all', label: 'All', countId: 'count-trait-all' },
        { key: 'beginner', label: 'Beginner', countId: 'count-trait-beginner' },
        { key: 'reef', label: 'Reef', countId: 'count-trait-reef' },
        { key: 'wall', label: 'Wall / Advanced', countId: 'count-trait-wall' },
        { key: 'video', label: 'Has video', countId: 'count-trait-video' },
    ],
    camp: [
        { key: 'all', label: 'All', countId: 'count-trait-all' },
        { key: 'glamping', label: 'Glamping', countId: 'count-trait-glamping' },
        { key: 'carcamp', label: 'Car camp', countId: 'count-trait-carcamp' },
        { key: 'beginner', label: 'Beginner', countId: 'count-trait-beginner' },
        { key: 'onsen', label: 'Onsen', countId: 'count-trait-onsen' },
    ],
};

const TRAIT_RULES = {
    beginner: /beginner|초보|입문|완만|novice|\beasy\b|처음/i,
    family: /family|가족|아이\s*동반|\bkids?\b|child/i,
    powder: /powder|파우더/i,
    onsen: /onsen|온천/i,
    daytrip: /day\s*trip|당일|weekend|주말|near\s*tokyo|도쿄\s*근교|tokyo\s*day/i,
    reef: /reef|산호|coral|point\s*break|reef\s*break/i,
    wall: /wall|월\s*다이브|드롭오프|drop.?off|advanced|상급/i,
    glamping: /글램핑|glamping/i,
    carcamp: /차박|car\s*camp|vanlife|캠핑카/i,
};

function itemText(item) {
    return `${item?.title || ''}\n${item?.summary || ''}`;
}

export function detectTraits(item) {
    const text = itemText(item);
    const found = [];
    for (const [key, re] of Object.entries(TRAIT_RULES)) {
        if (re.test(text)) found.push(key);
    }
    if (String(item?.youtube_id || '').trim()) found.push('video');
    return found;
}

export function withTraits(item) {
    item.traits = detectTraits(item);
    return item;
}

export function matchesTraitFilter(traits, traitFilter) {
    if (!traitFilter || traitFilter === 'all') return true;
    if (!traits || !traits.length) return false;
    return traits.includes(traitFilter);
}

export function traitsForActivity(activity) {
    return TRAITS_BY_ACTIVITY[activity] || [{ key: 'all', label: 'All', countId: 'count-trait-all' }];
}

export function isKnownTrait(activity, key) {
    if (!key || key === 'all') return true;
    return (TRAITS_BY_ACTIVITY[activity] || []).some(t => t.key === key);
}
