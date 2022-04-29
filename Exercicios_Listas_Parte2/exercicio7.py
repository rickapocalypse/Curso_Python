A = []

for i in range(10):
    line = []
    for j in range(10):
        if i < j:
            line.append(2*i + 7*j - 2)
        elif i == j:
            line.append(3*i**2 - 1)
        else:
            line.append(4*i**3 - 5*j**2 + 1)
    A.append(line)

print('\n'.join([''.join(['{:10}'.format(item) for item in row])
                 for row in A]))
