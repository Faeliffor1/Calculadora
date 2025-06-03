
import os
import time 

print("_____________________________________________________")

ano_nasce = int(input("Em que ano voce nasceu? "))
ano_atual = int(input("Ano atual: "))
idade = ano_atual - ano_nasce

print("_______________________________________________-")

print("Sua idade é de:", idade)

if idade >= 18:
    print("ESTÁ APTA A TIRAR A CARTEIRA")
else:
    print("NÃO ESTÁ APTO A TIRAR A CARTEIRA")

os.system('clr' if os.name == 'nt' else 'clear')    
