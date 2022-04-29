import random
v1 = []
c = 0

while c < 7:
    v1.append(random.randrange(1, 100))
    c += 1
print(v1)
print(v1[::-1])


