indice = []
v = []
while len(indice) < 10:
    x = int(input(f'Insira um numero único. {len(indice)}/10 '))
    if x in v:
        print(
            f'O numero {x} já foi adicionado, tente adicionar outro a seguir')
    else:
        indice.append(1)
        v.append(x)

print(v)
