# Tarea: Raíz cuadrada en ensamblador (MicroPython inline Thumb)
# Raspberry Pi Pico 2 (RP2350). El método A también corre en Pico 1.
#   A) Entera por restas sucesivas de impares (registros de enteros)
#   B) Punto flotante con la instrucción VSQRT de la FPU
from array import array
import math

# ---------- Método A: restas de impares 1, 3, 5, 7, ... ----------
# r0 -> array('i', [N, raiz, residuo])
@micropython.asm_thumb
def raiz_entera(r0):
    ldr(r1, [r0, 0])      # r1 = N (se va reduciendo)
    mov(r2, 0)            # r2 = raiz (contador de restas)
    mov(r3, 1)            # r3 = impar actual
    label(CICLO)
    cmp(r1, r3)
    blt(FIN)              # si N < impar, termina
    sub(r1, r1, r3)       # N = N - impar
    add(r2, r2, 1)        # raiz += 1
    add(r3, r3, 2)        # siguiente impar
    b(CICLO)
    label(FIN)
    str(r2, [r0, 4])      # guarda raiz
    str(r1, [r0, 8])      # guarda residuo
    mov(r0, r2)           # también la regresa

# ---------- Método B: FPU, VSQRT ----------
# r0 -> array('f', [x]),  r1 -> array('f', [resultado])
@micropython.asm_thumb
def raiz_fpu(r0, r1):
    vldr(s0, [r0, 0])     # s0 = x
    vsqrt(s2, s0)         # s2 = sqrt(x)
    vstr(s2, [r1, 0])     # resultado

def sqrt_fpu(x):
    if x < 0:
        raise ValueError("No se admiten negativos en la FPU")
    entrada = array('f', [x])
    salida = array('f', [0.0])
    raiz_fpu(entrada, salida)
    return salida[0]

# ---------- Pruebas ----------
print("=== Metodo A: raiz entera por restas de impares ===")
print("{:>6} {:>6} {:>8}  {}".format("N", "raiz", "residuo", "OK"))
for n in (0, 1, 2, 25, 27, 80, 100, 1000, 65535):
    d = array('i', [n, 0, 0])
    raiz_entera(d)
    ok = d[1] * d[1] + d[2] == n and d[1] == int(math.sqrt(n))
    print("{:>6} {:>6} {:>8}  {}".format(n, d[1], d[2], "si" if ok else "NO"))

print()
print("=== Metodo B: VSQRT de la FPU ===")
print("{:>10} {:>12} {:>12} {:>10}".format("x", "asm", "math.sqrt", "error"))
for x in (0.0, 2.0, 25.0, 80.0, 0.25, 12345.678):
    r = sqrt_fpu(x)
    print("{:>10} {:>12.7f} {:>12.7f} {:>10.2e}".format(x, r, math.sqrt(x), abs(r - math.sqrt(x))))

# ---------- Modo interactivo ----------
print()
print("=== Modo interactivo (Enter vacio para salir) ===")
while True:
    t = input("Numero entero >= 0: ").strip()
    if not t:
        break
    try:
        n = int(t)
        if n < 0:
            raise ValueError
    except ValueError:
        print("  Escribe un entero no negativo")
        continue
    d = array('i', [n, 0, 0])
    raiz_entera(d)
    print("  Metodo A (restas de impares): raiz = {}, residuo = {}".format(d[1], d[2]))
    print("  Metodo B (VSQRT de la FPU):   {:.7f}".format(sqrt_fpu(float(n))))
