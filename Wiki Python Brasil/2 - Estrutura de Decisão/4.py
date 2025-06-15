letra_busca = input("Digite a letra para saber se é vogal ou consoante: ")

if (letra_busca == "a" or letra_busca == "e" or letra_busca == "i" or letra_busca == "o" or letra_busca == "u" or letra_busca == "A"
    or letra_busca == "E" or letra_busca == "I" or letra_busca == "O" or letra_busca == "U"):

    print(f"A letra '{letra_busca}' é Vogal")

elif (letra_busca == "b" or letra_busca == "c" or letra_busca == "d" or letra_busca == "f" or letra_busca == "g" or letra_busca == "h"
    or letra_busca == "j" or letra_busca == "k" or letra_busca == "l" or letra_busca == "m" or letra_busca == "n" or letra_busca == "p"
    or letra_busca == "q" or letra_busca == "r" or letra_busca == "s" or letra_busca == "t" or letra_busca == "v" or letra_busca == "w"
    or letra_busca == "x" or letra_busca == "y" or letra_busca == "z" or letra_busca == "ç" or letra_busca == "B" or letra_busca == "C"
    or letra_busca == "D" or letra_busca == "F" or letra_busca == "G" or letra_busca == "H" or letra_busca == "J" or letra_busca == "K"
    or letra_busca == "L" or letra_busca == "M" or letra_busca == "N" or letra_busca == "P" or letra_busca == "Q" or letra_busca == "R"
    or letra_busca == "S" or letra_busca == "T" or letra_busca == "V" or letra_busca == "W" or  letra_busca =="X" or  letra_busca =="Y"
    or letra_busca == "Z" or letra_busca == "Ç"):

    print(f"A letra '{letra_busca}' é Consoante")

else:

    print(f"O caractere '{letra_busca}' não é nem vogal nem consoante")