#!/usr/bin/env python3
"""Genera las páginas de entregas de cada materia a partir de decimo/.

Por materia teórica: tareas.html, practicas.html, proyectos.html, examenes.html y entregas.html (resumen).
Por laboratorio: entregas.html (sus prácticas). Cada entrega muestra sus indicaciones (el .md se
muestra en la página; el .pdf se enlaza), lo entregado, los adicionales y su estado en Classroom.

Uso: python3 scripts/build_entregas.py   (correr después de agregar o mover archivos en decimo/)
"""
import html
import os
import re
from urllib.parse import quote

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
DEC = os.path.join(RAIZ, 'decimo')
V = '20261020a'  # cache-busting de assets, igual que el resto del sitio

MATERIAS = {  # slug: (sigla, nombre, color)
    'administracion-de-servicios-de-internet': ('ASI', 'Administración de Servicios de Internet', '#7C9CD6'),
    'arquitectura-cliente-servidor': ('ACS', 'Arquitectura Cliente-Servidor', '#E8735C'),
    'fundamentos-de-sistemas-embebidos': ('FSE', 'Fundamentos de Sistemas Embebidos', '#A98BD1'),
    'mineria-de-datos': ('MD', 'Minería de Datos', '#A98BD1'),
    'organizacion-y-arquitectura-de-computadoras': ('OAC', 'Organización y Arquitectura de Computadoras', '#45B8A8'),
    'reconocimiento-de-patrones': ('RP', 'Reconocimiento de Patrones', '#45B8A8'),
    'seguridad-informatica-basica': ('SIB', 'Seguridad Informática Básica', '#E8735C'),
}
LABS = {
    'lab-de-fundamentos-de-sistemas-embebidos': ('FSE', 'FSE-Lab', 'Lab. de Fundamentos de Sistemas Embebidos', '#E8735C'),
    'lab-de-organizacion-y-arquitectura-de-computadoras': ('OAC', 'OAC-Lab', 'Lab. de Organización y Arquitectura de Computadoras', '#7C9CD6'),
}

