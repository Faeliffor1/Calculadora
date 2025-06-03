print("______________________________________")
print("         BANGU X VASCO                ")
print("______________________________________")

g1 = int(input("Quantos gols Bangu fez? "))
g2 = int(input("Quantos gols Vasco fez? "))
diferenca = 0


if g1 > g2:
    diferenca = g1 - g2

elif g2 > g1:
    diferenca = g2 - g1


print("Diferença: ", diferenca)

if diferenca == 0:
    print("Empate")

elif diferenca in (1, 2, 3, 4):
    print("Partida normal")

else:
    print("Goleada")
