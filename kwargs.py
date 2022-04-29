"""
**kwargs

Poderiamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais  um parâmetro, mas diferente do *args que coloca os valores extras 
em uma tupla, o ** exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.



# Exemplo

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')



# Exemplo 2

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


# OBS: os parâmetros *args e **kwargs não são obrigatórios 



def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'Você recebeu um cumprimento pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza de quem você é'

print(cumprimento_especial())
print(cumprimento_especial(geek = 'python'))



# Nas nossas funções, podemos ter(Nessa ordem):

- Parâmetros obrigatorios
- *args:
- Parâmetros default (não obrigatorio):
- **kwargs:

exemplo:


def minha_funcao(idade, nome, *args, solteiro = False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felipe', 4, 5, 3, solteiro=True)
minha_funcao(34, 'felps', eu = 'não', voce='vai')
minha_funcao(19, 'Carla', 9,4,3, java = False, python=True)


# Entenda por que é importante manter a ordem dos parâmetros na declaração



def mostra_info(a, b,*args, instrutor ='geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

#
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
#

print(mostra_info(1,2,3, sobrenome='University', cargo='Instrutor'))

"""

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

list = [1, 2, 3]
tuple =(1, 2, 3)
set = {1, 2, 3}
dic = dict(a = 1, b = 2, c = 3)  # tem que receber a mesma chave

soma_multiplos_numeros(*list)
soma_multiplos_numeros(*tuple)
soma_multiplos_numeros(*set)
soma_multiplos_numeros(**dic)   # com 1 # desempacota as chaves

# * desempacota