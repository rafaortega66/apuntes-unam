"""
Generador del reporte final en PDF, formato IEEE de dos columnas.
Practica 1 - Analisis de Componentes Principales
Autor: Rafael Ortega de la Paz - No. de cuenta 420054085
"""
import os
from PIL import Image as PILImage

from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image,
    NextPageTemplate, PageBreak, Table, TableStyle, KeepTogether, FrameBreak
)
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from reportlab.lib import colors

OUTDIR = os.path.dirname(os.path.abspath(__file__))
OUTFILE = os.path.join(OUTDIR, "Practica1_Ortega_Rafael_420054085.pdf")

# ---------------------------------------------------------------------------
# Geometria de pagina (estilo IEEE, dos columnas)
# ---------------------------------------------------------------------------
PAGESIZE = letter
W, H = PAGESIZE
MARGIN = 0.62 * inch
USABLE_W = W - 2 * MARGIN
USABLE_H = H - 2 * MARGIN
COL_GAP = 0.28 * inch
COL_W = (USABLE_W - COL_GAP) / 2.0

TOP_H = 1.95 * inch  # espacio reservado para titulo/autor/resumen en pagina 1

frame_top = Frame(MARGIN, H - MARGIN - TOP_H, USABLE_W, TOP_H, id="top",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=6)
frame_l1 = Frame(MARGIN, MARGIN, COL_W, USABLE_H - TOP_H, id="l1",
                  leftPadding=0, rightPadding=6, topPadding=6, bottomPadding=0)
frame_r1 = Frame(MARGIN + COL_W + COL_GAP, MARGIN, COL_W, USABLE_H - TOP_H, id="r1",
                  leftPadding=6, rightPadding=0, topPadding=6, bottomPadding=0)

frame_l2 = Frame(MARGIN, MARGIN, COL_W, USABLE_H, id="l2",
                  leftPadding=0, rightPadding=6, topPadding=0, bottomPadding=0)
frame_r2 = Frame(MARGIN + COL_W + COL_GAP, MARGIN, COL_W, USABLE_H, id="r2",
                  leftPadding=6, rightPadding=0, topPadding=0, bottomPadding=0)

pt_first = PageTemplate(id="First", frames=[frame_top, frame_l1, frame_r1])
pt_later = PageTemplate(id="Later", frames=[frame_l2, frame_r2])


def _footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 7)
    canvas.drawCentredString(W / 2.0, MARGIN * 0.35, str(doc.page))
    canvas.restoreState()


pt_first.onPage = _footer
pt_later.onPage = _footer

doc = BaseDocTemplate(
    OUTFILE, pagesize=PAGESIZE,
    leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN,
    title="Practica 1 - Analisis de Componentes Principales",
    author="Rafael Ortega de la Paz",
)
doc.addPageTemplates([pt_first, pt_later])

# ---------------------------------------------------------------------------
# Estilos (tipografia estilo IEEE: Times, texto justificado, cuerpo pequeno)
# ---------------------------------------------------------------------------
S_TITLE = ParagraphStyle("S_TITLE", fontName="Times-Bold", fontSize=17, leading=20,
                          alignment=TA_CENTER, spaceAfter=6)
S_AUTHOR = ParagraphStyle("S_AUTHOR", fontName="Times-Roman", fontSize=10.5, leading=13,
                           alignment=TA_CENTER, spaceAfter=2)
S_AFFIL = ParagraphStyle("S_AFFIL", fontName="Times-Italic", fontSize=9, leading=11,
                          alignment=TA_CENTER, spaceAfter=8)
S_ABSTRACT = ParagraphStyle("S_ABSTRACT", fontName="Times-Roman", fontSize=8.7, leading=10.6,
                             alignment=TA_JUSTIFY, firstLineIndent=0)
S_H1 = ParagraphStyle("S_H1", fontName="Times-Bold", fontSize=10, leading=13,
                       spaceBefore=9, spaceAfter=5, alignment=TA_CENTER)
S_H2 = ParagraphStyle("S_H2", fontName="Times-BoldItalic", fontSize=9, leading=11.5,
                       spaceBefore=6, spaceAfter=3, alignment=TA_LEFT)
S_BODY = ParagraphStyle("S_BODY", fontName="Times-Roman", fontSize=9, leading=11.2,
                         alignment=TA_JUSTIFY, firstLineIndent=12, spaceAfter=4)
