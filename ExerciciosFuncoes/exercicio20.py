def fatorial(num1):
    atualiza_fator = 1
    for n in range(num1):
        recebe_fator = 0
        recebe_fator = num1 - n
        atualiza_fator = atualiza_fator * recebe_fator
    return atualiza_fator

