import random
v = []
c = 0
while c < 11:
    v.append(random.randrange(1, 10))
    c += 1

print(v)

for n in set(v):
    for p in range(1, n + 1):
        if n % p == 0:
            print(f'{p} é um divisor inteiro de {n}')