TITULOS = {
    'ACS-T01': 'Tarea 1 — Investigar procesos', 'ACS-T02': 'Tarea 2 — Permisos, fdisk y setuid',
    'ACS-T03': 'Tarea 3 — fork, exec y execve', 'ACS-T04': 'Tarea 4 — ejemplo_listen.c (cola de listen)',
    'ASI-P01': 'Práctica 1 — Entorno (uso básico de Linux)', 'ASI-P02': 'Práctica 2 — Servicio en la nube',
    'ASI-P03': 'Práctica 3 — Servidor DHCP', 'ASI-P04': 'Práctica 4 — Kali Linux',
    'ASI-T01': 'Tarea — Análisis de ENOE y ENIGH', 'ASI-R01': 'Reposición',
    'ASI-Sprint0': 'Preparación — «Formato 1» y «Diagramas UML»', 'ASI-Sprint1': 'DHCP y DNS — «Reporte de SCRUM 1»',
    'ASI-Sprint2': 'Apache — «Reporte Scrum» y «Reporte de la semana de scrum»',
    'ASI-Sprint3': 'Samba, SSH y permisos — «Reporte»',
    'FSE-T01': 'Tarea 01 — Plagio', 'FSE-T02': 'Tarea 02 — Código limpio', 'FSE-T03': 'Tarea 03 — Nombres con sentido',
    'FSE-T04': 'Tarea 04 — Funciones limpias', 'FSE-T05': 'Tarea 05 — Comentarios', 'FSE-T06': 'Tarea 06 — Formato',
    'FSE-T07': 'Tarea 07 — Límites claros', 'FSE-T08': 'Tarea 08 — Cuando algo huele raro (Clean Code, cap. 17)', 'FSE-T09': 'Tarea 09',
    'FSE-P01': 'Práctica 1 — Raspbian en Raspberry Pi', 'FSE-P02': 'Práctica 2 — LineageOS en Raspberry Pi',
    'FSE-P03': 'Práctica 3', 'FSE-P04': 'Práctica 4 — Control remoto por WiFi y servidor web', 'FSE-P05': 'Práctica 5',
    'FSE-P06': 'Práctica 6 — I²C con Raspberry Pi Pico', 'FSE-P07': 'Práctica 7', 'FSE-P08': 'Práctica 8',
    'FSE-ProyFinal': 'Proyecto final del laboratorio', 'FSE-E01': 'Primer examen parcial (Unidades 1 y 2)',
    'MD-P03-1': 'Práctica 3.1 — Agrupación', 'MD-P03-2': 'Práctica 3.2 — Asociación',
    'MD-P03-3': 'Práctica 3.3 — Regresión', 'MD-P03-4': 'Práctica 3.4 — Clasificación (Diabetes demo)',
    'RP-T02': 'Tarea 2', 'OAC-P05': 'Práctica 5 — Previo 1',
    'MD-Proy01': 'Proyecto 1 — KDD', 'MD-Proy02': 'Proyecto 2 — Arquitectura de minería de datos (Azure)',
    'MD-E01': 'Examen 1',
    'OAC-T01': 'Trabajo 1 — Raíz cuadrada en ensamblador', 'OAC-T02': 'Trabajo 2 — Producto punto',
    'OAC-Proy01': 'Proyecto 1 — Seno y coseno por series de Taylor', 'OAC-Proy02': 'Proyecto 2 — Filtro digital IIR',
    'OAC-P01': 'Práctica 1', 'OAC-P02': 'Práctica 2', 'OAC-P03': 'Práctica 3 — Cartas ASM',
    'OAC-P04': 'Práctica 4 — Máquinas de estados con memorias',
    'RP-T01': 'Tarea 1 — Momentos de Hu, GLCM y LBP', 'RP-P00': 'Práctica 0 — Manejo básico de librerías',
    'RP-P01': 'Práctica 1 — Análisis de componentes principales', 'RP-P02': 'Práctica 2 — Algoritmos de clustering',
    'RP-P03': 'Práctica 3 — Clasificadores bayesianos', 'RP-E01': 'Primer Examen Parcial (en papel, 28 sep)',
    'SIB-T01': 'Tarea 1 — Perfiles de protección (Equipo 4)', 'SIB-T02': 'Tarea 2 — Línea del tiempo (Equipo 4)',
    'SIB-T03': 'Tarea 3 — Tipos de atacantes (Equipo 4)', 'SIB-Exp01': 'Exposición — Normatividad (Equipo 4)',
    'SIB-EC01': 'Ejercicio en clase — Video (curso de colisión)',
    'SIB-EC02': 'Ejercicio en clase — Amenaza o vulnerabilidad, 20 reactivos (Clase 08)',
    'SIB-EC03': 'Ejercicio en clase — Caso «SaludIntegral»: etapas de un ataque (Clase 12)',
    'SIB-EC04': 'Ejercicio en clase — Clasificar mecanismos de seguridad, en parejas (Clase 14)',
    'SIB-EC05': 'Ejercicio en clase — Cuestionario de normatividad (Clase 04)',
    'SIB-EC06': 'Ejercicio en clase — Amenazas a la persona y a la casa (Clase 07)',
    'SIB-EC07': 'Ejercicio de clase — Investigación de ataques (Equipo 4; 20 oct, sin clase)',
    'ACS-E01': 'Examen parcial — cliente-servidor TCP (de casa)',
}
# Estado verificado en Google Classroom el 15 oct 2026 (las materias sin Classroom se marcan aparte).
ESTADO = {
    'RP-T01': 'Entregada · 100/100', 'RP-P01': 'Entregada · 80/100', 'RP-P02': 'Entregada · 95/100', 'RP-P03': 'Entregada',
    'RP-E01': 'Presentado en papel · 20/100 (Classroom solo registra la parte entera)',
    'RP-P00': 'Sin entrega (práctica de preparación)',
    'FSE-T01': 'Entregada tarde', 'FSE-T02': 'Entregada · 100/100', 'FSE-T03': 'Entregada · 100/100', 'FSE-T04': 'Entregada · 100/100',
    'FSE-T05': 'Entregada', 'FSE-T06': 'Entregada', 'FSE-T07': 'Entregada tarde', 'FSE-T08': 'Entregada (21 oct 2026, antes de las 23:59)',
    'FSE-P01': 'Entregada · 90/100', 'FSE-P02': 'Entregada · 60/100', 'FSE-P03': 'Entregada · 100/100', 'FSE-P04': 'Entregada',
    'FSE-P05': 'Entregada', 'FSE-P06': 'Entregada tarde',
    'OAC-P01': 'Entregada', 'OAC-P02': 'Entregada', 'OAC-P03': 'Entregada',
    'MD-P03-1': 'Entregada', 'MD-P03-2': 'Entregada', 'MD-Proy01': 'Entregada tarde', 'MD-Proy02': 'Entregada tarde', 'MD-E01': 'Entregada',
    'ASI-P01': 'Entregada tarde', 'ASI-P02': 'Entregada', 'ASI-P03': 'Entregada', 'ASI-P04': 'Entregada', 'ASI-T01': 'Entregada',
    'ASI-R01': 'Entregada',
    'ASI-Sprint0': 'Entregadas (20 y 21 sep)', 'ASI-Sprint1': 'Entregada (28 sep)', 'ASI-Sprint2': 'Entregadas (5 y 13 oct)',
    'ASI-Sprint3': 'Entregada (19 oct)',
    'ACS-E01': 'Entregada por correo (18 oct 2026, 18:34)',
    'FSE-E01': 'Presentado en papel (14 oct 2026) · 101 (36 + 65, incluye punto extra)',
    'SIB-EC02': 'Resuelto en mis apuntes · sin confirmar si se entregó',
    'MD-P03-3': 'Entregada (Classroom; la subió una compañera del Equipo 7)',
    'MD-P03-4': 'Pendiente · vence jueves 22 oct, 13:00', 'RP-T02': 'Pendiente · vence viernes 23 oct, 07:00',
    'OAC-P04': 'Reporte pendiente · vence viernes 23 oct, 23:59', 'OAC-P05': 'Entregada (20 oct 2026, antes de las 23:59)',
    'OAC-T01': 'Entregada por correo al profesor (21 oct 2026, Entrega_OAC_OrtegaDeLaPaz.zip)',
    'OAC-T02': 'Entregada por correo al profesor (21 oct 2026, Entrega_OAC_OrtegaDeLaPaz.zip)',
    'OAC-Proy01': 'Entregada por correo al profesor (21 oct 2026, Entrega_OAC_OrtegaDeLaPaz.zip)',
    'OAC-Proy02': 'Entregada por correo al profesor (21 oct 2026, Entrega_OAC_OrtegaDeLaPaz.zip)',
    'SIB-EC03': 'Ejercicio de clase · sin confirmar si se entregó',
    'SIB-EC04': 'Ejercicio de clase · sin confirmar si se entregó',
    'SIB-EC05': 'Calificado en clase · 3 aciertos',
    'SIB-EC06': 'Entregada en clase (en papel)',
    'SIB-EC07': 'Entregada (20 oct 2026, antes de las 11:15) · me tocaron los puntos 10 y 11',
}
SIN_CLASSROOM = {'ACS': 'Entregada (por correo; ACS no usa Classroom)', 'SIB': 'Entregada (por correo, en equipo)',
                 'OAC': 'Entregada (OAC teoría no usa Classroom)'}
