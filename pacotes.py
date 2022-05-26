'''
Pacotes

Módulo é um arquivo Python que pode ter diversas funções para utilizarmos;

Pacotes são um diretório que contém vários módulos Python.

OBS: Nas versões do Python 2, o pacote deve conter __init__.py.
'''

from package import geek1, geek2

from package.package import geek3

print(geek1.pi)

print(geek1.funcao1(1,2))

print(geek2.curso)

print(geek3.funcao3())

# Acessando só uma função

from package.package.geek4 import funcao4

print(funcao4())