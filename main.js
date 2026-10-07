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

  // Vergrößern auf Werkseiten
  var links = Array.prototype.slice.call(document.querySelectorAll('a[data-zoom]'));
  if (links.length) {
    var pos = 0, box = null;
    function zeige(i) {
      pos = (i + links.length) % links.length;
      box.querySelector('img').src = links[pos].getAttribute('href');
      box.querySelector('img').alt = links[pos].querySelector('img').alt;
      var mehr = links.length > 1;
      box.querySelector('.vor').style.display = mehr ? '' : 'none';
      box.querySelector('.weiter').style.display = mehr ? '' : 'none';
    }
    function schliesse() { if (box) { box.remove(); box = null; document.removeEventListener('keydown', taste); } }
    function taste(e) {
      if (e.key === 'Escape') schliesse();
      if (e.key === 'ArrowLeft') zeige(pos - 1);
      if (e.key === 'ArrowRight') zeige(pos + 1);
    }
    links.forEach(function (a, i) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        box = document.createElement('div');
        box.className = 'zoom';
        box.setAttribute('role', 'dialog');
        box.setAttribute('aria-label', 'Bild vergrößert');
        box.innerHTML = '<img alt=""><button class="zu" type="button" aria-label="Schließen">&times;</button><button class="vor" type="button" aria-label="Vorheriges Bild">&#8249;</button><button class="weiter" type="button" aria-label="Nächstes Bild">&#8250;</button>';
        document.body.appendChild(box);
        box.addEventListener('click', function (ev) {
          if (ev.target.classList.contains('zu') || ev.target === box) schliesse();
          if (ev.target.classList.contains('vor')) zeige(pos - 1);
          if (ev.target.classList.contains('weiter')) zeige(pos + 1);
        });
        document.addEventListener('keydown', taste);
        zeige(i);
      });
    });
  }

  // Soziale Knöpfe ohne Ziel, bis die Adressen feststehen
  Array.prototype.forEach.call(document.querySelectorAll('a.platzhalter'), function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); });
  });
})();
