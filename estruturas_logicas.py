"""
Estruturas lógicas: and(e), or (ou), not (não), is (é)

Operadores Unários:
    -not, is
Operadores Binários:
    -and, or


Para o 'and', ambos precisam ser True
Para o 'or', um ou outro precisa ser True
Para o 'not', o valor do booleano é invertido
Para o 'is',  o valor é comparado com um segundo
"""
ativo = True
logado = False

if ativo and logado:
    print('Bem vindo usuário') 
else:
    print('Você precisa ativas a sua conta. Por favor, cheque o seu e-mail')


# Ativo é falso ? 
print(ativo is False)