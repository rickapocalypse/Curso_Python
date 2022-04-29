import random
v = []
c = 0

while c < 10:
    v.append(random.randrange(1, 100))
    c += 1
print(v)
for n in range(1, len(v)):
    pontos_de_divisao = 0
    for p in range(2, v[n]):
        if v[n] % p == 0:
            #print(f'{v[n]} não é primo e {p} é um dos seus divisores ')
            pontos_de_divisao += 1

    if pontos_de_divisao == 0:
        if v[n] != 1:
            print(f'{v[n]} é primo e está na posição {v.index(v[n])}')
