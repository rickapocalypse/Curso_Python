import os
os.chdir('Exercicios_arquivos')

with open('lista_compra.txt', 'r') as arquivo:
    lines = arquivo.read()
shopping = lines.split('\n')

shopping_cart = []

for itens in shopping:
    shopping_cart.append(itens.split(' '))

if len(shopping_cart[-1]) <= 1:
    shopping_cart.pop()

total_price = 0
print(shopping_cart)
for itens in shopping_cart:

    total_price = total_price + float(itens[0])*float(itens[-1])

print(f'O total da compra é {total_price}')