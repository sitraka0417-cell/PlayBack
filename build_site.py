#!/usr/bin/env python3
"""Mandefa ny dossier rehetra ao amin'ny repo ary mamorona songs.json (artiste -> chants)."""
import json, os, re, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
EXCLUDE = {"_site", "assets", "node_modules"}
BASE_URL = "https://sitraka0417-cell.github.io/PlayBack/"

def natural(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]

def mp3s_in(folder):
    out = []
    for dp, dn, fn in os.walk(folder):
        dn[:] = [d for d in dn if not d.startswith(".")]
        for f in fn:
            if f.lower().endswith(".mp3"):
                full = os.path.join(dp, f)
                rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
                out.append({"title": os.path.splitext(f)[0].strip(), "file": rel})
    out.sort(key=lambda s: natural(s["file"]))
    return out

artists = []
for name in sorted(os.listdir(ROOT), key=natural):
    p = os.path.join(ROOT, name)
    if os.path.isdir(p) and not name.startswith(".") and name not in EXCLUDE:
        songs = mp3s_in(p)
        if songs:
            artists.append({"name": name, "songs": songs})

loose = [f for f in os.listdir(ROOT) if f.lower().endswith(".mp3")]
if loose:
    artists.append({"name": "Autres", "songs": [
        {"title": os.path.splitext(f)[0], "file": f} for f in sorted(loose, key=natural)]})

data = {
    "updated": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
    "artists": artists,
}
with open(os.path.join(ROOT, "songs.json"), "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
             f'  <url><loc>{BASE_URL}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>\n</urlset>\n')

print(f"{len(artists)} artiste(s), {sum(len(a['songs']) for a in artists)} chant(s)")
