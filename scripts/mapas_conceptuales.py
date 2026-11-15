#!/usr/bin/env python3
"""Mapas conceptuales en PDF horizontal (A4 apaisado), radiales: el tema al centro y
las ramas hacia los lados.

Uso como módulo:  render(mapa: dict, pdf: Path)
  mapa = {"titulo", "subtitulo", "centro", "color", "ramas": [{"t", "hijos": [str|{"t","hijos"}]}],
          "nota" (opcional, pie de página)}

Uso como script:
  python3 scripts/mapas_conceptuales.py clases [SIGLA ...]   → <SIGLA>-ClaseNN-mapa.pdf junto a cada resumen
  python3 scripts/mapas_conceptuales.py json archivo.json salida.pdf

Los mapas por clase salen de la PARTE 1 de decimo/<SIGLA>/<SIGLA>-Resumenes/fuente/<SIGLA>-ClaseNN.md:
cada «##» es una rama y los conceptos son los términos en negrita, los recuadros «!!!» y la primera
columna de las tablas de esa sección. No se inventa nada: todo sale del texto de los apuntes.
"""
import html
import json
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

COLORES = {"ASI": "#5B7FC4", "ACS": "#D9604A", "FSE": "#8B6BBE", "MD": "#8B6BBE",
           "OAC": "#2E9C8C", "RP": "#2E9C8C", "SIB": "#D9604A"}
MATERIAS = {"ASI": "Administración de Servicios de Internet", "ACS": "Arquitectura Cliente-Servidor",
            "FSE": "Fundamentos de Sistemas Embebidos", "MD": "Minería de Datos",
            "OAC": "Organización y Arquitectura de Computadoras", "RP": "Reconocimiento de Patrones",
            "SIB": "Seguridad Informática Básica"}
PALETA = ["#E07A5F", "#3D85C6", "#6AA84F", "#B4689B", "#E69138", "#45818E", "#8E7CC3",
          "#C27BA0", "#76A5AF", "#CC4125", "#93C47D", "#674EA7"]

