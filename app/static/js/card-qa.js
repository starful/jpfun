(function () {
    var THUMB_RATIO = 3 / 2;
    var RATIO_TOLERANCE = 0.2;

    function qaModeEnabled() {
        return /(?:^|[?&])qa=1(?:&|$)/.test(window.location.search);
    }

    function checkGridThumb(img) {
        if (!img.naturalWidth || !img.naturalHeight) return;
        var ratio = img.naturalWidth / img.naturalHeight;
        var offTarget = Math.abs(ratio - THUMB_RATIO) / THUMB_RATIO > RATIO_TOLERANCE;
        img.classList.toggle("card-thumb--ratio-warn", offTarget);
        if (offTarget) {
            console.warn(
                "[card-qa] thumbnail ratio off target (3:2 expected):",
                img.currentSrc || img.src,
                ratio.toFixed(2)
            );
        }
    }

    // Spot/guide card thumbnails: only audited when a reviewer opts in with
    // ?qa=1, so regular visitors never see the debug outline.
    if (qaModeEnabled()) {
        document.querySelectorAll(".card-thumb").forEach(function (img) {
            if (img.complete) checkGridThumb(img);
        });
        document.addEventListener(
            "load",
            function (event) {
                if (event.target.matches && event.target.matches(".card-thumb")) {
                    checkGridThumb(event.target);
                }
            },
            true
        );
    }

    // OG social-card size check: this page (/card/item, /card/guide) is
    // itself the pre-share preview tool, so run this unconditionally.
    function checkSocialCardSize() {
        var img = document.querySelector(".social-preview-media img");
        var note = document.querySelector(".social-preview-size-check");
        if (!img || !note) return;

        function report() {
            var w = img.naturalWidth;
            var h = img.naturalHeight;
            var declaredW = parseInt(img.getAttribute("width"), 10);
            var declaredH = parseInt(img.getAttribute("height"), 10);
            var ok = w === declaredW && h === declaredH;
            var label = ok ? note.dataset.okLabel : note.dataset.warnLabel;
            note.textContent = label
                .replace("{w}", w)
                .replace("{h}", h)
                .replace("{dw}", declaredW)
                .replace("{dh}", declaredH);
            note.classList.toggle("social-preview-size-check--ok", ok);
            note.classList.toggle("social-preview-size-check--warn", !ok);
        }

        if (img.complete) report();
        else img.addEventListener("load", report, { once: true });
    }

    checkSocialCardSize();
})();