S_BODY_NOIND = ParagraphStyle("S_BODY_NOIND", parent=S_BODY, firstLineIndent=0)
S_CODE = ParagraphStyle("S_CODE", fontName="Courier", fontSize=6.6, leading=8.0,
                         alignment=TA_LEFT, spaceBefore=3, spaceAfter=5,
                         backColor=colors.Color(0.94, 0.94, 0.94),
                         borderPadding=4, leftIndent=2, rightIndent=2)
S_CAPTION = ParagraphStyle("S_CAPTION", fontName="Times-Roman", fontSize=7.8, leading=9.4,
                            alignment=TA_JUSTIFY, spaceBefore=3, spaceAfter=8)
S_TABLE_CELL = ParagraphStyle("S_TABLE_CELL", fontName="Times-Roman", fontSize=6.7, leading=8)
S_TABLE_HEAD = ParagraphStyle("S_TABLE_HEAD", fontName="Times-Bold", fontSize=6.7, leading=8,
                               textColor=colors.white)

_fig_counter = [0]


def code_block(text):
    escaped = (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    escaped = escaped.replace("\n", "<br/>").replace(" ", "&nbsp;")
    return Paragraph(escaped, S_CODE)


def p(text, style=S_BODY):
    return Paragraph(text, style)


def figure_incolumn(filename, caption_text):
    """Figura dentro de una sola columna (imagenes de aspecto moderado)."""
    _fig_counter[0] += 1
    n = _fig_counter[0]
    path = os.path.join(OUTDIR, filename)
    iw, ih = PILImage.open(path).size
    w = COL_W
    h = w * ih / iw
    img = Image(path, width=w, height=h)
    cap = Paragraph(f"<b>Fig. {n}.</b> {caption_text}", S_CAPTION)
    return KeepTogether([img, cap]), n


_template_counter = [0]
MIN_TEXT_H = 1.55 * inch  # espacio minimo reservado para texto a 2 columnas
MAX_TOP_FRAC = 0.80       # tope: la figura no puede ocupar mas del 80% de la pagina


def _make_flow_template(top_height):
    """Crea (y registra) una plantilla de pagina con una franja superior a
    ancho completo (para figuras) de altura top_height, seguida de dos
    columnas que ocupan el resto de la pagina. El texto que se agregue
    despues de la figura sigue fluyendo en esas columnas, en la MISMA
    pagina, evitando dejar espacio en blanco."""
    _template_counter[0] += 1
    tid = f"Flow{_template_counter[0]}"
    top = Frame(MARGIN, H - MARGIN - top_height, USABLE_W, top_height, id=f"{tid}_top",
                leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=6)
    rest_h = USABLE_H - top_height
    l = Frame(MARGIN, MARGIN, COL_W, rest_h, id=f"{tid}_l",
              leftPadding=0, rightPadding=6, topPadding=2, bottomPadding=0)
    r = Frame(MARGIN + COL_W + COL_GAP, MARGIN, COL_W, rest_h, id=f"{tid}_r",
              leftPadding=6, rightPadding=0, topPadding=2, bottomPadding=0)
    pt = PageTemplate(id=tid, frames=[top, l, r])
    pt.onPage = _footer
    doc.addPageTemplates([pt])
    return tid


def figure_block(story_list, items):
    """Coloca una o mas figuras apiladas en una franja a ancho completo en la
    parte superior de una pagina, y hace que el texto siguiente continue
    fluyendo en dos columnas justo debajo, en la MISMA pagina (sin paginas en
    blanco). Cada item es (filename, caption_text) o (filename, caption_text,
    width_frac) -- width_frac (fraccion de USABLE_W, por defecto 0.92) sirve
    para imagenes casi cuadradas que no deben ocupar todo el ancho. Regresa
    la lista de numeros de figura asignados."""
    nums = []
    flowables = []
    block_h = 0.0
    caption_overhead = 0.34 * inch  # pie de figura + espaciado, por item
    total_budget = min(USABLE_H - MIN_TEXT_H, USABLE_H * MAX_TOP_FRAC)
    per_item_cap = total_budget / len(items) - caption_overhead
    for item in items:
        filename, caption_text = item[0], item[1]
        width_frac = item[2] if len(item) > 2 else 0.92
        _fig_counter[0] += 1
        n = _fig_counter[0]
        nums.append(n)
        path = os.path.join(OUTDIR, filename)
        iw, ih = PILImage.open(path).size
        w = USABLE_W * width_frac
        h = w * ih / iw
        if h > per_item_cap:
            h = per_item_cap
            w = h * iw / ih
        img = Image(path, width=w, height=h)
        img.hAlign = "CENTER"
        cap = Paragraph(f"<b>Fig. {n}.</b> {caption_text}", S_CAPTION)
        flowables += [img, cap]
        block_h += h + caption_overhead

    top_height = min(block_h + 0.1 * inch, total_budget)
    tid = _make_flow_template(top_height)
    story_list.append(NextPageTemplate(tid))
    story_list.append(PageBreak())
    story_list.extend(flowables)
    story_list.append(NextPageTemplate("Later"))
    return nums


def tabla(headers, filas, col_widths):
    data = [[Paragraph(h, S_TABLE_HEAD) for h in headers]]
    for fila in filas:
        data.append([Paragraph(str(c), S_TABLE_CELL) for c in fila])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2b3a55")),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0f0f5")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t


