import sys, re, html, subprocess, json
from pathlib import Path
sys.path.insert(0, "/Users/rafa/Desktop/apuntes-unam/scripts")
import build_resumenes as br
S = Path(sys.argv[1]); OUT = Path(sys.argv[2])
order = [f"{n:02d}" for n in range(0, 13)] + ["99"]
body = "\n".join((S/"doc2"/f"{k}.md").read_text() for k in order)
h = br.render_lines(body.splitlines())
toc = []
def mark(m):
    lvl, txt = m.group(1), m.group(3)
    n = len(toc); toc.append((lvl, re.sub(r"<[^>]+>", "", txt)))
    return f'<h{lvl}{m.group(2)} id="s{n}">{txt}<span class="mk">zqx{n}qz</span></h{lvl}>'
h = re.sub(r'<h([12])((?: class="[^"]*")?)>(.*?)</h\1>', mark, h)
CSS = br.CSS + """
@page { @top-right { content: "FSE · Unidad 3 · Guía para el 2.º parcial"; font: 8pt Arial; color:#777 }
        @bottom-center { content: "Página " counter(page) " de " counter(pages); font: 8pt Arial; color:#777 } }
h1.parte { break-before: page; }
.mk { font-size: 1px; color: #fff; }
h3 { color: #1a3d7c; border-top: 1px solid #e3e7ee; padding-top: 2mm; }
.toc h2 { font-size: 15pt; color:#1a3d7c; border-bottom: 1.5px solid #1a3d7c; }
.toc a { color: #111; text-decoration: none; display: flex; }
.toc .l1 { font-weight: 700; margin: 2.4mm 0 .6mm; font-size: 10.5pt; }
.toc .l2 { margin: .4mm 0 .4mm 6mm; font-size: 9.6pt; color:#333 }
.toc .dots { flex: 1; border-bottom: 1px dotted #aaa; margin: 0 1.5mm .9mm; }
.cover { text-align:center; padding-top: 55mm; break-after: page; }
.cover h1 { font-size: 26pt; margin: 0 0 4mm; color:#1a3d7c }
.cover .s { font-size: 12.5pt; color:#444; margin: 1.5mm 0 }
"""
def build(pages):
    items = "".join(
        f'<div class="l{l}"><a href="#s{i}"><span>{html.escape(t)}</span><span class="dots"></span><span>{pages.get(i, "000")}</span></a></div>'
        for i, (l, t) in enumerate(toc))
    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>FSE · Unidad 3 · Guía de estudio</title>
<style>{CSS}</style></head><body>
<div class="cover"><h1>Fundamentos de Sistemas Embebidos</h1>
<div class="s"><b>Unidad 3 · Sistemas operativos para plataformas embebidas</b></div>
<div class="s">Guía de estudio por concepto para el segundo examen parcial (25 nov 2026)</div>
<div class="s">Presentaciones del M.C. José Mauricio Matamoros de María y Campos + lo que explicó en clase + sus ejemplos para acordarse</div>
<div class="s" style="margin-top:12mm;color:#777">Generado el 25 nov 2026 · Fuentes: diapositivas de Classroom, audios en NotebookLM y apuntes del sitio</div></div>
<div class="toc"><h2>Índice</h2>{items}</div>
{h}</body></html>"""
    hp = S/"lectura.html"; hp.write_text(doc)
    subprocess.run([br.CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={OUT}", hp.as_uri()], check=True, capture_output=True)
    r = subprocess.run(["swift", str(S/"findmarks.swift"), str(OUT)], capture_output=True, text=True, check=True).stdout
    found = {int(m.group(1)): int(m.group(2)) for m in re.finditer(r"zqx(\d+)qz (\d+)", r)}
    print(r.splitlines()[0], "marcas:", len(found), "de", len(toc))
    return found
p1 = build({})
p2 = build(p1)
print("estable:", p1 == p2)
