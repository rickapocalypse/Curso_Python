num1 = int(input("informe um numero"))
u = num1 // 1 % 10
d = num1 // 10 % 10
c = num1 // 100 % 10
m = num1 // 1000 % 10
b = num1 // 10000 % 10
t = num1 // 100000 % 10
q = num1 // 1000000 % 10

if num1 >= 0:
    print(f'A soma de cada digito é {u + d + c + m + b + t + q}. E os dígitos dados foram {t}{b}{m}{c}{d}{u}{q}')
else:
    print(f'O numero é invalido')

