% materia: Organización y Arquitectura de Computadoras
% titulo: Clase 1 · Historia del hardware, Von Neumann vs. Harvard y pipeline
% subtitulo: Organización y Arquitectura de Computadoras · M.I. José Antonio de Jesús Arredondo Garza · lunes 31 ago 2026 · Temas 1, 2 y 4 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

!!! Fuentes
La historia viene del audio. Von Neumann/Harvard, CISC/RISC y el pipeline vienen de **fotos de apuntes a mano** (esa parte no se grabó); lo ilegible va marcado con [?].

## 1. Cálculo mecánico
- **Pascalina:** engranes; sumadoras que duraron en comercios de EE. UU. hasta el siglo XX; su manivela es el antecedente de la tecla Enter.
- **Babbage:** Máquina Diferencial (**1822**, tablas trigonométricas y logarítmicas) y Máquina **Analítica** (**1830**, primer ordenador de propósito general, con tarjetas perforadas).
!!! Por qué no se terminó (examen)
No por falta de tecnología, sino porque Babbage **modificaba continuamente** el diseño y no lo concluía.

## 2. Ada Lovelace
Hija de Lord Byron. Tradujo el artículo de Menabrea y añadió notas que **duplicaban** su extensión. En la **Nota G**, algoritmo para los **números de Bernoulli** con:
- cálculo en **paralelo**;
- condicionales **if-then**;
- **tarjetas perforadas** (de los telares de Jacquard) para álgebra.
El lenguaje **ADA** (Departamento de Defensa de EE. UU., aeronáutica) lleva su nombre.

## 3. Control programado y Enigma
- Antecedentes: cajas de música medievales (cilindros) y telares holandeses con tarjetas perforadas.
- **Enigma:** matemáticos **polacos** (años 20) hicieron avances y diseños; el equipo británico de **Turing** construyó y modificó la máquina. Aporte: **cálculos iterativos**. El profesor cuestiona atribuir todo a Turing.

## 4. Relevadores, bulbos y transistores
| Tecnología | Rasgos |
|---|---|
| Relevador (años 20) | Bobina + núcleo; conmuta como un transistor |
| Bulbo (1910; auge 30–40) | Cátodo, rejilla, ánodo; **100–1000 V**, mucho calor, vida corta; ENIAC usaba miles; el cinescopio de TV fue de los últimos |
| Transistor (Bell, **1947–48**) | Germanio; bajo voltaje; primeras computadoras en **kHz** |
| CI (1962) / compuertas (1969) | Amplificadores operacionales; luego compuertas en un encapsulado |
| Intel 8008 (1972), 8080 (1974) | 8 bits; sin coprocesador ni periféricos integrados; sus creadores fundaron Zilog |

## 5. Consumo y computación personal
| Tecnología | Consumo en vacío |
|---|---|
| PMOS (40 patitas, mediados de los 70) | **≈ 1 A** |
| CMOS, Motorola MC6800 (1976) | **≈ 200 mA** |
| Raspberry Pi Pico 2 (RP2350) | **2–5 mA** |
- Intel **8086 (1978)** → x86; 8088; **IBM PC (1980)**. Disquetes de 8" y 5.25" de ~150 KB.

## 6. Lógica programable
Tarjetas madre de hasta **50 × 50 cm** motivaron:
- **PROM/PAL:** fusibles que se queman una sola vez.
- **PLD y Gate Arrays** (~1988).
- **FPGA** (~1990): bloques reconfigurables; hoy de 2 nm (caras, calientes) a 25 nm. Clonar procesadores (clon del MC6800 del Dr. Szabó).
- **FPAA:** arreglos analógicos de amplificadores; poco éxito comercial.
Error común: creer que un procesador en FPGA alcanza la velocidad del chip original.

## 7. Von Neumann vs. Harvard (apuntes a mano)
| | Von Neumann | Harvard |
|---|---|---|
| Memoria | Una para datos e instrucciones | Separadas |
| Efecto | Busca instrucción **o** dato | Instrucción **y** dato en el mismo ciclo |
| Se asocia con | CISC | RISC |
Cada instrucción cuesta ciclos de reloj.

## 8. CISC vs. RISC (apuntes a mano)
- **CISC:** instrucciones complejas, cercanas al alto nivel; pocas líneas.
- **RISC:** simples y uniformes: carga, almacena, opera (`LDA A,(i)`, `SUB A,B`, `STA (i)`, `INC A`…). Hay números en los apuntes (33, 66, 20/80, 64) que no se leen [?].

## 9. Ciclo del procesador y pipeline
**Fetch → Decode → Execute → Write Back.** Con pipeline, cada instrucción entra un ciclo después de la anterior:
```
      T1 T2 T3 T4 T5 T6 T7
I1    F  D  E  WB
I2       F  D  E  WB
I3          F  D  E  WB
I4             F  D  E  WB
```
Una vez lleno, sale **un resultado por ciclo**.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Tema | Para recordar |
|---|---|
| Babbage | Diferencial 1822, Analítica 1830; no la terminó por cambiar el diseño |
| Ada | Nota G: Bernoulli, paralelo, if-then, tarjetas perforadas |
| Enigma | Polacos años 20; Turing; cálculos iterativos |
| Consumo | PMOS 1 A → CMOS 200 mA → Pico 2 2–5 mA |
| Lógica programable | PROM → PLD → FPGA; FPAA analógica |
| Von Neumann / Harvard | Una memoria / dos memorias |
| Pipeline | F, D, E, WB; un resultado por ciclo |
