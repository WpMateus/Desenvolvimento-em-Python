# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

par = 0
for entrada in range(5):
    valores = int(input())
    calculo = valores % 2

    if calculo == 0:
        par += 1

print(f'{par} valores pares')