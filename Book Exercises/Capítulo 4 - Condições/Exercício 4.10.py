print("Digite 1 para residências")

print("Digite 2 para comércios")

print("Digite 3 para indústrias")

print()

tipo = input("Qual o tipo de instalação? ")

if tipo == "1":

    consumo = float(input("Quanto foi consumido? "))

    if consumo <= 500:

        faixaConsumo = consumo * 0.40

        print("A quantidade consumida custou R$ %.2f" % faixaConsumo)

    else:

        faixaConsumo = consumo * 0.65

        print("A quantidade consumida custou R$ %.2f" % faixaConsumo)

elif tipo == "2":

    consumo = float(input("Quanto foi consumido? "))

    if consumo <= 1000:

        faixaConsumo = consumo*0.55

        print("A quanidade consumida custou R$ %.2f" % faixaConsumo)

    else:

        faixaConsumo = consumo*0.60

        print("A quantidade consumida custou R$ %.2f" % faixaConsumo)

elif tipo == "3":

    consumo = float(input("Quanto foi consumido? "))

    if consumo <= 5000:

        faixaConsumo = consumo*0.55

        print("A quantidade consumida custou %.2f" % faixaConsumo)

    else:

        faixaConsumo = consumo*0.60

        print("A quantidade consumida custou %.2f" % faixaConsumo)

else:

    print("Digite um valor entre 1 e 3 para proseguir para o próximo menu")