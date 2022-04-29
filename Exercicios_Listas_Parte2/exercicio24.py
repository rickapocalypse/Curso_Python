from abc import abstractproperty
import random
a = []
x = 20

for l in range(x):
    a.append([])
    for c in range(x):
        a[l].append(random.randrange(1, 99))

diagonal = []
vertical = []
horizontal = []


for l in range(x):
    diagonal.append([])
    vertical.append([])
    horizontal.append([])
    for c in range(x):
        diagonal[l].append(0)
        vertical[l].append(0)
        horizontal[l].append(0)
        if c <= 16:
            horizontal[l][c] = a[l][c] * a[l][c+1] * a[l][c+2] * a[l][c+3]
        if l <= 16:
            vertical[l][c] = a[l][c] * a[l + 1][c] * a[l+2][c] * a[l+3][c]
        if c <= 16 and l <= 16:
            diagonal[l][c] = a[l][c] * a[l+1][c+1] * a[l+2][c+2] * a[l+3][c+3]

horizontal_list = []
vertical_list = []
diagonal_list = []

for l in range(x):
    for c in range(x):
        horizontal_list.append(horizontal[l][c])
        vertical_list.append(vertical[l][c])
        diagonal_list.append(diagonal[l][c])

maior_vert = max(vertical_list)
maior_hori = max(horizontal_list)
maior_diag = max(diagonal_list)

if maior_vert > maior_hori and maior_vert > maior_diag:
    print(
        f'O maior produto de 4 elementos da matriz foi na vertical e deu {maior_vert}')
elif maior_hori > maior_vert and maior_hori > maior_diag:
    print(
        f'O maior produto de 4 elementos da matriz foi na horizontal e deu {maior_hori}')
elif maior_diag > maior_vert and maior_diag > maior_hori:
    print(
        f'O maior produto de 4 elementos da matriz foi na diagonal e deu {maior_diag}')
