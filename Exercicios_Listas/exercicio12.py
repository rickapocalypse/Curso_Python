import random
c = 0
v1 = []

while c < 6:
    v1.append(random.uniform(-100, 100))
    c += 1
print(v1)
print(min(v1))
print(max(v1))
print(sum(v1) / 5)
