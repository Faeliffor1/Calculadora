
nota1 = (float(input("Primeira nota: ")))
nota2 = (float(input("Segunda nota: ")))
m = (nota1 + nota2)/2

print("A media é: ", m)

if m >= 7:
    print("Aluno aprovado")
else:
    if m >= 5 and m <= 7:
        print("Aluno em recuperação")
    else:
        if m <= 5:
            print("Aluno Reprovado")
