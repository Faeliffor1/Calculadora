primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while cont <= 10:

    print(f'{termo} > ', end=' ')
    termo += razao
    cont += 1

print('Pausa')
while True:

        segundo = int(input('Quantos termos voce quer mostrar a mais? (0 para sair) '))
        if segundo == 0:
            print("Encerrado")
            break

        cont = 1

        while cont <= segundo:

            print(f'{termo} > ', end=' ')
            termo += razao
            cont += 1

        print("Pausa")
                
print(f"Progressão finalizada e teve {total} termos ")






