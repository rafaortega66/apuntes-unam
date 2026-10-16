# Experimento 5: efecto "fade" (encendido/apagado gradual) mediante PWM por software
#
# Comportamiento de cada ciclo:
#   1) Encendido gradual (fade in) del LED durante 1 segundo, de duty cycle 0 a 100.
#   2) Permanece a máxima potencia (duty cycle 100) durante 0.5 segundos.
#   3) Apagado gradual (fade out) del LED durante 1 segundo, de duty cycle 100 a 0.
# El ciclo se repite de manera continua hasta detener el programa con Ctrl+C.

# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa la función sleep del módulo time
from time import sleep

# Desactivar advertencias (warnings)
GPIO.setwarnings(False)

# Configurar la librería para usar el número de pin (BOARD)
GPIO.setmode(GPIO.BOARD)

# Se elige un solo LED de la fila para el efecto: LED1 -> pin físico 12
LED = 12

# Configurar el pin como salida y habilitar en bajo (LED apagado)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# Crear el objeto PWM sobre el pin del LED a 100 Hz (frecuencia alta -> sin parpadeo visible)
pwm = GPIO.PWM(LED, 100)

# Parámetros del efecto gradual
PASOS = 100                 # número de incrementos de duty cycle en cada rampa
INCREMENTO = 100 / PASOS    # tamaño de cada incremento de duty cycle (1 en este caso)
T_RAMPA = 1.0               # duración de cada rampa (subida y bajada) en segundos
PAUSA = T_RAMPA / PASOS     # pausa entre incrementos -> 100 pasos * 0.01 s = 1 segundo
T_MAXIMO = 0.5             # tiempo a máxima potencia (duty cycle 100) en segundos

# Iniciar el PWM con duty cycle 0 (LED apagado)
pwm.start(0)

try:
    # Bucle infinito: el efecto de fade in / máximo / fade out se repite de forma continua
    while True:

        # ----- 1) Encendido gradual (fade in): duty cycle de 0 a 100 en 1 segundo -----
        for paso in range(1, PASOS + 1):
            duty = paso * INCREMENTO         # duty cycle actual: 1, 2, ..., 100
            pwm.ChangeDutyCycle(duty)        # aplicar el nuevo duty cycle al LED
            sleep(PAUSA)                     # pausa corta entre incrementos

        # ----- 2) Permanecer a máxima potencia (duty cycle 100) durante 0.5 segundos -----
        pwm.ChangeDutyCycle(100)             # asegurar el LED a máxima potencia
        sleep(T_MAXIMO)                      # mantener el brillo máximo medio segundo

        # ----- 3) Apagado gradual (fade out): duty cycle de 100 a 0 en 1 segundo -----
        for paso in range(PASOS - 1, -1, -1):
            duty = paso * INCREMENTO         # duty cycle actual: 99, 98, ..., 0
            pwm.ChangeDutyCycle(duty)        # aplicar el nuevo duty cycle al LED
            sleep(PAUSA)                     # pausa corta entre incrementos

except KeyboardInterrupt:
    # Detener el PWM antes de liberar los puertos
    pwm.stop()
    # Reinicia los puertos GPIO (cambian de salida a entrada) al detener el programa
    GPIO.cleanup()
