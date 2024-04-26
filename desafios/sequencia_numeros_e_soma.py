"""Leia um conjunto não determinado de pares de valores M e N 
(parar quando algum dos valores for menor ou igual a zero). 
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles 
(incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. 
A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
5 2                 2 3 4 5 Sum=14
6 3                 3 4 5 6 Sum=18
5 0
"""

while True:
    soma = 0
    arm_valores = []
    m, n = map(int, input().split(" "))
    
    if m <= 0 or n <= 0:
        break

    if m > n:
        for sequencia in range(n, m+1):
            soma += sequencia
            arm_valores.append(sequencia)
    elif m < n:
        for sequencia in range(m, n+1):
            soma += sequencia
            arm_valores.append(sequencia)
    
    print(f'{" ".join(map(str, arm_valores))} Sum={soma}')