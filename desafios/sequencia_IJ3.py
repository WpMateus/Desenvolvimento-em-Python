"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

Exemplo de Saída
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
"""

I = 1
J = 7
while True:

    print(f'I={I} J={J}')
    J -= 1
    print(f'I={I} J={J}')
    J -= 1
    print(f'I={I} J={J}')
    J += 4
    I += 2

    if I > 10:
        break