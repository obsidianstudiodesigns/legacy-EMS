"""Builds the static Legacy EMS site from shared partials.
Run:  python build.py   (writes *.html next to this file)"""
from pathlib import Path

ROOT = Path(__file__).parent
TEL = "+27619960911"
NUM = "061 9960 911"
EMAIL = "admin@legacyems.co.za"
FB = "https://www.facebook.com/legacyemergencyspecialists"
WA = "https://wa.me/27619960911"

I = {
    "phone": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8Z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "left": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.25-.12-1.47-.72-1.7-.8-.23-.09-.4-.13-.56.12-.17.25-.64.8-.79.97-.14.16-.29.18-.54.06a6.7 6.7 0 0 1-3.34-2.92c-.25-.43.25-.4.72-1.34.08-.16.04-.3-.02-.43l-.76-1.82c-.2-.48-.4-.41-.56-.42h-.47a.9.9 0 0 0-.66.31 2.77 2.77 0 0 0-.86 2.06 4.8 4.8 0 0 0 1 2.56 11 11 0 0 0 4.22 3.73c1.57.68 2.19.74 2.98.62.48-.07 1.47-.6 1.68-1.18.2-.58.2-1.08.14-1.18-.06-.1-.23-.17-.48-.29Z"/></svg>',
    "school": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 9l10-5 10 5-10 5L2 9Z"/><path d="M6 11v5c0 1.5 2.7 3 6 3s6-1.5 6-3v-5M22 9v6"/></svg>',
    "brief": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/></svg>',
    "music": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0V4ZM7 6H4a3 3 0 0 0 3 4M17 6h3a3 3 0 0 1-3 4"/></svg>',
    "radio": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="8" width="12" height="13" rx="2"/><path d="M9 8 15 2M10 13h4M10 17h4"/></svg>',
    "boxes": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7l9-4 9 4-9 4-9-4Z"/><path d="M3 7v10l9 4 9-4V7M12 11v10"/></svg>',
    "clinic": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21V8l9-5 9 5v13H3Z"/><path d="M12 10v6M9 13h6"/></svg>',
    "clip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V2h6v2M9 11l2 2 4-4M9 17h6"/></svg>',
    "bandage": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="8" width="20" height="8" rx="4" transform="rotate(-45 12 12)"/><path d="M10 12h.01M12 10h.01M14 12h.01M12 14h.01"/></svg>',
    "flame": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22a7 7 0 0 0 7-7c0-4-3-6-4-10-2 2-3 4-3 6-1-1-2-2-2-4-2 2-5 4.5-5 8a7 7 0 0 0 7 7Z"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 5.6a5.5 5.5 0 0 0-7.8 0L12 6.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 22l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z"/><path d="M3 12h4l2-3 3 6 2-3h7"/></svg>',
    "pulse": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12h5l2-6 4 12 2-6h7"/></svg>',
    "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M17 4a4 4 0 0 1 0 8M22 21a7 7 0 0 0-4-6.3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/></svg>',
}

NAV = [
    ("ambulances.html", "Ambulance services"),
    ("events.html", "Events"),
    ("site-medical.html", "Site medical"),
    ("training.html", "Training"),
    ("about.html", "About"),
    ("gallery.html", "Gallery"),
    ("contact.html", "Contact"),
]

ECG = "M0 80 H380 L400 80 L410 60 L420 80 L440 80 L452 20 L466 120 L478 80 L520 80 L535 66 L552 80 H900 L920 80 L930 60 L940 80 L960 80 L972 20 L986 120 L998 80 L1040 80 L1055 66 L1072 80 H1440"


def head(title, desc, extra=""):
    return f"""<!doctype html>
<html lang="en-ZA" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#050d09">
<meta name="robots" content="noindex, nofollow">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/hero-mfezi.jpg">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Saira:wdth,wght@100..125,400..800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<aside class="concept-badge" aria-label="About this site"><span>Concept redesign by Obsidian Studio Designs. Official site: <a href="https://legacyems.co.za/" rel="noopener">legacyems.co.za</a></span><button type="button" aria-label="Hide this notice">×</button></aside>
"""


def header(active):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV
    )
    mlinks = "".join(f'<a href="{h}">{t}</a>' for h, t in [("index.html", "Home")] + NAV)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      <img src="assets/img/emblem.png" alt="" width="52" height="37">
      <span class="brand-word"><b>LEGACY</b><small>EMERGENCY MEDICAL SERVICES</small></span>
    </a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <a class="btn btn--siren header-call" href="tel:{TEL}" aria-label="Call emergency line {NUM}">{I['phone']}<span class="lbl">{NUM}</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="mobile-sheet" aria-label="Menu"><span></span><span></span></button>
  </div>
</header>
<div class="mobile-sheet" id="mobile-sheet" aria-hidden="true">
  {mlinks}
  <a class="btn btn--siren" href="tel:{TEL}">{I['phone']} Call {NUM}</a>
</div>
<div class="callbar">
  <a class="btn btn--siren" href="tel:{TEL}">{I['phone']} Call {NUM}</a>
  <a class="btn btn--wa" href="{WA}" aria-label="Message us on WhatsApp">{I['wa']}</a>
