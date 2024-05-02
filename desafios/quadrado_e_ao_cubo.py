"""Escreva um programa que leia um valor inteiro N (1 < N < 1000). 
Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
5                   1 1 1
                    2 4 8
                    3 9 27
                    4 16 64
                    5 25 125"""

n = int(input())
nmr1 = 1
for i in range(n):
    primeiro_quadrado = nmr1 * nmr1
    segundo_quadrado = nmr1 * primeiro_quadrado
    print(f"{nmr1} {primeiro_quadrado} {segundo_quadrado}")
    nmr1 += 1