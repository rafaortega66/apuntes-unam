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

  // ================= Barra superior fija =================
  function initTopBar() {
    var bar = document.createElement('div');
    bar.className = 'topbar';
    bar.innerHTML =
      '<a class="tb-brand" href="' + SITE_ROOT + 'index.html">Apuntes<span class="dot">.</span></a>' +
      '<div class="tb-right">' +
        '<a class="tb-link tb-pendientes" href="' + SITE_ROOT + 'pendientes.html">📌 Pendientes<span class="tb-badge" style="display:none"></span></a>' +
      '</div>';
    document.body.insertBefore(bar, document.body.firstChild);
    document.body.classList.add('has-topbar');

    fetch(SITE_ROOT + 'assets/pendientes.json')
      .then(function (r) { return r.json(); })
      .then(function (data) {
        var urgentes = (data.items || []).filter(function (it) {
          return it.urgencia === 'hoy' || it.urgencia === 'manana' || it.urgencia === 'vencido' || it.urgencia === 'verificar';
        }).length;
        if (urgentes > 0) {
          var badge = bar.querySelector('.tb-badge');
          badge.textContent = urgentes;
          badge.style.display = 'inline-block';
        }
      })
      .catch(function () {});
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
