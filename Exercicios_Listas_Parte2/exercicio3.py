A = []

for l in range(4):
    line = []
    for c in range(4):
        line.append(l * c)
    A.append(line)


print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))
