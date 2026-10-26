# Proyecto: sen(x) y cos(x) por series de Taylor + Calculadora con la FPU
# Raspberry Pi Pico 2 (RP2350). No corre en Pico 1 (sin FPU).
# Toda la aritmetica se hace en ensamblador (MicroPython inline Thumb):
#   - sen(x) y cos(x): series de Taylor evaluadas con Horner, solo multiplicaciones y sumas
#   - Suma, resta, multiplicacion, division y raiz: instrucciones de la FPU
#   - tan(x) = sen(x) / cos(x) con VDIV
# Python solo maneja el menu, la lectura de datos y la impresion.
from array import array
import math

# ---------------- Operaciones básicas en la FPU ----------------
# r0 -> array('f', [a, b, resultado]);  r1 = operación
#   0: a + b   1: a - b   2: a * b   3: a / b   4: raíz(a)
@micropython.asm_thumb
def fpu(r0, r1):
    vldr(s0, [r0, 0])     # s0 = a
    vldr(s1, [r0, 4])     # s1 = b
    cmp(r1, 0)
    beq(SUMA)
    cmp(r1, 1)
    beq(RESTA)
    cmp(r1, 2)
    beq(MULT)
    cmp(r1, 3)
    beq(DIVI)
    vsqrt(s2, s0)         # 4: raíz cuadrada
    b(FIN)
    label(SUMA)
    vadd(s2, s0, s1)
    b(FIN)
    label(RESTA)
    vsub(s2, s0, s1)
    b(FIN)
    label(MULT)
    vmul(s2, s0, s1)
    b(FIN)
    label(DIVI)
    vdiv(s2, s0, s1)
    label(FIN)
    vstr(s2, [r0, 8])     # resultado

# ---------------- sen(x) y cos(x) por Taylor (metodo de Horner) ----------------
# sen(x) = x(1 - u/3! + u^2/5! - u^3/7! + u^4/9!)        con u = x^2
# cos(x) =    1 - u/2! + u^2/4! - u^3/6! + u^4/8!
# Horner: el polinomio se evalua de adentro hacia afuera, t = t*u + c,
# asi se usan 5 multiplicaciones por funcion en lugar de calcular cada potencia.
# Coeficientes con signo = reciprocos de los factoriales (precalculados, sin dividir).
K = array('f', [1.0, -1 / 6, 1 / 120, -1 / 5040, 1 / 362880,      # seno:   offsets 0..16
                1.0, -1 / 2, 1 / 24, -1 / 720, 1 / 40320])        # coseno: offsets 20..36

# r0 -> array('f',[x]), r1 -> array('f',[sen, cos]), r2 -> K
@micropython.asm_thumb
def taylor(r0, r1, r2):
    vldr(s0, [r0, 0])     # s0 = x
    vmul(s1, s0, s0)      # s1 = u = x^2
    # ---- seno ----
    vldr(s2, [r2, 16])    # t = 1/9!
    vldr(s3, [r2, 12])
    vmul(s2, s2, s1)
    vadd(s2, s2, s3)      # t = t*u - 1/7!
    vldr(s3, [r2, 8])
    vmul(s2, s2, s1)
    vadd(s2, s2, s3)      # t = t*u + 1/5!
    vldr(s3, [r2, 4])
    vmul(s2, s2, s1)
    vadd(s2, s2, s3)      # t = t*u - 1/3!
    vldr(s3, [r2, 0])
    vmul(s2, s2, s1)
    vadd(s2, s2, s3)      # t = t*u + 1
    vmul(s2, s2, s0)      # sen = t*x
    vstr(s2, [r1, 0])
    # ---- coseno ----
    vldr(s2, [r2, 36])    # t = 1/8!
    vldr(s3, [r2, 32])
    vmul(s2, s2, s1)
    vadd(s2, s2, s3)      # t = t*u - 1/6!
    vldr(s3, [r2, 28])
    vmul(s2, s2, s1)
    vadd(s2, s2, s3)      # t = t*u + 1/4!
    vldr(s3, [r2, 24])
    vmul(s2, s2, s1)
    vadd(s2, s2, s3)      # t = t*u - 1/2!
    vldr(s3, [r2, 20])
    vmul(s2, s2, s1)
    vadd(s2, s2, s3)      # cos = t*u + 1
    vstr(s2, [r1, 4])

MEDIO_PI = math.pi / 2

def reducir(x):
    # x = n*(pi/2) + r, con r en [-pi/4, pi/4]: ahi la serie es practicamente exacta.
    # q = n mod 4 indica el cuadrante para acomodar sen y cos al final.
    n = math.floor(x / MEDIO_PI + 0.5)
    r = x - n * MEDIO_PI
    return r, int(n) % 4

# ---------------- Funciones de la calculadora ----------------
_ab = array('f', [0.0, 0.0, 0.0])
_x = array('f', [0.0])
_sc = array('f', [0.0, 0.0])

def op(a, b, codigo):
    _ab[0] = a
    _ab[1] = b
    fpu(_ab, codigo)
    return _ab[2]

