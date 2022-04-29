from exercicio20 import fatorial
def Fatorial4(num):
    n = 0
    fat4 = 1
    while num > ( fatorial(2*n) / fatorial(n)):
        n += 1
        fat4 = fat4 * ( fatorial(2*n) / fatorial(n))
    return fat4

print(Fatorial4(3))