</div>
"""


def footer():
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <div>
        <p class="foot-motto">Today’s footsteps, tomorrow’s Legacy.</p>
        <a class="foot-call livery-num" href="tel:{TEL}">{NUM}</a>
        <p>Legacy Emergency Medical Services (Pty) Ltd. Registered Advanced Life Support ambulance service, accredited by the Mpumalanga Department of Health. Est. 2016.</p>
      </div>
      <div><h2>Services</h2><ul>
        <li><a href="ambulances.html#emergencies">Medical &amp; trauma emergencies</a></li>
        <li><a href="ambulances.html#transfers">Interfacility transfers</a></li>
        <li><a href="events.html">Event medical cover</a></li>
        <li><a href="site-medical.html">Site &amp; industrial medical</a></li>
        <li><a href="training.html">Training courses</a></li></ul></div>
      <div><h2>Company</h2><ul>
        <li><a href="about.html">About Legacy</a></li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="{FB}" rel="noopener">Facebook</a></li></ul></div>
      <div><h2>Reach us</h2><ul>
        <li><a href="tel:{TEL}">Emergencies: 061 996 0911</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>Emalahleni (Witbank), Mpumalanga</li></ul></div>
    </div>
    <div class="foot-bottom">
      <span>© <span data-year>2026</span> Legacy Emergency Medical Services (Pty) Ltd</span>
      <span>In a life-threatening emergency, call {NUM} or 10177.</span>
      <span>Concept redesign by Obsidian Studio Designs, not affiliated with or published by Legacy EMS.</span>
    </div>
  </div>
</footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="assets/js/site.js"></script>
</body>
</html>
"""


def page_hero(img, crumb, h1, lede, pos="50% 50%", actions=""):
    return f"""<section class="page-hero grain">
  <div class="hero-media" data-lightrig="offscreen"><img src="assets/img/{img}.jpg" alt="" style="object-position:{pos}" fetchpriority="high"><canvas aria-hidden="true"></canvas></div>
  <div class="wrap hero-inner">
    <p class="crumb" data-in><a href="index.html">Home</a> / {crumb}</p>
    <h1 data-in>{h1}</h1>
    <p class="lede" data-in>{lede}</p>
    {f'<div class="hero-actions" data-in style="margin-top:2rem">{actions}</div>' if actions else ''}
  </div>
</section>
"""


def cta(h, p, ghost_href="contact.html", ghost="Request a quote"):
    return f"""<section class="cta-band section">
  <svg class="ecg" viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true"><path d="{ECG}"/></svg>
  <div class="wrap">
    <div><h2>{h}</h2><p class="lede">{p}</p></div>
    <div class="hero-actions">
      <a class="btn btn--siren pulse" href="tel:{TEL}">{I['phone']} Call {NUM}</a>
      <a class="btn btn--ghost" href="{ghost_href}">{ghost}</a>
    </div>
  </div>
</section>
"""


def field(name, label, kind="text", req=True, full=False, ph="", opts=None, auto=""):
    r = " required" if req else ""
    cls = "field full" if full else "field"
    fid = f"f-{name.lower().replace(' ', '-')}"
    a = f' autocomplete="{auto}"' if auto else ""
    if kind == "textarea":
        ctl = f'<textarea id="{fid}" name="{name}" placeholder="{ph}"{r}></textarea>'
    elif kind == "select":
        o = "".join(f"<option>{x}</option>" for x in opts)
        ctl = f'<select id="{fid}" name="{name}"{r}>{o}</select>'
    else:
        ctl = f'<input id="{fid}" name="{name}" type="{kind}" placeholder="{ph}"{a}{r}>'
    return f'<div class="{cls}"><label for="{fid}">{label}</label>{ctl}<span class="err" aria-live="polite"></span></div>'


def quote_form(subject, chips=None, extra_fields="", button="Send request"):
    chip_html = ""
    if chips:
        cs = "".join(
            f'<input type="radio" name="Service" id="c{i}" value="{c}"{" checked" if i == 0 else ""}><label for="c{i}">{c}</label>'
            for i, c in enumerate(chips)
        )
        chip_html = f'<fieldset class="field full" style="border:0;padding:0;margin:0"><legend style="font-weight:600;font-size:var(--t-sm);margin-bottom:.45rem">What do you need?</legend><div class="chips">{cs}</div></fieldset>'
    return f"""<form class="quote" data-subject="{subject}" novalidate>
  {chip_html}
  {field("Name", "Full name", auto="name")}
  {field("Organisation", "Company or school", req=False, auto="organization")}
  {field("Phone", "Phone number", "tel", auto="tel", ph="e.g. 082 123 4567")}
  {field("Email", "Email address", "email", auto="email")}
  {extra_fields}
  {field("Details", "Tell us what you need", "textarea", full=True, ph="Date, location, expected numbers, any special requirements")}
  <div class="form-foot">
    <p>We reply within one business day. For an emergency, don’t use this form — call {NUM}.</p>
    <button class="btn" type="submit">{button} {I['arrow']}</button>
  </div>
  <div class="form-done" role="status"><b>Your email is ready to send.</b> Your mail app has opened with the request filled in. Press send and we’ll reply within one business day.</div>
</form>"""


VOICES = [
    ("Thank you for not only transporting us safely but also for going above and beyond. The way you allowed us to wait for our Pastor to pray with us meant the world.", None,
     "Alicia Blignaut", "to paramedics Nelly and Kim, after an ambulance transfer"),
    ("Ngiyabonga my brother for assisting my boy and keeping me updated on the progress of transportation. You kept me and my wife calm. I have never experienced such professionalism from an ambulance company.", None,
     "A grateful father", "to Zac and the crew"),
    ("Die vinnige aankoms, die manier hoe hulle die pasiënt behandel. Jy word die heletyd op hoogte gehou oor die vordering. Ek wil net sê julle is puik, baie dankie.",
     "The fast arrival, the way they treat the patient. You’re kept up to date the whole time. I just want to say you are excellent — thank you.",
     "Family of a patient", "transported to Kosmos twice"),
    ("I attended a first aid training course with Legacy EMS and was impressed by the depth of knowledge and practical skills I gained. I feel confident in my ability to handle emergencies now.", None,
     "Jeaneth and Patrick", "first aid course graduates"),
    ("Thank you for the quick help. It really was a pleasure speaking to someone so friendly on the phone.", None,
     "Venessa", "called the emergency line"),
]


