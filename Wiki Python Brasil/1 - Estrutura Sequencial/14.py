peso_peixe = float(input("Digite o peso do peixe: "))

if peso_peixe > 50:

    peso_limite = 50

    peso_adicional = peso_peixe - peso_limite

    multa = peso_adicional * 4

    print(f"A multa será R$ {multa:.2f} por exceder o peso limite em {peso_adicional:.2f} quilos")

else:

    print("Não haverá pagamento de multa")