def tempo_segundos(hora = 0, minuto = 0, segundo = 0):
    tempo_hora_segundo = hora * 60 * 60
    tempo_minuto_segundo = minuto * 60
    tempo_total = tempo_hora_segundo + tempo_minuto_segundo + segundo
    print(f'{tempo_total} segundos')

tempo_segundos(0,1,30)