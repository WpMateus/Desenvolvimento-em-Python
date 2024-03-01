# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# Entrada
# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

codigo_peca1, nro_peca1, valor_peca1 = (input()).split(" ")
codigo_peca2, nro_peca2, valor_peca2 = (input()).split(" ")

soma_pecas1 = int(nro_peca1) * float(valor_peca1)
soma_pecas2 = int(nro_peca2) * float(valor_peca2)

total = float(soma_pecas1) + float(soma_pecas2)

print(f'VALOR A PAGAR: R$ {total:.2f}')