'''
Sistema de arquivos de navegação

Para fazer uso de manipulação de arquivos do sistema operacional precisamos importar e
usar a biblioteca os

os -> Operacional System - sistema operacional

# Fazer o import
import os

# getcwd() -> Retorna o diretório atual

print(os.getcwd())

#para mudar o diretório chdir()

os.chdir('..')

print(os.getcwd())

# Podemos checar se o diretório é absoluto ou relativo

print(os.path.isabs('/home/'))
'''

import os

print(os.name)