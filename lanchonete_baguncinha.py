import math
import os

productsFood = [
    {
        "id": 1, 
        "name": 'baguncinha',
        "price": 10
    },
    {
        "id": 2, 
        "name": 'x-tudo',
        "price": 0.10
    },
    {
        "id": 3, 
        "name": 'x-podrao',
        "price": 0.10
    }
]

productsFoodLabels = []
for pF in productsFood:
    productsFoodLabels.append(
        str(pF["id"]) + 
        " - " + 
        pF["name"] + 
        "......." + 
        "R$ " + 
        str(pF["price"])
    )

menus = {
    "start": {
        "title": "Menu inicial",
        "options": [
            '1 - lanches',
            '2 - bebidas',
            '3 - mostrar pedido',
            '4 - finalizar'
        ]
    },
    "food": {
        "title": "Menu de lanches",
        "options": [
            *productsFoodLabels,
            '4 - voltar ao menu inicial'
        ]
    },
    "drink" :{
        "title": "Menu de bebidas",
        "options" :[
            '1 - suco',
            '2 - refrigerante',
            '3 - cerveja',
            '4 - voltar ao menu inicial'
        ]
    },
    "order" :{
        "title": "Revisão de pedido",
        "options" :[
            '1 - Alterar pedido',
            '2 - voltar ao menu inicial',
            '3 - finalizar pedido'
        ]
    }
}

def isNaN(value):
    try:
        math.isnan(float(value))
        return True
    except:
        return False

def inputNumber(label):
    option = input(label)
    if(isNaN(option)):
        option = int(option)
        return option
    else:
        print("Digite uma opção valida...")
        return False

def printMenu(menuName):
    menu = menus[menuName]
    print(menu["title"])
    print('Escolha uma opção:')
    for option in menu["options"]:
        print(option)

def limpTela():
    os.system('cls')

# Inicial
def menuInicialService(option):
    match option:
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return 4

def menuInicial():
    printMenu('start')
    option = inputNumber(f'No que posso te ajudar? ')
    if(option):
        return menuInicialService(option)
    else:
        print("Digite uma opção valida...")
        menuInicial()
    limpTela()
# ==============

# Lanches
def menuLanchesService(option):
    match option:
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return 4

def menuLanches():
    printMenu('food')
    option = int(input(f'No que posso te ajudar? '))
    limpTela()
    return menuLanchesService(option)
# ==============

# Bebida
def menuBebidaService(option):
    match option:
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return 4

def menuBebida():
    printMenu('drink')
    menuBebidaOption = int(input(f'No que posso te ajudar? '))
    limpTela()
    return menuBebidaService(menuBebidaOption)
# ==============

# Pedido
def menuPedidoService(option):
    match option:
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return 4

def menuPedido():
    print(carrinho())
    printMenu('order')
    menuPedidoOption = int(input(f'No que posso te ajudar? '))
    limpTela()
    return menuPedidoService(menuPedidoOption)
# ==============

def carrinho():
    carrinho = {}
    for n in pedido:
        c = pedido.count(n)
        carrinho.update({n: c})
    limpTela()
    return(carrinho)

pedido = []

def start():
    while True:
        menuInicialOption = menuInicial()
        limpTela()
        match menuInicialOption:
            # Lanches
            case 1:
                menuLanchesOption = menuLanches()
                print(productsFood[menuLanchesOption - 1]["name"])
                pedido.append(productsFood[menuLanchesOption - 1]["name"])
                # match menuLanchesOption:
                #     case 1:
                #         print('baguncinha adicionada ao pedido')
                #         pedido.append('baguncinha')
                #     case 2:            
                #         print('x-tudo foi adicionado ao pedido')
                #         pedido.append('x-tudo')
                #     case 3:
                #         print('x-podrao foi adicionado ao pedido')
                #         pedido.append('x-podrao')
                #     case 4:
                #         print('voltar ao menu inicial')
            
            # Bebidas
            case 2:
                menuBebidaOption = menuBebida()
                match menuBebidaOption:
                    case 1:
                        print('suco foi adicionado ao pedido')
                        pedido.append('suco')
                    case 2:
                        print('refrigerante foi adicionado ao pedido')
                        pedido.append('refrigerante')
                    case 3:
                        print('cerveja foi adicionado ao pedido')
                        pedido.append('cerveja')
                    case 4:
                        print('voltar ao menu inicial')
            # Pedido
            case 3:
                menuPedidoOption = menuPedido()
                match menuPedidoOption:
                    case 1:
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
                            print(carrinho())
                    
                    case 2:
                        print('voltar ao menu inicial')
                    case 3:
                        print(f'Seu pedido é: {pedido}')
                        break

            # Finalizar 
            case 4:
                print('Pedido finalizado')
                print(f'O seu pedido é: {carrinho()}')
                break

            case _:
                break
start()
