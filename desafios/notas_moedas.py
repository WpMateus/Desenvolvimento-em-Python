# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.

reais, centavos = map(int, input().split('.'))
centavos = centavos + reais*100

print("NOTAS:")
#100
print(f'{centavos // 10000} nota(s) de R$ 100.00')
centavos = centavos%10000

#50
print(f'{centavos // 5000} nota(s) de R$ 50.00')
centavos = centavos%5000

#20
print(f'{centavos // 2000} nota(s) de R$ 20.00')
centavos = centavos%2000

#10
print(f'{centavos // 1000} nota(s) de R$ 10.00')
centavos = centavos%1000

#5
print(f'{centavos // 500} nota(s) de R$ 5.00')
centavos = centavos%500

#2
print(f'{centavos // 200} nota(s) de R$ 2.00')
centavos = centavos%200

print("MOEDAS:")

#1.00
print(f'{centavos // 100} moeda(s) de R$ 1.00')
centavos = centavos%100

#0.50
print(f'{centavos // 50} moeda(s) de R$ 0.50')
centavos = centavos%50

#0.25
print(f'{centavos // 25} moeda(s) de R$ 0.25')
centavos = centavos%25

#0.10
print(f'{centavos // 10} moeda(s) de R$ 0.10')
centavos = centavos%10

#0.05
print(f'{centavos // 5} moeda(s) de R$ 0.05')
centavos = centavos%5

#0.01
print(f'{centavos // 1} moeda(s) de R$ 0.01')
centavos = centavos%1


#--------------------------------------------//--------------------------------------------
#CÓDIGO ABAIXO FUNCIONA PERFEITAMENTE, PORÉM O EXECUTOR DO SITE BEECROWD, MOSTRA ERRO NOS CENTAVOS
 
# valor = float(input())

# valor_notas = [100, 50, 20, 10, 5, 2]
# valor_moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# print("NOTAS:")
# for notas in valor_notas:
#     quantidade = valor // notas
#     print(f'{quantidade:.0f} nota(s) de R$ {notas:.2f}')
#     valor -= quantidade * notas

# print('MOEDAS:')
# for moedas in valor_moedas:
#     quant_moedas = valor // moedas
#     print(f'{quant_moedas:.0f} moeda(s) de R$ {moedas:.2f}')
#     valor -= quant_moedas * moedas


