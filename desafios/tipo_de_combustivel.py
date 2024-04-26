'''
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. 
Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). 
Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). 
O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.

Exemplo de Entrada	
8
1
7
2
2
4

Exemplo de Saída
MUITO OBRIGADO
Alcool: 1
Gasolina: 2
Diesel: 0
'''

alcool = 0
gasolina = 0
diesel = 0

while True:
    codigo_valido = int(input())
    if codigo_valido == 1:
        alcool += 1
    elif codigo_valido == 2:
        gasolina += 1
    elif codigo_valido == 3:
        diesel += 1
    elif codigo_valido == 4:
#         print(f"""
# MUITO OBRIGADO
# Alcool: {alcool}
# Gasolina: {gasolina}
# Diesel: {diesel}
#         """)
        print('MUITO OBRIGADO')
        print(f'Alcool: {alcool}')
        print(f'Gasolina: {gasolina}')
        print(f'Diesel: {diesel}')
        break
    else:
        continue
        