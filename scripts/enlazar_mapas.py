#!/usr/bin/env python3
"""Agrega los mapas conceptuales a materias/<slug>/resumenes.html (idempotente).

- Columna «Mapa» al lado de cada guía: decimo/<SIGLA>/<SIGLA>-Resumenes/<SIGLA>-ClaseNN-mapa.pdf
- Recuadro arriba de la tabla con el mapa del curso y el mapa del examen (si existen).
- Filas de clases a las que no se asistió y que no tienen resumen (FALTAS), marcadas «Falta».

Correr después de scripts/build_resumenes.py --indices (que reescribe esas páginas).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLUG = {"ASI": "administracion-de-servicios-de-internet", "ACS": "arquitectura-cliente-servidor",
        "FSE": "fundamentos-de-sistemas-embebidos", "MD": "mineria-de-datos",
        "OAC": "organizacion-y-arquitectura-de-computadoras", "RP": "reconocimiento-de-patrones",
        "SIB": "seguridad-informatica-basica"}
# Clases sin resumen porque el usuario no asistió y no hay audio ni material: (n, fecha, tema)
FALTAS = {"MD": [(17, "29 oct", "No asistí: no hay audio ni material del profesor")]}
MARCA = "<!-- mapas -->"


def num(n):
    return f"m{abs(n):02d}" if n < 0 else f"{n:02d}"


def main():
    for s, slug in SLUG.items():
        f = ROOT / "materias" / slug / "resumenes.html"
        t = f.read_text(encoding="utf-8")
        res = ROOT / "decimo" / s / f"{s}-Resumenes"
        rel = f"../../decimo/{s}/{s}-Resumenes"
        # limpiar lo inyectado antes
        t = re.sub(r'<td class="mapa">.*?</td>', "", t)
        t = t.replace("<th>Mapa</th>", "")
        t = re.sub(rf"{MARCA}.*?{MARCA}\n?", "", t, flags=re.S)
        t = re.sub(r'<tr class="falta">.*?</tr>\n?', "", t)
        # filas de faltas
        for n, fecha, tema in FALTAS.get(s, []):
            fila = (f'<tr class="falta"><td>Clase {n}</td><td>{fecha}</td><td>{tema}</td>'
                    f'<td>❌ Falta</td></tr>\n')
            prev = re.search(rf"<tr><td>Clase {n - 1}</td>.*?</tr>\n", t)
            if prev:
                t = t[:prev.end()] + fila + t[prev.end():]
        # columna Mapa
        t = t.replace("<th>Guía (PDF)</th>", "<th>Guía (PDF)</th><th>Mapa</th>")

        def celda(m):
            fila = m.group(0)
            c = re.match(r'<tr(?: class="falta")?><td>Clase (-?\d+)</td>', fila)
            if not c:
                return fila
            n = int(c.group(1))
            pdf = res / f"{s}-Clase{num(n)}-mapa.pdf"
            if 'class="falta"' in fila:
                td = '<td class="mapa">❌ Falta</td>'
            elif pdf.exists():
                td = f'<td class="mapa"><a href="{rel}/{pdf.name}" target="_blank">🗺️ Mapa</a></td>'
            else:
                td = '<td class="mapa">—</td>'
            return fila[:-5] + td + "</tr>"

        t = re.sub(r"<tr(?: class=\"falta\")?><td>Clase -?\d+</td>.*?</tr>", celda, t)
        # filas de examen con colspan=4 → 5
        t = t.replace('<td colspan="4">', '<td colspan="5">')
        # recuadro con mapas de curso y examen
        enl = []
        curso = res / f"{s}-mapa-curso.pdf"
        if curso.exists():
            enl.append(f'<a href="{rel}/{curso.name}" target="_blank">🗺️ Mapa del curso completo</a>')
        for ex in sorted(res.glob(f"{s}-mapa-examen-*.pdf")):
            enl.append(f'<a href="{rel}/{ex.name}" target="_blank">🎯 Mapa de lo que viene en el examen</a>')
        if enl:
            caja = (f'{MARCA}<div class="section-block" style="border-left:4px solid var(--c)">'
                    f'<strong>Mapas conceptuales:</strong> {" · ".join(enl)}</div>{MARCA}\n')
            t = t.replace("<table>", caja + "<table>", 1)
        f.write_text(t, encoding="utf-8")
        print("✓", f.relative_to(ROOT))


if __name__ == "__main__":
    main()
