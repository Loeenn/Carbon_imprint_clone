import math


def brutto(m, V):
    m = float(m)
    V = float(V)
    quintity_vagons = max(math.ceil(V/120), math.ceil(m/69000))
    return quintity_vagons * 23000 + m
