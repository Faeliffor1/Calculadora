lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)


    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break
    
print('=-'*30)
print(f'Voce digitoui os valores {lista}')