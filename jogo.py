from gpiozero import *
from time import sleep
import random

led_1 = LED(22)
led_2 = LED(4)
rgb = RGBLED(vermelho=14, verde=17, azul=27)
botao_1 = Button(24)
botao_2 = Button(2)

jogador_1 = input("Digite o nome do Jogador 1: ")
jogador_2 = input("Digite o nome do Jogador 2: ")

pontuacao_jogador_1 = 0
pontuacao_jogador_2 = 0
num_rodada = 0

while True:

    truque = False
    num_rodada = num_rodada + 1

    espera = 0

    tempo = random.uniform(0, 10)
    cor_2 = random.uniform(0, 1)
    cor_3 = random.uniform(0, 1)

    fixo = random.randint(0, 3)

    if cor_2 == 0 and cor_3 == 0:
        cor_2 = 1

    sleep(tempo)

    if fixo == 3:
        truque = True
        rgb.cor = (1, 0, 0)
    else:
        rgb.cor = (0, cor_2, cor_3)

    while True:
        if botao_1.is_pressed and not truque:
            print(jogador_1, "vence!")
            pontuacao_jogador_1 = pontuacao_jogador_1 + 1
            rgb.cor = (0, 0, 0)
            print(jogador_1, ":", pontuacao_jogador_1)
            print(jogador_2, ":", pontuacao_jogador_2)
            espera = 0
            break
        elif botao_1.is_pressed and truque:
            print(jogador_1, "Oh não!")
            pontuacao_jogador_1 = pontuacao_jogador_1 - 1
            rgb.cor = (0, 0, 0)
            print(jogador_1, ":", pontuacao_jogador_1)
            print(jogador_2, ":", pontuacao_jogador_2)
            espera = 0
            break

        if botao_2.is_pressed and not truque:
            print(jogador_2, "vence!")
            pontuacao_jogador_2 = pontuacao_jogador_2 + 1
            rgb.cor = (0, 0, 0)
            print(jogador_1, ":", pontuacao_jogador_1)
            print(jogador_2, ":", pontuacao_jogador_2)
            espera = 0
            break
        elif botao_2.is_pressed and truque:
            print(jogador_2, "Oh não!")
            pontuacao_jogador_2 = pontuacao_jogador_2 - 1
            rgb.cor = (0, 0, 0)
            print(jogador_1, ":", pontuacao_jogador_1)
            print(jogador_2, ":", pontuacao_jogador_2)
            espera = 0
            break

        if truque and espera == 100000:
            print("Muito bem")
            rgb.cor = (0, 0, 0)
            print(jogador_1, ":", pontuacao_jogador_1)
            print(jogador_2, ":", pontuacao_jogador_2)
            espera = 0
            break

        espera = espera + 1

    if pontuacao_jogador_1 > pontuacao_jogador_2:
        led_1.on()
        led_2.off()
    elif pontuacao_jogador_2 > pontuacao_jogador_1:
        led_2.on()
        led_1.off()
    else:
        led_1.on()
        led_2.on()