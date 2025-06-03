num = list()
pares = list()
impar =  list()

while True:
    num.append(int(input('Digite um valor:')))
    
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print('=-'*30)    

for i, v in enumerate(num):
    if v % 2 == 0 :
        pares.append(v)
        
    else:
        if v % 2 == 1:
            impar.append(v)
                     
print(f'A lista completa é {num}')
print(f'Lista de pares é {pares}')
print(f'Lista de impares é {impar}')