def voices_section():
    items = ""
    for q, tr, who, ctx in VOICES:
        trh = f'<p class="translation">{tr}</p>' if tr else ""
        lang = ' lang="af"' if tr else ""
        items += f'<figure class="voice" style="margin:0"><blockquote{lang}>{q}</blockquote>{trh}<cite>{who} <span>— {ctx}</span></cite></figure>'
    return f"""<section class="section dark voices" aria-labelledby="voices-h">
  <div class="wrap">
    <div class="section-head"><h2 id="voices-h">In their words</h2><p>Messages families and clients sent us, unedited except for length — in the language they wrote them.</p></div>
    <div class="voices-grid"><div>
    <div class="voice-stage" aria-live="polite">{items}</div>
    <div class="voice-nav">
      <button class="voice-prev" aria-label="Previous message">{I['left']}</button>
      <button class="voice-next" aria-label="Next message">{I['arrow']}</button>
      <span class="voice-count">1 / {len(VOICES)}</span><span class="voice-bar"><i></i></span>
    </div></div>
    <div class="voices-emblem" aria-hidden="true"><img src="assets/img/emblem.png" alt=""></div></div>
  </div>
</section>
"""


def offer(icon, h, p):
    return f'<div class="offer"><span class="offer-icon">{I[icon]}</span><div><h3>{h}</h3><p>{p}</p></div></div>'


def steps(items):
    return '<ol class="steps">' + "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in items) + "</ol>"


def checks(items):
    return '<ul class="checks">' + "".join(f"<li><div><b>{a}</b><span>{b}</span></div></li>" for a, b in items) + "</ul>"


def write(name, body):
    (ROOT / name).write_text(body, encoding="utf-8")
    print("wrote", name)


# ============================================================== HOME
SCHEMA = f"""<script type="application/ld+json">{{
 "@context":"https://schema.org","@type":"EmergencyService",
 "name":"Legacy Emergency Medical Services","alternateName":"Legacy EMS",
 "url":"https://legacyems.co.za/","telephone":"{TEL}","email":"{EMAIL}",
 "image":"https://legacyems.co.za/wp-content/uploads/2025/09/Ambos-1.jpg",
 "foundingDate":"2016","areaServed":["Emalahleni","Witbank","Mpumalanga"],
 "address":{{"@type":"PostalAddress","addressLocality":"Emalahleni","addressRegion":"Mpumalanga","addressCountry":"ZA"}},
 "openingHours":"Mo-Su 00:00-23:59","sameAs":["{FB}"]
}}</script>"""

svc = [
    ("ambulances.html#emergencies", "Medical &amp; trauma emergencies", "Heart attacks, strokes, collisions, falls. Advanced Life Support crews, on the road day and night.", "crash-scene"),
    ("ambulances.html#transfers", "Interfacility transfers", "Ventilated, monitored and escorted moves between hospitals, including discreet executive transfers.", "ambulances-hospital"),
    ("events.html", "Event medical cover", "School sports, festivals, corporate days and races — a medical team on site, an ambulance on standby.", "event-tent"),
    ("site-medical.html", "Site &amp; industrial medical", "On-site medical rooms, emergency coordination and audits for mines, plants and construction.", "site-1"),
    ("training.html", "Training courses", "First Aid, Basic Life Support and Basic Fire Fighting for staff, schools and the public.", "event-field"),
]
svc_html = "".join(
    f'<li><a href="{h}"><h3>{t}</h3><p>{d}</p><span class="go">{I["arrow"]}</span></a></li>' for h, t, d, _ in svc
)
svc_float = "".join(f'<img src="assets/img/{im}.jpg" alt="" loading="lazy">' for *_, im in svc)

units = [
    ("hero-mfezi", "Mfezi", "Rapid response, VW Golf R", "First on scene. Carries a paramedic and Advanced Life Support kit ahead of the ambulance.", "50% 55%"),
    ("boomslang", "Boomslang", "Response vehicle, Toyota RAV4", "Our all-rounder for event standby and rural callouts where the road runs out.", "50% 55%"),
    ("black-mamba-fire", "Black Mamba", "Incident response", "Standing by at an industrial fire outside Emalahleni — the kind of scene our site teams train for.", "50% 40%"),
    ("ambulance-van", "ALS ambulances", "Nissan NV350 fleet", "Fully equipped Advanced Life Support ambulances for emergencies and interfacility transfers.", "50% 50%"),
    ("bakkie-dam", "Bakkie 4×4", "Off-road support, Nissan Navara", "Reaches dams, farms and open-cast sites that a standard ambulance can’t.", "50% 60%"),
]
units_html = "".join(
    f"""<article class="unit"><div class="unit-photo sheen"><img src="assets/img/{img}.jpg" alt="{name} — {tag}" loading="lazy" style="object-position:{pos}"></div>
<div class="unit-meta"><div><span class="unit-tag">{tag}</span><h3 class="unit-name">{name}</h3></div><p>{d}</p></div></article>"""
    for img, name, tag, d, pos in units
)

