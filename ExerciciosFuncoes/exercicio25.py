def serie(num):
    valor = 0
    for n in range(1, num + 1):
        valor = valor + (n**2 + 1)/(n + 3)
    return print(valor)
serie(5)