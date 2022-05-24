
def menu1():
    print('Escolha uma opção')
    print('1 - lanches')
    print('2 - bebidas')
    print('3 - mostrar pedido')
    print('4 - sair')
    x = int(input(f'No que posso te ajudar? '))
    return x

def menu2():
    print('1 - baguncinha')
    print('2 - x-tudo')
    print('3 - x-podrao')
    print('4 - voltar ao menu inicial')
    x = int(input(f'No que posso te ajudar? '))
    return x

def menu3():
    print('1 - suco')
    print('2 - refrigerante')
    print('3 - cerveja')
    print('4 - voltar ao menu inicial')
    x = int(input(f'No que posso te ajudar? '))
    return x

pedido = []

while True:
    x = menu1()
    if x == 1:
        x = menu2()
        if x == 1:
            print('baguncinha adicionada ao pedido')
            pedido.append('baguncinha')
        elif x == 2:            
            print('x-tudo foi adicionado ao pedido')
            pedido.append('x-tudo')
        elif x == 3:
            print('x-podrao foi adicionado ao pedido')
            pedido.append('x-podrao')
        elif x == 4:
            print('voltar ao menu inicial')
    elif x == 2:
        x = menu3()
        if x == 1:
            print('suco foi adicionado ao pedido')
            pedido.append('suco')
        elif x == 2:
            print('refrigerante foi adicionado ao pedido')
            pedido.append('refrigerante')
        elif x == 3:
            print('cerveja foi adicionado ao pedido')
            pedido.append('cerveja')
        elif x == 4:
            print('voltar ao menu inicial')
    elif x == 3:
        print(pedido)
    elif x == 4:
        print('sair')
        print(f'Seu pedido é: {pedido}')
        break