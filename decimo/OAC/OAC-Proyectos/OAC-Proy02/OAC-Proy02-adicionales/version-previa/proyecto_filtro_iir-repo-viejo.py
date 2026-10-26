# Proyecto: Filtro digital IIR de 2.º orden (pasabajas) en ensamblador con la FPU
# Raspberry Pi Pico 2 (RP2350). Salida para el Plotter de Thonny (Ver > Plotter).
#
# y[k] = a0 x[k] + a1 x[k-1] + a2 x[k-2] - b1 y[k-1] - b2 y[k-2]
# Diseño: H(s) = w0^2 / (s^2 + 2 z w0 s + w0^2), discretizado por transformada
# bilineal s = (2/Ts)(1 - z^-1)/(1 + z^-1).
from array import array
import math
import time

TS = 0.05            # tiempo de muestreo [s]  -> fs = 20 Hz, Nyquist = 10 Hz
F0 = 1.0             # frecuencia de corte [Hz] (debe ser < 10 Hz)
ZETA = 0.707         # amortiguamiento (0.707 = Butterworth)
MEDIO_PERIODO = 40   # muestras por semiciclo de la onda cuadrada (2 s)
RUIDO = False        # True: agrega ruido a la entrada para ver el filtrado

assert F0 < 1 / (2 * TS), "F0 debe ser menor que la frecuencia de Nyquist"

def coeficientes(ts, f0, zeta):
    w0 = 2 * math.pi * f0
    k = 2 / ts
    d = k * k + 2 * zeta * w0 * k + w0 * w0
    a0 = w0 * w0 / d
    a1 = 2 * w0 * w0 / d
    a2 = w0 * w0 / d
    b1 = (2 * w0 * w0 - 2 * k * k) / d
    b2 = (k * k - 2 * zeta * w0 * k + w0 * w0) / d
    return a0, a1, a2, b1, b2

C = array('f', coeficientes(TS, F0, ZETA))   # a0, a1, a2, b1, b2
U = array('f', [0.0, 0.0, 0.0])              # x[k], x[k-1], x[k-2]
Y = array('f', [0.0, 0.0, 0.0])              # y[k], y[k-1], y[k-2]

# r0 -> U, r1 -> Y, r2 -> C.  Sin ciclos: una muestra por llamada.
@micropython.asm_thumb
def iir(r0, r1, r2):
    vldr(s0, [r0, 0])     # x[k]
    vldr(s1, [r0, 4])     # x[k-1]
    vldr(s2, [r0, 8])     # x[k-2]
    vldr(s3, [r1, 4])     # y[k-1]
    vldr(s4, [r1, 8])     # y[k-2]
    vldr(s5, [r2, 0])     # a0
    vldr(s6, [r2, 4])     # a1
    vldr(s7, [r2, 8])     # a2
    vldr(s8, [r2, 12])    # b1
    vldr(s9, [r2, 16])    # b2
    vmul(s10, s0, s5)     # a0 x[k]
    vmul(s11, s1, s6)     # a1 x[k-1]
    vmul(s12, s2, s7)     # a2 x[k-2]
    vmul(s13, s3, s8)     # b1 y[k-1]
    vmul(s14, s4, s9)     # b2 y[k-2]
    vadd(s10, s10, s11)
    vadd(s10, s10, s12)
    vsub(s10, s10, s13)
    vsub(s10, s10, s14)   # s10 = y[k]
    vstr(s10, [r1, 0])    # y[k]
    vstr(s1, [r0, 8])     # x[k-2] <- x[k-1]
    vstr(s0, [r0, 4])     # x[k-1] <- x[k]
    vstr(s3, [r1, 8])     # y[k-2] <- y[k-1]
    vstr(s10, [r1, 4])    # y[k-1] <- y[k]

def reiniciar():
    for i in range(3):
        U[i] = 0.0
        Y[i] = 0.0

def filtrar(x):
    U[0] = x              # escribe la muestra en el arreglo (no reemplazar U)
    iir(U, Y, C)
    return Y[0]

# ---------- Prueba: respuesta al escalón, asm vs Python ----------
print("Coeficientes  a0={:.6f} a1={:.6f} a2={:.6f} b1={:.6f} b2={:.6f}".format(*C))
reiniciar()
xr = [0.0, 0.0]; yr = [0.0, 0.0]
a0, a1, a2, b1, b2 = C
err_max = 0.0
for k in range(100):
    y = filtrar(1.0)
    y_ref = a0 * 1.0 + a1 * xr[0] + a2 * xr[1] - b1 * yr[0] - b2 * yr[1]
    xr = [1.0, xr[0]]; yr = [y_ref, yr[0]]
    err_max = max(err_max, abs(y - y_ref))
    if k in (0, 1, 2, 5, 10, 20, 50, 99):
        print("k={:>3}  y_asm={:.6f}  y_python={:.6f}".format(k, y, y_ref))
print("Error maximo asm vs Python: {:.2e}".format(err_max))
print("Valor final (ganancia DC esperada = 1.0): {:.6f}".format(y))
time.sleep(3)

# ---------- Demostración: onda cuadrada para el Plotter de Thonny ----------
if RUIDO:
    import random
reiniciar()
k = 0
while True:
    x = 1.0 if (k // MEDIO_PERIODO) % 2 == 0 else 0.0
    if RUIDO:
        x += (random.random() - 0.5) * 0.4
    y = filtrar(x)
    print(x, y)           # dos números por línea: entrada y salida
    time.sleep(TS)
    k += 1
