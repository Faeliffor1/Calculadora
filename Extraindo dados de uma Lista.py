lista = []

while True:
      
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    lista.sort(reverse=True)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print('=-'*30)

print(f'Voce digitou {len(lista)} elementos')
print(f'Os valores em ordem decrecente são {lista}')

if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')    