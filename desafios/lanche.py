# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

codigo, quant_item = map(int, input().split(' '))
valor = 0.0

if codigo == 1:
    valor = 4.0
elif codigo == 2:
    valor = 4.5
elif codigo == 3:
    valor = 5.0
elif codigo == 4:
    valor = 2.0
elif codigo == 5:
    valor = 1.5

print(f'Total: R$ {quant_item*valor:.2f}')