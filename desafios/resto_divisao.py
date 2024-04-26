'''Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Sample Input
10
18
Sample Output
12
13
17'''

X = int(input())
Y = int(input())

#Converter as entradas caso o o Y seja menor que o X. Para deixar as entradas sempre iguais
if Y < X:
    new = X
    X = Y
    Y = new

for i in range(X+1,Y):
    if i % 5 == 3 or i % 5 == 2:
        print(i)
