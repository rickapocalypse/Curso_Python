"""
Funções com parametro de entrada

- funções que recebem dados para serem processados dentro da mesma

Funções podem:
- não possuem entrada
- não possuir saida
- possuem entrada mas não saida
- não possuem entra mas possuem saida
- possuem entrada e saida


"""


"""
def quadrado(numero):
    return numero*numero

print(quadrado(8))
"""
"""

def cantar_parabens(aniversariante):
    print(f'Parabens {aniversariante}')

cantar_parabens('henrique')

"""

# Funções podem ter n-parametros 

"""
def soma(a, b):
    return a + b
"""

# Parametros são as variaveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função


"""
keyword Arguments

Caso utilizemos nome dos parâmetros nos argumentos para informá-los, podemos
utilizar qualquer ordem


print(soma(b = 1, a = 2))
print(soma(a = 2, b = 1))  #Ordem não importa

"""



def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

