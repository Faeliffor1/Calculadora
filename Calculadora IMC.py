peso = float(input("Qual o seu peso: "))
altura = float(input("Qual sua altura: "))
imc = peso / (altura ** 2)
peso_ideal = 18.6 and 25 * (altura**2)

print("IMC {:.1f}".format(imc))

if imc >= 18.6 and imc < 25:
    print("Voce está no peso ideal")

elif imc > 25:
    print("Voce está a cima do peso, CUIDADO")

print("_____________________________________________")

print("Peso ideal é: ", peso_ideal)
