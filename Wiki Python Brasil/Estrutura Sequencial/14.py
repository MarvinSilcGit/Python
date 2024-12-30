pesoPeixe = float(input("Digite o peso do peixe: "))

if pesoPeixe > 50:

    pesoLimite = 50

    pesoAdicional = pesoPeixe - pesoLimite

    multa = pesoAdicional * 4

    print("A multa será R$ %.2f por exceder o peso limite em %.2f quilos " %(multa, pesoAdicional))

else:

    print("Não haverá pagamento de multa")