km = float(input('Qual a distancia em km: '))

print(f'Voce está prestes a começar uma viagem de {km} km')


if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45

print(f'O preço da passagem é de {preco:.2f}')
