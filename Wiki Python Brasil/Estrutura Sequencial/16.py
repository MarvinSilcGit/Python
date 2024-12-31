metragem = float(input("Digite a metragem: "))

metragemLata = 18

quantidadeLatas = 0

if metragem / metragemLata <= 1:

    quantidadeLatas = 1

    print("Será necessária, no máximo, uma lata de tinta para pintar %.2f metros²" % metragem)

else:

    print()