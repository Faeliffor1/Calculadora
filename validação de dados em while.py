sexo = str(input('Qual seu sexo: [M/F] ')).strip().upper()[0]


while sexo not in 'MF':
    sexo = str(input('Dado invalido, digite o seu sexo: '))
print(f'Seu sexo é {sexo}')


        