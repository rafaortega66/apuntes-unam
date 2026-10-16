# Experimento 3: marquesina de DERECHA A IZQUIERDA con velocidad variable
# El usuario define, por teclado, el tiempo de espera entre cada paso.

# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa la función sleep del módulo time
from time import sleep

# Desactivar advertencias (warnings)
GPIO.setwarnings(False)

# Configurar la librería para usar el número de pin (BOARD)
GPIO.setmode(GPIO.BOARD)

# Definir los 7 pines de la Raspberry Pi conectados al ULN2003
# El orden físico de la fila es: LED1 -> pin 12 (izquierda) ... LED7 -> pin 32 (derecha)
pines_leds = [12, 16, 18, 22, 24, 26, 32]

# Configurar la lista de pines como salida y habilitar en bajo
GPIO.setup(pines_leds, GPIO.OUT, initial=GPIO.LOW)

# Pedir al usuario el tiempo de espera entre pasos (una sola vez, al inicio)
espera = float(input("Tiempo de espera entre pasos en segundos (ej. 0.1): "))

try:
    # Bucle infinito: la marquesina se repite de manera continua
    while True:
        # Recorre la fila desde el ÚLTIMO LED (derecha, pin 32) hasta el PRIMERO (izquierda, pin 12)
        # range(6, -1, -1) genera los índices 6,5,4,3,2,1,0 -> movimiento de derecha a izquierda
        for i in range(len(pines_leds) - 1, -1, -1):
            GPIO.output(pines_leds[i], GPIO.HIGH)  # Enciende el LED actual
            sleep(espera)                          # Espera el tiempo indicado por el usuario
            GPIO.output(pines_leds[i], GPIO.LOW)   # Apaga el LED actual antes de pasar al siguiente

except KeyboardInterrupt:
    # Reinicia los puertos GPIO (cambian de salida a entrada) al detener el programa
    GPIO.cleanup()
