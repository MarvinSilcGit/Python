altura_homem = float(input("Digite a altura do homem: "))

altura_mulher = float(input("Digite a altura da mulher: "))

peso_ideal_homem = (72.7 * altura_homem) - 58

peso_ideal_mulher = (62.1 * altura_mulher) - 44.7

print("O peso ideal desse homem é %.2f.\nO peso ideal dessa mulher é %.2f" % (peso_ideal_homem, peso_ideal_mulher))