story = []

# ===========================================================================
# TITULO, AUTOR, RESUMEN  (frame_top de la pagina 1)
# ===========================================================================
story.append(Paragraph("Practica 1: Analisis de Componentes Principales", S_TITLE))
story.append(Paragraph("Rafael Ortega de la Paz &mdash; No. de cuenta 420054085", S_AUTHOR))
story.append(Paragraph(
    "Facultad de Ingenieria, Universidad Nacional Autonoma de Mexico &mdash; "
    "Reconocimiento de Patrones", S_AFFIL))
story.append(Paragraph(
    "<b>Resumen&mdash;</b>Este reporte documenta la implementacion y aplicacion del "
    "analisis de componentes principales (PCA) sobre cuatro conjuntos de datos: un "
    "dataset sintetico bivariado, Iris, Wine y Olivetti Faces. Se implementaron desde "
    "cero dos rutas de calculo equivalentes &mdash;mediante la matriz de covarianza "
    "(<font face='Courier'>pca_cov</font>) y mediante descomposicion en valores "
    "singulares (<font face='Courier'>pca_svd</font>)&mdash; y se compararon contra "
    "la implementacion de scikit-learn, confirmando su equivalencia numerica. Se "
    "analizan criterios de seleccion del numero de componentes (varianza acumulada, "
    "regla del codo, criterio de Kaiser), el efecto de estandarizar los datos, y la "
    "relacion entre el numero de componentes retenidas y el error de reconstruccion, "
    "ilustrada con el caso de EigenFaces.",
    S_ABSTRACT))

story.append(NextPageTemplate("Later"))

# ===========================================================================
# SECCION I. DATASET SINTETICO (2.1)
# ===========================================================================
story.append(p("I. Dataset sint&eacute;tico de dos variables", S_H1))
story.append(p(
    "Se genero un conjunto sintetico de n=200 muestras bivariadas, con "
    "x<sub>1</sub>&nbsp;~&nbsp;N(0,1) y x<sub>2</sub>&nbsp;=&nbsp;2x<sub>1</sub>&nbsp;+&nbsp;"
    "N(0,1.25), de forma que ambas variables estan fuertemente correlacionadas por "
    "construccion. Los datos se centraron restando la media de cada columna y, sobre "
    "los datos centrados, se calculo la matriz de covarianza junto con sus valores y "
    "vectores propios mediante <font face='Courier'>numpy.linalg.eigh</font>, "
    "ordenando el resultado de mayor a menor varianza (PC1 = mayor varianza).", S_BODY))

story.append(code_block(
    "Xc = X - X.mean(axis=0)\n"
    "cov = np.cov(Xc, rowvar=False)\n"
    "eigvals, eigvecs = np.linalg.eigh(cov)\n"
    "orden = np.argsort(eigvals)[::-1]\n"
    "eigvals, eigvecs = eigvals[orden], eigvecs[:, orden]"))

story.append(p(
    "La media original fue [0.0709, -0.0182] y, tras centrar, se redujo a "
    "valores del orden de 10<super>-17</super> (numericamente cero). La matriz de "
    "covarianza resultante fue:", S_BODY))