home = head("Legacy EMS — Advanced Life Support ambulance service in Emalahleni",
            "24-hour Advanced Life Support ambulance service in Emalahleni (Witbank), Mpumalanga. Emergencies, interfacility transfers, event and site medical cover, and first aid training. Call 061 996 0911.",
            SCHEMA) + header("index.html") + f"""
<div class="curtain" aria-hidden="true"><svg viewBox="0 0 520 120"><path d="M0 60 H170 L185 60 L195 40 L205 60 L220 60 L232 8 L248 112 L260 60 L300 60 L312 48 L326 60 H520"/></svg></div>
<main id="main">
<section class="hero grain" aria-labelledby="hero-h">
  <div class="hero-media" data-lightrig="mfezi">
    <img src="assets/img/hero-mfezi.jpg" alt="Legacy's Mfezi rapid response car at dusk with its lightbar on" fetchpriority="high">
    <canvas aria-hidden="true"></canvas>
  </div>
  <div class="scroll-cue" aria-hidden="true">Scroll</div>
  <div class="wrap hero-inner">
    <div class="hero-kicker" data-in><span class="live-dot">Crews on standby now</span><span>Advanced Life Support</span><span>Emalahleni, Mpumalanga</span></div>
    <a class="hero-num livery-num" href="tel:{TEL}" data-split aria-label="{NUM}">{NUM}</a>
    <div class="hero-sub">
      <h1 id="hero-h" data-in>The emergency line Emalahleni has trusted since 2016. Paramedics answer, day and night.</h1>
      <div class="hero-actions" data-in>
        <a class="btn btn--siren pulse" href="tel:{TEL}">{I['phone']} Call now</a>
        <a class="btn btn--ghost" href="#book">Book event or site cover</a>
      </div>
    </div>
  </div>
</section>

<section class="creds" aria-label="Credentials">
  <div class="wrap"><ul>
    <li><b>Advanced Life Support</b><span>Registered ALS ambulance service</span></li>
    <li><b>Mpumalanga DoH</b><span>Accredited by the Department of Health</span></li>
    <li><b>Since 2016</b><span>A decade on Emalahleni’s roads</span></li>
    <li><b>24 hours, 7 days</b><span>The emergency line never closes</span></li>
  </ul></div>
</section>

<section class="section" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="section-head"><h2 id="svc-h">One crew for every kind of emergency</h2><p>From a 2 a.m. call on the N4 to a school athletics day, the same accredited team, the same standard of care.</p></div>
    <ul class="svc-index">{svc_html}</ul>
  </div>
  <div class="svc-float" aria-hidden="true">{svc_float}</div>
</section>

<section class="fleet grain" aria-labelledby="fleet-h">
  <div class="wrap fleet-intro section-head" style="margin-bottom:0">
    <h2 id="fleet-h">Every unit has a name</h2>
    <p>Our response vehicles are named after Africa’s snakes — fast, unmistakable, and impossible to ignore on the road. Look for the green.</p>
  </div>
  <div class="fleet-track">{units_html}</div>
</section>

<section class="split-section section" aria-labelledby="als-h">
  <div class="wrap split">
    <div>
      <h2 id="als-h">What Advanced Life Support means for your family</h2>
      <p class="lede">A basic ambulance gets a patient to hospital. An ALS crew starts hospital-level treatment where they find you.</p>
      {checks([
          ("Airway and breathing", "Advanced airway management and ventilation on scene and in transit."),
          ("Heart monitoring", "Continuous cardiac monitoring and defibrillation for heart attacks and arrhythmias."),
          ("Medication and IV access", "Pain relief, fluids and emergency drugs given before you reach casualty."),
          ("You stay informed", "We keep families updated through the transfer — something our clients mention again and again."),
      ])}
      <a class="btn" href="ambulances.html">How our ambulance service works {I['arrow']}</a>
    </div>
    <div class="split-media reveal-img"><img src="assets/img/ambulance-door.jpg" alt="Legacy ambulance door with the Legacy Emergency Specialists livery" loading="lazy"></div>
  </div>
</section>

<section class="night-band grain" data-beacon="0.578,0.177" aria-labelledby="night-h">
  <div class="hero-media"><img src="assets/img/night-fleet.jpg" alt="Legacy response cars parked at night with a red beacon lit" loading="lazy"></div>
  <div class="beacon" aria-hidden="true"></div>
  <div class="wrap night-copy">
    <h2 id="night-h">2 a.m. is still business hours.</h2>
    <p>Emergencies don’t keep office hours, so neither do we. A real person answers {NUM} around the clock, and a crew is dispatched while you’re still on the line.</p>
    <a class="btn btn--siren pulse" href="tel:{TEL}" style="margin-top:1rem">{I['phone']} Save {NUM}</a>
  </div>
</section>

{voices_section()}

<section class="section" id="book" aria-labelledby="book-h">
  <div class="wrap book">
    <div class="book-aside">
      <h2 id="book-h">Book medical cover or a course</h2>
      <p class="lede">Planning an event, running a site, or training a team? Tell us the basics and we’ll send a quote and plan.</p>
      <a class="big-call" href="tel:{TEL}"><small>Emergency? Don’t fill in a form.</small><span class="livery-num">{NUM}</span></a>
      <ul class="contact-lines">
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{WA}">Message us on WhatsApp</a></li>
      </ul>
    </div>
    {quote_form("Quote request from website", ["Event cover", "Site medical", "Interfacility transfer", "Training course", "Something else"])}
  </div>
</section>
</main>
""" + footer()
write("index.html", home)