NOTAS = {  # avisos que no tienen carpeta propia
    ('FSE', 'tareas'): 'También se registró en Classroom «Ejemplos de sistemas embebidos» (completada, sin archivo).',
}

ENTREGA = re.compile(r'^(ACS|ASI|FSE|MD|OAC|RP|SIB)-(T|P|Proy|E|Exp|EC|R|Sprint)(\d[\d-]*|Final)$')
PAGINAS = [('tareas', 'Tareas', ('T', 'R', 'EC')), ('practicas', 'Prácticas', ('P',)),
           ('proyectos', 'Proyectos', ('Proy', 'Exp', 'Sprint')), ('examenes', 'Exámenes', ('E',))]


def sprints_de(sigla):
    """[(nombre, ruta)] de las carpetas decimo/<SIGLA>/<SIGLA>-Proyecto/<SIGLA>-SprintN, en orden."""
    base = os.path.join(DEC, sigla, f'{sigla}-Proyecto')
    if not os.path.isdir(base):
        return []
    ds = [d for d in os.listdir(base) if re.match(rf'^{sigla}-Sprint\d+$', d)]
    ds.sort(key=lambda d: int(d.rsplit('Sprint', 1)[1]))
    return [(d, os.path.join(base, d)) for d in ds]


def tipo(code):
    return ENTREGA.match(code).group(2)


