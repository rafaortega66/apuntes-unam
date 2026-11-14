% materia: Minería de Datos
% titulo: Clase 20 · Redes neuronales (exposiciones), CRISP-DM y evaluación de modelos
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 10 nov 2026 · Práctica 3.6 (redes neuronales) y Tema 4 (CRISP-DM y evaluación de modelos) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Exposiciones de la Práctica 3.6 de redes neuronales (RNN, CNN y MLP), encuadre del proyecto final y Tema 4: la metodología CRISP-DM y la evaluación de modelos (validación cruzada, subajuste, sobreajuste y análisis de errores).

!!! Fuente
Fuente: NotebookLM (audio `MD-Clase20.m4a`), 14 nov 2026. En el cuaderno solo hay audios. Las cifras de las exposiciones son de los alumnos. La Clase 19 (5 nov) fue el examen.

## 1. Exposiciones de la Práctica 3.6: redes neuronales
**RNN:** para datos secuenciales, donde cada registro depende de los anteriores (clima, finanzas). **CNN:** procesa imágenes con filtros que detectan bordes, texturas y patrones espaciales. **MLP:** para datos tabulares, donde cada columna es un atributo sin estructura espacial ni secuencial.

!!! En simple
Tres inspectores: el MLP lee un formulario con datos sueltos; la CNN recorre una foto con lupa cuadro por cuadro; la RNN lee una historia página por página recordando lo anterior. Límite: un alumno mostró que una RNN o un MLP también pueden usarse con imágenes (como secuencias o vectores de píxeles), solo que peor que una CNN.

| Caso | Red | Lo más importante |
|---|---|---|
| Temperatura máxima diaria (Kaggle) | RNN | 800 / 200 / resto; bloques de 10 días; 4 capas de 50 nodos con dropout; error ~0.83 en entrenamiento y 9.76 en validación. El profesor: en Acapulco o Cancún hace falta mucha precisión por los huracanes. |
| Neumonía en ~5,126 radiografías | CNN | 150×150, lotes de 32, un canal; a las 10 épocas rozaba 100 % (memorizaba): aumento de datos, dropout del 50 % y paro temprano. El profesor: «aprendió bien». |
| Retrasos en entregas de comida (3,000 registros simulados) | Red de 1 y 2 capas | Picos a las 15:00 y 23:00; paró en la época 20; exactitud 0.900, F1 0.854. |
| Peluches que solo cambian de color (~400 fotos) | CNN desde cero contra MobileNetV2 | Sin aumento de datos en el color (era el rasgo distintivo); ganó MobileNetV2; Grad-CAM para ver dónde mira la red. |
| Malware convertido en imágenes (26 clases, ~15,000) | CNN | 256×256; pérdida de 1.6 a 0.27, precisión de 53 % a 81 %; en ciberseguridad son preferibles los falsos positivos. |
| Precios de Walmart EUA, Costco y Walmart México | Series con redes | Ventanas de 30, 60 y 90 días; concluyó que tres mercados dispersaron el análisis. |
| Churn en telecomunicaciones (Kaggle) | MLP | 73.6 % se queda y 26.5 % se va: la exactitud engaña; peso de 1.88 a la clase de abandono y umbral de 0.3 → recall 0.78. |
| Fashion-MNIST (70,000 imágenes de 28×28) | CNN, MLP y LSTM | Ganó la CNN con 92.39 % (MLP 89.66 %, RNN 89.37 %), pero sin GPU tardó 32.4 minutos. |

Por qué importa: Cierra la práctica conectando arquitectura, sobreajuste y desbalanceo con problemas reales.
Error común: confiar en la exactitud con clases desbalanceadas; no regularizar una CNN que memoriza en pocas épocas.

## 2. CRISP-DM contra KDD
CRISP-DM es el estándar de la industria (Oracle, Google, Amazon, IBM, Microsoft, SAP) para proyectos de minería de datos, *machine learning* y ciencia de datos: parte del entendimiento del negocio y llega hasta el despliegue.

!!! En simple
KDD es el libro universitario de arquitectura con los planos conceptuales; CRISP-DM es el manual de obra de las grandes constructoras: primero te sientas con el dueño (presupuesto, riesgos, plazos) y no terminas hasta entregar las llaves con plan de mantenimiento. Límite: la obra suele ser lineal; en CRISP-DM, si la evaluación falla, se regresa entre fases.

KDD es más académico y conceptual, centrado en descubrir patrones con la minería como fase central. El proceso técnico de minería visto antes se enfocaba en lo tecnológico. CRISP-DM pone mucho peso en los objetivos de negocio desde el inicio y detalla hasta la implementación.

