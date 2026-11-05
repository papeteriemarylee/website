/* Papeterie Marylee — en-tête fixe et menu mobile */
(function () {
  var root = document.documentElement;
  var header = document.querySelector('.header');
  var burger = document.querySelector('.burger');
  var overlay = document.querySelector('.menu-overlay');

  // L'en-tête est fixe : on réserve sa hauteur en haut de la page.
  function setHeaderHeight() {
    if (header) root.style.setProperty('--header-h', header.offsetHeight + 'px');
  }
  setHeaderHeight();
  window.addEventListener('resize', setHeaderHeight);
  window.addEventListener('load', setHeaderHeight);

  if (!burger || !overlay) return;

  function setMenu(open) {
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.querySelector('.visually-hidden').textContent = open ? 'Fermer le menu' : 'Ouvrir le menu';
    overlay.setAttribute('aria-hidden', String(!open));
    document.body.style.overflow = open ? 'hidden' : '';
  }

  burger.addEventListener('click', function () {
    setMenu(!document.body.classList.contains('menu-open'));
  });
  overlay.addEventListener('click', function (e) {
    if (e.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && document.body.classList.contains('menu-open')) {
      setMenu(false);
      burger.focus();
    }
  });
  window.matchMedia('(min-width: 800px)').addEventListener('change', function (mq) {
    if (mq.matches) setMenu(false);
  });
})();
