/* Legacy EMS — interaction + light engine */
(() => {
  const html = document.documentElement;
  html.classList.remove("no-js");
  html.classList.add("js");
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced) html.classList.add("reduced");
  const hasGSAP = typeof window.gsap !== "undefined";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------------------------------------------------------------- grain */
  (() => {
    const c = document.createElement("canvas");
    c.width = c.height = 160;
    const x = c.getContext("2d");
    const d = x.createImageData(160, 160);
    for (let i = 0; i < d.data.length; i += 4) {
      const v = Math.random() * 255;
      d.data[i] = d.data[i + 1] = d.data[i + 2] = v;
      d.data[i + 3] = 255;
    }
    x.putImageData(d, 0, 0);
    html.style.setProperty("--grain", `url(${c.toDataURL()})`);
  })();

  /* object-fit: cover mapping — image-normalised point -> element pixels */
  function coverPoint(img, box, nx, ny) {
    const iw = img.naturalWidth || 1, ih = img.naturalHeight || 1;
    const bw = box.width, bh = box.height;
    const s = Math.max(bw / iw, bh / ih);
    const dw = iw * s, dh = ih * s;
    const pos = getComputedStyle(img).objectPosition.split(" ");
    const px = parseFloat(pos[0]) / 100, py = parseFloat(pos[1] ?? "50%") / 100;
    const ox = (bw - dw) * (isNaN(px) ? 0.5 : px);
    const oy = (bh - dh) * (isNaN(py) ? 0.5 : py);
    return { x: ox + nx * dw, y: oy + ny * dh, s };
  }

  /* ------------------------------------------------------------- header */
  const header = $(".site-header");
  const firstDark = $(".hero, .page-hero");
  const setHeader = () => {
    const limit = firstDark ? firstDark.offsetHeight - 90 : 0;
    header?.classList.toggle("is-solid", scrollY > Math.min(limit, 120) || !firstDark);
    const under = document.elementsFromPoint(innerWidth / 2, (header?.offsetHeight || 64) + 2)
      .find(el => !header.contains(el));
    header?.classList.toggle("on-dark", !!under?.closest(".dark, .fleet, .night-band, .forest, .hero, .page-hero, .cta-band, .site-footer"));
  };
  addEventListener("scroll", setHeader, { passive: true });
  setHeader();

  const menuBtn = $(".menu-btn");
  menuBtn?.addEventListener("click", () => {
    const open = !html.classList.contains("menu-open");
    html.classList.toggle("menu-open", open);
    menuBtn.setAttribute("aria-expanded", open);
    $(".mobile-sheet")?.setAttribute("aria-hidden", !open);
    if (window.__lenis) open ? window.__lenis.stop() : window.__lenis.start();
  });
  $$(".mobile-sheet a").forEach(a => a.addEventListener("click", () => html.classList.remove("menu-open")));
  addEventListener("keydown", e => {
    if (e.key === "Escape" && html.classList.contains("menu-open")) menuBtn.click();
  });

  const callbar = $(".callbar");
  const setCallbar = () => callbar?.classList.toggle("is-visible", scrollY > 260 && !html.classList.contains("menu-open"));
  addEventListener("scroll", setCallbar, { passive: true });
  setCallbar();

  /* ------------------------------------------------------ smooth scroll */
  if (hasGSAP && window.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);
  if (!reduced && window.Lenis && hasGSAP) {
    const lenis = new Lenis({ lerp: 0.11, smoothWheel: true });
    window.__lenis = lenis;
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    $$('a[href^="#"]').forEach(a => a.addEventListener("click", e => {
      const t = $(a.getAttribute("href"));
      if (t) { e.preventDefault(); lenis.scrollTo(t, { offset: -70 }); }
    }));
  }

  /* ========================================================= LIGHT ENGINE
     Composites emergency lighting onto the real photograph: an LED lightbar
     with a fast-attack / exponential-decay flash, bloom, an anamorphic lens
     streak, spill light washing the paint and road, and dust in the air that
     only shows when a flash catches it. Canvas is screen-blended over the
     photo, so light only ever adds — the way real light does. */
  class LightRig {
    constructor(canvas, img, cfg) {
      this.c = canvas; this.img = img; this.cfg = cfg;
      this.x = canvas.getContext("2d");
      this.dpr = Math.min(devicePixelRatio || 1, 1.5);
      this.t0 = performance.now();
      this.motes = Array.from({ length: cfg.motes ?? 90 }, () => ({
        x: Math.random(), y: Math.random() * 0.75, r: Math.random() * 1.6 + 0.4,
        vx: (Math.random() - 0.5) * 0.004, vy: -Math.random() * 0.006 - 0.001, a: Math.random()
      }));
      this.visible = true;
      this.resize = this.resize.bind(this);
      addEventListener("resize", this.resize);
      new IntersectionObserver(([e]) => { this.visible = e.isIntersecting; }).observe(canvas);
      this.resize();
      const loop = now => { if (this.visible) this.draw(now); requestAnimationFrame(loop); };
      requestAnimationFrame(loop);
    }
    resize() {
      const r = this.c.getBoundingClientRect();
      this.w = r.width; this.h = r.height;
      this.c.width = Math.round(r.width * this.dpr);
      this.c.height = Math.round(r.height * this.dpr);
      this.box = { width: r.width, height: r.height };
    }
    // LED envelope: on-windows within a cycle, 8ms attack, ~55ms decay tail
    env(t, windows) {
      let v = 0;
      for (const [a, b] of windows) {
        if (t >= a && t <= b) v = Math.max(v, Math.min(1, (t - a) / 0.008));
        else if (t > b) v = Math.max(v, Math.exp(-(t - b) / 0.055));
      }
      return v;
    }
    radial(x, y, r, stops, sx = 1, sy = 1) {
      const g = this.x;
      g.save();
      g.translate(x, y); g.scale(sx, sy);
      const grad = g.createRadialGradient(0, 0, 0, 0, 0, r);
      stops.forEach(([o, c]) => grad.addColorStop(o, c));
      g.fillStyle = grad;
      g.beginPath(); g.arc(0, 0, r, 0, Math.PI * 2); g.fill();
      g.restore();
    }
    draw(now) {
      const g = this.x, W = this.w, H = this.h, cfg = this.cfg;
      const time = window.__lightT ?? (now - this.t0) / 1000; // __lightT: freeze for screenshots
      g.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
      g.clearRect(0, 0, W, H);
      g.globalCompositeOperation = "lighter";
      const unit = Math.max(W, H);
      const cyc = cfg.cycle ?? 0.92;
      const t = (time % cyc) / cyc * cyc; // seconds into cycle

      let totalFlash = 0;
      const lit = [];
      for (const L of cfg.lights) {
        const p = coverPoint(this.img, this.box, L.x, L.y);
        const I = (reduced ? 0.35 : this.env(t, L.on)) * (cfg.gain ?? 1);
        totalFlash += I;
        lit.push({ ...p, I, col: L.col });
        if (I < 0.01) continue;
        const [r, gg, b] = L.col;
        // 1. spill: the whole scene picks up the colour
        this.radial(p.x, p.y, unit * 0.95, [[0, `rgba(${r},${gg},${b},${Math.min(1, 0.20 * I * (cfg.spill ?? 1))})`], [0.35, `rgba(${r},${gg},${b},${Math.min(1, 0.07 * I * (cfg.spill ?? 1))})`], [1, "rgba(0,0,0,0)"]]);
        // 2. bloom around the lens
        this.radial(p.x, p.y, unit * 0.16, [[0, `rgba(${r},${gg},${b},${0.75 * I})`], [0.25, `rgba(${r},${gg},${b},${0.28 * I})`], [1, "rgba(0,0,0,0)"]]);
        // 3. anamorphic streak
        this.radial(p.x, p.y, unit * 0.05, [[0, `rgba(255,255,255,${0.55 * I})`], [0.2, `rgba(${r},${gg},${b},${0.45 * I})`], [1, "rgba(0,0,0,0)"]], 9, 0.12);
        // 4. hot core
        this.radial(p.x, p.y, unit * 0.014, [[0, `rgba(255,255,255,${I})`], [0.4, `rgba(255,${Math.min(255, gg + 160)},${Math.min(255, b + 160)},${0.85 * I})`], [1, "rgba(0,0,0,0)"]]);
        // 5. road reflection
        if (cfg.ground) {
          const gp = coverPoint(this.img, this.box, L.x + (cfg.ground.dx || 0), cfg.ground.y);
          this.radial(gp.x, gp.y, unit * 0.22, [[0, `rgba(${r},${gg},${b},${0.16 * I})`], [1, "rgba(0,0,0,0)"]], 1.8, 0.35);
        }
      }

      // underglow breathing (the car's own green neon)
      for (const u of cfg.glow || []) {
        const p = coverPoint(this.img, this.box, u.x, u.y);
        const k = 0.55 + 0.45 * Math.sin(time * 1.6 + u.ph);
        this.radial(p.x, p.y, unit * u.r, [[0, `rgba(70,255,120,${0.16 * k})`], [1, "rgba(0,0,0,0)"]], 2.2, 0.5);
      }

      // airborne dust — invisible until a flash catches it
      if (!reduced) {
        for (const m of this.motes) {
          m.x += m.vx * 0.016; m.y += m.vy * 0.016;
          if (m.y < -0.05) { m.y = 0.8; m.x = Math.random(); }
          if (m.x < -0.05) m.x = 1.05; if (m.x > 1.05) m.x = -0.05;
          const mx = m.x * W, my = m.y * H;
          let catchLight = 0, cr = 255, cg = 255, cb = 255;
          for (const l of lit) {
            const d = Math.hypot(mx - l.x, my - l.y) / unit;
            const k = l.I * Math.max(0, 1 - d / 0.45);
            if (k > catchLight) { catchLight = k; [cr, cg, cb] = l.col; }
          }
          const a = 0.05 + catchLight * 0.9 * m.a;
          if (a < 0.03) continue;
          g.fillStyle = `rgba(${Math.min(255, cr + 90)},${Math.min(255, cg + 90)},${Math.min(255, cb + 90)},${a})`;
          g.beginPath(); g.arc(mx, my, m.r, 0, Math.PI * 2); g.fill();
        }
      }
      this.flash = totalFlash;
      g.globalCompositeOperation = "source-over";
    }
  }

  const rig = $("[data-lightrig]");
  if (rig) {
    const img = rig.querySelector("img");
    const canvas = rig.querySelector("canvas");
    const preset = {
      // Mfezi — VW Golf R response car. Lightbar spans the roof.
      mfezi: {
        cycle: 0.96,
        lights: [
          { x: 0.288, y: 0.214, col: [255, 28, 34], on: [[0.00, 0.055], [0.10, 0.155], [0.20, 0.245]] },
          { x: 0.315, y: 0.213, col: [255, 60, 50], on: [[0.02, 0.06], [0.12, 0.16]] },
          { x: 0.395, y: 0.220, col: [150, 190, 255], on: [[0.48, 0.535], [0.58, 0.635], [0.68, 0.725]] },
          { x: 0.422, y: 0.226, col: [255, 28, 34], on: [[0.50, 0.54], [0.60, 0.64]] },
          { x: 0.355, y: 0.217, col: [255, 255, 255], on: [[0.355, 0.385], [0.86, 0.885]] }
        ],
        ground: { y: 0.86, dx: 0.1 },
        glow: [{ x: 0.24, y: 0.76, r: 0.12, ph: 0 }, { x: 0.68, y: 0.92, r: 0.14, ph: 1.4 }],
        motes: 110
      },
      // a vehicle parked just out of frame: only its light reaches the shot
      offscreen: {
        cycle: 1.1, gain: 0.9, spill: 3,
        lights: [
          { x: -0.04, y: 0.08, col: [255, 30, 40], on: [[0.00, 0.05], [0.09, 0.14], [0.18, 0.23]] },
          { x: 1.04, y: 0.1, col: [120, 160, 255], on: [[0.50, 0.55], [0.59, 0.64], [0.68, 0.73]] }
        ],
        motes: 60
      }
    }[rig.dataset.lightrig];
    const start = () => new LightRig(canvas, img, preset);
    img.complete ? start() : img.addEventListener("load", start, { once: true });
  }

  /* beacon placement on the night band */
  const beaconImg = $("[data-beacon] img");
  if (beaconImg) {
    const host = beaconImg.closest("[data-beacon]");
    const [bx, by] = host.dataset.beacon.split(",").map(Number);
    const place = () => {
      const r = host.getBoundingClientRect();
      const p = coverPoint(beaconImg, r, bx, by);
      host.style.setProperty("--bx", `${p.x}px`);
      host.style.setProperty("--by", `${p.y}px`);
    };
    beaconImg.complete ? place() : beaconImg.addEventListener("load", place);
    addEventListener("resize", place);
  }

  /* ---------------------------------------------------------- home intro */
  const heroNum = $(".hero-num[data-split]");
  if (heroNum) {
    const text = heroNum.textContent.trim();
    heroNum.setAttribute("aria-label", heroNum.getAttribute("aria-label") || text);
    heroNum.innerHTML = [...text].map(ch => ch === " " ? '<span class="gap"></span>' : `<span class="ch" aria-hidden="true">${ch}</span>`).join("");
  }
  const curtain = $(".curtain");
  if (hasGSAP && !reduced) {
    const tl = gsap.timeline({ defaults: { ease: "expo.out" } });
    if (curtain) {
      const path = curtain.querySelector("path");
      const len = path.getTotalLength();
      gsap.set(path, { strokeDasharray: len, strokeDashoffset: len });
      tl.to(path, { strokeDashoffset: 0, duration: 1.1, ease: "power2.inOut" })
        .to(curtain, { clipPath: "inset(0 0 100% 0)", duration: 0.9, ease: "expo.inOut" }, "+=0.05")
        .set(curtain, { display: "none" });
    }
    const media = $(".hero .hero-media, .page-hero .hero-media");
    if (media) tl.fromTo(media, { scale: 1.18 }, { scale: 1.04, duration: 2.6, ease: "power3.out" }, curtain ? "-=0.8" : 0);
    if (heroNum) tl.from($$(".ch", heroNum), { yPercent: 110, opacity: 0, duration: 1.1, stagger: 0.035 }, "-=2.1");
    const fadeIns = $$(".hero [data-in], .page-hero [data-in]");
    if (fadeIns.length) tl.from(fadeIns, { y: 24, opacity: 0, duration: 1, stagger: 0.08 }, heroNum ? "-=0.8" : "-=2");
  } else if (curtain) curtain.remove();

  /* ------------------------------------------------------ scroll effects */
  if (hasGSAP && window.ScrollTrigger && !reduced) {
    // hero parallax + fade
    $$(".hero, .page-hero, .night-band").forEach(sec => {
      const m = sec.querySelector(".hero-media");
      if (m) gsap.to(m, { yPercent: 14, ease: "none", scrollTrigger: { trigger: sec, start: "top top", end: "bottom top", scrub: true } });
    });
    // aperture reveal on photographs
    $$(".reveal-img").forEach(el => {
      const img = el.querySelector("img");
      gsap.to(el, { clipPath: "inset(0% 0% 0% 0% round 18px)", ease: "power2.out", scrollTrigger: { trigger: el, start: "top 88%", end: "top 35%", scrub: 0.8 } });
      if (img) gsap.fromTo(img, { scale: 1.25 }, { scale: 1, ease: "none", scrollTrigger: { trigger: el, start: "top bottom", end: "bottom top", scrub: true } });
    });
    // specular sweep across paint, driven by scroll
    $$(".sheen").forEach(el => {
      gsap.fromTo(el, { "--sheen": "-70%" }, { "--sheen": "70%", ease: "none", scrollTrigger: { trigger: el, start: "top 90%", end: "bottom 10%", scrub: true } });
    });
    // fleet: pinned horizontal run on wide screens
    const mm = gsap.matchMedia();
    mm.add("(min-width: 761px)", () => {
      const track = $(".fleet-track");
      if (!track) return;
      const dist = () => track.scrollWidth - innerWidth;
      gsap.to(track, {
        x: () => -dist(), ease: "none",
        scrollTrigger: { trigger: ".fleet", start: "top top", end: () => "+=" + dist(), pin: true, scrub: 0.6, invalidateOnRefresh: true, anticipatePin: 1 }
      });
      $$(".unit-photo img", track).forEach(img => {
        gsap.fromTo(img, { xPercent: -6 }, { xPercent: 6, ease: "none", scrollTrigger: { trigger: ".fleet", start: "top top", end: () => "+=" + dist(), scrub: true } });
      });
    });
    // ECG line in CTA bands
    $$(".ecg path").forEach(p => {
      const len = p.getTotalLength();
      gsap.fromTo(p, { strokeDasharray: len, strokeDashoffset: len }, { strokeDashoffset: 0, ease: "none", scrollTrigger: { trigger: p.closest("section"), start: "top 80%", end: "bottom 60%", scrub: 1 } });
    });
    addEventListener("load", () => ScrollTrigger.refresh());
  }

  /* --------------------------------------- service index floating photo */
  const svcList = $(".svc-index");
  const float = $(".svc-float");
  if (svcList && float && matchMedia("(hover: hover) and (min-width: 761px)").matches) {
    let tx = 0, ty = 0, x = 0, y = 0, active = false;
    const imgs = $$("img", float);
    svcList.addEventListener("pointermove", e => { tx = e.clientX; ty = e.clientY; });
    $$("a", svcList).forEach((a, i) => {
      a.addEventListener("pointerenter", () => {
        active = true; float.style.opacity = 1; float.style.scale = "1.18";
        imgs.forEach((im, j) => im.classList.toggle("on", j === i));
      });
    });
    svcList.addEventListener("pointerleave", () => { active = false; float.style.opacity = 0; float.style.scale = "1"; });
    const tick = () => {
      x += (tx - x) * 0.14; y += (ty - y) * 0.14;
      const rot = Math.max(-8, Math.min(8, (tx - x) * 0.05));
      float.style.transform = `translate(${x + 30}px, ${y - 140}px) rotate(${rot}deg)`;
      requestAnimationFrame(tick);
    };
    tick();
  }

  /* ------------------------------------------------------- testimonials */
  const stage = $(".voice-stage");
  if (stage) {
    const items = $$(".voice", stage);
    const count = $(".voice-count");
    const bar = $(".voice-bar i");
    let i = 0, timer, t0;
    const DUR = 9000;
    const show = n => {
      i = (n + items.length) % items.length;
      items.forEach((v, j) => { v.classList.toggle("is-on", j === i); v.setAttribute("aria-hidden", j !== i); });
      if (count) count.textContent = `${i + 1} / ${items.length}`;
      t0 = performance.now();
    };
    const run = now => {
      const k = Math.min(1, (now - t0) / DUR);
      if (bar) bar.style.transform = `scaleX(${k})`;
      if (k >= 1 && !reduced) show(i + 1);
      timer = requestAnimationFrame(run);
    };
    $(".voice-prev")?.addEventListener("click", () => show(i - 1));
    $(".voice-next")?.addEventListener("click", () => show(i + 1));
    stage.addEventListener("pointerenter", () => cancelAnimationFrame(timer));
    stage.addEventListener("pointerleave", () => { t0 = performance.now(); timer = requestAnimationFrame(run); });
    show(0);
    timer = requestAnimationFrame(run);
  }

  /* ---------------------------------------------------------------- FAQ */
  $$(".faq details").forEach(d => {
    const body = d.querySelector(".faq-body");
    d.querySelector("summary").addEventListener("click", e => {
      if (!hasGSAP || reduced) return;
      e.preventDefault();
      if (d.open) {
        gsap.to(body, { height: 0, duration: 0.4, ease: "power2.inOut", onComplete: () => { d.open = false; gsap.set(body, { clearProps: "height" }); } });
      } else {
        d.open = true;
        gsap.from(body, { height: 0, duration: 0.5, ease: "expo.out" });
      }
    });
  });

  /* -------------------------------------------------------------- forms */
  $$("form.quote").forEach(form => {
    form.addEventListener("submit", e => {
      e.preventDefault();
      let ok = true;
      $$("[required]", form).forEach(f => {
        const wrap = f.closest(".field");
        const err = wrap?.querySelector(".err");
        let msg = "";
        if (!f.value.trim()) msg = `Enter your ${(wrap?.querySelector("label")?.textContent || "details").toLowerCase()}.`;
        else if (f.type === "email" && !/^\S+@\S+\.\S+$/.test(f.value)) msg = "Enter an email address like name@company.co.za.";
        else if (f.type === "tel" && f.value.replace(/\D/g, "").length < 9) msg = "Enter a phone number with at least 10 digits.";
        wrap?.classList.toggle("invalid", !!msg);
        if (err) err.textContent = msg;
        if (msg && ok) { f.focus(); ok = false; }
      });
      if (!ok) return;
      const data = new FormData(form);
      const lines = [];
      for (const [k, v] of data) if (v) lines.push(`${k}: ${v}`);
      const subject = form.dataset.subject || "Website enquiry";
      const done = $(".form-done", form);
      done?.classList.add("show");
      location.href = `mailto:admin@legacyems.co.za?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join("\n"))}`;
    });
  });

  /* ------------------------------------------------------------ gallery */
  const masonry = $(".masonry");
  if (masonry) {
    const figs = $$("figure", masonry);
    $$(".gallery-filter button").forEach(b => b.addEventListener("click", () => {
      $$(".gallery-filter button").forEach(x => x.setAttribute("aria-pressed", x === b));
      const f = b.dataset.filter;
      figs.forEach(fig => fig.classList.toggle("hide", f !== "all" && !fig.dataset.tags.includes(f)));
      if (hasGSAP && !reduced) gsap.from(figs.filter(x => !x.classList.contains("hide")), { opacity: 0, y: 20, duration: 0.5, stagger: 0.03, ease: "power2.out" });
      window.ScrollTrigger?.refresh();
    }));
    const lb = $(".lightbox");
    const lbImg = $("img", lb), lbCap = $("p", lb), lbClose = $("button", lb);
    let lastFocus;
    const open = fig => {
      lastFocus = fig;
      const im = $("img", fig);
      lbImg.src = im.currentSrc || im.src; lbImg.alt = im.alt;
      lbCap.textContent = $("figcaption", fig)?.textContent || "";
      lb.classList.add("open"); lb.setAttribute("aria-hidden", "false");
      window.__lenis?.stop(); lbClose.focus();
    };
    const close = () => { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); window.__lenis?.start(); lastFocus?.focus(); };
    figs.forEach(fig => {
      fig.addEventListener("click", () => open(fig));
      fig.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(fig); } });
    });
    lbClose.addEventListener("click", close);
    lb.addEventListener("click", e => { if (e.target === lb) close(); });
    addEventListener("keydown", e => { if (e.key === "Escape" && lb.classList.contains("open")) close(); });
  }

  /* concept notice: dismiss for this visit */
  const badge = $(".concept-badge");
  try { if (sessionStorage.getItem("concept-hidden")) badge?.classList.add("is-hidden"); } catch (e) {}
  badge?.querySelector("button")?.addEventListener("click", () => {
    badge.classList.add("is-hidden");
    try { sessionStorage.setItem("concept-hidden", "1"); } catch (e) {}
  });

  /* year */
  $$("[data-year]").forEach(el => (el.textContent = new Date().getFullYear()));
})();
