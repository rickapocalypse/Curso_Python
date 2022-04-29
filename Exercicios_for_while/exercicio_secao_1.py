qtd = 10
soma = 0
for n in range(1, qtd+1):
    num=int(input(f'Informe um numero da soma {n}/{qtd} '))
    soma = soma + num
print(soma)