def entregas(sigla, solo_lab=None):
    """[(ruta_relativa_a_decimo, code)] de una materia, en orden."""
    out = []
    base = os.path.join(DEC, sigla)
    for dp, dns, _ in os.walk(base):
        dns.sort()
        for d in dns:
            if ENTREGA.match(d) and 'Material' not in dp:
                rel = os.path.relpath(os.path.join(dp, d), DEC)
                es_lab = '-Lab/' in rel + '/'
                if solo_lab is None or solo_lab == es_lab:
                    out.append((rel, d))
    return out


def archivos(d):
    out = []
    if os.path.isdir(d):
        for dp, dns, fs in os.walk(d):
            dns.sort()
            for f in sorted(fs):
                if f != '.gitkeep':
                    out.append(os.path.relpath(os.path.join(dp, f), d))
    return out


def url(rel):
    return '../../decimo/' + quote(rel)


def md_html(texto):
    """Markdown mínimo (títulos, listas, citas, negritas, código, enlaces) para los -indicaciones.md."""
    def inline(s):
        s = html.escape(s)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'«([^»]+)»', r'«\1»', s)
        return re.sub(r'(https?://[^\s<)]+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', s)
    out, lista, tabla = [], None, False
    for linea in texto.splitlines():
        if linea.startswith('# '):
            continue  # el título ya está en la tarjeta
        if linea.strip().startswith('|'):  # tabla: | a | b | (la fila |---| se salta)
            celdas = [c.strip() for c in linea.strip().strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?', c) for c in celdas):
                continue
            if not tabla:
                out.append('<table>'); tabla = True
            out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in celdas) + '</tr>')
            continue
        if tabla:
            out.append('</table>'); tabla = False
        m = re.match(r'^\s*(?:[-*]|\d+\.)\s+(.*)', linea)
        if m:
            tag = 'ol' if re.match(r'^\s*\d+\.', linea) else 'ul'
            if lista != tag:
                if lista:
                    out.append(f'</{lista}>')
                out.append(f'<{tag}>'); lista = tag
            out.append(f'<li>{inline(m.group(1))}</li>')
            continue
        if lista:
            out.append(f'</{lista}>'); lista = None
        if linea.startswith('> '):
            out.append(f'<blockquote>{inline(linea[2:])}</blockquote>')
        elif linea.strip():
            out.append(f'<p>{inline(linea.strip())}</p>')
    if lista:
        out.append(f'</{lista}>')
    if tabla:
        out.append('</table>')
    return '\n'.join(out)


# Entregas cuyos archivos que no son PDF llevan, junto al enlace normal, un botón «⬇ descargar» (atributo download).
# Pedido del usuario el 20 oct 2026, empezando por estas; agregar aquí las demás.
DESCARGA = {'MD-P03-1', 'MD-P03-2', 'MD-P03-3'}


def link(rel, f, descargar=False):
    a = f'<a href="{url(rel)}" target="_blank">{html.escape(f)}</a>'
    if descargar and not f.lower().endswith('.pdf'):
        a += f' <a class="btn-descarga" href="{url(rel)}" download="{html.escape(os.path.basename(f))}">⬇ descargar</a>'
    return a


