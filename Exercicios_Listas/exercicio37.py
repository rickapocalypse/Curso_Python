import random
indice = []
v = []

while len(indice) < 11:
    indice.append(1)
    v.append(random.randrange(0, 10))

print(v)
vetor = list(range(0, 11))
inicial = 0
j = 10
final = 0


while len(v) != 0:
    minimo = min(v)

    if inicial <= final:
        vetor[inicial] = minimo
        inicial += 1
    else:
        vetor[j] = minimo
        j -= 1
        final += 1
    v.pop(v.index(min(v)))

print(vetor)
