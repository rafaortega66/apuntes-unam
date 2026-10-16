# Experimento 4: marquesina tipo "rebote" (efecto ping-pong) con velocidad variable
# El LED encendido recorre la fila de un extremo a otro y regresa, sin encender
# dos veces seguidas el mismo LED de la orilla. El usuario define el tiempo de espera.

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

# Construir la secuencia de índices del recorrido de ida y vuelta:
#   ida    : 0,1,2,3,4,5,6
#   vuelta : 5,4,3,2,1        (se omiten los índices 6 y 0 para no repetir las orillas)
# El patrón completo 0..6..1 se repite y produce el efecto de rebote continuo.
ida = list(range(len(pines_leds)))          # 0,1,2,3,4,5,6
vuelta = list(range(len(pines_leds) - 2, 0, -1))  # 5,4,3,2,1
secuencia = ida + vuelta                     # recorrido completo sin repetir extremos

try:
    # Bucle infinito: el rebote se repite de manera continua
    while True:
        # Recorre cada índice de la secuencia de rebote
        for i in secuencia:
            GPIO.output(pines_leds[i], GPIO.HIGH)  # Enciende el LED actual
            sleep(espera)                          # Espera el tiempo indicado por el usuario
            GPIO.output(pines_leds[i], GPIO.LOW)   # Apaga el LED actual antes de pasar al siguiente

except KeyboardInterrupt:
    # Reinicia los puertos GPIO (cambian de salida a entrada) al detener el programa
    GPIO.cleanup()
