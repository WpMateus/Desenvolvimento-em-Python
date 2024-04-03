# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split(" "))

#converter para minuto inicial
minuto_inicial += hora_inicial * 60
minuto_final += hora_final * 60

tempo = minuto_final - minuto_inicial

# Se a hora for 0 acrescentar mais 24 no tempo, assim informa que o jogo está acabando no outro dia
if tempo <= 0:
    tempo += 24*60

hora = tempo // 60
minutos = tempo % 60

print(f"O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)")