story.append(code_block(
    "Cov = [[1.0485, 2.1886],\n"
    "       [2.1886, 5.9575]]"))
story.append(p(
    "Los valores propios obtenidos fueron &lambda;<sub>1</sub>=6.7915 y "
    "&lambda;<sub>2</sub>=0.2145, con vectores propios asociados "
    "v<sub>1</sub>=(0.3561, 0.9344) y v<sub>2</sub>=(-0.9344, 0.3561). La razon "
    "&lambda;<sub>1</sub>/&lambda;<sub>2</sub>&asymp;31.7 confirma que casi toda la "
    "varianza del conjunto se concentra en una sola direccion, consistente con el "
    "hecho de que x<sub>2</sub> se construyo como una funcion (casi) lineal de "
    "x<sub>1</sub>. El producto punto entre v<sub>1</sub> y v<sub>2</sub> fue de "
    "7.48&times;10<super>-18</super> y la matriz V<super>T</super>V resulto "
    "practicamente identidad, por lo que los vectores propios son ortogonales entre "
    "si, como garantiza la teoria para una matriz de covarianza (simetrica).", S_BODY))

fig1, n1 = figure_incolumn(
    "fig_2_1_datos_y_vectores_propios.png",
    "Datos sinteticos (n=200) y direcciones principales. Cada vector propio se "
    "grafico escalado por la raiz de su valor propio, partiendo de la media de los "
    "datos.")
story.append(fig1)
story.append(p(
    f"La Fig. {n1} muestra que PC1 se alinea con la direccion de maxima dispersion "
    "de la nube de puntos (la diagonal principal), mientras que PC2, perpendicular a "
    "PC1, apunta en la direccion de mucha menor varianza, coherente con los valores "
    "propios calculados.", S_BODY))

# ===========================================================================
# SECCION II. IRIS (2.2)
# ===========================================================================
story.append(p("II. Dataset Iris", S_H1))
story.append(p(
    "Sobre las 150 muestras y 4 caracteristicas (largo/ancho de sepalo y petalo) del "
    "dataset Iris se genero primero un <font face='Courier'>pairplot</font> con "
    "seaborn, coloreado por especie.", S_BODY))
(n2,) = figure_block(story, [(
    "fig_2_2_iris_pairplot.png",
    "Pairplot del dataset Iris, coloreado por especie (setosa, versicolor, "
    "virginica).")])
story.append(p(
    f"Como se observa en la Fig. {n2}, los pares que incluyen largo y ancho de "
    "petalo (petal length / petal width) son los que mejor separan las tres clases: "
    "setosa forma un grupo completamente aislado, mientras que versicolor y "
    "virginica, aunque cercanas, muestran una frontera razonablemente clara en esas "
    "dos variables. Los pares que usan unicamente medidas de sepalo separan mucho "
    "peor a versicolor de virginica.", S_BODY))

story.append(p(
    "Se implemento la funcion <font face='Courier'>pca_cov(X, k)</font>, que centra "
    "los datos, calcula la matriz de covarianza, obtiene sus valores/vectores propios "
    "y regresa los datos proyectados Z junto con los k vectores y valores propios de "
    "mayor varianza:", S_BODY))
story.append(code_block(
    "def pca_cov(X, k):\n"
    "    Xc = X - X.mean(axis=0)\n"
    "    cov = np.cov(Xc, rowvar=False)\n"
    "    eigvals, eigvecs = np.linalg.eigh(cov)\n"
    "    orden = np.argsort(eigvals)[::-1]\n"
    "    eigvals, eigvecs = eigvals[orden], eigvecs[:, orden]\n"
    "    eigvals_k, eigvecs_k = eigvals[:k], eigvecs[:, :k]\n"
    "    Z = Xc @ eigvecs_k\n"
    "    return Z, eigvecs_k, eigvals_k"))

story.append(p(
    "Aplicando <font face='Courier'>pca_cov</font> con k=4 se obtuvieron los valores "
    "propios &lambda;=(4.2282, 0.2427, 0.0782, 0.0238), con varianza explicada de "
    "92.46%, 5.31%, 1.71% y 0.52% respectivamente (acumulada: 92.46%, 97.77%, "
    "99.48%, 100%).", S_BODY))

