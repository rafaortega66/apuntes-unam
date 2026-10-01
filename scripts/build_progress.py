#!/usr/bin/env python3
"""
Genera assets/progreso.json: qué clases hay en el sitio por materia (número,
fecha, resumen, formato) + las últimas entradas del git log.

La página progreso.html cruza esto contra assets/horario.json para mostrar
qué clases faltan y cuál es la siguiente que hay que meter. El cálculo de
"faltantes" se hace en el navegador (con la fecha de hoy), así que no hace
falta regenerar el JSON cada día — solo cuando se agrega o edita una clase.

Lo corre automáticamente scripts/build_search_index.py; también se puede
correr solo:
    python3 scripts/build_progress.py
"""
import glob
import html
import json
import os
import re
import subprocess
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(ROOT, "assets", "progreso.json")
HORARIO = os.path.join(ROOT, "assets", "horario.json")

MESES = {m: i + 1 for i, m in enumerate(
    ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"])}
FECHA_RE = re.compile(r"(\d{1,2}) (?:de )?(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\w*\.? (?:de )?(\d{4})")


def strip_tags(s):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", s)).split())


def formato(src):
    """estudio = formato nuevo orientado a examen (meta formato=estudio);
    prosa = formato del 16 sep (cuerpo completo en <details class="section-block sec">);
    viejo = resumen "En corto"/"Para el examen"."""
    if re.search(r'<meta name="formato" content="estudio', src):
        return "estudio"
    if 'class="section-block sec"' in src:
        return "prosa"
    return "viejo"


def clase_info(path, slug):
    src = open(path, encoding="utf-8").read()
    num = int(re.search(r"clase-(\d+)\.html$", path).group(1))
    head = re.search(r'<div class="detail-head".*?</div>', src, re.S)
    prof = re.search(r'<p class="prof">(.*?)</p>', head.group(0) if head else src, re.S)
    texto = strip_tags(prof.group(1)) if prof else ""
    m = FECHA_RE.search(texto) or FECHA_RE.search(strip_tags(src[:20000]))
    fecha = f"{m.group(3)}-{MESES[m.group(2)]:02d}-{int(m.group(1)):02d}" if m else None
    # resumen = lo que va después de la fecha en la línea del profesor
    resumen = texto[m.end():].lstrip(" ·—-") if m and m.group(0) in texto else texto
    return {
        "num": num,
        "fecha": fecha,
        "resumen": resumen[:220],
        "url": f"materias/{slug}/clase-{num:02d}.html",
        "formato": formato(src),
    }


def git_log(n=60):
    try:
        out = subprocess.run(
            ["git", "log", f"-{n}", "--date=iso-strict", "--format=%h%x1f%ad%x1f%s"],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except Exception:
        return []
    log = []
    for line in out.strip().splitlines():
        h, d, s = line.split("\x1f", 2)
        log.append({"hash": h, "fecha": d, "mensaje": s})
    return log


def main():
    horario = json.load(open(HORARIO, encoding="utf-8"))
    materias = {}
    for m in horario["materias"]:
        clases = [clase_info(p, m["slug"])
                  for p in sorted(glob.glob(os.path.join(ROOT, "materias", m["slug"], "clase-*.html")))]
        materias[m["slug"]] = sorted(clases, key=lambda c: c["num"])
    out = {
        "generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "materias": materias,
        "gitlog": git_log(),
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    total = sum(len(v) for v in materias.values())
    sin_fecha = [c["url"] for v in materias.values() for c in v if not c["fecha"]]
    print(f"OK: {total} clases -> {OUT_PATH}")
    for u in sin_fecha:
        print(f"  ⚠️ sin fecha detectable: {u}")


if __name__ == "__main__":
    main()
