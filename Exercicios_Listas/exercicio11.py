import random
vposi = []
vnega = []
c = 0

while c < 11:
    x = random.uniform(-10.0, 10.0)
    if x > 0:
        vposi.append(x)
    else:
        vnega.append(x)
    c += 1
print(vposi + vnega)
print(f'Existem {len(vnega)} numero negativos')
print(f'A soma dos valores positivos é {sum(vposi)}')
