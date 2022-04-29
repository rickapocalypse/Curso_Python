'''
POO - atributos

atributos -> Representam as características do objeto. Ou seja, pelos atributos, nós conseguimos 
representar computacionalmente os estados de um objeto.


atributos
    - atributo de Instancia:
    - atributo de classe:
    - atributo Dinâmico:

# atributo de instância: São atributos declarados dentro do método construtor.

# Método construtor: É um método especial utilizado para a construção do objeto.







'''


class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem             #__ no inicio faz ser private e só pode ser utilizado                            
        self.__cor = cor                       #dentro da class
        self.__ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    contador = 0
    imposto = 1.05 

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id

class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
    
    def mostra_senha(self):
        print(self.__senha)
    def mostra_email(self):
        print(self.email)


user1 = Usuario('rick.apocalypse@hotmail.com','123456789')
user2 = Usuario('leo.eiji@outlok.com', 'baiana')



user1.mostra_email()
user2.mostra_email()
user2.mostra_senha()





p1 = Produto('playstation 4', 'Video game', 2300)
p2 = Produto('xbox s', 'Video game', 4500)
p3 = Produto('bolacha', 'Alimento', 2)
print(p1.valor)
print(p1.id)
print(p2.id)
print(p3.valor)



# Atributo dinâmico

# É um produto de instancia que pode ser criado em tempo de execução

# obs : o atributo dinâmico será exclusivo da instância que o criou

p3.peso = '1kg'  # Note que na classe produto não tem peso

# uma instancia do objeto

print(p3.peso)

# Visualizar atributos
print(p1.__dict__)

# Deletando atributos

del p1.descricao

print(p1.__dict__)


