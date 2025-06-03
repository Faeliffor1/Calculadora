nome = str(input("Qual seu nome: "))
salario = float(input("Qual seu salário: "))
dep = int(input("Quantos dependentes: "))


if dep == 0:

    nsal = salario + (salario * 5/100)

elif dep in (1, 2, 3):

    nsal = salario + (salario * 10/100)

elif dep in (4, 5, 6):

    nsal = salario + (salario * 15/100)

else:
    nsal = salario + (salario * 18/100)


print("O novo salário de", nome, 'é {:.2f}'.format(nsal), "R$")
