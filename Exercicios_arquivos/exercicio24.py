#! py -3.10
# ESTOQUE
# Crie um programa que leia o nome de um produto e a quantidade disponível.


import os
import math
os.chdir('Exercicios_arquivos')

menus = {
    'start': {
        'title' : '\n====Menu Principal====\n',
        'options': [
            '1 - Adicionar Produto',
            '2 - Remover Produto',
            '3 - Listar e alterar Produtos',
            '0 - Finalizar inspeção']
    },
    'Adicionar Produto': {
        'title' : 'Adicionando Produto',
        'options': [
            '1 - Para digitar o nome do produto: ',
            '0 - Para voltar ao Menu Principal',
        ]
    },
    'Remover Produto': {
        'title' : 'Removendo Produto',
        'options': [
            '1 - Para digitar o nome do produto: ',
            '0 - Voltar ao Menu Principal',
        ]
    },
    'Listar Produtos': {
        'title' : 'Listando Produtos',
        'options': [
            '1 - Para listar todos os produtos: ',
            '2 - Encontrar Produto especifico: ',
            '3 - Alterar quantidade de produtos: ',
            '0 - Voltar ao Menu Principal',
        ]
    }
}   

def cleanMenu():
    os.system('cls')

def nonValue(value):
    try:
        math.isnan(float(value)) or value == 0
        return True
    except:
        return False

def inputNumber(label):
    option = input(label)
    if(nonValue(option) or (option == 0)):
        option = int(option)
        return option
    else:
        print("Digite uma opção valida...")
        return False

def printMenu(menuName):
    menu = menus[menuName]
    print(menu["title"])
    print('\nEscolha uma opção:')
    for option in menu["options"]:
        print(option)

# Inicial
def menuInicialOption(option):
    match option:
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 0: 
            return 0

def menuInicial():
    cleanMenu()
    printMenu('start')
    option = inputNumber('Escolha uma opção:')
    if(option) or (option == 0):
        return menuInicialOption(option)
    else:
        print("Digite uma opção valida...")
        menuInicial()

# Adicionar Produto
def menuAdicionarProdutoOption(option):
    match option:
        case 1:
            return 1
        case 0:
            return 0

def menuAdicionarProduto():
    cleanMenu()
    printMenu('Adicionar Produto')
    option = inputNumber('Digite um opção: ')
    print(option)
    if(option) and (option == 1):
        cleanMenu()
        product = input('Digite o nome do produto: ')
        quantity = input('Digite a quantidade do produto: ')
        with open('products.txt', 'a') as file:
            file.write(f'{product.lower()} - {quantity}\n')
        return menuAdicionarProduto()
    elif (option == 0):
        return 0
    else:
        print("Digite uma opção valida...")
        return menuAdicionarProduto()
    
# Menu remover produto
def menuRemoverProdutoOption(option):
    match option:
        case 1:
            return 1
        case 0:
            return 0

def menuRemoverProduto():
    cleanMenu()
    printMenu('Remover Produto')
    option = inputNumber('Digite um opção: ')
    if(option) and (option == 1):
        product = input('Digite o nome do produto: ')
        with open('products.txt', 'r') as file:
            lines = file.readlines()
        with open('products.txt', 'w') as file:
            for line in lines:
                if(line.find(product) == -1):
                    file.write(line.lower())
        return menuRemoverProduto()
    elif(option == 0):
        return 0

# Menu listar produtos
def menuListarProdutosOption(option):
    match option:
        case 1:
            return 1
        case 0:
            return 0

def menuListarProdutos():
    cleanMenu()
    printMenu('Listar Produtos')
    option = inputNumber('Digite um opção: ')
    if(option) and (option == 1):
        with open('products.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            print(line)
        waitTime = inputNumber('Pressione qualquer botão para continuar: ')
        cleanMenu()
        return menuListarProdutos()

    if(option) and (option == 2):   # Encontrar produto especifico
        cleanMenu()
        product = input('Digite o nome do produto: ').lower()
        with open('products.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            if(line.find(product) != -1):
                find = True
                line = line
                break
            else:
                line = product
                find = False
        if (find):
            print(f'O produto {line.split()[0]} tem {line.split()[2]} unidades no estoque')
        else:   
            print(f'O produto {line.split()[0]} não está no estoque')     
        waitTime = inputNumber('Pressione qualquer botão para continuar: ')
        cleanMenu()

    elif(option == 0):
        cleanMenu()
        return 0


def start():
    while True:
        menuInicialOption = menuInicial()
        cleanMenu()
        match menuInicialOption:
            case 1:
                menuAdicionarProduto()
            case 2:
                menuRemoverProduto()
            case 3:
                menuListarProdutos()
            case 0:
                print('Finalizando...')
                break

start()