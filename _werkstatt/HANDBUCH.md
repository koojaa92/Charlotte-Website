# Werkstatt-Handbuch: Websites mit Claude Code bauen

Für Jakob und für Claude. Baut auf dem Website-Playbook aus dem Projekt essential-guidance.space (Herbst 2026) auf und erweitert es für die Arbeit mit Kundinnen und Kunden.

Drei Dokumente gehören zusammen:

| Dokument | Für wen | Wo |
|---|---|---|
| Kunden-Handreichung | die Kundin, vor dem Interview | Claude-Doc, als PDF oder Google Doc verschicken |
| Werkstatt-Handbuch (dieses) | Jakob und Claude | `_werkstatt/HANDBUCH.md` im Vorlagen-Repo |
| `CLAUDE.md` | Claude Code, liest es bei jedem Start | Wurzel des Vorlagen-Repos |

---

## 1. Haltung

1. **Das Interview ist der Wert, nicht der Code.** Die Technik erledigt Claude. Was niemand automatisieren kann: zuhören, nachfragen, den Kern eines Menschen finden. Das ist das Angebot.
2. **Erst die Essenz, dann das Design.** Klar wird eine Website, wenn klar ist, wer der Mensch ist, was er anbietet und was nicht. Das klärt das Interview, nicht eine Layout-Runde.
3. **Live von Anfang an.** Früh online, dann am echten Handy verfeinern.
4. **Eine Quelle der Wahrheit pro Thema.** Regeln in `CLAUDE.md`, Stand in `_projekt/STAND.md`, Termine in einer Datei. Nie dieselbe Info an zwei Orten.
5. **Die Inhalte gehören dem Menschen.** Claude schlägt Texte vor, schreibt sie aber nie ungefragt um. Technik, Abstände und Struktur darf Claude selbst verbessern.
6. **Weniger ist mehr.** Wenige Seiten, Schriften, Farben, Tools. Jedes Tool ist ein Konto, ein Login und eine Datenschutzzeile mehr.
7. **Befähigen statt abhängig machen.** Am Ende kann die Kundin Kleinigkeiten selbst ändern.

---

## 2. Das Angebot

**Für wen:** Solo-Selbstständige, die ihr Geschenk in die Welt bringen und sichtbar machen wollen.

**Jakobs Rolle:** Zuhörer, Gestalter, Umsetzer, bei Bedarf Fotograf, Website-Bauer. Ziel ist, dass die Kundin ihre Seite später selbst pflegen kann.

**Was dazugehört:** Neue Websites, gebaut mit Claude Code. Code und Hosting immer auf GitHub (GitHub Pages), keine anderen Plattformen. Die Domain darf bei jedem Anbieter liegen.

**Jede Website ist anders.** Andere Menschen, andere Ziele, andere Funktionen: eine ruhige Visitenkarte, eine Seite mit Terminen und Tickets, ein Portfolio, eine Seite für Buchungen von Einzelsitzungen. Dieses Handbuch ist ein Werkzeugkasten, kein Bauplan. Die Beispiele stammen aus essential-guidance.space und gelten nur, wo sie zur Person passen.

**Was nicht dazugehört:** Bestehende Websites übernehmen oder reparieren (WordPress, Wix, Squarespace). Alte Texte und Bilder dürfen Material sein, der Code nicht.

**Umfang und Feedbackrunden:** Paket, Preis und Zahl der Feedbackrunden stehen im Angebot an die Kundin, nicht in diesem Repo. Ohne vereinbarte Grenze wird jedes Projekt so lang wie das erste.

**Eigene Marke:** Das Angebot bekommt eine eigene Website. Name: [offen].

---

## 3. Werkzeuge und wie sie zusammenhängen

GitHub ist der Speicher, GitHub Pages zeigt den Inhalt als Website, die Domain ist das Türschild, der DNS-Eintrag beim Domain-Anbieter leitet das Türschild auf die Website, Claude Code ist der Handwerker, der im Speicher arbeitet.

| Werkzeug | Wofür | Learning |
|---|---|---|
| **Claude / Claude Code** | Claude für Interview-Auswertung und Texte, Claude Code baut, prüft per Screenshot, stellt live | Braucht mindestens Claude Pro (rund 20 US-Dollar im Monat, günstiger jährlich; aktuellen Preis auf claude.com/pricing prüfen). Claude Code ist in allen bezahlten Plänen enthalten. Im Auftritt „Claude und Claude Code“ sagen, nicht „die KI“. Arbeitet auf einem Entwicklungszweig und schiebt nach `main`. `main` ist live. |
| **GitHub** (Repo) | Speichert den Code, jede Änderung als Version | Für kostenloses GitHub Pages muss das Repo **öffentlich** sein. Nichts Privates ins Repo (siehe Abschnitt 4). |
| **GitHub Pages** | Hosting, kostenlos | Ordner mit Unterstrich (`_projekt/`, `_werkstatt/`) werden nicht als Website ausgeliefert, sind auf GitHub aber sichtbar. |
| **Domain-Anbieter** (z. B. Cloudflare, Strato, IONOS) | Domain, DNS | Jeder Anbieter funktioniert. Bei neuen Domains Cloudflare empfehlen: Kauf und DNS an einem Ort, schnelle Umstellung. Hat die Kundin schon eine Domain, bleibt sie erst einmal, wo sie ist (Abschnitt 16). Einträge immer gleich: vier A-Einträge `185.199.108.153` bis `185.199.111.153`, CNAME `www` → `<user>.github.io`, dazu die Datei `CNAME` im Repo. Mit und ohne www testen. **Cloudflare Pages wird nicht gebraucht.** |
| **Google Docs** (Connector) | Alle Website-Texte an einem Ort, gegliedert wie die Seite | Hat sich bewährt. Claude hält das Doc per Connector automatisch aktuell, die Kundin kommentiert am Satz, Gegenleser brauchen keine Technik. Auf dem Google-Konto der Kundin anlegen, mit Jakob teilen. |
| **GoatCounter** | Besucherstatistik ohne Cookies | Kein Cookie-Banner nötig. In der Datenschutzerklärung nennen. |
| **Search Console / Bing Webmaster** | Gefunden werden | Sitemap einreichen. Bing zählt, weil ChatGPT und Copilot den Bing-Index nutzen. |
| **Ticketing** (z. B. Eventfrog) | Tickets | Pro Termin verlinken. Kein eigenes Bezahlsystem. |
| **Newsletter-Tool** | Später | Erst einrichten, wenn wirklich verschickt wird. Bis dahin ein Mail-Link. |

