% materia: Seguridad Informática Básica
% titulo: Clase 6 · Amenazas, riesgo y clasificaciones de las amenazas
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · jueves 17 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Del equilibrio operacional al Tema 2
- Repaso: los servicios de seguridad se gradúan según el negocio (ejemplo de Liverpool).
- **Amenaza y vulnerabilidad no son sinónimos**; tampoco hay relación uno a uno entre ellas.
- Hay que evaluar la **frecuencia** de cada amenaza (una vez al año, cada 24 h, cada 2 h…).
- Identificar activos, amenazas y vulnerabilidades responde la primera pregunta: **"¿qué quiero proteger?"**
Error común: buscar solo vulnerabilidades (o solo amenazas), o ignorar la frecuencia.

## 2. Describir con precisión y jerarquizar pérdidas
- Ejemplo de la vivienda: quedarse sin lugar, gastos no contemplados, bienes irrecuperables.
- Perro de globo (teme al cerillo) y origami (teme a la chincheta): el cerillo destruye **a los dos**. Hay pérdidas totales que no se recuperan "ni con todo el oro del mundo" → priorizar la inversión contra lo catastrófico.
!!! Precisión (examen)
No basta "robo" o "que tiemble": hay que decir **qué modalidad** de robo o **qué magnitud** (1.3 frente a 7.1, 7.5, 8.1/8.5; sismo de 2017; Haití sin protocolos). Lo de baja frecuencia (meteorito, avión que cae) **no se descarta**.

## 3. Definiciones formales
- **Amenaza:** cualquier actividad, evento o circunstancia que intenta o puede causar daño a la información o a cualquier bien (hardware, software, instalaciones, personas). Es un **factor latente** y multifactorial, siempre presente.
!!! Fórmula del riesgo
**Riesgo = Ocurrencia × Consecuencia.** Da la probabilidad concreta y la severidad del impacto si la amenaza se materializa.
- Ejemplos de disponibilidad: agua, gas, internet; si la UNAM dejara de existir; caídas del portal del SAT en abril.
- Puntos de acceso físicos o lógicos; desconfiguraciones ("así estaba cuando llegué" no vale).
- Errores de programación: software hecho "para ayer" sin seguridad; el de seguridad sí debe saber programar y viceversa.
Error común: tratar amenaza y riesgo como sinónimos.

## 4. Cinco fuentes de origen
| Fuente | Nota |
|---|---|
| **Factor humano** | La principal: descuidos, exceso de confianza |
| Fallas de hardware | Componentes físicos |
| Fallas de software | Código, aplicaciones, SO |
| Red | Hardware + software + comunicaciones |
| Desastres naturales (Actos de Dios) | Sin responsabilidad humana directa |
Todas se relacionan con el factor humano: las personas diseñan, configuran y mantienen la tecnología.

## 5. Clasificaciones
| Por flujo de información | Qué pasa | Atenta contra |
|---|---|---|
| Intercepción | Alguien no autorizado ve o escucha en el traslado | Confidencialidad |
| Interrupción / destrucción | No llega o deja de estar disponible | Disponibilidad |
| Modificación | Un tercero altera el contenido en tránsito | Integridad |
| Suplantación / falsificación | Alguien se hace pasar por el emisor | (engaña al receptor) |
| Por objetivo | Por ubicación |
|---|---|
| **Intencionadas:** planeadas o abuso de autoridad → **85–95 %** de los incidentes | **Internas:** empleados o activos internos → **85–95 %** de los problemas reales |
| No intencionadas: negligencia, ignorancia, accidentes | Externas: suelen requerir complicidad o descuido interno |
Error común: creer que lo más peligroso viene de fuera (sesiones abiertas, contraseña "Hola123").

## Pendiente
- Traer desayuno individual en recipiente cerrado (actividad práctica).
- Hoja carta: al frente foto individual con margen; al reverso foto de la fachada sin número ni dirección.
- Ejercicio en equipo hecho en clase: descripción detallada de un escenario (p. ej. un OXXO), una hoja firmada en orden alfabético.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Lo esencial
**Riesgo = Ocurrencia × Consecuencia.** Amenaza = factor latente. Amenazas descritas con precisión (modalidad, magnitud). 85–95 % de los incidentes son **internos e intencionados**.

| Flujo | Pilar |
|---|---|
| Intercepción | Confidencialidad |
| Interrupción | Disponibilidad |
| Modificación | Integridad |
| Suplantación | Engaño al receptor |

**Fuentes:** humano (la principal), hardware, software, red, desastres naturales.
