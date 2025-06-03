cont = total_homens = cont2 = 0

while True:
    print('-'*30) 
    print(f'{'CADASTRE UMA PESSOA':^30}')   
    print('-'*30) 

    idade = int(input('Digite sua idade: '))

    if idade > 18: 
        cont += 1

    print('-'*30) 

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
        

        if sexo == 'M':
            total_homens +=1

        if sexo == 'F'and idade < 20:
            cont2 +=1   
    
    print('-'*30) 

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if continuar == 'N':
        break

    print('-'*30) 

print(f'Total de pessoas com mais de 18 são {cont}')
print(f'Ao todo temos {total_homens} homens cadastrados')
print(f'E temos {cont2} mulheres com menos de 20 anos ')