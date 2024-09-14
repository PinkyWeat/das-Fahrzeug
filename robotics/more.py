from machine import Pin, PWM
from utime import sleep

# ======= Configuración de pines como PWM =======
VERDE_UNO = PWM(Pin(4))
VERDE_DOS = PWM(Pin(7))
AZUL_TRES = PWM(Pin(15))
AZUL_CUATRO = PWM(Pin(16))
NARANJA_UNO = PWM(Pin(20))
NARANJA_DOS = PWM(Pin(19))
VIOLETA_TRES = PWM(Pin(18))
VIOLETA_CUATRO = PWM(Pin(17))

# Establecer la frecuencia de PWM (por ejemplo, 1000 Hz)
frecuencia_pwm = 15
VERDE_UNO.freq(frecuencia_pwm)
VERDE_DOS.freq(frecuencia_pwm)
AZUL_TRES.freq(frecuencia_pwm)
AZUL_CUATRO.freq(frecuencia_pwm)
NARANJA_UNO.freq(frecuencia_pwm)
NARANJA_DOS.freq(frecuencia_pwm)
VIOLETA_TRES.freq(frecuencia_pwm)
VIOLETA_CUATRO.freq(frecuencia_pwm)

# Configurar el ciclo de trabajo para moverse lentamente
velocidad_lenta = 32000  # Valor entre 0 y 65535 (ajústalo según tu placa)

# Funciones de control de movimiento
def adelante_lento():
    VERDE_UNO.duty_u16(velocidad_lenta)
    VERDE_DOS.duty_u16(0)
    AZUL_TRES.duty_u16(velocidad_lenta)
    AZUL_CUATRO.duty_u16(0)
    NARANJA_UNO.duty_u16(velocidad_lenta)
    NARANJA_DOS.duty_u16(0)
    VIOLETA_TRES.duty_u16(velocidad_lenta)
    VIOLETA_CUATRO.duty_u16(0)
    sleep(1)

def adelante():
    VERDE_UNO.duty_u16(65535)  # Máximo ciclo de trabajo para avanzar
    VERDE_DOS.duty_u16(0)
    AZUL_TRES.duty_u16(65535)
    AZUL_CUATRO.duty_u16(0)
    NARANJA_UNO.duty_u16(65535)
    NARANJA_DOS.duty_u16(0)
    VIOLETA_TRES.duty_u16(65535)
    VIOLETA_CUATRO.duty_u16(0)
    sleep(1)
    
def adelante_lento():
    VERDE_UNO.duty_u16(45535)  # Máximo ciclo de trabajo para avanzar
    VERDE_DOS.duty_u16(0)
    AZUL_TRES.duty_u16(45535)
    AZUL_CUATRO.duty_u16(0)
    NARANJA_UNO.duty_u16(45535)
    NARANJA_DOS.duty_u16(0)
    VIOLETA_TRES.duty_u16(45535)
    VIOLETA_CUATRO.duty_u16(0)
    sleep(1)

def mega_adelante_lento():
    VERDE_UNO.duty_u16(25535)  # Máximo ciclo de trabajo para avanzar
    VERDE_DOS.duty_u16(0)
    AZUL_TRES.duty_u16(25535)
    AZUL_CUATRO.duty_u16(0)
    NARANJA_UNO.duty_u16(25535)
    NARANJA_DOS.duty_u16(0)
    VIOLETA_TRES.duty_u16(25535)
    VIOLETA_CUATRO.duty_u16(0)
    sleep(4)

def atras():
    VERDE_UNO.duty_u16(0)
    VERDE_DOS.duty_u16(65535)
    AZUL_TRES.duty_u16(0)
    AZUL_CUATRO.duty_u16(65535)
    NARANJA_UNO.duty_u16(0)
    NARANJA_DOS.duty_u16(65535)
    VIOLETA_TRES.duty_u16(0)
    VIOLETA_CUATRO.duty_u16(65535)
    sleep(1)

def girar_izquierda():
    # Ruedas del lado izquierdo se detienen o retroceden
    VERDE_UNO.duty_u16(0)
    VERDE_DOS.duty_u16(55535)
    AZUL_TRES.duty_u16(0)
    AZUL_CUATRO.duty_u16(55535)
    NARANJA_UNO.duty_u16(55535)
    NARANJA_DOS.duty_u16(0)
    VIOLETA_TRES.duty_u16(55535)
    VIOLETA_CUATRO.duty_u16(0)
    sleep(1)
    
    # Ruedas del lado derecho avanzan
    VIOLETA_TRES.duty_u16(95535)
    VIOLETA_CUATRO.duty_u16(0)
    AZUL_TRES.duty_u16(95535)
    AZUL_CUATRO.duty_u16(0)
    sleep(3)

def parar():
    VERDE_UNO.duty_u16(0)
    VERDE_DOS.duty_u16(0)
    AZUL_TRES.duty_u16(0)
    AZUL_CUATRO.duty_u16(0)
    NARANJA_UNO.duty_u16(0)
    NARANJA_DOS.duty_u16(0)
    VIOLETA_TRES.duty_u16(0)
    VIOLETA_CUATRO.duty_u16(0)
    sleep(2)

# ======= Lógica de control =======
def control_1():
    vueltas = 0

    #while vueltas != :
     #   print("a ver")
      #  print(vueltas)
       # vueltas += 1
    #print("adelante")
    #mega_adelante_lento()
    #print("paro")
    #parar()
    mega_adelante_lento()
    girar_izquierda()
    mega_adelante_lento()
    print("giramos?")
    
    parar()


control_1()

