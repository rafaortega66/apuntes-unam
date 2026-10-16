#!/usr/bin/env python3
"""Genera decimo/INDICE.md: cada entrega (carpeta X-NN) con indicaciones, entregables y adicionales.

Uso: python3 scripts/indice_decimo.py
"""
import os
import re

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'decimo')
NOMBRES = {'ACS': 'Arquitectura Cliente-Servidor', 'ASI': 'Administración de Servicios de Internet',
           'FSE': 'Fundamentos de Sistemas Embebidos (+ Lab)', 'MD': 'Minería de Datos',
           'OAC': 'Organización y Arquitectura de Computadoras (+ Lab L+)', 'RP': 'Reconocimiento de Patrones',
           'SIB': 'Seguridad Informática Básica', 'docs': 'Documentos académicos'}
ENTREGA = re.compile(r'^(ACS|ASI|FSE|MD|OAC|RP|SIB)-(T|P|Proy|E|Exp|EC|R)(\d[\d-]*|Final)$')


def archivos(d):
    out = []
    for dp, _, fs in os.walk(d):
        for f in fs:
            if f != '.gitkeep':
                out.append(os.path.relpath(os.path.join(dp, f), d))
    return sorted(out)


def enlace(texto, ruta):
    return f'[{texto}]({ruta.replace(" ", "%20")})'


lineas = ['# Índice de decimo/', '',
          'Generado por `scripts/indice_decimo.py`. Una fila por entrega: indicaciones, lo **entregado** y cuántos',
          'archivos hay en `-adicionales`. Material independiente del profesor: carpetas `*-Material`.', '']
for sigla in sorted(os.listdir(RAIZ)):
    ds = os.path.join(RAIZ, sigla)
    if not os.path.isdir(ds):
        continue
    lineas += [f'## {sigla} — {NOMBRES.get(sigla, "")}', '']
    if sigla == 'docs':
        lineas += ['- ' + enlace(f, 'docs/' + f) for f in archivos(ds)] + ['']
        continue
    entregas, materiales = [], []
    for dp, dns, _ in os.walk(ds):
        dns.sort()
        for d in dns:
            ruta = os.path.relpath(os.path.join(dp, d), RAIZ)
            if d.endswith('-Material'):
                materiales.append(ruta)
            elif ENTREGA.match(d) and 'Material' not in dp:
                entregas.append(ruta)
    for m in materiales:
        lineas.append(f'- **{os.path.basename(m)}**: {len(archivos(os.path.join(RAIZ, m)))} archivos ({m}/)')
    if materiales:
        lineas.append('')
    actual = None
    for e in entregas:
        cat = os.path.dirname(e)
        if cat != actual:
            actual = cat
            lineas += ['', f'### {os.path.basename(cat)}', '', '| Entrega | Indicaciones | Entregado | Adicionales |', '|---|---|---|---|']
        code = os.path.basename(e)
        de = os.path.join(RAIZ, e)
        ind = [f for f in os.listdir(de) if f.startswith(code + '-indicaciones')]
        ind_txt = '<br>'.join(enlace(f, f'{e}/{f}') for f in sorted(ind)) or '—'
        ent = archivos(os.path.join(de, code + '-entregables'))
        ent_txt = '<br>'.join(enlace(f, f'{e}/{code}-entregables/{f}') for f in ent) or '_(sin entrega aún)_'
        n_ad = len(archivos(os.path.join(de, code + '-adicionales')))
        lineas.append(f'| {code} | {ind_txt} | {ent_txt} | {n_ad or "—"} |')
    lineas.append('')

open(os.path.join(RAIZ, 'INDICE.md'), 'w').write('\n'.join(lineas) + '\n')
print('OK: decimo/INDICE.md')
