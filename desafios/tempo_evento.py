"""
Pedrinho está organizando um evento em sua Universidade. 
O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. 
O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. 
Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. 
Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Exemplo de Entrada	Exemplo de Saída
Dia 5               3 dia(s)
08 : 12 : 23        22 hora(s)
Dia 9               1 minuto(s)
06 : 13 : 23        0 segundo(s)
"""

# Aqui pego o dia com o split 1 inicial que vai entrar DIA 7 e pego apenas o valor depois da string
dia1 = int(input().split()[1])
hr1, min1, s1 = map(int, input().split(":"))

# Converto tudo para segundos
tempo_inicial = s1 + min1*60 + hr1*60*60 + dia1*24*60*60


dia2 = int(input().split()[1])
hr2, min2, s2 = map(int, input().split(":"))

# Converto tudo para segundos
tempo_final = s2 + min2*60 + hr2*60*60 + dia2*24*60*60

# Faço a diferença do tempo final pelo inicial
diferenca = tempo_final - tempo_inicial

# Converto tudo novamente para dia, hr, min, seg
d = diferenca // (24*60*60)
diferenca = diferenca % (24*60*60)

h = diferenca // (60*60)
diferenca = diferenca % (60*60)

m = diferenca // (60)
diferenca = diferenca % (60)

s = diferenca

print(f'{d} dia(s)')
print(f'{h} hora(s)')
print(f'{m} minuto(s)')
print(f'{s} segundo(s)')