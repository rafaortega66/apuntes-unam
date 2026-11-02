#!/usr/bin/env python3
"""Experimento 2: mostrar la potencia real que modula el Arduino.

El Arduino reporta el retardo de disparo que realmente programo y el
semiperiodo de linea que mide entre cruces por cero. Con eso:
    alpha = pi * t_disparo / (T/2)
    P/Pmax = 1 - alpha/pi + sin(2 alpha)/(2 pi)        (Ec. 3 del manual)
"""
import p7_i2c

HEADER = "{:>8} {:>9} {:>8} {:>8} {:>9} {:>10}".format(
    "pedido%", "t_disp ms", "alpha°", "f Hz", "P real%", "Vo/Vrms%")


def show(st):
    print("{requested:8.1f} {delay_ms:9.3f} {alpha_deg:8.1f} {freq_hz:8.2f} "
          "{power_pct:9.1f} {vo_vrms_pct:10.1f}".format(**st))


def main():
    print("Potencia del foco (0-100 %). Enter vacio = releer. Ctrl+C para salir.")
    print(HEADER)
    while True:
        try:
            txt = input("Power? ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        try:
            if txt:
                pwr = float(txt)
                if not 0 <= pwr <= 100:
                    raise ValueError
                p7_i2c.write_power(pwr)
            show(p7_i2c.read_status())
        except ValueError:
            print("\tInvalid!")
        except OSError as e:
            print("\tI2C error:", e)


if __name__ == '__main__':
    main()
