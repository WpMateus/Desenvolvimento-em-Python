'''Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste de dois inteiros X e Y. 
Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

Exemplo de Entrada	Exemplo de Saída
7

4 5                 0

13 10               11

6 4                 5

3 3                 0

3 5                 0

3 4                 0

3 8                 12

'''

casos_teste = int(input())

for casos in range(casos_teste):
    x, y = list(map(int, input().split(' ')))
    arm_nmr = 0
    if (x == y):
        print(0)
    else:
        c = 0
        if (x > y):
            c = x
            x = y
            y = c
        while (x < ( y - 1)):
            x += 1
            if(x % 2 != 0):
                arm_nmr += x
        print(arm_nmr)
   