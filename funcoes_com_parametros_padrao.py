"""
Funções com parâmetros Padrão

- Funções onde a passagem de parâmetro seja opcional;


print('Henrique')

print()

- é opcional no caso acima 

def quadrado(numero):
    return numero**2

print(quadrado(4))

- o parametro é obrigatório 

def exponencial(numero, potencia = 2):   # Colocando o = 2 é opcional o parametro 
    return numero ** potencia



def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que era um instrutor'
    return f'olá {nome}'


print(mostra_informacao(instrutor=True))
print(mostra_informacao('Henrique'))


def soma(num1, num2):
    return num1 + num2

def subtração(num1, num2):
    return num1 - num2

def mat(num1, num2, fun = soma):
    return fun(num1, num2)

print(mat(5,1,subtração))



# Escopo - Evitar problema e confusões...

# Variáveis globais 
# Variáveis locais

instrutor = 'henrique' # variavel global

def diz_oi():
    instrutor = 'Python' # Variavel local
    return f'oi {instrutor}'

print(diz_oi())

# Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência

# Variaveis locais não são reconhecidas fora do seus blocos

# Atenção com variaveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1  #A vaiavel está local está sendo utilizada para processamento sem ter sido inicializada
    return total

# Arrumando
 
total = 0


def incrementa():
    global total # Avisando que queremos utilizar a variavel local
    total = total + 1  
    return total


print(incrementa())
print(incrementa())
print(total)



"""



def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador =+ 1
        return contador
    return dentro()

print(3*fora())
