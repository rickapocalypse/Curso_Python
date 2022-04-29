"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma das estruturas
for(int i = 0; i < limitador; i++){    #para java
    \\execução do loop

}

Python

for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis 

Exemplo de iteráveis
- String
    nome = 'geek university'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    números = range(1, 10)

nome = 'geek university'
lista =[1, 3, 5, 7, 9] #list(input('informe 3 números')) #[1, 3, 5, 7, 9]
numeros = range(1, 10) #tem que transformar em uma lista 

# Exemplo de for 1 (string)

for letra in nome:
    print(letra)

# Exemplo de for 2 (lista)

for numero in lista:
    print(numero)


# Exemplo de for 3 (range)
#range(valor_inicial, valor_final) O valor final não incluído 
for numero in range(1, 10):
    print(numero)


for valor in enumerate(nome):
    print(valor) 


nome = ' pinto'
for letra in nome:
    print(letra) 
"""

nome = ' pinto'
for letra in range(1,30):
    print('\U0001F633' * letra) 