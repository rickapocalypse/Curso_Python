import random
va = []
vb = []
c = 0

while c < 11:
    va.append(random.randrange(1, 100))
    vb.append(random.randrange(1, 100))
    c += 1

print(va)
print(vb)

vc = []
for n in va:
    index = va.index(n)
    vc.append(va[index] - vb[index])

print(vc)