PLANTILLA = r"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<style>
@page { size: 297mm 210mm; margin: 0; }
html, body { margin: 0; padding: 0; }
body { width: 297mm; height: 210mm; overflow: hidden; font-family: Arial, "Helvetica Neue", sans-serif;
  color: #1d1d1f; background: #fff; position: relative; }
header { position: absolute; top: 6mm; left: 10mm; right: 10mm; display: flex; justify-content: space-between;
  align-items: baseline; border-bottom: 1.2px solid __COLOR__; padding-bottom: 1.5mm; }
header h1 { font-size: 13pt; margin: 0; color: __COLOR__; }
header span { font-size: 8.5pt; color: #555; }
footer { position: absolute; bottom: 4mm; left: 10mm; right: 10mm; font-size: 7pt; color: #777; }
#area { position: absolute; top: 17mm; bottom: 17mm; left: 6mm; right: 6mm; }
#lienzo { position: absolute; left: 0; top: 0; width: max-content; }
svg#lineas { position: absolute; left: 0; top: 0; overflow: visible; }
.mapa { display: flex; align-items: center; gap: 46px; }
.lado { display: flex; flex-direction: column; gap: 12px; }
.rama { display: flex; align-items: center; gap: 22px; }
.izq .rama { flex-direction: row-reverse; }
.izq .hijos { align-items: flex-end; }
.nodo-rama { font-weight: 700; font-size: 11pt; color: #fff; padding: 6px 10px; border-radius: 9px;
  max-width: 190px; line-height: 1.2; text-align: center; }
.hijos { display: flex; flex-direction: column; gap: 4px; }
.hijo { font-size: 9pt; line-height: 1.2; padding: 3px 7px; border: 1.3px solid; border-radius: 6px;
  background: #fff; max-width: 270px; }
.nieto { font-size: 7.6pt; color: #444; margin-top: 2px; }
.centro { font-size: 15pt; font-weight: 700; text-align: center; color: #fff; background: __COLOR__;
  padding: 14px 18px; border-radius: 50%; min-width: 150px; max-width: 220px; min-height: 90px;
  display: flex; flex-direction: column; align-items: center; justify-content: center; line-height: 1.2;
  box-shadow: 0 0 0 4px #fff, 0 0 0 6px __COLOR__; }
</style></head><body>
<header><h1>__TITULO__</h1><span>__SUB__</span></header>
<div id="area"><div id="lienzo"><svg id="lineas"></svg>
<div class="mapa"><div class="lado izq">__IZQ__</div><div class="centro" id="centro">__CENTRO__</div>
<div class="lado der">__DER__</div></div></div></div>
<footer>__NOTA__</footer>
<script>
(function(){
 const lz=document.getElementById('lienzo'), area=document.getElementById('area'), svg=document.getElementById('lineas');
 const W=lz.scrollWidth, H=lz.scrollHeight; svg.setAttribute('width',W); svg.setAttribute('height',H);
 const r=e=>{const b=e.getBoundingClientRect(), o=lz.getBoundingClientRect(); return {l:b.left-o.left,r:b.right-o.left,t:b.top-o.top,b:b.bottom-o.top,cy:(b.top+b.bottom)/2-o.top,cx:(b.left+b.right)/2-o.left};};
 const curva=(x1,y1,x2,y2,c,w)=>{const p=document.createElementNS('http://www.w3.org/2000/svg','path'); const m=(x1+x2)/2;
   p.setAttribute('d',`M${x1},${y1} C${m},${y1} ${m},${y2} ${x2},${y2}`); p.setAttribute('stroke',c); p.setAttribute('stroke-width',w);
   p.setAttribute('fill','none'); p.setAttribute('stroke-linecap','round'); svg.appendChild(p);};
 const ce=r(document.getElementById('centro'));
 document.querySelectorAll('.rama').forEach(ra=>{
   const izq=ra.closest('.izq'), n=ra.querySelector('.nodo-rama'), c=n.dataset.c, rn=r(n);
   curva(izq?ce.l:ce.r, ce.cy, izq?rn.r:rn.l, rn.cy, c, 3.2);
   ra.querySelectorAll('.hijo').forEach(h=>{const rh=r(h); curva(izq?rn.l:rn.r, rn.cy, izq?rh.r:rh.l, rh.cy, c, 1.4);});
 });
 const s=Math.min(area.clientWidth/W, area.clientHeight/H, 1.35);
 lz.style.zoom=s;
 lz.style.left=((area.clientWidth-W*s)/2/s)+'px'; lz.style.top=((area.clientHeight-H*s)/2/s)+'px';
})();
</script></body></html>"""


def esc(s):
    """Escapa texto pero conserva <sub>, <sup>, <em> simples."""
    s = html.escape(s, quote=False)
    return re.sub(r"&lt;(/?)(sub|sup|em)&gt;", r"<\1\2>", s)


def _rama_html(rama, color):
    hijos = []
    for h in rama.get("hijos", []):
        if isinstance(h, dict):
            nietos = "".join(f'<div class="nieto">• {esc(x)}</div>' for x in h.get("hijos", []))
            hijos.append(f'<div class="hijo" style="border-color:{color}">{esc(h["t"])}{nietos}</div>')
        else:
            hijos.append(f'<div class="hijo" style="border-color:{color}">{esc(h)}</div>')
    return (f'<div class="rama"><div class="nodo-rama" data-c="{color}" style="background:{color}">'
            f'{esc(rama["t"])}</div><div class="hijos">{"".join(hijos)}</div></div>')


def _peso(rama):
    return 1 + sum(1 + (len(h.get("hijos", [])) * 0.6 if isinstance(h, dict) else 0)
                   for h in rama.get("hijos", []))


def render(mapa, pdf):
    ramas = mapa["ramas"]
    color = mapa.get("color", "#333")
    con_color = [(r, PALETA[i % len(PALETA)]) for i, r in enumerate(ramas)]
    # Reparte las ramas entre derecha (primera mitad, como manecillas del reloj) e izquierda,
    # equilibrando el «peso» de cada lado.
    total = sum(_peso(r) for r in ramas)
    der, izq, acc = [], [], 0
    for r, c in con_color:
        if acc < total / 2 or not der:
            der.append((r, c))
            acc += _peso(r)
        else:
            izq.append((r, c))
    if not izq and len(der) > 1:
        izq.append(der.pop())
    izq.reverse()  # para que se lean en sentido de las manecillas del reloj
    doc = (PLANTILLA.replace("__COLOR__", color)
           .replace("__TITULO__", esc(mapa.get("titulo", "")))
           .replace("__SUB__", esc(mapa.get("subtitulo", "")))
           .replace("__CENTRO__", esc(mapa.get("centro", "")).replace("\n", "<small style=\"font-size:9.5pt;font-weight:400;margin-top:4px\">", 1) + ("</small>" if "\n" in mapa.get("centro", "") else ""))
           .replace("__NOTA__", esc(mapa.get("nota", "")))
           .replace("__DER__", "".join(_rama_html(r, c) for r, c in der))
           .replace("__IZQ__", "".join(_rama_html(r, c) for r, c in izq)))
    pdf = Path(pdf)
    pdf.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        h = Path(td) / "m.html"
        h.write_text(doc, encoding="utf-8")
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=3000", "--window-size=1123,794", f"--print-to-pdf={pdf}", h.as_uri()],
                       check=True, capture_output=True)
    return pdf


# ---------- Mapas por clase, a partir de la fuente .md ----------

def limpiar(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    s = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", s)
    return s.strip(" .:;,—-·")


def corto(s, n=60):
    s = limpiar(s)
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


RELLENO = {"en simple", "explicado en simple", "qué es", "cómo funciona", "por qué importa", "errores comunes",
           "por qué importa / con qué se conecta", "ojo", "importante", "nota", "ejemplo", "resumen",
           "para el examen", "dato clave", "atención", "recuerda", "en corto"}


def conceptos(texto, maxn=6):
    vistos, out = set(), []

    def add(x):
        x = corto(x, 58)
        k = x.lower()
        if (len(x) < 2 or k in vistos or re.fullmatch(r"[\d.,%\s≈~→]+", x) or k in RELLENO
                or re.fullmatch(r"\(.*\)", x)):
            return
        vistos.add(k)
        out.append(x)

    for ln in texto.splitlines():
        if ln.startswith("!!! "):
            add(ln[4:])
    for ln in texto.splitlines():
        if ln.startswith("|") and not re.match(r"^\|\s*-", ln):
            cel = [c.strip() for c in ln.strip("|").split("|")]
            if cel and cel[0]:
                out_before = len(out)
                add(cel[0])
                # la primera fila de una tabla suele ser el encabezado: la quitamos si es genérica
                if len(out) > out_before and out[-1].lower() in {"elemento", "paso", "concepto", "línea",
                                                                 "término", "tipo", "caso", "aspecto",
                                                                 "bus", "comando", "parámetro", "campo",
                                                                 "fase", "nivel", "modelo", "método", "algoritmo",
                                                                 "característica", "criterio", "pregunta", "cálculo", "dato", "valor", "función", "definición", "qué es", "concepto clave"}:
                    vistos.discard(out.pop().lower())
    for m in re.finditer(r"\*\*(.+?)\*\*", texto):
        add(m.group(1))
    return out[:maxn]


def mapa_de_clase(md: Path, sigla: str):
    t = md.read_text(encoding="utf-8")
    meta = dict(re.findall(r"^% (\w+): (.*)$", t, re.M))
    parte1 = re.split(r"^# PARTE 2", t, flags=re.M)[0]
    secs = re.split(r"^## (.+)$", parte1, flags=re.M)
    ramas = []
    for i in range(1, len(secs), 2):
        tit = limpiar(secs[i])
        if re.match(r"(?i)contexto|anécdota|pendiente", tit):
            continue
        tit = re.sub(r"^\d+(\.\d+)*\.?\s+", "", tit)
        ramas.append({"t": corto(tit, 70), "hijos": conceptos(secs[i + 1])})
    if not ramas:
        return None
    titulo = meta.get("titulo", md.stem)
    centro = re.sub(r"^Clase -?\d+\s*·\s*", "", titulo)
    sub = meta.get("subtitulo", "")
    fecha = next((p for p in sub.split(" · ") if re.search(r"\d{4}", p)), "")
    return {"titulo": f"{MATERIAS.get(sigla, sigla)} — {titulo.split(' · ')[0]}",
            "subtitulo": f"Mapa conceptual · {fecha}",
            "centro": corto(centro, 90), "color": COLORES.get(sigla, "#333"), "ramas": ramas[:10],
            "nota": "Generado de los apuntes de la clase (Parte 1 de la guía de estudio). "
                    "Cada rama es un tema en el orden de la clase; cada recuadro, un concepto de esa parte."}


def clases(siglas):
    hechos = []
    for s in siglas:
        for md in sorted((DECIMO / s / f"{s}-Resumenes" / "fuente").glob(f"{s}-Clase*.md")):
            m = mapa_de_clase(md, s)
            if not m:
                print("  sin ramas:", md.name)
                continue
            pdf = md.parent.parent / f"{md.stem}-mapa.pdf"
            render(m, pdf)
            hechos.append(pdf)
            print("  ✓", pdf.relative_to(ROOT))
    return hechos


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "clases":
        clases(a[1:] or list(COLORES))
    elif a and a[0] == "json":
        render(json.loads(Path(a[1]).read_text(encoding="utf-8")), a[2])
    else:
        print(__doc__)
