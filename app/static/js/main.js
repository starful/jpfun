/**
 * JPFun activity map — one activity, region filters, SEO paths /ski/hokkaido
 */

import {
    matchesActivityFilter,
    matchesRegionFilter,
    regionsForActivity,
    activityPath,
    withRegion,
} from './regions.js';
import {
    initGoogleMap,
    renderClinicMarkers,
    renderNearbyMarkers,
    filterMapByClinicIds,
    closeInfoWindow,
    focusClinicById,
} from './map-core.js';

const mapRoot = document.getElementById('map');
const currentActivity = (mapRoot?.dataset.activity || 'ski').toLowerCase();
const regionFilters = regionsForActivity(currentActivity);

const params = new URLSearchParams(window.location.search);
let currentLang = params.get('lang') || document.documentElement.lang || 'en';
if (!['en', 'ko'].includes(currentLang)) currentLang = 'en';

let outdoorItems = [];
let currentRegion = (mapRoot?.dataset.region || 'all').toLowerCase();

function itemBaseId(item) {
    return String(item?.id || item?.base_id || '').replace(/_(en|ko)$/i, '');
}

function langSuffix(path) {
    if (currentLang === 'en') return path;
    const join = path.includes('?') ? '&' : '?';
    return `${path}${join}lang=${currentLang}`;
}

async function loadItems(lang) {
    const qs = new URLSearchParams({ lang, activity: currentActivity });
    const res = await fetch(`/api/items?${qs}`);
    const data = await res.json();
    const key = Object.keys(data).find(k => Array.isArray(data[k]));
    const items = data[key] || [];
    outdoorItems = items
        .filter(i => matchesActivityFilter(i, currentActivity))
        .map(withRegion);

    const el = document.getElementById('last-updated-date');
    if (el) el.textContent = data.last_updated || '';
}

function filteredItems() {
    return outdoorItems.filter(item =>
        matchesRegionFilter(item.region, currentRegion)
    );
}

async function initApp() {
    try {
        await loadItems(currentLang);
        const mapId = mapRoot?.dataset.mapId || '';
        await initGoogleMap(mapId);
        bindFilterButtons();
        syncActiveFilterButton();
        await updateUI();
    } catch (err) {
        console.error('JPFun activity map failed', err);
    }
}

async function updateUI() {
    const items = filteredItems();
    renderList(items);
    await renderClinicMarkers(items);
    await renderNearbyMarkers([]);
    filterMapByClinicIds(items.map(itemBaseId), {
        scope: currentRegion === 'all' ? 'all' : 'sido',
    });
    updateCounts();
}

function activityEmoji() {
    if (currentActivity === 'ski') return '⛷️';
    if (currentActivity === 'surf') return '🏄';
    if (currentActivity === 'dive') return '🤿';
    if (currentActivity === 'camp') return '🏕️';
    return '🎉';
}

function renderList(data) {
    const container = document.getElementById('item-list');
    if (!container) return;

    if (data.length === 0) {
        container.innerHTML = `
            <div style="grid-column:1/-1; text-align:center; padding:100px 0; color:#999;">
                <p style="font-size:1.2rem;">No spots in this region.</p>
            </div>`;
        return;
    }

    const emoji = activityEmoji();
    container.innerHTML = data.map(item => `
        <div class="onsen-card" data-resort-id="${item.id || ''}">
            <a href="${item.link}">
                <img src="${item.thumbnail}" class="card-thumb" alt="${item.title}" loading="lazy"
                     onerror="this.src='/static/images/default.jpg'">
            </a>
            <div class="card-content">
                <h3 class="card-title"><a href="${item.link}">${emoji} ${item.title}</a></h3>
                <p class="card-summary">${item.summary || ''}</p>
                <div class="card-meta">
                    <span>📍 ${item.address || ''}</span>
                    <span>📅 ${item.published || item.date || ''}</span>
                </div>
                <button type="button" class="card-map-focus" data-resort-id="${item.id || ''}">Show on map</button>
            </div>
        </div>
    `).join('');

    container.querySelectorAll('.card-map-focus').forEach(btn => {
        btn.addEventListener('click', () => {
            const id = btn.dataset.resortId;
            if (!id || !focusClinicById(id)) return;
            document.getElementById('map')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });
}

function updateCounts() {
    const totalEl = document.getElementById('total-items');
    if (totalEl) totalEl.textContent = String(filteredItems().length);

    for (const btn of regionFilters) {
        const el = document.getElementById(btn.countId);
        if (!el) continue;
        if (btn.key === 'all') {
            el.textContent = String(outdoorItems.length);
            continue;
        }
        el.textContent = String(
            outdoorItems.filter(i => matchesRegionFilter(i.region, btn.key)).length
        );
    }
}

function syncActiveFilterButton() {
    document
        .querySelectorAll('.theme-filter-buttons[data-level="region"] .theme-button')
        .forEach(b => {
            const key = b.dataset.region || 'all';
            b.classList.toggle('active', key === currentRegion);
        });
}

function bindFilterButtons() {
    document.querySelectorAll('.theme-filter-buttons[data-level="region"] .theme-button').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault();
            const next = btn.dataset.region || 'all';
            currentRegion = next;
            const path = langSuffix(activityPath(currentActivity, next));
            window.history.pushState({ activity: currentActivity, region: next }, '', path);
            if (mapRoot) mapRoot.dataset.region = next;
            syncActiveFilterButton();
            closeInfoWindow();
            await updateUI();
            if (window.innerWidth < 768) {
                document.getElementById('list-section')?.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

window.addEventListener('popstate', async () => {
    const parts = window.location.pathname.replace(/\/+$/, '').split('/').filter(Boolean);
    currentRegion = (parts[1] || 'all').toLowerCase();
    if (mapRoot) mapRoot.dataset.region = currentRegion;
    syncActiveFilterButton();
    closeInfoWindow();
    await updateUI();
});

document.querySelectorAll('.lang-btn[data-lang]').forEach(btn => {
    btn.addEventListener('click', async () => {
        // full navigation via <a href> — no SPA lang switch on activity pages
    });
});

if (mapRoot) initApp();
