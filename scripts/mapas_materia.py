#!/usr/bin/env python3
"""Mapas conceptuales por materia (curso completo) y por examen.

  python3 scripts/mapas_materia.py curso [SIGLA ...]
      → decimo/<SIGLA>/<SIGLA>-Resumenes/<SIGLA>-mapa-curso.pdf
        Centro: la materia. Ramas: los temas del plan (vista «Por tema» de index.html);
        recuadros: subtemas (✓ = ya visto en clase), con sus sub-subtemas.

  python3 scripts/mapas_materia.py examen SIGLA
      → decimo/<SIGLA>/<SIGLA>-Resumenes/<SIGLA>-mapa-examen-N.pdf
        Centro: el examen. Ramas: cada clase que entra; recuadros: los puntos de
        «🎯 Lo que probablemente viene en el examen» de esa clase.
        Los datos de cada examen (clases que entran, fecha, formato) están en EXAMENES.
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mapas_conceptuales as mc  # noqa: E402

ROOT = mc.ROOT
SLUG = {"ASI": "administracion-de-servicios-de-internet", "ACS": "arquitectura-cliente-servidor",
        "FSE": "fundamentos-de-sistemas-embebidos", "MD": "mineria-de-datos",
        "OAC": "organizacion-y-arquitectura-de-computadoras", "RP": "reconocimiento-de-patrones",
        "SIB": "seguridad-informatica-basica"}

# Datos de cada examen próximo. Fuente: audios de clase (vía NotebookLM) y páginas de clase.
EXAMENES = {
    "SIB": dict(n=2, desde=1, hasta=None, titulo="examen final",
                fecha="martes 24 nov 2026, 9:00 (lo confirmó el usuario el 18 nov 2026)",
                formato="Entra TODO el curso («para el siguiente examen lo que tengo que evaluar es todo», "
                        "audio SIB-Clase19); aún por definir si es individual o en equipo"),
    "FSE": dict(n=2, desde=13, hasta=None, fecha="miércoles 25 nov 2026 (Classroom: «Segundo examen parcial», vence 2:30 PM)",
                formato="Entra la Unidad 3 (sistemas operativos embebidos). Ningún audio da fecha ni formato "
                        "(NotebookLM, 14 nov 2026); el 1.er parcial fue de 50 preguntas, 25 abiertas y 25 de opción múltiple",
                dicho=["6 pasos de una llamada a servicio (Clase 13)",
                       "Programa vs. programa en ejecución vs. proceso (Clase 13)",
                       "Orden de atención de las colas con prioridad: analogías «para que se acuerden en el examen» (Clase 17)",
                       "Ejercicios de Minimal Laxity First y la regla de oro de tiempo real; la demostración del 70 % de Rate Monotonic NO viene (Clase 18)",
                       "Los 5 algoritmos de asignación de memoria: First, Next, Best, Worst y Quick Fit (Clase 19)",
                       "Temporizador asíncrono periódico sincronizado con semáforo binario: «pregunta para entrar a Google», no dijo examen (Clase 20)",
                       "Controladores dedicados vs. genéricos: «esto es pregunta de examen» (Clase 21)",
                       "Sistemas de archivos embebidos; initramfs «sí se lo tienen que saber» (Clase 21)"]),
    "ASI": dict(n=2, desde=1, hasta=None, titulo="examen final",
                fecha="miércoles 18 nov 2026 (se movió del lunes 16, que no hay clase; audio ASI-Clase19)",
                formato="Entra TODO el curso («todo, todo, todo, todo») más los RFC; individual, en hojas, sin celular "
                        "y escribiendo código, con base en el examen extraordinario (audio ASI-Clase17)",
                dicho=["Todo el temario del curso, no solo desde el 1.er parcial (Clase 17)",
                       "Los RFC expuestos: 2616, 3501, 1939, 4510, 1700, 854, 1034, 3898 y 8446, más 2081 del temario (Clases 17–19)",
                       "Escribir código en papel (Clase 17)",
                       "Definición de servidor (Clase 3)",
                       "Cubos de información / OLAP (Clase 10, para el examen anterior)"]),
}


def txt(s):
    return html.unescape(re.sub(r"<.*?>", "", s)).strip()


def puntos_examen(sigla, n):
    f = ROOT / "materias" / SLUG[sigla] / f"clase-{n:02d}.html"
    if not f.exists():
        return None, []
    t = f.read_text(encoding="utf-8")
    if 'content="no-aplica"' in t:
        return "examen", []
    m = re.search(r'id="c\d+-examen".*?</details>', t, re.S)
    pts = []
    for li in re.findall(r"<li>(.*?)</li>", m.group(0), re.S) if m else []:
        s = txt(li)
        s = re.split(r"\.?\s*Evidencia\b", s)[0].strip()
        pts.append(mc.corto(s, 125))
    return "ok", pts


def temas_resumenes(sigla):
    """{n: (fecha, tema)} a partir de la tabla de resumenes.html."""
    t = (ROOT / "materias" / SLUG[sigla] / "resumenes.html").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"<tr><td>Clase (-?\d+)</td><td>(.*?)</td><td>(.*?)</td>", t):
        out[int(m.group(1))] = (txt(m.group(2)), txt(m.group(3)))
    return out


def mapa_examen(sigla, por_pagina=8):
    """Devuelve una lista de mapas (una página por cada bloque de hasta `por_pagina` clases)."""
    e = EXAMENES[sigla]
    temas = temas_resumenes(sigla)
    ultimo = max(temas)
    ramas = []
    for n in range(e["desde"], (e["hasta"] or ultimo) + 1):
        estado, pts = puntos_examen(sigla, n)
        if estado != "ok" or not pts:
            continue
        fecha, tema = temas.get(n, ("", ""))
        ramas.append({"t": f"Clase {n} · {mc.corto(tema, 55)}", "hijos": pts[:6]})
    bloques = [ramas[i:i + por_pagina] for i in range(0, len(ramas), por_pagina)]
    # reparte parejo (p. ej. 17 clases → 9 + 8, no 8 + 8 + 1)
    if len(bloques) > 1:
        k = len(bloques)
        tam = -(-len(ramas) // k)
        bloques = [ramas[i:i + tam] for i in range(0, len(ramas), tam)]
    nota = ("Cada rama es una clase que entra al examen; cada recuadro, un punto de «Lo que probablemente "
            "viene en el examen» de esa clase (con su evidencia en la página de la clase). ")
    if e["fecha"]:
        nota += f"Fecha: {e['fecha']}. "
    if e["formato"]:
        nota += e["formato"] + "."
    if e.get("dicho"):
        bloques[0] = [{"t": "★ Lo que el profesor dijo que viene", "hijos": e["dicho"]}] + bloques[0]
    mapas = []
    for i, b in enumerate(bloques, 1):
        cl = [r for r in b if r["t"].startswith("Clase")]
        a_, z_ = cl[0]["t"].split(" ·")[0], cl[-1]["t"].split(" ·")[0]
        nombre = e.get("titulo", f"{e['n']}.º examen")
        centro = f"{nombre[0].upper() + nombre[1:]} de {sigla}"
        sub = f"{a_} a {z_.replace('Clase ', '')}"
        if len(bloques) > 1:
            sub += f" · página {i} de {len(bloques)}"
        centro += "\n" + (e["fecha"].split(" (")[0] if e["fecha"] else "") + (f" · {a_}–{z_.replace('Clase ', '')}" if len(bloques) > 1 else "")
        mapas.append({"titulo": f"{mc.MATERIAS[sigla]} — {nombre}",
                      "subtitulo": f"Mapa del examen · {sub}", "centro": centro.strip(),
                      "color": mc.COLORES[sigla], "ramas": b, "nota": nota})
    return mapas


def render_varias(mapas, pdf):
    import subprocess
    import tempfile
    pdf = Path(pdf)
    if len(mapas) == 1:
        return mc.render(mapas[0], pdf)
    with tempfile.TemporaryDirectory() as td:
        partes = [str(mc.render(m, Path(td) / f"p{i}.pdf")) for i, m in enumerate(mapas)]
        subprocess.run(["/System/Library/Automator/Combine PDF Pages.action/Contents/MacOS/join",
                        "-o", str(pdf), *partes], check=True, capture_output=True)
    return pdf


def mapa_curso(sigla):
    t = (ROOT / "materias" / SLUG[sigla] / "index.html").read_text(encoding="utf-8")
    ramas = []
    for m in re.finditer(r'<details class="section-block tema"[^>]*>\s*<summary><span class="stitle">(.*?)</span>'
                         r'(.*?)</summary>(.*?)</details>', t, re.S):
        tit = txt(m.group(1))
        cuerpo = m.group(3)
        hijos, actual = [], None
        for li in re.findall(r"<li>(.*?)</li>", cuerpo, re.S):
            sn = re.search(r'<span class="sn">(.*?)</span>', li)
            num = txt(sn.group(1)) if sn else ""
            visto = 'class="seen"' in li
            nombre = txt(re.sub(r'<span class="(sn|seen)">.*?</span>', "", li)).rstrip(".")
            etiqueta = mc.corto(nombre, 60) + (" ✓" if visto else "")
            nivel = num.count(".")
            if nivel <= 1 or actual is None:
                actual = {"t": etiqueta, "hijos": []}
                hijos.append(actual)
            elif len(actual["hijos"]) < 5:
                actual["hijos"].append(mc.corto(nombre, 45))
        hijos = [h if h["hijos"] else h["t"] for h in hijos]
        ramas.append({"t": mc.corto(tit, 60), "hijos": hijos[:9]})
    return {"titulo": f"{mc.MATERIAS[sigla]} — mapa del curso", "subtitulo": "Temario oficial completo",
            "centro": mc.MATERIAS[sigla], "color": mc.COLORES[sigla], "ramas": ramas,
            "nota": "Ramas = temas del plan de estudios; recuadros = subtemas (✓ = ya visto en clase, "
                    "según la vista «Por tema» del sitio)."}


def mapas_curso(sigla, por_pagina=8):
    """Página 1: el temario oficial. Siguientes: todo lo visto, clase por clase (temas de cada clase)."""
    mapas = [mapa_curso(sigla)]
    temas = temas_resumenes(sigla)
    fuente = ROOT / "decimo" / sigla / f"{sigla}-Resumenes" / "fuente"
    ramas = []
    for n in sorted(temas):
        md = fuente / f"{sigla}-Clase{('m%02d' % -n) if n < 0 else ('%02d' % n)}.md"
        m = mc.mapa_de_clase(md, sigla) if md.exists() else None
        if not m:
            continue
        ramas.append({"t": f"Clase {n} · {mc.corto(temas[n][1], 50)}", "hijos": [r["t"] for r in m["ramas"]][:7]})
    if ramas:
        k = -(-len(ramas) // por_pagina)
        tam = -(-len(ramas) // k)
        bloques = [ramas[i:i + tam] for i in range(0, len(ramas), tam)]
        for i, b in enumerate(bloques, 1):
            a_, z_ = b[0]["t"].split(" ·")[0], b[-1]["t"].split(" ·")[0].replace("Clase ", "")
            mapas.append({"titulo": f"{mc.MATERIAS[sigla]} — mapa del curso",
                          "subtitulo": f"Todo lo visto en clase · {a_} a {z_} · parte {i} de {len(bloques)}",
                          "centro": f"{mc.MATERIAS[sigla]}\n{a_}–{z_}", "color": mc.COLORES[sigla], "ramas": b,
                          "nota": "Ramas = clases; recuadros = los temas de cada clase, en el orden en que se vieron "
                                  "(de la guía de estudio de cada clase)."})
    return mapas


def main(a):
    base = lambda s: ROOT / "decimo" / s / f"{s}-Resumenes"  # noqa: E731
    if a and a[0] == "curso":
        for s in a[1:] or list(SLUG):
            print("✓", render_varias(mapas_curso(s), base(s) / f"{s}-mapa-curso.pdf").relative_to(ROOT))
    elif a and a[0] == "examen":
        for s in a[1:] or list(EXAMENES):
            n = EXAMENES[s]["n"]
            print("✓", render_varias(mapa_examen(s), base(s) / f"{s}-mapa-examen-{n}.pdf").relative_to(ROOT))
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
