
# VARIAVEIS

import os
import time


num1 = 0
num2 = 0
result = 0
op = ""


while True:

    num1 = (float(input("Digite o primeiro número: ")))
    op = (input("Qual a operação: "))
    num2 = (float(input("Qual o segundo número: ")))

    if op == "+":
        result = num1 + num2

    elif op == '-':
        result = num1 - num2

    elif op == '*':
        result = num1 * num2

    elif op == '/':
        if num2 != 0:
            result = num1 / num2

        else:
            print("Divisão por 0 não é permitida ")
            continue

    else:
        print("OPERAÇÃO INVÁLIDA!!!!")
        continue

    print("{} {} {} = {}".format(num1, op, num2, result))

    print("__________________________________________________________")

    os.system('cls' if os.name == 'nt' else 'clear')
