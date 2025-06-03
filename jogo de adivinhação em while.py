from random import randint

computador = randint(0,10)

print('Vamos brincar de adivinhação? ')
print('Tente adivinhar um número de 0 a 10')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual seu palpipe: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:    
        if jogador < computador:
          print('Mais ... tente novamente')
        elif jogador > computador:
          print('Menos ... tente novamente')
         
print(f'Acertou, o número foi {computador} e voce teve {palpite} tentativas')



