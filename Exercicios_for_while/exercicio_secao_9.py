import random
num = int(input('Quantas vezes vamos jogar a moeda ?'))
prob = []
c = 0
k = 0
for n in range(1, num + 1):
    x = random.randint(1, 100)

    if x <= 50:
        c = + 1
        prob.append('c')
    else:
        k = + 1
        prob.append('k')

    # prob.sort()
print(prob)
p = prob.count('c')
print(f'Apareceu {p} caras em um total de {num} jogadas ')
