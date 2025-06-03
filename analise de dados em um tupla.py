num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))

print(f'Voce digitou os valores: {num}')

print(f'O número 9 apareceu {num.count(9)}')

if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1} posição')
else:
    print('O número 3 não foi digitado')

print('Os números pares são: ', end='')
for n in num:
    if n %2 == 0:
        print(f'{n}', end=' ')    
