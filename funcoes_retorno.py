"""
Funções com retorno

"""

"""
def quadrado_de_7():
    return 7*7


ret = quadrado_de_7()

print(ret)
"""


"""
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
"""


"""
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
"""


# função para jogar moeda




import random
def joga_moeda():
    valor = random()
    if valor > 0.5:
        return "cara"
    return "coroa"
