/* Newsletter popup for workshopai.com.au.
 * Shows Substack's own signup form (an iframe) inside our popup, so visitors subscribe
 * without leaving the site. Rules agreed 24 Nov 2026:
 * - first-time visitors only (first 7 days after their first visit)
 * - shows at 50% scroll or on the second page view; exit intent is a desktop backstop
 * - desktop: centred popup; phones: bottom slide-in, never full screen
 * - at most 2 views a week, 30 days quiet after "No thanks" or close,
 *   never again once someone clicks into the form or arrives from the newsletter
 * - never on /for/, /floor-ready/, /proposals/ or /privacy/
 * Add ?popup=preview to any page to see it straight away, ?popup=reset to clear your state.
 * Loaded on every page by _src/build.py (the subscribe:start block). */
(function () {
  'use strict';
  if (window.__waiSubscribe) return;
  window.__waiSubscribe = true;

  var COPY = {
    headline: 'What are other trade businesses actually doing with AI?',
    line: 'Short, free reads. Unsubscribe any time.',
    noThanks: 'No thanks'
  };
  var EMBED = 'https://workshopai.substack.com/embed';
  var EXCLUDE = [/^\/for\//i, /^\/floor-ready\//i, /^\/proposals\//i, /^\/privacy\//i];
  var DAY = 864e5, NEW_DAYS = 7, MAX_VIEWS = 2, WINDOW_DAYS = 7, QUIET_DAYS = 30;
  var KEY = 'wai_newsletter', PV_KEY = 'wai_pv';
  // Substack's form sits vertically centred in a 320px frame. A 114px window from 176px down
  // shows the email box and terms (not Substack's header) at every width from 300px up.
  var FRAME_H = 320, CROP_TOP = 176, VIEW_H = 114;

  var now = Date.now();
  var params = new URLSearchParams(location.search);
  var mode = params.get('popup');

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; }
  }
  function save(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* storage blocked */ }
  }
  if (mode === 'reset') {
    try { localStorage.removeItem(KEY); sessionStorage.removeItem(PV_KEY); } catch (e) { /* ignore */ }
  }

  var preview = mode === 'preview';
  if (!preview && EXCLUDE.some(function (r) { return r.test(location.pathname); })) return;

  var st = load();
  if (!st.first) st.first = now;
  st.views = (st.views || []).filter(function (t) { return now - t < WINDOW_DAYS * DAY; });
  // Arriving from the newsletter means they already subscribe.
  if (/substack/i.test(document.referrer) || /substack/i.test(params.get('utm_source') || '')) st.done = now;
  save(st);

  var pv = 0;
  try { pv = (parseInt(sessionStorage.getItem(PV_KEY), 10) || 0) + 1; sessionStorage.setItem(PV_KEY, pv); } catch (e) { pv = 1; }

  function eligible() {
    if (st.done) return false;
    if (st.dismissed && now - st.dismissed < QUIET_DAYS * DAY) return false;
    if (now - st.first > NEW_DAYS * DAY) return false;
    return st.views.length < MAX_VIEWS;
  }
  if (!preview && !eligible()) return;

  var phone = window.matchMedia('(max-width: 640px)');
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  var shown = false, root, lastFocus, loadedAt = now;

  var CSS = [
    '.wai-sub{position:fixed;inset:0;z-index:1000;display:flex;align-items:center;justify-content:center;padding:20px;background:rgba(15,23,27,.74);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);opacity:0;transition:opacity .25s ease}',
    '.wai-sub.in{opacity:1}',
    '.wai-sub-card{position:relative;width:100%;max-width:420px;background:#FFFFFF;border-radius:14px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.45);transform:translateY(12px);transition:transform .25s ease;font-family:"Instrument Sans",system-ui,sans-serif;color:#22333B;max-height:calc(100vh - 40px);overflow-y:auto}',
    '.wai-sub.in .wai-sub-card{transform:none}',
    '.wai-sub-top{background:#A9927D;padding:26px 56px 22px 26px}',
    '.wai-sub-h{font-family:"Archivo",system-ui,sans-serif;font-weight:800;text-transform:uppercase;font-size:25px;line-height:1.05;letter-spacing:-.005em;color:#22333B;margin:0}',
    '.wai-sub-x{position:absolute;top:10px;right:10px;width:44px;height:44px;border:0;border-radius:8px;background:transparent;color:#22333B;font-size:28px;line-height:1;cursor:pointer}',
    '.wai-sub-x:hover,.wai-sub-x:focus-visible{background:rgba(34,51,59,.12)}',
    '.wai-sub-x:focus-visible,.wai-sub-no:focus-visible{outline:2px solid #22333B;outline-offset:2px}',
    '.wai-sub-line{font-size:16px;font-weight:500;line-height:1.5;color:#22333B;margin:0;padding:18px 26px 12px}',
    '.wai-sub-form{height:' + VIEW_H + 'px;overflow:hidden;margin:0 14px;border-radius:10px;background:#F4F3F2}',
    '.wai-sub-form iframe{display:block;width:100%;height:' + FRAME_H + 'px;margin-top:-' + CROP_TOP + 'px;border:0;background:#F4F3F2}',
    '.wai-sub-foot{padding:4px 26px 12px;text-align:center}',
    '.wai-sub-no{background:none;border:0;padding:10px 12px;font:inherit;font-size:14px;color:#54565C;text-decoration:underline;text-underline-offset:3px;cursor:pointer;min-height:44px}',
    '.wai-sub-no:hover{color:#22333B}',
    '.wai-sub.sheet{inset:auto 0 0 0;padding:0 8px calc(8px + env(safe-area-inset-bottom));background:none;-webkit-backdrop-filter:none;backdrop-filter:none;align-items:flex-end;pointer-events:none}',
    '.wai-sub.sheet .wai-sub-card{max-width:520px;pointer-events:auto;transform:translateY(110%);max-height:75vh;border:2px solid #22333B;box-shadow:0 -8px 48px rgba(14,22,26,.5)}',
    '.wai-sub.sheet.in .wai-sub-card{transform:none}',
    '.wai-sub.sheet .wai-sub-top{padding:18px 54px 16px 18px}',
    '.wai-sub.sheet .wai-sub-h{font-size:21px}',
    '.wai-sub.sheet .wai-sub-x{top:6px;right:6px}',
    '.wai-sub.sheet .wai-sub-line{font-size:15px;padding:12px 18px 10px}',
    '.wai-sub.sheet .wai-sub-form{margin:0 6px}',
    '.wai-sub.sheet .wai-sub-foot{padding:0 18px 2px}',
    '@media (prefers-reduced-motion: reduce){.wai-sub,.wai-sub-card{transition:none}}',
    '@media print{.wai-sub{display:none}}'
  ].join('\n');

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text) n.textContent = text;
    return n;
  }

  function close(reason) {
    if (!root) return;
    if (reason === 'dismiss' && !st.done) { st.dismissed = Date.now(); save(st); }
    root.classList.remove('in');
    document.removeEventListener('keydown', onKey);
    window.removeEventListener('blur', onBlur);
    var r = root; root = null;
    setTimeout(function () { r.remove(); }, 260);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function onKey(e) { if (e.key === 'Escape') close('dismiss'); }

  // A click into Substack's email box moves focus into the iframe and blurs this window.
  // We can't see the submit itself (it happens on Substack), so engaging counts as done.
  function onBlur() {
    setTimeout(function () {
      if (root && document.activeElement && document.activeElement.tagName === 'IFRAME' && root.contains(document.activeElement)) {
        st.done = Date.now(); save(st);
        var n = root.querySelector('.wai-sub-no'); if (n) n.textContent = 'Close';
      }
    }, 0);
  }

  function show() {
    if (shown) return;
    shown = true;
    detach();
    if (!preview) { st.views.push(Date.now()); save(st); }

    if (!document.getElementById('wai-sub-css')) {
      var style = el('style'); style.id = 'wai-sub-css'; style.textContent = CSS;
      document.head.appendChild(style);
    }
    var sheet = phone.matches;
    root = el('div', 'wai-sub' + (sheet ? ' sheet' : ''));
    // Pin the sheet to the screen width even if something on the page overflows sideways.
    if (sheet) { root.style.right = 'auto'; root.style.width = document.documentElement.clientWidth + 'px'; }
    var card = el('div', 'wai-sub-card');
    card.setAttribute('role', 'dialog');
    card.setAttribute('aria-modal', sheet ? 'false' : 'true');
    card.setAttribute('aria-labelledby', 'wai-sub-h');
    card.tabIndex = -1;

    var top = el('div', 'wai-sub-top');
    var h = el('h2', 'wai-sub-h', COPY.headline); h.id = 'wai-sub-h';
    top.appendChild(h);
    var x = el('button', 'wai-sub-x', '×');
    x.type = 'button'; x.setAttribute('aria-label', 'Close');
    x.addEventListener('click', function () { close('dismiss'); });

    var line = el('p', 'wai-sub-line', COPY.line);

    var form = el('div', 'wai-sub-form');
    var frame = document.createElement('iframe');
    frame.src = EMBED;
    frame.title = 'Subscribe to the Workshop AI newsletter';
    frame.setAttribute('scrolling', 'no');
    frame.setAttribute('frameborder', '0');
    // The signup completes inside the frame. Leaving out allow-popups stops Substack opening its
    // own welcome page in a new tab afterwards, so visitors stay on our site.
    frame.setAttribute('sandbox', 'allow-scripts allow-forms allow-same-origin');
    form.appendChild(frame);

    var foot = el('div', 'wai-sub-foot');
    var no = el('button', 'wai-sub-no', COPY.noThanks);
    no.type = 'button';
    no.addEventListener('click', function () { close('dismiss'); });
    foot.appendChild(no);

    card.appendChild(top); card.appendChild(x); card.appendChild(line); card.appendChild(form); card.appendChild(foot);
    root.appendChild(card);
    if (!sheet) root.addEventListener('click', function (e) { if (e.target === root) close('dismiss'); });
    document.body.appendChild(root);

    document.addEventListener('keydown', onKey);
    window.addEventListener('blur', onBlur);
    lastFocus = document.activeElement;
    requestAnimationFrame(function () {
      root && root.classList.add('in');
      if (!sheet) card.focus({ preventScroll: true });
    });
  }

  function scrolledHalf() {
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    return window.scrollY > 150 && max > 0 && window.scrollY / max >= 0.5;
  }
  function onScroll() { if (scrolledHalf()) show(); }
  function onLeave(e) {
    if (!e.relatedTarget && e.clientY <= 0 && Date.now() - loadedAt > 4000) show();
  }
  function detach() {
    window.removeEventListener('scroll', onScroll);
    document.removeEventListener('mouseout', onLeave);
  }

  function start() {
    if (preview) { show(); return; }
    if (pv >= 2) { setTimeout(show, 2500); return; }
    window.addEventListener('scroll', onScroll, { passive: true });
    if (finePointer.matches && !phone.matches) document.addEventListener('mouseout', onLeave);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
