lista_consoantes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç",
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ç"]

lista_vogais = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

letra_busca = input("Digite a letra para saber se é vogal ou consoante: ")

if letra_busca in lista_vogais:

    print("A letra '%s' é Vogal" % letra_busca)

elif letra_busca in lista_consoantes:

    print("A letra '%s' é Consoante" % letra_busca)

else:

    print("A letra '%s' não é nem vogal nem consoante" % letra_busca)