(n3,) = figure_block(story, [(
    "fig_2_2_iris_scree_plot.png",
    "Scree plot (izquierda) y varianza explicada acumulada (derecha) para Iris, "
    "con lineas de referencia en 90% y 95%.")])

story.append(p(
    f"La Fig. {n3} muestra que la primera componente por si sola ya explica 92.46% "
    "de la varianza total, es decir, cae dentro del rango de 90%&ndash;95% "
    "solicitado; por lo tanto, con un solo vector propio (el asociado a "
    "&lambda;<sub>1</sub>=4.2282, con carga principal en petal length y petal "
    "width) bastaria para cumplir ese criterio. Si se buscara superar el 95%, "
    "se necesitarian 2 componentes (97.77% acumulado).", S_BODY))

fig4, n4 = figure_incolumn(
    "fig_2_2_iris_pca_2d.png",
    "Proyeccion de Iris sobre sus dos primeras componentes principales, coloreada "
    "por especie.")
story.append(fig4)
story.append(p(
    f"En la Fig. {n4}, al proyectar los datos sobre PC1-PC2, la especie setosa "
    "queda completamente separada del resto a lo largo de PC1, mientras que "
    "versicolor y virginica muestran un ligero traslape, en linea con lo observado "
    "en el pairplot original. Es importante notar que PCA no elimina ni crea "
    "caracteristicas fisicas: construye NUEVAS variables (PC1, PC2, ...) que son "
    "combinaciones lineales de las 4 caracteristicas originales, elegidas para "
    "maximizar la varianza capturada; la informacion de las variables originales no "
    "se descarta, se re-expresa de forma comprimida en menos dimensiones.", S_BODY))

# ===========================================================================
# SECCION III. WINE (2.3)
# ===========================================================================
story.append(p("III. Dataset Wine", S_H1))
story.append(p(
    "Se implemento la funcion <font face='Courier'>pca_svd(X, k)</font>, que "
    "entrega la misma informacion que <font face='Courier'>pca_cov</font> pero "
    "calculada mediante SVD de los datos centrados X<sub>c</sub>=USV<super>T</super>: "
    "los valores propios de la covarianza equivalen a S<super>2</super>/(n-1) y los "
    "vectores propios son las columnas de V.", S_BODY))
story.append(code_block(
    "def pca_svd(X, k):\n"
    "    Xc = X - X.mean(axis=0)\n"
    "    n = Xc.shape[0]\n"
    "    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)\n"
    "    eigvals = (S**2) / (n - 1)\n"
    "    eigvecs = Vt.T\n"
    "    eigvals_k, eigvecs_k = eigvals[:k], eigvecs[:, :k]\n"
    "    Z = Xc @ eigvecs_k\n"
    "    return Z, eigvecs_k, eigvals_k"))

story.append(p(
    "El dataset Wine (178 muestras, 13 caracteristicas fisico-quimicas) se "
    "estandarizo (media 0, desviacion estandar 1 por columna) y se aplico "
    "<font face='Courier'>pca_svd</font> con k=13.", S_BODY))

filas_wine = [
    (1, "4.7324", "36.20%", "36.20%"), (2, "2.5111", "19.21%", "55.41%"),
    (3, "1.4542", "11.12%", "66.53%"), (4, "0.9242", "7.07%", "73.60%"),
    (5, "0.8580", "6.56%", "80.16%"), (6, "0.6453", "4.94%", "85.10%"),
    (7, "0.5541", "4.24%", "89.34%"), (8, "0.3505", "2.68%", "92.02%"),
    (9, "0.2905", "2.22%", "94.24%"), (10, "0.2523", "1.93%", "96.17%"),
    (11, "0.2271", "1.74%", "97.91%"), (12, "0.1697", "1.30%", "99.20%"),
    (13, "0.1040", "0.80%", "100.00%"),
]
story.append(p("Autovalores y varianza explicada (datos estandarizados):", S_BODY_NOIND))
story.append(tabla(
    ["PC", "&lambda;", "Var. expl.", "Var. acum."], filas_wine,
    [0.35 * inch, 0.85 * inch, 0.85 * inch, 0.85 * inch]))

