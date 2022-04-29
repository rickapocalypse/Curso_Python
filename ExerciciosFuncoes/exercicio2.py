def redefinindo_dada(dia,mes,ano):
    nome_mes = 0
    mes = int(mes)
    if mes == 1:
        nome_mes = 'janeiro'
    elif mes == 2:
        nome_mes = 'fevereiro'
    elif mes == 3:
        nome_mes = 'março'
    elif mes == 4:
        nome_mes = 'abril'
    elif mes == 5:
        nome_mes = 'maio'
    elif mes == 6:
        nome_mes = "junho"
    elif mes == 7:
        nome_mes = "julho"
    elif mes == 8:
        nome_mes = "agosto"
    elif mes == 9:
        nome_mes = "setembro"
    elif mes == 10:
        nome_mes = "outubro"
    elif mes == 11:
        nome_mes = "novembro"
    elif mes == 12: 
        nome_mes = "dezembro"

    return print(f'{dia} de {nome_mes} de {ano}')



redefinindo_dada(6, "04", 2022)