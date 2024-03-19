# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# Entrada
# Leia três valores de ponto flutuante (double) A, B e C.

# Saída
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

# Exemplos de Entrada	Exemplos de Saída
# 10.0 20.1 5.1         # R1 = -0.29788
                        # R2 = -1.71212

# 0.0 20.0 5.0          # Impossivel calcular

A, B, C = map(float, input().split(' '))

delta = B**2 - 4 * A * C

if (A != 0 and delta > -1):
    x1 = (((-1)*B) + (delta ** 0.5)) / (2*A)
    x2 = (((-1)*B) - (delta ** 0.5)) / (2*A)

    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
else:
    print("Impossivel calcular")