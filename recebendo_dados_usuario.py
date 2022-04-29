"""
Recebendo dados do usuário
input() -> Todo dado recebido via input é do tipo String
Qualquer
- aspas simples = 'Henrique'
- aspas dublas = "Henrique"
- 

"""
"""
#   exemplo de print antigo(tirar indentação)

    print("Qual o seu nome? ")
    nome = input()          #Entrada dados

    print('Seja bem-vindx %s' % nome)

    print('Qual a sua idade? ')

    idade = input()
    #   processamento

    #   Saída de dados
    print('Olá %s você tem %s anos ?' % (nome, idade ))
"""
"""
#   Exemplo de print moderno (tirar indentação)
    print('Qual o seu nome ?')
    nome = input()

    print('Seja bem_vindx {0}'.format(nome))

    print('Qual a sua idade?')
    idade=input()

    #   saida
    print('O {0} tem {1} anos de idade'.format(nome, idade))
"""
#Exemplo de print mais atual

nome=input('Qual o seu nome ?')

print(f'Seja bem-vindx {nome.title()}')

idade=int(input('Qual a sua idade?'))

print(f' {nome.title()} tem {idade} anos de idade e nasceu em {2020 - idade}')

#   saida   #
