velocidade = int(input('Qual a velocidade do carro: '))

if velocidade >= 80:
    execesso = velocidade - 80
    multa = execesso *7
    print('Multado!!!, voce está a cima do limite de velocidade de 80 km ')
    print(f'Sua multa é de {multa}R$')

else:
    print('Voce está na velocidade correta, boa viajem')    