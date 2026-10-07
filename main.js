(function () {
  var kopf = document.querySelector('.kopf');
  function messen() {
    if (kopf) document.documentElement.style.setProperty('--kopf', kopf.offsetHeight + 'px');
  }
  messen();
  window.addEventListener('resize', messen);

  var knopf = document.querySelector('.menue-knopf');
  var nav = document.getElementById('nav');
  if (knopf && nav) {
    knopf.addEventListener('click', function () {
      var offen = nav.classList.toggle('offen');
      knopf.setAttribute('aria-expanded', offen ? 'true' : 'false');
      knopf.textContent = offen ? 'Schließen' : 'Menü';
    });
  }
})();
