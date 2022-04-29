from collections import Counter
import random
v1 = []
c = 1

while c < 11:
    v1.append(random.randrange(1, 10))
    c += 1

print(v1)
print(f'O maior elemento do vetor é {max(v1)}.')
print(f'E ele se encontra na posição {v1.index(max(v1)) + 1}')

valor = v1.index(max(v1))
res = Counter(v1)

print(f'O {max(res)} apareceu {res[max(res)]}')
pos1 = v1.index(max(v1))
rep = res[max(res)]
if rep > 1:
    print(
        f'O {max(v1)} também aparece na posição {v1.index(max(v1), pos1 + 1) +1 }')
    pos2 = v1.index(max(v1), pos1) + 1

    if rep > 2:
        print(
            f'O {max(v1)} também aparece na posição {v1.index(max(v1), pos2 + 1) + 1 }')
