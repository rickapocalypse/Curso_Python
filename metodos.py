'''
POO - Metodos

- Metodos (funções) -> Representam os comportamentos do objeto. Ou seja, as
ações que esse objeto pode realizar no seu sistema

Dividimos os metodos, em dois grupos

# metodos de Instancia
'''

class Lampada:
    def __init__(self,cor, voltagem, luiminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luiminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem) / 100)

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuarios no sistema ')
    
    @staticmethod
    def definicao():
        return 'UXR344'


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 200000, salt_size=16)
        Usuario.contador = self.__id

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def NomeCompleto(self):
        return f'{self.__nome} {self.__sobrenome}'

    def __gera_usuario(self):         #Método privado
        return self.__email.split('@')[0]

p1 = Produto('Ps4', ' Video Game', 2300)

print(p1.desconto(10))
# ou
print(Produto.desconto(p1, 10))


user1 = Usuario('Henrique', 'Apocalypse', 'rick.apocalypse@hotmail.com', '123456')
user2 = Usuario('Bianca', 'Takano', 'TiankaBacano@hotmail.com', '123456')
user3 = Usuario('Leonardo', 'Eiji', 'leo-eiji@outlok.com', '123456')
""" 
senha = input('Informe a senha para acessar: ')

if user1.checa_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso negado')

print(user1._Usuario__senha)

print(user1.NomeCompleto())
# ou
print(Usuario.NomeCompleto(user1))
print(Usuario.NomeCompleto(user2))

"""

# Metodos de classe

Usuario.conta_usuarios()

print(user1._Usuario__gera_usuario())