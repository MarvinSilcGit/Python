def fahrenheit_celsius (temperatura: float):

    temperatura_celsius = (temperatura - 32) * 5 / 9

    return "A temperatura em %.1f° Fahrenheit equivale à %.1f° Celsius" % (temperatura, temperatura_celsius)

def fahrenheit_kelvin (temperatura: float):

    temperatura_kelvin = (temperatura - 32) * 5 / 9 + 273.15

    return "A temperatura em %.1f° Fahrenheit equivale à %.1f° Kelvin" % (temperatura, temperatura_kelvin)


def fahrenheit_rankine (temperatura: float):

    temperatura_rankine = temperatura + 459.67

    return "A temperatura em %.1f° Fahrenheit equivale à %.1f° Rankine" % (temperatura, temperatura_rankine)


def celsius_fahrenheit (temperatura: float):

    temperatura_fahrenheit = (temperatura * 5 / 9) + 32

    return "A temperatura em %.1f° Celsius equivale à %.1f° Fahrenheit" % (temperatura, temperatura_fahrenheit)


def celsius_kelvin (temperatura: float):

    temperatura_kelvin = temperatura + 273.15

    return "A temperatura em %.1f° Celsius equivale à %.1f° Kelvin" % (temperatura, temperatura_kelvin)


def celsius_rankine (temperatura: float):

    temperatura_rankine = (temperatura - 491.67) * 5 / 9

    return "A temperatura em %.1f° Celsius equivale à %.1f° Rankine" % (temperatura, temperatura_rankine)


def kelvin_fahrenheit (temperatura: float):

    temperatura_fahrenheit = (temperatura - 273.15) * 9 / 5 + 32

    return "A temperatura em %.1f° Kelvin equivale à %.1f° Fahrenheit" % (temperatura, temperatura_fahrenheit)


def kelvin_celsius (temperatura: float):

    temperatura_celsius = temperatura - 273.15

    return "A temperatura em %.1f° Kelvin equivale à %.1f° Celsius" % (temperatura, temperatura_celsius)


def kelvin_rankine (temperatura: float):

    temperatura_rankine = temperatura * 9 / 5

    return "A temperatura em %.1f° Kelvin equivale à %.1f° Rankine" % (temperatura, temperatura_rankine)


def rankine_fahrenheit (temperatura: float):

    temperatura_fahrenheit = temperatura - 459.67

    return  "A temperatura em %.1f° Rankine equivale à %.1f° Fahrenheit" % (temperatura, temperatura_fahrenheit)


def rankine_celsius (temperatura: float):

    temperatura_celsius = (temperatura - 491.67) * 5 / 9

    return "A temperatura em %.1f° Rankine equivale à %.1f° Celsius" % (temperatura, temperatura_celsius)


def rankine_kelvin (temperatura: float):

    temperatura_kelvin = temperatura * 5 / 9

    return "A temperatura em %.1f° Rankine equivale à %.1f° Kelvin" % (temperatura, temperatura_kelvin)