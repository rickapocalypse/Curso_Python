v = []
c = 0
soma = 0

while c < 101:
    soma += 1
    if soma % 7 != 0:
        v.append(soma)
        c += 1
print(v)