**Nur bei Cloudflare – die Wolke:** Steht im DNS eine orange Wolke („Proxied“), laufen Besucher über Cloudflare, dann gehört Cloudflare in die Datenschutzerklärung. Graue Wolke („DNS only“) heißt: nur Adressbuch.

**Klickanleitungen** für fremde Oberflächen immer Klick für Klick, mit dem genauen Menünamen. Oberflächen ändern sich: lieber um einen Screenshot bitten als aus dem Gedächtnis beschreiben.

---

## 4. Konten, Zugriff, Übergabe

**Grundsatz:** Alle Konten laufen auf die Kundin. Jakob bekommt Zugriff.

| Konto | Auf wen | Jakobs Zugriff |
|---|---|---|
| GitHub | Kundin | als Collaborator eingeladen |
| Domain-Anbieter (Domain, DNS) | Kundin | als Mitglied eingeladen, wenn der Anbieter das kann. Sonst stellt die Kundin die Einträge gemeinsam mit Jakob ein. |
| Google (Text-Doc, Search Console) | Kundin | Doc geteilt, in der Search Console als Nutzer |
| GoatCounter | Kundin | als Nutzer hinzugefügt |
| Claude Pro | Kundin, erst zur Übergabe | keiner, Jakob arbeitet mit seinem eigenen Konto |

**Wie Claude Code an ein Repo kommt** (Stand Oktober 2026, beim ersten Kundenprojekt einmal durchtesten)
- Claude Code verbindet sich über die Claude-GitHub-App mit GitHub. Lesen geht bei jedem öffentlichen Repo. **Schreiben und live stellen** geht nur bei Repos, auf denen die App installiert ist und auf die das verbundene GitHub-Konto Schreibrechte hat.
- Ein neues Repo kann Claude Code nicht selbst anlegen. Das macht Jakob oder die Kundin auf GitHub mit „Use this template“.

**Zwei Wege**

- **Weg A, erst bei Jakob bauen, dann übertragen (empfohlen):**
  1. Jakob legt das Repo in seinem GitHub aus der Vorlage an. Claude Code arbeitet darin wie bei seinem eigenen Projekt.
  2. Gebaut und geprüft wird unter `<jakob>.github.io/<repo>`. Die Kundin sieht den Stand jederzeit am Handy.
  3. Zur Übergabe: GitHub → Settings des Repos → „Transfer ownership“ an das Konto der Kundin. Code, gesamte Versionsgeschichte und Einstellungen ziehen mit. Den alten Link leitet GitHub weiter.
  4. Danach im neuen Repo prüfen: GitHub Pages aktiv, eigene Domain eingetragen, HTTPS an. DNS bei der Domain auf `<kundin>.github.io` umstellen.
  5. Die Kundin lädt Jakob als Collaborator ein und installiert die Claude-GitHub-App auf ihrem Repo. Dann können beide mit Claude Code weiterarbeiten.
  Vorteil: Die Kundin braucht ihre Konten erst am Ende, und Jakob hat im Bau keine Zugriffsfragen.
- **Weg B, direkt bei der Kundin:** Kundin legt GitHub-Konto und Repo an, installiert die Claude-GitHub-App für dieses Repo und lädt Jakob als Collaborator ein. Mehr Einrichtung am Anfang, dafür keine Übertragung am Ende.

**Zusammenarbeit**
- Immer nur eine Person arbeitet gleichzeitig an der Seite, sonst überschreiben sich Änderungen. Kurz absprechen, wer gerade dran ist.
- Alles Wichtige steht in `CLAUDE.md` und `_projekt/STAND.md`. So weiß jede neue Claude-Code-Sitzung Bescheid, egal ob Jakob oder die Kundin sie startet.
- Texte gegenlesen läuft über das Google Doc, nicht über GitHub.

**Was nie ins Repo gehört** (es ist öffentlich): Interview-Aufnahmen und Transkripte, persönliche Notizen, Preise der Zusammenarbeit, Rechnungen, Passwörter, private Adressen, die nicht ins Impressum gehören. Diese liegen bei Jakob (lokal oder in einem privaten Ordner). Ins Repo kommt nur das Destillat: Regeln in `CLAUDE.md`, Stand in `_projekt/STAND.md`.

**Neues Repo anlegen:** Das macht Jakob auf GitHub mit „Use this template“ im Vorlagen-Repo `website-werkstatt`. Claude Code kann kein Repo anlegen und keine Repo-Einstellungen ändern (Template-Häkchen, Pages, Transfer). Ist die Claude-Code-Sitzung in einem anderen Repo gestartet, muss das neue Repo ausdrücklich angebunden werden.

**Die Kundin nicht vorschnell als Collaborator einladen.** Collaborators haben Schreibrechte auf `main`, also auf die öffentliche Seite. In der Bauphase braucht sie nur den Vorschau-Link.

**Fremdes Google Doc:** Der Connector arbeitet mit Jakobs Rechten. Teilt die Kundin ihr Doc mit ihm, kann Claude es lesen, mit Bearbeiten-Recht auch schreiben. (Noch nicht getestet.)

