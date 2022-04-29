premio = 1_000_000


q1 = int(input('Quanto o jogador 1 apostou ?'))
q2 = int(input('E o jogador 2 ?'))
q3 = int(input('E o jogador 3 ?'))

total_investido = q1 + q2 + q3

p1 = q1 / total_investido
p2 = q2 / total_investido
p3 = q3 / total_investido

print(f'o jogador 1 contribuiu com {p1 * 100} então receberá uma parcela de {premio * p1} do premio total de {premio} ')
print(f'o jogador 2 contribuiu com {p2 * 100} então receberá uma parcela de {premio * p2} do premio total de {premio} ')
print(f'o jogador 3 contribuiu com {p3 * 100} então receberá uma parcela de {premio * p3} do premio total de {premio} ')