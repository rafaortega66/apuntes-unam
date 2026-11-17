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
