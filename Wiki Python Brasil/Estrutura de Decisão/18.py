formatoData = input("Digite a data no formato dd/mm/aaaa: ")

if len(formatoData) != 10 or formatoData[2] == "/" or formatoData[5] == "/":

    print("Formato de data inválida")

else:

    print("Formato de data válida")