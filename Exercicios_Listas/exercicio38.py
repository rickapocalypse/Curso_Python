indice = []
v = []
while len(indice) < 10:
    x = int(
        input(f'Adicione numeros, e te mostrarei eles em ordem. {len(indice)} / 10 '))
    indice.append(1)
    v.append(x)
    g = sorted(v)

print(g)
for n in g:
    print(n)
