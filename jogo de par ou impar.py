from random import randint

v = 0

print('-=-'*10)
print(f'{"Vamos jogar par ou impar":^30}')
print('-=-'*10)

while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
            tipo = str(input('Par ou ímpar? [P/I]  ')).upper().strip()[0]

    print(f'Voce jogou {jogador} e o computador {computador} e o total deu {total}')

    if tipo == 'P':
        if total %2 == 0:
             print('Voce venceu')
             v += 1
        else:
          print('Voce perdeu')  
          break  
    elif tipo == 'I':
         if total %2 == 1:
              print('Voce venceu')
              v += 1
         else:
              print('Voce perdeu')  
              break   

    print('Vamos jogar novamnete ...')      
print(f'GAME OVER!, Voce ganhou {v} vezes ')

    

    

    


    

