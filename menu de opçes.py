num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num = '1234'

acertou = False

while not acertou:
    print('\n[1] somar')
    print('\n[2] subtrair')
    print('\n[3] multiplicar')
    print('\n[4] dividir')
    op = int(input('\nQual operação deseja: '))
    if op == num:
        acertou = True 
        

    if op == 1:
        result = num1 + num2
        print(f'A soma de {num1} e {num2} é {result}')
    elif op == 2:
        result = num1 * num2
        print(f'A multiplicação de {num1} e {num2} é {result}')

    elif op == 3:
        if num1 > num2:
            print(f'O {num1} é maior que {num2}')
        elif num2 > num1:
            print(f'O {num2} é maior que o {num1}')

    elif op == 4:
        print('Digite novamente')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif op == 5:
        print('Finalizando....')    

        
    else:
        print('Invalido')  
                   
print('-=-'*50)