from exercicio20 import fatorial
import math

def grausRadiano(graus):
    rad = (math.pi * graus)/180
    return rad


def cosTaylor(graus, num = 5):
    cosx = 0
    for n in range(0, num + 1):
        cosx = cosx + (((-1) ** n) * grausRadiano(graus) ** (2*n)) / fatorial(2 * n)
    return cosx

x = cosTaylor(45)
print(x)