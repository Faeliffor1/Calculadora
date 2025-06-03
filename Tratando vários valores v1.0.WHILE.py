n = soma = cont = 0 #variavel de n sem valor pois fora do laço não pode ser contado

while n != 999 :

    n = int(input("Digite um número: [999 para parar]   "))

# condição para saida de dados
    if n == 999:
        break

    soma += n #soma dos valores do usuario para saida de dados 
    cont += 1

print(f'Acabou, voce digitou {cont} vezes e a soma foi de {soma}')

