import random
v1 = []
c1 = 0
c2 = 0
npar = 0
while c1 < 11:
    v1.append(random.randrange(1, 1000))
    c1 += 1
print(v1)

for n in v1:
    if n % 2 == 0:
        print(n)
        npar = npar + n
        c2 += 1
print(f'O vetor contem {c2} numeros parés ')
print(f'A soma desses números pares é {npar}')
