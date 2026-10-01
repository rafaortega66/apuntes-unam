#!/usr/bin/env python3
"""Imprime el prompt de NotebookLM para /migrar-clase (una línea; se mete con insertText, así que puede llevar acentos).
Uso: python3 scripts/prompt_migracion.py <clase-NN.html> <audio> "<materia con profesor>" "<dia fecha>" <N>"""
import os,sys,subprocess,unicodedata
page,src,materia,fecha,num=sys.argv[1:6]
secs=subprocess.run(['python3',os.path.join(os.path.dirname(os.path.abspath(__file__)),'migrar_formato_estudio.py'),'--secciones',page],capture_output=True,text=True).stdout.strip().splitlines()
def a(s): return s
p=(f'Usa SOLO la fuente {src} (clase de {materia}, {fecha}, Clase {num}). No inventes nada; todo debe salir de lo que se dijo en esa clase. '
 'Escribe con ortografia correcta en espanol (acentos, enes y signos de apertura). Responde EXACTAMENTE en este formato de texto plano, sin tablas, sin numeros de cita y sin texto antes ni despues. '
 'Primero una linea === EXAMEN y debajo de 3 a 6 lineas con el formato: - punto que probablemente viene en el examen || evidencia de la clase (lo dijo explicitamente, lo repitio, lo resolvio en vivo o lo ligo a una tarea; si la evidencia es debil dilo). '
 'Despues, para CADA id de la lista de abajo, una linea === SECCION seguida del id exacto, y debajo cuatro lineas: '
 'SIMPLE: como se lo explicarias a alguien sin la carrera, con una analogia cotidiana. '
 'ROMPE: donde deja de servir esa analogia. '
 'IMPORTA: por que importa o con que se conecta, segun lo dicho en clase. '
 'ERRORES: errores o confusiones que senalo el profesor o que se notaron en las respuestas de los alumnos; si no hubo, escribe NINGUNO. '
 'Al final una linea === PRUEBA y debajo 8 pares de lineas P: pregunta y R: respuesta, mezclando recordar, explicar con tus palabras, aplicar (un ejercicio como los de clase con otros datos) y comparar. '
 'Lista de secciones (id | tema): ' + ' ; '.join(a(s) for s in secs))
print(p)
