#!/usr/bin/env python3
"""Experimento 1: controlar el brillo del foco tecleando 0-100 % en la consola."""
import p7_i2c


def main():
    print("Potencia del foco (0-100 %). Ctrl+C para salir.")
    while True:
        try:
            txt = input("Power? ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        try:
            pwr = float(txt)
        except ValueError:
            print("\tInvalid!")
            continue
        if not 0 <= pwr <= 100:
            print("\tInvalid!")
            continue
        try:
            p7_i2c.write_power(pwr)
            st = p7_i2c.read_status()
            print("\tPower set to {:.1f} %".format(st['requested']))
        except OSError as e:          # Arduino desconectado o sin responder
            print("\tI2C error:", e)


if __name__ == '__main__':
    main()
