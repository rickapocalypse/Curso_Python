def maior_fator_primo(num1):
    p = 2
    fatores = []
    while p < num1 + 1:
        if num1 % p == 0:
            num1 = num1 / p
            fatores.append(p)
        else:
            p += 1
    print(fatores)
    print(f'E o maior fator primo é {max(fatores)}')


maior_fator_primo(322)