---

## 5. Der Ablauf

Phasen 0 bis 3 sind fertig, **bevor** der erste Entwurf entsteht. Das ist der wichtigste Hebel gegen das Klein-Klein.

**Phase 0: Vorgespräch und Angebot**
- Kurzes Kennenlernen. Passt das Projekt (neu bauen, Solo-Selbstständig)?
- Paket, Preis und Zahl der Feedbackrunden schriftlich festhalten.
- Bestandsaufnahme: Gibt es eine Domain, wo liegt sie, hängt E-Mail daran, gibt es eine alte Website, wird sie bei Google gefunden? Wenn ja: Abschnitt 16.
- Kunden-Handreichung schicken.

**Phase 1: Vorbereitung der Kundin**
- Checkliste aus der Handreichung: Absicht, Referenzseiten, Angebote, Fotos, vorhandene Texte, Pflichtangaben, Kanäle.
- Zugänge geprüft: Die Kundin kann sich bei Domain-Anbieter, alter Website, Mailpostfach und Google wirklich einloggen.
- Tor: Material liegt vor. Fehlt viel, wird das Interview verschoben, nicht der Entwurf vorgezogen.
- Parallel bei Jakob, ohne Design und Inhalt: Repo aus der Vorlage anlegen, CLAUDE.md „Projekt“ und `_projekt/STAND.md` füllen, das **neutrale Gerüst** bauen (Abschnitt 10), GitHub Pages aktivieren. Ergebnis: ein Vorschau-Link unter `<user>.github.io/<repo>`, der später nur noch gefüllt wird.

**Phase 2: Interview**
- Live, alternativ per Zoom. Mit Einwilligung aufnehmen, transkribieren lassen.
- Leitfaden in Abschnitt 6.
- Transkript an Claude geben, nicht ins Repo legen.

**Phase 3: Grundlage festlegen**
- Website-Typ, Ziel und Funktionen festlegen (Abschnitt 7).
- Claude fasst zusammen: Seitenliste, Angebote mit Preis, Ort, Zeit, Anmeldung. Markenarchitektur (Dachmarke, Angebote, Schreibweisen). Wörter, die immer und nie vorkommen. Die eine Handlung, die Besucher tun sollen.
- Referenzseiten auswerten und daraus `_projekt/DESIGN.md` ableiten (Abschnitt 20).
- Drei Varianten für den Anfang der Startseite (Hero) als Screenshot. Die Kundin wählt eine.
- `CLAUDE.md` mit den Marken-Regeln füllen, `_projekt/STAND.md` pflegen.
- Tor: Kundin gibt Grundlage und Hero-Variante frei.

**Phase 4: Erster Entwurf und Live-Gang**
- Das Gerüst füllen: Struktur nach Abschnitt 7, Texte aus dem Interview, Gestaltung nach `DESIGN.md`.
- Domain verbinden, sobald die Kundin mit dem Stand zufrieden ist (Abschnitt 16). Vorher reicht die github.io-Adresse.
- Link an die Kundin: am eigenen Handy ansehen.

**Phase 5: Feedbackrunden (vereinbarte Anzahl)**
- Pro Runde eine gesammelte Liste der Kundin, Claude setzt um, Jakob prüft, live.
- Reihenfolge: Inhalte und Angaben vor Geschmack.

**Phase 6: Technik, SEO, Recht**
- Strukturierte Daten, Sitemap, `llms.txt`, Search Console, Bing, Impressum, Datenschutz (Abschnitte 10 und 13).

**Phase 7: Übergabe und Befähigung**
- Konten prüfen, Zugriffe klären.
- Der Kundin zeigen, wie sie mit Claude Code selbst ändert (Abschnitt 15).
- `STAND.md` auf den Endstand bringen.

---

## 6. Interview-Leitfaden

Ziel: konkret, greifbar, ehrlich. Ruhig konfrontierend fragen. Die echten Worte der Kundin sind das Rohmaterial für die Texte.

**Ein Fragenpool, kein Fragebogen.** Für jede Person wird der Leitfaden neu zusammengestellt: je nachdem, wer sie ist, was sie anbietet und wo sie gerade steht. Wer noch sucht, braucht mehr Kern-Fragen. Wer klar ist, braucht mehr Praktisches. Tipp: Vor dem Interview Claude die Vorbereitung der Kundin geben und sagen: „Stell aus dem Fragenpool einen Leitfaden für diese Person zusammen.“

**Einstieg**
1. Was soll die Website für dich tun? Woran merkst du in einem Jahr, dass sie wirkt?
2. Wer soll sie lesen? Beschreib einen Menschen, für den du das machst.

**Kern**
3. Was machst du, in einem Satz, so dass deine Oma es versteht?
4. Was zieht sich durch alle deine Angebote?
5. Wofür willst du *nicht* gehalten werden?

**Pro Angebot**
6. Was passiert konkret, von der Ankunft bis zum Gehen? In Schritten.
7. Für wen ist es, und für wen ausdrücklich nicht?
8. Was nimmt jemand mit, wenn es gut lief? Und wenn es nur okay war?
9. Was unterscheidet dich von ähnlichen Angeboten in deiner Stadt? Gibt es eine Lücke (Wochentag, Format, Zielgruppe)?
10. Preis, Ort, Zeit, Dauer, Anmeldung, was ist inklusive?
11. Welche drei Fragen stellen Menschen dir immer wieder? (Wird zur FAQ.)

**Person und Haltung**
12. Was hat dich geprägt: Lehrer, Methoden, Wendepunkte?
13. Wie hältst du einen Raum? Was tust du, wenn es schwierig wird?
14. Was ist deine Vision, größer als dein Angebot?
15. Ein persönliches Detail, das dich menschlich macht.

