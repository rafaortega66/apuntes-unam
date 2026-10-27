#!/usr/bin/env python3
"""Genera los PDFs de resumen por clase (estilo del resumen de FSE U1–U2).

Fuente:  decimo/<SIGLA>/<SIGLA>-Resumenes/fuente/<SIGLA>-ClaseNN.md
Salida:  decimo/<SIGLA>/<SIGLA>-Resumenes/<SIGLA>-ClaseNN-resumen.pdf

Uso:
    python3 scripts/build_resumenes.py            # solo los .md más nuevos que su PDF
    python3 scripts/build_resumenes.py --todos    # regenera todo
    python3 scripts/build_resumenes.py RP-Clase18 # uno (o varios) por nombre

Formato del .md (mini-markdown propio, sin dependencias):
    % materia: Reconocimiento de Patrones
    % titulo: Clase 18 · Redes neuronales
    % subtitulo: Ing. … · 26 oct 2026 · Apuntes y resumen de estudio
    # PARTE 1 · Apuntes completos     → título de parte
    ## 1. Tema                         → sección
    ### Subtema                        → subsección
    - viñeta   /   - - sub-viñeta      → listas (1. 2. … numeradas)
    | a | b |                          → tabla (la primera fila es encabezado)
    !!! Título del recuadro            → recuadro; sus líneas siguen hasta una línea vacía
    ```                                → bloque de código
    **negrita**, *cursiva*, `código`
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECIMO = ROOT / "decimo"
CHROME = "google-chrome"
for c in ("google-chrome", "chromium", "chromium-browser",
          "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
    if subprocess.run(["which", c], capture_output=True).returncode == 0 or Path(c).exists():
        CHROME = c
        break

CSS = """
@page { size: A4; margin: 22mm 20mm 20mm 20mm;
  @top-right { content: var(--materia); font: 8.5pt Arial, sans-serif; color: #666; }
  @bottom-center { content: "Página " counter(page); font: 8.5pt Arial, sans-serif; color: #666; } }
body { font: 10.5pt/1.42 Arial, "Liberation Sans", sans-serif; color: #111; }
.portada { text-align: center; margin: 2mm 0 9mm; }
.portada h1 { font-size: 21pt; margin: 0 0 2mm; font-weight: 700; }
.portada .sub { font-size: 11pt; color: #444; }
h1.parte { font-size: 14pt; color: #1a3d7c; border-bottom: 1.5px solid #1a3d7c;
  padding-bottom: 1mm; margin: 6mm 0 3mm; break-after: avoid; }
h1.parte.nueva { break-before: page; }
h2 { font-size: 12.5pt; margin: 5mm 0 1.5mm; break-after: avoid; }
h3 { font-size: 11pt; margin: 3.5mm 0 1mm; break-after: avoid; }
p { margin: 0 0 2mm; text-align: left; }
ul, ol { margin: 0 0 2mm; padding-left: 7mm; }
li { margin: 0 0 .8mm; }
li > ul { margin-top: .8mm; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 3mm; font-size: 9.6pt; }
tr { break-inside: avoid; }
th { text-align: left; background: #f1f3f6; font-weight: 700; }
th, td { border-bottom: 1px solid #ccc; padding: 1.6mm 2mm; vertical-align: top; }
.caja { border: 1px solid #1a3d7c; background: #f3f6fb; padding: 2.5mm 3.5mm; margin: 2.5mm 0 3.5mm;
  break-inside: avoid; }
.caja .t { font-weight: 700; color: #1a3d7c; margin-bottom: 1mm; }
.caja p:last-child, .caja ul:last-child { margin-bottom: 0; }
code { font-family: "DejaVu Sans Mono", Menlo, monospace; font-size: 9pt; background: #f2f2f2; padding: 0 .6mm; }
pre { font-family: "DejaVu Sans Mono", Menlo, monospace; font-size: 8.6pt; line-height: 1.35;
  background: #f6f6f6; border-left: 3px solid #bbb; padding: 2mm 3mm; white-space: pre-wrap;
  break-inside: avoid; margin: 1.5mm 0 3mm; }
.intro { color: #333; font-style: italic; }
"""


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    return s


def render_lines(lines):
    out, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        st = ln.strip()
        if not st:
            i += 1
            continue
        if st.startswith("```"):
            j = i + 1
            buf = []
            while j < n and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            out.append("<pre>" + html.escape("\n".join(buf)) + "</pre>")
            i = j + 1
            continue
        if st.startswith("!!! "):
            j = i + 1
            buf = []
            while j < n and lines[j].strip():
                buf.append(lines[j])
                j += 1
            out.append(f'<div class="caja"><div class="t">{inline(st[4:])}</div>'
                       + render_lines(buf) + "</div>")
            i = j
            continue
        if st.startswith("|"):
            # \| dentro de una celda es una barra literal; una fila |---| después de
            # la segunda fila empieza otra tabla (dos tablas pegadas sin línea vacía)
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                raw = lines[i].strip().strip("|")
                cells = [c.strip().replace("\x00", "|")
                         for c in raw.replace("\\|", "\x00").split("|")]
                if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    if len(rows) > 1:
                        i -= 1
                        rows.pop()
                        break
                else:
                    rows.append(cells)
                i += 1
            t = "<table><tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr>"
            for r in rows[1:]:
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</table>")
            continue
        m = re.match(r"(#{1,3}) (.*)", st)
        if m:
            lvl, txt = len(m.group(1)), m.group(2)
            if lvl == 1:
                cls = "parte nueva" if "PARTE 2" in txt else "parte"
                out.append(f'<h1 class="{cls}">{inline(txt)}</h1>')
            else:
                out.append(f"<h{lvl}>{inline(txt)}</h{lvl}>")
            i += 1
            continue
        if re.match(r"(- |\d+\. )", st):
            ordered = bool(re.match(r"\d+\. ", st))
            tag = "ol" if ordered else "ul"
            items = []
            while i < n:
                s2 = lines[i].strip()
                if re.match(r"- - ", s2) and items:
                    items[-1][1].append(s2[4:])
                elif re.match(r"(- |\d+\. )", s2) and bool(re.match(r"\d+\. ", s2)) == ordered:
                    items.append([re.sub(r"^(- |\d+\. )", "", s2), []])
                else:
                    break
                i += 1
            h = f"<{tag}>"
            for txt, subs in items:
                h += "<li>" + inline(txt)
                if subs:
                    h += "<ul>" + "".join(f"<li>{inline(x)}</li>" for x in subs) + "</ul>"
                h += "</li>"
            out.append(h + f"</{tag}>")
            continue
        cls = ""
        if st.startswith("~ "):
            st, cls = st[2:], ' class="intro"'
        out.append(f"<p{cls}>{inline(st)}</p>")
        i += 1
    return "\n".join(out)


def build(md: Path):
    meta, body = {}, []
    for ln in md.read_text(encoding="utf-8").splitlines():
        m = re.match(r"% (\w+): (.*)", ln)
        if m and not body:
            meta[m.group(1)] = m.group(2).strip()
        else:
            body.append(ln)
    materia = meta.get("materia", "")
    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>{html.escape(meta.get('titulo', md.stem))}</title>
<style>:root {{ --materia: "{materia}"; }} {CSS}</style></head><body>
<div class="portada"><h1>{inline(meta.get('titulo', ''))}</h1>
<div class="sub">{inline(meta.get('subtitulo', ''))}</div></div>
{render_lines(body)}
</body></html>"""
    pdf = md.parent.parent / f"{md.stem}-resumen.pdf"
    with tempfile.TemporaryDirectory() as td:
        h = Path(td) / "r.html"
        h.write_text(doc, encoding="utf-8")
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", h.as_uri()],
                       check=True, capture_output=True)
    return pdf


# ---------------------------------------------------------------- páginas índice
MATERIAS = {  # sigla: (slug, nombre, color)
    "ACS": ("arquitectura-cliente-servidor", "Arquitectura Cliente-Servidor", "#E8735C"),
    "ASI": ("administracion-de-servicios-de-internet", "Administración de Servicios de Internet", "#7C9CD6"),
    "FSE": ("fundamentos-de-sistemas-embebidos", "Fundamentos de Sistemas Embebidos", "#A98BD1"),
    "MD": ("mineria-de-datos", "Minería de Datos", "#A98BD1"),
    "OAC": ("organizacion-y-arquitectura-de-computadoras", "Organización y Arquitectura de Computadoras", "#45B8A8"),
    "RP": ("reconocimiento-de-patrones", "Reconocimiento de Patrones", "#45B8A8"),
    "SIB": ("seguridad-informatica-basica", "Seguridad Informática Básica", "#E8735C"),
}
# Exámenes: stem de la clase donde ocurrió -> (descripción, desde qué clase se estudia el siguiente)
EXAMENES = {
    "MD": {"MD-Clase05": ("1.er parcial · 17 sep · Temas 1 y 2", "MD-Clase06")},
    "RP": {"RP-Clase10": ("1.er parcial · 28 sep · calificación 20.5 · la Clase 11 es la revisión del examen", "RP-Clase11")},
    "SIB": {"SIB-Clase11": ("1.er parcial · 6 oct · Temas 1 a 3 hasta CVSS", "SIB-Clase12")},
    "ASI": {"ASI-Clase12": ("1.er parcial · 7 oct · reposición el 12 oct (Clase 13)", "ASI-Clase14")},
    "FSE": {"FSE-Clase14": ("1.er parcial · 14 oct · Unidades 1 y 2 · calificación 101", "FSE-Clase15")},
    "ACS": {"ACS-Clase15": ("1.er parcial de casa · asignado el 15 oct, entregado el 18 oct", "ACS-Clase16")},
    "OAC": {},
}
MESES = {"ago": 8, "sep": 9, "oct": 10, "nov": 11}


def _label(stem):
    n = stem.split("Clase")[1]
    return f"Clase −{int(n[1:])}" if n.startswith("m") else f"Clase {int(n)}"


def _meta(md):
    meta = {}
    for ln in md.read_text(encoding="utf-8").splitlines():
        m = re.match(r"% (\w+): (.*)", ln)
        if not m:
            break
        meta[m.group(1)] = m.group(2).strip()
    d = re.search(r"(\d{1,2}) (ago|sep|oct|nov) 2026", meta.get("subtitulo", ""))
    meta["fecha"] = (MESES[d.group(2)], int(d.group(1)))
    meta["fecha_txt"] = f"{d.group(1)} {d.group(2)}" if d else ""
    meta["tit"] = re.sub(r"^Clase [−\d]+ · ", "", meta.get("titulo", ""))
    return meta


def build_indices():
    for sigla, (slug, nombre, color) in MATERIAS.items():
        carpeta = DECIMO / sigla / f"{sigla}-Resumenes"
        filas = []
        for md in (carpeta / "fuente").glob("*.md"):
            if (carpeta / f"{md.stem}-resumen.pdf").exists():
                filas.append((md.stem, _meta(md)))
        filas.sort(key=lambda f: (f[1]["fecha"], f[0]))
        ex = EXAMENES.get(sigla, {})
        cuerpo = []
        if ex:
            for _, (_, desde) in ex.items():
                d = dict(filas)[desde]
                cuerpo.append(f'<div class="section-block" style="border-left:4px solid {color}">'
                              f'<strong>Para el 2.º examen, estudia desde la {_label(desde)}</strong> '
                              f'({d["fecha_txt"]} · {html.escape(d["tit"])}).</div>')
        else:
            cuerpo.append('<div class="section-block">Todavía no hay un examen registrado en esta materia: '
                          'los resúmenes van de corrido por clase.</div>')
        cuerpo.append('<table><thead><tr><th>Clase</th><th>Fecha</th><th>Tema</th><th>Guía (PDF)</th></tr></thead><tbody>')
        for stem, m in filas:
            pdf = f"../../decimo/{sigla}/{sigla}-Resumenes/{stem}-resumen.pdf"
            cuerpo.append(f'<tr><td>{_label(stem)}</td><td>{m["fecha_txt"]}</td>'
                          f'<td>{html.escape(m["tit"])}</td>'
                          f'<td><a href="{pdf}" target="_blank">📄 Resumen</a></td></tr>')
            if stem in ex:
                desc, desde = ex[stem]
                cuerpo.append(f'<tr style="background:{color}22"><td colspan="4"><strong>📝 EXAMEN — {html.escape(desc)}</strong>'
                              f'<br>↓ Lo que sigue entra al <strong>2.º examen</strong> (desde la {_label(desde)}).</td></tr>')
        cuerpo.append("</tbody></table>")
        pag = f"""<!-- Generado por scripts/build_resumenes.py --indices. No editar a mano. -->
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Guías de estudio — {nombre}</title>
<link rel="stylesheet" href="../../assets/style.css?v=20261020a">
<script src="../../assets/app.js?v=20261020a" defer></script>
</head>
<body style="--c:{color}">
<div class="wrap">
<a class="back" href="index.html">← {nombre}</a>
<div class="detail-head" style="border-color:{color}"><h2>Guías de estudio por clase</h2>
  <p class="prof">Un PDF por clase: apuntes completos y resumen para estudiar. Los exámenes aparecen marcados en su fecha.</p>
</div>
{chr(10).join(cuerpo)}
</div>
</body>
</html>
"""
        (ROOT / "materias" / slug / "resumenes.html").write_text(pag, encoding="utf-8")
        idx = ROOT / "materias" / slug / "index.html"
        t = idx.read_text(encoding="utf-8")
        if "resumenes.html" not in t:
            card = (f'  <a class="card" style="--c:{color}" href="resumenes.html"><h3>Guías de estudio</h3>'
                    f'<p>Un PDF por clase y marca de dónde cae cada examen</p></a>\n')
            t = re.sub(r'(  <a class="card"[^\n]*href="material\.html"[^\n]*\n)', lambda m: m.group(1) + card, t, count=1)
            idx.write_text(t, encoding="utf-8")
        print("página", slug, len(filas), "clases")


def main(args):
    if "--indices" in args:
        build_indices()
        return
    srcs = sorted(DECIMO.glob("*/*-Resumenes/fuente/*.md"))
    todos = "--todos" in args
    nombres = [a for a in args if not a.startswith("--")]
    for md in srcs:
        pdf = md.parent.parent / f"{md.stem}-resumen.pdf"
        if nombres and md.stem not in nombres:
            continue
        if not (todos or nombres) and pdf.exists() and pdf.stat().st_mtime >= md.stat().st_mtime:
            continue
        print("→", build(md).relative_to(ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])
