import random
indice = []
v = []
while len(indice) < 10:
    indice.append(1)
    v.append(random.randrange(0, 10000))

vord = sorted(v)
print(vord)
for n in vord:
    print(n)