**Sprache und Bild**
16. Welche Wörter benutzt du gern, welche magst du gar nicht?
17. Was genau gefällt dir an deinen Referenzseiten? Was stößt dich ab?
18. Welche Fotos gibt es, wer ist darauf, sind die Rechte geklärt? Braucht es ein Fotoshooting?

**Gestaltung**
- Wie soll sich die Seite anfühlen? Drei Wörter. Welche Ruhe, welches Tempo soll sie vermitteln?
- One-Pager zum Durchscrollen, Startseite mit Unterseiten, oder etwas ganz Eigenes?
- Wie viel Bewegung: keine Animationen, sanftes Einblenden, oder mehr?
- Dicht oder luftig? (Zeigen statt fragen: zwei Referenzseiten nebeneinander.)

**Praktisches**
19. Kontaktweg und Mailadresse.
20. Was gibt es schon: Ticketing, Newsletter, Social Media? Was kommt später?
21. Impressum: Name, Anschrift, USt-IdNr. (falls vorhanden).
22. Rechtlich heikle Begriffe: Therapie, Heilung, Coaching? Braucht es einen Hinweis „keine Heilkunde“?

**Nachfrage-Werkzeuge**
- „Was meinst du damit konkret?“
- „Gib mir ein Beispiel von letzter Woche.“
- „Wenn du nur einen Satz hättest?“
- „Was würde jemand sagen, der dich gut kennt?“

---

## 7. Struktur, die funktioniert

**Erst den Typ klären, dann die Struktur.** Ziel und Funktionen der Website bestimmen den Aufbau, nicht diese Vorlage. Fragen dazu:
- Was soll die Seite leisten: informieren, Vertrauen aufbauen, Anmeldungen holen, Buchungen, Verkauf?
- One-Pager zum Durchscrollen, Startseite mit Unterseiten, oder etwas ganz Eigenes?
- Welche Funktionen braucht es wirklich: Termine, Tickets, Kontakt, Newsletter, Galerie, Musik, Video?

Was folgt, ist das Muster aus essential-guidance.space: eine Angebots-Website mit mehreren Formaten und Terminen. Ein guter Ausgangspunkt für ähnliche Seiten, aber kein Muss.

**Seiten:** Startseite · eine Seite pro Angebot · Über mich · Termine (falls es Termine gibt) · Impressum · Datenschutz.

**Startseite von oben nach unten**
1. Hero, genau einen Bildschirm hoch: Slogan, Zeile mit den Angeboten, kurzer Absatz, zwei Buttons.
2. „Was ist [Marke]?“: ein bis zwei Absätze Essenz.
3. Nächste Termine, falls vorhanden, automatisch aktuell.
4. Ein Block pro Angebot, immer gleich: Überzeile mit Art (`Tanz · Sonntags 17–20 Uhr · Ort`), Titel, Claim, kurzer Text, zwei Buttons („Mehr erfahren“ + konkrete Handlung).
5. Bleib in Verbindung: Kanäle, dann Footer.

**Angebotsseite:** Hero mit Überzeile · Einstieg mit Infobox (Wo, Wann, Preis, Inklusive, Anmeldung) · Ablauf in Schritten · Haltung · Was es ausmacht · Termine (nur die nächsten drei) · FAQ · Hinweis.

**Muster**
- Jede Unterseite hat dieselbe Abfolge.
- FAQ immer am Ende, grauer Hintergrund.
- Preis-Hinweise dort, wo die Entscheidung fällt (unter den Terminen).
- Mail-Buttons mit vorausgefülltem Betreff je nach Zweck.

---

## 8. Texte

- **Konkret vor schön.** Erst Ort, Zeit, Ablauf, dann Bedeutung.
- **Startseite kurz, Unterseiten dürfen ausführlich sein.**
- **Die Sprache der Kundin** aus dem Interview, keine Marketingfloskeln.
- **Feste Schreibweisen** in `CLAUDE.md`: Markennamen, Ort, Mailadresse.
- **Heikle Wörter klären** (Therapie, Heilung, Coaching). Bei Bedarf nur verneinend in der FAQ.
- **Fremde Markennamen** nur beschreibend („inspiriert von …“), nie im Titel.
- **Kurz in Überschriften:** „begegnest“ statt „begegnen kannst“.
- **FAQ doppelt:** sichtbar und als FAQPage-JSON-LD im `<head>`.
- **Alt und Neu nebeneinander** im Google Doc zeigen, die Kundin kommentiert.

---

## 9. Design

Erfahrungen, keine Regeln. Die Gestaltung folgt der Person: Ruhe, Tempo und Farbigkeit kommen aus dem Interview und den Referenzseiten, nicht aus der letzten Website.

**Referenzseiten zuerst.** Mit drei Referenzen und einem Satz „was genau gefällt“ spart man mehr Runden als mit jeder Beschreibung.

**Schrift**
- Zwei Schriften: Überschriften und Fließtext.
- Immer in Originalgröße auf der echten Seite vergleichen, nummeriert nebeneinander. Nie nach Beschreibung wählen.
- DSGVO-freundlich laden: selbst hosten oder Bunny Fonts. Nie Google Fonts direkt.

**Farben:** Wenige (Grundfarbe, Papier, ein Akzent), als CSS-Variablen.

**Abstände:** Eng statt großzügig. Eine globale Abstandsregel am Ende der CSS. Mehr Abstand zwischen Überschrift und Text, weniger zwischen Abschnitten.

**Bilder**
- Ein Format pro Bereich, Kacheln gleich groß.
- Ähnliche Farbstimmung, leicht entsättigt.
- Personen schauen zum Text hin.
- Am Handy lieber quadratisch oder leicht hochkant.

