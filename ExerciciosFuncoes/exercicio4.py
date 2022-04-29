

def quadra_int(num):
    if num ** 0.5 % 2 == 0:
        print(f'{num} é um quadrado perfeito de {int(num**0.5)}')
    else:
        print(f'{num} não é um quadrado perfeito, e sua raiz é {num **0.5} ')

quadra_int(6)