# ======================================================== AMBULANCES
amb = head("Ambulance services — Legacy EMS Emalahleni",
           "Advanced Life Support emergency response, interfacility transfers and executive transfers in Emalahleni and across Mpumalanga. Call 061 996 0911.") + header("ambulances.html") + f"""
<main id="main">
{page_hero("ambulance-van", "Ambulance services", "Swift response. Hospital-level care on the way.",
           "Advanced Life Support ambulances for emergencies, hospital-to-hospital transfers and private executive transfers.", "50% 55%",
           f'<a class="btn btn--siren pulse" href="tel:{TEL}">{I["phone"]} Call {NUM}</a><a class="btn btn--ghost" href="#transfers">Book a transfer</a>')}

<section class="section" id="emergencies" aria-labelledby="em-h">
  <div class="wrap split">
    <div>
      <h2 id="em-h">Medical &amp; trauma emergencies</h2>
      <p class="lede">Heart attacks, strokes, severe injuries and road accidents — our paramedics stabilise first and transport second.</p>
      <p>Every second counts. Our crews are trained to manage complex medical and trauma cases on scene, using the same equipment you’d find in a resuscitation room. We treat with precision and compassion, and we keep the people waiting at home informed.</p>
      {checks([("Cardiac and stroke calls", "ECG monitoring, defibrillation and time-critical transport to the right facility."),
               ("Road traffic collisions", "Scene safety, spinal care and trauma management on the N4, N12 and local roads."),
               ("Medical emergencies at home", "Breathing difficulty, diabetic emergencies, seizures, falls and more.")])}
    </div>
    <div class="split-media reveal-img"><img src="assets/img/crash-scene.jpg" alt="Legacy crew at a road accident scene in the mountains" loading="lazy"></div>
  </div>
</section>

<section class="section forest" aria-labelledby="call-h">
  <div class="wrap">
    <div class="section-head"><h2 id="call-h">What happens when you call</h2><p>The first minutes decide the outcome, so here’s exactly what to expect.</p></div>
    {steps([("Your call is answered", "A trained call-taker answers 061 9960 911 and asks where you are and what happened."),
            ("A crew is dispatched", "The nearest ALS crew is sent while you’re still on the line. Stay on the phone if you can."),
            ("Care starts on scene", "Paramedics assess, stabilise and begin treatment before moving the patient."),
            ("Safe handover", "We transport to the most suitable hospital and update your family along the way.")])}
  </div>
</section>

<section class="section" id="transfers" aria-labelledby="ift-h">
  <div class="wrap split split--flip">
    <div>
      <h2 id="ift-h">Interfacility transfers</h2>
      <p class="lede">Safe, monitored transport between hospitals when a patient needs care their current facility can’t provide.</p>
      <p>We coordinate directly with the sending and receiving medical teams so treatment continues without a gap. Our ambulances carry advanced life support systems and our crews are trained for a wide range of conditions — so families can focus on recovery, not logistics.</p>
      {checks([("Hospital-to-hospital", "Including ICU and specialist referrals across Mpumalanga and Gauteng."),
               ("Booked or same-day", "Scheduled transfers and urgent moves, arranged with the ward.")])}
      <a class="btn" href="contact.html">Book a transfer {I['arrow']}</a>
    </div>
    <div class="split-media reveal-img"><img src="assets/img/ambulances-hospital.jpg" alt="Two Legacy ambulances parked at a hospital emergency unit" loading="lazy"></div>
  </div>
</section>

<section class="section dark grain" id="executive" aria-labelledby="ex-h" style="position:relative;overflow:hidden">
  <div class="wrap split">
    <div class="split-media wide reveal-img sheen"><img src="assets/img/legacy-mono.jpg" alt="Close-up of the Legacy Emergency Specialists lettering on a vehicle" loading="lazy"></div>
    <div>
      <h2 id="ex-h">Executive interfacility transfers</h2>
      <p class="lede">Private, discreet transport for high-profile patients and their families.</p>
      {checks([("Dedicated crew", "A senior ALS crew assigned to one patient for the whole journey."),
               ("Discretion first", "Confidential bookings, unmarked arrival on request and a single point of contact."),
               ("Family comfort", "Space for a companion and regular updates to the people who need them.")])}
      <a class="btn btn--gold" href="contact.html" style="margin-top:1.4rem">Arrange an executive transfer {I['arrow']}</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="kit-h">
  <div class="wrap split">
    <div>
      <h2 id="kit-h">Equipped like a resuscitation room</h2>
      <p class="lede">Clean, checked and restocked after every call.</p>
      <p>Every ambulance carries advanced life support equipment, with stretchers and scoops designed for safe patient movement. Vehicles and kit are checked at every shift change.</p>
    </div>
    <div class="split-media reveal-img"><img src="assets/img/stretcher.jpg" alt="Orange scoop stretcher inside a Legacy ambulance" loading="lazy"></div>
  </div>
</section>
{cta("Save the number before you need it.", "Add 061 9960 911 to your phone now — it takes five seconds and it’s the one number you won’t want to search for.")}
</main>
""" + footer()
write("ambulances.html", amb)

