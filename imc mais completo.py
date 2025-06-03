

while True:

    peso = float(input("Qual seu peso: "))
    altura = float((input("Qual sua altura: ")))
    imc = peso / (altura ** 2)
    peso_ideal = 18.5 and 25 * (altura ** 2)

    print("IMC {:.1f}".format(imc))

    if imc < 17:
        print("Muito abaixo do peso")
    else:
        if imc >= 17 and imc <= 18.5:
            print("Abaixo do peso")
        else:
            if imc >= 18.5 and imc <= 25:
                print("Peso ideal")
            else:
                if imc >= 25 and imc <= 30:
                    print("Sobre peso")
                else:
                    if imc >= 30 and imc <= 35:
                        print("Obesidade")
                    else:
                        if imc >= 35 and imc <= 40:
                            print("Obesidade Severa")
                        else:
                            print("Obesidade mórbida")
    print("_________________________________________________________")
