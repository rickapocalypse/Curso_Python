def Fatorial2(num):
    n = 0
    fatorial = 1
    while num > (2*n + 1):
        n += 1
        fatorial = fatorial * (2*n + 1)
    return fatorial

print(Fatorial2(5))