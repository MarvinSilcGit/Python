alturaHomem = float(input("Digite a altura do homem: "))

alturaMulher = float(input("Digite a altura da mulher: "))

pesoIdealHomem = (72.7 * alturaHomem) - 58

pesoIdealMulher = (62.1  * alturaMulher) - 44.7

print("O peso ideal desse homem é %.2f.\nO peso ideal dessa mulher é %.2f" % (pesoIdealHomem, pesoIdealMulher))