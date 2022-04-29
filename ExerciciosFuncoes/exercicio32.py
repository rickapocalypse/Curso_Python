def simplifica(num1, num2):
    maior = [num1, num2]
    divisores = []
    for n in range(1, max(maior)):
        if num1 % n == 0 and num2 % n == 0:
            divisores.append(n)
    return print(f'os divisores possíveis para essa fração {divisores}, e a fração simplificada é {num1 / max(divisores)} / {num2 / max(divisores)}')

simplifica(36,60)