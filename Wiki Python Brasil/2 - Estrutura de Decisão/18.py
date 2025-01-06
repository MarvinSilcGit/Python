formato_data = input("Digite a data no formato dd/mm/aaaa: ")

if len(formato_data) != 10 or formato_data[2] == "/" or formato_data[5] == "/":

    print("Formato de data inválida")

else:

    print("Formato de data válida")