n = int(input('Digite um número: '))
fatorial = 1
contador = n

print(f'Calculando fatorial {n}! = ', end='')

while contador > 0:
    
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')

    fatorial *= contador
    contador -= 1

print(f'{fatorial}')    