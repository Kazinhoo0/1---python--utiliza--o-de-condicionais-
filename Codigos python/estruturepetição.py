print("-=" * 45)
print("Este programa lê um numero inteiro e diga se ele é ou não um numero primo.")
print("-=" * 45)

numero = int(input("Digite o numero: "))
total = 0
for c in range(1, numero + 1):
        if numero % c == 0:
            print("\033[32m", end="") 
            total = total + 1  
        else :
            print("\033[31m", end= "")
        print("{}".format(c), end= "")
print("\n\033[34mO numero {} foi divisível {} vezes\033m".format(numero,total))

if total == 2:
    print("O numero é primo.")
else:
     print("O numero não é primo")
     