(function () {
    var ACTIVITY_EMOJI = { ski: "⛷️", surf: "🏄", dive: "🤿", camp: "🏕️" };

    function cardHtml(item, lang, activity) {
        var emoji = ACTIVITY_EMOJI[activity] || "🎉";
        var meta = item.address || (item.region && item.region.sido) || "";
        var thumb = item.thumbnail || "/static/images/default.jpg";
        return (
            '<a class="related-spot-card" href="' + (item.link || "#") + '" ' +
            'data-track="related_spot_click" data-track-label="' + (item.id || "") + '">' +
                '<div class="related-spot-thumb-wrap">' +
                    '<img class="related-spot-thumb" src="' + thumb + '" alt="' + (item.title || "") +
                    '" loading="lazy" onerror="this.src=\'/static/images/default.jpg\'">' +
                '</div>' +
                '<div class="related-spot-body">' +
                    '<span class="related-spot-name">' + emoji + " " + (item.title || "") + "</span>" +
                    '<span class="related-spot-meta">' + meta + "</span>" +
                '</div>' +
            '</a>'
        );
    }

    function sortByRegion(items, region) {
        if (!region) return items;
        var same = items.filter(function (item) {
            return item.region && item.region.sido === region;
        });
        var rest = items.filter(function (item) {
            return !(item.region && item.region.sido === region);
        });
        return same.concat(rest);
    }

    function loadRelated(section) {
        var grid = section.querySelector("[data-related-spots-grid]");
        var activity = section.dataset.activity || "";
        var region = section.dataset.region || "";
        var lang = section.dataset.lang || "en";
        var excludeId = section.dataset.excludeId || "";
        if (!grid || !activity) {
            section.hidden = true;
            return;
        }

        var qs = new URLSearchParams({ lang: lang, activity: activity });
        fetch("/api/items?" + qs.toString())
            .then(function (res) {
                if (!res.ok) throw new Error("related spots fetch failed");
                return res.json();
            })
            .then(function (data) {
                var key = Object.keys(data).filter(function (k) {
                    return Array.isArray(data[k]);
                })[0];
                var items = (key ? data[key] : []).filter(function (item) {
                    return item && item.id !== excludeId;
                });
                items = sortByRegion(items, region).slice(0, 5);

                if (items.length < 3) {
                    section.hidden = true;
                    return;
                }
                grid.innerHTML = items
                    .map(function (item) {
                        return cardHtml(item, lang, activity);
                    })
                    .join("");
            })
            .catch(function () {
                section.hidden = true;
            });
    }

    document.querySelectorAll(".related-spots").forEach(loadRelated);
})();
