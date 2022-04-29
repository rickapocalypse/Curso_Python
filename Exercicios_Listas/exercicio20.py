import random
v = []
vimp = []
c = 0

while c < 11:
    v.append(random.randrange(0, 50))
    c += 1

for n in v:
    if n % 2 != 0:
        vimp.append(n)

print(v)
print(vimp)