def lista_links(base_rel, fs, descargar=False):
    return ' · '.join(link(base_rel + "/" + f, f, descargar) for f in fs)


def tarjeta(rel, code, sigla, leeme=None):
    d = os.path.join(DEC, rel)
    titulo = TITULOS.get(code, code)
    estado = ESTADO.get(code) or SIN_CLASSROOM.get(sigla) or ''
    ent = archivos(os.path.join(d, code + '-entregables'))
    if not ent and code not in ESTADO:
        estado = 'Pendiente / sin entrega todavía'
    ad = archivos(os.path.join(d, code + '-adicionales'))
    ind = sorted(f for f in os.listdir(d) if f.startswith(code + '-indicaciones'))
    h = [f'<div class="section-block entrega" id="{code}">',
         f'<h4>{code} · {html.escape(titulo)}</h4>']
    if estado:
        h.append(f'<p class="estado">{html.escape(estado)}</p>')
    if leeme:  # README.md del sprint (ASI): qué historias cubre
        h.append('<div class="indicaciones">' + md_html(open(leeme, encoding='utf-8').read()) + '</div>')
    h.append('<h5>Indicaciones</h5>')
    for f in ind:
        if f.endswith('.md'):
            h.append('<div class="indicaciones">' + md_html(open(os.path.join(d, f), encoding='utf-8').read()) + '</div>')
        else:
            h.append(f'<p><a href="{url(rel + "/" + f)}" target="_blank">{html.escape(f)}</a> (enunciado del profesor)</p>')
    if not ind:
        h.append('<p>—</p>')
    h.append('<h5>Entregado</h5>')
    h.append(f'<p>{lista_links(rel + "/" + code + "-entregables", ent, code in DESCARGA)}</p>' if ent else '<p>— (sin archivo entregado)</p>')
    if ad:
        h.append(f'<details><summary>Adicionales ({len(ad)})</summary><p>{lista_links(rel + "/" + code + "-adicionales", ad, code in DESCARGA)}</p></details>')
    h.append('</div>')
    return '\n'.join(h)


ESTILO = """<style>
.entrega h5{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-soft);margin:14px 0 4px}
.entrega .estado{display:inline-block;font-size:12.5px;padding:2px 10px;border-radius:99px;border:1px solid var(--c);color:var(--c);margin:2px 0 4px}
.entrega .indicaciones p,.entrega .indicaciones li{font-size:14px;line-height:1.6;white-space:normal}
.entrega .indicaciones blockquote{margin:6px 0;padding:4px 12px;border-left:3px solid var(--c);color:var(--ink-soft)}
.entrega a{color:var(--indigo);word-break:break-word}
.entrega details{margin-top:10px}.entrega summary{cursor:pointer;font-size:13px;color:var(--ink-soft)}
.entrega details p{font-size:13px;line-height:1.7}
.indice-entregas{font-size:14px;line-height:1.9}
</style>"""


def pagina(titulo_pag, nombre, color, cuerpo, desc):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo_pag} — {nombre}</title>
<link rel="stylesheet" href="../../assets/style.css?v={V}">
<script src="../../assets/app.js?v={V}" defer></script>
{ESTILO}
</head>
<body style="--c:{color}">
<div class="wrap">
<a class="back" href="index.html">← {nombre}</a>
<div class="detail-head" style="border-color:{color}"><h2>{titulo_pag}</h2>
  <p class="prof">{desc}</p>
