# Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

# Entrada
# O arquivo de entrada contém 1 valor inteiro qualquer.

# Saída
# Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

valor = int(input())

# Itera do 1 até o valor informado, incluindo o valor final (se ímpar)
for entrada in range(1,valor + 1):
    # Se o número for ímpar ele é impresso
    if entrada % 2 == 1:
        print(entrada)