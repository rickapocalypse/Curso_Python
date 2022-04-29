import random
v1 = []
c = 0

while c < 6:
    v1.append(random.randrange(1, 100))
    c += 1

print(v1)

for n in v1:
    print(f'O {v1[v1.index(n)]} está na posição {v1.index(n)}')
