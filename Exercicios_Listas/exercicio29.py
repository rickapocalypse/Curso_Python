import random
v = []
c = 0

while c < 6:
    v.append(random.randrange(1, 100))
    c += 1
vpar = []
quant_imp = []
for n in range(1, len(v)):
    if v[n] % 2 == 0:
        print(f'{v[n]} é par')
        vpar.append(v[n])
    else:
        print(f'{v[n]} é ímpar')
        quant_imp.append(1)
print(f'{sum(vpar)} é a soma de todos os pares')
print(f'{sum(quant_imp)} vezes em que apareceu numeros ímpares')
print(v)
