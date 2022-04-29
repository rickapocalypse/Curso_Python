from exercicio20 import fatorial

def hiper_fatorial(num):
    n = 0
    hfatorial = 1

    while num > n:
        n +=1
        hfatorial = hfatorial * n**n
    
    return hfatorial

print(hiper_fatorial(5)) 
