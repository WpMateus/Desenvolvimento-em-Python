# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

pares = 0
impare = 0
positivo = 0
negativo = 0

for entrada in range(5):
    valores = int(input())
    par = valores % 2
    if par == 0:
        pares += 1
    else:
        impare += 1    
    if valores > 0:
        positivo += 1
    elif valores < 0:
        negativo += 1

print(f'{pares} valor(es) par(es)')
print(f'{impare} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
