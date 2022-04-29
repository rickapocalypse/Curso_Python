vt=int(input('Qual o valor total ?'))


desc = 10/100


com = 5/100


valor_desconto = vt - vt * desc


parcelado = vt / 3


comissao_parcelado = valor_desconto * com


comissao_avista = vt * com


pergunta = input ('Foi pago parcelado ? Digite sim ou nao')


if pergunta == "sim":
    print(f' As parcelas serão {parcelado} e a comissão {comissao_parcelado} ')
else:
    print(f'Então o valor a pagar é {valor_desconto} por conta do desconto de {desc * 100}%. E a comissão é de {comissao_avista}')