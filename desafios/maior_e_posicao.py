"""Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
2                   34565
113                 4
45
34565
6
...
8

"""

armazenar_valores = []

for valores in range(100):
    nrm_informado = int(input())
    armazenar_valores.append(nrm_informado)

maior_valor = max(armazenar_valores)
posicao_maior_valor = armazenar_valores.index(maior_valor) + 1

print(maior_valor)
print(posicao_maior_valor)