# ============================================================ EVENTS
events = head("Event medical cover — Legacy EMS",
              "Medical standby for school sports, corporate events, concerts, festivals and races in Mpumalanga. On-site paramedics, ambulances and first aid stations.") + header("events.html") + f"""
<main id="main">
{page_hero("event-tent", "Events", "Medical cover, so you can run the event.",
           "School sports days, corporate functions, concerts, festivals and races. We plan for the unexpected and handle it when it happens.", "50% 40%",
           f'<a class="btn btn--siren" href="#quote">Get an event quote</a>')}
<section class="section" aria-labelledby="types-h">
  <div class="wrap">
    <div class="section-head"><h2 id="types-h">Events we cover</h2><p>Every plan is scaled to your crowd, venue and risk — from a single paramedic at a school gala to a full medical post at a festival.</p></div>
    <div class="offers">
      {offer("school", "School events", "Athletics, rugby, galas and camps. On-site medical professionals and equipment for students, staff and parents.")}
      {offer("brief", "Corporate events", "Tailored safety plans, risk assessments and emergency response for conferences, launches and year-end functions.")}
      {offer("music", "Concerts &amp; festivals", "Medical tents, roaming teams and ambulance standby for crowds of every size.")}
      {offer("trophy", "Sports events", "Injury management and rapid response for athletes and spectators at races, tournaments and fun runs.")}
    </div>
  </div>
</section>
<section class="section" style="padding-top:0" aria-labelledby="day-h">
  <div class="wrap split">
    <div class="split-media reveal-img"><img src="assets/img/event-field.jpg" alt="Legacy medical post with branded gazebo and stretchers at a sports field" loading="lazy"></div>
    <div>
      <h2 id="day-h">What arrives on the day</h2>
      <p class="lede">You’ll see us before the first guest does.</p>
      {checks([("A branded medical post", "Gazebo, stretchers and treatment area, clearly marked with our emergency number."),
               ("Paramedics and medics", "Staffed to the size and risk of your event."),
               ("Ambulance on standby", "For fast transport if a patient needs hospital care."),
               ("A post-event report", "Every patient seen, every treatment given — for your records and insurers.")])}
    </div>
  </div>
</section>
<section class="section forest" aria-labelledby="plan-h">
  <div class="wrap">
    <div class="section-head"><h2 id="plan-h">From enquiry to all-clear</h2><p>Most events are planned in a single call and a site visit.</p></div>
    {steps([("Tell us about the event", "Date, venue, expected crowd and activities."),
            ("We assess the risk", "A medical plan and quote matched to your crowd and venue."),
            ("We’re on site", "Medical post set up before gates open, crew briefed with your organisers."),
            ("You get the report", "A summary of every incident handled, sent after the event.")])}
  </div>
</section>
<section class="section" id="quote" aria-labelledby="eq-h">
  <div class="wrap book">
    <div class="book-aside"><h2 id="eq-h">Get an event quote</h2><p class="lede">Give us the basics and we’ll come back with a medical plan and price.</p>
      <a class="big-call" href="tel:{TEL}"><small>Prefer to talk it through?</small><span class="livery-num">{NUM}</span></a></div>
    {quote_form("Event medical cover quote", ["School event", "Corporate", "Concert or festival", "Sports event", "Other"], field("Date", "Event date", "date", req=False) + field("Crowd", "Expected attendance", "number", req=False, ph="e.g. 800"), "Request quote")}
  </div>
</section>
</main>
""" + footer()
write("events.html", events)

# ====================================================== SITE MEDICAL
site = head("Site & industrial medical services — Legacy EMS",
            "On-site medical rooms, emergency coordination, resource planning and site audits for mines, plants and construction in Emalahleni and Mpumalanga.") + header("site-medical.html") + f"""
<main id="main">
{page_hero("black-mamba-fire", "Site medical", "Medical readiness for sites that can’t stop.",
           "Mines, plants and construction sites around Emalahleni rely on us for on-site medical cover, coordination and audits.", "50% 35%",
           f'<a class="btn btn--siren" href="#quote">Talk to us about your site</a>')}
<section class="section" aria-labelledby="sv-h">
  <div class="wrap">
    <div class="section-head"><h2 id="sv-h">Site management services</h2><p>Our mission: every emergency site runs with precision, risks are minimised and patient care is maximised.</p></div>
    <div class="offers">
      {offer("radio", "Emergency coordination", "Expert coordination so medical teams and resources are deployed where they’re needed, the moment they’re needed.")}
      {offer("boxes", "Resource allocation", "The right equipment and personnel available at a moment’s notice, matched to each site’s risk profile.")}
      {offer("clinic", "On-site medical rooms", "Equipped first aid and treatment rooms set up, stocked and staffed on your site.")}
      {offer("clip", "Site medical audits", "We inspect your medical readiness — rooms, kits, plans and people — and give you a clear report.")}
    </div>
  </div>
</section>
<section class="section dark" aria-labelledby="rooms-h">
  <div class="wrap">
    <div class="section-head"><h2 id="rooms-h">Medical rooms we’ve set up</h2><p>Climate-controlled, clean and stocked — ready for the day something goes wrong.</p></div>
    <div class="trio">
      <div class="split-media reveal-img"><img src="assets/img/site-1.jpg" alt="On-site medical room with air conditioning and spinal board" loading="lazy"></div>
      <div class="split-media reveal-img"><img src="assets/img/site-2.jpg" alt="Empty site medical room before fit-out" loading="lazy"></div>
      <div class="split-media reveal-img"><img src="assets/img/site-3.jpg" alt="Treatment bed and stocked kit in an on-site medical room" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="section" aria-labelledby="faq-h">
  <div class="wrap split" style="align-items:start">
    <div><h2 id="faq-h">Your questions answered</h2><p class="lede" style="margin-top:1.2rem">Common questions from safety officers and site managers.</p></div>
    <div class="faq">
      <details><summary>What’s included in site management?</summary><div class="faq-body"><p>Emergency planning, on-site medical support and staff training to make sure your site is prepared for any situation.</p></div></details>
      <details><summary>How do you ensure quality?</summary><div class="faq-body"><p>Continuous staff training, regular equipment checks and adherence to industry best practice.</p></div></details>
      <details><summary>Can you cover large-scale operations and events?</summary><div class="faq-body"><p>Yes. We have the capacity to manage medical services for sites and events of any size, with quick response times.</p></div></details>
      <details><summary>What training do you offer for site staff?</summary><div class="faq-body"><p>CPR, first aid, basic fire fighting and basic life support, tailored to the hazards on your site.</p></div></details>
      <details><summary>How quickly can you deploy?</summary><div class="faq-body"><p>Our team is on standby 24/7 and can be deployed rapidly for immediate medical support.</p></div></details>
      <details><summary>Do you offer custom packages?</summary><div class="faq-body"><p>Yes. We build packages around your site’s size, shift patterns and risk profile.</p></div></details>
    </div>
  </div>
</section>
<section class="section forest" id="quote" aria-labelledby="sq-h">
  <div class="wrap book">
    <div class="book-aside"><h2 id="sq-h">Talk to us about your site</h2><p class="lede">Tell us about your operation and we’ll arrange a site visit.</p>
      <a class="big-call" href="tel:{TEL}"><small>Call the operations line</small><span class="livery-num">{NUM}</span></a></div>
    <div style="color:var(--ink);background:var(--paper);padding:clamp(1.2rem,3vw,2.4rem);border-radius:20px">
    {quote_form("Site medical enquiry", ["On-site medic", "Medical room", "Site audit", "Emergency plan", "Staff training"], button="Request site visit")}
    </div>
  </div>
</section>
</main>
""" + footer()
write("site-medical.html", site)

