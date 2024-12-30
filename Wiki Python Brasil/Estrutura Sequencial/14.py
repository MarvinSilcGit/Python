contador = 1

while contador != 0:

    pesoPeixe = float(input("Digite o peso do peixe: "))

    if pesoPeixe > 50:

        pesoLimite = 50

        pesoAdicional = pesoPeixe - pesoLimite

        multa = pesoAdicional * 4

        print("A multa será R$ %.2f por exceder o peso limite em %.2f quilos " %(multa, pesoAdicional))

    else:

        print("Não haverá pagamento de multa")

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()