**Bildschirm-Logik**
- Hero füllt genau den ersten Bildschirm, Desktop und Handy.
- Am Handy füllt jedes Angebot einen Bildschirm, sanftes Einrasten.
- Am Desktop der Mittelweg: Angebot mittig und groß, Nachbarn schauen schmal herein.

---

## 10. Technik (für Claude Code)

**Grundaufbau**
- Statisches HTML, eine `styles.css`, eine `main.js`. Kein Framework, kein Build-Schritt.
- `styles.css?v=...` und `main.js?v=...` in allen HTML-Dateien hochzählen.
- Neue CSS-Regeln ans Ende, auf Spezifität achten.

**Das neutrale Gerüst** (Phase 1, passt in jedes Projekt)
- Drei Seiten: Start („Website im Aufbau“), Impressum, Datenschutz. `styles.css` mit Farb- und Schrift-Variablen als Platzhalter, `main.js` misst die Kopfzeilenhöhe.
- Kein Design, keine Inhalte. Das Gerüst darf nichts vorwegnehmen.
- `noindex` in jeder HTML-Datei und `Disallow: /` in `robots.txt`, damit Google keinen Entwurf erfasst. **Vor dem Live-Gang beides entfernen.**
- Links relativ und ohne führenden Schrägstrich. Eine Projektseite liegt unter `/<repo>/`, absolute Pfade brechen dort.
- Keine `.nojekyll`-Datei anlegen. Ohne sie liefert GitHub Pages Ordner mit Unterstrich (`_projekt`, `_werkstatt`) nicht aus. Das ist gewollt.
- `sitemap.xml` zuerst mit der github.io-Adresse, nach Domain-Umzug oder Repo-Übertragung ersetzen.

**GitHub Pages aktivieren** (kann nur der Repo-Besitzer)
Settings → Pages → Source „Deploy from a branch“ → Branch `main`, Ordner `/ (root)` → Save. Direkt danach zeigt die Adresse noch „404“, der erste Bau dauert ein bis zwei Minuten. Eine Domain braucht man dafür nicht.

**Bilder**
- Originalbilder bleiben außerhalb des öffentlichen Repos (bei Jakob oder im Claude-Projekt). Ins Repo kommen nur ausgewählte, für das Web verkleinerte Versionen.

**Handy und iOS Safari**
- Vollbild-Abschnitte mit `lvh` und etwas Polster unten.
- Kopfzeilenhöhe per JS messen, als `--kopf` setzen.
- `scroll-snap-type: y proximity`, nie `mandatory`.
- `text-wrap: balance` für Überschriften, `pretty` für Text, plus geschütztes Leerzeichen zwischen den letzten zwei Wörtern.

**Prüfen vor jedem Live-Gang**
- Playwright-Screenshots bei 390 px und 1280 px, bei Layoutfragen auch 1440 px.
- Lokal mit `python3 -m http.server`.
- Fallback-Schriften und blasse Einblend-Animationen im Screenshot sind kein Fehler, aber dazusagen.

**Termine automatisieren** (falls es Termine gibt)
- `tools/termine.json` als einzige Quelle.
- `tools/make-ics.py` erzeugt Karten, Kalenderdateien, Event-JSON-LD. Karten nie von Hand ändern.
- Vergangene Termine per JS ausblenden. Ohne Ticketlink: „Tickets folgen“.
- Vorlage: Repo `koojaa92/Website-Essential-Guidance`, Ordner `tools/`.

**Daten für Maschinen:** JSON-LD (Organisation, Person, Angebot, Events, FAQPage), `sitemap.xml`, `robots.txt`, `llms.txt`.

**Arbeitsweise im Repo**
- Eigener Branch, live mit `git push origin <branch>:main`.
- Entscheidungen sofort in `CLAUDE.md` oder `STAND.md`, nicht nur im Chat. Lange Chats werden zusammengefasst und vergessen Details.

---

## 11. Gute Prompts

Ein guter Prompt sagt: **was**, **wo**, **wie es sein soll**, und **ob umgesetzt oder nur gezeigt** wird.

**Schwach:** „Mach die Startseite schöner.“
**Stark:** „Startseite, Hero: Slogan eine Stufe kleiner, Abstand zum Button halbieren. Umsetzen, bei 390 und 1280 px prüfen, live stellen.“

**Vor dem Absenden prüfen:** Steht noch ein Platzhalter wie `[hier einfügen]` im Prompt? Dann kommt der Inhalt nie an, und Claude arbeitet ohne ihn weiter. Ist bei Bettina passiert.

**Chats teilen kein Gedächtnis.** Verschiedene Chats verbinden sich nur über Dateien: `CLAUDE.md` und `STAND.md` im Repo sowie das Google Doc. Was ein anderer Chat wissen soll, gehört in eine dieser Dateien.

**Drei Modi klar benennen**
- „**Nur zeigen**, nicht umsetzen“ → Vorschau als Screenshot.
- „**Sag erst, was du machen würdest**“ → Optionen mit Empfehlung, dann warten.
- „**Mach**“ → umsetzen, prüfen, live, kurz berichten.

**Start-Prompt für ein neues Projekt** (nach „Use this template“)
```
Neue Website für [Name], [Angebot] in [Stadt].
Lies CLAUDE.md und _werkstatt/HANDBUCH.md.
Repo: [owner/repo]. Domain: [domain oder noch offen].
Wir sind in Phase [Nummer]. [Material: Transkript, Fotos, Referenzseiten folgen.]
```

**Grundlage aus dem Interview erstellen**
```
Hier ist das Interview-Transkript. Erstelle die Grundlage nach Phase 3:
Seitenliste, Angebote mit allen Angaben, Markenarchitektur, Schreibweisen,
Wörter immer/nie, die eine Handlung. Markiere, was fehlt.
Noch keinen Code. Danach CLAUDE.md und _projekt/STAND.md füllen.
```

