(function () {
  var KEY = 'apuntes-view';

  function getView() {
    try { return localStorage.getItem(KEY) || 'tema'; } catch (e) { return 'tema'; }
  }
  function setView(v) {
    try { localStorage.setItem(KEY, v); } catch (e) {}
  }
  function apply(v) {
    document.documentElement.setAttribute('data-view', v);
    var sw = document.querySelector('.viewswitch');
    if (sw) sw.setAttribute('aria-checked', v === 'clase' ? 'true' : 'false');
  }

  function initViewSwitch() {
    apply(getView());
    var sw = document.querySelector('.viewswitch');
    if (!sw) return;
    sw.addEventListener('click', function () {
      var next = getView() === 'tema' ? 'clase' : 'tema';
      setView(next);
      apply(next);
    });
  }

  // ---- abrir automáticamente el <details> al que apunta el hash de la URL ----
  function openHashTarget() {
    var id = decodeURIComponent((location.hash || '').replace(/^#/, ''));
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    var d = el.closest ? el.closest('details') : null;
    if (el.tagName === 'DETAILS') d = el;
    if (d && !d.open) d.open = true;
    // dar tiempo a que el layout se asiente (details recién abierto) antes de hacer scroll
    setTimeout(function () {
      el.scrollIntoView({ block: 'start', behavior: 'smooth' });
      el.classList.add('hash-hit');
      setTimeout(function () { el.classList.remove('hash-hit'); }, 2200);
    }, 30);
  }

  // ================= Pendientes con reloj =================
  // Fuente: assets/pendientes.json. Cada ítem trae "vence" (ISO con zona, p. ej.
  // 2026-10-06T23:59:00-06:00) o null. La hora "actual" es la del SERVIDOR
  // (cabecera Date de la respuesta), no la del reloj del dispositivo, y el
  // listado se recalcula cada 30 s: al pasar "vence", el ítem desaparece solo.
  var TZ = 'America/Mexico_City';
  var Pend = { items: [], offset: 0, loaded: false, listeners: [] };

  Pend.now = function () { return Date.now() + Pend.offset; };
  Pend.dayKey = function (ms) {
    return new Intl.DateTimeFormat('en-CA', { timeZone: TZ, year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date(ms));
  };
  Pend.fmt = function (ms, opts) {
    return new Intl.DateTimeFormat('es-MX', Object.assign({ timeZone: TZ }, opts)).format(new Date(ms));
  };
  Pend.esc = function (t) {
    return String(t == null ? '' : t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  };
  Pend.vigentes = function () {
    var now = Pend.now();
    return Pend.items.filter(function (it) {
      if (it.oculto) return false;
      if (!it.vence) return true;            // sin fecha: se muestra aparte
      return new Date(it.vence).getTime() > now;
    }).sort(function (a, b) {
      var ta = a.vence ? new Date(a.vence).getTime() : Infinity;
      var tb = b.vence ? new Date(b.vence).getTime() : Infinity;
      return ta - tb;
    });
  };
  Pend.faltan = function (ms) {
    var d = ms - Pend.now();
    var min = Math.floor(d / 60000);
    if (min < 60) return 'en ' + Math.max(min, 1) + ' min';
    var h = Math.floor(min / 60);
    if (h < 48) return 'en ' + h + ' h ' + (min % 60) + ' min';
    return 'en ' + Math.floor(h / 24) + ' días';
  };
  Pend.grupo = function (it) {
    if (!it.vence) return 'sin';
    var t = new Date(it.vence).getTime();
    var hoy = Pend.dayKey(Pend.now());
    var k = Pend.dayKey(t);
    if (k === hoy) return 'hoy';
    if (k === Pend.dayKey(Pend.now() + 86400000)) return 'manana';
    if (t - Pend.now() < 7 * 86400000) return 'semana';
    return 'despues';
  };
  Pend.cardHtml = function (it, compact) {
    var t = it.vence ? new Date(it.vence).getTime() : null;
    var cuando = t
      ? Pend.fmt(t, { weekday: 'short', day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit', hour12: false }) +
        (it.hora_confirmada === false ? ' (fin del día)' : '')
      : (it.fecha_texto || 'Sin fecha');
    var faltan = t && (t - Pend.now() < 48 * 3600000) ? ' · ' + Pend.faltan(t) : '';
    var href = it.link ? (SITE_ROOT + it.link) : (it.classroom || '#');
    return '<a class="pend-card" href="' + Pend.esc(href) + '" style="--c:' + Pend.esc(it.color || '#7C9CD6') + '">' +
      '<div class="pend-top"><span class="pend-materia">' + Pend.esc(it.materia) + '</span>' +
      '<span class="pend-fecha">' + Pend.esc(cuando + faltan) + '</span></div>' +
      '<div class="pend-titulo">' + Pend.esc(it.titulo) + '</div>' +
      (compact || !it.detalle ? '' : '<div class="pend-detalle">' + Pend.esc(it.detalle) + '</div>') +
      '</a>';
  };
  Pend.onChange = function (fn) { Pend.listeners.push(fn); if (Pend.loaded) fn(); };
  Pend.tick = function () { Pend.listeners.forEach(function (fn) { fn(); }); };
  Pend.load = function () {
    return fetch(SITE_ROOT + 'assets/pendientes.json', { cache: 'no-store' })
      .then(function (r) {
        var d = r.headers.get('Date');
        if (d) { var sv = new Date(d).getTime(); if (!isNaN(sv)) Pend.offset = sv - Date.now(); }
        return r.json();
      })
      .then(function (data) {
        Pend.items = data.items || [];
        Pend.meta = data;
        Pend.loaded = true;
        Pend.tick();
      })
      .catch(function () { Pend.loaded = true; Pend.failed = true; Pend.tick(); });
  };

  // ================= Barra superior fija =================
  function initTopBar() {
    var bar = document.createElement('div');
    bar.className = 'topbar';
    bar.innerHTML =
      '<a class="tb-brand" href="' + SITE_ROOT + 'index.html">Apuntes<span class="dot">.</span></a>' +
      '<div class="tb-right"><a class="tb-link tb-pendientes" href="' + SITE_ROOT + 'pendientes.html">📌 Pendientes<span class="tb-badge" style="display:none"></span></a></div>';
    document.body.insertBefore(bar, document.body.firstChild);
    document.body.classList.add('has-topbar');
    var badge = bar.querySelector('.tb-badge');
    Pend.onChange(function () {
      var n = Pend.vigentes().filter(function (it) {
        return it.vence && (new Date(it.vence).getTime() - Pend.now()) < 48 * 3600000;
      }).length;
      badge.textContent = n;
      badge.style.display = n ? 'inline-block' : 'none';
    });
  }

  // ================= Panel de pendientes (portada) =================
  function initHomePendientes() {
    var mount = document.getElementById('pend-carousel');
    if (!mount) return;
    Pend.onChange(function () {
      var v = Pend.vigentes().filter(function (it) { return it.vence; }).slice(0, 5);
      if (!v.length) { mount.innerHTML = ''; return; }
      mount.innerHTML =
        '<div class="pend-carousel-head"><h2>📌 Próximos vencimientos</h2><a href="' + SITE_ROOT + 'pendientes.html">Ver todo →</a></div>' +
        v.map(function (it) { return Pend.cardHtml(it, true); }).join('');
    });
  }

  // ================= Página de pendientes =================
  function initPendientesPage() {
    var root = document.getElementById('pend-root');
    if (!root) return;
    var GRUPOS = [
      ['hoy', '🔥 Hoy'], ['manana', '⏰ Mañana'], ['semana', '📅 Esta semana'],
      ['despues', '🗓 Después'], ['sin', '📌 Sin fecha límite (aún)']
    ];
    var clock = document.getElementById('pend-clock');
    var upd = document.getElementById('pend-updated');
    Pend.onChange(function () {
      if (clock) clock.textContent = 'Ahora: ' + Pend.fmt(Pend.now(), { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false }) + ' (hora de la Ciudad de México)';
      if (upd && Pend.meta) upd.textContent = 'Lista actualizada: ' + Pend.meta.actualizado + '. ' + (Pend.meta.nota || '');
      if (Pend.failed) { root.innerHTML = '<p class="pend-empty">No se pudo cargar la lista de pendientes.</p>'; return; }
      var v = Pend.vigentes();
      if (!v.length) { root.innerHTML = '<p class="pend-empty">No hay pendientes obligatorios vigentes. 🎉</p>'; return; }
      var html = '';
      GRUPOS.forEach(function (g) {
        var grupo = v.filter(function (it) { return Pend.grupo(it) === g[0]; });
        if (!grupo.length) return;
        html += '<div class="pend-group"><h2>' + g[1] + '<span class="pend-count">' + grupo.length + '</span></h2>' +
          grupo.map(function (it) { return Pend.cardHtml(it, false); }).join('') + '</div>';
      });
      root.innerHTML = html;
    });
  }

  // ================= Buscador global =================
  // .src siempre resuelve a URL absoluta (no la ruta relativa cruda del atributo),
  // así que la raíz del sitio se obtiene quitando "assets/app.js" del final —
  // sirve igual en local, en GitHub Pages, y bajo cualquier subcarpeta de repo.
  var ASSETS_BASE = (function () {
    var cur = document.currentScript;
    if (!cur) {
      var scripts = document.getElementsByTagName('script');
      for (var i = 0; i < scripts.length; i++) {
        if (/app\.js(\?.*)?$/.test(scripts[i].src)) cur = scripts[i];
      }
    }
    return cur ? cur.src.replace(/app\.js(\?.*)?$/, '') : 'assets/';
  })();
  var SITE_ROOT = ASSETS_BASE.replace(/assets\/$/, '');

  var searchState = { items: null, loading: false, activeIndex: -1 };

  function loadIndex(cb) {
    if (searchState.items) return cb(searchState.items);
    if (searchState.loading) {
      var iv = setInterval(function () {
        if (searchState.items) { clearInterval(iv); cb(searchState.items); }
      }, 60);
      return;
    }
    searchState.loading = true;
    fetch(ASSETS_BASE + 'search-index.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        searchState.items = data.items || [];
        cb(searchState.items);
      })
      .catch(function () {
        searchState.items = [];
        cb(searchState.items);
      });
  }

  function scoreItem(q, it) {
    var title = it.title.toLowerCase();
    var sub = (it.subtitle || '').toLowerCase();
    var materia = (it.materia || '').toLowerCase();
    var text = it.text.toLowerCase();
    var score = 0;
    if (title.indexOf(q) === 0) score += 20;
    else if (title.indexOf(q) !== -1) score += 12;
    if (materia.indexOf(q) !== -1) score += 6;
    if (sub.indexOf(q) !== -1) score += 4;
    var ti = text.indexOf(q);
    if (ti !== -1) {
      score += 3;
      // cuenta ocurrencias extra (tope para no favorecer textos gigantes)
      var count = 0, from = 0;
      while (count < 8) {
        var idx = text.indexOf(q, from);
        if (idx === -1) break;
        count++; from = idx + q.length;
      }
      score += Math.min(count, 8) * 0.4;
      if (it.kind === 'section') score += 1.5; // resultados específicos primero
    }
    return { score: score, textIndex: ti };
  }

  function snippetAround(text, q, idx) {
    if (idx === -1) return text.slice(0, 140) + (text.length > 140 ? '…' : '');
    var start = Math.max(0, idx - 60);
    var end = Math.min(text.length, idx + q.length + 80);
    var s = (start > 0 ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '');
    return s;
  }

  function highlight(text, q) {
    if (!q) return text;
    var i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i === -1) return text;
    var esc = function (s) {
      return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    };
    return esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length));
  }

  function buildResults(query) {
    var q = query.trim().toLowerCase();
    if (q.length < 2) return [];
    var items = searchState.items || [];
    var scored = [];
    for (var i = 0; i < items.length; i++) {
      var r = scoreItem(q, items[i]);
      if (r.score > 0) scored.push({ item: items[i], score: r.score, textIndex: r.textIndex });
    }
    scored.sort(function (a, b) { return b.score - a.score; });
    return scored.slice(0, 30);
  }

  function resolveUrl(url) {
    return SITE_ROOT + url;
  }

  function renderResults(container, query, results) {
    container.innerHTML = '';
    if (!query.trim()) {
      container.innerHTML = '<div class="search-empty">Escribe para buscar en las 9 materias — clases, temarios, entregas…</div>';
      return;
    }
    if (query.trim().length < 2) {
      container.innerHTML = '<div class="search-empty">Sigue escribiendo…</div>';
      return;
    }
    if (!results.length) {
      container.innerHTML = '<div class="search-empty">Sin resultados para "' + query + '"</div>';
      return;
    }
    var q = query.trim();
    results.forEach(function (r, i) {
      var it = r.item;
      var row = document.createElement('a');
      row.className = 'search-row';
      row.href = resolveUrl(it.url);
      row.dataset.idx = i;
      var snip = snippetAround(it.text, q.toLowerCase(), r.textIndex);
      row.innerHTML =
        '<span class="sr-dot" style="background:' + it.color + '"></span>' +
        '<span class="sr-body">' +
        '<span class="sr-title">' + highlight(it.title, q) + '</span>' +
        '<span class="sr-sub">' + (it.subtitle || it.materia) + '</span>' +
        '<span class="sr-snip">' + highlight(snip, q) + '</span>' +
        '</span>';
      container.appendChild(row);
    });
  }

  function initSearch() {
    var btn = document.createElement('button');
    btn.className = 'search-fab';
    btn.setAttribute('aria-label', 'Buscar en todas las materias');
    btn.innerHTML = '🔍';
    document.body.appendChild(btn);

    var overlay = document.createElement('div');
    overlay.className = 'search-overlay';
    overlay.innerHTML =
      '<div class="search-box" role="dialog" aria-label="Buscador">' +
      '<input type="text" class="search-input" placeholder="Buscar en tus apuntes… (ej. SIGCHLD, DHCP, PCA)" autocomplete="off">' +
      '<div class="search-results"></div>' +
      '<div class="search-hint">Esc para cerrar</div>' +
      '</div>';
    document.body.appendChild(overlay);

    var input = overlay.querySelector('.search-input');
    var results = overlay.querySelector('.search-results');

    function open() {
      overlay.classList.add('open');
      loadIndex(function () { renderResults(results, input.value, buildResults(input.value)); });
      setTimeout(function () { input.focus(); }, 10);
    }
    function close() {
      overlay.classList.remove('open');
      searchState.activeIndex = -1;
    }

    btn.addEventListener('click', open);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) close();
    });
    document.addEventListener('keydown', function (e) {
      var typing = /input|textarea/i.test((document.activeElement || {}).tagName || '');
      if (!overlay.classList.contains('open') && e.key === '/' && !typing) {
        e.preventDefault();
        open();
        return;
      }
      if (overlay.classList.contains('open') && e.key === 'Escape') {
        close();
      }
    });

    input.addEventListener('input', function () {
      renderResults(results, input.value, buildResults(input.value));
    });
  }

  function init() {
    initTopBar();
    initHomePendientes();
    initPendientesPage();
    Pend.load();
    setInterval(Pend.tick, 30000);
    initViewSwitch();
    initSearch();
    openHashTarget();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
