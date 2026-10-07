# CLAUDE.md – Regeln für diese Website

Gilt für jede Sitzung in diesem Repo. Lies zu Beginn auch `_projekt/STAND.md`. Bei einem neuen Projekt zusätzlich `_werkstatt/HANDBUCH.md`.

## Projekt
- Website für: Charlotte (nur Vorname im Repo), Generative Painting, Beratung und Kunst, Freiburg.
- Repo: koojaa92/Charlotte-Website. Live ist der Branch `main` (GitHub Pages).
- Domain: [offen], DNS bei [offen]. E-Mail an der Domain: [offen]. MX- und TXT-Einträge nie ändern.
- Website-Typ und Ziel: Startseite mit Unterseiten Generative Painting (Methode und Marke), Coaching, Teams und Führungskräfte, Kunst (Galerie wie bei einer Künstlerseite, eine Seite pro Werk), Über mich. Zeigt auf einen Blick, was Charlotte macht, wer sie ist und wo ihre Kunst ist, mit vielen Bildern echter Projekte. Funktionen: Mail-Kontakt (Erstgespräch, Preisanfrage), Galerie.
- Pflege: Charlotte lernt, die Seite mit Claude Code selbst zu pflegen (wie Jakob). Jakob pflegt teilweise für sie. Darum alles einfach, ohne Build-Schritt und mit klaren Quellen (siehe Werke).
- Aktuelle Phase: 0. Bewusst vorgezogener Entwurf auf Grundlage ihrer bisherigen Website (echte Bilder, gekürzte Texte), damit Jakob und Charlotte etwas Sichtbares haben. Interview und Grundlage stehen aus.
- Der Nachname steht nirgends im Repo (auch nicht in Mailadressen oder Links), bis Charlotte zustimmt.

## Arbeitsweise
- Sprache: Deutsch, Du-Form, sofern unten nicht anders festgelegt.
- Drei Modi: „nur zeigen“ = Vorschau, nichts ändern. „Sag erst, was du machen würdest“ = Optionen mit Empfehlung, dann warten. „Mach“ = umsetzen, prüfen, live, kurz berichten.
- Vor Phase 4 kein Design und keine Inhalte. Erst Interview und freigegebene Grundlage (`_projekt/GRUNDLAGE.md`). Erlaubt ist ab Phase 1 nur das neutrale Gerüst (Handbuch Abschnitt 10).
- Inhaltstexte nie ungefragt umschreiben, nur Vorschläge machen. Technik, Abstände und Struktur selbst verbessern.
- Bei größeren Eingriffen (Layout-Umbau, Texte, SEO-Titel) erst Optionen nennen.
- Bei Unklarem eine präzise Rückfrage statt drei Annahmen.
- Ehrlich sagen, was nicht geprüft werden konnte (echtes iPhone, echte Schrift).
- Entscheidungen sofort in diese Datei oder `_projekt/STAND.md` schreiben, nicht nur im Chat lassen.

## Werke (Galerie)
- Werke nur in `tools/werke.json` ändern, danach `python3 tools/make-werke.py` ausführen. Das Skript baut die Galerie in `kunst.html` (zwischen den Marken `werke:start` und `werke:end`), die empfohlenen Werke auf der Startseite (`empfohlen:start`, `empfohlen:end`), eine Seite `werk-<slug>.html` pro Werk und die `sitemap.xml`. Werkseiten und Galerie nie von Hand ändern.
- Ein Eintrag hat: `slug` (nur Kleinbuchstaben und Bindestriche, einmalig), `titel`, `jahr`, `masse`, `technik`, `schlagworte` (Liste), optional `text`, `status` (leer, `verkauft`), `hinweis`, `empfohlen` (true/false) und `bilder` (Liste mit `datei` und `alt`). Mehrere Bilder pro Werk: weitere Einträge in `bilder`, die Seite zeigt sie untereinander (Gesamtansicht, Detail, im Raum).
- Neue Bilder als WebP, längste Seite höchstens 1000 px, in `images/` ablegen. Erstes Bild in `bilder` ist das Galerie-Bild.
- Preisanfrage geht per Mail-Link mit dem Werktitel im Betreff.