n5, n6 = figure_block(story, [
    ("fig_2_3_wine_scree_estandarizado.png",
     "Scree plot y varianza explicada acumulada para Wine, datos estandarizados."),
    ("fig_2_3_wine_scree_sin_estandarizar.png",
     "Scree plot y varianza explicada acumulada para Wine, datos SIN estandarizar."),
])

story.append(p(
    f"Con base en la Fig. {n5} y la tabla anterior, los tres criterios de decision "
    "vistos en clase dan resultados distintos. (i) <i>Umbral de varianza</i>: en "
    "clase se establecio como meta estandar capturar entre 90% y 95% de la "
    "varianza; aqui se requieren 8 componentes para superar 90% y 10 para superar "
    "95%. (ii) <i>Criterio de Kaiser</i>: definido en clase como retener los "
    "componentes con autovalor &gt;1 (validos sobre la matriz de correlacion, es "
    "decir, datos estandarizados); sugiere 3 componentes (&lambda;=4.73, 2.51, "
    "1.45). (iii) <i>Regla del codo</i>: en clase se definio de forma visual y "
    "heuristica &mdash;sin una formula rigurosa&mdash; como el punto donde ocurre "
    "el cambio mas abrupto en la curva y este empieza a aplanarse; en la Fig. 5 "
    "ese aplanamiento se observa claramente entre los componentes 3 y 4 (caida de "
    "1.45 a 0.92, seguida de caidas mucho menores). Como aproximacion numerica "
    "reproducible de esa inspeccion visual (calculando la distancia perpendicular "
    "maxima entre la curva y la cuerda que une su primer y ultimo punto) se "
    "obtiene el componente 4, consistente con la lectura visual de la grafica. "
    "Los tres criterios son razonables y coinciden en un rango compacto "
    "(3&ndash;4 componentes) si se prioriza compresion, o hasta 8&ndash;10 si se "
    "prioriza preservar casi toda la varianza.", S_BODY))

story.append(p(
    f"Al aplicar PCA sobre los datos sin estandarizar (Fig. {n6}), la primera "
    "componente concentra 99.81% de la varianza total (contra 36.20% en el caso "
    "estandarizado), y con solo 2 componentes se alcanza 99.98%. Esto ocurre porque "
    "la variable 'proline' tiene una escala numerica (cientos a miles) muchisimo "
    "mayor que el resto (p. ej. 'ash', en el rango 1-3), por lo que domina "
    "artificialmente la varianza total y, con ello, casi toda la primera "
    "componente. El efecto de no estandarizar es que PCA deja de reflejar la "
    "estructura de correlacion real entre variables y en su lugar refleja "
    "principalmente diferencias de escala/unidades, lo cual es indeseable cuando "
    "las variables se miden en unidades distintas (como es el caso de Wine).",
    S_BODY))

story.append(p(
    "Finalmente, se reconstruyeron los datos estandarizados usando "
    "k=1,&hellip;,13 componentes (X<sub>rec</sub>=Z<sub>k</sub>V<sub>k</sub><super>T</super>"
    "+&mu;) y se calculo el MSE entre X y su reconstruccion:", S_BODY))

filas_mse_wine = [
    (1, "0.6380"), (2, "0.4459"), (3, "0.3347"), (4, "0.2640"), (5, "0.1984"),
    (6, "0.1490"), (7, "0.1066"), (8, "0.0798"), (9, "0.0576"), (10, "0.0383"),
    (11, "0.0209"), (12, "0.0080"), (13, "0.0000"),
]
story.append(tabla(["k", "MSE"], filas_mse_wine, [0.7 * inch, 1.6 * inch]))

fig7, n7 = figure_incolumn(
    "fig_2_3_wine_mse_vs_k.png",
    "MSE de reconstruccion vs. numero de componentes k, dataset Wine "
    "(estandarizado).")
story.append(fig7)
story.append(p(
    f"La Fig. {n7} confirma que el MSE decrece monotonamente y de forma cada vez "
    "mas lenta, llegando a 0 en k=13 (reconstruccion exacta al usar todas las "
    "componentes, ya que no se pierde informacion).", S_BODY))

# ===========================================================================
# SECCION IV. COMPARACION DE METODOS (2.4)
# ===========================================================================
story.append(p("IV. Comparaci&oacute;n de m&eacute;todos (Iris)", S_H1))
story.append(p(
    "Se aplico PCA sobre Iris con tres implementaciones distintas: "
    "<font face='Courier'>pca_cov</font>, <font face='Courier'>pca_svd</font> y "
    "<font face='Courier'>sklearn.decomposition.PCA</font>, comparando los 4 "
    "valores y vectores propios que entrega cada una.", S_BODY))

