#!/usr/bin/env python3
"""Genera materias/<slug>/guia-final.html (una por materia) y guias-finales.html (índice)
a partir de las guías para el examen final que hizo NotebookLM (Drive, 16 nov 2026),
exportadas a Markdown en decimo/<SIGLA>/<SIGLA>-Resumenes/fuente/<SIGLA>-guia-examen-final.md.

Uso: python3 scripts/build_guias_finales.py
Para actualizar una guía: volver a exportar el Doc de Drive a Markdown en esa ruta y correr el script.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSSV = '20261117b'

DRIVE_DOC = 'https://docs.google.com/document/d/{}/edit'
DRIVE_PDF = 'https://drive.google.com/file/d/{}/view'

MATERIAS = [
    # sigla, slug, nombre, color, guía (Doc), apuntes y resumen (Doc), mapa mental detallado (PDF)
    ('ACS', 'arquitectura-cliente-servidor', 'Arquitectura Cliente-Servidor', '#E8735C',
     '1NeYIiZeyNwmtHDzR47WpThlRyYFDc20t08GeO-QP-lI', '1ELLf3oMJ5i-f0PS7EiQ7FB_y3HvNln5Hvm6h9KzKR_U', '1i204QLbxnoZ0j5es2cWGmDgKv-Ss78GN'),
    ('ASI', 'administracion-de-servicios-de-internet', 'Administración de Servicios de Internet', '#7C9CD6',
     '1jhbhQWg9nWUX9Px6uBr-bMdaofB0ESfnrTV-fPn3UnY', '1QOPXf275iYkitd4E6XimdhAxFfP8pfzF7WxZEyp1F3s', '1GdsSfaS1vmDQ8qhMVHJ6-FnjGQPSz6ly'),
    ('FSE', 'fundamentos-de-sistemas-embebidos', 'Fundamentos de Sistemas Embebidos', '#A98BD1',
     '1MDfj1ayv8KlybmUOZIMJEjV0mshScoi-AwayxL3bV10', '1d534lgJF7VyRr3iqVfk_tFMGIDQ_k90JzydHd0qbQlU', '1Wipwbb5Fpro5IDL-hTPl4r7m19h-JdR4'),
    ('MD', 'mineria-de-datos', 'Minería de Datos', '#A98BD1',
     '18DOhoWrCpib07wG_QY24YEFlecwCeawitLKimn37Zek', '1xSlr_WSZeO7lX4Ilz1q5PlKbrUUDaLghGa5uCqt2wx4', '1ZRUAWQFLvSqrcL4g6SMeetm9xIkQGQhs'),
    ('OAC', 'organizacion-y-arquitectura-de-computadoras', 'Organización y Arquitectura de Computadoras', '#45B8A8',
     '10oh4HJ7SUQ3XR6ytJAeGq9BeUQAjWuUBcACQ4jjsq5Q', '16T4v--amtvC2Dj1URuxguQyFZxnF0PHEYn3TbKtFX6s', '1i3NjsfsZoMaEed9XAvZ17GjAFSGkp88B'),
    ('RP', 'reconocimiento-de-patrones', 'Reconocimiento de Patrones', '#45B8A8',
     '1KIjXNfAu3HNb_u0f9eZ5BW4n2MF3Ih1a9OYjjjjZRfs', '1JLhvnxOuCkfadJVRzaB8cBuf2wVN30ZUmzj0v-bzATs', '1XDD3QuG9tcZ1EOVjUJAbFWS2k4P-lgdn'),
    ('SIB', 'seguridad-informatica-basica', 'Seguridad Informática Básica', '#E8735C',
     '1kElhsg7coX46Yx_M1CEWED3phoRe-IeL3epGx42dxRM', '1_U1AzAhjld-K4CymGqSvkK43idNyWCBea4SNZlTPRtM', '1JR69n3Uu10ErKszrFn69Von1IV0CYPgK'),
]


def unescape_md(s):
    return re.sub(r'\\([\\`*_{}\[\]()#+\-.!>=|~<])', r'\1', s)


def inline(s):
    s = html.escape(unescape_md(s), quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'&lt;(https?://[^\s&]+)&gt;', r'<a href="\1" target="_blank">\1</a>', s)
    return s.replace('<strong></strong>', '')


def plain(s):
    return re.sub(r'<[^>]+>', '', inline(s)).strip()


def slugify(s, used):
    base = re.sub(r'[^a-z0-9]+', '-', plain(s).lower()
                  .translate(str.maketrans('áéíóúüñ', 'aeiouun'))).strip('-')[:40] or 'sec'
    slug, n = base, 2
    while slug in used:
        slug, n = f'{base}-{n}', n + 1
    used.add(slug)
    return slug


def convert(md, sigla):
    """Markdown (export de Google Docs) -> (html_cuerpo, subtítulo)."""
    lines = md.replace('\r', '').split('\n')
    out, para, used = [], [], set()
    list_stack = []  # niveles de sangría abiertos
    in_table, table_rows = False, []
    section_open = False
    sub = []

    def flush_para():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para.clear()

    def close_lists(level=-1):
        while list_stack and list_stack[-1] > level:
            list_stack.pop()
            out.append('</li></ul>')

    def flush_table():
        nonlocal in_table
        if not table_rows:
            in_table = False
            return
        rows = [r for r in table_rows if not re.match(r'^\|\s*:?-{2,}', r)]
        cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
        h = '<div class="tabla-scroll"><table>'
        for i, row in enumerate(cells):
            tag = 'th' if i == 0 else 'td'
            h += '<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in row) + '</tr>'
        out.append(h + '</table></div>')
        table_rows.clear()
        in_table = False

    def close_section():
        nonlocal section_open
        if section_open:
            out.append('</details>')
            section_open = False

    first_h1 = True
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        # tablas
        if stripped.startswith('|'):
            flush_para(); close_lists()
            in_table = True
            table_rows.append(stripped)
            continue
        elif in_table:
            flush_table()

        if not stripped:
            flush_para()
            continue
        if re.fullmatch(r'(#+\s*)?(\\?-){3,}|\*{3,}|_{3,}', stripped):
            flush_para(); close_lists()
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        bm = None if m else re.fullmatch(r'\*\*(.{3,220})\*\*:?', stripped)
        if bm:  # Docs exporta muchos títulos como párrafo en negritas
            t = unescape_md(bm.group(1)).strip('* ')
            es_seccion = re.match(r'(\d+\.\s|UNIDAD|Unidad|LO QUE|Lo que|CONEXIONES|Conexiones|HILO|Hilo|Anexo|TEMAS|UNIDADES)', t)
            if es_seccion or ('**' not in bm.group(1) and len(t) <= 120):
                m = re.match(r'^(#{1,6})\s+(.*)$', ('##' if es_seccion else '####') + ' ' + stripped)
        if m:
            level, text = len(m.group(1)), m.group(2).strip()
            txt = plain(text)
            if not txt or re.fullmatch(r'-{3,}', txt):
                continue
            flush_para(); close_lists()
            if level == 1 and first_h1:
                first_h1 = False
                continue  # el título ya va en el encabezado de la página
            if re.match(r'(UNIDAD|Unidad)\s+\d', txt):
                level = 2  # cada unidad, su propio desplegable
            if 'UNIDADES Y TEMAS' in txt.upper():
                continue
            if len(txt) > 140:  # párrafos que Docs exportó como encabezado
                cls = 'nota' if txt.startswith('>') or 'fuente' in txt.lower()[:60] else ''
                out.append(f'<p class="{cls}">' + inline(text.replace('**', '')).lstrip('&gt; ') + '</p>')
                continue
            if level <= 2:
                close_section()
                sid = slugify(text, used)
                low = txt.lower()
                abierto = ' open' if ('probablemente' in low or 'hilo conductor' in low) else ''
                out.append(f'<details class="section-block sec" id="gf-{sid}"{abierto}>'
                           f'<summary><span class="stitle">{html.escape(txt)}</span></summary>')
                section_open = True
            else:
                tag = 'h3' if level == 3 else 'h4'
                out.append(f'<{tag}>{html.escape(txt)}</{tag}>')
            continue
        # listas (incluye "> * " de Docs)
        lm = re.match(r'^(\s*)(?:>\s*)?([*\-+]|\d+[.)])\s+(.*)$', line)
        if lm:
            flush_para()
            indent = len(lm.group(1).replace('\t', '    '))
            level = indent // 2
            if not list_stack or level > list_stack[-1]:
                out.append('<ul><li>')
                list_stack.append(level)
            else:
                close_lists(level)
                if list_stack and list_stack[-1] == level:
                    out.append('</li><li>')
                else:
                    out.append('<ul><li>')
                    list_stack.append(level)
            out.append(inline(lm.group(3)))
            continue
        text = re.sub(r'^>\s?', '', stripped)
        if list_stack and raw.startswith(' '):
            out.append(' ' + inline(text))
            continue
        close_lists()
        if not out and not section_open:
            sub.append(text)
            continue
        para.append(text)
    flush_para(); close_lists()
    if in_table:
        flush_table()
    close_section()
    return '\n'.join(out), ' '.join(sub)


PAGE = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="formato" content="no-aplica">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Guía para el examen final — {nombre}</title>
<link rel="stylesheet" href="../../assets/style.css?v={cssv}">
<script src="../../assets/app.js?v={cssv}" defer></script>
<style>
.gf h3{{margin:1.2em 0 .4em}} .gf h4{{margin:1em 0 .3em;opacity:.9}}
.gf .tabla-scroll{{overflow-x:auto}} .gf table td,.gf table th{{font-size:.9em;vertical-align:top}}
.gf p.nota{{border-left:3px solid var(--c);padding:.3em .8em;opacity:.9}}
.gf li{{margin:.25em 0}}
</style>
</head>
<body style="--c:{color}">
<div class="wrap gf">
<!-- Generado por scripts/build_guias_finales.py. No editar a mano. -->
<a class="back" href="index.html">← {nombre}</a>
<div class="detail-head" style="border-color:{color}"><h2>📘 Guía para el examen final</h2>
  <p class="prof">{nombre} · semestre 2027-1 · hecha con NotebookLM a partir de los audios de clase y el material del profesor (16 nov 2026).</p>
  <p class="prof">Las fechas y cálculos de NotebookLM pueden fallar: ante la duda, revisa la página de la clase que cita.</p>
</div>
<div class="files">
  <a class="btn" href="{drive_guia}" target="_blank">📄 Original en Drive</a>
  <a class="btn" href="{drive_resumen}" target="_blank">📝 Apuntes y resumen (Drive)</a>
  <a class="btn" href="{drive_mapa}" target="_blank">🧠 Mapa mental detallado</a>
  {extra}<a class="btn" href="resumenes.html">📚 Guías por clase</a>
</div>
{cuerpo}
</div>
</body>
</html>
'''

INDEX = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Guías para el examen final</title>
<link rel="stylesheet" href="assets/style.css?v={cssv}">
<script src="assets/app.js?v={cssv}" defer></script>
</head>
<body>
<div class="wrap">
<!-- Generado por scripts/build_guias_finales.py. No editar a mano. -->
<a class="back" href="index.html">← Inicio</a>
<div class="detail-head"><h2>📘 Guías para el examen final</h2>
  <p class="prof">Una por materia: hilo conductor, unidades con sus conceptos, lo que más probablemente viene y conexiones. Hechas con NotebookLM (16 nov 2026).</p>
</div>
<div class="cards">
{cards}
</div>
</div>
</body>
</html>
'''


def main():
    cards = []
    for sigla, slug, nombre, color, g, r, mapa in MATERIAS:
        src = ROOT / 'decimo' / sigla / f'{sigla}-Resumenes' / 'fuente' / f'{sigla}-guia-examen-final.md'
        if not src.exists():
            print('falta', src)
            continue
        cuerpo, _ = convert(src.read_text(encoding='utf-8'), sigla)
        extra = ''
        if (ROOT / 'materias' / slug / 'examen-final.html').exists():
            extra += '<a class="btn" href="examen-final.html">📝 Repaso del examen</a>\n  '
        for p in sorted((ROOT / 'decimo' / sigla / f'{sigla}-Resumenes').glob(f'{sigla}-mapa-examen*.pdf')):
            extra += f'<a class="btn" href="../../decimo/{sigla}/{sigla}-Resumenes/{p.name}" target="_blank">🗺️ Mapa de examen</a>\n  '
        page = PAGE.format(nombre=nombre, color=color, cssv=CSSV, cuerpo=cuerpo, extra=extra,
                           drive_guia=DRIVE_DOC.format(g), drive_resumen=DRIVE_DOC.format(r),
                           drive_mapa=DRIVE_PDF.format(mapa))
        (ROOT / 'materias' / slug / 'guia-final.html').write_text(page, encoding='utf-8')
        cards.append(f'  <a class="card" style="--c:{color}" href="materias/{slug}/guia-final.html">'
                     f'<h3>{sigla}</h3><p>{nombre}</p></a>')
        print('OK', sigla)
    (ROOT / 'guias-finales.html').write_text(INDEX.format(cssv=CSSV, cards='\n'.join(cards)), encoding='utf-8')
    print('OK guias-finales.html')


if __name__ == '__main__':
    main()
