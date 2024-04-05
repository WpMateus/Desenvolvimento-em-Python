# Faça um programa que mostre os números pares entre 1 e 100, inclusive.

# Entrada
# Neste problema extremamente simples de repetição não há entrada.

# Saída
# Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

for par in range(1,101):
    calculo = par % 2
    if calculo == 0:
        print(par)