def sen_cos(x):
    r, q = reducir(x)
    _x[0] = r
    taylor(_x, _sc, K)
    s, c = _sc[0], _sc[1]
    if q == 1:
        s, c = c, -s      # sen(r + 90) = cos(r),   cos(r + 90) = -sen(r)
    elif q == 2:
        s, c = -s, -c     # sen(r + 180) = -sen(r), cos(r + 180) = -cos(r)
    elif q == 3:
        s, c = -c, s      # sen(r + 270) = -cos(r), cos(r + 270) = sen(r)
    return s + 0.0, c + 0.0   # + 0.0 evita imprimir "-0.0000000"

def leer(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("  Escribe un numero (usa punto decimal)")

# ---------------- Prueba clasica: sen(45) = cos(45) ----------------
# A 45 grados (pi/4 rad) el triangulo rectangulo es isosceles: los dos catetos
# miden lo mismo, asi que sen(45) = cos(45) = 1/raiz(2) = raiz(2)/2 = 0.7071068.
# Todas las cuentas de esta prueba se hacen en la FPU (ensamblador).
def prueba_clasica():
    x = math.radians(45)
    s, c = sen_cos(x)
    r2_2 = op(op(2.0, 0.0, 4), 2.0, 3)              # raiz(2) / 2   (VSQRT y VDIV)
    dif = op(s, c, 1)                                # sen - cos     (VSUB)
    tan = op(s, c, 3)                                # sen / cos     (VDIV)
    pit = op(op(s, s, 2), op(c, c, 2), 0)            # sen^2 + cos^2 (VMUL y VADD)
    print()
    print("=== Prueba clasica: sen(45) = cos(45) ===")
    print("  45 grados = pi/4 rad = {:.7f} rad".format(x))
    print("  sen(45)           = {:.7f}   (serie de Taylor, ensamblador)".format(s))
    print("  cos(45)           = {:.7f}   (serie de Taylor, ensamblador)".format(c))
    print("  raiz(2)/2         = {:.7f}   (valor exacto, VSQRT de la FPU)".format(r2_2))
    print("  sen(45) - cos(45) = {:.1e}     (0 hasta la precision de 32 bits, ~1e-7)".format(abs(dif)))
    print("  tan(45) = sen/cos = {:.6f}".format(tan))
    print("  sen^2 + cos^2     = {:.6f}".format(pit))

# ---------------- Prueba: tabla de sen y cos ----------------
print("=== sen(x) y cos(x) por Taylor en ensamblador (FPU) ===")
print("{:>6} {:>11} {:>11} {:>9} {:>11} {:>11} {:>9}".format(
    "grados", "sen asm", "math.sin", "error", "cos asm", "math.cos", "error"))
for g in (0, 30, 45, 60, 90, 120, 180, 225, 270, 330, 360, -45, -150):
    x = math.radians(g)
    s, c = sen_cos(x)
    print("{:>6} {:>11.7f} {:>11.7f} {:>9.1e} {:>11.7f} {:>11.7f} {:>9.1e}".format(
        g, s, math.sin(x), abs(s - math.sin(x)), c, math.cos(x), abs(c - math.cos(x))))

prueba_clasica()

# ---------------- Calculadora ----------------
grados = True

MENU = """
========= CALCULADORA FPU - Raspberry Pi Pico 2 =========
 1) Suma        2) Resta       3) Multiplicacion
 4) Division    5) Raiz cuadrada
 6) sen(x)      7) cos(x)      8) tan(x)
 9) Cambiar unidades de angulo (actual: {})
10) Prueba clasica: sen(45) = cos(45)
 0) Salir
========================================================="""

while True:
    print(MENU.format("grados" if grados else "radianes"))
    opcion = input("Opcion: ").strip()

    if opcion == "0":
        print("Fin.")
        break

    elif opcion in ("1", "2", "3", "4"):
        a = leer("a = ")
        b = leer("b = ")
        simbolo = "+-*/"[int(opcion) - 1]
        if opcion == "4" and b == 0:
            print("  Error: division entre cero")
            continue
        r = op(a, b, int(opcion) - 1)
        print("  {} {} {} = {:.7g}".format(a, simbolo, b, r))

    elif opcion == "5":
        a = leer("a = ")
        if a < 0:
            print("  Error: la FPU no admite raiz de negativos")
            continue
        print("  raiz({}) = {:.7g}".format(a, op(a, 0.0, 4)))

    elif opcion in ("6", "7", "8"):
        ang = leer("x ({}) = ".format("grados" if grados else "radianes"))
        x = math.radians(ang) if grados else ang
        s, c = sen_cos(x)
        if opcion == "6":
            print("  sen({}) = {:.7f}".format(ang, s))
        elif opcion == "7":
            print("  cos({}) = {:.7f}".format(ang, c))
        else:
            if abs(c) < 1e-4:
                print("  tan({}) = indefinida (cos = 0)".format(ang))
            else:
                print("  tan({}) = {:.6f}".format(ang, op(s, c, 3)))

    elif opcion == "10":
        prueba_clasica()

    elif opcion == "9":
        grados = not grados
        print("  Ahora en", "grados" if grados else "radianes")

    else:
        print("  Opcion no valida")
