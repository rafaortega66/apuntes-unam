#!/usr/bin/env python3
# Practice 8 - 16x2 LCD marquee + temperature
#   Line 1: paternal surnames of the team, infinite left-scrolling marquee.
#   Line 2: temperature in degrees Celsius.
#
# The display is found automatically on the I2C bus:
#   0x0A     Raspberry Pi Pico W that emulates the PCF8574 adapter and also
#            returns the LM35 temperature as a little-endian float (Lab 7c).
#   0x27/0x3F  standard PCF8574 backpack; temperature from a DS18B20 (1-Wire).
import glob
import os
import struct
import threading
import time

from smbus2 import SMBus, i2c_msg

I2C_BUS = 1
CANDIDATES = (0x0A, 0x27, 0x3F)
PICO_ADDR = 0x0A
COLS = 16

SURNAMES = ["Ortega", "Valdez", "Said"]
DELAY = 0.30            # seconds between marquee shifts
TEMP_PERIOD = 2.0       # seconds between temperature readings
W1_PATTERN = os.environ.get("W1_PATTERN", "/sys/bus/w1/devices/28-*/w1_slave")

# PCF8574 bits: P0=RS P1=RW P2=EN P3=Backlight P4..P7=D4..D7
RS, EN, BL = 0x01, 0x04, 0x08
DEGREE = 0xDF           # degree symbol in the HD44780 ROM (A00)
STEP = 0.002            # the Pico polls the bus, so every byte needs 2 ms


class LCD:
    def __init__(self, bus, addr):
        self.bus, self.addr = bus, addr
        time.sleep(0.05)
        for b in (0x33, 0x32, 0x28, 0x0C, 0x06, 0x01):  # 4-bit init
            self._send(b, 0)
        time.sleep(0.005)

    def _write4(self, nibble, rs):
        data = (nibble & 0xF0) | BL | rs
        self.bus.write_byte(self.addr, data | EN)
        time.sleep(STEP)
        self.bus.write_byte(self.addr, data & ~EN & 0xFF)
        time.sleep(STEP)

    def _send(self, byte, rs):
        self._write4(byte & 0xF0, rs)
        self._write4((byte << 4) & 0xF0, rs)

    def text(self, line, s):
        self._send(0x80 | (0x00 if line == 0 else 0x40), 0)
        for ch in s.ljust(COLS)[:COLS]:
            self._send(ord(ch) if ord(ch) < 256 else 0x3F, RS)


def find_lcd(bus):
    """Return the first candidate address that acknowledges a write."""
    for addr in CANDIDATES:
        try:
            bus.write_byte(addr, BL)
            return addr
        except OSError:
            continue
    return None


def parse_w1(raw):
    """Parse the two-line w1_slave text; return degrees Celsius or None."""
    lines = raw.strip().splitlines()
    if len(lines) < 2 or not lines[0].rstrip().endswith("YES"):
        return None
    if "t=" not in lines[1]:
        return None
    milli = int(lines[1].split("t=")[1])
    if milli == 85000:      # power-on reset value, not a real measurement
        return None
    return milli / 1000.0


def read_pico(bus):
    """Read the 4-byte little-endian float the Pico returns (LM35)."""
    msg = i2c_msg.read(PICO_ADDR, 4)
    bus.i2c_rdwr(msg)
    value = struct.unpack("<f", bytes(list(msg)))[0]
    if value != value or not -55.0 <= value <= 150.0:   # NaN or out of range
        return None
    return value


class W1Reader(threading.Thread):
    """Reads the DS18B20 in the background (a conversion takes ~750 ms)."""

    def __init__(self):
        super().__init__(daemon=True)
        self.value = None

    def run(self):
        while True:
            try:
                paths = sorted(glob.glob(W1_PATTERN))
                if paths:
                    with open(paths[0]) as f:
                        self.value = parse_w1(f.read())
                else:
                    self.value = None
            except (OSError, ValueError):
                self.value = None
            time.sleep(TEMP_PERIOD)


def temp_line(value):
    if value is None:
        return "Temp: --.-" + chr(DEGREE) + "C"
    return "Temp: %.1f" % value + chr(DEGREE) + "C"


def run(bus, addr, w1):
    lcd = LCD(bus, addr)
    msg = " ".join(SURNAMES) + "   "
    loop = msg * 2 + msg[:COLS]
    pos = 0
    last = None
    value = None
    next_read = 0.0
    while True:
        now = time.monotonic()
        if now >= next_read:
            next_read = now + TEMP_PERIOD
            if addr == PICO_ADDR:
                try:
                    value = read_pico(bus)
                except (OSError, struct.error):
                    value = None
            else:
                value = w1.value
        lcd.text(0, loop[pos:pos + COLS])
        line2 = temp_line(value)
        if line2 != last:
            lcd.text(1, line2)
            last = line2
        pos = (pos + 1) % len(msg)
        time.sleep(DELAY)


def main():
    w1 = W1Reader()
    w1.start()
    while True:                     # keep retrying: hardware may come up late
        try:
            with SMBus(I2C_BUS) as bus:
                addr = find_lcd(bus)
                if addr is None:
                    time.sleep(2.0)
                    continue
                run(bus, addr, w1)
        except OSError:
            time.sleep(2.0)


if __name__ == "__main__":
    main()
