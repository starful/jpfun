(function () {
  var root = document.querySelector("[data-hero-slider]");
  if (!root) return;

  var slides = Array.prototype.slice.call(root.querySelectorAll(".lp-hero-img"));
  var dots = Array.prototype.slice.call(root.querySelectorAll("[data-hero-dot]"));
  if (slides.length < 2) return;

  var index = 0;
  var timer = null;
  var INTERVAL = 5500;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function show(next) {
    index = (next + slides.length) % slides.length;
    slides.forEach(function (img, i) {
      img.classList.toggle("is-active", i === index);
    });
    dots.forEach(function (dot, i) {
      var on = i === index;
      dot.classList.toggle("is-active", on);
      dot.setAttribute("aria-selected", on ? "true" : "false");
    });
  }

  function next() {
    show(index + 1);
  }

  function prev() {
    show(index - 1);
  }

  function stop() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  function start() {
    if (reduceMotion) return;
    stop();
    timer = setInterval(next, INTERVAL);
  }

  var prevBtn = root.querySelector("[data-hero-prev]");
  var nextBtn = root.querySelector("[data-hero-next]");
  if (prevBtn) {
    prevBtn.addEventListener("click", function () {
      prev();
      start();
    });
  }
  if (nextBtn) {
    nextBtn.addEventListener("click", function () {
      next();
      start();
    });
  }
  dots.forEach(function (dot) {
    dot.addEventListener("click", function () {
      var i = parseInt(dot.getAttribute("data-hero-dot"), 10);
      if (!isNaN(i)) show(i);
      start();
    });
  });

  root.addEventListener("mouseenter", stop);
  root.addEventListener("mouseleave", start);
  root.addEventListener("focusin", stop);
  root.addEventListener("focusout", function (e) {
    if (!root.contains(e.relatedTarget)) start();
  });

  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stop();
    else start();
  });

  // light swipe on touch
  var touchX = null;
  root.addEventListener(
    "touchstart",
    function (e) {
      touchX = e.changedTouches[0].clientX;
    },
    { passive: true }
  );
  root.addEventListener(
    "touchend",
    function (e) {
      if (touchX == null) return;
      var dx = e.changedTouches[0].clientX - touchX;
      touchX = null;
      if (Math.abs(dx) < 40) return;
      if (dx < 0) next();
      else prev();
      start();
    },
    { passive: true }
  );

  start();
})();
