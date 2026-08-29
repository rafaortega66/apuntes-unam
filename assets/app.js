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

  function init() {
    apply(getView());
    var sw = document.querySelector('.viewswitch');
    if (!sw) return;
    sw.addEventListener('click', function () {
      var next = getView() === 'tema' ? 'clase' : 'tema';
      setView(next);
      apply(next);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
