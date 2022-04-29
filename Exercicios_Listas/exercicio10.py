import random         # Usando numero aléatorios para não ter que escrever as 15 notas
nota = []
c = 0

while c < 16:
    nota.append(random.randrange(1, 10))
    c += 1
print(nota)

print(sum(nota) / 15)
