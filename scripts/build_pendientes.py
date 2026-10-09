#!/usr/bin/env python3
import json
from datetime import datetime
import re

# Mapeo de siglas a colores
COLORES = {
    "ASI": "#7C9CD6",
    "ACS": "#E8735C",
    "FSE": "#A98BD1",
    "Lab FSE": "#E8735C",
    "Lab OAC": "#7C9CD6",
    "MD": "#A98BD1",
    "OAC": "#45B8A8",
    "RP": "#45B8A8",
    "SIB": "#E8735C",
}

with open('assets/pendientes-actualizados.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

items = []
for task in data.get('pendientes', []):
    sigla = task.get('sigla', '')
    color = COLORES.get(sigla, '#7C9CD6')

    # Convertir fecha a ISO con hora 23:59 (fin del día)
    fecha_str = task.get('fechaEntrega', '')
    hora = task.get('hora')
    if fecha_str:
        vence = fecha_str + 'T' + (hora or '23:59') + ':00-06:00'
    else:
        vence = None

    item = {
        'materia': task.get('materia', ''),
        'sigla': sigla,
        'color': color,
        'titulo': task.get('tarea', ''),
        'detalle': task.get('descripcion', ''),
        'vence': vence,
        'hora_confirmada': bool(hora),
    }
    for k in ('tipo', 'link'):
        if task.get(k):
            item[k] = task[k]
    items.append(item)

output = {
    'items': items,
    'actualizado': datetime.now().strftime('%Y-%m-%d %H:%M (hora de servidor)'),
    'nota': 'Generado por build_pendientes.py desde pendientes-actualizados.json'
}

with open('assets/pendientes.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'✅ pendientes.json generado con {len(items)} tareas')
