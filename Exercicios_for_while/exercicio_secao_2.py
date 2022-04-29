qtd = int(input('Informe a quantidade de nota que colocara '))
nota = 0

for n in range(1, qtd +1):
    num = float(input(f'Informe a {n}° nota'))
    if num < 0:
        print(f'Não aceitamos a nota {num} pois se trata de um negativo')
        break
    else:
        nota = nota + num

notaf= nota / qtd

if nota >= 0:
    print(notaf)
else:
    print('tente novamente')