n = 0

while True:
    
    n = int(input('Qual número deseja ver a tabuada? '))
    print('-=-'*30)

    if n < 0:
        break
    for c in range(0, 11):
        
        print(f'{n } x {c:2} = {n * c}')

    print('-=-'*30)
print('Programa finalizado')
    
