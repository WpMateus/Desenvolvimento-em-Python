"""Ler um valor N. 
Calcular e escrever seu respectivo fatorial. 
Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.

Exemplo de Entrada	Exemplo de Saída
4                   24
"""

n = int(input())
fat = 1
i = 2

while i <= n:
    fat = fat * i
    i += 1

print(fat)