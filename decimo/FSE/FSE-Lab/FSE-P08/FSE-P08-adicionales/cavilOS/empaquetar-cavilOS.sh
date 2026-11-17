#!/usr/bin/env bash
# empaquetar-cavilOS.sh - Prepara el paquete para Enzo en el escritorio.
# Uso:  bash empaquetar-cavilOS.sh                       (apellidos: Ortega Valdes Luna)
#       bash empaquetar-cavilOS.sh Ortega Valdez Said    (apellidos distintos)
set -euo pipefail

BR="${BR:-$HOME/myPiLinux/buildroot-2025.02}"
if   [ -d "$HOME/Desktop" ];   then DESK="$HOME/Desktop"
elif [ -d "$HOME/Escritorio" ]; then DESK="$HOME/Escritorio"
else echo "No encontre el escritorio (~/Desktop ni ~/Escritorio)"; exit 1; fi
OUT="$DESK/cavilOS-para-Enzo"

[ -d "$BR" ] || { echo "No existe $BR"; exit 1; }
command -v zip >/dev/null || { echo "Falta zip: sudo apt install -y zip"; exit 1; }

if [ "$#" -eq 3 ]; then SUR="\"$1\", \"$2\", \"$3\""; else SUR='"Ortega", "Valdes", "Luna"'; fi
echo ">> Apellidos de la marquesina: $SUR"

mkdir -p "$OUT"

# 1) test.py (con los apellidos elegidos) y LEEME.md
cat > "$OUT/test.py" <<'EOF_TEST_PY'
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
EOF_TEST_PY
sed -i "s/^SURNAMES = .*/SURNAMES = [$SUR]/" "$OUT/test.py"
grep '^SURNAMES' "$OUT/test.py"
python3 -m py_compile "$OUT/test.py" && rm -rf "$OUT/__pycache__"

cat > "$OUT/LEEME.md" <<'EOF_LEEME'
# Práctica 8 – cavilOS (Linux embebido con Buildroot) – paquete para la brigada

Contenido de este paquete
- `cavilOS.zip` (se manda aparte): imagen lista para grabar (`sdcard.img`).
- `cavilOS-fuentes.zip` (este): configuración de Buildroot para reconstruirla o modificarla.

## A) Solo probar la imagen (sin compilar)
1. Descomprime `cavilOS.zip` y verifica el hash: `sha256sum sdcard.img` (debe coincidir con el que te pasó Rafael).
2. Graba en una microSD de 1 GB o más (esto borra la tarjeta):
   - Balena Etcher, o
   - `lsblk` para identificar el disco y luego
     `sudo dd if=sdcard.img of=/dev/<disco> bs=10M status=progress conv=fsync && sync`
3. Conecta el circuito de la Práctica 7 (LCD con Pico W en 0x0A, SDA = pin 3, SCL = pin 5) y una pantalla HDMI. Enciende.
4. Debe verse el logo cavilOS; en el LCD, la marquesina de apellidos (línea 1) y la temperatura (línea 2).
   Usuario `pi`, contraseña `raspberry` (root también `raspberry`).
5. Validación sin hardware: `uname -r` (6.6.28-v8), `lsmod | grep -E "i2c|w1"`, `i2cdetect -y 1`, `python3 /home/pi/test.py`.

## B) Reconstruir o modificar (requiere Linux tipo Debian/Ubuntu, 20 GiB libres)
1. Dependencias:
   `sudo apt install -y git bc bison flex libssl-dev make libc6-dev libncurses5-dev build-essential crossbuild-essential-arm64 crossbuild-essential-armhf zip`
2. Descarga Buildroot:
   `mkdir -p ~/myPiLinux && cd ~/myPiLinux && wget https://buildroot.org/downloads/buildroot-2025.02.tar.xz && tar xf buildroot-2025.02.tar.xz && cd buildroot-2025.02`
3. Aplica las fuentes (sobre la raíz de Buildroot):
   `unzip -o ~/Downloads/cavilOS-fuentes.zip`
   Esto crea `.config`, `board/raspberrypi/...` (overlay, parche del logo, logo.png, users.txt, config.txt, cmdline.txt) y `package/python-smbus2/`.
