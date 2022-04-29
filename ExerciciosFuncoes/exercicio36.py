from exercicio20 import fatorial

def super_fatorial(num):
    n = 0
    sfatorial = 1
    
    while num > n:
        n += 1
        sfatorial = sfatorial * fatorial(n)
    return sfatorial

print(super_fatorial(4))