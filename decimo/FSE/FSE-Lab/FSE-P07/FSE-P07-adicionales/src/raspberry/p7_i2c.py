"""Comunicacion I2C con el Arduino de la Practica 7 y calculos de potencia.

Corrige los dos errores de readPower() del Apendice C del manual: guardaba el
resultado en `temp` pero devolvia `pwr` (NameError, que el `except` convertia
siempre en None) y no tomaba el elemento [0] de la tupla de struct.unpack.
"""
import math
import struct

SLAVE_ADDR = 0x0A
LINE_FREQ_NOMINAL = 60.0  # Hz, red de CU/Mexico

_bus = None


def _i2c():
    global _bus
    if _bus is None:
        import smbus2  # solo existe en la Raspberry Pi
        _bus = smbus2.SMBus(1)
    return _bus


def write_power(pct):
    """Envia la potencia solicitada (0-100 %) como float little-endian."""
    import smbus2
    data = struct.pack('<f', float(pct))
    _i2c().i2c_rdwr(smbus2.i2c_msg.write(SLAVE_ADDR, data))


def read_status():
    """Lee los 12 bytes del Arduino: potencia pedida, retardo y semiperiodo."""
    import smbus2
    msg = smbus2.i2c_msg.read(SLAVE_ADDR, 12)
    _i2c().i2c_rdwr(msg)
    requested, delay_ms, half_ms = struct.unpack('<3f', bytes(list(msg)))
    return describe(requested, delay_ms, half_ms)


def describe(requested, delay_ms, half_ms):
    """Convierte el retardo de disparo en potencia real (Ecs. 3 y 11 del manual)."""
    if half_ms <= 0 or half_ms > 20:          # sin cruces por cero detectados
        half_ms = 1000.0 / (2 * LINE_FREQ_NOMINAL)
    freq = 1000.0 / (2 * half_ms)
    if requested <= 0.5 or delay_ms <= 0:      # lampara apagada
        alpha = math.pi
    else:
        alpha = min(math.pi, math.pi * delay_ms / half_ms)   # alpha = w t
    p_frac = 1 - alpha / math.pi + math.sin(2 * alpha) / (2 * math.pi)
    p_frac = max(0.0, p_frac)
    return {
        'requested': requested,          # % que pidio el usuario (escala de la Tabla 1)
        'delay_ms': delay_ms,            # retardo aplicado tras el cruce por cero
        'half_period_ms': half_ms,
        'freq_hz': freq,
        'alpha_deg': math.degrees(alpha),
        'power_pct': 100 * p_frac,       # P/Pmax para carga resistiva (Ec. 3)
        'vo_vrms_pct': 100 * math.sqrt(p_frac),   # Vo/Vrms (Ecs. 6 y 11)
    }
