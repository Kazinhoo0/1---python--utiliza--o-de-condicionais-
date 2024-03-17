from random import randint
print("Este programa é um jogo de jokenpô, que utiliza pedra papel e tesoura ")

print("!!VAMOS VER SE VOCE É MAIS ESPERTO QUE A CPU!!")
itens = "Pedra", "Papel", "Tesoura"
computador = randint (0, 2)
print("""Qual opção voce escolhe: 
     [0] "Pedra"
     [1] "Papel"
     [2] "Tesoura""")
print("-=" * 20)
jogador = (int(input("Qual sua opção? ")))
print("-=" * 20)
print("O computador escolheu: {}".format(itens[computador]))
print("O jogador escolheu: {}".format (itens[jogador]))
print("-=" * 20)
if computador == 0: #Computador pedra
    if jogador == 0:
        print("Empate")
    if jogador == 1:
        print("Jogador Ganhou!")
    if jogador == 3: 
        print("Computador Ganhou!")

if computador == 1: # Computador papel
    if jogador == 0:
        print("Computador Ganhou!")
    if jogador == 1:
        print("Empate")
    if jogador == 2:
        print("Jogador Ganhou!")

if computador == 2: #computador tesoura
    if jogador == 0:
        print("Jogador Ganhou!")
    if jogador == 1:
        print("Computador Ganhou!")
    if jogador == 2:
        print("Empate")
