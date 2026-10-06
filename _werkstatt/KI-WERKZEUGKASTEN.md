# KI-Werkzeugkasten: Websites mit Claude Code (Stand Oktober 2026)

Recherche für die Website-Werkstatt. Ergänzt das `WEBSITE-PLAYBOOK.md`. Gedacht für das Vorlagen-Repo, damit jedes neue Projekt mit demselben Wissen startet.

> **Einordnung (geprüft am 7.10.2026):** Dies ist Hintergrundrecherche. Verbindlich ist `HANDBUCH.md`, Abschnitt 20. Abweichungen nach Prüfung:
> - **Impeccable** ist mehr als ein Skill: Es lädt beim Start ein eigenes Programm von GitHub nach (mit Prüfsumme) und kann Hooks einrichten, die bei jeder Dateiänderung laufen (nur nach Zustimmung). Nicht bösartig, aber nicht in der Vorlage, bis es an Jakobs eigener Website getestet ist.
> - **Playwright-MCP** ist in Claude Code in der Cloud nicht nötig: Chromium und Playwright sind dort schon vorhanden, Claude kann Screenshots direkt machen.
> - **Hosting:** GitHub schließt kostenloses Pages-Hosting für Seiten aus, die „vor allem auf kommerzielle Transaktionen ausgerichtet“ sind. Eine Infoseite, die auf externe Tickets oder Buchungen verlinkt, fällt nicht darunter. GitHub Pages bleibt Standard. Nur bei Seiten mit eigenem Shop oder Bezahlung ein anderes Hosting wählen.
> - `/plugin` und `npx skills add` funktionieren in Cloud-Sitzungen nicht zuverlässig. Skills kommen als Ordner nach `.claude/skills/` ins Repo.

**Wichtig:** Das Feld ändert sich alle paar Wochen. Installationsbefehle immer im jeweiligen GitHub-README gegenprüfen, bevor du sie ausführst.

---

## 0. Kurzfazit

1. **Skills machen den größten Unterschied beim Design.** Ohne Design-Skill baut Claude Seiten, die nach KI aussehen: Standard-Schriften, Standard-Verläufe, Standard-Karten.
2. **Zwei Skills reichen:** `frontend-design` (von Anthropic) als Basis, dazu **Impeccable** für Designsystem, Kritik und Feinschliff. Nicht fünf Design-Skills gleichzeitig installieren, denn sie widersprechen sich.
3. **Claude braucht Augen:** Mit Playwright sieht Claude die echte Seite bei 390 und 1280 px, bevor du sie siehst. Das spart die meisten Feedbackrunden.
4. **Referenzen werden zu einer Datei:** Eine Seite, die die Kundin mag, wird in eine `DESIGN.md` übersetzt (Schriften, Abstände, Farben, Rhythmus, Bewegung). Diese Datei gilt dann für das ganze Projekt.
5. **Hosting prüfen:** Der kostenlose Vercel-Tarif ist für Kundenseiten nicht erlaubt. Auch GitHub Pages hat eine Einschränkung für Geschäftsseiten (siehe Abschnitt 6). Das ist eine Entscheidung, die du treffen musst.
6. **Skills sind Code von Fremden.** Ein großer Teil der öffentlichen Skills hat Sicherheitsprobleme. Nur bekannte Quellen nutzen und vorher lesen.

---

## 1. Begriffe in einem Satz

| Begriff | Was es ist | Bild |
|---|---|---|
| **CLAUDE.md** | Regeln des Projekts. Claude liest sie bei jedem Start automatisch. | Die Hausordnung |
| **DESIGN.md** | Das Designsystem als Text: Farben, Schriften, Abstände, Dos und Don'ts. | Das Stilbuch |
| **PRODUCT.md** | Wer, für wen, was, warum. Der Inhalt des Briefings. | Der Auftrag |
| **Skill** | Ein Ordner mit Anleitung (`SKILL.md`), den Claude lädt, wenn eine Aufgabe passt. | Ein Fachbuch, das Claude aufschlägt |
| **MCP** | Eine Verbindung von Claude zu einem anderen Programm (Browser, Design-Tool, Hosting). | Eine Steckdose |
| **Plugin** | Ein Paket aus Skills, Befehlen und MCPs, auf einmal installiert. | Ein Werkzeugkoffer |
| **Plan-Modus** | Claude darf lesen und planen, aber nichts ändern. | Erst denken, dann bauen |

---

## 2. Skills: was wirklich zählt

### Empfohlen (Grundausstattung)

