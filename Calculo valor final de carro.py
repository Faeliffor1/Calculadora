fabrica = float(input('Qual o preço de fábrica ? '))

custo = (fabrica * 45)/100

distri = (fabrica * 28)/100

valor_final = distri + fabrica + custo

print('O valor final é {:2}'.format(valor_final))
