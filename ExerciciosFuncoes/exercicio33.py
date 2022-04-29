def fatorial(num):
    fatorial = 1
    for n in range(num):
        fatorial = fatorial * (num - n)
    print(fatorial)
    return fatorial

def soma(num):
    x = str(fatorial(num))
    soma = 0
    for n in x:
        soma = soma + int(n)
    return soma


print(soma(4))

