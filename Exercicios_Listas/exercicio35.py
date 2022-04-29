import random
from typing import Deque
a = random.randrange(0, 10000)
b = random.randrange(0, 10000)
list1 = Deque(str(a))
list2 = Deque(str(b))

v1 = []
v2 = []

for n in list1:
    v1.append(int(n))

for n in list2:
    v2.append(int(n))

va = []
while len(v1) != 0:
    menor = min(v1)
    v1.pop(v1.index(menor))
    va.append(menor)
print(va)

vb = []
while len(v2) != 0:
    menor = min(v2)
    v2.pop(v2.index(menor))
    vb.append(menor)
print(vb)

print(va + vb)

# é mais fácil usar sorted()
