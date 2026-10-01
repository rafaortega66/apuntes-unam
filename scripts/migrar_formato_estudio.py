#!/usr/bin/env python3
"""
Migra una página clase-NN.html al "formato de estudio" (ver CLAUDE.md) SIN
tocar la prosa que ya tiene: solo le agrega lo nuevo que sale de NotebookLM.

  1. <meta name="formato" content="estudio"> en el <head>
  2. Nota de formato + "🎯 Lo que probablemente viene en el examen" después del detail-head
  3. Dentro de cada <details class="section-block sec" id="..."> de contenido,
     al final: Explicado en simple (+ dónde falla la analogía), Por qué importa,
     Errores comunes
  4. "🧠 Ponte a prueba" justo antes de la sección de contexto (o pendiente)

Uso:
    python3 scripts/migrar_formato_estudio.py <clase-NN.html> <salida_notebooklm.txt>
    python3 scripts/migrar_formato_estudio.py --secciones <clase-NN.html>   # lista ids para el prompt

La salida de NotebookLM debe venir con este formato (es lo que pide el
prompt de /migrar-clase):

    === EXAMEN
    - <punto> || <evidencia>
    === SECCION <id-del-details>
    SIMPLE: <analogía>
    ROMPE: <dónde falla la analogía>
    IMPORTA: <por qué importa / con qué se conecta>
    ERRORES: <errores comunes, o NINGUNO>
    === PRUEBA
    P: <pregunta>
    R: <respuesta>
"""
import html
import re
import sys

SALTAR = ("-contexto", "-pendiente", "-examen", "-prueba")


def inline(s):
    """Markdown mínimo de NotebookLM → HTML (escapa primero)."""
    s = s.strip()
    s = re.sub(r"\\+([()\[\]$])", lambda m: "" if m.group(1) in "()[]" else "$", s)   # \( \) \[ \] \$ de LaTeX
    for a, b in (("\\rightarrow", "→"), ("\\times", "×"), ("\\approx", "≈"), ("\\cdot", "·"),
                 ("\\log_2", "log₂"), ("\\leq", "≤"), ("\\geq", "≥"), ("\\neq", "≠"), ("^2", "²")):
        s = s.replace(a, b)
    s = s.replace("\\", "")
    s = html.escape(s, quote=False)
    s = re.sub(r"\s*\[\d+(?:[,\-–]\s*\d+)*\]", "", s)          # citas [3], [3, 4]
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    return s


def secciones(src):
    return [(i, re.sub(r"<[^>]+>", "", t)) for i, t in
            re.findall(r'<details class="section-block sec" id="([^"]+)"[^>]*><summary><span class="stitle">(.*?)</span>', src)]


def parse(txt):
    txt = txt.replace("\r", "")
    out = {"examen": [], "sec": {}, "prueba": []}
    bloques = re.split(r"^\s*=+\s*", txt, flags=re.M)
    for b in bloques:
        b = b.strip()
        if not b:
            continue
        head, _, body = b.partition("\n")
        head = head.strip().strip("*").strip()
        if head.upper().startswith("EXAMEN"):
            for ln in body.splitlines():
                ln = ln.strip().lstrip("-*•0123456789.) ").strip()
                if not ln:
                    continue
                punto, _, ev = ln.partition("||")
                out["examen"].append((punto.strip(), ev.strip()))
        elif head.upper().startswith("SECCION"):
            partes = head.split(None, 1)
            if len(partes) == 1:                       # "=== SECCION" y el id en la línea siguiente
                head2, _, body = body.strip().partition("\n")
                partes.append(head2)
            sid = partes[1].strip().strip("`*")
            d = {}
            clave = None
            for ln in body.splitlines():
                m = re.match(r"\s*\**(SIMPLE|ROMPE|IMPORTA|ERRORES)\**\s*:\s*\**\s*(.*)", ln)
                if m:
                    clave = m.group(1)
                    d[clave] = m.group(2)
                elif clave and ln.strip():
                    d[clave] += " " + ln.strip()
            out["sec"][sid] = d
        elif head.upper().startswith("PRUEBA"):
            p = None
            for ln in body.splitlines():
                m = re.match(r"\s*\**([PR])\**\s*\d*\s*[:.]\s*\**\s*(.*)", ln)
                if m and m.group(1) == "P":
                    p = [m.group(2), ""]
                    out["prueba"].append(p)
                elif m and p is not None:
                    p[1] = m.group(2)
                elif p is not None and ln.strip():
                    p[1 if p[1] else 0] += " " + ln.strip()
    return out


