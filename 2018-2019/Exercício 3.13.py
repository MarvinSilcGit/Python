celsius = float(input("digite a temperatura para ser convertida de celsius para fahrenheit: "))

fahrenheit = (celsius*1.8)+32

print("A temperatura em %.2f celsius equivale à %.2f fahrenheit" % (celsius, fahrenheit))

fahrenheit = float(input("digite a temperautra para ser convertida de fahrenheit para celsius: "))

celsius = (fahrenheit-32)/1.8

print("A temperatura em %.2f fahrenheit equivale à %.2f celsius" % (fahrenheit, celsius))