4. Registra el paquete smbus2 (una sola vez):
   `sed -i '/package\/python-smbus-cffi\/Config.in/a source "package/python-smbus2/Config.in"' package/Config.in`
5. Normaliza la configuración: `make olddefconfig`
6. Compila (tarda de 90 min a 4 h la primera vez):
   `make HOSTCC=gcc-14 HOSTCXX=g++-14 2>&1 | tee build.log`
   (Si tu GCC es anterior a la versión 15 puedes omitir `HOSTCC`/`HOSTCXX`. Con GCC 15 `host-m4` no compila.
   Para tener gcc-14: `sudo apt install gcc-14 g++-14`.)
7. La imagen queda en `output/images/sdcard.img`.

## C) Cambios frecuentes (sin recompilar todo)
- Apellidos o lógica del LCD: editar `board/raspberrypi/rootfs-overlay/home/pi/test.py` y ejecutar `make HOSTCC=gcc-14 HOSTCXX=g++-14` (minutos).
- Cambios a `config_4_64bit.txt`: además hay que ejecutar antes
  `make HOSTCC=gcc-14 HOSTCXX=g++-14 rpi-firmware-reinstall`
  (si no, Buildroot conserva el config.txt viejo en la imagen).
- Cambiar el logo: reemplazar `board/raspberrypi/logo.png` y ejecutar `make HOSTCC=gcc-14 HOSTCXX=g++-14 linux-reconfigure` y después `make ...`.
- Probar un cambio sin regrabar toda la tarjeta: montar la partición 2 (`rootfs`) y copiar el archivo, p. ej.
  `sudo mount /dev/<disco>p2 /mnt && sudo cp test.py /mnt/home/pi/test.py && sudo umount /mnt`.

## D) Qué hace el sistema
- Arranque con logo personalizado centrado (parche `000-center-logo.patch`, `quiet loglevel=3`).
- `S02modules` carga `i2c-bcm2835`, `i2c-dev`, `w1-gpio`, `w1-therm`; `S10i2cperms` da permisos de I2C al grupo `i2c`; `S99autostart` ejecuta `/home/pi/start.sh` como usuario `pi`.
- `test.py` detecta el LCD por I2C (0x0A = Pico que emula el PCF8574 y entrega la temperatura del LM35; 0x27/0x3F = backpack PCF8574 con DS18B20 en GPIO4) y hace la marquesina de apellidos con temperatura.

## E) Pendiente
- Video de evidencia: arranque (logo) + LCD con marquesina y temperatura (experimentos 1, 2, 3 y 4).
- Reporte en inglés, por brigada, con el formato de los anteriores (header solo en la primera página, Arial 12, justificado, márgenes 2.5 cm, sangría 1 cm, sin portada) y `19-OEPR-L08-adicionales.zip`.
- Experimento 5 (kiosco con video/fotos, +10): no se hizo; requeriría ffmpeg sin X en la imagen y una compilación larga.
EOF_LEEME

# 2) Instalar test.py en el overlay de Buildroot
DEST="$BR/board/raspberrypi/rootfs-overlay/home/pi/test.py"
[ -f "$DEST" ] && cp "$DEST" "$DEST.bak-$(date +%H%M%S)" || true
cp "$OUT/test.py" "$DEST"

# 3) Recompilar (incremental, minutos)
cd "$BR"
echo ">> make (esto tarda unos minutos)..."
make HOSTCC=gcc-14 HOSTCXX=g++-14 2>&1 | tee "$HOME/make-empaquetar.log" | tail -8
[ -f output/images/sdcard.img ] || { echo "ERROR: no se genero sdcard.img (ver ~/make-empaquetar.log)"; exit 1; }
if [ "$(grep -c PICO_ADDR output/target/home/pi/test.py)" -lt 1 ]; then
  echo "ERROR: la imagen no tiene el test.py nuevo"; exit 1
fi

# 4) Zip de la imagen + hash + logo
rm -f "$OUT/cavilOS.zip"
( cd output/images && zip -9 "$OUT/cavilOS.zip" sdcard.img && sha256sum sdcard.img > "$OUT/hash.txt" )
cp board/raspberrypi/logo.png "$OUT/logo.png"

echo; echo "=== LISTO: $OUT ==="
ls -lh "$OUT"
echo; cat "$OUT/hash.txt"
