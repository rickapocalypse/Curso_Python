"""
Definição de funções 

- Funções são pequenos partes de código que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

"""

# utilizando funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

# print(cores)
"""
def nome_da_funcao(parametros_de_entrada):
    bloco_da_função


Onde:

nome_da_funcao -> Sempre, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não;
bloco_da_funcao -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece;
Neste bloco, pode ter ou não retorno da função.
"""

# Definindo uma função


def diz_oi():
    print('oi!')

# Chamando a função


diz_oi()


def cantar_parabens():
    print('Parabens para voce')
    print('Nesta data querida')
    print('Muitas felicidades')


canta = cantar_parabens

canta()
