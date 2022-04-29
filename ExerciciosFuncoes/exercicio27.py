from exercicio20 import fatorial
import math

def sinTaylor(graus,num = 5):
    sinx = 0
    for n in range(0, num + 1):
        sinx = sinx + (((-1) ** n) * graus ** (2*n + 1)) / fatorial(2 * n + 1)
    return sinx

x = sinTaylor(math.pi / 4)
print(x)