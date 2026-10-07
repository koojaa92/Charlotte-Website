# Charlotte: Projektstand und offene Punkte

Stand: 2026-10-07. Live: Entwurf unter https://koojaa92.github.io/Charlotte-Website/ (noindex). Phase: 0, vorgezogener Entwurf.
Feedbackrunden: 2 Entwürfe gezeigt.

## Was steht
- Seiten: Startseite, Generative Painting, Coaching, Teams und Führungskräfte, Kunst (Galerie mit 47 Werken, je eine eigene Seite), Über mich. Impressum und Datenschutz sind Platzhalter.
- Aufbau Startseite: Header mit ganzem Foto, vier Wege (Generative Painting, Coaching, Teams, Kunst), Methode in drei Schritten, Aus der Arbeit, drei empfohlene Werke, Über Charlotte, Erstgespräch.
- Gestaltung: ruhig, klar, Typewriter für Titel, Spectral für Text, viel Raum, ganze Header-Fotos mit goldener Zeile.
- Werke: `tools/werke.json` und `python3 tools/make-werke.py` (siehe CLAUDE.md).
- Texte: aus der bisherigen Website gekürzt, dazu Vorschläge (goldene Linie). Quellen: `_projekt/TEXTE.md`.
- Bilder: von ihrer bisherigen Website, verkleinert. Kein Foto von Kundschaft oder Retreat-Teilnehmenden.

## Offene Punkte
### Von der Kundin
- [ ] Wording der Angebote festlegen: Generative Painting (Methode und Marke), Coaching, Teams und Führungskräfte (Führungskräfte-Entwicklung, Teamentwicklung, Organisationsentwicklung)
- [ ] Du oder Sie in den Texten
- [ ] Alle Vorschläge (goldene Linie) freigeben, ändern oder streichen
- [ ] Neue Header-Bilder und Projektfotos liefern (die jetzigen sind teils veraltet)
- [ ] Zustimmung zur Nutzung ihrer Bilder und Werke im öffentlichen Repo
- [ ] Zu jedem Werk: Jahr, ggf. weitere Fotos (Detail, im Raum), Status verfügbar oder verkauft
- [ ] Entscheidung, ob Kundenliste und Kundenstimmen erscheinen
- [ ] Impressumsdaten, Kontaktadresse
### Von Jakob / Claude
- [ ] Charlotte beibringen, die Seite mit Claude Code zu pflegen (Werke, Texte, Bilder)
- [ ] Entscheidung eigene Kunstwebsite oder ein Auftritt: Empfehlung ein Auftritt unter einer Marke mit Kunst als eigenem Bereich. Eine eigene Seite lässt sich später über eine Unterseite oder Subdomain ergänzen.
- [ ] Squarespace-Auszug und Domain planen (Umleitungen von alten Adressen)
- [ ] Mailadresse: im Entwurf steht `hallo@example.org`
- [ ] Angabe „Geschäftsführerin von Freibaden Consulting“ von Charlotte bestätigen lassen
- [ ] Heilkunde-Hinweis für Coaching und Generative Painting klären (Handbuch Abschnitt 13)
- [ ] Preise, Termine, FAQ, Referenzen, Impressum, Datenschutz, `llms.txt`
- [ ] Vor Live-Gang: `noindex` und `Disallow: /` entfernen, Sitemap anpassen
### Später
- [ ] Englische und französische Fassung (Charlotte arbeitet dreisprachig)

## Entschieden (nicht wieder aufmachen)
- Galerie zeigt zunächst nur die Werke von „traces“ bis „love“ (18). Die übrigen bleiben in `tools/werke.json` mit `"sichtbar": false` und lassen sich wieder einblenden.
- Werkseite wie bei Kirsch: großes Hauptbild, bis zu zwei Ansichten daneben, weitere Bilder darunter, Vergrößern per Klick, Leiste zum vorigen und nächsten Werk. Kein Kontaktband auf Werkseiten.
- Instagram und LinkedIn sind kleine Knöpfe oben rechts, noch ohne Ziel (`class="platzhalter"`). Die Adressen enthalten ihren Nachnamen, darum erst nach ihrer Zustimmung eintragen. Es gibt zwei Instagram-Konten (art.space und creative.space), Charlotte wählt.
- Logo bleibt erhalten. Es enthält ihren Nachnamen, darum offen: Zustimmung zur Namensnennung im öffentlichen Repo.
- Drei Angebote: Generative Painting, Coaching, Teams und Führungskräfte. Dazu Kunst als eigener Bereich.
- Generative Painting ist Charlottes Methode und Marke.
- Galerie wie bei einer Künstlerseite: ganze Werke, eine Seite pro Werk, Preisanfrage, mehrere Bilder pro Werk möglich.
- Pflege über Claude Code durch Charlotte und Jakob, nicht über ein CMS im Browser.
- Schrift: Typewriter nur für Titel und Beschriftung, ruhige Schrift für Text.
- Abstände großzügig. Nur Vorname im Repo.
- Dieser Entwurf weicht bewusst von der Regel „vor Phase 4 kein Design“ ab, auf Jakobs Wunsch.
