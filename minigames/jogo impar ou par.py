print("Este programa joga par ou impar com o computador, o jogo só sera interrompido quando o jogar perder, mostrando o total de vitorias consecutivas que ele conquitou no final do jogo.")
import random
from time import sleep

jogador = 0
vitorias_consecutivas = 0
resultado = 0

while True:
    jogador = int(input("Digite um valor\n:"))
    escolha = str(input("IMPAR OU PAR ? [P/I]\n: ")).upper()
    
    computador = random.randint(1,11)
    soma = jogador + computador

    if soma % 2 == 0:
        resultado = "PAR"
    elif soma % 2 != 0:
        resultado = "ÍMPAR"
    sleep(1)
    print(f"Você jogou {jogador} e o cumputador {computador}. Total de {soma} deu {resultado}")
          
    sleep(1)   
    if (escolha == "P" and resultado == "PAR") or (escolha == "I" and resultado == "ÍMPAR"):
        vitorias_consecutivas += 1
        print(f"Você venceu! Vitórias consecutivas: {vitorias_consecutivas}")
    else:
        print(f"Você perdeu. Vitórias consecutivas: {vitorias_consecutivas}")
        break       