**Texte schreiben**
```
Schreib die Texte für [Seite] aus dem Transkript. Sprache der Kundin übernehmen,
keine Floskeln, konkret vor schön. Alt und Neu nebeneinander ins Google Doc.
```

**Feedback einarbeiten**
```
Hier die Feedbackrunde [Nummer] als Liste. Ordne nach Seiten, setze Punkt für Punkt um,
prüfe bei 390 und 1280 px, stell live. Sag am Ende, was offen bleibt.
```

**Nützliche Sätze**
- „Jetzt ist es zu extrem. Finde einen Mittelweg.“
- „Zeig mir drei Schriften in Originalgröße nebeneinander, nummeriert.“
- „Das ist am Handy angeschnitten. Jeder Abschnitt soll auf einen Bildschirm passen.“
- „Schreib alles in STAND.md, ich mache später weiter.“
- „Gleiche das Google Doc mit dem aktuellen Stand ab.“

**Modellwahl:** Opus für Grundlage und Texte. Sonnet für das Bauen und Feedbackrunden. Haiku für kleine Korrekturen.

---

## 12. Das Klein-Klein begrenzen

Man wird es nicht los. Man kann es begrenzen:

1. **Tore einhalten.** Kein Entwurf ohne Interview, Material und freigegebene Grundlage.
2. **Runden zählen.** Feedback kommt gesammelt pro Runde. Die Zahl steht im Angebot.
3. **Inhalt vor Geschmack.** Erst Angaben und Texte, dann Farben und Abstände.
4. **Referenz statt Beschreibung.** „Wie auf Seite X“ schlägt drei Absätze Erklärung.
5. **Mittelweg anfordern** statt zwischen Extremen hin und her.
6. **„Entschieden“ in STAND.md.** Was entschieden ist, wird nicht wieder aufgemacht.
7. **Gut genug erkennen.** Wenn Struktur, Texte und Handy-Ansicht stimmen, ist die Seite fertig.

---

## 13. Recht und Pflichtangaben (Deutschland, keine Rechtsberatung)

- **Impressum:** vollständiger Name, ladungsfähige Anschrift, Kontakt. USt-IdNr. nur, wenn vorhanden. Normale Steuernummer gehört nicht hinein. Nie Nummern erfinden. Rechtsgrundlage heute § 5 DDG (nicht mehr TMG).
- **Datenschutz:** jedes eingebundene Tool nennen (Hosting, Domain, Statistik, Player, Fonts, Ticketing). Tools ohne Cookie-Banner wählen.
- **Schriften:** nie direkt von Google Fonts laden (Urteil LG München 2022).
- **Formulare:** nur, wenn sie wirklich senden. Sonst Mail-Link.
- **Newsletter:** Double-Opt-in, Abmeldelink, Datenschutz anpassen.
- **Begleitungsangebote:** Hinweis „keine Heilkunde, ersetzt keine Therapie, Teilnahme in Eigenverantwortung“.
- **Fotos:** Rechte und Einwilligung der abgebildeten Personen, schriftlich.
- **Interview-Aufnahme:** nur mit Einwilligung, außerhalb des Repos speichern, nach Projektende löschen oder archivieren wie vereinbart.
- **Affiliate-Links** kennzeichnen. **Musikveranstaltungen:** GEMA bedenken.

---

## 14. Zeitfresser (aus dem eigenen Projekt)

- **Im Artefakt bauen.** Für eine wachsende Website zu langsam und unhandlich. Gleich mit Claude Code und Repo starten.
- **Zwei Domain-Anbieter gleichzeitig.** Neue Domains direkt dort kaufen, wo auch das DNS liegt.
- **„Cloudflare Pages“ suchen.** GitHub Pages reicht.
- **Newsletter-Tool vor dem ersten Newsletter.**
- **Schriftwahl nach Beschreibung.**
- **Extreme Layouts** (komplett bildschirmfüllend, viel Weißraum).
- **Alles im Chat lassen** statt in `CLAUDE.md` und `STAND.md`.
- **Platzhalter und tote Formulare** bis kurz vor Livegang stehen lassen.
- **Perfektionismus.** Die Website lebt von den Angeboten.

---

## 15. Übergabe: die Kundin befähigen

Ziel: Die Kundin ändert Termine, Texte und Bilder selbst mit Claude Code.

1. Kundin schließt Claude Pro ab und verbindet ihr GitHub mit Claude Code, dazu den Google-Docs-Connector für ihr Text-Doc.
2. Gemeinsame Übungsrunde: eine kleine Textänderung, eine Terminänderung, ein Bildtausch.
3. Sie bekommt drei Sätze an die Hand:
   - „Lies CLAUDE.md. Ändere [was] auf [Seite]. Prüfe bei 390 und 1280 px und stell live.“
   - „Nur zeigen, nicht umsetzen: Wie sähe es aus, wenn …?“
   - „Dreh die letzte Änderung zurück.“
4. Grenze klären: Was macht sie selbst, wofür meldet sie sich bei Jakob (Struktur, neue Seiten, Recht)?
5. `CLAUDE.md` ist ihre Gebrauchsanweisung. Sie bleibt im Repo und wächst mit.

---

## 16. Bestehende Domain und alte Website: umziehen, ohne etwas zu verlieren

Gilt, wenn die Kundin schon eine Domain hat, besonders wenn E-Mail daran hängt oder die alte Seite bei Google gefunden wird. Oberflächen und Regeln der Anbieter ändern sich: jeden Schritt beim konkreten Anbieter nachprüfen, nicht aus dem Gedächtnis.

