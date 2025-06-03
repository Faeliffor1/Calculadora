
print("________________________________")
print("      CRIANÇA ESPERANÇA         ")
print("________________________________")

print("[1] Para doar 10 R$")
print("[2] Para doar 25 R$")
print("[3] Para doar 50 R$")
print("[4] Para doar outros valores ")
print("[5] Para cancelar")

escolha = (int(input("Escolha uma opção: ")))

if escolha == 1:
    print("Muito obrigado por doar 10 R$")

elif escolha == 2:
    print("Muito obrigado por doar 25 R$")

elif escolha == 3:
    print("Muito obrigado por doar 50 R$")

elif escolha == 4:
    valor = input("Qual o valor deseja? ")
    print("Muito obrigado por doar", valor, "R$")

elif escolha == 5:
    print("Cancelado, Muito Obrigado")
