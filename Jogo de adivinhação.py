from random import randint
from time import sleep

computador = randint(0, 100)
print('-=-'*10)
jogador = int(input('Qual número eu pensei ? '))
print('-=-'*10)

print('Processando ...')

print('-=-'*10)

sleep(2)

if jogador == computador:
    print('ACERTOU, o número que pensei é o {}'.format(computador))
else:
    print('ERROU, o número pensado foi {}'.format(computador))
