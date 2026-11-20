/* Spot detail page loading diagnostics: lazy-load body images + report LCP via visit_track.js */
(function () {
    "use strict";

    // Content images come from markdown and never carry loading/decoding hints.
    // Mark them lazy so they don't compete with the hero image for bandwidth.
    document.querySelectorAll(".detail-content img:not([loading])").forEach(function (img) {
        img.loading = "lazy";
        img.decoding = "async";
    });

    if (!("PerformanceObserver" in window)) return;

    var lastLcp = null;
    try {
        var po = new PerformanceObserver(function (list) {
            var entries = list.getEntries();
            var entry = entries[entries.length - 1];
            if (!entry) return;
            var ms = Math.round(entry.renderTime || entry.loadTime || 0);
            var url = (entry.url || "").replace(location.origin, "").slice(0, 100);
            // visitkit's /events only stores a fixed param whitelist (screen/href/label/kind/q),
            // so the LCP time and asset url are packed into those instead of custom keys.
            lastLcp = { label: ms + "ms", href: url, kind: "lcp" };
        });
        po.observe({ type: "largest-contentful-paint", buffered: true });
    } catch (e) {
        return;
    }

    var sent = false;
    function reportLcp() {
        if (sent || !lastLcp) return;
        sent = true;
        po.disconnect();
        if (typeof window.StarfulVisitTrack === "function") {
            window.StarfulVisitTrack("perf_lcp", lastLcp);
        }
    }

    addEventListener("pagehide", reportLcp);
    addEventListener("visibilitychange", function () {
        if (document.visibilityState === "hidden") reportLcp();
    });
})();
