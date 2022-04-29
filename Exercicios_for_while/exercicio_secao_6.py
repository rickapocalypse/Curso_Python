qtd = int(input('Quantos numeros vc gostaria de escolher ? '))


maior = 0
cotg = 0


for n in range(1, qtd + 1):
    num = float(input(f'Informe um numero aqui. {n} de {qtd} '))
    if num > maior :
        maior = num

        cotg = 1

    elif num == maior:
        cotg += 1

print (f'O maior numero foi {maior} e apareceu {cotg} vezes')


