resp = 'S'
soma = quant = media = maior = menor = 0


while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja contirnuar? [S/N]:  ')).upper().strip()[0]  
print('-='*40)
print(f'Acabou, voce digitou {quant} vezes e a soma foi de {soma}')
print(f'O maior número foi {maior} e o menor {menor}')                   



