import random
v = []
v1 = []
v2 = []

c = 0

while c < 10:
    c += 1
    x = random.randrange(1, 100)
    v.append(x)
    if x % 2 == 0:
        v1.append(x)
    else:
        v2.append(x)
print(f'O vetor impar {v2}')
print(f'O vetor par {v1}')
