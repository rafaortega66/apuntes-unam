% materia: Minería de Datos
% titulo: Clase 4 · Bases vectoriales, de conocimiento y arquitectura de datos
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 10 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Bases de datos vectoriales y embeddings
- **Embedding:** convertir datos no estructurados (PDF, texto, imagen, voz, video) en vectores de miles de dimensiones que capturan su contexto semántico.
- **Chunking:** dividir el contenido en fragmentos; la pregunta del usuario se vuelve vector y se buscan los chunks más parecidos (base de los LLM/ChatGPT).
- **Índice vectorial:** agrupa por clustering; la consulta entra directo al cluster, sin revisar millones de registros.
| | SQL tradicional | Vectorial |
|---|---|---|
| Busca | Coincidencia **exacta** (edad > 48) | **Similitud semántica** aproximada |
| Índice | B-Tree / Hash | Clusters por zonas |
| Si no coincide | No devuelve nada | Devuelve lo más cercano |

## 2. Diseñar una arquitectura de datos (pregunta de examen)
1. Requerimientos **funcionales y no funcionales** (rendimiento, seguridad, escalabilidad, tolerancia a fallos).
2. Tipo de base de datos (relacional, no relacional, vectorial, especializada).
3. Esquema y relaciones.
4. Infraestructura (nube vs. local) y escalabilidad.
5. Seguridad y control de acceso por roles.
6. Pruebas de volumen, rendimiento y optimización.
| Componente | Qué hace |
|---|---|
| API | Reglas para acceder a funciones o datos de forma segura (conectores Oracle, IBM, Python) |
| Gateway | Enruta el tráfico entrante y saliente hacia servicios autorizados |
| ETL Batch | Extracción, transformación (formatos, fórmulas) y carga masiva |
Error común: omitir los requerimientos no funcionales o la infraestructura.

## 3. Vectorizar imagen, audio y video
- **Imagen (CNN):** convolución (extrae patrones) → **ReLU** (filtra características) → **Softmax** (vector de probabilidades: 70 % perro, 20 % caballo, 10 % otro). Usos: reconocimiento facial, fraudes, calidad (salpicaderas al 99 %).
- **Audio:** frecuencia, timbre, ritmo, forma de onda; identificar al hablante por su huella vocal.
- **Video:** por frames; vigilancia (cruce de línea) y análisis deportivo (Bayern Múnich).

## 4. Bases de datos de conocimiento
- Llegan **"vacías", como un Excel**: hay que configurar reglas, fórmulas y datos.
- Se cargan con **plantillas y cuestionarios** por área (RRHH, Finanzas, Ventas): documentos, glosarios (p. ej. ROI), reglamentos.
- Usos: onboarding con exámenes de reglamento; capacitación obligatoria cada 6 meses (empresas de 3,000 empleados).

## 5. Arquitectura para minería e IA
Capas: origen (Excel, AWS/Google, IoT) → ETL → Data Lake / Data Warehouse → servicio y visualización.
**Caso IoT:** 500 sensores (electricidad, temperatura, gas, agua) cada 20 s → Data Warehouse → modelo predictivo que dispara alerta **amarilla** al supervisor antes de la falla.
Error común: conectar la analítica directo a las bases transaccionales.

## 6. Caso Nu (mi exposición)
| Elemento | Dato |
|---|---|
| Escala | 135 millones de clientes; 37.2 billones de dólares en crédito |
| Problema | Morosidad temprana (15–90 días) de 4.1 % a 5 %; provisiones +33 %; 70 % de rechazos por falta de historial |
| Metodología | CRISP-DM |
| Variables | Historial de pagos, uso de la línea, antigüedad, comportamiento en la App |
| Modelos | Regresión logística, Random Forest, XGBoost |
| Métricas / explicabilidad | **Gini, KS, SHAP, WoE** |
| Arquitectura | Kafka → Spark → Data Lake/DW → API de scoring en la nube (99.5 %) |
Retroalimentación: buen rol de vendedor y presentación limpia; mantener contacto visual ≥ 80 % del tiempo.

## Pendiente
- Proyecto 2 (Tema 2): viernes 18 sep 2026, 14:00 (Classroom).
- Próxima: exposiciones de proveedores nube/BD, 8 min por equipo (AWS con TimeStream).
- **Confirmado para examen:** diagrama completo de arquitectura de minería con requerimientos funcionales y no funcionales.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Pregunta segura de examen
Arquitectura en 6 pasos: requerimientos (funcionales y no funcionales) → tipo de BD → esquema → infraestructura → seguridad por roles → pruebas.

| Concepto | Para recordar |
|---|---|
| Vectorial vs. SQL | Similitud semántica por clusters vs. coincidencia exacta con B-Tree |
| Embedding + chunking | Datos → vectores; fragmentos que se recuperan por cercanía |
| CNN | Convolución → ReLU → Softmax |
| BD de conocimiento | Llega vacía; plantillas por área |
| Crédito (Nu) | Gini, KS, SHAP, WoE; Kafka + Spark |
