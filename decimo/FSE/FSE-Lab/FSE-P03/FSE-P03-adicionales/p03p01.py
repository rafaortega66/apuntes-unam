# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa la función sleep del módulo time
from time import sleep

# Desactivar advertencias (warnings)
GPIO.setwarnings(False)

# Configurar la librería para usar el número de pin (BOARD)
GPIO.setmode(GPIO.BOARD)

# Definir los 7 pines de la Raspberry Pi conectados al ULN2003
pines_leds = [12, 16, 18, 22, 24, 26, 32]

# Configurar la lista de pines como salida y habilitar en bajo
GPIO.setup(pines_leds, GPIO.OUT, initial=GPIO.LOW)

try:
    # Bucle infinito
    while True: 
        sleep(0.5)  # Espera 500ms
        GPIO.output(pines_leds, GPIO.HIGH) # Enciende todos los LEDs de la lista
        sleep(0.5)  # Espera 500ms
        GPIO.output(pines_leds, GPIO.LOW)  # Apaga todos los LEDs de la lista

except KeyboardInterrupt:
    # Reinicia los puertos GPIO (cambian de salida a entrada) al detener el programa
    GPIO.cleanup()