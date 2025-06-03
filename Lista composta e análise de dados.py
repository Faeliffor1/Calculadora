temp = []
principal = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]    
    principal.append(temp [:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Foram cadastradas {len(principal)} pessoas')
print(f'O maior peso é de {mai} que são de ', end=' ')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()        
print(f'O menor peso é {men} que são de', end=' ')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}]', end='')