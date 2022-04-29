num = int(1000)
cp = 0
ci = 0

for n in range(1, num +1):
    if n % 2 == 0:
        cp += 1
    else:
        ci += 1

print(f' A quantidade de numeros par é {cp} e impar é {ci} e o total de dados lidos foi {cp + ci}')