**Die zwei Dinge, die man nicht verwechseln darf**
- **DNS umstellen:** Die Domain bleibt beim alten Anbieter, nur die Einträge zeigen auf GitHub Pages. Schnell, risikoarm, jederzeit umkehrbar. **Der Standardweg.**
- **Domain übertragen (Transfer):** Die Domain wechselt den Anbieter. Nur sinnvoll, wenn die Kundin den alten Anbieter loswerden will. Erst machen, wenn die neue Seite stabil läuft.

**Bestandsaufnahme vorher (Pflicht)**
1. Wo liegt die Domain, und wo liegt ihr DNS? (Nicht immer derselbe Anbieter.)
2. **Alle DNS-Einträge sichern** (Screenshot oder Export): A, CNAME, **MX** (E-Mail), **TXT** (Google-Bestätigung, SPF, DKIM), Subdomains.
3. **Hängt E-Mail an der Domain?** Wenn ja: Wo liegt das Postfach? Das ist das größte Risiko. Falsche oder fehlende MX-Einträge heißt: Mails kommen nicht an, und niemand merkt es sofort.
4. **Alte URLs sammeln:** alte Sitemap, Search Console (Seiten mit Klicks), Suche `site:domain.de` bei Google.
5. Laufzeit und Kündigungsfrist beim alten Anbieter. Manche Anbieter löschen die Domain bei Kündigung des Pakets mit.

**Ablauf DNS-Umstellung**
1. Neue Seite fertig bauen und unter `<user>.github.io/<repo>` prüfen.
2. Weiterleitungskarte anlegen: jede alte URL mit Besuchern → passende neue URL.
3. TTL der Einträge am Vortag senken (z. B. auf 5 Minuten), damit die Umstellung schnell greift.
4. Nur A-Einträge und `www`-CNAME ändern. **MX und TXT unverändert lassen.**
5. Im Repo die Datei `CNAME` mit der Domain anlegen, in GitHub Pages die Domain eintragen, „Enforce HTTPS“ aktivieren, sobald verfügbar. Das Zertifikat kann eine Weile dauern.
6. Testen: mit und ohne www, https, eine Testmail an die Kundin und eine von ihr zurück.
7. Alte Website erst kündigen, wenn alles eine Woche ruhig läuft.

**Weiterleitungen (301)**
- GitHub Pages kann keine echten Serverweiterleitungen pro Pfad. Notlösung: kleine HTML-Seite unter dem alten Pfad mit Meta-Refresh und Canonical auf die neue Seite.
- Sauberer: Domain-DNS bei Cloudflare mit Proxy (orange Wolke) und dort Weiterleitungsregeln für die alten Pfade. Dann Cloudflare in der Datenschutzerklärung nennen.
- Bleiben Domain und wichtige Pfade gleich, ist für Google fast nichts zu tun.

**Domain-Transfer zu einem anderen Anbieter (optional, später)**
- Nur, wenn die Kundin es will. Die Website braucht den Transfer nicht.
- Prüfen, ob der neue Anbieter die Endung unterstützt.
- Alle DNS-Einträge beim neuen Anbieter vorab anlegen und kontrollieren (vor allem MX und TXT).
- Beim alten Anbieter Transfersperre aufheben und den Auth-Code holen, Transfer beim neuen Anbieter starten.
- Bei Cloudflare zusätzlich: Domain zuerst als Site anlegen und die Nameserver umstellen, erst dann den Transfer starten.
- Nach Registrierung oder Transfer gilt oft eine Sperre von 60 Tagen für weitere Transfers.
- E-Mail-Postfach: Zieht man vom Paketanbieter weg, braucht das Postfach oft ein neues Zuhause. Vorher klären, nicht nachher.

**Google und Co. nach dem Umzug**
- Search Console: Domain-Property per TXT-Eintrag bestätigen (überlebt Anbieterwechsel), neue Sitemap einreichen.
- Neue Domain statt alter: in der Search Console „Adressänderung“ ausführen, alte Domain dauerhaft per 301 weiterleiten.
- Links aktualisieren: Google-Unternehmensprofil, Instagram, Ticketing, Partnerseiten.
- Nicht Domain, Struktur und Texte gleichzeitig radikal ändern, wenn die alte Seite gut gefunden wird. Lieber in Schritten.

---

## 17. Gefunden werden (zweiter Schritt)

Kommt nach dem Live-Gang. Eine gute Seite, die niemand findet, ist ein schönes Geheimnis.

**Suchbegriffe**
- Im Interview fragen: Was tippen Menschen ein, die dich suchen sollten? Meist Art + Ort + Zeit („Tanzen Freiburg Sonntag“), selten Markennamen.
- Fünf bis zehn Begriffe festhalten und in `CLAUDE.md` eintragen.
- Begriffe natürlich unterbringen: Seitentitel, Hauptüberschrift, erster Absatz, FAQ. Kein Begriffe-Stapeln.

**Auf der Seite**
- Pro Seite ein eigener `<title>` und eine Beschreibung (`meta description`), mit Ort.
- Bilder mit Alt-Texten und sprechenden Dateinamen.
- Strukturierte Daten (JSON-LD), `sitemap.xml`, `robots.txt`, `llms.txt`.

**Außerhalb der Seite** (nach Wirkung sortiert)
1. Google-Unternehmensprofil, auch ohne öffentliche Adresse als Anbieter mit Einzugsgebiet.
2. Search Console und Bing Webmaster Tools (Bing speist ChatGPT und Copilot).
3. Branchenverzeichnisse, die wirklich zum Angebot passen.
4. Partner, Veranstaltungsorte, Kooperationen: um einen Link bitten.
5. Regionale Veranstaltungskalender.

**Geduld:** Indexierung dauert Tage, Rankings Wochen. Nach einigen Wochen in der Search Console unter „Leistung“ nachsehen, mit welchen Begriffen die Seite gefunden wird, und Texte behutsam nachschärfen.

---

## 18. Noch offen in der Werkstatt

