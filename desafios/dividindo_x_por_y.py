'''Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

Exemplo de Entrada	Exemplo de Saída
3
3 -2                -1.5
-8 0                divisao impossivel
0 8                 0.0
'''

quantidade_valores = int(input())

for leitura in range(quantidade_valores):
    x, y = map(int, input().split(' '))
    if y == 0:
        print('divisao impossivel')
    else:
       resultado = x / y
       print(f'{resultado:.1f}')