def main():
    if sys.argv[1] == "--secciones":
        src = open(sys.argv[2], encoding="utf-8").read()
        for sid, t in secciones(src):
            if not sid.endswith(SALTAR):
                print(f"{sid} | {html.unescape(t)}")
        return
    path, nb = sys.argv[1], sys.argv[2]
    src = open(path, encoding="utf-8").read()
    if 'name="formato" content="estudio"' in src:
        sys.exit("Ya está en formato de estudio: " + path)
    data = parse(open(nb, encoding="utf-8").read())
    num = re.search(r"clase-(\d+)\.html", path).group(1)
    pre = "c" + str(int(num))
    color = re.search(r'class="detail-head" style="border-color:(#[0-9A-Fa-f]{6})', src).group(1)

    # 1. meta + versión de CSS con los estilos de estudio
    src = src.replace('<meta name="viewport"', '<meta name="formato" content="estudio">\n<meta name="viewport"', 1)
    src = re.sub(r"style\.css\?v=[0-9a-z]+", "style.css?v=20261001c", src)

    # 2. nota + examen después del detail-head
    items = "\n".join(
        f'<li><strong>{inline(p)}</strong>' + (f'<span class="evid">Evidencia: {inline(e)}</span>' if e else "") + "</li>"
        for p, e in data["examen"])
    bloque = (
        f'\n<div class="section-block nota" style="border-left:3px solid {color}"><p style="margin:0"><strong>Formato de estudio.</strong> '
        "Arriba, lo que probablemente viene en el examen y por qué. En cada tema, la explicación completa de la clase y, al final, "
        "el concepto explicado en simple, por qué importa y los errores comunes. Al final, preguntas para ponerte a prueba. "
        "Lo nuevo sale del audio de la clase procesado en NotebookLM.</p></div>\n\n"
        f'<details class="section-block sec" id="{pre}-examen" open><summary><span class="stitle">🎯 Lo que probablemente viene en el examen</span></summary>\n'
        f'<ol class="examen-lista">\n{items}\n</ol>\n</details>\n')
    m = re.search(r'<div class="detail-head".*?</div>\n', src, re.S)
    src = src[:m.end()] + bloque + src[m.end():]

    # 3. bloques por sección
    faltan = []
    for sid, _ in secciones(src):
        if sid.endswith(SALTAR):
            continue
        d = data["sec"].get(sid)
        if not d:
            faltan.append(sid)
            continue
        extra = ""
        if d.get("SIMPLE"):
            rompe = f'<span class="rompe">Dónde falla la analogía: {inline(d["ROMPE"])}</span>' if d.get("ROMPE") else ""
            extra += f'<span class="lbl">Explicado en simple</span>\n<div class="simple"><p>{inline(d["SIMPLE"])}{rompe}</p></div>\n'
        if d.get("IMPORTA"):
            extra += f'<span class="lbl">Por qué importa / con qué se conecta</span>\n<p>{inline(d["IMPORTA"])}</p>\n'
        if d.get("ERRORES") and not d["ERRORES"].strip().upper().startswith("NINGUNO"):
            extra += f'<div class="errores"><p><strong>Errores comunes:</strong> {inline(d["ERRORES"])}</p></div>\n'
        extra = f'<div class="estudio-extra">\n{extra}</div>\n' if extra else ""
        i = src.index(f'id="{sid}"')
        # cierre del <details> de esta sección (sin anidados de tipo sec)
        j = src.index("</details>", i)
        src = src[:j] + extra + src[j:]

    # 4. ponte a prueba
    qas = "\n".join(
        f'<details class="qa"><summary>{n}. {inline(p)}</summary><p>{inline(r)}</p></details>'
        for n, (p, r) in enumerate(data["prueba"], 1))
    prueba = (f'<details class="section-block sec" id="{pre}-prueba"><summary><span class="stitle">🧠 Ponte a prueba</span></summary>\n'
              "<p>Intenta contestar cada pregunta antes de abrirla. Recordar por tu cuenta es lo que fija la información; releer no la fija.</p>\n"
              f"{qas}\n</details>\n\n")
    m = re.search(r'<details class="section-block sec" id="[^"]*(contexto|pendiente)"', src)
    if m:
        k = m.start()
    elif '<div class="puntos-clave"' in src:
        k = src.index('<div class="puntos-clave"')
    else:                                   # páginas sin contexto/pendiente/puntos clave: antes de cerrar .wrap
        k = src.rindex("</div>\n</body>")
    src = src[:k] + prueba + src[k:]

    open(path, "w", encoding="utf-8").write(src)
    print(f"OK {path}: examen={len(data['examen'])} secciones={len(data['sec'])} prueba={len(data['prueba'])}")
    if faltan:
        print("  ⚠️ secciones sin bloque de NotebookLM:", ", ".join(faltan))


if __name__ == "__main__":
    main()