Niveles: el **nivel 1** son las 6 fases, iguales en todas las compañías; el **nivel 2** tiene variantes en las subtareas; en los **niveles 3 y 4** cada proveedor usa sus herramientas (IBM con SPSS), hasta unas 500 actividades.

Por qué importa: Es la base del proyecto final: las 6 fases en niveles 1 y 2 y actividades seleccionadas del nivel 3.
Error común: confundir KDD con CRISP-DM; querer cubrir las ~500 actividades en un proyecto escolar.

## 3. Las 6 fases de CRISP-DM (ejemplo de e-commerce)
(1) Entendimiento del negocio, (2) entendimiento de los datos, (3) preparación de los datos, (4) modelado, (5) evaluación y (6) despliegue.

!!! En simple
Abrir una cafetería con datos: acuerdas metas con el dueño, revisas los cuadernos de ventas, los limpias en una sola hoja, pruebas combos, haces una degustación con el dueño y lanzas el menú en todas las sucursales con plan de revisión.

**1. Entendimiento del negocio:** objetivos, entorno, inventario de recursos, limitantes, supuestos, riesgos y contingencias, costo-beneficio, criterios de éxito de negocio *y* metas de ciencia de datos (sin ambas no se avanza) y un primer plan (rutas críticas de 100 a 150 actividades con un *project manager*). **Ejemplo:** un e-commerce quiere vender más con recomendaciones; se reúne a ventas y marketing (no a mantenimiento) con TI; el problema es la baja conversión porque no encuentran productos relevantes; metas: +10 % ventas y −20 % tiempo de respuesta (negocio) y precisión > 90 % (ciencia de datos); recursos: historial de compras, visitas y clics; limitantes: competencia y presupuesto; riesgos: datos de usuarios desactualizados.

**2. Entendimiento de los datos:** recopilar, describir, explorar (EDA) y verificar calidad. En un proyecto de churn: edad, género, plan, minutos y facturación; ya se ven patrones antes de los algoritmos.

**3. Preparación:** seleccionar con justificación, limpiar (mediana para vacíos o eliminar registros erróneos), construir atributos derivados (totales y promedios), integrar fuentes (clientes, pagos, demografía) y dar formato uniforme (todo a minutos).

**4. Modelado:** «el corazoncito, el *kernel* de minería de datos»: particionar, elegir algoritmos, ajustar parámetros y construir el modelo.

**5. Evaluación:** técnica (métricas) y de negocio (sentarse con el cliente y obtener su aprobación).

**6. Despliegue:** plan de implementación, de monitoreo y mantenimiento, informe final o memoria técnica y evaluación de qué funcionó.

Por qué importa: En el proyecto final pidió darle más peso a las fases 1 y 6 («pónganle un poquito más de calza»).
Error común: arrancar sin criterios cuantitativos de éxito de negocio y de ciencia de datos.

## 4. Evaluación de modelos: validación cruzada y tipos de ajuste
**Validación cruzada (K-folds):** dividir los datos en K partes, entrenar y probar rotando, y promediar los scores. **Subajuste:** el modelo es demasiado sencillo (malo en entrenamiento y en prueba). **Sobreajuste:** memoriza (excelente en entrenamiento, malo en prueba). **Buen ajuste:** bueno y consistente en ambos.

!!! En simple
Validación cruzada: divides el temario en 5 bloques, cada día estudias 4 y te examinas con el quinto, y promedias. Subajuste: estudiar tan por encima que repruebas todo. Sobreajuste: memorizar la guía palabra por palabra y reprobar en cuanto cambian la redacción. Límite: con datos médicos, si un paciente tiene varios registros, todos deben quedar en la misma partición.

Hay cerca de 20 técnicas de validación cruzada; la idea de K-fold (por ejemplo 5-fold en Python) es rotar el bloque de prueba y promediar. Un 70/30 basta en modelos sencillos (marketing); en médicos o científicos hace falta K-fold, agrupando por paciente.

**Subajuste:** faltan datos o variables ricas (o hay mucha correlación entre pocas). Ser sincero con el cliente y enriquecer el dataset (edad, estudios, residencia, experiencia).

**Sobreajuste:** particiones sesgadas, variables que sobran o demasiadas épocas. Cinco vías: (1) revisar variable por variable (correlaciones, eliminación recursiva, sin recortar de más); (2) muestreo y estratificación (por tienda, región o categoría, o promediar sensores cada 5 minutos); (3) regularización (Lasso, Ridge, dropout); (4) simplificar el modelo (podar árboles); (5) validación cruzada y aumento de datos.

**Umbrales por dominio:** en ventas, más de 80 % suele ser bueno; en medicina o ciencia, 90 % o más (nunca hay 100 %; el tope real ronda 92–94 %). En finanzas, con un pronóstico de 8,350,000 pesos ±500,000, la dirección usa el límite superior para protegerse.

