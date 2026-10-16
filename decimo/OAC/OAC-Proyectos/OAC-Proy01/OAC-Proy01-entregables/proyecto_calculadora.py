# Proyecto: Calculadora con la FPU de la Raspberry Pi Pico 2 (RP2350)
# Toda la aritmética se hace en ensamblador (MicroPython inline Thumb):
#   - Suma, resta, multiplicación, división y raíz: instrucciones de la FPU
#   - sen(x) y cos(x): series de Taylor, solo multiplicaciones (factoriales precalculados)
#   - tan(x) = sen(x) / cos(x) con VDIV
# Python solo maneja el menú, la lectura de datos y la impresión.
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

# ---------------- sen(x) y cos(x) por Taylor ----------------
# Recíprocos de factoriales: 1/0!, 1/2!, 1/3!, ..., 1/9!
K = array('f', [1.0, 1 / 2, 1 / 6, 1 / 24, 1 / 120,
                1 / 720, 1 / 5040, 1 / 40320, 1 / 362880])

# r0 -> array('f',[x]), r1 -> array('f',[sen, cos]), r2 -> K
@micropython.asm_thumb
def taylor(r0, r1, r2):
    vldr(s0, [r0, 0])     # s0 = x
    vmul(s1, s0, s0)      # x^2
    vmul(s2, s1, s0)      # x^3
    vmul(s3, s2, s0)      # x^4
    vmul(s4, s3, s0)      # x^5
    vmul(s5, s4, s0)      # x^6
    vmul(s6, s5, s0)      # x^7
    vmul(s7, s6, s0)      # x^8
    vmul(s8, s7, s0)      # x^9
    # sen(x) = x - x^3/3! + x^5/5! - x^7/7! + x^9/9!
    vldr(s10, [r2, 8])
    vmul(s11, s2, s10)
    vsub(s20, s0, s11)
    vldr(s10, [r2, 16])
    vmul(s11, s4, s10)
    vadd(s20, s20, s11)
    vldr(s10, [r2, 24])
    vmul(s11, s6, s10)
    vsub(s20, s20, s11)
    vldr(s10, [r2, 32])
    vmul(s11, s8, s10)
    vadd(s20, s20, s11)
    vstr(s20, [r1, 0])
    # cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + x^8/8!
    vldr(s21, [r2, 0])
    vldr(s10, [r2, 4])
    vmul(s11, s1, s10)
    vsub(s21, s21, s11)
    vldr(s10, [r2, 12])
    vmul(s11, s3, s10)
    vadd(s21, s21, s11)
    vldr(s10, [r2, 20])
    vmul(s11, s5, s10)
    vsub(s21, s21, s11)
    vldr(s10, [r2, 28])
    vmul(s11, s7, s10)
    vadd(s21, s21, s11)
    vstr(s21, [r1, 4])

def reducir(x):
    # Lleva x a [-pi/2, pi/2], donde la serie con pocos términos es precisa.
    x = math.fmod(x, 2 * math.pi)
    if x > math.pi:
        x -= 2 * math.pi
    elif x < -math.pi:
        x += 2 * math.pi
    signo_cos = 1.0
    if x > math.pi / 2:
        x, signo_cos = math.pi - x, -1.0
    elif x < -math.pi / 2:
        x, signo_cos = -math.pi - x, -1.0
    return x, signo_cos

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
    xr, signo_cos = reducir(x)
    _x[0] = xr
    taylor(_x, _sc, K)
    return _sc[0], signo_cos * _sc[1]

def leer(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("  Escribe un numero (usa punto decimal)")

grados = True

MENU = """
========= CALCULADORA FPU - Raspberry Pi Pico 2 =========
 1) Suma        2) Resta       3) Multiplicacion
 4) Division    5) Raiz cuadrada
 6) sen(x)      7) cos(x)      8) tan(x)
 9) Cambiar unidades de angulo (actual: {})
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
                print("  tan({}) = {:.7f}".format(ang, op(s, c, 3)))

    elif opcion == "9":
        grados = not grados
        print("  Ahora en", "grados" if grados else "radianes")

    else:
        print("  Opcion no valida")
