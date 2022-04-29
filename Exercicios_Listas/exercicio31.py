import random
from typing import Counter
indice = []
v1 = []
v2 = []
while len(indice) < 10:
    indice.append('loop')
    v1.append(random.randrange(1, 100))
    v2.append(random.randrange(1, 100))
v_uniao = set.union(set(v1), set(v2))

print(v1)
print(v2)
print(v_uniao)
