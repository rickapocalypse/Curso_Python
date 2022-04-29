v = []

for n in range(5):
    v.append([0] * 5)
    v[n][n] = 1

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in v]))
