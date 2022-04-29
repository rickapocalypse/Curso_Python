"""
Escopo de variaveis

Escopo é o espaço onde existe e atua a tua variavel

1 - Variáveis Globais
     - Variavel globais são reconhecidas, ou seja, seu escopo compreende, todo o programa

2 - Variaveis locais
     - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada.



Para declarar vaiveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declarar uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos valor á mesma 
"""
numero = 11
print(numero)
print(type(numero))

if numero > 10:                            
    novo = numero + 10                  #novo no caso é uma variavel local. e ela não existe no escopo global se não atender a condição
    print(novo)

print(dir(novo))