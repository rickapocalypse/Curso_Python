"""
Estruturas condicionais
if, else, elif


"""

idade = int(input('Qual a sua idade ?'))

if idade < 18:                                  # o bloco inicial com os ":"
    print('menor de idade'.title())

elif idade == 18:
    print('Tem 18 anos'.title())
elif idade == 26:
    print('tem 26 anos'.title())
else:
    print('maior de idade'.title())


