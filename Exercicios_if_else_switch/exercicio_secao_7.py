import random


a = random.randint(1,99)
b = random.randint(1,99)
c = 0

res1 = int(input(f'1) Quanto é {a} + {b} ? '))

if res1 == a + b:
    c = c + 1
    print('Parabéns, vc ganhou 1 ponto')
else:
    c = c + 0
    print(f"vc errou, a resposta é {a + b}" )

a = random.randint(1,99)
b = random.randint(1,99)


res2 = int(input(f'2) Quanto é {a} + {b} ? '))

if res2 == a + b:
    c = c + 1
    print('Parabéns, vc ganhou 1 ponto')
else:
    c = c + 0
    print(f"vc errou, a resposta é {a + b}" )

a = random.randint(1,99)
b = random.randint(1,99)


res3 = int(input(f'3) Quanto é {a} + {b} ? '))

if res3 == a + b:
    c = c + 1
    print('Parabéns, vc ganhou 1 ponto')
else:
    c = c + 0
    print(f"vc errou, a resposta é {a + b}" )

a = random.randint(1,99)
b = random.randint(1,99)


res4 = int(input(f'4) Quanto é {a} + {b} ? '))

if res4 == a + b:
    c = c + 1
    print('Parabéns, vc ganhou 1 ponto')
else:
    c = c + 0
    print(f"vc errou, a resposta é {a + b}" )

a = random.randint(1,99)
b = random.randint(1,99)


res5 = int(input(f'5) Quanto é {a} + {b} ? '))

if res5 == a + b:
    c = c + 1
    print('Parabéns, vc ganhou 1 ponto')
else:
    c = c + 0
    print(f"vc errou, a resposta é {a + b}" )

print(f'Sua nota foi {c} / 5')