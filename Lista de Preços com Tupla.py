produtos = ( 'Smartphone' , 1500 , 'Notebook' , 4000 , 'Fone de ouvido ' , 150, 'Rélogio' , 190, 'Tablet' , 2100 , 
            'Playstation' , 2500 , 'Aspirador de pó'  , 1000 ,  'Air fryer' , 250 , 'Kindle' , 100 , 'Camera' , 10000 )

print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0 , len(produtos)):
    if pos %2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:.>6.2f}')    
print('-'*40)

