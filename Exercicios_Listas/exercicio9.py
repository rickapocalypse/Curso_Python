import random
vpar = []
vimp = []
c = 0

while c < 7:
    x = random.randrange(1, 100)
    if x % 2 == 0:
        vpar.append(x)
        c += 1
    else:
        vimp.append(x)
print(vpar)

print(vimp)

print(vpar[::-1])
