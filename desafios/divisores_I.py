"""Ler um número inteiro N e calcular todos os seus divisores.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Escreva todos os divisores positivos de N, um valor por linha.

Exemplo de Entrada	Exemplo de Saída
6                   1
                    2
                    3
                    6
"""

n = int(input())

for x in range(1, n+1):
    if n % x == 0:
        print(x)