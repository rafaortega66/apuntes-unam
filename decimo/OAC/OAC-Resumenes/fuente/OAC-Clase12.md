% materia: Organización y Arquitectura de Computadoras
% titulo: Clase 12 · Minicomputadoras, almacenamiento y ruido eléctrico
% subtitulo: Organización y Arquitectura de Computadoras · M.I. José Antonio de Jesús Arredondo Garza · lunes 19 oct 2026 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Sesión sin tema nuevo del temario: el profesor borró por accidente sus notas del día. Charla sobre tarjetas monoplaca (SBC), almacenamiento y ruido eléctrico, y luego revisión individual de proyectos. Sin código ni fórmulas.

## 1. Elegir una minicomputadora según el proyecto
Evaluar las SBC (Single Board Computers) por núcleos, capacidad de correr un SO y costo, frente a lo que de verdad pide el proyecto.
| Tarjeta | Dato |
|---|---|
| Orange Pi 5 | 8 núcleos (le regalaron una, sin estrenar) |
| Orange Pi 6 | 12 núcleos |
| Raspberry Pi 5 | $3,000 – $4,000 MXN |
| **Raspberry Pi Zero 2 W** | Opción barata: SO completo, ≈ 4 núcleos (según recuerda), apenas mayor que una Pico 2, MicroSD, USB-C y un USB para periféricos |
!!! Criterio de diseño
Pedirle 8 o 12 núcleos a un programa pequeño o de enseñanza es excesivo: elegir la plataforma por requerimientos reales y presupuesto antes de desarrollar.

## 2. Experiencia: 40 bioseñales con una Raspberry Pi multinúcleo
- Proyecto del profesor: adquirir y transmitir **40 bioseñales** en tiempo real con módulos de Texas Instruments, repartiendo el trabajo en los **4 núcleos** de una Raspberry Pi 4 (luego evaluó la Pi 5).
- El montaje artesanal tenía graves problemas de **ruido eléctrico**.
- Terminó comprando un equipo comercial cerrado ("caja negra" portátil) a una empresa inglesa con hasta 30 % de descuento.
Lección: los multinúcleo sirven en instrumentación, pero **más núcleos no arreglan una señal con ruido**, y a veces conviene comprar una solución comercial.

## 3. Almacenamiento: MicroSD frente a SSD M.2
En la Raspberry Pi 4 o 5, la **MicroSD es el cuello de botella** del sistema operativo. El profesor conectó un **SSD M.2 externo de 128 GB** y el sistema se aceleró muchísimo.
| Medio | Precio aproximado | Desempeño |
|---|---|---|
| MicroSD estándar 32 GB | $100 – $200 | Lento para el SO |
| MicroSD "ultra rápida" (reporteros, fotógrafos) | $8,000 – $10,000 | Sigue por debajo del M.2 |
| **SSD M.2 128 GB** | Una fracción de la SD ultra rápida | Mucho mejor |
Error común: gastar miles de pesos en una MicroSD ultra rápida creyendo que es la única forma de acelerar la Pi. El M.2 necesita adaptador o puerto y ocupa más espacio.

## 4. Ruido eléctrico en mediciones sensibles
La Pico (1 y 2) y las Raspberry Pi grandes tienen **ruido eléctrico propio**, y las fuentes de grado médico cuestan miles de pesos. Solución del profesor:
1. **Baterías de litio** en lugar de fuente de pared (las fuentes conmutadas meten ruido).
2. **Conversor de puerto serie a fibra óptica** para sacar los datos con aislamiento eléctrico.
3. Para entornos muy sensibles, la Pico dentro de una **jaula de Faraday**.
Clave en adquisición analógica e instrumentación biomédica. Error común: suponer que la alimentación o el ADC de la Pico entregan señales limpias sin filtrado ni aislamiento.

## 5. Resto de la sesión
Revisión individual de proyectos de quienes los tenían listos. Próximas clases: arquitectura de CPU y minicomputadoras.

# PARTE 2 · Resumen para estudiar
~ No hubo tema nuevo; si algo entra al examen, será como criterio de diseño.

**Hardware a la medida.** Para proyectos chicos, una Pi Zero 2 W (SO completo, barata); 8–12 núcleos (Orange Pi 5/6) sobran.

!!! Almacenamiento (criterio de diseño)
La MicroSD es el cuello de botella de la Pi. Un SSD M.2 de 128 GB la acelera mucho y cuesta una fracción de una MicroSD ultra rápida ($8,000–$10,000): no comprar esas para una SBC.

| Problema | Solución del profesor |
|---|---|
| Ruido de la fuente | Baterías de litio |
| Ruido por el cable de datos | Serie → fibra óptica (aislamiento) |
| Entorno muy sensible | Jaula de Faraday |
| 40 bioseñales en tiempo real | Repartir en 4 núcleos (Pi 4); al final, equipo comercial |
