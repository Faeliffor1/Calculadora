valor = [int(input('Digite o valor 0: ')), int(input('Digite o valor 1: ')),int(input('Digite o valor 2: ')),int(input('Digite o valor 3: ')),
         int(input('Digite o valor 4: '))]
print('-='*30)

print(f'Voce digitou os valores {valor}')

print(f'O maior valor foi {max(valor)} nas posiçoes ', end='')
for i, v in enumerate(valor):
    if v == max(valor):
        print(f'{i} ...', end=' ')
print()
print(f'O menor valor foi {min(valor)} nas posiçoes ', end=' ')

for i, v in enumerate(valor):
    if v == min(valor):
        print(f'{i} ...', end=' ')