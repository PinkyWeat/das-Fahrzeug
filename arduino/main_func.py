from machine import Pin, PWM
from utime import sleep
import select
import sys

# ======= Configuración de pines como PWM =======
VERDE_UNO = PWM(Pin(4))
VERDE_DOS = PWM(Pin(7))
AZUL_TRES = PWM(Pin(15))
AZUL_CUATRO = PWM(Pin(16))
NARANJA_UNO = PWM(Pin(20))
NARANJA_DOS = PWM(Pin(19))
VIOLETA_TRES = PWM(Pin(18))
VIOLETA_CUATRO = PWM(Pin(17))

# establezco PWM
frecuencia_pwm = 15
VERDE_UNO.freq(frecuencia_pwm)
VERDE_DOS.freq(frecuencia_pwm)
AZUL_TRES.freq(frecuencia_pwm)
AZUL_CUATRO.freq(frecuencia_pwm)
NARANJA_UNO.freq(frecuencia_pwm)
NARANJA_DOS.freq(frecuencia_pwm)
VIOLETA_TRES.freq(frecuencia_pwm)
VIOLETA_CUATRO.freq(frecuencia_pwm)

# establezco velocidad
def set_speed(pwm_pin, speed):
    pwm_pin.duty_u16(speed)

# controlan el movimiento
def avanzar(velocidad=36500):
    set_speed(VERDE_UNO, velocidad)
    set_speed(VERDE_DOS, 0)
    set_speed(AZUL_TRES, velocidad)
    set_speed(AZUL_CUATRO, 0)
    set_speed(NARANJA_UNO, velocidad)
    set_speed(NARANJA_DOS, 0)
    set_speed(VIOLETA_TRES, velocidad)
    set_speed(VIOLETA_CUATRO, 0)

def retroceder(velocidad=36500):
    set_speed(VERDE_UNO, 0)
    set_speed(VERDE_DOS, velocidad)
    set_speed(AZUL_TRES, 0)
    set_speed(AZUL_CUATRO, velocidad)
    set_speed(NARANJA_UNO, 0)
    set_speed(NARANJA_DOS, velocidad)
    set_speed(VIOLETA_TRES, 0)
    set_speed(VIOLETA_CUATRO, velocidad)

def detener():
    set_speed(VERDE_UNO, 0)
    set_speed(VERDE_DOS, 0)
    set_speed(AZUL_TRES, 0)
    set_speed(AZUL_CUATRO, 0)
    set_speed(NARANJA_UNO, 0)
    set_speed(NARANJA_DOS, 0)
    set_speed(VIOLETA_TRES, 0)
    set_speed(VIOLETA_CUATRO, 0)

# leo el comando desde Raspberry Pi
while True:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        comando = sys.stdin.read(1)  # Leer un caracter (comando)
        
        if comando == 'A':
            avanzar()
        elif comando == 'R':
            retroceder()
        elif comando == 'S':
            detener()
        else:
            print("cmd not recognized")

