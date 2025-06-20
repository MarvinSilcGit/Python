araja = 80000

bacalaca = 200000

anos = 0

while araja < bacalaca:

    araja += araja / 100 * 3

    bacalaca += bacalaca / 100 * 1.5

    anos +=1

    print(araja)

    print(bacalaca)

print(f"Serão necessários pelos menos {anos} anos")