- [ ] Das neutrale Gerüst aus dem Bettina-Repo in diese Vorlage übernehmen, damit jedes neue Projekt damit startet.
- [ ] Ein wiederverwendbares Prüf-Skript für Screenshots bei 390 und 1280 px.
- [ ] 404-Seite und Grundlagen der Barrierefreiheit im Gerüst (Alt-Texte, Kontraste, Tastaturbedienung).
- [ ] Material-Eingang festlegen: wohin Kundinnen Fotos und Texte schicken.
- [ ] Ablauf Collaborator + Claude-GitHub-App auf fremdem Repo beim ersten Transfer testen.
- [ ] Impeccable an Jakobs eigener Website testen, dann entscheiden, ob es in die Vorlage kommt.
- [ ] Claude Design gegen Google Stitch testen.

---

## 19. Vorlagen im Repo

- `CLAUDE.md`: Regeln und Arbeitsweise für Claude Code.
- `_projekt/STAND.md`: Projektstand und offene Punkte.
- `_projekt/GRUNDLAGE.md`: Ergebnis von Phase 3 (wer, für wen, was, warum).
- `_projekt/DESIGN.md`: das Stilbuch der Seite (Abschnitt 20).
- `.claude/skills/frontend-design/`: Design-Skill von Anthropic.
- `_werkstatt/KI-WERKZEUGKASTEN.md`: Hintergrundrecherche zu Skills und Werkzeugen.

---

## 20. Design-Werkzeuge und Referenz-System

**Ziel:** Geschmack wird zu einer Datei, nicht zu zwanzig Feedbackrunden.

**Referenzen → DESIGN.md**
1. Die Kundin bringt zwei bis drei Seiten mit, die sie berühren, und sagt je einen Satz, *was* sie berührt.
2. Claude öffnet jede Seite und hält fest: Schriften und Größenstufen, Abstände, Rhythmus der Abschnitte, Farbstimmung, Bildsprache, Bewegung.
3. Daraus entsteht **eine** `_projekt/DESIGN.md`, passend zur Kundin, keine Kopie.
4. Drei Hero-Varianten als Screenshot. Die Kundin wählt.
5. Ab dann ist `DESIGN.md` der Ausgangspunkt für jede neue Seite.
6. **Das Stilbuch lebt.** Weicht die Kundin oder Jakob bewusst ab, gilt die Abweichung und wird in `DESIGN.md` nachgetragen. Claude dreht nichts zurück und fällt nicht in einen Standard- oder Skill-Look zurück. Der Skill hilft beim Anfang, die Menschen entscheiden.

Grenze: Inspiration ja, Nachbau nein. Keine Logos, Texte, Bilder oder unverwechselbaren Layouts fremder Seiten.

Prompt:
```
Hier sind Referenzseiten, die [Name] mag:
1. [URL]: „[was sie daran berührt]“
2. [URL]: „[…]“
Öffne jede Seite und analysiere die Designsprache: Schriften und Größenstufen,
Abstände, Rhythmus, Farben, Bildsprache, Bewegung. Kopiere nichts.
Leite daraus eine eigene _projekt/DESIGN.md ab, passend zu _projekt/GRUNDLAGE.md.
Nenne am Ende drei Dinge, die du bewusst NICHT übernommen hast, und warum.
```

**Skills**
- In der Vorlage: nur `frontend-design` von Anthropic (eine Textdatei in `.claude/skills/`). Er hilft gegen den typischen KI-Look.
- Weitere Skills nur nach Prüfung und nie mehrere Design-Skills gleichzeitig, sie widersprechen sich.
- **Impeccable** (Designsystem, Kritik, Feinschliff): wird zuerst an Jakobs eigener Website getestet. Es lädt ein eigenes Programm nach und kann Hooks einrichten. Erst nach gutem Test in die Vorlage.
- Skills sind Code von Fremden. Nur bekannte Quellen, vorher lesen lassen: „Lies diesen Skill und sag mir, ob er etwas Riskantes tut.“ Projektweise im Repo installieren, nie global.
- In Cloud-Sitzungen funktionieren `/plugin` und `npx skills add` nicht zuverlässig. Skills kommen als Ordner nach `.claude/skills/` ins Repo. Danach eine neue Sitzung starten, dann sind sie aktiv.

**Augen für Claude:** In Claude Code in der Cloud sind Playwright und Chromium schon da. Ein Playwright-MCP ist nicht nötig. Einfach verlangen: „Mach Screenshots bei 390 und 1280 px und prüfe sie gegen DESIGN.md, bevor du mir berichtest.“

**Arbeitsweise**
- Größere Schritte im Plan-Modus beginnen: Claude plant, ändert nichts. Erst wenn der Plan stimmt: „Mach.“
- `CLAUDE.md` kurz halten. Ausführliches in eigene Dateien, in der `CLAUDE.md` nur darauf verweisen.
- Neue Aufgabe, neuer Chat. Lange Chats werden schlechter. Entscheidungen stehen in `STAND.md`.

**Bilder:** KI-Bilder nur für Texturen und Hintergründe, nie von Menschen oder echten Situationen. Die Kundinnen wollen echt gesehen werden.

**Hosting:** GitHub Pages bleibt Standard. GitHub schließt nur Seiten aus, die vor allem auf Verkäufe ausgerichtet sind. Eine Infoseite mit Links zu Tickets oder Buchung ist in Ordnung. Hat eine Kundin einen eigenen Shop oder Bezahlung auf der Seite, wird das Hosting vorher neu entschieden.

**Noch offen:** Impeccable testen; Claude Design gegen Google Stitch testen, um zu sehen, ob überhaupt ein weiteres Design-Werkzeug nötig ist.

---

*Die Seite ist lebendig und muss nicht perfekt sein. Sie lebt von den Angeboten.*
