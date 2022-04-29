import random

v = []
c = 0
while c < 11:
    v.append(random.randrange(-10, 10))
    c += 1

print(v)


for n in v:
    if n < 0:
        v[v.index(n)] = 0

print(v)
