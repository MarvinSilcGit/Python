print("Digite 1 para residências")

print("Digite 2 para comércios")

print("Digite 3 para indústrias")

tipo = int(input("Qual o tipo de instalação? "))

if tipo == 1:

    consumo = float(input("Quanto foi consumido? "))

    if consumo <= 500:

        faixa = consumo * 0.40

        print("A quantidade consumida custou R$ %.2f" % faixa)

    elif consumo > 500:

        faixa = consumo * 0.65

        print("A quantidade consumida custou R$ %.2f" % faixa)

elif tipo == 2:

    consumo = float(input("Quanto foi consumido? "))

    if consumo <= 1000:

        faixa = consumo*0.55

        print("A quanidade consumida custou R$ %.2f" % faixa)

    elif consumo > 1000:

        faixa = consumo*0.60

        print("A quantidade consumida custou R$ %.2f" % faixa)

elif tipo == 3:

    consumo = float(input("Quanto foi consumido? "))

    if consumo <= 5000:

        faixa = consumo*0.55

        print("A quantidade consumida custou %.2f" % faixa)

    elif consumo > 5000:

        faixa = consumo*0.60

        print("A quantidade consumida custou %.2f" % faixa)

else:

    print("Digite um valor entre 1 e 3 para proseguir para o próximo menu")