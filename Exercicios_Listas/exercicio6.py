a = []
c = 1
while c < 11:
    valor = int(input(f' Informe valores inteiro {c}/10 '))
    c += 1
    a.append(valor)
print(f'O seu vetor é {a}')
print(f'O maior valor informado foi {max(a)}')
print(f'E o menor valor informado foi {min(a)}')

indmin = a.index(min(a))

a.pop(indmin)

print(f' O segundo menor valor é {min(a)}')
