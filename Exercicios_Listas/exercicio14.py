import random
from typing import Counter
v1 = []
c = 0
b = 0

while c < 10:
    v1.append(random.randrange(1, 10))
    c += 1

print(v1)

# Conta todos os elementos do meu vetor v1, colocando eles como chave e o numero de vezes que aparece como valor {chave:valor}
res = Counter(v1)
print(res)

for n in res:
    if res[n] > 1:
        print(f' O {n} se repete {res[n]} vezes')
