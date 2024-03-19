# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

# O símbolo ( representa "maior que". Por exemplo:
# [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

# Entrada
# O arquivo de entrada contém um número com ponto flutuante qualquer.

# Saída
# A saída deve ser uma mensagem conforme exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 25.01                 # Intervalo (25,50]

Valor = float(input())

if Valor >= 0.0 and Valor <= 25.00:
    print(f'Intervalo [0,25]')
elif Valor >= 25.01 and Valor <= 50.00:
    print(f'Intervalo (25,50]')
elif Valor >= 50.01 and Valor <= 75.00:
    print(f'Intervalo (50,75]') 
elif Valor >= 75.01 and Valor <= 100.00:
    print(f'Intervalo (75,100]')  
else:
    print('Fora de intervalo')
    
