from time import sleep
print("eSTE PROGRAMA lê A IDADE E O SEXO DE VARIAS PESSOAS, A CADA PESSOA CADASTRADA O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR. \n NO FINAL, MOSTRA INFORMACOES.")
print("-=" * 45)
print("CADASTRE UMA PESSOA ")
print("-=" * 45)
idade = 0 
sexo = 0
contador = 0
mais_18 = 0
homens = 0
mulheres_menos_20 = 0
while True:
    sleep(0.5)
    idade = int(input("Digite sua idade?\n:"))
    sleep(0.5)
    sexo = input("Qual seu sexo ? \033[35mFEMININO\033[m OU \033[32mMASCULINO\033[m \n[F/M]: ").upper()
    if idade > 18:
        mais_18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1
    contador += 1
    sleep(0.5)
    continuar = input("Quer continuar? SIM OU NÃO [S/N]\n:").upper()
    if continuar == "N":
        break


print(f"""A)Quantas pessoas tem mais de \033[33m18 anos\033[m?\n:{mais_18} pessoas\n 
B)Quantos \033[32mhomens\033[m foram cadastrados?\n:{homens} pessoas\n
C)Quantas \033[35mmulheres\033[m tem menos de \033[33m20 anos?\033[m\n:{mulheres_menos_20} pessoas\n""")
