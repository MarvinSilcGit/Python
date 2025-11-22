velocidade = int(input("Qual a velocidade do veículo? "))

if velocidade > 80:

    multa = (velocidade - 80) * 5

    print("O condutor foi multado em R$ %.2f por estar %.0f quilômetro(s) acima do limite de velocidade" % (multa, velocidade - 80))

if velocidade <= 80:

    print("O condutor não foi multado por estar dentro do limite de velocidade")