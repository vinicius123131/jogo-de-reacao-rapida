import RPi.GPIO as GPIO
import time
import math

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

limite_alvorecer = 50
pino_a = 18
pino_b = 23
pino_buzzer = 24
pino_vermelho1 = 27
pino_vermelho2 = 22

GPIO.setup(pino_buzzer, GPIO.OUT)
GPIO.setup(pino_vermelho1, GPIO.OUT)
GPIO.setup(pino_vermelho2, GPIO.OUT)

def descarregar():
    GPIO.setup(pino_a, GPIO.IN)
    GPIO.setup(pino_b, GPIO.OUT)
    GPIO.output(pino_b, False)
    time.sleep(0.01)

def tempo_carga():
    GPIO.setup(pino_b, GPIO.IN)
    GPIO.setup(pino_a, GPIO.OUT)
    GPIO.output(pino_a, True)
    t1 = time.time()
    while not GPIO.input(pino_b):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000

def leitura_analogica():
    descarregar()
    return tempo_carga()

def leitura_resistencia():
    n = 20
    total = 0
    for i in range(1, n):
        total = total + leitura_analogica()
    leitura = total / float(n)
    resistencia = leitura * 6.05 - 939
    return resistencia

def luz_de_R(R):
    return math.log(1000000.0 / R) * 10.0

while True:
    GPIO.output(pino_vermelho1, False)
    GPIO.output(pino_vermelho2, False)
    luz = luz_de_R(leitura_resistencia())
    x = 0
    if luz > limite_alvorecer:
        GPIO.output(pino_vermelho1, True)
        GPIO.output(pino_vermelho2, False)
        while True:
            x = x + 1
            GPIO.output(pino_buzzer, True)
            time.sleep(0.001)
            GPIO.output(pino_buzzer, False)
            time.sleep(0.001)
            if x == 250:
                x = 0
                break
        GPIO.output(pino_vermelho1, False)
        GPIO.output(pino_vermelho2, True)
        while True:
            x = x + 1
            GPIO.output(pino_buzzer, True)
            time.sleep(0.001)
            GPIO.output(pino_buzzer, False)
            time.sleep(0.001)
            if x == 250:
                x = 0
                break
