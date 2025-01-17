def fahrenheit_celsius (temperatura: float):

    celsius = (temperatura - 32) / 1.8

    return "A temperatura em %.1f° Fahrenheit equivale à %.1f° Celsius" % (temperatura, celsius)


def fahrenheit_kelvin (temperatura: float):

    kelvin = (temperatura - 32) / 1.8 + 273.15

    return "A temperatura em %.1f° Fahrenheit equivale à %.1f° Kelvin" % (temperatura, kelvin)


def fahrenheit_rankine (temperatura: float):

    rankine = temperatura + 459.67

    return "A temperatura em %.1f° Fahrenheit equivale à %.1f° Rankine" % (temperatura, rankine)


def celsius_fahrenheit (temperatura: float):

    fahrenheit = (temperatura * 1.8) + 32

    return "A temperatura em %.1f° Celsius equivale à %.1f° Fahrenheit" % (temperatura, fahrenheit)


def celsius_kelvin (temperatura: float):

    kelvin = temperatura + 273.15

    return "A temperatura em %.1f° Celsius equivale à %.1f° Kelvin" % (temperatura, kelvin)


def celsius_rankine (temperatura: float):

    rankine = (temperatura - 491.67) * 5 / 9

    return "A temperatura em %.1f° Celsius equivale à %.1f° Rankine" % (temperatura, rankine)


def kelvin_fahrenheit (temperatura: float):

    fahrenheit = (temperatura - 273.15) * 9 / 5 + 32

    return "A temperatura em %.1f° Kelvin equivale à %.1f° Fahrenheit" % (temperatura, fahrenheit)


def kelvin_celsius (temperatura: float):

    celsius = temperatura - 273.15

    return "A temperatura em %.1f° Kelvin equivale à %.1f° Celsius" % (temperatura, celsius)


def kelvin_rankine (temperatura: float):

    rankine = temperatura * 9 / 5

    return "A temperatura em %.1f° Kelvin equivale à %.1f° Rankine" % (temperatura, rankine)


def rankine_fahrenheit (temperatura: float):

    fahrenheit = temperatura - 459.67

    return  "A temperatura em %.1f° Rankine equivale à %.1f° Fahrenheit" % (temperatura, fahrenheit)


def rankine_celsius (temperatura: float):

    celsius = (temperatura - 491.67) * 5/ 9

    return "A temperatura em %.1f° Rankine equivale à %.1f° Celsius" % (temperatura, celsius)


def rankine_kelvin (temperatura: float):

    kelvin = temperatura * 5 / 9

    return "A temperatura em %.1f° Rankine equivale à %.1f° Kelvin" % (temperatura, kelvin)