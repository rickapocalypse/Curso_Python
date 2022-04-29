import random
indice = []
x = []
y = []
while len(indice) < 5:
    indice.append(1)
    x.append(random.randrange(1, 100))
    y.append(random.randrange(1, 100))
indice = []

print(x)
print(y)

for n in range(1, len(x)):
    print(f'A soma no indice {n} é {x [n] + y[n]}')
    print(f'O produto no indice {n} é {x [n] * y[n]}')
print(f'Todos os elementos presentes apenas no x são {set(x) - set(y)}')
print(f'A intersecção dos dois vetores é {set.intersection(set(x), set(y))}')
print(
    f'A união de todos os elementos dos vetores é {set.union(set(x), set(y))}')

