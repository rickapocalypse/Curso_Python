import random
v1 = []
v2 = []
c = 0

while c < 6:
    v1.append(random.randrange(1, 100))
    v2.append(random.randrange(1, 100))
    c += 1
print(v1)
print(v2)

for n in v1:
    index = v1.index(n)
    print(v1[index] * v2[index])