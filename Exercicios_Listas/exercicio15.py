import random
from typing import Counter


c = 0
v = []

while c < 21:
    v.append(random.randrange(1, 10))
    c += 1

vordem = sorted(v)
print(vordem)
print(set(vordem))

