#!/usr/bin/env python3
"""Baut die Galerie und alle Werkseiten aus tools/werke.json.

Aufruf im Repo-Hauptordner:  python3 tools/make-werke.py

Was das Skript tut:
- kunst.html: ersetzt alles zwischen <!-- werke:start --> und <!-- werke:end --> durch die Galerie.
- index.html: ersetzt alles zwischen <!-- empfohlen:start --> und <!-- empfohlen:end --> durch die empfohlenen Werke.
- werk-<slug>.html: eine Seite pro Werk (Kopf, Menü und Fuß kommen aus kunst.html).
- sitemap.xml: wird neu geschrieben.

Werke nie direkt im HTML ändern, nur in tools/werke.json.
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://koojaa92.github.io/Charlotte-Website/"
MAIL = "mailto:hallo@example.org"
SEITEN = ["index.html", "generative-painting.html", "coaching.html", "teams.html", "kunst.html", "ueber-mich.html"]


def lies(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return f.read()


def schreibe(name, inhalt):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(inhalt)


def e(s):
    return html.escape(s, quote=True)


def bild_groesse(datei):
    try:
        from PIL import Image
        with Image.open(os.path.join(ROOT, "images", datei)) as im:
            return im.size
    except Exception:
        return (900, 900)


def zeile(w):
    teile = []
    if w.get("masse"):
        teile.append(w["masse"])
    if w.get("technik"):
        teile.append(w["technik"])
    return ", ".join(teile)


def karte(w):
    b = w["bilder"][0]
    iw, ih = bild_groesse(b["datei"])
    status = f' <span class="status">{e(w["status"])}</span>' if w.get("status") else ""
    return (
        f'<figure class="werk">'
        f'<a href="werk-{w["slug"]}.html"><span class="rahmen"><img src="images/{b["datei"]}" alt="{e(b.get("alt") or w["titel"])}" '
        f'width="{iw}" height="{ih}" loading="lazy"></span>'
        f'<figcaption><strong>{e(w["titel"])}</strong><span>{e(zeile(w))}{status}</span></figcaption></a>'
        f'</figure>'
    )


def ersetze(text, marke, neu):
    muster = re.compile(r"(<!-- %s:start -->).*?(<!-- %s:end -->)" % (marke, marke), re.S)
    if not muster.search(text):
        raise SystemExit(f"Marke {marke} fehlt")
    return muster.sub(lambda m: m.group(1) + "\n" + neu + "\n" + m.group(2), text)


def detail(w, werke, i, rahmen_vor, rahmen_nach):
    bilder = "".join(
        f'<figure><img src="images/{b["datei"]}" alt="{e(b.get("alt") or w["titel"])}" '
        f'width="{bild_groesse(b["datei"])[0]}" height="{bild_groesse(b["datei"])[1]}"></figure>'
        for b in w["bilder"]
    )
    daten = []
    for k, v in (("Maße", w.get("masse")), ("Technik", w.get("technik")), ("Jahr", w.get("jahr")),
                 ("Hinweis", w.get("hinweis")), ("Status", w.get("status"))):
        if v:
            daten.append(f"<div><dt>{k}</dt><dd>{e(v)}</dd></div>")
    schlag = ""
    if w.get("schlagworte"):
        schlag = '<ul class="schlagworte">' + "".join(f"<li>{e(s)}</li>" for s in w["schlagworte"]) + "</ul>"
    text = f'<p class="werk-text">{e(w["text"])}</p>' if w.get("text") else ""
    vorher = werke[i - 1]
    nachher = werke[(i + 1) % len(werke)]
    anfrage = f'{MAIL}?subject={e("Preisanfrage: " + w["titel"]).replace(" ", "%20")}'
    knopf = "" if w.get("status") == "verkauft" else f'<div class="knoepfe"><a class="knopf" href="{anfrage}">Preis anfragen</a></div>'
    main = f'''<main>
<section class="abschnitt werk-seite">
<div class="wrap">
<p class="zurueck"><a href="kunst.html">Zur Galerie</a></p>
<div class="werk-raster">
<div class="werk-bilder">{bilder}</div>
<div class="werk-info">
<h1>{e(w["titel"])}</h1>
<dl class="info">{"".join(daten)}</dl>
{text}{schlag}
{knopf}
<p class="blaettern"><a href="werk-{vorher["slug"]}.html">Vorheriges Werk</a><a href="werk-{nachher["slug"]}.html">Nächstes Werk</a></p>
</div>
</div>
</div>
</section>
</main>'''
    kopf = rahmen_vor
    kopf = re.sub(r"<title>.*?</title>", f"<title>{e(w['titel'])} – Charlotte (Entwurf)</title>", kopf, flags=re.S)
    kopf = re.sub(r'<meta name="description" content="[^"]*">',
                  f'<meta name="description" content="Gemälde {e(w["titel"])} von Charlotte, {e(zeile(w))}.">', kopf)
    return kopf + main + rahmen_nach


def main():
    werke = json.load(open(os.path.join(ROOT, "tools", "werke.json"), encoding="utf-8"))
    slugs = [w["slug"] for w in werke]
    assert len(slugs) == len(set(slugs)), "Doppelte Slugs in werke.json"

    kunst = lies("kunst.html")
    galerie = '<div class="galerie-raster">' + "".join(karte(w) for w in werke) + "</div>"
    kunst = ersetze(kunst, "werke", galerie)
    schreibe("kunst.html", kunst)

    index = lies("index.html")
    emp = [w for w in werke if w.get("empfohlen")]
    schreibe("index.html", ersetze(index, "empfohlen", '<div class="galerie-raster drei">' + "".join(karte(w) for w in emp) + "</div>"))

    # Rahmen aus kunst.html: alles vor <main> und alles nach </main>
    vor = kunst[: kunst.index("<main>")]
    nach = kunst[kunst.index("</main>") + len("</main>"):]
    for name in os.listdir(ROOT):
        if name.startswith("werk-") and name.endswith(".html") and name[5:-5] not in slugs:
            os.remove(os.path.join(ROOT, name))
    for i, w in enumerate(werke):
        schreibe(f"werk-{w['slug']}.html", detail(w, werke, i, vor, nach))

    urls = SEITEN + [f"werk-{s}.html" for s in slugs]
    schreibe("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
             + "".join(f"<url><loc>{BASE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    print(f"{len(werke)} Werke, {len(emp)} empfohlen")


if __name__ == "__main__":
    main()
