listaConsoante = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç",
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ç"]

listaVogal = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

letraBusca = input("Digite a letra para saber se é vogal ou consoante: ")

if letraBusca in listaVogal:

    print("A letra '%s' é Vogal" % letraBusca)

elif letraBusca in listaConsoante:

    print("A letra '%s' é Consoante" % letraBusca)

else:

    print("A letra '%s' não é nem vogal nem consoante" % letraBusca)