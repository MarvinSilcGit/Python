nota_parcial1 = float(input("Digite a primeira nota parcial: "))

if nota_parcial1 > 10 or nota_parcial1 < 0:

    print("Nota inválida")

nota_parcial2 = float(input("Digite a segunda nota parcial: "))

if nota_parcial2 > 10 or nota_parcial2 < 0:

    print("Nota inválida")

media_final = (nota_parcial1 + nota_parcial2) / 2

if media_final >= 6:

    print(f"Aprovado e a média foi {media_final:.2f}")

    if 9 <= media_final <= 10: # Equals to media_final >= 9 and media_final <= 10:

        print("Conceito A")

    elif 7.5 <= media_final < 9: # Equals to media_final >= 7.5 and media_final < 9:

        print("Conceito B")

    elif 6 <= media_final < 7.5: # Equal to media_final >= 6 and media_final < 7.5:

        print("Conceito C")

else:

    print(f"Reprovado e a média foi {media_final:.2f}")

    if 4 <= media_final < 6: # Equals to media_final >= 4 and media_final < 6:

        print("Conceito D")

    else:

        print("Conceito E")