filas_comp = [
    ("&lambda;1", "4.22824171", "4.22824171", "4.22824171"),
    ("&lambda;2", "0.24267075", "0.24267075", "0.24267075"),
    ("&lambda;3", "0.07820950", "0.07820950", "0.07820950"),
    ("&lambda;4", "0.02383509", "0.02383509", "0.02383509"),
]
story.append(tabla(
    ["Valor propio", "pca_cov", "pca_svd", "sklearn.PCA"], filas_comp,
    [0.55 * inch, 0.85 * inch, 0.85 * inch, 0.85 * inch]))

story.append(p(
    "Los cuatro valores propios coinciden exactamente (diferencias &le; "
    "3.55&times;10<super>-15</super>, error de punto flotante) entre las tres "
    "implementaciones. Para los vectores propios, las tres tecnicas entregan las "
    "mismas direcciones, pero antes de alinear signos algunas columnas difieren "
    "por un factor de -1 (p. ej. la columna 1 de <font face='Courier'>pca_cov</font> "
    "es exactamente la columna 1 de <font face='Courier'>pca_svd</font> multiplicada "
    "por -1). Tras fijar el signo de cada vector con respecto a una referencia comun, "
    "la diferencia maxima absoluta entre vectores propios de cualquier par de "
    "metodos fue de 2.11&times;10<super>-15</super>.", S_BODY))

story.append(p(
    "&iquest;A que se debe esta diferencia? Ni los eigenvectores de una matriz "
    "simetrica ni los vectores singulares de una SVD tienen un signo unico "
    "definido: si v es un vector propio (o vector singular) unitario, -v tambien lo "
    "es, y ambos representan la misma direccion/eje principal. Las tres "
    "implementaciones son matematicamente equivalentes &mdash;diagonalizar la matriz "
    "de covarianza (<font face='Courier'>pca_cov</font>) y aplicar SVD a los datos "
    "centrados (<font face='Courier'>pca_svd</font>, y lo que "
    "<font face='Courier'>sklearn.PCA</font> hace internamente) resuelven el mismo "
    "problema de optimizacion&mdash; por lo que las magnitudes coinciden salvo el "
    "signo, que depende de detalles de implementacion del algoritmo numerico "
    "subyacente (LAPACK) y no tiene significado estadistico.", S_BODY))

# ===========================================================================
# SECCION V. EIGENFACES (2.5)
# ===========================================================================
story.append(p("V. EigenFaces (Olivetti Faces)", S_H1))
story.append(p(
    "El dataset Olivetti Faces (400 imagenes de rostro de 64&times;64 pixeles, 40 "
    "sujetos) se cargo ya en forma de matriz X de (400, 4096) &mdash;n=400 imagenes, "
    "p=4096 pixeles por imagen&mdash; y se centro restando el rostro promedio "
    "(media de X). Sobre X centrada se aplico "
    "<font face='Courier'>pca_svd</font>, reutilizando la misma funcion de la "
    "Seccion III, obteniendo hasta 400 componentes (eigenfaces).", S_BODY))

n8, n9, n10 = figure_block(story, [
    ("fig_2_5_rostro_promedio.png",
     "Rostro promedio del dataset Olivetti Faces (media de X).", 0.32),
    ("fig_2_5_primeras_10_eigenfaces.png", "Primeras 10 eigenfaces (mayor varianza)."),
    ("fig_2_5_ultimas_10_eigenfaces.png", "Ultimas 10 eigenfaces (menor varianza)."),
])

story.append(p(
    f"La Fig. {n8} muestra el rostro promedio, un rostro suave y generico producto "
    f"de promediar las 400 imagenes. Las Fig. {n9} y {n10} muestran, "
    "respectivamente, las eigenfaces de mayor y menor varianza. Las primeras "
    "capturan patrones globales y de baja frecuencia que varian de forma consistente "
    "entre muchos sujetos (iluminacion general, contorno de la cara, presencia de "
    "lentes, sombras alrededor de ojos/nariz/boca); son reconocibles como rostros "
    "'borrosos' pero estructurados. Las ultimas eigenfaces, en cambio, lucen como "
    "patrones de alta frecuencia, ruidosos y sin estructura facial clara: capturan "
    "variaciones muy especificas de pocas imagenes (posiblemente ruido de "
    "adquisicion), consistente con sus valores propios cercanos a cero.", S_BODY))