**Análisis de errores:** en una matriz de confusión de cáncer (sano, nivel 3, nivel 5), lo grave son los falsos negativos (decir sano a quien tiene nivel 3) y también los falsos positivos. Qué hacer: revisar caso por caso, ajustar el umbral, balancear clases, replantear variables, probar 2 o 3 algoritmos y validar con precisión, recall y F1.

Por qué importa: Unifica todas las prácticas bajo criterios para que el modelo no dé sorpresas en producción.
Error común: creer que un 70/30 basta en problemas médicos; esperar 100 %; recortar demasiadas variables.

## Pendiente / próxima clase
- El profesor enviaría ese día las diapositivas de CRISP-DM, la lista de casos de negocio asignados para el proyecto final y la descripción del contenido.
- **Próximo jueves (12 nov):** Tema 5, evaluación de proyectos.
- **Proyecto final: jueves 19 nov a la 1:00 p.m.** Individual, las 6 fases de CRISP-DM (más peso en la 1 y la 6), programas en Python según el caso asignado y una presentación ejecutiva de exactamente 10 láminas, más el código. Pesa casi el doble que los proyectos 1 y 2. Las exposiciones empiezan ese jueves y siguen en la última clase.
- **Tercer parcial:** el martes después del jueves 19 (todo el temario).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Las 6 fases de CRISP-DM y su diferencia con KDD y con el proceso técnico de minería de datos.** dijo que el tercer parcial cubre «todo lo que hemos visto» de la unidad y dedicó media clase a CRISP-DM.
- **Distinguir sobreajuste, subajuste y buen ajuste con las métricas de entrenamiento y prueba.** «muchos de ustedes mismos ya me lo han hasta contestado en el examen»; detalló cómo diagnosticar y corregir cada caso.
- **Validación cruzada (K-folds), muestreo estratificado y desbalanceo.** lo resumió como parte formal del Tema 4.
- **Matriz de confusión, umbrales según el dominio y qué hacer cuando las métricas fallan.** analizó un caso médico de niveles de cáncer y listó las correcciones.
- **Qué red neuronal según el tipo de datos (CNN, RNN, MLP).** evidencia moderada: ocupó media clase con 8 exposiciones.

!!! Puntos clave
- MLP = tabular; CNN = imágenes; RNN = secuencias. Con desbalanceo, la exactitud engaña: pesos por clase y umbral.
- CRISP-DM: negocio → datos → preparación → modelado → evaluación → despliegue; criterios de negocio y de ciencia de datos.
- Subajuste: malo en todo → más variables. Sobreajuste: memoriza → revisar variables, estratificar, regularizar, simplificar, K-fold.
- Ventas > 80 %; medicina ≥ 90 %; nunca 100 %. Cuidado con los falsos negativos en salud.

## Ponte a prueba
1. **¿En qué se diferencian KDD y CRISP-DM?** KDD es académico y conceptual, centrado en descubrir patrones; CRISP-DM es el estándar de la industria, orientado al negocio desde el inicio y hasta el despliegue.
2. **¿Cuáles son las 6 fases de CRISP-DM y a cuáles pidió más peso en el proyecto?** Negocio, datos, preparación, modelado, evaluación y despliegue; más peso a la 1 y a la 6.
3. **Subajuste contra sobreajuste en entrenamiento y prueba.** Subajuste: bajo en ambos. Sobreajuste: excelente en entrenamiento y malo en prueba.
4. **Reingresos hospitalarios: 2,000 consultas de 600 pacientes; 97 % en entrenamiento y 64 % en prueba. ¿Qué pasa y qué haces?** Sobreajuste, quizá por mezclar consultas del mismo paciente entre particiones. K-fold agrupando por paciente, regularización o dropout, y revisar variables o reducir épocas.
5. **En el ejemplo de e-commerce, ¿quién va a la reunión inicial y qué criterios se definen?** Ventas y marketing con TI; criterios de negocio (+10 % ventas, −20 % tiempo) y de ciencia de datos (precisión > 90 %).
6. **¿Por qué MLP para churn, CNN para imágenes y RNN para clima o bolsa?** MLP: datos tabulares; CNN: patrones espaciales con filtros; RNN: secuencias que dependen de lo anterior.
7. **¿Qué precisión es aceptable en ventas y en medicina?** Más de 80 % en ventas; 90 % o más en medicina (el tope real ronda 92–94 %).
8. **¿Por qué muestrear o agregar millones de tickets o lecturas de sensores?** Porque registros casi idénticos no aportan y afectan el rendimiento; estratificar o promediar conserva lo sustancial.
