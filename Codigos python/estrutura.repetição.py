print("Este programa lê a idade de atletas e diz se eles são mirim,infantil,junior, sênior ou master")


print("-=" * 50)
print("BEM VINDO A FEDERAÇÃO NACIONAL DE NATAÇÃO")
print("Abaixo voce ira digitar sua data de nascimento.")
print("-=" * 50)
ano = int(input("Digite aqui: "))
idade = 2024 - ano

if 2013 <= ano <= 2020:
    print("Com {} anos de idade você se encaixa na categoria MIRIM".format(idade))

elif 2010 <=ano <=2013:
    print("Com {} anos de idade você se encaixa na categoria INFANTIL ".format(idade))

elif 2004 <= ano <= 2013:
    print("Com {} anos de idade você se encaixa na categoria JUNIOR".format(idade))

elif 2003 <= ano <= 2004:
    print("Com {} anos de idade você se encaixa na categoria SÊNIOR".format(idade))

else:
    print("Com {} anos de idade você se encaixa na categoria MASTER".format(idade))