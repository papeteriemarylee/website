#!/usr/bin/env python3
"""
Télécharge toutes les images hébergées chez Squarespace dans le dossier
images/ et remplace les liens dans les fichiers HTML.

À lancer UNE fois, avant de fermer votre compte Squarespace :
    python3 tools/download_images.py
"""
import os, re, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "images")
PATTERN = re.compile(r'https://images\.squarespace-cdn\.com/[^"\'\s)]+')
os.makedirs(IMG_DIR, exist_ok=True)

html_files = []
for folder, _, files in os.walk(ROOT):
    if "/.git" in folder or folder.startswith(os.path.join(ROOT, "tools")):
        continue
    html_files += [os.path.join(folder, f) for f in files if f.endswith(".html")]

downloaded = {}

def local_name(url):
    path = urllib.parse.urlparse(url).path
    name = urllib.parse.unquote(path.rsplit("/", 1)[-1]).replace("+", "-").replace(" ", "-")
    return re.sub(r"[^A-Za-z0-9._-]", "", name.encode("ascii", "ignore").decode()) or "image"

def fetch(url):
    base = url.split("?")[0]
    if base in downloaded:
        return downloaded[base]
    name = local_name(base)
    dest = os.path.join(IMG_DIR, name)
    if not os.path.exists(dest):
        src = base if base.endswith(".ico") else base + "?format=2500w"
        req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as r, open(dest, "wb") as out:
            out.write(r.read())
        print("  ✓", name)
    downloaded[base] = name
    return name

for path in html_files:
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(IMG_DIR, os.path.dirname(path)).replace(os.sep, "/")
    new = PATTERN.sub(lambda m: f"{rel}/{fetch(m.group(0))}", text)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
        print("Mis à jour :", os.path.relpath(path, ROOT))

print(f"\nTerminé : {len(downloaded)} images dans images/")
