def kw_cv (kilowatts: float):

    cv = kilowatts * 1.36

    return "%.2f kilowatts equivalem à %.2f Cavalos" % (kilowatts, cv)


def cv_kw (cavalos: float):

    kw = cavalos / 1.36

    return "%.2f cavalos equivalem à %.2f Kilowatts" % (cavalos, kw)