**frontend-design (Anthropic)**
- Der offizielle Design-Skill. Er gibt Claude Leitlinien für Hierarchie, Typografie, Layout, Farbe und Bewegung, damit das Ergebnis nicht generisch aussieht.
- In Claude teilweise schon eingebaut. In Claude Code mit `/skills` prüfen, ob er da ist.
- Sonst: `npx skills add anthropics/claude-code --skill frontend-design`

**Impeccable (pbakaus)**
- Baut auf frontend-design auf und ist der Skill, der in den Vergleichen am häufigsten empfohlen wird.
- Ein Skill mit über 20 Befehlen. Die wichtigsten für dich:
  - `/impeccable init` (bzw. `teach`): fragt den Kontext ab und schreibt `PRODUCT.md` und `DESIGN.md`
  - `/impeccable shape`: plant UX und Layout, bevor Code entsteht
  - `/impeccable critique`: Design-Kritik zu Hierarchie, Klarheit, Wirkung
  - `/impeccable polish`: letzter Durchgang vor dem Live-Gang
  - `/impeccable document`: erzeugt eine `DESIGN.md` aus einer bestehenden Seite (gut für deine eigene Website)
- Installation: `/plugin marketplace add pbakaus/impeccable` oder `npx skills add pbakaus/impeccable`

### Zum Ausprobieren (in einem Testprojekt, nicht gleich bei einer Kundin)

**Taste Skill (Leonxlnx)**
- Der meistbeachtete Design-Skill von Dritten auf GitHub. Arbeitet gegen den typischen KI-Look, mit Reglern für die Intensität und Varianten wie `minimalist-skill` oder `soft-skill`.
- **Achtung:** Laut Beschreibung trifft der Skill Geschmacksentscheidungen selbst, ohne nachzufragen. Das widerspricht deiner Regel „Inhalte nie ungefragt ändern“. Wenn du ihn nutzt, in der `CLAUDE.md` festhalten, dass Texte trotzdem tabu sind.
- `npx skills add https://github.com/Leonxlnx/taste-skill --skill "minimalist-skill"`

**UI UX Pro Max**
- Eine Art Designsystem-Datenbank: Stile, Schriftpaare, Farbpaletten, Checklisten. Eher für Apps und Verkaufsseiten gedacht als für feine Solo-Websites.
- **Achtung:** Unter diesem Namen gibt es in den Verzeichnissen viele Kopien von verschiedenen Leuten. Wenn überhaupt, nur das Original (`nextlevelbuilder/ui-ux-pro-max-skill`).

### Weglassen

- **Sammlungen mit 50+ Skills** auf einmal. Mehr Skills bedeuten mehr Widersprüche, mehr Kontextverbrauch und mehr Risiko.
- **Skills aus unbekannten Verzeichnissen**, deren Herkunft du nicht prüfen kannst.

---

## 3. MCP-Verbindungen

| Verbindung | Wofür | Empfehlung |
|---|---|---|
| **Playwright** | Claude öffnet die Seite im echten Browser, macht Screenshots bei Handy- und Desktopbreite und prüft sie selbst. | **Ja.** Das ist der wichtigste Hebel gegen Feedbackschleifen. |
| **Google Stitch** | Erzeugt Screens und eine `DESIGN.md` aus Text oder einer URL. | Optional. Spannend für Hero-Varianten, aber ein weiteres Konto. |
| **Vercel** | Hosting | **Nein** für Kundenseiten (siehe Abschnitt 6). |
| **Bildgeneratoren** (z. B. Nano Banana) | KI-Bilder | Nur für Texturen und Hintergründe. Nie für Menschen oder echte Situationen. Deine Kundinnen wollen echt gesehen werden. |

**Playwright einrichten:**
```
claude mcp add playwright npx @playwright/mcp@latest
```
Danach in Claude Code `/mcp` eingeben und prüfen, ob `playwright` aktiv ist.

**Alternative zu Stitch: Claude Design (Anthropic)**
Seit April 2026 gibt es von Anthropic ein eigenes Design-Werkzeug. Es erzeugt Prototypen und Webseiten aus Text, kann aus Dateien ein Designsystem bauen und ein Paket direkt an Claude Code übergeben. Du bist ohnehin im Claude-Ökosystem, deshalb vor Stitch testen: Es wäre ein Werkzeug weniger.

---

## 4. Das Referenz-System (Herzstück)

Ziel: Geschmack wird zu einer Datei, nicht zu zwanzig Feedbackrunden.