# ========================================================== TRAINING
training = head("First aid, BLS & fire fighting training — Legacy EMS",
                "First Aid, Basic Life Support (CPR & AED), Basic Fire Fighting and advanced medical response courses in Emalahleni for companies, schools and individuals.") + header("training.html") + f"""
<main id="main">
{page_hero("golf-stadium", "Training", "Learn what to do in the first five minutes.",
           "Practical, instructor-led courses taught by working paramedics — for healthcare workers, first responders, companies and the public.", "50% 60%",
           f'<a class="btn btn--siren" href="#enrol">Enquire about a course</a>')}
<section class="section" aria-labelledby="c-h">
  <div class="wrap">
    <div class="section-head"><h2 id="c-h">Our courses</h2><p>Real-world scenarios, hands-on practice and the confidence to act when every second counts.</p></div>
    <div class="offers">
      {offer("bandage", "First Aid", "Manage common injuries and illnesses until professional help arrives. Ideal for workplaces, schools and parents.")}
      {offer("heart", "Basic Life Support", "Perform high-quality CPR and use an AED. The course that saves the most lives.")}
      {offer("flame", "Basic Fire Fighting", "Respond to fire emergencies safely, choose the right extinguisher and protect lives and property.")}
      {offer("pulse", "Advanced Medical Response", "For those who want to go further: managing complex medical situations under pressure.")}
    </div>
  </div>
</section>
<section class="section forest" aria-labelledby="who-h">
  <div class="wrap split">
    <div>
      <h2 id="who-h">Who it’s for</h2>
      {checks([("Healthcare professionals", "Doctors, nurses and paramedics sharpening emergency skills."),
               ("First responders", "Fire, police and security teams who arrive first."),
               ("Companies and sites", "Group training on your premises to meet safety requirements."),
               ("Everyone else", "Parents, coaches and community leaders who want to be ready.")])}
    </div>
    <div class="split-media reveal-img"><img src="assets/img/event-tent.jpg" alt="Legacy medical team at a community event" loading="lazy"></div>
  </div>
</section>
<section class="section" id="enrol" aria-labelledby="en-h">
  <div class="wrap book">
    <div class="book-aside"><h2 id="en-h">Enquire about a course</h2><p class="lede">Tell us which course and how many people. We’ll send dates and pricing.</p></div>
    {quote_form("Training course enquiry", ["First Aid", "Basic Life Support", "Basic Fire Fighting", "Advanced Medical Response"], field("People", "Number of people", "number", req=False, ph="e.g. 12"), "Send enquiry")}
  </div>
</section>
</main>
""" + footer()
write("training.html", training)

# ============================================================= ABOUT
values = [("Empathy", "We understand and meet our patients’ healthcare and emotional needs."),
          ("Resilience", "We put the same passion and energy into every patient’s fight."),
          ("Timeliness", "Emergency and non-emergency transport, on time."),
          ("Accountability", "We own every patient’s wellbeing while they’re in our care."),
          ("Delivery", "We aim to exceed patient and client expectations."),
          ("Quality", "We monitor our service through evaluation and reporting."),
          ("Education", "We help patients and providers make better life-saving decisions."),
          ("Teamwork", "Information flows clearly and securely through the whole team."),
          ("Efficiency", "Technology and protocols measured against medical best practice.")]
