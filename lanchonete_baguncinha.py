
def limpTela():
    print('\n' * 100)

def menu1():
    print('Escolha uma opção')
    print('1 - lanches')
    print('2 - bebidas')
    print('3 - mostrar pedido')
    print('4 - finalizar')
    x = int(input(f'No que posso te ajudar? '))
    limpTela()
    return x

def menu2():
    print('1 - baguncinha')
    print('2 - x-tudo')
    print('3 - x-podrao')
    print('4 - voltar ao menu inicial')
    x = int(input(f'No que posso te ajudar? '))
    limpTela()
    return x

def menu3():
    print('1 - suco')
    print('2 - refrigerante')
    print('3 - cerveja')
    print('4 - voltar ao menu inicial')
    x = int(input(f'No que posso te ajudar? '))
    limpTela()
    return x

def menu4():
    print(carrinho1())
    print('1 - Alterar pedido')
    print('2 - voltar ao menu inicial')
    print('3 - finalizar pedido')
    x = int(input(f'No que posso te ajudar? '))
    limpTela()
    return x

def carrinho1():
    for n in pedido:
        c = pedido.count(n)
        carrinho.update({n: c})
    return(carrinho)

carrinho = {}
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
        x = menu4()
        if x == 1:
            c = 1
            print('0 - Para voltar ao menu inicial')
            
            for n in pedido:
                print(f'{c} - {n}')
                c += 1
            p = int(input(('Deseja retirar ou voltar ao menu: ')))
            
            if p == 0:
                print('voltar ao menu inicial')
            else:
                pedido.pop(p-1)
                print(carrinho1())
        
        elif x == 2:
            print('voltar ao menu inicial')
        elif x == 3:
            print(f'Seu pedido é: {pedido}')
            break
    elif x == 4:
        print('Pedido finalizado')
        print(f'O seu pedido é: {pedido}')
        break