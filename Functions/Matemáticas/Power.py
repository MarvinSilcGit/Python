def kw_cv (kilowatts: float):

    cv = kilowatts * 1.36

    return f"{kilowatts:,.2f} kilowatts equivalem à {cv:,.2f} Cavalos"


def cv_kw (cavalos: float):

    kw = cavalos / 1.36

    return f"{cavalos:,.2f} Cavalos equivalem à {kw:,.2f} Kilowatts"