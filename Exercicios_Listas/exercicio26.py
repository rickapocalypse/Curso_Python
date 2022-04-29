import math
import random
c = 0
v = []

while c < 11:
    v.append(random.randrange(1, 10))
    c += 1
print(v)
m = sum(v) / len(v)
print(m)

for n in range(1, len(v)):
    desv = math.sqrt(1/(len(v)) * (v[n] - m)**2)
print(desv)
