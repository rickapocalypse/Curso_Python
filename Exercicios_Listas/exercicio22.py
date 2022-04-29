import random
v1 = []
v2 = []
c = 0
while c < 11:
    v1.append(random.randrange(1, 100))
    v2.append(random.randrange(1, 100))
    c += 1

print(v1)
print(v2)

v3 = []

for n in v1:
    if n % 2 == 0:
        v3.append(n)
for n in v2:
    if n % 2 != 0:
        v3.append(n)
print(v3)