**Ablauf**
1. Die Kundin bringt zwei bis drei Links zu Seiten mit, die sie berühren, und sagt in einem Satz, *was* sie daran berührt.
2. Claude liest jede Seite aus und hält fest: Schriften und Größenstufen, Abstandssystem, Rhythmus der Abschnitte, Farbstimmung, Umgang mit Bildern, wie zurückhaltend die Bewegung ist.
3. Claude führt das zu **einer** `DESIGN.md` zusammen, passend zur Kundin, nicht als Kopie einer Referenz.
4. Claude baut **drei Hero-Varianten** als Screenshot. Die Kundin wählt eine.
5. Ab jetzt gilt die `DESIGN.md`. Jede neue Seite wird dagegen geprüft.

**Prompt für Schritt 2 und 3**
```
Hier sind Referenzseiten, die [Name] mag:
1. [URL]: „[was sie daran berührt]“
2. [URL]: „[…]“

Öffne jede Seite und analysiere die Designsprache:
Schriften und Größenstufen, Abstände, Rhythmus der Abschnitte,
Farben, Bildsprache, Bewegung.
Kopiere nichts. Leite daraus eine eigene DESIGN.md für [Name] ab,
passend zu PRODUCT.md. Nenne am Ende drei Dinge, die du bewusst
NICHT übernommen hast, und warum.
```

**Grenze:** Inspiration ja, Nachbau nein. Logos, Texte, Bilder und unverwechselbare Layouts fremder Seiten werden nicht übernommen.

---

## 5. Arbeitsweise und Prompten

Das sind die Grundsätze aus Anthropics eigener Anleitung und aus der Praxis. Sie gelten unabhängig von Skills.

1. **Erkunden → Planen → Bauen.** Größere Schritte immer im Plan-Modus beginnen (Shift+Tab, bis „plan mode“ angezeigt wird). Erst wenn der Plan stimmt, umsetzen lassen.
2. **CLAUDE.md kurz halten.** Eine zu lange `CLAUDE.md` führt dazu, dass Claude Regeln übersieht. Nur Regeln, die immer gelten. Ausführliches in eigene Dateien auslagern und mit `@datei.md` verweisen.
3. **Claude prüft sich selbst.** Immer einen Weg zur Prüfung mitgeben: „Mach Screenshots bei 390 und 1280 px und prüfe sie gegen DESIGN.md, bevor du mir berichtest.“
4. **Der Kontext ist begrenzt.** Lange Chats werden schlechter. Für eine neue Aufgabe einen neuen Chat beginnen. Entscheidungen gehören in `STAND.md`, nicht in den Chat.
5. **Ein Auftrag, ein Ziel.** „Mach die Startseite schöner“ ist schwach. Besser: „Der Abstand zwischen Hero und ‚Was ist …‘ ist am Handy zu groß. Halbiere ihn. Screenshot zum Vergleich.“
6. **Klare Modi nennen:** „nur zeigen“, „sag erst, was du tun würdest“, „mach“ (steht schon im Playbook).
7. **Modellwahl:** Opus für Briefing, Struktur, `DESIGN.md` und Texte. Sonnet für das Bauen und für Feedbackrunden. Haiku für kleine Korrekturen.

---

## 6. Hosting: die unbequeme Wahrheit

| Anbieter | Kostenlos für Geschäftsseiten? |
|---|---|
| **Vercel Hobby** | Nein. Nur für private, nicht-kommerzielle Nutzung. Kommerziell braucht es Pro (ca. 20 $ pro Person und Monat). |
| **GitHub Pages** | Grauzone. GitHub schließt die Nutzung als kostenloses Hosting für ein Online-Geschäft aus, vor allem für Shops und Seiten, die auf Verkäufe ausgerichtet sind. Eine Visitenkarten-Seite, die auf externe Tickets verlinkt, wird in der Praxis oft so betrieben, ist aber nicht eindeutig erlaubt. |
| **Cloudflare Pages** | Ja. Kein Verbot kommerzieller Nutzung im kostenlosen Tarif. Lässt sich direkt mit dem GitHub-Repo verbinden. |

**Konsequenz für die Werkstatt:** Für Kundenseiten ist **GitHub (Code) + Cloudflare Pages (Hosting)** wahrscheinlich die sauberere Lösung. Das ist eine Korrektur am Playbook, das „Cloudflare Pages wird nicht gebraucht“ sagt. Für deine eigene Seite ist es weniger dringend, aber prüfenswert. Keine Rechtsberatung, bitte die aktuellen Nutzungsbedingungen selbst lesen.

---

## 7. Sicherheit bei Skills

