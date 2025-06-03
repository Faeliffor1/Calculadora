total= tomil = menor = cont =  0

while True:
    print('-'*40)
    print(f'{'LOJA SUPER BARATÃO':^40}')
    print('-'*40)

    nome_produto = str(input('Nome do produto: '))

    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        tomil += 1

    if cont == 1:
        menor = preco
    else:
        if cont < menor:
            menor = preco        

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total de compras foi de R${total:.2f}')  
print(f'Temos {tomil} produto que é acima de R$1000.00')
print(f'O produto mais barato custa R${menor}')  

