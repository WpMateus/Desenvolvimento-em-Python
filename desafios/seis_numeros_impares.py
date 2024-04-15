"""Leia um valor inteiro X. 
Em seguida apresente os 6 valores ímpares consecutivos a partir de X, 
um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

Exemplo de Entrada	Exemplo de Saída
8                   9
                    11
                    13
                    15
                    17
                    19
"""


#Pode ser resolvido com while
valor = int(input())
impar = 0
"""
Menor que 12, 12 por conta que se colocar 6
vai ler apenas 6 numeros e retornar 3 valores impares
e como o impar é de 2 em 2, é necessário colocar o 12
para que lê 6 números impares
"""
while impar < 12:
    impar += 1
    if valor % 2 == 1:
        print(valor)
    # Aqui adiciona +1 no valor de entrada
    valor += 1


#Pode ser resolvido com for
valor = int(input())
"""Mesma coisa que o while
começado do valor informado e somado 
12 números ao valor a frente
"""
for impar in range(valor, (valor + 12)):
    if impar % 2 != 0:
        print(impar)