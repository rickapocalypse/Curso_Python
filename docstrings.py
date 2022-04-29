"""
Documentando funções em Docstrings

OBS: podemos ter acesso á documentação de uma função em python
utilizando a propriedade especial __doc__


Podemos ainda fazer acesso á documentação com a função help()
"""


def diz_oi():
    """Uma função simples que retorna a string 'oi!"""
    return 'Oi!'

help(diz_oi)
