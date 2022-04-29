import random

v = []
c = 0

while c < 6:
    v.append(random.randrange(-10, 10))
    c += 1

print(v)

res = sum(v)

if res == 0:
    print(f'O resultado foi {res}. Finalizando o programa.')
elif res == 1:
    print(f'Como o resultado foi {res} então o seu vetor é: {v}')
elif res == 2:
    print(f'Como o resultado foi {res} então o seu vetor é: {v[::-1]}')
else:
    print('Código invalido')
