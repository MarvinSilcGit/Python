peso_peixe = float(input("Digite o peso do peixe: "))

if peso_peixe > 50:

    peso_limite = 50

    peso_adicional = peso_peixe - peso_limite

    multa = peso_adicional * 4

    print("A multa será R$ %.2f por exceder o peso limite em %.2f quilos " % (multa, peso_adicional))

else:

    print("Não haverá pagamento de multa")