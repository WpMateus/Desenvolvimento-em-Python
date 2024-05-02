"""Escreva um programa que leia um valor inteiro N. 
Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
7                   1 2 3 PUM
                    5 6 7 PUM
                    9 10 11 PUM
                    13 14 15 PUM
                    17 18 19 PUM
                    21 22 23 PUM
                    25 26 27 PUM
"""

n = int(input())

n1 = 1
n2 = 2
n3 = 3
for i in range(n):
    print(f"{n1} {n2} {n3} PUM")
    n1 += 4
    n2 += 4
    n3 += 4