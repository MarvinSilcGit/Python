# Manipulação de strings;

imposto = ("olá mundo")

print(imposto[8])
# concatenação;

imposto = "ABCDEFGHI"

x = 111

print(imposto+"d")

# utilizaçao de marcador do tipo inteiro "%d"; Composição de strings;

print("João tem %d anos" % x)

print("[%4d]" % x)

print("[%-4d]" % x)

print("[%3d]" % x)

        #utilização de marcador do tipo flutuante "%f"; Composição de strings;

print("joão tem [%4.2f]" % x)

print("joão tem [%10.1f]" % x)

#utilização de marcador do tipo string "%s"; Composição de strings;

joão = "joão"

idade = x

dinheiro = x*10

print("%s tem %d anos e %4.2f reais de dinheiro" % (joão, idade, dinheiro))


#fatiamento de strings;

print()

print(imposto[0:4])

print(imposto[1:4])

print(imposto[-3:])

print(imposto[-4:9])

print(imposto[:8])

print(imposto[-2:])
