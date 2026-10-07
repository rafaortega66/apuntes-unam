#!/usr/bin/env python3
"""Genera tareas/<id>.html: una página por asignación de assets/pendientes.json.

Los datos base salen de pendientes.json (titulo, vence, detalle, link, classroom).
Las instrucciones detalladas (pasos, citas textuales de NotebookLM, texto oficial
del PDF, lo que falta) viven en assets/tareas-detalle.json, con la misma clave (id).
Si una asignación no tiene detalle todavía, la página lo dice y muestra lo que hay.

Uso: python3 scripts/build_tareas.py
"""
import json
import os
import html
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'tareas')
SIN_PAGINA = {'oac-c8-audio'}  # pendientes que no son tareas (se quedan con su enlace original)

DIAS = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']


def cuando(it):
    v = it.get('vence')
    if not v:
        return it.get('fecha_texto') or 'Sin fecha límite confirmada'
    d = datetime.fromisoformat(v)
    s = '%s %d %s %d, %02d:%02d' % (DIAS[d.weekday()], d.day, MESES[d.month - 1], d.year, d.hour, d.minute)
    if it.get('hora_confirmada') is False:
        s += ' (fin del día; la hora no está confirmada)'
    return s


def e(t):
    return html.escape(str(t), quote=False)


def seccion(sid, titulo, cuerpo, abierta=True):
    return ('<details class="section-block sec" id="%s"%s><summary><span class="stitle">%s</span></summary>\n%s\n</details>\n'
            % (sid, ' open' if abierta else '', titulo, cuerpo))


def pagina(it, det):
    color = it.get('color', '#7C9CD6')
    partes = []
    if det.get('resumen'):
        partes.append('<p class="tarea-resumen">%s</p>' % det['resumen'])
    elif it.get('detalle'):
        partes.append('<p class="tarea-resumen">%s</p>' % e(it['detalle']))

    if not det:
        partes.append('<div class="section-block nota" style="border-left:3px solid %s"><p style="margin:0">'
                      '<strong>Instrucciones completas:</strong> todavía no se extraen del notebook para esta asignación. '
                      'Pídele a Claude «extrae las instrucciones de %s del notebook» y esta página se actualiza.</p></div>'
                      % (color, e(it['titulo'])))

    cuerpo = ''
    pr = det.get('progreso')
    if pr:
        hechos = sum(1 for x in pr['pasos'] if x['hecho'])
        lista = ''.join('<li class="%s">%s %s</li>' % ('hecho' if x['hecho'] else 'falta', '✅' if x['hecho'] else '⬜', x['t']) for x in pr['pasos'])
        cuerpo += seccion('donde-nos-quedamos', '📍 Dónde nos quedamos (%d de %d pasos)' % (hechos, len(pr['pasos'])),
                          '<p>%s</p><ul class="tarea-progreso">%s</ul><p class="tarea-fuente">Actualizado: %s</p>' % (pr['donde'], lista, e(pr['actualizado'])))
    if det.get('pasos'):
        cuerpo += seccion('que-hacer', '✅ Qué tienes que hacer',
                          '<ol class="tarea-pasos">%s</ol>' % ''.join('<li>%s</li>' % p for p in det['pasos']))
    if det.get('entrega'):
        cuerpo += seccion('entrega', '📤 Cómo y cuándo se entrega', '<p>%s</p>' % det['entrega'])
    if det.get('texto_oficial'):
        cuerpo += seccion('texto-oficial', '📄 Enunciado oficial (texto exacto)', det['texto_oficial'])
    if det.get('citas'):
        li = ''.join('<li><span class="tarea-audio">%s</span><blockquote>«%s»</blockquote>'
                     '<span class="evid">→ %s</span></li>' % (e(c['audio']), e(c['cita']), c['implica'])
                     for c in det['citas'])
        cuerpo += seccion('citas', '🎧 Lo que dijo el profesor (citas textuales del audio)',
                          '<ul class="tarea-citas">%s</ul>' % li)
    if det.get('faltante'):
        cuerpo += seccion('faltante', '⚠️ Lo que NO está dicho / por confirmar',
                          '<ul>%s</ul>' % ''.join('<li>%s</li>' % f for f in det['faltante']))

    enlaces = list(det.get('enlaces', []))
    urls = {x['u'] for x in enlaces}
    if it.get('classroom') and it['classroom'].startswith('https://classroom.google.com/c/') and it['classroom'] not in urls:
        enlaces.append({'t': 'Abrir la tarea en Classroom', 'u': it['classroom']})
    if it.get('link'):
        u = '../' + it['link']
        if u not in urls:
            enlaces.append({'t': 'Ir a la sección de la materia donde se explica', 'u': u})
    if enlaces:
        cuerpo += seccion('enlaces', '🔗 Enlaces',
                          '<ul>%s</ul>' % ''.join('<li><a href="%s"%s>%s</a></li>' % (
                              e(x['u']), ' target="_blank" rel="noopener"' if x['u'].startswith('http') else '', e(x['t']))
                              for x in enlaces))
    partes.append(cuerpo)
    if det.get('fuente'):
        partes.append('<p class="tarea-fuente">Fuente: %s</p>' % e(det['fuente']))

    vence_attr = ' data-vence="%s"' % it['vence'] if it.get('vence') else ''
    return '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo_plano} — {materia}</title>
<link rel="stylesheet" href="../assets/style.css?v=20261007b">
<script src="../assets/app.js?v=20261007b" defer></script>
</head>
<body>
<div class="wrap">
<a class="back" href="../pendientes.html">← Pendientes</a>
<div class="detail-head" style="border-color:{color}"><h2>{titulo}</h2>
  <p class="prof"><strong style="color:{color}">{materia}</strong> · Vence: {cuando}<span class="tarea-faltan" id="tarea-faltan"{vence_attr}></span></p>
</div>
{cuerpo}
</div>
<script>
(function () {{
  var el = document.getElementById('tarea-faltan');
  if (!el || !el.dataset.vence) return;
  function tick() {{
    var d = new Date(el.dataset.vence).getTime() - Date.now();
    if (d <= 0) {{ el.textContent = ' · ya venció'; return; }}
    var m = Math.floor(d / 60000), h = Math.floor(m / 60);
    el.textContent = ' · ' + (h < 48 ? 'faltan ' + h + ' h ' + (m % 60) + ' min' : 'faltan ' + Math.floor(h / 24) + ' días');
  }}
  tick(); setInterval(tick, 30000);
}})();
</script>
</body>
</html>
'''.format(titulo_plano=e(it['titulo']), materia=e(it['materia']), color=color, titulo=e(it['titulo']),
           cuando=e(cuando(it)), vence_attr=vence_attr, cuerpo='\n'.join(partes))


def main():
    pend = json.load(open(os.path.join(ROOT, 'assets', 'pendientes.json'), encoding='utf-8'))
    det = json.load(open(os.path.join(ROOT, 'assets', 'tareas-detalle.json'), encoding='utf-8'))
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for it in pend['items']:
        if it['id'] in SIN_PAGINA:
            continue
        with open(os.path.join(OUT, it['id'] + '.html'), 'w', encoding='utf-8') as f:
            f.write(pagina(it, det.get(it['id'], {})))
        n += 1
    print('OK: %d páginas de asignación -> %s' % (n, OUT))


if __name__ == '__main__':
    main()