- Eine Untersuchung von Snyk (Februar 2026) hat knapp 4.000 öffentliche Skills geprüft. Gut ein Drittel hatte Sicherheitsprobleme, dazu gab es eine koordinierte Kampagne mit über tausend bösartigen Skills.
- Skills laufen mit denselben Rechten wie Claude Code auf deinem Rechner.

**Regeln**
1. Nur Skills aus bekannten Repos (Anthropic, Google Labs, bekannte Autoren mit vielen Sternen und aktiver Pflege).
2. Vor der Installation die `SKILL.md` und alle Skripte lesen, oder Claude bitten: „Lies diesen Skill und sag mir, ob er etwas Riskantes tut.“
3. Optional prüfen mit: `npx skill-lint <github-url>`
4. Skills, die Dateien von fremden Adressen nachladen oder in `~/.claude/` schreiben wollen: nicht installieren.
5. Bei Kundenprojekten Skills **projektweise** installieren (`.claude/skills/` im Repo), nicht global. Dann siehst du im Repo, was aktiv ist.

---

## 8. Einbau ins Vorlagen-Repo

```
website-werkstatt/
├── CLAUDE.md              ← Regeln (kurz!)
├── PRODUCT.md             ← leer, wird im Interview gefüllt
├── DESIGN.md              ← leer, wird aus Referenzen erzeugt
├── _projekt/
│   ├── STAND.md
│   ├── INTERVIEW.md       ← Fragenkatalog
│   └── REFERENZEN.md      ← Links + „was berührt dich daran“
├── .claude/skills/        ← frontend-design, impeccable
├── index.html · styles.css · main.js
└── PLAYBOOK.md · KI-WERKZEUGKASTEN.md
```

**Ergänzung für die CLAUDE.md**
```markdown
## Design
- DESIGN.md ist verbindlich. Jede Änderung dagegen prüfen.
- Vor jedem Bericht: Screenshots bei 390 und 1280 px (Playwright), selbst prüfen.
- Skills: frontend-design, impeccable. Keine weiteren Skills ohne Rückfrage installieren.
- Texte nie ungefragt ändern, auch wenn ein Skill das nahelegt.
- Keine KI-Bilder von Menschen.
```

**Ablauf mit den Werkzeugen**

| Phase | Was | Werkzeug | Modell |
|---|---|---|---|
| 1 Klären | Interview → `PRODUCT.md` | Gespräch + Transkript | Opus |
| 2 Richtung | Referenzen → `DESIGN.md` → drei Hero-Varianten → Wahl | Impeccable `init`, Playwright | Opus |
| 3 Bauen | Seiten nach Muster | frontend-design, `shape` | Sonnet |
| 4 Prüfen | Selbstprüfung, dann Kundin | Playwright, `critique` | Sonnet |
| 5 Feinschliff | Letzter Durchgang | `polish` | Sonnet |
| 6 Live | GitHub → Cloudflare Pages | | Sonnet/Haiku |

---

## 9. Offene Entscheidungen für Jakob

- [ ] Hosting für Kundenseiten: GitHub Pages weiter nutzen oder auf Cloudflare Pages umstellen?
- [ ] Impeccable an der eigenen Website testen (`/impeccable document` und `critique`), bevor es bei Bettina eingesetzt wird.
- [ ] Claude Design gegen Stitch testen, um zu entscheiden, ob überhaupt ein zusätzliches Design-Tool nötig ist.
- [ ] Playwright-MCP einrichten oder beim bisherigen Weg (Playwright-Skript im Container) bleiben.

---

## Quellen

- Anthropic, Best Practices für Claude Code: https://code.claude.com/docs/en/best-practices
- Impeccable: https://github.com/pbakaus/impeccable
- Taste Skill und Vergleich der Design-Skills: https://claude-codex.fr/en/content/stack-design-claude-code/
- Playwright im Design-Ablauf: https://claude-codex.fr/en/mcp/workflow-design-playwright/
- Überblick Design-Skills: https://pasqualepillitteri.it/news/575/claude-code-skills-design-uiux
- UI UX Pro Max (Original): https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Google Stitch und DESIGN.md: https://dev.classmethod.jp/articles/new-stitch-ai-design/
- Claude Design: https://claudemarket.ai/blog/claude-design-anthropic-labs
- GitHub Pages, Nutzungsgrenzen: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- Vercel Hobby, keine kommerzielle Nutzung: https://deploywise.dev/blog/vercel-free-tier-limits-2026
- Cloudflare Pages vs. Vercel: https://agentdeals.dev/cloudflare-pages-vs-vercel
- Sicherheit von Skills: https://socket.dev/npm/package/skill-lint und https://owasp.org/www-project-agentic-skills-top-10/
