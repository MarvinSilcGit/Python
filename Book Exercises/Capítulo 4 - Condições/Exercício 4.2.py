velocidade = int(input("qual a velocidade do veículo? "))

if velocidade > 80:

    multa = (velocidade - 80) * 5

    print("o condutor foi multado em R$ %.2f , por estar acima do limite de velodade" % multa)

if velocidade <= 80:

    print("o condutor não foi multado por estar no limite de velocidade")
