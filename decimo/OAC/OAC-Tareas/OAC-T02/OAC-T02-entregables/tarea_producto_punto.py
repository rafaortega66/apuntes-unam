# Tarea: Sumatoria de productos (producto punto) en ensamblador con la FPU
# Raspberry Pi Pico 2 (RP2350)
from array import array

# r0 -> data1 (array 'f'), r1 -> data2 (array 'f'), r2 -> res (array 'f', 1 elem), r3 -> N
@micropython.asm_thumb
def producto_punto(r0, r1, r2, r3):
    mov(r4, 0)
    vmov(s4, r4)          # acumulador s4 = 0.0 (bits en cero = 0.0 flotante)
    cmp(r3, 0)
    ble(FIN)              # N <= 0: no hay nada que sumar
    label(CICLO)
    vldr(s0, [r0, 0])     # s0 = data1[i]
    vldr(s1, [r1, 0])     # s1 = data2[i]
    vmul(s2, s0, s1)      # s2 = data1[i] * data2[i]
    vadd(s4, s4, s2)      # acumula
    add(r0, r0, 4)        # siguiente flotante: 4 bytes
    add(r1, r1, 4)
    sub(r3, r3, 1)        # N -= 1
    bgt(CICLO)            # repite mientras N > 0
    label(FIN)
    vstr(s4, [r2, 0])     # res = acumulador

def punto(a, b):
    if len(a) != len(b):
        raise ValueError("Los vectores deben tener la misma dimension")
    res = array('f', [0.0])
    producto_punto(a, b, res, len(a))
    return res[0]

# ---------- Pruebas ----------
casos = [
    ([1.0, 2.0], [3.0, 4.0]),                       # 11
    ([1.0, 2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0]),   # 40
    ([0.5, -1.5, 2.25], [4.0, 2.0, -1.0]),          # -3.25
    ([float(i) for i in range(1, 101)], [1.0] * 100),  # 5050
]
print("=== Producto punto en ensamblador (FPU) ===")
for a, b in casos:
    va, vb = array('f', a), array('f', b)
    r = punto(va, vb)
    ref = sum(x * y for x, y in zip(va, vb))
    print("N={:>3}  asm={:>12.4f}  python={:>12.4f}  {}".format(
        len(a), r, ref, "OK" if abs(r - ref) < 1e-3 * max(1, abs(ref)) else "ERROR"))

# ---------- Modo interactivo ----------
print()
def leer_vector(t):
    # acepta 1,2,3  (1,2,3)  [1, 2, 3]  o separados por espacios
    for c in "()[]":
        t = t.replace(c, " ")
    return [float(v) for v in t.replace(",", " ").split()]

print("=== Modo interactivo (Enter vacio para salir) ===")
while True:
    t1 = input("Vector 1 (ej. 1,2,3): ").strip()
    if not t1:
        break
    t2 = input("Vector 2 (misma dimension): ").strip()
    try:
        va = array('f', leer_vector(t1))
        vb = array('f', leer_vector(t2))
        print("  Producto punto (asm) = {:.4f}".format(punto(va, vb)))
    except ValueError as e:
        print("  Error:", e)
