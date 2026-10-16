#!/usr/bin/env python3
"""Genera noveno/INDICE.md: cada entrega (carpeta X-NN) con sus archivos y su carpeta -ad.

Uso: python3 scripts/indice_noveno.py
"""
import os

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'noveno')
NOMBRES = {'ACS': 'Arquitectura Cliente-Servidor', 'ASI': 'Administración de Servicios de Internet',
           'FSE': 'Fundamentos de Sistemas Embebidos (+ Lab)', 'MD': 'Minería de Datos',
           'OAC': 'Organización y Arquitectura de Computadoras (+ Lab L+)', 'RP': 'Reconocimiento de Patrones',
           'SIB': 'Seguridad Informática Básica', 'docs': 'Documentos académicos'}


def archivos(d):
    out = []
    for dp, _, fs in os.walk(d):
        for f in sorted(fs):
            if f != '.gitkeep':
                out.append(os.path.relpath(os.path.join(dp, f), d))
    return sorted(out)


def enlace(ruta):
    return ruta.replace(' ', '%20')


lineas = ['# Índice de noveno/', '',
          'Generado por `scripts/indice_noveno.py`. Una fila por entrega; **Entregado** = contenido de la carpeta',
          '`X-NN`, **Adicionales** = número de archivos en `X-NN-ad`.', '']
for sigla in sorted(os.listdir(RAIZ)):
    ds = os.path.join(RAIZ, sigla)
    if not os.path.isdir(ds):
        continue
    lineas += [f'## {sigla} — {NOMBRES.get(sigla, "")}', '']
    if sigla == 'docs':
        lineas += [f'- [{f}]({enlace("docs/" + f)})' for f in archivos(ds)] + ['']
        continue
    for cat in sorted(os.listdir(ds)):
        dc = os.path.join(ds, cat)
        if not os.path.isdir(dc):
            continue
        hijos = sorted(h for h in os.listdir(dc) if os.path.isdir(os.path.join(dc, h)))
        entregas = [h for h in hijos if not h.endswith('-ad')]
        sueltos = [f for f in os.listdir(dc) if os.path.isfile(os.path.join(dc, f)) and f != '.gitkeep']
        solo_ad = [h for h in hijos if h.endswith('-ad') and h[:-3] not in entregas]
        lineas.append(f'### {cat}')
        if not (entregas or sueltos or solo_ad):
            lineas += ['', '_(vacío)_', '']
            continue
        if entregas or solo_ad:
            lineas += ['', '| Entrega | Entregado | Adicionales |', '|---|---|---|']
            for e in entregas:
                fs = archivos(os.path.join(dc, e))
                ad = os.path.join(dc, e + '-ad')
                n_ad = len(archivos(ad)) if os.path.isdir(ad) else 0
                ent = '<br>'.join(f'[{f}]({enlace(f"{sigla}/{cat}/{e}/{f}")})' for f in fs) or '—'
                lineas.append(f'| {e} | {ent} | {n_ad or "—"} |')
            for a in solo_ad:
                lineas.append(f'| {a[:-3]} | _sin entrega (solo material)_ | {len(archivos(os.path.join(dc, a)))} |')
        if sueltos:
            lineas += ['', f'{len(sueltos)} archivos sueltos (material).']
        lineas.append('')

open(os.path.join(RAIZ, 'INDICE.md'), 'w').write('\n'.join(lineas) + '\n')
print('OK: noveno/INDICE.md')
