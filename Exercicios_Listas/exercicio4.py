import random
a = []
c = 0

while c < 9:
    a.append(random.randrange(0, 100))
    c += 1

print(a)


x = random.randrange(1, 9)

soma1 = a[x]

y = random.randrange(1, 9)

soma2 = a[y]

print(
    f' O indice do x é {x} e seu valor na matriz x={a[x]} e o indice de y é {y} y={a[y]}. Então a soma deles é {soma1 + soma2}')
