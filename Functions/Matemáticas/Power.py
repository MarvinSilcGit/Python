def kw_cv (kilowatts: float):

    cv = kilowatts * 1.36

    return f"{kilowatts:,.2f} kilowatts equivalem à {cv:,.2f} Cavalos"


def cv_kw (cavalos: float):

    kw = cavalos / 1.36

    return f"{cavalos:,.2f} Cavalos equivalem à {kw:,.2f} Kilowatts"


def consumo_aparelho (volts: float, amperes: float):

    return f"Com {volts:,.2f}v e {amperes:,.2f}A, a potência máxima será {volts * amperes:,.2f} Watts"

print(consumo_aparelho(12,5))