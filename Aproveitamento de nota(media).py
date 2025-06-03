n1 = float(input("Qual a primeira nota: "))
n2 = float(input("Qual a segunda nota: "))
media = (n1 + n2)/2

print("__________________________________________________")


print("Sua media foi", media)

if media <= 10 and media >= 9:
    print("APROVEITAMENTO: A")

elif media <= 9 and media >= 8:
    print("APROVEITAMENTO: B")

elif media <= 8 and media >= 7:
    print("APROVEITAMENTO: C")

elif media <= 7 and media >= 6:
    print("APROVEITAMENTO: D")

elif media <= 6 and media >= 5:
    print("APROVEITAMENTO: E")

elif media < 5:
    print("APROVEITAMENTO : F ")
