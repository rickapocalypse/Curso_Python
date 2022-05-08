'''
Levantando os proprios erros com raise

raise -> Lança exceções.

Raise pode ser utilizado para criar propria exceções e mencionar o erro.

raise TipoDoErro('Mensagem de erro')
'''

def colere(texto,cor):
    cores = ['vermelho','azul','amarelo','verde','roxo']
    if type(texto) != str:
        raise TypeError('O texto deve ser uma string')
    if type(cor) != str:
        raise TypeError('A cor deve ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor {cor} não é valida')
    print(f'{texto} {cor}')
colere('oi','vermelho')