about = head("About Legacy Emergency Medical Services",
             "Established in 2016, Legacy EMS is a registered Advanced Life Support ambulance service accredited by the Mpumalanga Department of Health.") + header("about.html") + f"""
<main id="main">
{page_hero("legacy-mono", "About", "Today’s footsteps, tomorrow’s Legacy.",
           "A registered Advanced Life Support ambulance service, accredited by the Mpumalanga Department of Health. Established in 2016.", "50% 50%")}
<section class="section" aria-labelledby="st-h">
  <div class="wrap split">
    <div>
      <h2 id="st-h">From one ALS service to a complete emergency partner</h2>
      <p class="lede">Legacy began in 2016 as an Advanced Life Support emergency service in Emalahleni.</p>
      <p>As our clients’ needs grew, so did we. Today Legacy covers every part of pre-hospital care: emergency response, transfers, event and site medical, training, equipment sales and specialist VIP transfers.</p>
      <p>We believe in a hands-on approach to every project, in teamwork as the foundation of success, and in giving each client specialist, individual attention.</p>
    </div>
    <div class="split-media reveal-img"><img src="assets/img/ambulance-side.jpg" alt="Side of a Legacy ambulance showing the heart and caduceus logo and emergency number" loading="lazy"></div>
  </div>
</section>
<section class="section" style="padding-top:0" aria-label="Mission and vision">
  <div class="wrap offers">
    <div class="offer" style="grid-template-columns:1fr"><div><h3>Our mission</h3><p>To save lives, reduce suffering and enhance quality of life through accessible, responsive patient care and transport — delivered by a unified team of highly qualified professionals, with integrity at all times.</p></div></div>
    <div class="offer" style="grid-template-columns:1fr"><div><h3>Our vision</h3><p>To be the preferred service provider for every client through excellence and efficiency, and to build collaborative relationships with the public, healthcare facilities, other ambulance services and community organisations.</p></div></div>
  </div>
</section>
<section class="section forest" aria-labelledby="v-h">
  <div class="wrap">
    <div class="section-head"><h2 id="v-h">What we stand for</h2><p>Nine values that shape how we treat patients, clients and each other.</p></div>
    <div class="values">{''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in values)}</div>
  </div>
</section>
{cta("Want to work with Legacy?", "Hospitals, schools, sites and event organisers — let’s talk about how we can support you.")}
</main>
""" + footer()
write("about.html", about)

# =========================================================== GALLERY
gal = [("hero-mfezi", "Mfezi rapid response car", "fleet"), ("night-fleet", "The fleet at night", "fleet"),
       ("boomslang", "Boomslang response vehicle", "fleet"), ("ambulance-van", "ALS ambulance", "fleet"),
       ("event-tent", "Medical post at a community event", "events"), ("crash-scene", "Road accident response", "scenes"),
       ("black-mamba-fire", "Standby at an industrial fire", "scenes"), ("site-3", "On-site medical room", "sites"),
       ("event-field", "First aid station at a sports field", "events"), ("lightbar-sunset", "Lightbar at sunset", "fleet"),
       ("ambulances-hospital", "Ambulances at the emergency unit", "fleet scenes"), ("golf-stadium", "Standby at a school sports day", "events"),
       ("site-1", "Medical room fit-out", "sites"), ("bakkie-dam", "4×4 support at the dam", "fleet"),
       ("ambulance-door", "Legacy livery", "fleet"), ("boomslang-front", "Boomslang, front view", "fleet"),
       ("stretcher", "Scoop stretcher", "fleet"), ("site-2", "Site room before fit-out", "sites"), ("legacy-mono", "Legacy lettering", "fleet")]
gal_html = "".join(
    f'<figure tabindex="0" data-tags="{t}"><img src="assets/img/{im}.jpg" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
    for im, cap, t in gal)
gallery = head("Gallery — Legacy EMS", "Photos of the Legacy EMS fleet, event medical posts, site medical rooms and emergency scenes in Mpumalanga.") + header("gallery.html") + f"""
<main id="main">
{page_hero("night-fleet", "Gallery", "On the road, on site, on standby.", "A look at our fleet, our event posts and the places we work.", "50% 40%")}
<section class="section">
  <div class="wrap">
    <div class="gallery-filter" role="group" aria-label="Filter photos">
      <button data-filter="all" aria-pressed="true">All</button><button data-filter="fleet" aria-pressed="false">Fleet</button>
      <button data-filter="events" aria-pressed="false">Events</button><button data-filter="sites" aria-pressed="false">Sites</button>
      <button data-filter="scenes" aria-pressed="false">On scene</button>
    </div>
    <div class="masonry">{gal_html}</div>
  </div>
</section>
<div class="lightbox" aria-hidden="true" role="dialog" aria-label="Photo viewer"><button aria-label="Close photo">×</button><div><img alt=""><p></p></div></div>
</main>
""" + footer()
write("gallery.html", gallery)

# =========================================================== CONTACT
contact = head("Contact Legacy EMS — 061 996 0911",
               "Emergencies: call 061 996 0911, 24/7. For quotes, transfers, events, site medical and training, email admin@legacyems.co.za.") + header("contact.html") + f"""
<main id="main">
{page_hero("lightbar-sunset", "Contact", "In an emergency, call. For everything else, write.",
           "Our emergency line is answered 24 hours a day. Quotes and bookings are answered within one business day.", "50% 60%",
           f'<a class="btn btn--siren pulse" href="tel:{TEL}">{I["phone"]} Call {NUM}</a><a class="btn btn--ghost" href="{WA}">{I["wa"]} WhatsApp</a>')}
<section class="section" aria-labelledby="ct-h">
  <div class="wrap book">
    <div class="book-aside">
      <h2 id="ct-h">Get in touch</h2>
      <a class="big-call" href="tel:{TEL}"><small>Emergencies, 24/7</small><span class="livery-num">{NUM}</span></a>
      <ul class="contact-lines">
        <li><b>General and accounts</b><br><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><b>Facebook</b><br><a href="{FB}">legacyemergencyspecialists</a></li>
        <li><b>Area</b><br>Emalahleni (Witbank) and greater Mpumalanga</li>
      </ul>
    </div>
    {quote_form("Website enquiry", ["Event cover", "Site medical", "Interfacility transfer", "Training course", "Accounts", "Compliment"])}
  </div>
</section>
{voices_section()}
</main>
""" + footer()
write("contact.html", contact)