story.append(p(
    "Se reconstruyo una imagen de prueba utilizando k=10, 50, 100, 200 y 300 "
    "eigenfaces, comparando contra la imagen original:", S_BODY))
(n11,) = figure_block(story, [(
    "fig_2_5_reconstruccion_por_k.png",
    "Reconstruccion de una imagen de Olivetti Faces usando k=10,50,100,200,300 "
    "eigenfaces, junto con la imagen original.")])
story.append(p(
    f"En la Fig. {n11} se aprecia como, con pocos componentes (k=10), la "
    "reconstruccion es muy borrosa y solo conserva rasgos generales; conforme k "
    "crece, se recuperan progresivamente detalles finos (lentes, textura de barba, "
    "arrugas) hasta lucir practicamente identica a la original con k=300 de un total "
    "de 400 posibles.", S_BODY))

story.append(p(
    "Se calculo tambien el MSE de reconstruccion sobre todo el dataset, variando k "
    "en intervalos de 20:", S_BODY_NOIND))
filas_mse_faces = [
    (20, "0.004559"), (60, "0.002093"), (100, "0.001246"), (140, "0.000791"),
    (180, "0.000507"), (220, "0.000319"), (260, "0.000193"), (300, "0.000106"),
    (340, "0.000047"), (380, "0.000010"), (400, "0.000000"),
]
story.append(tabla(["k", "MSE"], filas_mse_faces, [0.7 * inch, 1.6 * inch]))

fig12, n12 = figure_incolumn(
    "fig_2_5_mse_vs_k.png",
    "MSE de reconstruccion vs. numero de eigenfaces utilizadas k.")
story.append(fig12)

story.append(p(
    f"Como muestra la Fig. {n12}, el error decrece de forma monotona y convexa. "
    "En k=300, la varianza acumulada explicada es de 99.45% (0.55% de varianza "
    "descartada), lo que es consistente con un MSE ya muy cercano a cero "
    "(0.000106) en ese punto. Esto responde directamente a la pregunta de "
    "interpretacion: el error de reconstruccion disminuye al aumentar k porque "
    "cada eigenface adicional que se incorpora aporta exactamente la varianza "
    "asociada a su valor propio, informacion que antes se estaba descartando. De "
    "hecho, el MSE de reconstruccion es, salvo un factor de escala "
    "(1/p, con p el numero de pixeles), la suma de los valores propios de las "
    "componentes NO utilizadas (la varianza descartada): al ordenar las "
    "componentes de mayor a menor varianza, cada eigenface adicional agregada es "
    "la que mas reduce ese residuo en cada paso, por lo que el MSE cae rapido al "
    "inicio (las primeras eigenfaces concentran la mayor parte de la varianza) y "
    "se aplana conforme se agregan componentes cuyo valor propio es cada vez mas "
    "pequeno.", S_BODY))

# ===========================================================================
# CONCLUSIONES
# ===========================================================================
story.append(p("VI. Conclusiones", S_H1))
story.append(p(
    "El desarrollo de esta practica permitio verificar de forma empirica varias "
    "propiedades teoricas de PCA: los vectores propios de una matriz de covarianza "
    "son ortogonales entre si; el calculo via matriz de covarianza y via SVD son "
    "equivalentes (salvo signo) y coinciden con la implementacion de referencia de "
    "scikit-learn; estandarizar es indispensable cuando las variables tienen "
    "escalas distintas, pues de lo contrario PCA queda dominado por la variable de "
    "mayor varianza numerica en lugar de reflejar la estructura de correlacion "
    "real de los datos; y el error de reconstruccion al truncar a k componentes "
    "esta directamente ligado a la varianza (valores propios) descartada en las "
    "componentes no retenidas, lo cual se observo tanto en Wine como en EigenFaces.",
    S_BODY))

doc.build(story)
print(f"Reporte generado: {OUTFILE}")
print(f"Total de figuras numeradas en el reporte: {_fig_counter[0]}")
