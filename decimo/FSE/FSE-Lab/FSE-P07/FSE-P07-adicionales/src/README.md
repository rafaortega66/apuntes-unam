# FSE-P07 — Código de la Práctica 7 (dimmer con TRIAC)

Código preparado el 2 nov 2026 a partir del manual (`../../FSE-P07-indicaciones.pdf`).
**Probado solo en simulación** (sketch compilado con stubs de Arduino en la Mac, I²C simulado);
falta probarlo con el circuito real. Las mediciones del reporte salen del circuito, no de aquí.

## Archivos

| Archivo | Va en | Para |
|---|---|---|
| `arduino/p7_dimmer/p7_dimmer.ino` | Arduino UNO | Cruce por cero (D2) → Timer1 → pulso al MOC3021 (D3); esclavo I²C 0x0A |
| `raspberry/p7_i2c.py` | Raspberry Pi | Lectura/escritura I²C + cálculo de potencia real (Ecs. 3 y 11) |
| `raspberry/exp1_consola.py` | Raspberry Pi | **Experimento 1** [6 pt]: teclear 0–100 % |
| `raspberry/exp2_potencia_real.py` | Raspberry Pi | **Experimento 2** [4 pt]: muestra retardo, α, frecuencia medida y potencia real |
| `raspberry/exp3_web.py` | Raspberry Pi | **Experimento 3** [+2 pt]: página con slider en `http://<ip-pi>:8080` (`--simulate` para probar sin hardware) |

## Pasos en el laboratorio

1. **Seguridad primero** (127 V AC): todo el lado AC aislado con cinta, fusible en la fase,
   y medir con multímetro que no haya > 5 V en el lado DC y que entre pines optoacoplados haya impedancia infinita.
2. Arma la Figura 8 (AC) y prueba: el LED UB del detector debe encender tenue; 5 V al MOC → foco encendido.
3. Arma la Figura 9 (DC): Zero cross → D2, Dimmer → D3, SDA/SCL/GND según Tabla 2.
4. Sube `p7_dimmer.ino` (Arduino IDE, placa UNO). Monitor serie a **57600**: debe mostrar `T/2 ≈ 8.333 ms`
   (si sale 0 o ≫ 8.3, el detector no está llegando a D2).
5. En la Pi: `sudo raspi-config` → I2C, `sudo apt install i2c-tools python3-smbus2`
   (o `pip install smbus2`), `i2cdetect -y 1` debe mostrar `0a`.
   Ojo: en la Pi quedó el kiosko de la P5 usando GPIO2/3 (ya se renombró `/etc/rc.local` en la P6; verificar).
6. Copia `raspberry/` a la Pi y corre `python3 exp1_consola.py`, luego `exp2_potencia_real.py`, luego `exp3_web.py`.

## Qué anotar para el reporte (lo que hay que medir de verdad)

- Voltaje de línea real y frecuencia que reporta el Arduino (`T/2`).
- Para 0, 25, 50, 75, 100 % pedidos: retardo aplicado, potencia real que calcula `exp2`, y cómo se ve el foco.
- Si hay osciloscopio: forma de onda en el foco a 50 % (debe verse el recorte de fase de la Figura 5b).
- Capturas de la consola de exp1/exp2 y de la página de exp3 abierta desde el celular.

## Observaciones sobre el manual (para la discusión del reporte)

- **La Tabla 1 no es potencia, es Vo/Vrms.** Sus tiempos coinciden (±30 µs) con invertir la Ec. 6/11
  (Vo/Vrms), no con la Ec. 3 (P/Pmax). Por eso «50 %» en la tabla = 5.245 ms ⇒ α = 113° ⇒ **25.5 % de la potencia real**,
  mientras que el 50 % real se obtiene a α = π/2 = 4.167 ms (que la Ec. 3 y el pie de página 3 sí dan como 50 %).
  El propio texto llama «factor de potencia» a Vo/Vrms, que no es la definición usual.
  El código usa la tabla (es lo que pide el profesor) y `exp2` reporta la potencia real con la Ec. 3.
- En un foco incandescente R no es constante (el filamento frío tiene mucha menor resistencia), así que la Ec. 3
  solo es aproximada; el manual mismo lo advierte en la nota 3.
- Apéndice C: `readPower()` guarda en `temp` y regresa `pwr` (NameError oculto por el `except` → siempre `None`)
  y no toma `[0]` de `struct.unpack`.
- Apéndice B: falta `;` tras `Serial.write(buffer)`, el prototipo de `i2c_request_handler(int)` no coincide con la
  definición sin parámetros, y `sprintf("%.2f")` no funciona en AVR (imprime `?`) → se usa `dtostrf`.
- Apéndice A: configura `TRIAC` dos veces como salida y nunca el pin 13 (LED); el retardo con `delayMicroseconds()`
  en `loop()` se desfasa si el loop hace otra cosa → aquí se usa Timer1.
- Experimento 3 dice «modifique el código del punto 3»; debe ser del punto 2.