## Technik
- Statisches HTML, eine `styles.css`, eine `main.js`. Kein Framework, kein Build-Schritt.
- Bei Änderungen an `styles.css` oder `main.js` die Versionsnummer (`?v=...`) in allen HTML-Dateien hochzählen.
- Jede Änderung bei 390 px und 1280 px per Screenshot prüfen.
- Entwickeln auf eigenem Branch, live mit `git push origin <branch>:main`.
- Links relativ, ohne führenden Schrägstrich (die Seite liegt bis zur Domain unter `/<repo>/`). Keine `.nojekyll`-Datei.
- Bis zum Live-Gang `noindex` in allen HTML-Dateien und `Disallow: /` in `robots.txt`. Vor dem Live-Gang beides entfernen.
- Originalbilder nie ins Repo, nur verkleinerte Web-Versionen. Keine Fotos von Kundinnen, Kunden oder Retreat-Teilnehmenden ohne Einverständnis.
- Abstände zwischen Abschnitten bei Charlotte großzügig (Entscheidung von Jakob, anders als bei Essential Guidance). Variable `--luft` in `styles.css`.
- Schriften selbst hosten oder über Bunny Fonts, nie direkt von Google Fonts.
- Formulare nur, wenn sie wirklich senden. Sonst Mail-Link.
- FAQ sichtbar und als FAQPage-JSON-LD im `<head>`, beides angleichen. FAQ-Abschnitte mit grauem Hintergrund.
- Termine (falls vorhanden) nur in `tools/termine.json`, danach `python3 tools/make-ics.py`.
- `llms.txt` und `sitemap.xml` bei Änderungen an Angeboten, Preisen oder Seiten mitpflegen.

## Design
- `_projekt/DESIGN.md` ist ein lebendiges Stilbuch, kein starres Regelwerk. Es ist der Ausgangspunkt, Abweichungen sind erwünscht.
- Was Jakob oder die Kundin bewusst anders entscheiden, gilt. Nie zurückdrehen und nie in einen Standard- oder Skill-Look zurückfallen. Die Entscheidung sofort in `DESIGN.md` nachtragen, damit sie bleibt.
- Vor jedem Bericht: Screenshots bei 390 und 1280 px, selbst prüfen.
- Schrift: Titel und Beschriftungen in Typewriter (Courier Prime, passend zu ihrer Marke), Fließtext in Spectral. Nur so, sofern Charlotte nichts anderes festlegt.
- Textquellen: Alles, was Charlotte gesagt oder geschrieben hat, trennen von Vorschlägen. Vorschläge von Claude tragen im HTML `class="vorschlag"` (goldene Linie links). Vor dem Live-Gang gibt Charlotte jeden Vorschlag frei, ändert ihn oder streicht ihn, dann wird die Klasse entfernt. Die Quellen stehen in `_projekt/TEXTE.md`.
- Skill: `frontend-design`. Keine weiteren Skills ohne Rückfrage installieren.
- Texte nie ungefragt ändern, auch wenn ein Skill das nahelegt.
- Keine KI-Bilder von Menschen.
- Hintergrund zu Skills und Werkzeugen: `_werkstatt/HANDBUCH.md` Abschnitt 20.

## Datenschutz im Repo
- Das Repo ist öffentlich. Keine Interview-Transkripte, privaten Notizen, Preise der Zusammenarbeit, Passwörter oder privaten Adressen ins Repo.
- Ordner mit Unterstrich (`_projekt/`, `_werkstatt/`) werden nicht als Website ausgeliefert, sind auf GitHub aber sichtbar.

## Recht
- Impressum nach § 5 DDG: Name, ladungsfähige Anschrift, Kontakt. USt-IdNr. nur, wenn vorhanden. Nie Nummern erfinden.
- Datenschutzerklärung nennt jedes eingebundene Tool.
- [Bei Begleitungsangeboten: Hinweis „keine Heilkunde, ersetzt keine Therapie, Teilnahme in Eigenverantwortung“.]

## Marke (verbindlich, nach Phase 3 füllen)
- Dachmarke: [Name]. Angebote: [A], [B], [C].
- Schreibweisen: [...]
- Ort immer gleich: [Ort, Adresse].
- Alle Mail-Links an: [mail]. Betreff je nach Button.
- Wörter, die immer vorkommen: [...]
- Wörter, die nie vorkommen: [...]
- Die eine Handlung für Besucher: [...]
- Schriften: [Überschrift], [Fließtext]. Farben: [...]
