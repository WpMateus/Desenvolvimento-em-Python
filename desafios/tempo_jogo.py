# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, 
# sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

# Entrada
# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

# Saída
# Apresente a duração do jogo conforme exemplo abaixo.

hora_inicial, hora_final = map(int, input().split(" "))

# calculo da hora final menos a hora inicial
tempo = hora_final - hora_inicial

# Se a hora for 0 acrescentar mais 24 no tempo, assim informa que o jogo está acabando no outro dia
if tempo <= 0:
    tempo += 24

print(f"O JOGO DUROU {tempo} HORA(S)")