</div>
{cuerpo}
</div>
</body>
</html>
"""

AVISO = ('<!-- Generado por scripts/build_entregas.py desde decimo/. No editar a mano: '
         'agrega o mueve archivos en decimo/ y vuelve a correr el script. -->\n')
DESC = ('Generado desde <code>decimo/</code>. Cada entrega: indicaciones del profesor, lo que se entregó y '
        'los archivos adicionales. Estado verificado en Classroom el 15 oct 2026.')


def escribir(path, texto):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(AVISO + texto)


hechas = []
for slug, (sigla, nombre, color) in MATERIAS.items():
    todas = entregas(sigla, solo_lab=False)
    resumen = []
    for pag, titulo, tipos in PAGINAS:
        sel = [(r, c) for r, c in todas if tipo(c) in tipos]
        if pag == 'practicas' and not sel and not os.path.exists(os.path.join(RAIZ, 'materias', slug, 'practicas.html')):
            continue
        partes = []
        if (sigla, pag) in NOTAS:
            partes.append(f'<div class="section-block nota"><p>{NOTAS[(sigla, pag)]}</p></div>')
        if pag == 'practicas' and sigla in ('FSE', 'OAC'):
            lab = [s for s, v in LABS.items() if v[0] == sigla][0]
            partes.append(f'<div class="section-block nota"><p>Las prácticas de laboratorio están en <a href="../{lab}/entregas.html">la página del laboratorio</a>.</p></div>')
        sprints = sprints_de(sigla) if pag == 'proyectos' else []
        if sprints:
            # Proyecto por sprints (ASI): cada carpeta <SIGLA>-SprintN es UNA entrega (todo lo del sprint junto) + su README
            leeme_general = os.path.join(DEC, sigla, f'{sigla}-Proyecto', 'README.md')
            if os.path.exists(leeme_general):
                partes.append('<div class="section-block indicaciones">' + md_html(open(leeme_general, encoding='utf-8').read()) + '</div>')
            for nombre_sp, ruta_sp in sprints:
                leeme = os.path.join(ruta_sp, 'README.md')
                if ENTREGA.match(nombre_sp) and os.path.exists(os.path.join(ruta_sp, nombre_sp + '-entregables')):
                    partes.append(tarjeta(os.path.relpath(ruta_sp, DEC), nombre_sp, sigla, leeme if os.path.exists(leeme) else None))
                elif os.path.exists(leeme):  # sprint sin carpetas de entrega todavía
                    partes.append(f'<div class="section-block entrega" id="{nombre_sp}"><h4>{nombre_sp}</h4>'
                                  f'<div class="indicaciones">{md_html(open(leeme, encoding="utf-8").read())}</div></div>')
            partes += [tarjeta(r, c, sigla) for r, c in sel if '-Sprint' not in r]
        else:
            partes += [tarjeta(r, c, sigla) for r, c in sel]
        if not sel and not partes:
            partes.append(f'<p class="empty">No hay {titulo.lower()} registradas todavía en <code>decimo/{sigla}/</code>.</p>')
        escribir(os.path.join(RAIZ, 'materias', slug, pag + '.html'), pagina(titulo, nombre, color, '\n'.join(partes), DESC))
        hechas.append(f'{slug}/{pag}.html')
        resumen += [(c, pag) for _, c in sel]
    # entregas.html = índice de todo lo de la materia
    filas = ''.join(f'<li><a href="{p}.html#{c}">{c}</a> — {html.escape(TITULOS.get(c, c))}'
                    f' <span style="color:var(--ink-soft)">({html.escape(ESTADO.get(c) or SIN_CLASSROOM.get(sigla, ""))})</span></li>'
                    for c, p in resumen)
    cuerpo = f'<div class="section-block"><ul class="indice-entregas">{filas}</ul></div>'
    escribir(os.path.join(RAIZ, 'materias', slug, 'entregas.html'), pagina('Entregas', nombre, color, cuerpo, DESC))
    hechas.append(f'{slug}/entregas.html')

for slug, (sigla, cat, nombre, color) in LABS.items():
    sel = entregas(sigla, solo_lab=True)
    cuerpo = '\n'.join(tarjeta(r, c, sigla) for r, c in sel)
    escribir(os.path.join(RAIZ, 'materias', slug, 'entregas.html'), pagina('Entregas', nombre, color, cuerpo, DESC))
    hechas.append(f'{slug}/entregas.html')

print(f'OK: {len(hechas)} páginas generadas')
