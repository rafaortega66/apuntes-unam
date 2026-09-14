#!/usr/bin/env python3
"""
Genera assets/search-index.json a partir de todas las páginas HTML del sitio.

Indexa dos niveles por página:
  - "page"    -> la página completa (título, subtítulo, todo el texto visible)
  - "section" -> cada <details id="..."> dentro de la página (temario, clases,
                 secciones de apuntes), enlazando directo a esa ancla (#id)

Se debe correr cada vez que se agrega o edita contenido (clases nuevas,
correcciones, etc.) y luego commitear el JSON generado junto con los cambios.

Uso:
    python3 scripts/build_search_index.py
"""
import os
import re
import json
import html
from html.parser import HTMLParser
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(ROOT, "assets", "search-index.json")


def strip_tags(fragment):
    """Quita tags HTML de un fragmento y normaliza espacios/entidades."""
    text = re.sub(r"<[^>]+>", " ", fragment)
    text = html.unescape(text)
    return " ".join(text.split())


class DetailsExtractor(HTMLParser):
    """Extrae el texto completo de la página y, por separado, el texto de
    cada <details id="..."> (soporta anidamiento simple)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.full_text_parts = []
        self.details_stack = []
        self.sections = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.skip_depth += 1
            return
        if tag == "details":
            self.details_stack.append(
                {"id": attrs.get("id"), "buf": [], "in_summary": False, "title_buf": []}
            )
            return
        if tag == "summary" and self.details_stack:
            self.details_stack[-1]["in_summary"] = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            if self.skip_depth > 0:
                self.skip_depth -= 1
            return
        if tag == "summary" and self.details_stack:
            self.details_stack[-1]["in_summary"] = False
            return
        if tag == "details" and self.details_stack:
            d = self.details_stack.pop()
            body_text = " ".join(d["buf"]).strip()
            title_text = " ".join(d["title_buf"]).strip()
            if d["id"] and (body_text or title_text):
                self.sections.append(
                    {
                        "id": d["id"],
                        "title": " ".join(title_text.split()),
                        "text": " ".join(body_text.split()),
                    }
                )
            # propaga el contenido al details padre (si lo hay) para que
            # temas que envuelven sub-secciones también las incluyan
            if self.details_stack:
                self.details_stack[-1]["buf"].append(title_text)
                self.details_stack[-1]["buf"].append(body_text)

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        self.full_text_parts.append(data)
        for d in self.details_stack:
            if d["in_summary"]:
                d["title_buf"].append(data)
            else:
                d["buf"].append(data)

    @property
    def full_text(self):
        return " ".join(" ".join(self.full_text_parts).split())


def load_materias(root_index_path):
    """Lee index.html (raíz) y arma slug -> {name, color}."""
    with open(root_index_path, encoding="utf-8") as f:
        raw = f.read()
    materias = {}
    for m in re.finditer(
        r'<a class="card" style="--c:(#[0-9A-Fa-f]{6})" href="materias/([^/]+)/index\.html">'
        r"<h3>(.*?)</h3><p>(.*?)</p></a>",
        raw,
    ):
        color, slug, name, prof = m.groups()
        materias[slug] = {"name": strip_tags(name), "color": color, "prof": strip_tags(prof)}
    return materias


def extract_head(raw):
    """Saca <title>, y dentro de detail-head el <h2> y <p class="prof">."""
    title = ""
    m = re.search(r"<title>(.*?)</title>", raw, re.S)
    if m:
        title = strip_tags(m.group(1))

    h2 = ""
    prof = ""
    m = re.search(r'<div class="detail-head"[^>]*>(.*?)</div>', raw, re.S)
    if m:
        block = m.group(1)
        mh = re.search(r"<h2>(.*?)</h2>", block, re.S)
        if mh:
            h2 = strip_tags(mh.group(1))
        mp = re.search(r'<p class="prof">(.*?)</p>', block, re.S)
        if mp:
            prof = strip_tags(mp.group(1))
    return title, h2, prof


def classify(filename):
    if filename == "index.html":
        return "index"
    if re.match(r"clase-\d+\.html$", filename):
        return "clase"
    if filename == "evaluacion.html":
        return "evaluacion"
    if filename == "entregas.html":
        return "entregas"
    return "otro"


def main():
    root_index = os.path.join(ROOT, "index.html")
    materias = load_materias(root_index)

    items = []

    materias_dir = os.path.join(ROOT, "materias")
    for slug in sorted(os.listdir(materias_dir)):
        mdir = os.path.join(materias_dir, slug)
        if not os.path.isdir(mdir):
            continue
        info = materias.get(slug, {"name": slug, "color": "#7C9CD6", "prof": ""})
        for filename in sorted(os.listdir(mdir)):
            if not filename.endswith(".html"):
                continue
            fpath = os.path.join(mdir, filename)
            with open(fpath, encoding="utf-8") as f:
                raw = f.read()

            url = f"materias/{slug}/{filename}"
            title, h2, prof = extract_head(raw)
            kind_type = classify(filename)

            page_title = h2 or title or filename
            page_subtitle = prof or info["name"]

            parser = DetailsExtractor()
            parser.feed(raw)

            items.append(
                {
                    "url": url,
                    "materiaSlug": slug,
                    "materia": info["name"],
                    "color": info["color"],
                    "kind": "page",
                    "pageType": kind_type,
                    "title": page_title,
                    "subtitle": page_subtitle,
                    "text": parser.full_text,
                }
            )

            for sec in parser.sections:
                if not sec["title"] and not sec["text"]:
                    continue
                items.append(
                    {
                        "url": f"{url}#{sec['id']}",
                        "materiaSlug": slug,
                        "materia": info["name"],
                        "color": info["color"],
                        "kind": "section",
                        "pageType": kind_type,
                        "title": sec["title"] or page_title,
                        "subtitle": f"{page_title} · {info['name']}",
                        "text": sec["text"],
                    }
                )

    out = {
        "generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "items": items,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

    print(f"OK: {len(items)} entradas indexadas -> {OUT_PATH}")


if __name__ == "__main__":
    main()
