print("-" * 30)
termos=(int(input("Escreva o numero de termos a serem mostrados\n:")))
n1 = 0
n2 = 1

print("{} ⮕ {}".format(n1,n2), end = " ")
cont = 3

while cont <= termos:
    n3 = n1 + n2
    print("⮕ {}".format(n3), end=" ")
    n1 = n2
    n2 = n3
    
    if cont == termos:
        digite = input("""\n\nPara continuar escolha alguma opção asseguir:
            [1] Quer continuar ? 
        [2] Sair do programa.\n\n:""")
        if digite == "1":
            n1 = 0
            n2 = 1
            termos = int(input("Digite o novo numero de termos a serem mostrados\n:"))
            print("{} ⮕ {}".format(n1,n2), end = " ")
            n3 = n1 + n2
            print("⮕ {}".format(n3), end=" ")
            n1 = n2
            n2 = n3
            cont = 3
        else:
            print("Fim do programa")
            break
    cont = cont +1