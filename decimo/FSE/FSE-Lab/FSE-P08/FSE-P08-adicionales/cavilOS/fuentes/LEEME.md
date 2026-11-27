# Fuentes de Buildroot 2025.02 para cavilOS

Copia de los archivos propios del árbol de Buildroot (ver `../LEEME.md` para compilar).

- `buildroot.config` → copiar como `.config` en la raíz de Buildroot.
- `board/raspberrypi/` → copiar a `board/raspberrypi/` (`raspberrypi4-64` es un enlace a esa carpeta).
- `package/python-smbus2/` → copiar a `package/` y registrarlo en `package/Config.in`.
- `p08-logo.sh` → script que activa el logo de arranque y reconstruye la imagen.
