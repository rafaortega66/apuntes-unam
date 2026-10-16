import RPi.GPIO as GPIO
from time import sleep

# Desactivar advertencias
GPIO.setwarnings(False)

# Configurar la librería para usar el número de pin físico (BOARD)
GPIO.setmode(GPIO.BOARD)

# Pines conectados a las entradas 1 a 7 del ULN2003, ordenados de izquierda a derecha
pines_leds = [12, 16, 18, 22, 24, 26, 32]

# Configurar todos los pines como salida y apagados inicialmente
GPIO.setup(pines_leds, GPIO.OUT, initial=GPIO.LOW)

try:
    while True: # Bucle infinito para mantener la marquesina continua
        # Bucle 'for each' en Python iterando sobre la lista de pines
        for pin in pines_leds:
            GPIO.output(pin, GPIO.HIGH) # Enciende el LED en la posición actual
            sleep(0.2)                  # Mantiene el LED encendido por 200ms
            GPIO.output(pin, GPIO.LOW)  # Apaga el LED antes de pasar al siguiente

except KeyboardInterrupt:
    # Reinicia los puertos GPIO al presionar Ctrl+C
    GPIO.cleanup()
