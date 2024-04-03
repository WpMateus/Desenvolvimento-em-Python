binario = int(input())

quociente = 1
lista = []

while quociente >= 1:
    resto = binario % 2
    lista.insert(0, resto)
    quociente = binario // 2
    binario = quociente

resultado = ''.join([str(item) for item in lista])
print(resultado)