# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

N = int(input())

#horas
horas = N // (60*60)
N = N%(60*60)

#minutos
minutos = N // 60
N = N % 60

print(f'{horas}:{minutos}:{N}')
