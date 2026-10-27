% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 1 · Qué es (y qué no es) un sistema embebido
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · miércoles 26 ago 2026 · Tema 1 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Definición: el "ínfimo"
!!! Definición (examen)
Un sistema embebido es el **ínfimo** ("la máxima cota inferior") de hardware y software necesario para resolver una tarea específica **con control digital**: ni más ni menos de lo que la tarea exige.
| Ejemplo | ¿Embebido? | Por qué |
|---|---|---|
| Serie navideña (9 V) | No | Sin lógica programable |
| Control remoto | Sí (mínimo) | Microcontrolador que genera el tren de pulsos |
| Aspersor de jardín | No | "Mecánico maravilloso": agua, pico y resorte |
| Marcapasos | Digital sí; mecánico no | — |
| Reloj Casio | Sí | Control digital de la pantalla |

## 2. Clasificación en vivo
- **Cámara de seguridad:** digital (sensor + microcontrolador).
- **Microondas analógico:** temporizador de resorte ("tac tac") y capacitores en la perilla: **no** digital.
- **Lavadora manual:** perilla mecánica, sin ciclos programados.
- **Alarma de humo analógica:** sensor a la **base** de un transistor; colector a la alimentación; emisor con resistencia y **buzzer** a tierra. Con humo, el transistor se **satura** y suena: sin computadora.
- **Tamagotchi** y **calculadora:** computadoras dedicadas.

## 3. Medidor de la CFE
- **Electromecánico:** inductor → campo magnético → disco → engranes → contadores. Consumos de nanoamperios no vencen la **fricción** y no se registran.
- **Digital:** si la corriente de activación del transistor supera el consumo, tampoco registra.
- **Consumo fantasma** (standby): muchos consumos diminutos suman algo significativo; la CFE puso medidores con corriente de activación muy baja.

## 4. Más ejemplos mecánicos
- **Oxímetro:** embebido (procesador para el sensor óptico).
- **"Planchadora" de tarjetas:** rodillo y papel carbón; no lee nada ni puede clonar.
- **Termostato bimetálico** (nitinol, níquel-titanio): un metal se dilata más que el otro y se tuerce; engranes reductores convierten 1/8 de vuelta en 1/2. **No aluminio con hierro** (el aluminio se dilata demasiado).
- **Semáforo electromecánico** (fines del siglo XIX): plato giratorio sincronizado con la red; láminas de cobre tocan tres escobillas.

## 5. Motores y carbones
Taladro de CA: bobinas en estator y rotor; **escobillas de carbón** sobre el conmutador, que invierte la polaridad cada media vuelta para que no se detenga.
!!! Por qué carbón
Es **conductor**, **suave** y **lubricante sólido**: metal contra cobre se destruiría por fricción. Se desgasta hasta que el resorte ya no lo empuja; se cambia por unos pesos en vez de tirar la herramienta.

## 6. Propiedades de los materiales
| Propiedad | Definición | Ejemplo |
|---|---|---|
| **Dureza** | Resistencia a la fricción: no se raya; suele ir con fragilidad | Diamante (se fractura de un golpe) |
| **Tenacidad** | Deformarse sin romperse | Acero (se raya, pero se dobla) |
| **Ductilidad** | Estirarse en hilos o láminas sin fracturarse | Oro (blando) |

## 7. Tabla de clasificación
| Embebido / digital | Híbrido | Mecánico / analógico |
|---|---|---|
| Frenos ABS, impresora, puerta automática, rover de Marte, cerradura electrónica, RFID/biométrico, termómetro digital, Roomba, piano digital, bocinas Bluetooth, Apple Pencil | Multímetro, elevador, expendedora, diálisis (lazo abierto 3 h vs. lazo cerrado por conductividad de la sangre), hub de red vs. USB, radio, inyección de combustible, lector de código de barras | Detonador de C4, cafetera de estufa, cámara de rollo, bomba de insulina básica, semáforo peatonal con relé, walkie-talkie de los 80, tornamesa |
Error central de la clase: llamar "embebido" a algo analógico o mecánico.

## 8. Computadora
!!! Definición (examen)
"Una máquina que consta de **elementos de entrada**, **elementos de salida**, **procesador central** y **memoria**."

## Pendiente
Próxima: procesadores y arquitecturas (PIC, AVR…). Repasar la diferencia entre digital y mecánico/analógico.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Embebido | Ínfimo de hardware y software con control digital |
| No embebido | Aspersor, alarma con transistor, termostato bimetálico, medidor electromecánico |
| Computadora | Entrada, salida, procesador, memoria |
| Carbón | Conductor + lubricante sólido |
| Materiales | Dureza (diamante), tenacidad (acero), ductilidad (oro) |
| CFE | Consumo fantasma → medidores digitales sensibles |
