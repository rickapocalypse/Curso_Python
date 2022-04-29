import random
indice = []
v = []

while len(indice) < 15:
    indice.append(1)
    v.append(random.randrange(0, 10))
print(v)

for n in v:
    if n == 0:
        v.pop(v.index(n))
print(v)
